# asp-downloader
A python script to download African short stories from africanstorybook.org. Books are downloaded by language, and stored by category.

Specifiy the desired languages, and directory for them to be stored in, at the top of the file. Then run the script, and the books
will be downloaded to the sub-folders in that directory.

Currently, the program downloads the files into a pre-existing folder structure, with the 5 category folders in a folder
with the language's name. The path the folder containing the language folder must be specified at the top of the program.

For example, if you want English and Afrikaans books in the C directory, you must create folders called 'english' and
'afrikaans' (each containing the 5 cateogory folders), and place them in the C directory. Then add "C:\" in the specified
place in the program.

A template file structure for each language, containing the 5 category folders, is provided as a zip file.

---------------------------------------------------------------------------------------------------------------------------------
Dependencies
---------------------------------------------------------------------------------------------------------------------------------
Python 3 must be installed. Get it from https://www.python.org/. I recommend choosing the option to install it for all
users, and select the option to install pip.

Beautiful Soup must be installed. See https://beautiful-soup-4.readthedocs.org/en/latest/#installing-beautiful-soup. 
On windows, the simplest is to open a command window and run "pip install beautifulsoup4". You might need to have installed
Python for all users for this to work.

I used the free community edition of PyCharm to run this program. https://www.jetbrains.com/pycharm/ 
Other IDEs should also work.


