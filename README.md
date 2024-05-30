# technologies used
  1. Django
  2. sqlite database
  3. python
  4. beautifulsoup
  5. pillow
  6. html
  7. css, bootstrap
  


# CloudSek-Backend-Intern-Post-Comment-Assignment

   preview of the project


   

https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/c1403d9b-36b2-408e-b41f-2823bbd26462


i cant upload more than 10 mb file so this is a short prview of  to do a comment 



# how to run locally 

   1. first of all create a virtual environment (make sure python is installed in your computer and path is added in environmental variables )
           create a virtual environment like this
           command -> python -m venv (name of your virtual environment) , sample is shown below
           <img width="697" alt="image" src="https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/43321f8a-ad2a-4ce8-a695-7010a0df065e">
   2. now activate your virtual environment
         command -> (your virtual environment name)\Scripts\Activate.bat   (for windows)
         command ->  source (your virtual environment name)/bin/activate    (for mac)  , sample is shown below for windows
         <img width="692" alt="image" src="https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/297db68c-98c9-4803-9635-2ba627229557">
   3. now install all dependencies :
        . pip install requests
        . pip install django-allauth
        . pip install django
        . pip install beautifulsoup4
        . pip install pillow
        . python manage.py migrate
  4. now apply migration to the database
       command ->  python manage.py migrate  , sample is shown below
       <img width="692" alt="image" src="https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/9a3e34b3-5223-4937-928b-8f5dea47cadf">

  5. now run the  server using following command
      command -> python manage.py runserver  , sample is shown below
      ![image](https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/2d7f62d0-a593-47a3-aaf1-9fbc8ffd6c3f)
    
   6. now your application will run on this server -> http://127.0.0.1:8000/     



# why i choose Django over other 
  Django has built-in features that make it safer to use the user-submitted data on the application
  and django is having inbuilt sqlite database however we cannot use its inbuilt database for large projects 

  and django also provides us these features 
   1. Battries included
   2. flexible and scalable
   4. easy to use
   5. active community (it addapts python community )


# lets see in action of this project 

  1. this is our home page 
    

![Screenshot 2024-05-12 181405](https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/60731d7c-0098-4371-81bb-2a0a70fb0b36)
    2. this is our sign up page (however we can use bootstrap on it and can make it more beautiful )
    
![Screenshot 2024-05-12 181415](https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/ff8249e3-b20e-4003-9007-cad287e10220)
    3. this our post create tab in this we can create post this post-create tab contains two arguments image and text (image you can select from flickr link is given just above from add url section )
    
 <img width="527" alt="cloudsek img" src="https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/56504ed5-d550-40d9-933f-c7af1c2fbdaf">
 
 4. comment section  - in this multiple users can comment on one post and those users username will show on their comment 
    

![Screenshot 2024-05-12 181456](https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/194dad12-41df-464d-9673-9e90d5377840)
