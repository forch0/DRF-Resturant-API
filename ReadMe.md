## Restaurant-Management-API-DRF

Below is a paraphrased version of the provided text:

---

This Management RESTful API serves as the backend for restaurant operations, intended to cater to various client applications. It empowers customers to browse food items, view daily specials, and place orders. Managers utilize the API to update daily specials, monitor orders, and assign deliveries. Delivery crew members access the API to check their assigned orders and update order statuses post-delivery.

The system relies on a database for data storage, primarily SQLite, with the flexibility to switch to MySQL if required. Leveraging a database enables efficient management and access to substantial data sets in an organized manner, facilitating swift data retrieval and seamless updates. SQLite serves as the default choice, ensuring reliability and efficiency, while MySQL offers versatility and compatibility.

Developed with Django REST Framework, this API is fully operational and incorporates user authentication and authorization managed via Djoser. Users authenticate using a username and password to acquire individual tokens for authorization. The API supports three user groups: managers, delivery crew, and customers, although only managers and delivery crew are relevant for this project.

The API provides endpoints for user registration, token generation, and management of menu items, categories, user groups, carts, and orders. These endpoints are tailored to accommodate the API's functionalities and consider various user permissions. Authentication and authorization using individual tokens are mandatory for most endpoints.

Additionally, the API implements features like filtering, pagination, sorting, searching, and throttling to enhance performance and minimize API calls. It delivers appropriate error messages with corresponding HTTP status codes for specific error scenarios such as unauthorized requests or invalid data submissions.

Output data can be rendered in JSON or HTML format. 

To sum up, this RESTful API serves as a comprehensive backend service for restaurant operations, featuring user authentication, menu management, and database storage. It incorporates performance optimization features and ensures robust error handling for enhanced functionality.

**ENDPOINTS**</br>



**WELCOME PAGE**</br>

| Endpoints 	| Group  	| Method 	| DESCRIPTION  	|
|-----------	|--------	|--------	|--------------	|
| */api/*     | Anyone 	| *GET*   | Welcome Page 	|

</br>


**USER REGISTRATION AND TOKEN GENERATION**</br>
Here are djoser endpoints (https://djoser.readthedocs.io/en/latest/getting_started.html), listed only the most important; refer to the docs for more.
For authentication, you have to create a new user with a valid username and password; later, with this user, you can obtain a token, which you have to use in the HEADER of your request to authorise the request you will be making in this API.</br>

| Endpoints      	    | Group                                     	| Method 	| DESCRIPTION                                                         	|
|-------------------    |-------------------------------------------	|--------	|---------------------------------------------------------------------	|
| */auth/users*         | Anyone                                     	| *POST*   	| Creates a new user with the given: 'username', 'email', 'password'' 	|
| */auth/users/me/*     | Anyone with a valid token                 	| *GET*    	| Displays only the current user                                      	|
| */auth/token/login/*	| Anyone with a valid username and password 	| *POST*   	| Generates access tokens that can be used in other API calls    

**CATEGORIES**</br>
Endpoints to manage categories.</br>
Any other endpoints or different combinations of endpoints and methods will result in bad requests or unauthorised HTTP status errors.</br>

| Endpoints                    	| Group                   	| Method     	| DESCRIPTION              	|
|------------------------------	|-------------------------	|------------	|--------------------------	|
| */api/categories*            	| Customer, delivery crew 	| *GET*        	| List all categories.     	|
| */api/categories/{categoryId}*| Customer, delivery crew 	| *GET*        	| Lists single category.   	|
| */api/categories*            	| Manager                 	| *GET*        	| List all categories.     	|
| */api/categories*            	| Manager                 	| *POST*       	| Creates a new category. 	|
| */api/categories/{categoryId}*| Manager                 	| *GET*        	| Lists single category.   	|
| */api/categories/{categoryId}*| Manager                 	| *PUT*, *PATCH*| Updates single category. 	|
| */api/categories/{categoryId}*| Manager                 	| *DELETE*     	| Deletes single category. 	|



**MENU ITEMS**</br>
Endpoints to manage menu items.</br>
Any other endpoints or different combinations of endpoints and methods will result in bad requests or unauthorised HTTP status errors.</br>

| Endpoints                    	| Group                   	| Method     	| DESCRIPTION              	|
|------------------------------	|-------------------------	|------------	|--------------------------	|
| */api/menu-items*            	| Customer, delivery crew 	| *GET*        	| List all menu items.     	|
| */api/menu-items/{menuItemId}*| Customer, delivery crew 	| *GET*        	| Lists single menu item.  	|
| */api/menu-items*            	| Manager                 	| *GET*        	| List all menu items.     	|
| */api/menu-items*            	| Manager                 	| *POST*       	| Creates a new menu item. 	|
| */api/menu-items/{menuItemId}*| Manager                 	| *GET*        	| Lists single menu item.  	|
| */api/menu-items/{menuItemId}*| Manager                 	| *PUT*, *PATCH*| Updates single menu item. |
| */api/menu-items/{menuItemId}*| Manager                 	| *DELETE*     	| Deletes single menu item.	|


**USER GROUP MANAGMENT**</br>
Endpoints to manage the assignment of users to the Manager or Delivery Crew groups.</br>
Any other endpoints or different combinations of endpoints and methods will result in bad requests or unauthorised HTTP status errors.</br>

| Endpoints                                	| Group            	| Method 	| DESCRIPTION                                                	|
|------------------------------------------	|------------------	|--------	|------------------------------------------------------------	|
| */api/groups/manager/users*               | Manager or Admin 	| *GET*    	| List all managers.                                         	|
| */api/groups/manager/users*               | Manager or Admin 	| *POST*   	| Asigns the user in the payload to the manager group.       	|
| */api/groups/manager/users/{userId}*      | Manager or Admin 	| *DELETE* 	| Removes this particular user from the manager group.       	|
| */api/groups/delivery-crew/users*         | Manager or Admin 	| *GET*    	| List all delivery crew.                                    	|
| */api/groups/delivery-crew/users*         | Manager or Admin 	| *POST*   	| Asigns the user in the payload to the delivery crew group. 	|
| */api/groups/delivery-crew/users/{userId}*| Manager or Admin 	| *DELETE* 	| Removes this particular user from the delivery crew group. 	|


**CART MANAGMENT**</br>
Endpoints to manage the assignment of menu items to the cart by a customer.</br>
Any other endpoints or different combinations of endpoints and methods will result in bad requests or unauthorised HTTP status errors.</br>


| Endpoints            	| Group     	| Method 	| DESCRIPTION                                                                        	|
|----------------------	|-----------	|--------	|------------------------------------------------------------------------------------	|
| */api/cart/menu-items*| Customers 	| *GET*    	| Returns current items in the cart from the current user token.                     	|
| */api/cart/menu-items*| Customers 	| *POST*   	| Adds the menu item to the cart. Sets the authenticated user as owner of this cart. 	|
| */api/cart/menu-items*| Customers 	| *DELETE* 	| Deletes all menu items created by the current user token.                          	|


**ORDER MANAGMENT**</br>
Endpoints to manage the orders.</br>
Any other endpoints or different combinations of endpoints and methods will result in bad requests or unauthorised HTTP status errors.</br>
This endpoint: */api/orders* can be used interchangeably with */api/cart/orders* .</br>

| Endpoints             	| Group         	| Method     	| DESCRIPTION                                                                                                                	|
|-----------------------	|---------------	|------------	|----------------------------------------------------------------------------------------------------------------------------	|
| */api/orders*           	| Customers     	| *GET*        	| Returns all orders with order items created by this user.                                                                  	|
| */api/orders*           	| Customers     	| *POST*       	| Creates a new order, transfers all cart items to order items, and deletes the cart for the current user.                   	|
| */api/orders/{orderId}* 	| Customers     	| *GET*        	| Returns the given order with all the order items for the current user.                                                     	|
| */api/orders*           	| Manager       	| *GET*        	| Lists all orders with order items for all users.                                                                           	|
| */api/orders/{orderId}* 	| Manager       	| *PUT*, *PATCH*| Updates the given order. Managers can use this endpoint to asign users to delivery crew and change the status of an order. 	|
| */api/orders*           	| Delivery Crew 	| *GET*        	| List all orders with order items assigned to the authenticated delivery crew user.                                         	|
| */api/orders/{orderId}* 	| Delivery Crew 	| *PATCH*      	| A delivery crew user can update the status of the given order from 0 to 1.                                                 	|
