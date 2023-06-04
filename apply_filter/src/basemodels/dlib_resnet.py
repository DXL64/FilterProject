import torch.nn as nn
from torchvision import models

class DlibResnet(nn.Module):
    def __init__(self,
                 model_name: str ="resnet18",
                 weights: str ="DEFAULT",
                 output_shape: list =[68, 2]):
        super().__init__()

        self.output_shape = output_shape

        backbone = models.get_model(name=model_name, weights=weights)

        layers = list(backbone.children())[:-1]
        self.feature_extractor = nn.Sequential(*layers)

        for param in self.feature_extractor.parameters():
            param.requires_grad = False

        for param in self.feature_extractor[-2][1].parameters():
            param.requires_grad = True

        num_filters = backbone.fc.in_features

        self.output_layer = nn.Linear(in_features=num_filters,
                                      out_features=output_shape[0]*output_shape[1])
        
    def forward(self, x):
        # ### DETAIL
        # # forward pass the feature_extractor
        # x = self.feature_extractor(x)

        # # (B, 3, 224, 224) -> (B, 3 * 224 *224)
        # batch_size, channels, width, height = x.size()
        # x = x.view(batch_size, -1)

        # # forward pass the output_layer
        # x = self.output_layer(x)

        # # (B, 68*2) -> (B, 68, 2)
        # batch_size, _ = x.size()
        # x.reshape(batch_size, self.output_shape[0], self.output_shape[1])

        # return x

        return self.output_layer(self.feature_extractor(x).view(x.size(0), -1)).reshape(x.size(0), self.output_shape[0], self.output_shape[1])

if __name__ == "__main__":
    from torchinfo import summary
    import torch

    simple_resnet = DlibResnet()

    batch_size = 16
    summary(model=simple_resnet,
            input_size=(batch_size, 3, 224, 224),
            col_names=["input_size", "output_size", "num_params", "trainable"],
            col_width=20,
            row_settings=["var_names"])
    
    random_input = torch.randn([16, 3, 224, 224])
    output = simple_resnet(random_input)
    print(f"\n\nINPUT SHAPE: {random_input.shape}")
    print(f"OUTPUT SHAPE: {output.shape}")