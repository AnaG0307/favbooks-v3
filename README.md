# **FavBOOKS**

![App page screenshot](...)

[View the app in Heroku here](https://favbooks-v3.herokuapp.com/)

## **Table of Contents**

1. [About](#About)
2. [User Stories](#User-Stories)
3. [Features](#Features)
4. [Data Model](#Data-Model)
5. [Testing](#Testing)
6. [Technologies Used](#Technologies-Used)
7. [Deployment](#Deployment)
8. [Credits](#Credits)



## **About**

(Add site description)


## **User Stories**

| User Story ID  | As a/an  | I want to be able to...  | So that I can... |
|---|---|---|---|
| Viewing Products & Navigation |
| 1  | Site User | view a list of products | see what products I can purchase. |
| 2  |  | see the details of a specific product | make a more informed decision before a purchase about the price, rating. |
| 3  |  | see the details of a subscription | make a more informed decision before purchasing a subscription. |
| 4  |  | quickly identify the different sections of the site (book genres,  events, etc.) | navigate through the areas of my interest and discover new ones. |
| 5  |  | easily view what is on my cart | check all I need to purchase is correct. |
| 6  |  | easily view the total amount on my cart | check I am not spending too much. |
| Registration and User Accounts |
| 7  | User/Shopper | register for an account | get a profile for the site and view my profile. |
| 8  |  | login and logout | acces my personal information. |
| 9  |  | recover my password if forgotten | recover access to my account. |
| 10  |  | receive a registration confirmation email | verify my registration to the site was successfull. |
| 11  |  | be able to personalise my user profile | modify my personal information when necessary. |
| 12  |  | be able to access my user profile information | view my profile and what information is stored. |
| Searching and Sort Products |
| 13  | User/Shopper | sort the list of available products | easily identify best rated, best priced and categorycally sorted products. |
| 14  |  | sort a specific category of products | Find the best-priced, best-rated product in a specific category or sort the products in that category by author. |
| 15  |  | sort multiple categories of products at the same time | find the best-priced, best-rated product accross categories, such as "fantasy" or "Teen&Young Age". |
| 16  |  | search a product by name or description | find a specific product I would like to purchase |
| 17  |  | see my search results and how many products are matching | quickly decide wheter the product I want is available. |
| Checkout |
| 18  | Shopper | easily access my purchase history | be aware of my past purchases. |
| 19  |  | easily select the type and quantity of a product when purchasing it | be sure I make no mistakes about the quantity and type of book (paperback/hardcover). |
| 20  |  | be able to register/unregister for a monthly subscription | receive or stop receiving books every month. |
| Admin & Management (CRUD) |
| 21  | Admin User | Add new products (books&subscriptions) | offer new incoming products to my customers. |
| 22  |  | modify product details (books&subscriptions) | update the product details.  |
| 23  |  | delete products (books&subscriptions) | update the site when a product is not for selling anymore. |
| About the Site |
| 24  |  Site User | I am aware of the site Privacy Policy (GDPR compliant) | trust the site. |
| 25  |  | I see pop up messages when I make an action to confirm transactions and changes throughout my activity | rest assured my transactions have been successfull. |
| 26  |  | I can access the site's social media profiles | follow them if I want and stay up to date. |
| Popup Messages |
| 27  | Store owner/Admin | see a pop up message after submitting my purchase  | know if my transaction is been successfull or not.  |
| 28  |  | see a pop up message when adding/deleting products to my bag | be aware if my product was succesfully added or not to my cart. |
| 29  |  | see a pop up message when logging in/out of the site | be aware if I have logged in/out successfully or not. |
| 30  |  | see a pop up message when I subscribe/unsubscribe from a monthly subscription | be aware the action was successfull or not. |


## **Features**

#### **Existing Features**
- **Navigation Bar:** the navigation bar is available through all the pages on the site to ensure the site users can access any page they want at any time. In it the user can find a link to all books, different book actegories, sogn up for the newsletter and the home page. The site user and admin user can also login, logout, resgiter and access their shopping bag.


- **Footer:**  the footer is available through all the pages on the site as well, from there the site users can access the different social media pages, find the physical bookshop address and opening times.


-**Home Page:** the homepage is been kept pretty simple, the site user can see an image of the site as thr main background to create the effect they are already inside the bookshop. At its center there is the "Shop Now" link that takes the site user to see all the books available in the shop.


- **Login/Logout/Register:** situated on the top right corner this feature allows all user to register and create an account to access all the features of the site as well as to log in and out. There are two different levels of user, the admin user and site user. The admin user has extra access that allow them to add, update and remove books from the inline store.

- **Shopping Bag:** the shopping bag is also situated on the top right corner of the site and it is always visible for the user throughout all the pages. With one click they can access their shopping bag to see what is in there, update the quantities of book they wish to purchase or to delete them from the shopping bag.


- **Checkout:** The checkout feature is accessible through the shopping bag, once the site users have made their last decision about what to purchase and they are happy with it. At the checkout the site user can enter and save their personal details and see a summary of what they are about to purchase before entering their card details.


- **Add/Update/Delete Book:** the admin user is able to add, delete and update books into the site without having to enter the default 'admin site' from django. The admin user is the only type of user able to access this feature from two different places: first from 'Book Management' link in the 'My Account' menu from the navigation bar to create a new book, and second from the book details page where they have the option to 'edit' or 'delete' the book selected.


- **Newsletter:** all site users can sign up to receive a newsletter from FavBOOKS. This is accessible from the main navigation bar and if an address is already signed up an informational pop up message will inform the user of it.


- **Admin Site:** 


- **Pop Up Messages:** throughout the site, depending on the actions of the users different pop up messages will appear all along to inform the user of the actions taken. There are different levels of messages: information, success and error. For example, when adding a book to the shopping bag a message will appear informing so, when purchasing a product and everything worked correctly a success message will appear and in case something went wrong an error message will show and explain what went wrong. This ensures the users have extra information and do not unnecessarily repeat processes which might cause major issues (like for example when doing a purchase it would help avoiding an unnecesary double charge).


#### **Future Features**

- **Events:**
- **Reviews:**
- **My Wishlist:**


### **Wireframes**
Below are the initial wireframes for the site for both desktop screens and smaller devices:

**Desktop screens**

![Desktop](...)

**Smaller screens**

![Mobile](...)




## **Data Model**




## **Testing**



#### **Remaining Bugs**



#### **Validator Testing**

- Used [PEP8online.com](http://pep8online.com/) to validate Python code.
- User [W3C](https://validator.w3.org/#validate_by_input) to validate HTML and CSS code


##### **Remaining errors**


## **Technologies Used**

- [Gitpod](https://gitpod.io/)
- [Github](https://github.com/)
- [Unsplash](https://unsplash.com/)
- [Lucidchart](https://www.lucidchart.com/pages/)
- [Fontawesome](https://fontawesome.com/start)
- [Django](https://www.djangoproject.com/)
- [Heroku](https://id.heroku.com/)
- [Balsamiq](https://balsamiq.cloud/)
- [PEP8online.com](http://pep8online.com/)
- [W3C](https://validator.w3.org/#validate_by_input)
- [Stackoverflow](https://stackoverflow.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Coolors](https://coolors.co/)



## **Deployment**



## **Credits**


[Back to Top ⇧](#FavBOOKS) 