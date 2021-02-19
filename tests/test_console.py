#!/usr/bin/python3

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import re

class testing(unittest.TestCase):
    """ Test the Console """

    def test_prompt(self):
        """ Test prompt """
        with patch('sys.stdout', new=StringIO()) as salida:
            outputexpected = HBNBCommand.prompt
            self.assertEqual(outputexpected, "(hbnb) ")
    
    def setUp(self):
        """Set up tests."""
        storage.reload()

    def test_exit(self):
        """Test to validate quit works."""
        with patch("sys.stdout", new=StringIO()) as o:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_all_count(self):
        """ test count"""

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual("0\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual("0\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual("0\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual("0\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual("0\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual("0\n", salida.getvalue())

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
        out1 = "List available commands with \""
        out2 = "help\" or detailed help with \"help cmd\"."
        outputexpected = out1 + out2
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
        out1 = "Updates an instance based on the class name"
        out2 = " and\n        id by adding or updating attribute"
        outputexpected = out1 + out2
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_message(self):
        """ Test only help message """
        out1 = "Documented commands (type help <topic>):\n="
        out2 = "=======================================\n"
        out3 = "EOF  all  count  create  destroy  help  quit  show  update"
        outputexpected = out1 + out2 + out3
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
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_User(self):
        """ Test create a User """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_amenity(self):
        """ Test create a Amenity """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_city(self):
        """ Test create a City """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

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

    def test_show_error(self):
        """ Test only show error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show asd"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_show_only(self):
        """ Test only show """
        outputexpected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_show_class_only(self):
        """ Test only class show """
        outputexpected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_show_class_id_error(self):
        """ Test id error """
        outputexpected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel asdasd22342"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_only(self):
        """ Test test_destroy_only"""
        outputexpected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_error(self):
        """ Test destroy class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy asd"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_class_only(self):
        """ Test only show """
        outputexpected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_id_error(self):
        """ Test id error """
        outputexpected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel asdasd22342"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_all_class(self):
        """ Test all class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("all asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())
   
    def test_update_class(self):
        """ Test update class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("update asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_eleven(self):
        """ Test task 11 """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("all aasd"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_eleven_two(self):
        outputexpected = "*** Unknown syntax: asd.all()"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("asd.all()"))
            self.assertEqual(outputexpected, salida.getvalue().strip())
    
    def test_quit(self):
        """ checks if quit command is valid"""
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_do_ni_idea(self):
        """all with errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")
    
    def resetStorage(self):
        """ test reset """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_random(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random2(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random3(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random4(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random5(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_02_create_errors(self):
        """Validate create errors."""
        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create")
            self.assertEqual(output, o.getvalue())

        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(output, o.getvalue())

    def test_03_create(self):
        """Validate create functionality"""
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create BaseModel")
            i_d = o.getvalue()
            p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            prog = re.compile(p)
            match = prog.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create User")
            i_d = o.getvalue()
            p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            prog = re.compile(p)
            match = prog.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create State")
            i_d = o.getvalue()
            p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            prog = re.compile(p)
            match = prog.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create City")
            i_d = o.getvalue()
            p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            prog = re.compile(p)
            match = prog.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create Amenity")
            i_d = o.getvalue()
            p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            prog = re.compile(p)
            match = prog.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create Place")
            i_d = o.getvalue()
            p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            prog = re.compile(p)
            match = prog.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("create Review")
            i_d = o.getvalue()
            p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            prog = re.compile(p)
            match = prog.match(i_d)
            self.assertTrue(match is not None)
    
    def test_update_function(self):
        """Validating dictionary update."""
        b = BaseModel()
        b_id = b.id
        u = User()
        u_id = u.id
        s = State()
        s_id = s.id
        c = City()
        c_id = c.id
        a = Amenity()
        a_id = a.id
        p = Place()
        p_id = p.id
        r = Review()
        r_id = r.id
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('BaseModel.update("' + b_id +
                                 '", {\'fn\': "John", "age": 89, "w": 12.3})')
            self.assertTrue(hasattr(b, 'fn'))
            self.assertTrue(hasattr(b, 'age'))
            self.assertTrue(hasattr(b, 'w'))
            HBNBCommand().onecmd("BaseModel.show(" + b_id + ")")
            self.assertIn('John', o.getvalue())
            self.assertIn('89', o.getvalue())
            self.assertIn('12.3', o.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('User.update("' + u_id +
                                 '", {\'fn\': "John", "age": 89, "w": 12.3})')
            self.assertTrue(hasattr(b, 'fn'))
            self.assertTrue(hasattr(b, 'w'))
            HBNBCommand().onecmd("User.show(" + u_id + ")")
            self.assertIn('John', o.getvalue())
            self.assertIn('89', o.getvalue())
            self.assertIn('12.3', o.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('State.update("' + s_id +
                                 '", {\'fn\': "John", "age": 89, "w": 12.3})')
            self.assertTrue(hasattr(b, 'fn'))
            self.assertTrue(hasattr(b, 'age'))
            self.assertTrue(hasattr(b, 'w'))
            HBNBCommand().onecmd("State.show(" + s_id + ")")
            self.assertIn('John', o.getvalue())
            self.assertIn('89', o.getvalue())
            self.assertIn('12.3', o.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('City.update("' + c_id +
                                 '", {\'fn\': "John", "age": 89, "w": 12.3})')
            self.assertTrue(hasattr(b, 'fn'))
            self.assertTrue(hasattr(b, 'w'))
            HBNBCommand().onecmd("City.show(" + c_id + ")")
            self.assertIn('John', o.getvalue())
            self.assertIn('89', o.getvalue())
            self.assertIn('12.3', o.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('Amenity.update("' + a_id +
                                 '", {\'fn\': "John", "age": 89, "w": 12.3})')
            self.assertTrue(hasattr(b, 'fn'))
            self.assertTrue(hasattr(b, 'w'))
            HBNBCommand().onecmd("Amenity.show(" + a_id + ")")
            self.assertIn('John', o.getvalue())
            self.assertIn('89', o.getvalue())
            self.assertIn('12.3', o.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('Place.update("' + p_id +
                                 '", {\'fn\': "John", "age": 89, "w": 12.3})')
            self.assertTrue(hasattr(b, 'fn'))
            self.assertTrue(hasattr(b, 'w'))
            HBNBCommand().onecmd("Place.show(" + p_id + ")")
            self.assertIn('John', o.getvalue())
            self.assertIn('89', o.getvalue())
            self.assertIn('12.3', o.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('Review.update("' + r_id +
                                 '", {\'fn\': "John", "age": 89, "w": 12.3})')
            self.assertTrue(hasattr(b, 'fn'))
            self.assertTrue(hasattr(b, 'w'))
            HBNBCommand().onecmd("Review.show(" + r_id + ")")
            self.assertIn('John', o.getvalue())
            self.assertIn('89', o.getvalue())
            self.assertIn('12.3', o.getvalue())
