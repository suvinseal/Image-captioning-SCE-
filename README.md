# ImageCaptioning 

A thesis inspired by the paper “Deep Visual-Semantic Alignments for Generating Images Descriptions.” by Andrej Karpathy and Li Fei-Fei presents on a model that generates natural language descriptions of images and their regions using Convolutional and Recurrent Neural Networks.

## Introduction

We trained a model using Python that generates a sentence based on the objects it recognizes in an image. We used images from the Microsoft COCO dataset where a pre-trained neural network helped identify objects in the image. The descriptions of these objects were fed into another neural net that arranged these descriptions sequentially to generate a sentence as an output. 

## Overview 

COCO is a large-scale object detection, segmentation and captioning dataset.  COCO stands for Common Objects in Context. The content of the images in dataset consist of everyday scenes. This dataset consists of more than 220,000 labelled images. Each image can have up to five captions. Some applications of this dataset include object segmentation, recognition in context etc. We use this image as a tool that can help a model recognize regions of interest in an image. We also used the Flickr8k dataset to train models and test the images we tested on Microsoft COCO dataset. The Flickr dataset has around five thousand images and each image have a caption.  

### Machine learning

-	Preparing Photo Data: 
We used a pre-trained convolutional neural net (CNN) to recognize objects of interest in the image and extract important features from the images. 

a)	Transfer learning:

	Transfer learning helps with time efficiency while building models. Starting the learning process from scratch can be a very time-consuming process and hence we make use of patterns that have been learned while solving a similar but different problem [3]. 
  
b)	Convolutional Neural Net (CNN): 
The pre-trained model we use is based on a CNN. A typical CNN has two parts
i.	Convolutional base: Stack of convolutional and pooling layers.
ii.	The Classifier: Composed of fully connected layers. 

c)	Repurposing a pre-trained model:

The original classifier is removed from the net which solves the purpose of our goal. If we get poor accuracy, we can fine-tune the model. In this capstone, we train some layers (RNN) and leave others frozen (CNN). 

