#### Data Formats: JSON and XML

Web apps transfer data between frontend and backend. 

**XML**: a markup language (tag-based) in which tags enlcose content. Difference between HTML, is that in XML you can define your own arbitrary tags. Nested tags form a heirarchy, which starts from the root tag.

**XPath**: Provides a way to make a query for accessing parts of an XML document. to access a specific tag you can query it using "/tagname" and to access child elements we append them after the appropriate amount of forward slashes- very similar to filesytem traversal.

In XML we can define any arbitrary attribute for any tag.
The **Document Type Definition (DTD)** defines the document structure and legal elements and attributes. Declared in the document inside the !DOCTYPE tag.
Example:
```xml
<!DOCTYPE note [
	<!ELEMENT note (name, body)>
	<!ELEMENT name(#PCDATA)>
	<!ELEMENT body (#PCDATA)>
]>

<!DOCTYPE tag_name [
	<!ELEMENT allowed_tasks(children_tags)>
]
```
Entities are ways to abbreviate things. three parts ; ampersand, entity ame and semicolon.
internal entities are defined inside of the xml while external entities are defined in a  dtd file- possibly on a remote system (introduce more security concerns). 

Tool for XPath: `https://codebeautify.org/Xpath-Tester`

**XXE Attack**: stands for XML External Entity Injection attack, refers to an exploit by which an attacker will make an application execute arbitrary code by sending an external entity to an application expecting a legitimate external entity. The best defense is to disable external entities on the server.

# JSON

- JavaScript Object Notation: based on data interchange format. 
- More efficient to parse

JSON has no way to natively constrain the structure of the data.
