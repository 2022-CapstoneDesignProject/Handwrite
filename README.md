# :pencil2: Handwrite font generator
## :high_brightness: Project Background
To simplify the whole font generating process and to reduce the total time to make a font,
we develop this handwrite font generator
so that user can easily access this web service and use freely.

## :books: Main Features & Processes
### 1. Upload and Preview the written template   
First, download the template by clicking the "download template" button on the main homepage.   
Write down all the korean alphabet in the template and save it as png image file.   
Then, upload the written template image on the webpage by clicking "select file" button.   
You can see the uploaded image by clicking the upload button.   
<br>

### 2. Crop uploaded file into each Korean alphabet as a rectangle   
By using cropRect.py code, the korean alphabet images are generated by detecting rectangle.   
<br>

### 3. Remove margin
By using rmMargin.py, the margin of the cropped images are trimmed.   
<br>

### 4. Combine Korean alphabets as Korean letters
Combine korean letters by using jamoComb1.py ~ jamoComb9.py   
The image below shows the combination of korean letters. This is how we make letters using jamo.   
![image](https://user-images.githubusercontent.com/81309465/204545246-3bb97968-789d-4f25-b2da-eedfa60afd00.png)

<br>

### 5. Download the gerated file
In the download.html page, you can download the generated file.   

<br>

## How to implement fontToImage.py 
<pre><code> python fontToImage.py ./font/font_name.ttf fontsize </code></pre>

## :gem: How to implement webpage
Download font folder, web upload & preview folder
  In the terminal, run 
<pre><code> node app.js </code></pre>
  If CSS does not applied to your webpage, 
  change ```html <link rel="stylesheet" href="/public/style.css">``` to ```html <link rel="stylesheet" href="style.css">``` in index.html
    
    
  ![homepage](https://user-images.githubusercontent.com/81309465/172995534-ded909f5-d361-4dcc-84c4-f6a885ba095d.jpg)
  
## How to implement craft
<code><pre>python test.py --test_folder="./test_folder/" </code></pre>
  
  
## Our Prototype

https://user-images.githubusercontent.com/81309465/172995792-57ab9088-97a7-4de2-950d-b3642319a28d.mp4
