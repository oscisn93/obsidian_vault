# HTTP, XML, and JSON, Applications Architectures, and BurpSuite

#### 1. Please complete the following TryHackMe learning path: https://tryhackme.com/paths

#### 2. Consider the following XML document:
```xml
<class department="CPSC">
<number> 455 </number>
<section> 01 </section>
<scheduling>
<days> Wednesday </days>
<room> CS-104</room>
<time> 7:00 pm -- 9:45 pm </time>
</scheduling>
<description> Covers the principles and practices of web security</description>
</class>
```

	Please do the following:
1. Write a DTD that defines the structure of the document. Hint: please see https://www.w3schools.com/xml/xml_dtd_attributes.asp for an example on how to specify the DTD for attributes.
2. Use the following XML validator: https://freeonlineformatter.com/xml-validator to show that your DTD is valid.  Provide a screenshot.
3. What is the XPath to the node time?
4. Convert the above XML to an equivalent JSON format.
5. Complete the following TryHackMe room: https://tryhackme.com/room/owasptop10mw, that will give you hands-on experience with XXE attacks.  HINT: You can use the BurpSuite knowledge you have gained in the last question to perform this attack.  Please feel free to also check out this for more information: https://thehackerish.com/xxe-tutorial-in-practice-owasp-top-10-training/

#### 3. Describe the basics of the Monolothic, Microservices, and Serverless architectures and their impacts on security.

