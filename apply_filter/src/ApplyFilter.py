from PIL import Image
from .filter import filter_image, filter_video, filter_functions
from .functions import load_image, load_pil_image
import cv2
from .detectors.dlib_resnet_wrapper import load_model

def apply_filter_on_image(image, filter_name = "squid_game_front_man", output_path = None)->Image:
    image = load_pil_image(image)
    image = filter_image.filter_image(image, filter_name)

    if output_path is None:
        return image
    else:
        image.save(output_path)

def apply_filter_on_video(source, filter_name = "squid_game_front_man", output_path = None)->None:

    cap = cv2.VideoCapture(source)
    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    if source != 0 and output_path != None:
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path / 'annotated_video.mp4', fourcc, fps, frame_size)

    model, simple_transform = load_model()

    if filter_name is None:
        iter_filter_keys = iter(filter_functions.filters_config.keys())
        filter_name = next(iter_filter_keys)

    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == False:
            break
        if source == 0:
            frame = cv2.flip(frame, 1)

        frame = filter_video.filter_frame(frame, filter_name, model, simple_transform)

        if source == 0:

            cv2.imshow("Filter app", frame)

            keypressed = cv2.waitKey(1) & 0xFF
            if keypressed == 27:
                break
            elif keypressed == ord('f'):
                try:
                    filter_name = next(iter_filter_keys)
                except:
                    iter_filter_keys = iter(filter_functions.filters_config.keys())
                    filter_name = next(iter_filter_keys)
        else:
            if output_path != None:
                out.write(frame)  
    
        cap.release()
    if source != 0 and output_path != None:
        out.release()
    cv2.destroyAllWindows()