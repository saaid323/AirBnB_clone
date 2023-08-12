DESCRIPTION 

This is our Airbnb clone project. During this initial phase, a fundamental console was developed utilizing the Python cmd module. This console serves to oversee the project's objects, allowing for the implementation of essential methods such as create, show, update, all and destroy across existing classes and subclasses.

File	Description
AUTHORS	Contains info about authors of the project
base_model.py	Defines BaseModel class (parent class), and methods
user.py	Defines subclass User
amenity.py	Defines subclass Amenity
city.py	Defines subclass City
place.py	Defines subclass Place
review.py	Defines subclass Review
state.py	Defines subclass State
file_storage.py	Creates new instance of class, serializes and deserializes data
console.py	creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object
test_base_model.py	unittests for base_model
test_user.py	unittests for user
test_amenity.py	unittests for amenity
test_city.py	unittests for city
test_place.py	unittests for place
test_review.py	unittests for review
test_state.py	unittests for state
test_file_storage.py	unittests for file_storage
test_console.py	unittests for console

Usage
Method	Description
create	Creates object of given class
show	Prints the string representation of an instance based on the class name and id
all	Prints all string representation of all instances based or not on the class name
update	Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
destroy	Deletes an instance based on the class name and id (save the change into the JSON file)
count	Retrieve the number of instances of a class
help	Prints information about specific command
quit/ EOF	Exit the program
