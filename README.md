# Getting Started with Create React App (IN PROGRESS)

[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)

## Technology and tools used

[![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCKspdO30Fea8ZCxwg-0svOg)
![noce js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)
![react](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![django](https://img.shields.io/badge/Paypal-092E70?style=for-the-badge&logo=paypal&logoColor=white)

# Project setup

## ***Clone this peoject***

## React Project Setup

1. open Command prompt or terminal in frontend folder where ```pacjage.json``` file is located and write command ```npm install``` or ```yarn install```
2. To run the project run command ```npm start``` or ```yarn start```

3. To setup PayPal Payment
    - Create your developer account on <http://developer.paypal.com/>
    - Login on dashboard
    - In Dashboard go in ***SENDBOX SECTION and there you will see option `Accounts`*** and in accouunt you need to create 2 accounts
        - Personal
            - click on *create account* and in that go to *Create custom account*
            - There select your region (According to your coiuntry)
            - Account type should be ***Personal***, Give your email id (FAKE ID ALLOWED FOR DEVELOPMENT AND TESTING)
            - In ***PAYPAL Balance enter your ammount(This will not be real money for developing and testing)***
            - Select payment card should be ***Discover***
            - Cradit Card should be Visa
        - Business
            - click on *create account* and in that go to *Create custom account*
            - There select your region (According to your coiuntry)
            - Account type should be ***Business***, Give your email id (FAKE ID ALLOWED FOR DEVELOPMENT AND TESTING)
            - In ***PAYPAL Balance enter your ammount(This will not be real money for developing and testing)***
            - Select payment card should be ***Discover***
            - Cradit Card should be Visa
    - In Dashboard go in ***My Apps and Credentials and click on create app*** and there type should be **Merchant** and give your business mail id you can select from dropdown (It will show business mail id automatically if you have followed above steps)
    - After Creating app you will see you will see Client Id that you need to copy and paste in `./frontend/src/screens/OrderScreen.js`. Replace that id with `Your PAYPAL CLIENT ID HERE`
    and do not remove "=" sign.

    ![client id of paypal](./readmess/s1.png?raw=true "CLIENT Id SS")

## Django Project setup

1. Install virtualenv by command ```pip install virtualenv```
2. Open terminal where frontend and backend folder located and type command ```virtualenv venv```
3. After creating virtial environment we need to activate it
    - In windows command is ```venv\Script\activate```
    - In linux based operating system and mac command is ```source venv/scripts/activate```
3. Package you need to install
    - ```pip install -r requirement.txt```
4. After installing packages and activating virtual environment cd in backend folder and run command ```python manage.py migrate```
6. And to run the project run command ```python manage.py runserver```
