## **Description**

This repository contains a Python POM framework for automated testing of Mobile application. The framework is designed to provide a structured and organized approach to Page object testing, making it easy to write, execute, and manage tests with POM.

## **Features**

## **Table of Contents**
- [Pre-Requitesites](#Pre-Requitesites)
- [Technology](#Technology_used_in_Framework)
- [Installation](#Installation)
- [Execution](#Execution)
- [Framework Structure](#Fmework_Structure)

## Pre-Requisite
### *Required tools for the project*

- Python
- Selenium
- Pytest


## Technology_used_in_Framework
#### AUTOMATION:
- `Python`
- `Selenuim`
- `Pyest`

#### REPORTING TOOL :
- `Allure-Report`


#### FRAMEWORK DESIGN PATTERN :
- `Page Object Model(POM)`

#### OS for Execution on Local:
- `Windows or Mac or Linux`

#### OS for Execution on CI/CD:
- `Windows or Mac or Linux`

**Note:** 
##### Please make sure you have all technologies in your local machine installed or configured.

## Installation
### To Clone this repository to a local directory
Commands to clone and run the test cases<br />
- #### git clone: 
``

This command clone this repository to your local VS code.
- #### Install the dependencies mentioned in prerequisite
    
    Run the following command, and it will install all the packages listed in requirement.txt file
      
        pip install -r requirement.txt


## Execution

#### To run test 
        pytest .\TestCases\test_BH.py 
Or 
        We can use `.\run_test.bat` file for allure report

        

## Github_Workflow_File 
This repository contains a CI/CD pipeline for automated testing of Python APIs using Behave and generating Allure reports. The pipeline is configured to run on every push to the "main" branch, and it performs the following steps:

#### *Set up Python:*
Sets up the Python environment using the actions/setup-python action, specifying the Python version to use as 3.8.9.

#### *Install Dependencies:* 
Upgrades pip and installs the dependencies listed in the requirement.txt file using the pip command.

### **Usage**
#### To use the CI/CD workflow in your own project, follow these steps:

- Create a .github/workflows directory in the root of the GitHub repository, if it doesn't already exist.

- Copy the contents of the api.yml file from this repository into a new file with the same name (api.yml) in the .github/workflows directory of the repository.

- Commit and push the changes to the repository.

- The CI/CD workflow will now be automatically triggered to run on every push or pull request to the master branch of the repository.

