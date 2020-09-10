# Digi-Market-Cap

![Project Image](/static/images/multi_device_image.png)

### Table of Contents

- [Description](#description)
- [Deployment](#deployment)
- [Live Site](https://digi-marketcap.herokuapp.com/)
- [How To Use](#how-to-use)
- [Testing](#testing)
- [Author Info](#author-info)


---

## Description
The purpose of this project was to create an app with full CRUD capability. I choose the subject of Crypto currencies as I find the topic and tech very interesting.

This site is intended to allow users to follow the top 200 Crypto's by market cap. In addition users can track their purchases of crypto by creating a position, updating, editing and deleting. The design, layout and typography are designed intuitive functionality and for a clean and easy user expirience. However due to the complex nature of finance, money as well as on-top crypto, I feel that the site could improve on UX. 

Please note for now the only currency available on the site is USD.

The site is far from finished but due to time constraints this is as far as I can take it for now.

- The wireframes for the project can be found [here](static/images/wireframes.pdf)
- The site data schema is available [here](static/images/DataSchema.png)

### UX

* As site owner, the objective is to provide a simple soultion for crypto fans to follow their favorite 'coins'. In doing so create traffic to the site for potentional add or subscription revenue. 
* There is also a possibility to notice trends forming amoung users should there be enough data.

* As a visitor, the objective of the website to provide a simple, visual content with intutive design, of the users holdings of cryptos. The user should be able to browse the current top 200. View lastest info provided by the API and preform full CRUD capabilities on their holdings.


### User stories 

#### New users
- As a user, I want to create my own account, so that I can save, view and edit my crypto 'holdings'.

#### All users
- As a user, I expect to access the website from any device, so that I can use the website anytime and anywhere.
- As a user, I expect to be able to view my cryptp purchases, update, edit and delete as required.
- As a user, I expect  the site to be easy to use and not need to read instructions to use.
- As a user, I want to use the site to see the current value of some of my favorite cryptos easily.
- As a user, I want to be able to check on my crypto value and performance in terms of percentage gains or losses.


### Existing Features
* Full CRUD capability on crypto positions. Allows for additon to an exsisting position.
* The site displays an avrage buy-in cost and amount invested based on users inputs.
* The site dispalys a percentage profit or loss based on the user inputs and current price.
* Current Crypto information form Coinmarketcap.api.com. (updated every 5 mins)
* Global Crypto market cap and Bitcoin Dominance
* Top 200 Crypto by market cap
* Easy to search and sort data in Table, with formatted data (datatables.net cdn)
* Track preformance of holdings/positions
* Pie chart of portfolio balance of holdings

### Future Features

* Additional currency support
* Historical price info to support more charts
* Better UX desgin
* Favorite Tab

### Technologies

- Python
- Flask
- MongoDb
- JavaScript



[Back To The Top](#Digi-Market-Cap)

## Deployment

I Deployed my app on Heroku and you can visit the live site: 

[here]https://digi-marketcap.herokuapp.com/

The repository can be found on:
 
[here](https://github.com/NickBell123/Digi-Market-Cap)


### How I did this

1. Created a Heroku account

2. Created a instance of the application with a unique name  

3. Go to settings and set the VARS for IP, PORT and SECERT KEYS for the API and MONGODB

4. login in to Heroku login via terminal  

5. Used “git init“ to initialise and new repository

6. Used command “pip3 freeze > requirements.txt” 

7. Created a procfile 

8. Ran the command “git remote add” and the app URL which can be found on the Heroku dashboard

9. Commited code 

10. then ran “git push Heroku master”



## How To Use

Step 1: On first visit to site from the home page, click the link to create an account.

![Create Account Image](/static/images/create_account.png)

Step 2: On the Register page fill out the fields. Enter an available username (one which is not already in use) and password and click the submit button.

![Create Account form Image](/static/images/create_account_form.png)

Step 3: On succesful loggin you will be directed to the coin list page. Here you can view stats on the top 200 cryptos by market cap.

![Coin List Image](/static/images/coin_list.png)

#### Create a position

Step 4: To create a position/holding of crypto click the 'Add a Crypto' button in the top right of the navbar. 

![Coin List Image](/static/images/create_position.png)

Step 5: Select the crypto you wish to add to you holdings. Enter the amount you are 'holding' or have.

Step 6: Enter the <strong>price</strong> of the crypto at the <strong>at the time of purchase</strong>. Not the total amount paid for the crypto.
        Example, I buy 0.25 of Bitcoin and the price at purchase was $11500 per Bitcoin, I would enter 0.25 for amount and 11500 for price per unit.

Step 7: Enter the date of purchase (optional).

![Positions Instructions](/static/images/position_instruction_image.png)

Step 8: Click the submit button at the bottom of the form. You then automatically be redirect to the My Crypto page where you can view information
        on your new holding.

![Positions Instructions](/static/images/positions_page_example.png)

#### Editing a position

Step 9: You can amend your holding at any time. If, for instance, you make an error duing input. Simply click the edit button in the corresponding
        row to make changes.
        
![Positions Instructions](/static/images/edit_page_example_image.png)

#### Adding to a position

Step 10: You can also add to an exsisting position by clicking the add button. This feature will add the input amount submitted in the form to 
        the exsisting amount of the crypto selected. An average price is then worked out by the input price and the exsisting price input.
        
 ![Positions Instructions](/static/images/add_to_holding_example_image.png)

#### Deleting a holding

Step 11: You can delete a position or holding buy clicking the delete button in the table row. This will remove the position form the My Crypto page
         and the data base.

## Testing
* Crome dev tools was use throughout the project for checking and handling errors

* All HTML went through W3C HTML validator

* CSS through W3C CSS validator

* Lighthouse (Test showed that there is styling on pages being loaded that is not needed)

* PEP8 for Python

* JSHint was used for checking for errors in my javascript file.


Futher testing can be found in the [testing.md](https://github.com/NickBell123/Digi-Market-Cap/blob/master/TESTING.md)

## Credits

- Materialize and Materialize icons were used thoroughout the project.

- Background image came form a [pngitem.com](https://www.pngitem.com/)

- Crypto information made available via [coinmarketcap-api](https://coinmarketcap.com/api/)

- Table sorting by [datatables cdn](datatables.net)

- Pie chat Js from [Chartist.js](https://gionkunz.github.io/chartist-js/examples.html)

### Resources & Guidence
MongoDb Documentation
Stack Overflow
Slack
YouTube
Code Institue Lessons
Chartist.js documentation


Thanks to the Code Institue Slack team and other students for the help and input. Big thanks to Tony Ngene for continued support and guidence. 



## Author Info

- GitHub - [Nick Bell](https://github.com/NickBell123)
 

[Back To The Top](#Digi-Market-Cap)
