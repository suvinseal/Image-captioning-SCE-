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

### Tools Used

We used Python 3 as our choice of language for this project. We also used popular libraries like Keras with tensorflow as the backend along with pandas, numpy and scikit-learn. First, we tested our code on the Flickr8k dataset which consists of 8092 photographs in jpeg format and descriptions of these images. After testing our code on this dataset, we used the steps on the Microsoft COCO dataset. This dataset consists of over 220,000 images and each image has five captions.

### Data

COCO is a large-scale captioning dataset with several features like object segmentation, recognition in context, over 220k labelled images, 80 object categories, 91 stuff categories, 5 captions per image and 1.5 million object instances. Deep learning models require large datasets to get good accuracy on the predictions. Training our model correctly on over 220k images is expected to give decent predictions. The Flickr8k dataset on the other hand is expected to perform not as well as the COCO dataset due to significantly less data for the model to learn from. 

## Preparing Photo data

We used a pre-trained model to interpret the content of the images. Among many other architectures to choose from, we ended up using the VGG architecture. We used the Keras in-built pre-trained model. This model can also be used as a broader image caption model, however, using this model to run through each photo through the network is not time efficient [2]. Hence, we pre-compute “photo-feature” using the pre-trained model and save it to a file. These features can be loaded later and fed in our model as the interpretation of a given photo in the dataset. This optimization makes training the models much faster and consume less memory. 

