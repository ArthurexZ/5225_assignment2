import json
import numpy as np
import sys
import time
import cv2
import os
import boto3
import base64


# Function for 3.2.2 (Find images based on the tags of an image)


dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
TABLE_NAME = 'ass2-image-tags'
image_bucket = 'image-trigger'
yolo_bucket = 'yolo-configs-test'
confthres = 0.1
nmsthres = 0.1


def get_labels(labels_path):
    # load the COCO class labels 
    response = s3.get_object(
        Bucket=yolo_bucket,
        Key=labels_path
    )
    LABELS = response.get('Body').read().decode('utf8').strip().split("\n")
    print(LABELS)
    return LABELS


def get_weights(weights_path):
    # derive the paths to the YOLO weights and model configuration
    response = s3.get_object(
        Bucket=yolo_bucket,
        Key=weights_path
    )
    WEIGHTS = response.get('Body').read()
    print(WEIGHTS)
    return WEIGHTS


def get_config(config_path):
    response = s3.get_object(
        Bucket=yolo_bucket,
        Key=config_path
    )
    CONFIG = response.get('Body').read()
    print(CONFIG)
    return CONFIG


def load_model(configpath, weightspath):
    # load our YOLO object detector trained on COCO dataset (80 classes)
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configpath, weightspath)
    return net


def do_prediction(image, net, LABELS):
    (H, W) = image.shape[:2]
    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the input image and then perform a forward
    # pass of the YOLO object detector, giving us our bounding boxes and
    # associated probabilities
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    # print(layerOutputs)
    end = time.time()

    # show timing information on YOLO
    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    classIDs = []

    # loop over each of the layer outputs
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            # print(scores)
            classID = np.argmax(scores)
            # print(classID)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > confthres:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])

                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confthres,
                            nmsthres)

    # TODO Prepare the output as required to the assignment specification
    # ensure at least one detection exists
    tags = []
    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            tags.append(LABELS[classIDs[i]])
            print("detected item:{}, accuracy:{}, X:{}, Y:{}, width:{}, height:{}".format(LABELS[classIDs[i]],
                                                                                          confidences[i],
                                                                                          boxes[i][0],
                                                                                          boxes[i][1],
                                                                                          boxes[i][2],
                                                                                          boxes[i][3]))
    return list(set(tags))


## Yolov3-tiny versrion
labelsPath = "coco.names"
cfgpath = "yolov3-tiny.cfg"
wpath = "yolov3-tiny.weights"

Lables = get_labels(labelsPath)
CFG = get_config(cfgpath)
Weights = get_weights(wpath)


def detect_image(image_key):
    image_dict = s3.get_object(
        Bucket=image_bucket,
        Key=image_key
    )
    imagefile = image_dict.get('Body').read()
    nparr = np.fromstring(imagefile, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
    image = img_np.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    nets = load_model(CFG, Weights)
    tags = do_prediction(image, nets, Lables)
    return tags




def handle_postimage(event):
    body = json.loads(event['body'])
    image_key = body.get('s3url')
    tags = detect_image(image_key)
    targetTags =  tags
    search_tags = tags
    response = dynamodb.scan(TableName=TABLE_NAME)
    items = response.get('Items')
    urls = []
    for i in items:
        item_tags = i.get('tags').get('L')
        for d in item_tags or []:
            tag = d.get("S")
            if tag in search_tags:
                url = i.get('s3-url').get('S')
                new_url = 'https://image-trigger.s3.amazonaws.com/' + url
                urls.append(new_url)

    return {"targetTags":targetTags, "urls": urls}


def lambda_handler(event, context):
    # TODO implement
    response_image = handle_postimage(event)
    return {
        'statusCode': 200,
        'body': json.dumps(response_image)
    }
