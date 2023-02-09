#### Data Formats: JSON and XML

Web apps transfer data between frontend and backend. 

**XML**: a markup language (tag-based) in which tags enlcose content. Difference between HTML, is that in XML you can define your own arbitrary tags. Nested tags form a heirarchy, which starts from the root tag.

**XPath**: Provides a way to make a query for accessing parts of an XML document. to access a specific tag you can query it using "/tagname" and to access child elements we append them after the appropriate amount of forward slashes- very similar to filesytem traversal.

In XML we can define any arbitrary attribute for any tag.
The **Document Type Definition (DTD)** defins the document structure and legal elements and attributes. Declared in the document inside the !DOCTYPE tag.
Example:
```xml
<!DOCTYPE note [
	<!ELEMENT note (name, body)>
	<!ELEMENT name(#PCDATA)>
	<!ELEMENT body (#PCDATA)>
]>
```
Entities are ways to abbreviate things. 