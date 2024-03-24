#!/usr/bin/python3
"""
Console.py is a python command interpreter
"""

import cmd
import models
import re


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

    def emptyline(self):
        """
        Empty line + ENTER should not execute anything
        """
        pass

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

    def count_instances(self, class_name):
        """
        Counts instances of a specific class.
        """
        count = 0
        for instance in models.storage.all().values():
            if instance.__class__.__name__ == class_name:
                count += 1
        print(count)

    def default(self, line):
        """
        Catch-all for commands that do not match do_* commands.
        """
        # Match pattern <class name>.all()
        all_match = re.match(r'^(\w+)\.all\(\)$', line)
        count_match = re.match(r'^(\w+)\.count\(\)$', line)
        show_match = re.match(r'^(\w+)\.show\("(.+)"\)$', line)
        destroy_match = re.match(r'^(\w+)\.destroy\("(.+)"\)$', line)
        if all_match:
            class_name = all_match.group(1)
            self.do_all(class_name)
        elif count_match:
            class_name = count_match.group(1)
            self.count_instances(class_name)
        elif show_match:
            class_name, instance_id = show_match.groups()
            self.do_show(f'{class_name} {instance_id}')
        elif destroy_match:
            class_name, instance_id = destroy_match.groups()
            self.do_destroy(f'{class_name} {instance_id}')
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
