# ImageSnatcher
Exploiting prnt.sc and its poor image hosting URLs.

# READ THIS
You will need to install the module BeautifulSoup4. You also need **Python 3**.

```
pip3 install -r /path/to/requirements.txt
```


# How it works?
Prnt.sc hosts images under a specific URL, generated from a string of two letters followed by four numbers. For example:
```
https://prnt.sc/de8234
```
If an image does not exist, then it skips it and tries another random string.

# Why create this?
Users that use image hosting sites should be aware that their images are not private and can be potentially viewed by others. Please be aware that you should never upload sensitive information.

# Disclaimer
I am not responsible for anything very strange or incriminating you find.
