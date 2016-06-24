#! python3
# maillist and mail merge for CBD + Theos customer lists
# data is from CSV files downloaded from Theos and CBD web
# copy the files into the mailist directory on D:\
# Chad Cropley 2016-06-23 a RAD design solution
#
# import modules
import os
import csv
import shutil

# make sure we're in the right directory
os.chdir('d:\\maillist\\')
# print(os.getcwd())

# read file1
filename = input('Enter a Theos mail list filename: ')

shutil.copyfile(filename, 'MAILLIST-THEOS.csv')
# shutil.copyfile('MAILLIST-06.19.16.csv', 'MAILLIST-THEOS.csv')

with open('MAILLIST-THEOS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    with open('output1.csv','w') as output:
        writer = csv.DictWriter(output, delimiter=',', fieldnames=reader.fieldnames)
        headers = ('Email, Mailing list, Language')
        print(headers, file = output)
#       writer.writeheader('EMail', 'Mailing list', 'Language')
        for row in reader:
            if row['Email'] != '':
                print(row['Email'],',', 'CBD Mailing List',',', 'EN', file = output)

# read file2
filename2 = input('Enter a CBD mail list filename: ')

shutil.copyfile(filename2, 'users_cbd.csv')
# shutil.copyfile('users_general_06162016.csv', 'users_cbd.csv')

with open('users_cbd.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    with open('output1.csv','a') as output:
        writer = csv.DictWriter(output, delimiter=',', fieldnames=reader.fieldnames)
        for row in reader:
            if row['E-mail'] != '':
                print(row['E-mail'],',', 'CBD Mailing List',',', 'EN', file = output)

# os.system('pause')

# Remove duplicate items from merge

inFile = open('output1.csv','r')

outFile = open('output2.csv','w')

listLines = []

for line in inFile:
    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()

print ('open output2.csv to export to CBD CS-Cart subscriber list')
os.system('pause')
