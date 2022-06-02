# Semantic-Segmentation-For-The-Road

# The Goal
*How to make vechile able to segment all objects of
the scene and classify each pixel to the suitable class*
*****
# Dataset

- *collection of recorded videos of vehicles driven in Germany in
different seasons and different times of the day*
- *it has 2975 training images files and 500 validation image files*
- *The depth of entities in the scene are also included in this dataset* 
*****

# Data Preprocessing 

#### *Each data in the data file is about one combined image, the left half represents the landscape(real image) and the right half represents the ground truth (label) of the landscape*

* *spliting each data file into two parts so the first half has to add to the data
part and the second has to add to the label part*
* *Label Clustering*
> - *because the label image is three channels we have to convert it to one channel
> manner so we can do training as supervised learning because each pixel in the
> landscape image, the corresponding of its in label image will be a number representing
> the number of true class*
> - used **K-means** to solve it
*****

# Dataset Class 
*implemnting a dataset class that will make the operation of storing the data, matched
with deep learning frameworks format*

# Network Architecture
* Fully Convolutional Neural Networks
- The output shape of the network equals the input shape of the
network, we have to use FCNN rather than the normal CNN, because in CNN the
architecture has fully connected layers in the last layersand this idea is not suitable for
this step, where we want the desired output includes **localization**
- The output has c channels, each pixel in this channel represents the probability of
belonging to this class channel



