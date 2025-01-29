# Local Machine Solution

## Note: 
for linux or mac user use `pip3` or `python3`
windows user use `pip` or `python`

## Installation Guide

### Step 1

Go to project directory

```bash
cd ./local_machine_solution/
```

### Step 2

create a virtualenv

```bash
python3 -m venv myenv
```

if you dont have virtual environment installed

```bash
pip3 install virtualenv
```

### Step 3
run the directory by using command

```bash
source ./myenv/Scripts/activate
```

for linux or mac users

```bash
source ./myenv/bin/activate
```
### Step 4

we have to install the pip packages called WSQ

`pip3 install -U wsq`

### Step 5
run all the necessary library from the `requirements.txt`

command `pip install -r requirements.txt`

### Step 6

Finally run the code

`python3 fingerprint_matcher_wsq.py`



## About Dataset
Here we used the kaggle dataset. dataset Link: https://www.kaggle.com/datasets/ruizgara/socofing

We took total Real 50 data for 10 fingers eachtime. So whole total 500 data is going to used to test the finger match.

Another extra 1 data we also included into our `dataset/Real` folder which is the result fingerprint for our testing. the name of the file is `output_image_Real.BMP` 

This data is converted from WSQ format. However, why we converted this data is briefly described into the previous readme file.
