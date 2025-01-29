# Matching Fingerprint from WSQ (Wavelet Scalar Quantization) format.

## Problem Statement: 

Develop a Python program to match a fingerprint image recorded from paper in WSQ (Wavelet Scalar Quantization) format.

## Submission Guidelines:

Submit your solution in a well-structured format, including code, documentation, and any dependencies required to run the program. Ensure your code is efficient, well-documented, and follows best coding practices.

## Solution
I divided my work in two different solutions. Both solution will work perfectly if all the dependencies are installed correctly. However,For my case I like to solve the problem in google colab environment because of its free, faster as well as pre-installed libraries.

1. One part belongs to local machine where all the python packages and work will be stored in local machine.
- [Local Machine Solution](https://github.com/Maxyee/julhas-data-science-projects/tree/master/AWS)
2. Other part belongs to Google colab environment.
- [Google Colab Solution](https://github.com/Maxyee/julhas-data-science-projects/tree/master/AWS)


## What is WSQ:
The WSQ (Wavelet Scalar Quantization) format is a specialized image compression standard designed for grayscale fingerprint images. It is widely used in biometric and forensic applications due to its high compression efficiency while maintaining the quality necessary for accurate fingerprint analysis. The format is standardized by the FBI for storing and exchanging fingerprint images.

## For Dataset
For this project I used the dataset from kaggle:
The Sokoto Coventry Fingerprint Dataset (SOCOFing) is a biometric fingerprint database for academic research, containing 6,000 images from 600 African subjects. It includes labels for gender, hand, and finger name, along with synthetically altered versions at three levels: obliteration, central rotation, and z-cut. For details and usage policy, see the paper: https://arxiv.org/abs/1807.10609.

- Kaggle
https://www.kaggle.com/datasets/ruizgara/socofing

If we want to work more with other dataset then below link will help us to do that

- Github
https://github.com/robertvazan/fingerprint-datasets/blob/master/README.md


## Why Can't We Match WSQ Directly?
you cannot directly match fingerprints in WSQ format without decoding them because WSQ is a compressed format, not a raw fingerprint feature representation. To perform matching, you need the actual fingerprint image or its minutiae points.

Key Points:

- WSQ is a compressed format (similar to JPEG but optimized for fingerprints). It stores the image in a wavelet-transformed form.
- Matching requires minutiae points (ridge endings, bifurcations, etc.), which are extracted from the decompressed image.
- Algorithms work on pixel data, not on compressed data.