# Convolutional Neural Networks (CNN)

> Classic hierarchical feature extractors matching early-to-mid visual cortex processing.

---

## Overview

CNNs were the dominant architecture for computer vision from ~2012 to ~2020:

| Model | Year | Key Feature |
|-------|------|------------|
| **AlexNet** | 2012 | First deep CNN; ImageNet breakthrough |
| **VGGNet** | 2014 | Deep, simple stacks of 3×3 convolutions |
| **ResNet** | 2015 | Residual connections; enabled very deep networks |
| **EfficientNet** | 2019 | Neural architecture search; scalable |

---

## Role in Brain Decoding and Encoding

### Hierarchical Correspondence
One of the most significant findings in computational neuroscience (Yamins & DiCarlo, 2016) is the hierarchical alignment between deep CNN layers and the ventral visual stream of primates:
- **Early layers** (e.g., AlexNet `conv1`, `conv2`) capture low-level features such as Gabor-like edges and orientations, correlating highly with primary visual cortex (**V1** and **V2**).
- **Mid layers** (e.g., AlexNet `conv3`, `conv4`, `conv5`) capture texture, shape, and parts of objects, correlating with intermediate visual areas (**V4**).
- **Deep layers** (e.g., AlexNet `fc6`, `fc7`) encode high-level semantic categories, aligning closely with the inferior temporal (**IT**) cortex.

### Voxel Encoding Models
CNNs are frequently used in visual encoding models. A linear mapping (e.g., ridge regression) is fitted between the activation patterns of specific CNN layers and fMRI voxel activities recorded from corresponding visual regions of interest (ROIs).
