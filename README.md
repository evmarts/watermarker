# watermarker

The goal of this project is to automate the process of adding a simple watermark to an image.

## Motivation

The sharing of images on social media platforms has become notorious for the recycling of content amongst their users. If a user has posted an image that has gained popularity, other users will see the success of the image and post it to their own account in hopes of attracting more followers to their account. This is usually done without credit to the original user. 

A common strategy is for the original poster to watermark their userhandle in their image to retain some credit for their content:

<img src="./figs/meme_marked.jpg" width="200px" alt="">


## Getting Started

Clone:
```git clone https://github.com/evmarts/watermarker.git```

Run the script:
```python watermarker.py```

### Prerequisites

- Python

## Built With

* Python Imaging Library (PIL)

* Python textwrap module

## Examples

Suppose we have the following image we would like to watermark with our usersname, *@userhandle*:

<img src="./figs/meme_clean.jpg" width="200px" alt=""> 

After placing the image of the text in the ```in/``` directory, we can run the script:


## Authors

Evan Martin

## Acknowledgments

* Tesseract Open Source OCR Engine
