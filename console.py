#!/usr/bin/python3
"""
Console.py is a python command interpreter
"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    Class for the command line interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command exits the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command exits the program
        """
        return True

    def do_emptyline(self):
        """
        Empty line + ENTER should not execute anything
        """
        return False

    def do_create(self, input):
        """
        Creates an instance of a class
        Args:
            input: argument to enter with a command
            ex: 'create User'
        """
        if not input:
            print("** class name missing **")
            return
        cls = next((cls for cls in models.classes
                    if cls.__name__ == input), None)

        if cls is None:
            print("** class doesn't exist **")
            return

        obj_ = cls()
        obj_.save()
        print(obj_.id)

    def do_show(self, input):
        args = input.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        cls = next((cls for cls in models.classes
                    if cls.__name__ == class_name), None)
        if cls is None:
            print("** class doesn't exist")
            return
        key = f"{class_name}.{instance_id}"
        obj = models.storage.all().get(key, None)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_update(self, input):
        args = input.split()
        if len(args) < 4:
            print("** class name missing **" if len(args) == 0 else
                  "** instance id missing **" if len(args) == 1 else
                  "** attribute name missing **" if len(args) == 2 else
                  "** value missing **")
            return
        cls_name, instance_id, attr_name = args[:3]
        attr_value = " ".join(args[3:]).strip('"')
        if attr_name in ["id", "created_at", "updated_at"]:
            return
        cls = next((cls for cls in models.classes
                    if cls.__name__ == cls_name), None)
        if cls is None:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        obj = models.storage.all().get(key, None)
        if obj is None:
            print("** no instance found **")
            return
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()

    def do_all(self, input):
        """
        Print all instances of a class
        Args:
            input: the line to read
        """
        class_name = input.strip()
        objects = models.storage.all()

        if class_name:
            matching_class = next((cls for cls in models.classes
                                   if cls.__name__ == class_name), None)
            if matching_class is None:
                print("** class doesn't exist **")
                return
            filtered_objects = [str(obj) for obj in objects.values()
                                if obj.__class__.__name__ == class_name]
            print(filtered_objects)
        else:
            print([str(obj) for obj in objects.values()])

    def do_destroy(self, input):
        args = input.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        cls_name, instance_id = args[0], args[1]
        cls = next((cls for cls in models.classes
                    if cls.__name__ == cls_name), None)
        if cls is None:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
