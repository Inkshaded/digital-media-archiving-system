# Design Patterns
## SOLID Design Principles
### Single Responsibility Principle
Below, all functional program files in src will be summarised simply to demonstrate adherence to the Single Responsibility Principle
```
Program Files

implementations/ # holds concrete behaviors
    csv_record_store : Implementation of RecordStorageInterface that creates/appends to a 'records' file to keep track of when and what has been archived
    local_search : Implementation of SearchInterface that searches for files with queried filenames in a specified directory when given a query
    local_storage.py : Implementation of FileStorageInterface that archives files locally
    tkinter_file_selector.py : Implementation of FileSelector that opens a tkinter dialog box to select a file

ui/
    ui_start.py : Handles Tkinter UI layout and updates

search/
    search_interface.py : defines abstraction for SearchInterface

storage_structure/
    file_storage_interface.py : defines abstraction for FileStorageInterface
    record_storage_interface.py : defines abstraction for RecordStorageInterface

    audio/
        audio_storage_interface.py : defines abstraction for AudioStorageInterface
    documents/
        documents_storage_interface.py : defines abstraction for DocumentsStorageInterface
    misc/
        misc_storage_interface.py : defines abstraction for MiscStorageInterface
    video/
        video_storage_interface.py : defines abstraction for VideoStorageInterface
    web/
        web_storage_interface.py : defines abstraction for WebStorageInterface

controller_interface/
    file_selector.py : defines abstraction for FileSelector
    user_state.py : defines UserState interface and UserState concrete states (ReaderState and ArchivistState)

app.py : Acts as controller, in charge of interactions between UI and logic
main.py : Application root
```
### Open/Closed Principle
FileStorageInterface, RecordStorageInterface, FileSelector, and SearchInterface can all be extended, as they are utilized by the controller in app.py through their abstract interfaces. This means that any concrete implementation that still adheres to the logic of any interface can be created to "extend" the functionality.

### Liskov Substitution Principle

### Interface Segregation Principle
The interfaces in the program are kept tiny and seperate from one another, minimizing dependencies.

Existing dependencies:
```
ArchiveApp (controller)
|-- depends on -> FileSelector.select_file()
|-- depends on -> SearchInterface.search_files()
|-- depends on -> FileStorageInterface.save() 
|-- depends on -> RecordStorageInterface.append(), RecordStorageInterface.read_tail
```
Implementations of interfaces:

    TkFileSelector ->  implements -> FileSelector

    LocalStorage ->  implements -> Storage

    CsvRecordStore -> implements -> RecordStore

### Dependency Inversion Principle
The high-level controller only relies on the abstractions of the FileStorageInterface, RecordStorageInterface, FileSelector, and SearchInterface interfaces. The actual details of how the concrete implementations work only matter at the lower level and are therefore only accessed there. For example, LocalStorage implementation can be directly applied to the program through the FileStorageInterface interface, but not vice versa.

## Design Patterns

### Singleton - Creational - Classes that are ensured to have only one instance
----
No classes are currently ensured to only have one instance

### Immutable Classes - Creational - Classes whose variables cannot be changed after initialization
----
No classes are currently set to be immutable

### Factory Method - Creational - Provides interfaces for creating objects in a superclass and allows subclasses to alter the types of objects created
----
All objects are currently instantiated manually

### Abstract Factory - Creational - Allows production of families of related objects without specifying concrete classes
----
All objects are currently instantiated manually

### Marker - Creational - An iterface with no behavior that is primarily used to specify a type (for metadata purposes)
----
Markers were added that can be applied to various types of media files that can be stored in the archive. In future, these markers can be used to assist with searching through particular filetypes in the archive using a search function that can analyze that data.


### Proxy - Structural - Provides a substitute or placeholder for another object and assists in controlling access to the original object
----
No access-control or wrapper classes are currently used

### Prototype - Creational - Copies existing objects without making code dependent on those classes
----
There isn't currently a need for clones of existing objects

### Object Pool - Creational - A cache of reusable, high-cost objects
----
No high-cost, reusable objects are currently required

### Iterator - Behavioral - Traverse elements of a collection without exposing the underlying representation
----
No complex Iterators are currently being used. A simple 

### Facade - Structural - Provides a simplified interface to libraries, frameworks, or any other complex set of classes
----
No Facade is currently being used

### Builder - Creational - Constructs complex objects step by step
----
No complex object construction is currently done by this program

### Bridge - Structural - Separates an abstraction from its implementation so that they can vary independently
----
While the project does separate many an implementation from an abstraction, all currently separated implementation/abstraction pairs are used as Strategies

### Composite - Structural - Compose objects into tree structures and work with the structures as though they are individual objects
----
Thouch the archival system would probably benefit from the use of a Composite storage structure, it is not currently implemented.

### Chain of Responsibility - Behavioral - Enables passing of requests along a chain of handlers, with handlers either handling the request or passing it to the next handler
----
Current archive system does have handlers but not chains of handlers

### Filter - Structural - Perform composable transformations and computations on streams (Just think about how filtering actually works)
----
Currently not used in the archiving system, but will likely have a use in a  more complex storage or search system wherein files can be organized automatically based on their filetype.

### Adapter - Structural - Defines a class that allows interfaces that are incompatible to work together (like an interface for your interfaces)
----
No Adapters are currently implemented

### Flyweight - Structural - Fits more objects into memory by sharing common parts of objects between said objects, rather than storing individual instances in each
----
Currently, there are no unchanging objects that can be shared for the sake of efficiency

### Strategy - Behavioral - Defines a family of algorithms in separate classes that are interchangable
----
FileSelector, FileStorageInterface, RecordStorageInterface and SearchInterface are all abstractly defined so that different implementations can be applied at runtime, and are thus defining families of algorithms that are interchangable

### State - Behavioral - Lets an object alter its behavior when internal state changes, making it appear as though it changes classes 
----
The UserState abstract class manages the ArchivistState and ReaderState concrete states to determine a user's ability to modify the content of the archive

### Decorator - Structural - Attach new behaviors to objects by placing them in wrapper objects that contain the behaviors
----
No behavior extensions are being made using Decorators

### Command - Behavioral - Turns a request into a standalone object that contains all information about the request
----
No Command objects are being used

### Mediator - Behavioral - Reduces chaotic dependencies between objects (Handlers are an example of this)
----
ArchiveApp connects the archive subsystems together and allows communication between them whilst preventing dependencies between them, making it the Mediator for pretty much all subsystems of the app

### Memento - Behavioral - Saves and restores state of object without revealing details of implementation
----
No Mementos are used, though they could be used to create a backup system for the archive in the future

### Observer - Behavioral - Defines a subscription mechanism to notify multiple objects of events
----
No Observers are currently used

### Visitor - Behavioral - Used to perform an operation on a group of similar objects and allows trhe definition of new operations for classes without changing said classes
----
No Visitors being used

### Null Object - Behavioral - Encapsulate the absence of an object (that is optionally null) by providing an alternative that offers suitable default do-nothing behavior
----
No Null Objects being used
