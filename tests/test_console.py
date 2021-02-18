#!/usr/bin/python3

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class testing(unittest.TestCase):
    """ Test the Console """

    def test_prompt(self):
        """ Test prompt """
        with patch('sys.stdout', new=StringIO()) as salida:
            outputexpected = HBNBCommand.prompt
            self.assertEqual(outputexpected, "(hbnb) ")

    def test_quit_message(self):
        """ Test quit message """
        outputexpected = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_EOF_message(self):
        """ Test EOF message """
        outputexpected = "exit the program"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_all(self):
        """ Test help all message """
        outputexpected = "Prints all the str representation of the instances"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(outputexpected, salida.getvalue().strip())
            
    def test_help_count(self):
        """ Test help count message """
        outputexpected = "Prints amount of instances of a class"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_create(self):
        """ Test help create message """
        outputexpected = "Creates instances of class"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_help(self):
        """ Test help help message """
        outputexpected = "List available commands with \"help\" or detailed help with \"help cmd\"."
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_show(self):
        """ Test help show message """
        outputexpected = "Str representation of instances"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_destroy(self):
        """ Test help destroy message """
        outputexpected = "Deletes instances based on ID"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_update(self):
        """ Test help update message """
        outputexpected = "Updates an instance based on the class name and\n        id by adding or updating attribute"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_message(self):
        """ Test only help message """
        outputexpected = "Documented commands (type help <topic>):\n========================================\nEOF  all  count  create  destroy  help  quit  show  update"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_empty_line_and_enter(self):
        """ Test empty line """
        outputexpected = ""
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_sintax_error(self):
        """ Test sintax error """
        outputexpected = "*** Unknown syntax: asdas"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_create_BaseModel(self):
        """ Test create a BaseModel """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertEqual(outputexpected, str(type(salida.getvalue().strip())))

    def test_create_User(self):
        """ Test create a User """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertEqual(outputexpected, str(type(salida.getvalue().strip())))

    def test_create_amenity(self):
        """ Test create a Amenity """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertEqual(outputexpected, str(type(salida.getvalue().strip())))
   
    def test_create_city(self):
        """ Test create a City """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertEqual(outputexpected, str(type(salida.getvalue().strip())))

    def test_create_error(self):
        """ Test create a create class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_create_error_two(self):
        """ Test only create without class """
        outputexpected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(outputexpected, salida.getvalue().strip())