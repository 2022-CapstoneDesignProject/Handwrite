# :pencil2: Handwrite font generator
## :high_brightness: Project Background
To simplify the whole font generating process and to reduce the total time to make a font,
we develop this handwrite font generator
so that user can easily access this web service and use freely.

## :books: Main Features & Processes
1. Upload and Preview the written template   
2. Crop uploaded file into each Korean alphabets as a rectangle   
3. Remove unnecessary background   
4. Remove margin of the cropped images as mentioned on number 2   
5. Combine Korean alphabets as Korean letters
6. Convert png files into a svg file
7. Convert svg files into a font file
8. Download a font generated   

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
