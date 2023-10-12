This program Extract the text from the image

## Description:

---

This is a simple web pages, that extract a text in image (jpeg/png) file. Its use 'easyocr' a python library.

The extraction may not be 100% accuracy, but sometimes it do the job done.

For more detail of the library, look for yourself.

## <https://github.com/JaidedAI/EasyOCR>

1. Make python venv (virtual environment) name whatever you want

2. git clone this repo

```
git clone <url this repo >

```

3. pip install all the dependency in the requirement.txt

```
pip install -r requirement.txt

```

4. Since we are using flask

```
flask --app < whatever your app is | in my case I use web > run
```

5. flask will output the default url that is { localhost:5000 }

6. Pretty fun

### TODO:

- [x] The Basic fundamental
- [x] Style the Page
- [ ] Improvement

### OUTPUT:

1. Upload any image that contain text
   ![image](./screenshot/s1.png)

2. The extract will be display in this play
   ![image](./screenshot/s2.png)

### OUTPUT: with css

1. Upload any image that contain text
   ![image](./screenshot/s3.png)

2. The extract will be display in this play
   ![image](./screenshot/s4.png)
