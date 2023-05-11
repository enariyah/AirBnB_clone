## 0x00. AirBnB clone - The console project

The goal of the project is to deploy on your server a simple copy of the AirBnB website.
The first part is **`The console`**

### The console:

 - create your data model
 - manage (create, update, destroy, etc) objects via a console / command interpreter
 - store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### The Command Interpreter
