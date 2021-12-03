#!/usr/bin/env python
#Import the HTML file to parse

def read():

    #fileName = "test.htm"
    fileName = input("Enter HTML file: ")
    from parserHTML import parse

    
    if (fileName == "test.htm"):
        fileName = "core/test.htm"    
    if (":"  not in fileName):
        #Parse HTML for local file
        try:
            with open(fileName, "r") as file:
                HTML=file.read().split("\n")
                parse(HTML, False, fileName)
                

        except AssertionError as msg:
            print(msg)
    else:
        #Parse HTML for websites on the internet
        from requests import get
        HTML = get(fileName, verify=True)
        parse(HTML.text.split(">"), False, fileName)
read()