
import requests
from bs4 import BeautifulSoup
import os, csv
from bs4 import SoupStrainer
import re
#this is a list of the languages you would like to list on the page, but in a nice format (i.e. capitalised and everything)
languages = ["English","Afrikaans", "isiNdebele", "isiXhosa", "isiZulu", "Sepedi", "Sesotho (Lesotho)", "Sesotho (South Africa)", "Setswana", "Siswati", "Tshivenda", "Xitsonga"]

#this is a dictionary with the key being the formatted name, exactly the same as in 'langauges'. The value is the exact name of the language, as used in the file structure
k = {"English": "english","Afrikaans":"afrikaans", "isiNdebele":"isindebele", "isiXhosa":"isixhosa", "isiZulu":"isizulu", "Sepedi":"sepedi", "Sesotho (Lesotho)":"sesotho-lesotho", "Sesotho (South Africa)": "sesotho-safrica", "Setswana":"setswana", "Siswati":"siswati", "Tshivenda":"tshivenda", "Xitsonga":"xitsonga"}
category = {'3':'First words', '4':'First sentences', '5':'First paragraphs', '6':'Longer paragraphs', '7':'Read aloud'}

with open("C:/Users/johnl/Dropbox/storybooks_with_html/africanstorybooks.htmlf", "w") as index:  #save it as a file. Using the 'with' ... 'as' means the file is automatically closed.
    #write all the blurb before the list. Specifies the css file (in the same folder as this file), and specifies a 2 coloumn list.
                                                                                                                                                    #change the css file here if necessary. It was "/index-modu.... before I removed the /
    index.write(' <!DOCTYPE html> \n <html> \n<head>\n    <meta charset="utf-8">\n    <title>African Storybooks</title>\n    <link rel="stylesheet" href="index-module-style.css">\n    <base target="_blank" />\n</head>\n<body>\n\n<div id="content">\n<div class="indexmodule">\n  <a href = "mods/africanstorybooks/index.html"> \n <img src="mods/africanstorybooks/af.jpg" alt="African_Storybooks">\n </a>\n   <a href = "mods/africanstorybooks/index.html"> \n <h2>African Storybook Project</h2>\n </a>\n    <p>These stories are in the 11 official languages of South Africa.  These enjoyable stories will assist young children as they learn to read.  Because the stories are in a language familiar to the children, as well as a language they are learning, the children will have fun practicing while they learn to love reading.</p>\n    <ul class="double">\n')

    #create a listing of the categories for each language
    for lang in languages: # we loop through the language list as we know what order it will be in, we don't with the dictionary
        index.write('\n<li class="listhead">'+lang+'</li>\n')
        index.write('<li><a href="mods/africanstorybooks/'+k[lang]+'/'+category['3']+'/" target="content">'+category['3']+'</a>\n')
        index.write('<li><a href="mods/africanstorybooks/'+k[lang]+'/'+category['4']+'/" target="content">'+category['4']+'</a>\n')
        index.write('<li><a href="mods/africanstorybooks/'+k[lang]+'/'+category['5']+'/" target="content">'+category['5']+'</a>\n')
        index.write('<li><a href="mods/africanstorybooks/'+k[lang]+'/'+category['6']+'/" target="content">'+category['6']+'</a>\n')
        index.write('<li><a href="mods/africanstorybooks/'+k[lang]+'/'+category['7']+'/" target="content">'+category['7']+'</a>\n')

    #end off the document
    index.write('    </ul>\n</div>\n</div>\n</body>\n</html>')