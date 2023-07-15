# <center> AirBnB clone - The Console
## <center> Purpose
It is a simple command interpreter to manage the objects used in the AirBnB clone project by:
- Allowing for the creation of new objects.
- Allows retrieval of an object from a file, a database, etc.
- Allows operations to be performed on objects
- Allows object attributes to be updated.
- Allows objects to be destroyed.

The project contains:
- A parent class (called `BaseModel`) used for initialization, serialization, and deserialization of instances.
- Creates a simple flow of serialization/deserialization, as follows: Instance <-> Dictionary <-> JSON string <-> file
- Creation of all subclasses (`User`, `State`, `City`, `Amenity`, `Place`, `Review`)
- Creation of a the first abstracted storage engine of the project: File storage.
- Unittests to validate all classes as well as the storage engine.

## <center>How to Use (with examples)
The user of the console will be able to utilize it in an interactive or non-interactive mode as desired. Running `./console.py` in terminal will open up a prompt that the user can call functions from. For example:

    ./console.py
    (hbtn) help
    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

Commands may be executed non-interactively by piping them into the console. For example:

Both

echo "create BaseModel" | ./console.py

and

    ./console.py
    (hbtn) create BaseModel

will create an instance of the BaseModel class and print its id. 

The `EOF` command is used to terminate the console.  Alternatively, Ctrl+D may be used.

## Contributors
This project exists because of the following contributors:<br />

Ntuthuko Zimu<br />
<a href= "https://github.com/NtuthukoLu"><img src="https://avatars.githubusercontent.com/u/122148642?s=400&v=4">
</a>

Tsuphane Morake<br />
<a href= "https://github.com/Papase14"><img src="https://avatars.githubusercontent.com/u/40323964?v=4">
</a>
