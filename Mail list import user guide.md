Import Theos Mail list to website
Description
This procedure is used to update the website mail list for newsletters and e-mail flyers.
Why
In order to ensure that current CBD customers are receiving business correspondence in a timing manner it is important to maintain the mail list on a regular basis. No duplicate email addresses or inactive customers should be in the mail list.
When
This procedure is run quarterly or as requested.
Where
This can be run from the IT Managers work station or by installing the maillistcsv.exe application on any other computer. It may be necessary to change the working directory used by the program if installed and/or run on an alternate computer.
How
1)	Download the Theos mail list (usually Renie will provide this file) to the mail list directory (d:\maillist)
2)	Login into CBD admin area of website
3)	Select Administration -> Export Data -> Subscribers from the top menu
4)	On the export screen change “CSV Delimiter” drop down menu to “Comma”
5)	Select file , local (use default name)
6)	Download the CBD subscriber list to the mail list directory.
7)	Run the maillistcsv.py program. You will be prompted for the names of the Theos & CB files. Enter the full file name including the extension (re:  .csv).
8)	Follow the prompt to open (import) the file to the CBD web site. (Default file name is output2.csv, this is the merged result file).
9)	Login into CBD admin area of website
10)	Select Administration -> Import Data-> Subscribers from the top menu
11)	On the import screen change “CSV delimiter”  to  “Comma”
12)	Select file local and find the output2.csv file in the mail list directory
13)	Select the import button and compare the record count to the number of entries in the output2 file.
