t text](https://raw.github.com/facu2279/AirBnB_clone/main/airbnbimage.png)
# Airbnb Clone Proyect

General
-------------
As a first step we were asked to write a command interpreter to manage our AirBnB objects.
This is the first step towards building our first complete web application: the AirBnB clone. This first step was very important because you will use what we created during this project with all the other projects below: HTML / CSS templates, database storage, API, front-end integration ...

The tasks we carried out were:

- Create a main class (called BaseModel) that takes care of the initialization, serialization, and deserialization of new instances.
- We create a simple serialization / deserialization flow: Instance <-> Dictionary <-> JSON String <-> file
- We create all the classes used for AirBnB (user, state, city, place ...) that all inherit from BaseModel
- We create a storage engine to be able to save data.
- We create all the unit tests to validate all our classes and storage engine.

What’s a command interpreter?
------------------
The command interpreter is the program that receives what is written in the terminal and converts it into instructions for the operating system. In this case, we create our own command interpreter for the functions that we need for the correct functioning of our Airbnb clone.

How to use the interpreter?
-----------------------

Usage in interactive mode: 
```
$ ./console.py
```
This: displays a message:
```
(hbnb)
```
and waits for the user to type a command. A command line always ends with a new line. The prompt is displayed again each time a command is executed.

and in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
Here is a simple example of how to use our console
```
(hbnb) create BaseModel
de2630a8-7556-4e6d-8b55-8b0a4ba8082d
(hbnb) show BaseModel de2630a8-7556-4e6d-8b55-8b0a4ba8082d
[BaseModel] (de2630a8-7556-4e6d-8b55-8b0a4ba8082d) {'updated_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 756946), 'created_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 756836), 'id': 'de2630a8-7556-4e6d-8b55-8b0a4ba8082d'}
(hbnb) quit
```

# Files and folders
- models
    - engine
        - __init__.py
        - file_storage.py
    - __init__.py
    - amenity.py
    - base_model.py
    - city.py
    - place.py
    - review.py
    - state.py
    - user.py
    - tests
        - __init__.py
        - test_models
            - __init__.py
            - test_amenity.py
            - test_base_model.py
            - test_city.py
            - test_file_storage.py
            - test_place.py
            - test_review.py
            - test_state.py
            - test_user.py
- console.py
- README.md
- AUTHORS
- airbnbimage.png

# Authors
Made by [Facundo Diaz](https://github.com/facu2279)
and [Tomas De Castro](https://github.com/tomi1710)
to Holberton School 2021

Social Networks Facundo
-------------------
- [Linkedin](https://www.linkedin.com/in/facundo-d%C3%ADaz-720110149/)
- [Twitter](https://twitter.com/facudiazuy)

Social Networks Tomas
-------------------
- [Linkedin](https://www.linkedin.com)
- [Twitter](https://twitter.com/Tomasdecastro6)