# ImageCaptioning 

A thesis inspired by the paper “Deep Visual-Semantic Alignments for Generating Images Descriptions.” by Andrej Karpathy and Li Fei-Fei presents on a model that generates natural language descriptions of images and their regions using Convolutional and Recurrent Neural Networks.

## Introduction

We trained a model using Python that generates a sentence based on the objects it recognizes in an image. We used images from the Microsoft COCO dataset where a pre-trained neural network helped identify objects in the image. The descriptions of these objects were fed into another neural net that arranged these descriptions sequentially to generate a sentence as an output. 

## Overview 

COCO is a large-scale object detection, segmentation and captioning dataset.  COCO stands for Common Objects in Context. The content of the images in dataset consist of everyday scenes. This dataset consists of more than 220,000 labelled images. Each image can have up to five captions. Some applications of this dataset include object segmentation, recognition in context etc. We use this image as a tool that can help a model recognize regions of interest in an image. We also used the Flickr8k dataset to train models and test the images we tested on Microsoft COCO dataset. The Flickr dataset has around five thousand images and each image have a caption.  
