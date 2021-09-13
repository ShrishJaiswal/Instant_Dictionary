# Instant English Dictionary Application

This project is purely based on python and has feature of generating definitions of the word input by the user.

## Description:- A web application that lets user input a word in the text area and returns the meaning or definition of the words.

The application has simple user web-interface and has 3 pages:
1) About
2) Home
3) Dictionary

The framework used here is "Justpy". Justpy is a web-framework for python for development of Front-end of an application.
It has easy methods and libraries which makes the tast of developing front-end for an application easy.

### Dataset- dictionar.csv is the dataset used for this application.
The dataset contains words and respective definition in the form of dictionaries: {"words":"definition"} as key-value pair. The data extraction is done using pandas library.
The defintion.py is the source of the application as it deals with the extraction of words from dataset and displaying their meanings.

The other files include:
1) Home.py- A python file for development of home page for our application.
2) dictionary.py- A file which uses web-interfaces for displaying search result.
3) about.py- A python file containing description of the website and owner.

All the above mentioned files are used for web-development using justpy framework.

The project also contains design.txt file for brief understanding about this project.

## Main-Feature: The main feature of this project is the modification of traditional dictionary applications.
In this project, there is no usage of the "get-result/Enter" button for generating result. Instead it generates or predicts the result as user types the word.
This removes the hassle of clicking "enter" button everytime. 

The scope of this project is vast and can be incorporated in various other projects as needed.

# Note:- 
This project also has a rest-api for ease of access. The api is currently hosted locally using justpy framework. The api details can be found here: https://github.com/ShrishJaiswal/Instant_DictionaryApp_api
