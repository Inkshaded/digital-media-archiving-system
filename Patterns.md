# Design Patterns
## SOLID Design Principles
### Single Responsibility Principle
Below, all functional program files will be summarised simply to demonstrate adherence to the Single Responsibility Principle
```
Program Files

implementations/ # holds concrete behaviors
    csv_record_store : Implementation of RecordStorage that creates/appends to
    a 'records' file to keep track of when and what has been archived
    local_storage.py : Implementation of Storage that archives files locally
    tkinter_file_selector.py : Implementation of FileSelector that opens a
    tkinter dialog box to select a file

ui/
    ui_start.py : Handles Tkinter UI layout and updates

controller_interface.py : defines abstractions for FileSelector and Storage

main.py : Acts as controller, in charge of interactions between UI and logic
```
### Open/Closed Principle
Storage, RecordStore, and FileSelector can all be extended, as they are utilized by the controller in main.py through their abstract interfaces, as defined in controller_interface.py. Additionally, this means that if an additional implementation were added to, say, store files in the cloud, the local_storage.py implementation could remain unchanged.

### Liskov Substitution Principle
Any implementation of Storage, FileSelector, or RecordStore can be implemented through the controller_interface.py definitions

### Interface Segregation Principle
The interfaces in the program are kept tiny and seperate from one another, minimizing dependencies.

Existing dependencies:
```
ArchiveApp (controller)
|-- depends on -> FileSelector.select_file()
|-- depends on -> Storage.save() 
|-- depends on -> RecordStore.append(), RecordStore.read_tail
```
Implementations of interfaces:

    TkFileSelector ->  implements -> FileSelector

    LocalStorage ->  implements -> Storage

    CsvRecordStore -> implements -> RecordStore

### Dependency Inversion Principle
The high-level controller only relies on the abstractions of the FileSelector, Storage, and RecordStore interfaces. The actual details of how the concrete implementations work only matter at the lower level and are therefore only accessed there. For example, LocalStorage implementation can be directly applied to the program through the Storage interface, but not vice versa.

## Design Patterns

### Singleton - Creational - Classes that are ensured to have only one instance
----


### Immutable Classes - Creational - Classes whose variables cannot be changed after initialization
----


### Factory Method - Creational - Provides interfaces for creating objects in a superclass and allows subclasses to alter the types of objects created
----


### Abstract Factory - Creational - Allows production of families of related objects without specifying concrete classes
----


### Marker - Creational - An iterface with no behavior that is primarily used to specify a type (for metadata purposes)
----


### Proxy - Structural - Provides a substitute or placeholder for another object and assists in controlling access to the original object


### Prototype - Creational - Copies existing objects without making code dependent on those classes
----


### Object Pool - Creational - A cache of reusable, high-cost objects
----


### Iterator - Behavioral - Traverse elements of a collection without exposing the underlying representation
----


### Facade - Structural - Provides a simplified interface to libraries, frameworks, or any other complex set of classes
----


### Builder - Creational - Constructs coimplex objects step by step
----


### Bridge - Structural - Separates an abstraction from its implementation so that they can vary independently
----


### Composite - Structural - Compose objects into tree structures and work with the structures as though they are individual objects
----


### Chain of Responsibility - Behavioral - Enables passing of requests along a chain of handlers, with handlers either handling the request or passing it to the next handler
----


### Filter - Structural - Perform composable transformations and computations on streams (Just think about how filtering actually works)
----


### Adapter - Structural - Defines a class that allows interfaces that are incompatible to work together (like an interface for your interfaces)
----


### Flyweight - Structural - Fits more objects into memory by sharing common parts of objects between said objects, rather than storing individual instances in each
----


### Strategy - Behavioral - Defines a family of algorithms in separate classes that are interchangable
----


### State - Behavioral - Lets an object alter its behavior when internal state changes, making it appear as though it changes classes 
----


### Decorator - Structural - Attach new behaviors to objects by placing them in wrapper objects that contain the behaviors
----


### Command - Behavioral - Turns a request into a standalone object that contains all information about the request
----


### Mediator - Behavioral - Reduces chaotic dependencies between objects (Handlers are an example of this)
----


### Memento - Behavioral - Saves and restores state of object without revealing details of implementation
----


### Observer - Behavioral - Defines a subscription mechanism to notify multiple objects of events
----


### Visitor - Behavioral - Used to perform an operation on a group of similar objects and allows trhe definition of new operations for classes without changing said classes
----


### Null Object - Behavioral - Encapsulate the absence of an object (that is optionally null) by providing an alternative that offers suitable default do-nothing behavior
----

