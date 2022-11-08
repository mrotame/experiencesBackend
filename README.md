# Django backend-project

### Description
This is a simple Django backend-only Rest API project that will be serving to manage my experiences and my portfolio. This project is not finished and will be receiving a lot of upgrades that will probably change the entire architecture over time

### Already Implemented

 - **Custom user model and custom user management:** *I overwrote the default user model due to the necessity to remove some unused, add and replace other fields over the model*
 
 - **Custom JWT Authentication and Authorization systems:** *I overwrote the Django's default Authentication and Authorization for a database-less  auth-token system using JWT*
 - **Rest Framework:** *Implemented Rest Framework over the project to develop in an agile way default generic CRUD APIs with less coding and getting better time management across the project by using Generic API and Mixins classes*
 - **Database Model Serializers:** *Implemented Rest Framework serializers (Similar to Django Forms) to the generic APIs to reduce time on converting models to JSON (to the response) besides saving time implementing request basic validators and basic data testing*
 - **Django database Migrations:** *Implemented the default Django Database Migrations to manage database versioning*
 - **Unitest Test Cases:** *Implemented test cases to ensure the project stability and security by reducing manuability errors across implementations of the project*
