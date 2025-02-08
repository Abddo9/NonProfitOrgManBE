import numpy as np
from vision_agent.tools import *
from typing import *
from .models import Product

def detect_and_count_objects(image :np.ndarray, classes = None, is_debug=None) -> dict:
    """
    Detects specified industrial objects in an image, counts them, overlays bounding boxes,
    and saves the resulting image.

    Parameters:
    -----------
    img : np.ndarray
        The path or URL to the image.
    classes : str
    comma seperated list of classes to detect

    Returns:
    --------
    dict
        A dictionary containing the counts for each detected object label.
    """

    if not classes and is_debug:
        classes = "pipe, duct, mechanical equipment, valve, pump"
    elif not classes:
        classes = ",".join([p.name for p in Product.objects.all()])
    
    # 2. Detect objects using the owlv2_object_detection tool
    detections = owlv2_object_detection(
        prompt=classes,
        image=image,
        box_threshold=0.1
    )

    # 3. Count the objects by label
    object_counts = {}
    for det in detections:
        label = det["label"]
        object_counts[label] = object_counts.get(label, 0) + 1

    # 4. Overlay bounding boxes on the image
    image_with_boxes = overlay_bounding_boxes(image, detections)
    save_image(image_with_boxes, "detected_objects.jpg")

    return object_counts