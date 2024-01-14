# 0x00. AirBnB Clone - The Console

## Description

This project is an implementation of a console for an AirBnB clone. The console provides a command-line interface (CLI) for managing AirBnB objects, such as users, places, reviews, etc.

## Features

- Create, Read, Update, and Delete (CRUD) operations on AirBnB objects.
- Interactive and non-interactive modes.
- Supports various classes including BaseModel, User, State, City, Amenity, Place, and Review.
- JSON serialization and deserialization for persistent storage.
- Command-line commands to manage AirBnB objects.

## Usage

### Interactive Mode

Run the console in interactive mode by executing:

```bash
./console.py

(hbnb) create User
5bc3c3b1-65aa-4266-ae59-e7012e7a0744

(hbnb) show User 5bc3c3b1-65aa-4266-ae59-e7012e7a0744
[User] (5bc3c3b1-65aa-4266-ae59-e7012e7a0744) {'id': '5bc3c3b1-65aa-4266-ae59-e7012e7a0744', 'created_at': datetime.datetime(2024, 1, 12, 19, 21, 8, 960829), 'updated_at': datetime.datetime(2024, 1, 12, 19, 21, 8, 960809)}

(hbnb) quit
```

### Non-Interactive Mode
echo "your_command_here" | ./console.py


## Commands

Here are some example commands you can use in the console:

- create: Creates a new instance of a specified class.
- show: Prints the string representation of an instance based on the class name and id.
- destroy: Deletes an instance based on the class name and id.
- all: Prints all string representations of instances based on the class name.
- update: Updates an instance based on the class name and id.

## Authors
- [Geraldine Nwaribe]
- [Collaborator Shekwogaza Solomon]



Feel free to customize the README to include specific details about your project and team.
