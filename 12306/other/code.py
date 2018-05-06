# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12306-code
   Description :
   Author :       XWH
   date：          2018/2/1
-------------------------------------------------
   Change Activity:
                   2018/2/1:
-------------------------------------------------
"""
# python v2.7
__author__ = 'XWH'

from PIL import Image
from PIL import ImageFilter
import urllib
import urllib2
import requests
import re
import json
from cons import *

# hack CERTIFICATE_VERIFY_FAILED
# https://github.com/mtschirs/quizduellapi/issues/2
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def get_img():
    return Image.open(name_verification_code)

def get_sub_img(im, x, y):
    assert 0 <= x <= 3
    assert 0 <= y <= 2
    IMAGEWH = 67
    left = 5 + (IMAGEWH + 5) * x
    top = 41 + (IMAGEWH + 5) * y
    right = left + IMAGEWH
    bottom = top + IMAGEWH

    return im.crop((left, top, right, bottom))


def baidu_image_upload(im,index):

    imagepath = './images/query_temp_img_{0}.png'.format(index)
    im.save(imagepath)
    raw = open(imagepath, 'rb').read()

    files = {
        'fileheight'   : "0",
        'newfilesize'  : str(len(raw)),
        'compresstime' : "0",
        'Filename'     : "image.png",
        'filewidth'    : "0",
        'filesize'     : str(len(raw)),
        'filetype'     : 'image/png',
        'Upload'       : "Submit Query",
        'filedata'     : ("image.png", raw)
    }

    resp = requests.post(url_upload_baidu, files=files, headers=headers)

    #  resp.url
    redirect_url = url_image_baidu + resp.text
    print redirect_url
    return redirect_url



def baidu_stu_lookup(im,index):
    redirect_url = baidu_image_upload(im,index)

    resp = requests.get(redirect_url)

    html = resp.text

    return baidu_stu_html_extract(html)


def baidu_stu_html_extract(html):
    pattern = re.compile(r"'multitags':\s*'(.*?)'")
    matches = pattern.findall(html)
    if not matches:
        return '[ERROR?]'

    tags_str = matches[0]

    result =  list(filter(None, tags_str.replace('\t', ' ').split()))

    return '|'.join(result) if result else '[UNKOWN]'


def ocr_question_extract(imageTitle):
    # git@github.com:madmaze/pytesseract.git
    global pytesseract
    try:
        import pytesseract
    except:
        print ("[ERROR] pytesseract not installed")
        return

    imageResult = imageTitle.crop((120,0,290,25))
    # imageResult.show()
    # imageResult = pre_ocr_processing(imageResult)
    imageResult.show()
    return pytesseract.image_to_string(imageResult, lang='chi_sim').strip()


def pre_ocr_processing(im):
    im = im.convert("RGB")
    width, height = im.size

    white = im.filter(ImageFilter.BLUR).filter(ImageFilter.MaxFilter(23))
    grey = im.convert('L')
    impix = im.load()
    whitepix = white.load()
    greypix = grey.load()

    for y in range(height):
        for x in range(width):
            greypix[x,y] = min(255, max(255 + impix[x,y][0] - whitepix[x,y][0],
                                        255 + impix[x,y][1] - whitepix[x,y][1],
                                        255 + impix[x,y][2] - whitepix[x,y][2]))

    new_im = grey.copy()
    binarize(new_im, 150)
    return new_im


def binarize(im, thresh=120):
    assert 0 < thresh < 255
    assert im.mode == 'L'
    w, h = im.size
    for y in xrange(0, h):
        for x in xrange(0, w):
            if im.getpixel((x,y)) < thresh:
                im.putpixel((x,y), 0)
            else:
                im.putpixel((x,y), 255)

if __name__ == '__main__':
    image = get_img()
    # im = Image.open("./tmp.jpg")
    # im.show()
    try:
        print ('OCR Question:', ocr_question_extract(image))
    except Exception as e:
        print ('<OCR failed>', e)
    for y in range(2):
        for x in range(4):
            imageSub = get_sub_img(image, x, y)
            result = baidu_stu_lookup(imageSub,"{0}{1}".format(x,y))
            print ((y,x), result)