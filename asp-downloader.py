#This program was written by John Lewis,


import requests
from bs4 import BeautifulSoup
import os, csv
from bs4 import SoupStrainer
import re


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#USER MODIFICATION REQUIRED BELOW
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is a list of all the desired languages. The name of language is taken from http://my.africanstorybook.org/stories-by-language. Spaves are replaced with a dash (-), and
#the names are all lower case (although it appears to be case-insensitive). You can see the exact term that must go in this list by opening a link to a language in a new tab
#and looking at the URL.


#EXAMPLE LANGUAGES
#languages = ["english","afrikaans", "isindebele", "isixhosa", "isizulu", "sepedi", "sesotho-lesotho", "sesotho-safrica", "setswana", "tshivenda"]#"english"

languages = ["lang1", "lang2", "lang3"]

#You must specify where the folder containing the language folders is.

#EXAMPLE DIRECTORY
#directory = "C:/Users/johnl/Dropbox/storybooks/"

directory = "YOUR DIRECTORY HERE"

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This is the list of category codes with corresponding category names.
#A453 = First words
#A454 = First sentences
#A455 = First paragraphs
#A456 = Longer paragraphs
#A457 = Read aloud

# 'category' is a dictionary link the last digit of the code (the key) with the category name (the value)
category = {'3':'First words', '4':'First sentences', '5':'First paragraphs', '6':'Longer paragraphs', '7':'Read aloud'}

#This tells sets up a filter to tell Beautiful soup to only parse items of class "sysbook" (the class containing all the book info on the page
only_books = SoupStrainer("div", {"class": "sysbook"})
cont = True          #continue variable, intialised to true to start the while loop below. Set to false when there are no more pages
page = 0             #initialised to zero, used to loop through the pages for a category
no_book = 0          #counter to track the number of books in a category. Printed out for diagnostics



#loop through all languages, assigning the current one to 'lang'
for lang in languages:
    print(lang)
    #loop through all categories, assigning the key and value to k and v, respectively
    for k,v in category.items():
        while cont:

            #generate the url based on the current language, the current page, and current category. This format was derived from the africanstory book project
            #website. You need to open category links in new pages to see this full URL and figure out the structure, if you want to change it. This also only selects
            #ASP approved books, see the next link if you want to change that
            url = "http://my.africanstorybook.org/language/"+lang+"?page="+str(page)+"&f[0]=bm_field_asp_approved%3Atrue&f[1]=im_field_reading_level%3A45"+k

            #This link does not have the filter for ASP approved books, so it should download all the books for a category+language
            # url = "http://my.africanstorybook.org/language/"+lang+"?page="+str(page)+"&f[0]=im_field_reading_level%3A45"+k


            print(url) #print current generated url for debugging purposes
            page += 1  #track number of pages

            r = requests.get(url)
            data = r.text
            # print(BeautifulSoup(data, "html.parser", parse_only=only_books).prettify())  #prints out the retrieved page, for debugging
            soup = BeautifulSoup(data, "html.parser", parse_only=only_books)   #creat a BS4 object called soup by calling BeautifulSoup with the page and filter as parameters

            books = soup.find_all("div", {"class": "sysbook"})  #this finds all the 'sysbook' items, and stores them in the 'books' variable
            if books:                                           #testing to see if any books were found. If none were found, this will evaulate to false, as 'books' will be empty

                for book in books:                              #loop through all the books, assigning the current one to 'book'
                    no_book += 1
                    title = book.find("div", {"class": "title"}).a.get_text()       #find the title of the book
                    link = book.find("a", {"class": "print_link"}).get('href')      #find the link of the book. It starts /asp/downloads... or something similiar

                    link = "http://my.africanstorybook.org" + link                  #attach the prefix so it's a valid link

                    name = re.sub(r'[?|:|/|\|<|>|"|*|||\x0b|]',r'',title)           #remove any special characters that are not allowed in Windows file names. The '\x0b' is a
                                                                                    #new line character part of a book's name (found when the program threw an error)
                    name = directory+lang+"/"+v+"/"+name + ".pdf"    #generate the full file path, with extension. A relative file path can also be used, but
                                                                                                #it's important that the folder already exists.

                    r = requests.get(link)          #download the pdf
                    with open(name, "wb") as code:  #save it as a file. Using the 'with' ... 'as' means the file is automatically closed.
                        code.write(r.content)


            else:  #if no more books are found (i.e. when we've gone past the final page), stop looking in this category
                print("no more books")
                cont = False


            print(v)
            print(no_book)
            print(page)     #prints the category, page and number of books for tracking purposes
        cont = True         #reset the variables as we're now going to move to a new category
        page = 0
        no_book = 0