# Part 3: Knowledge Modeling <br> - Semantic Web 

## Implicit vs. Explicit Knowledge

Information retrieval and data mining aim at extracting and using knowledge that is implicitly represented in documents

Alternatively, knowledge can, and is, also explicitly represented

## 1. SEMI-STRUCTURED DATA

## Database Schemas

Schemas define data structures for databases

- Relational database schemas, XML Schemas

Agreement on data structures

- Well understood meaning of data values
- Data consistency, e.g., integrity constraints

Optimizing query evaluation and data storage

- e.g. indexing, query optimization

Schemas in database management systems play two important roles. On the one hand they define a priori data structures that capture that application semantics. In particular they label data values with names (e.g. attribute names) that have a wellunderstood semantics. By defining fixed data structures and additionally imposing integrity constraints they additionally assure that data stored in the database remains structurally and semantically coherent. Exploiting knowledge on data structures also enables query and storage optimizations.

However, in many information processing settings, e.g., on the Web, schema information is not always readily available, and imposing the use of schema might be too rigid and turn into a disadvantage.

## Data on the Web

In the typical Web setting no schema information is being used. When searching for information content-oriented queries are used, e.g., by providing keywords. This may work well for very specific search terms, such as illustrated for the example "anglerfish", but might become problematic, when the search term has an ambiguous meaning, as illustrated for the example "leech". The problem is that when the type of the information that is searched is not specified (in the case of the example the type would be "Organism"), the search algorithm cannot disambiguate the different potential meanings of the search term. If we consider the search term as a data value, this would correspond to the case where we consider a data value in a relational database without knowing it's type and attribute name. For purely data-oriented searches, such as for a numerical value the problem becomes even more evident. Thus it appears for some cases having a data schema available, would seem also helpful for searches in the Web.

## Using HTML to Structure Data

A typical approach to handle data in the Web is to used structured layouts, e.g. using HTML tables. In this way a context is provided, that allows to correctly interpret data values. When inspecting the source code of a typical HTML-based page with structured data, we recognize however that it might become difficult to automatically process such a page and correctly interpret the data contained in it. Such processing might be very involved and error-prone, even more so that in the context of editing Web page layout no mechanisms assure that the intended page structure is correctly implemented. The problem is that a layout language, such as HTML, never has been conceived to specify semantics of data.

## Web Scraping

It might be obvious and it might not be the sexiest challenge, but sloppy and always changing website formats is by far the biggest challenge you will face when extracting data at scale. Not necessarily because of the complexity of the task, but the time and resources you will spend dealing with it.

## Application-specific Markup

## Limitations of HTML

- Structure of data expressed as layout : $<$ tr><td> leech </td><tr>
- Semantics of data hard to analyse and difficult to share
- No schemas, no constraints


## Embedding of schema information into the data

Therefore an alternative approach for specifying the meaning of data contained in documents, in particular in Web documents, has been conceived. As for HTML it is based on the idea of using tags, i.e. markup that associates to parts of a document a name. However, instead of using tags to provide layout instructions (e.g. a table format), tags are used to provide domain-specific meaning to data contained in a document. For example, markup can be used to specify that a specific name (such as leech) denotes an organism. This approach is of course well known and widely used. For example, email formats contain different standard markups to indicate the different parts of a mail. In the Web this approach has found wide-spread adoption through the XML format. XML generalizes the markup approach from HTML to allow applications to specify their application-specific tags and to embed them into documents.

Exercise: refresh your knowledge on XML and schemas in XML.

## Semi-structured Data

Data that contains embedded schema information, such as tags or markup, is generally called semi-structured data. Semistructured data allows to indicate the meaning of data values, as in structured data with schemas, without requiring predefined schemas. This combines flexibility with the ability to capture meaning. The fact that semi-structured data does not require schemas, does not imply that we cannot define schemas for semi-structured data. XML is an example of this. We can have XML structured documents without schema, so-called wellformed XML documents, but define in addition schemas for XML (document type definitions, so-called XML DTDs). Documents that follow such a schema are then called valid XML documents.

## XML - a Document Markup Language

```
<?xml version="1.0"?>
<purchaseOrder orderDate="1999-10-20">
    <shipTo country="US">
        <name>Alice Smith</name>
        <street>123 Maple Street</street>
        <city>Mill Valley</city>
        <state>CA</state>
        <zip>90952</zip>
    </shipTo>
    <billTo country="US">
        <name>Robert Smith</name>
        <street>8 Oak Avenue</street>
        <city>Old Town</city>
        <state>PA</state>
        <zip>95819</zip>
    </billo>
    <comment>Hurry, my lawn is going wild!
        </comment>
```

Originally XML has been conceived as a document model. In this example of an XML document we can clearly see the document nature of XML. An XML document consists of hierarchically nested tags which enclose textual content.

## XML- a Semi-structured Data Model

However, the same XML document can also be viewed as structured data. An XML parser would typically generate a hierarchical data structure as illustrated. This explains why we can understand XML also as a data model, more precisely a semi-structure data model, as it embeds schema information into the data.

## Schema-less data

## Benefits of schema-less data

Increased flexibility

- e.g. dynamically adding or dropping structural elements such as attributes

Self-contained data

- e.g. context (schema information) directly encoded into data (markup)


## Drawbacks

Loss of consistency

Certain optimizations not feasible

Semi-structured data can be schema-less. This has significant advantages for applications that do not know the structural elements in advance. For example, often it is helpful if new types of attributes can be added in a database as application requirements evolve. Another advantage is that by embedding schema information into the data, data can be interpreted without requiring additional context information in the form of database schemas. This can be useful in applications where data is exchanged, as illustrated before for the case of XML. Having no schema has however also its drawbacks as, the additional flexibility also my be at the detriment of data consistency. Applications might, for example, not be able to properly process attributes that have been arbitrarily added. Also many optimizations that rely on the availability of a schema, and on the assumption that the schema is stable, can not be applied.

The duality of $X M L$, being a document model and a data model at the same time makes it particularly suitable for applications that have to exchange data over communication networks. For every data collection or database that is represented in XML there exists a canonical encoding into a text (document). The encoding is called serialization. Since documents are sequences of symbols they can be naturally exchanged over communication networks.

## Serialised vs. Semi-structured Data

Many of the popular semi-structured data models have a serialized format (XML) or have been conceived to serialise data (JSON)

However, there exist semi-structured data models that are not based on a serialized representation $->$ knowledge graphs

## 2. SEMANTIC WEB

## The Semantic Web

XML provides a framework to encode data on the Web in a standardized fashion, to deal with irregular Web data structures and to exchange Web data among information systems. Thus it contributes in particular to overcoming syntactic heterogeneity on the Web.

The markup used in XML can be interpreted by applications. This enables automatic processing of Web data. However, for properly interpreting the markup, semantic heterogeneity needs to be overcome as well. The same concepts can (and will be) represented in different application contexts differently, e.g., by using different terms to denote the same meaning. This is a major obstacle to enable interoperability on the Web and indeed in industry this is considered as one of the major problems in the use of information technology.

## The Vision of W3C: Semantic Web

The Semantic Web is an extension of the current Web in which information is given well-defined meaning, better enabling computers and people to work in cooperation. The mix of content on the Web has been shifting from exclusively human-oriented content to more and more data content. The Semantic Web brings to the Web the idea of having data defined and linked in a way that it can be used for more effective discovery, automation, integration, and reuse across various applications. For the Web to reach its full potential, it must evolve into a Semantic Web, providing a universally accessible platform that allows data to be shared and processed by automated tools as well as by people. The Semantic Web is an initiative of the World Wide Web Consortium (W3C), with the goal of extending the current Web to facilitate Web automation, universally accessible content, and the 'Web of Trust'.

In order to address the problem of semantic interoperability and thus enable automated processing of Web data, the W3C initiated the "Semantic Web" initiative. The Semantic Web is a framework that builds on Web technology, including the XML framework and extends it with technologies that facilitate semantic interoperability.

## Three Ways to Overcome Semantic Heterogeneity 

There exist three basic approaches to tackle the problem of automating semantic processing of the data on the Web:

1. Standardization avoids the problem of semantic heterogeneity a priori. This approach is used when there exists already (historically) a wide agreement on the structure of relevant data and their interpretation. For example, terminology in the financial insustry is largely standardized, and therefore it is not a major problem to come up with agreed upon formal specifications of such terminology and corresponding schemas to represent the data. This is even more the case as there exist in this type of business environment typically strong players that can enforce the standards.
2. Translation or mapping between different schemas and databases is the second possibility to establish semantic interoperability. This is the approach that has been extensively studied for data integration problems in relatively small and controlled domains, such as inside businesses and organizations. The requirements in these domains are typically changing not too quickly, thus much effort can be invested into developing the necessary mappings in order to properly map data from one representation into another, or to map data from multiple representations into one common global representation.
3. The third possibility is slightly different from the second: instead of engineering mappings between heterogeneous schemas for each integration problem, one first agrees on a common conceptualization of the domain, covering relevant aspects for a large class of applications. This conceptualization is normally called an ontology and is supposed to be application independent. Since ontologies have a formal representation they are machine-processable. Once such an ontology is in place existing information sources can relate their structural elements for expressing certain concepts (e.g. element names) to concepts from the ontology. This then (ideally) enables other applications to properly interpret the contents of the information system. In addition, ontologies in the general case should include reasoning capabilities, which would permit to use not only hard-coded, or pre-canned knowledge (e.g. in form of explicitly relating concepts from an information system to the ontology), but also to derive new knowledge from combining existing knowledge in different ways such that new implied relations can be derived that have not been explicitly provided.

## Mapping: Three Approaches

Conceptually there exists three main possibilities of how to address semantic heterogeneity. A first approach is to map all the models everything to one common global model. This approach is taken with standardization. For example, EDIFACT is an international standard that models all concepts that are commonly used in business and trade. For exchanging information systems used in that domain map their data to EDIFACT and can thus exchange their information. A second approach, is to relate the model of an information system to a common model, frequently called ontology, and use this mapping to construct a direct mapping among the different models used in the information systems. A third approach consists of trying to construct directly a mapping among two information systems, without having any additional, shared knowledge in form of standards or ontologies among the two information systems.

## Direct Schema Mapping

Creating direct mappings among information systems has been intensively explored for mapping data that is stored in relational and XML databases, and where the model is represented as a database schema. The problem is known as the schema mapping problem. Given two schemas of databases, first schema elements are identified that are likely to correspond to each other, i.e. that are likely representing the same real world aspect. This can be done by using many types of analysis using structural and content features of the database schema and the database. Tools for supporting this steps are called schema mapping tools. Once this step is performed some conflicting correspondences may occur, e.g. mapping the some concept in one schema to two different ones in the other. These not to be resolved, typically through decisions taken by humans. Once the correspondences are consistent, mappings can be automatically derived. The mappings are typically expressed as queries of the data manipulation language.

## Annotation

This differentiation among different approaches to semantic interoperability can be nowadays found in standardization documents: according to ISO 14258 (Concepts and rules for enterprise models), there are three basic ways to relate entities together:

Integrated approach. There exists a common format for all models. This format must be as detailed as the models themselves. The common format is not necessarily a standard but must be agreed upon by all parties in order to elaborate models and build systems. (-> Standardization)

Federated approach. There is no common format. In order to establish interoperability parties must accommodate on the fly. Federated approach implies that no partner imposes their models, languages and methods of work. This means they must share a common ontology. (-> Translation)

Unified approach. There exists a common format but only at a meta-level. This meta-model is not an executable entity as in the case of the integrated approach but provides a way for semantic equivalence to allow mapping between models. (-> Annotation)

This simple example illustrates of how ontologies might help to increase semantic interoperability and how new knowledge may be generated by reasoning. Take our earlier example of biological databases. These typically use different schemas to model related facts. For example, Database 1 uses the term Organism to denote an organism, and database 2 uses the term Species to do the same. Two annotators, who share the same ontology, now inspect the document and each of them associates the elements with terms taken from the ontology. So Annotator 1 decides that the element Organism corresponds to information related to an organism, whereas annotator 2 recognizes actually from the content that the element is related to information about a fish and annotates correspondingly (by establishing a is-instance-of relationship). At this point, the fact that both annotators used the same ontology and that reasoning is possible in this ontology comes into play. Since in the ontology a Fish is a subconcept of Organism (a fact represented formally by a ISA relationship in the ontology) an automated processing tool (e.g. for searching for information) might exploit this relationship and correctly identify for a request for information on Organisms in both databases the related elements.

## Ontologies

Ontologies are an explicit specification of a conceptualization of the real world (Gruber, 1993)

Ideally

- different information systems agree on the same ontology
- relate their model/schema/data elements to the ontology
- mapping can be constructed via the ontology

Thus ontologies provide a "proxy representation" for the real world, to which the interpretation of data in information systems refers to and thus provide an interpretation of the data in an information system that can be automatically processed. In order to realize this vision a number of technical challenges need to be addressed.

## Creating Ontologies

## Different approaches to create ontologies

1. Ontology engineering

- Manual effort
- Tools for editing and checking consistency

2. Automatic generation of ontologies

- From large document collections or existing structured data sources

Ontologies need to be built: this requires an agreement on the meaning of terms (symbols). In practice, there exists no other way to establish such an agreement than by extensively collecting knowledge (from humans) and represent it within a formal specification. This has been done in practice and as a result there exist extensive ontologies, some of them have been built up over many years. In the recent years, also approaches to construct ontologies automatically from existing data sources, either knowledge bases or large document collections, have been developed.

## Modeling and Encoding of Ontologies

Issues

- Modeling primitives and their semantics:
- what does an arrow mean?
- what does "instance-of" mean?
- what does ISA mean?
- Standardized encodings of the model
- Into document language (XML, HTML)
- Enriching document content with semantic markup

Ontologies need to be represented in a language or data model: in order to store the ontology a representation mechanism (a model) is needed, and the model needs to be encoded into data. The choice of the model is an important issue, since it should be very expressive (as a wide variety of aspects of the real world need to be modeled) and easy to use (as ontologies should be used in a wide range of applications) at the same time. The encoding is equally important, as it should be done in a standardized form. If this were not the case we would immediately loose the advantage of having a common conceptualization of the world at the abstract level, since we were not able to exchange it properly with others.

## Model Requirements for Ontologies

|  | HTML | XML | RDF | OWL |
| :---: | :---: | :---: | :---: | :---: |
| Simplicity | + | + | + | + |
| Exchangeability | + | + | + | + |
| Non-intrusive annotation | + | - | + | + |
| Domain-specific vocabularies | - | + | + | + |
| Modeling primitives | - | - | + | + |
| Reasoning capabilities | - | - | - | + |

With respect to modeling and encoding of ontologies for the Semantic Web, there exist a number of requirements, some of which follow from what we have discussed earlier:

1. Simplicity: the success of the Web was always founded on the principle of simplicity of concepts to encourage wide-spread use. Therefore complex models will not be successful. This is an important criterion, since some of the existing ontologies (one example is Cyc) are expressed in fairly complex knowledge representation models.
2. Exchangeability: Since the web is a communication environment, any kind of data that is processed must be easily exchangeable. This is what motivated the use of XML as a data representation format in the first place and should hold for metadata and ontology data as well.
3. Non-intrusive annotation: as the example on annotation we gave earlier demonstrated, machine-processable knowledge required for the interpretation of data will be associated with the data typically a-posteriori. Also there does not always exists a unique interpretation for the same data. Therefore any attempt to encode the knowledge required for interpretation directly into the data is not practical. This excludes, for example, the approach to use XML elements for annotation.
4. Domain-specific vocabularies: the model must provide a mechanism that permits to introduce vocabulary or terminology that is specific to a domain, in other words the possibility to specify schemas for different domains.
5. Modeling primitives: since an ontology model will be used in many different, and potentially very complex contexts (applications) they have to offer a sufficiently rich set of possibilities to model complex situations (e.g. complex structures or complex relationships). There exists a rich experience in modeling (e.g. from data modeling in databases, e.g. the entity-relationship model) and models for ontologies can draw from them.
6. Reasoning Capabilities: the example we discussed earlier already illustrates that even simple forms of reasoning within the ontology layer can make the interpretation of the data much more powerful (and thus the processing in the Semantic Web).

In this table we evaluate HTML, XML, RDF and OWL with respect to each of these aspects. RDF is the Resource Description Framework and is the first WWW standard proposed for the Semantic Web. OWL is the ontology interchange language, an extension of RDF proposed to enrich it with more reasoning capabilities and providing a well-defined semantics. We will introduce both models subsequently.

An interesting interpretation of the role of ontologies in the Web architecture is the following: ontology models support automated processing of semantics on the Web, and thus separate semantic concerns from the concern of structuring data; This is similar to the step from HTML to XML, were the issues of structuring data where separated from the issues related to the presentation (layout) of data. With the Semantic Web thus an attempt is made to separate meaning from structure.

## W3C Web architecture

The Semantic Web standards RDF and OWL are positioned in the Semantic Web architecture in top of the syntactic layer.

## 3. RDF RESOURCE DESCRIPTION FRAMEWORK

RDF consists of two parts: a language for representing metadata instances (RDF), which allows to annotate Web resources with statements. The Web resources are addressed by Universal Resource Identifiers (URI), of which URL's are the most important example. Thus any Web document or part of it can be annotated. The second part of the RDF standard is a language for specifying schemas for RDF Instances. This language enables specification of the vocabulary and grammar that is used for forming statements for annotation. Since RDF statements can be created also without using RDF schemas, RDF is a semi-structured data model, similar as with well-formed XML (instances) and XML-DTD (schemas).

The RDF model is similar to the entity-relationship (ER) model. Entities correspond to resources and relationships correspond to properties. The main difference is that RDF requires that relationships are directed, and have a specific semantics: the resource from which the (directed) relationship emerges is assigned a property with the value to which the relationship points. This reflects the intention to use RDF to associated metadata (the value) with data (the source of the relationship). Sample RDF applications include PICS (annotating documents with information on the suitability of the content for certain groups, e.g. like the movie rating system) and Dublin Core (annotating documents with basic bibliographic information.

It is important to know that the syntax of RDF and its encoding into XML is well-specified, but that the semantics RDF is only specified in a «semi-formal» manner. This introduces certain
ambiguities for applications interpreting RDF statements.

## RDF Statements Example

The basic constituent of RDF is an RDF statement. We can view RDF statements in three different ways: we can view them like natural language sentences, where the subject is a URI (uniform resource identifier) and the object can be either a URI or a String; we can view them as directed graphs, where the subject and object are represented as nodes (an ellipsis is used to represent resources (identified by a URI) and rectangles to represent literals (atomic XML values) and the predicate is represented as directed link, or we can view them as XML documents where the RDF statement is encoded into XML format. The graph representation is in particular suitable for visual presentation and reasoning, whereas the XML representation is used for exchange and storage.

## RDF Syntax

For encoding RDF into XML there exist many syntactic variations, which can make the understanding of RDF documents sometimes rather difficult. Here we summarize the most important variants. The basic pattern of encoding is as follows: the subject is represented by an XML element called rdf:Description. This element is the root of the document fragment representing the RDF statement. In the content of this element one finds one (or more) predicates, represented by XML elements, e.g. s:Creator. The content of this XML element in turn represents the object of the RDF statement. If the object is not a literal, one can alternatively represent the object as an attribute of the predicate element. Also, both the predicate and the object can be encoded into the element representing the statement, as it is shown for s:Date predicate.

## Typing Resources

RDF allows us to categorize resources into different classes (typing). For that purpose one associates with the resource that should be categorized another resource, that represents the category, using a special RDF property rdf:type. We will see later, when introducing RDF schema, what are possible uses of typing. With respect to encoding, the type property can either be represented explicitly like any other property, or one can use a special abbreviated syntax, where the name of the type becomes the element name of the element representing the statement.

## RDF Complex Values

Associating a subject with a property whose value is a simple object is just the simplest form of a statement. In general, the value of a property (the object of the statement) may be a complex statement itself (in data type parlance "of a complex type"). In order to represent such complex object values a new intermediate resource is created (in the example Person://1234/1) to which different properties are associated. Note that this is different of directly associating these properties with the subject of the overall statement (http://www.doc.ch/ in the example) (why?).

In the XML encoding such a complex object value can be represented by directly inlining the complex object into the content of the statement.

## RDF Containers

Containers

- Bag (unordered)
- Seq (ordered)
- Alt (alternatives)

Statements can be made not only using single resources, but as well using collections of resources. For that purpose RDF provides the container concept. Containers are special resources of one of three container types that are specified in the RDF standard. A container resource is then associated with a set of other resources. By creating a statement using the container object as "object", one can express statements made about the set of objects. More precisely, one can specify whether the statement is a statement of the set of objects "as a whole" or a statement that applies to each element of the set individually (what the consequences of this distinction are is not further specified in RDF, this is an example where the semantics of RDF is not clearly specified).

There exist three different types of containers: bags which are unordered multi-sets (= sets with multiple occurrences of the same resources), sequences which are ordered sets (i.e. lists) of resources and alternatives which is a single resource that is to be chosen out of a given set. The property labels can be used to impose an order on the elements of the set, by using labels _1, _2 etc. If the order is irrelevant one can use the alternative syntax rdf:li instead of rdf:_1, rdf:_2 etc.

## Creating New Resources

RDF resources need not necessarily be pre-existing Web resources identified by URIs, but can also be instantiated within RDF statements, i.e., new resources can be defined as part of RDF statements. A resource is in general anything that can be identified on the Web. As a consequence also a new resource requires foremost an identifier. For this purpose RDF provides the rdf:ID attribute to introduce the identifier of the resource. This attribute replaces rdf:about attribute when the statement is about a new resource instead about an existing resource. Using the identifier, this new resource can then be referred to in other RDF statements.

## RDF Reification

In RDF everything is a resource. In particular, RDF statements are considered as resources and therefore it should be possible to make statements about them. From the viewpoint of the Semantic Web this is in fact extremely important. Since annotations do not express absolute truth but rather different interpretations of data, it is important to foresee the possibility of annotating annotations (such as illustrated in the simple example). This allows to comment on annotations, to agree or dispute them etc..

When considering the graph representation of RDF, it is not immediately clear of how to treat a statement as a resource, since a statement consists of three structural elements, the subject, the object, and the predicate. But we can apply the same "trick" as we did already for complex objects and collections. We introduce a new resource which serves as representative for the statement. This resource obtains as properties all the constituents that make up the statement it represents. This process is called reification. It is straightforward to connect the resource representing the statement it to it's subject and object, as they are both resources themselves. Also the type of the object can be determined through a property rdf:type pointing to the special resource rdf:statement representing the category of statements. For the predicate a specific new resource representing the predicate is required. We will see later, when introducing RDF schema, that this new resource is indeed part of a schema for RDF statements, expressing that statements using this properties are possible in the given context. The reified RDF statement is connected to its constituents through the special RDF properties rdf:object, rdf:subject and rdf:property. By reifying a statement one creates a new resource, which can be anonymous, if no identifier is associated with it using rdf:ID, or can be referenced if it has such an identifier.

## RDF Reification - Syntax

The statement has an anonymous resource as subject, namely the reified statement which is fully characterized by its properties!

```
<rdf:RDF>
<rdf:Description about="#triple123">
<rdf:subject resource="http://www.doc.ch"/>
<rdf:predicate resource="http://description.org/schema#Creator"/>
<rdf:object>ohn Smith</rdf:object>
<rdf:type resource="http://www.w3.org/TR/WD-rdf-syntax#Statement"/>
<dc:Creator>Anne Gold</dc:Creator>
</rdf:Description>
</rdf:RDF>
```

The XML encoding of reified statements follows the principles that have been introduced before. The reified statement is represented as a complex, anonymous object.

## RDF Schema - Classification 

We now introduce RDF Schema. RDF Schema provides two basic mechanisms.

1. Categorization RDF resources, into classes.
2. Constraints on the possible use of properties, in the form of constraints expressing which classes can participate as subjects and objects in statements using a specific property.

First we describe the classification mechanism. Classes are represented themselves as resources, which are of type rdfs:Class, a special class in the RDFS specification. The type property rdf:type is used (as in RDF) to indicate the type of a class resource. If an application resource is of a specific type then the resource is connected to the corresponding class resource via the rdf:type property. In the illustration two examples of this are included: the resource with ID "John Smith" belongs to the class (or is of type) Person and the resource "Married" is of type MaritalStatus (which is a resource representing a specific predicate type). Between different classes a subclass relationship can be specified, by using the attribute rdfs:subClassOf. The intended semantics is that any resource belonging to the subclass also belongs to the superclass (containment relationship).

An interesting aspect of RDFS is the modeling of the RDF and RDFS concepts within RDFS itself. This is done by introducing a meta-class level that models the modeling constructs and reflects the paradigm that in RDF everything is a resource, including the concepts introduced by RDF and RDFS. In particular classes are sets of resources, and thus the rdfs:Class resource is a subClass of rdfs:Resource. Application classes, such as "Animal", are sets of resources, and thus also subclass of rdfs:Resource. On the other hand, the type of a resource is indicated by the rdf:type property. Since rdfs:Resource is a class it is connected via the rdf:Type property to the rdfs:Class resource. This produces the cyclic structure that we can observe within the RDF meta-class schema (in fact in the figure only a small fragment of the RDFS meta-class schema is shown).

## RDF Schema - Properties

RDF properties: connect resources

- The RDF instance must have the properties that are declared for the class
- rdfs:domain: classes of which the instances may have a property
- rdfs:range: classes of which the instances may be the value of a property

The second important concept of RDFS is the possibility to constrain the usage of RDF properties that connect resources. As everything in RDF, RDF properties are resources themselves. Thus, they are represented in an RDF schema as resources. For example maritalStatus is a resource representing a property. In RDF schema it is now possible to constrain the usage of properties as follows: by connecting the property resource through the property rdfs:domain to a class resource, one specifies that the subject when using this property must originate from that class, i.e., be of the type of this class. Similarly for the object, the range can be constrained using rdfs:range. Ranges can also be of atomic type, in that case one connects the property resource to (predefined) resources representing the data type of the atomic type. In the example above this is the atomic type STRING.

The RDFS model bears a lot of similarity with object-oriented models (or type specifications in the context of OO programming languages). However a fundamental difference is that properties (attributes in $\mathrm{OO}$ terminology) are defined independently of
classes.

## RDF Schema - Syntax

```
<rdf:RDF xml:lang="en"
        xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
<rdfs:Class rdf:ID="Person">
    <rdf::subClassOf rdf:resource="http://www.w3.org/classes#Animal"/>
</rdf:Class>
<rdf:Property ID="maritalStatus">
    <rdfs:range rdf:resource="#MaritalStatus"/>
    <rdfs:domain rdf:resource="#Person"/>
</rdf:Property>
<rdf:Property |D="name">
    <rdfs:range rdf:resource="http://www.w3.org/classes#String"/>
    <rfs:domain rdf:resource="#Person"/>
</rdf:Property>
<rdf:Property ID="age">
    <rdfs:range rdf:resource="http://www.w3.org/classes#Integer"/>
    <rdfs:domain rdf:resource="#Person"/>
</rdf:Property>
<rdfs:Class rdf:ID="MaritalStatus"/>
<MaritalStatus rdf:ID="Married"/>
<MaritalStatus rdf:ID="Divorced"/>
<MaritalStatus rdf:ID="Single"/>
<MaritalStatus rdf:ID="Widowed"/>
```

Since RDF schemas are expressed as RDF statements they can be encoded into XML along the same principles that we have introduced for RDF statements earlier. This example shows the complete encoding of the RDF schema we have used in our example before. Throughout the schema the abbreviated syntax for statements is used, replacing the element name "Description" by the corresponding class name of the subject of the description. Note of how using the ID attribute, in the RDF schema new resources are introduced. They can be referred to from other statements using the newly introduced identifier prefixed with \#. The specification of the class with ID "MaritalStatus" includes the specification of the complete extension of the class, enumerating all possible values the members of this class can take, i.e., all possible predicate names that predicates of type MaritalStatus can take. Strictly speaking, the statements creating the instances of class are not part of the schema level but part of the instance level of RDF.

## 4. SEMANTIC WEB RESOURCES

## WordNet

English dictionary with semantic relationships

Synonymy. Words that have similar meanings, e.g. happy and glad.

Antonymy. The opposite of synonymy, e.g. happy and sad.

## Nouns only

Hypernymy. Hierarchical relationship between words, e.g., furniture is a hypernym of chair since every chair is a piece of furniture.

Hyponymy. Opposite of hypernymy. Dog is a hyponym of canine since every dog is a canine.

Meronymy. Part-whole relationship. For example, paper is a meronym of book, since paper is a part of a book.

## Schema.org

Collaborative, community activity to create, maintain, and promote schemas for structured data on the Internet.

- Sponsoring companies: Google, Microsoft, Yahoo and Yandex
- Two type hierarchies: textual property values, things that they describe
- Core vocabulary currently consists of 642 Types, 992 Properties, and 219 Enumeration values
- Used by other knowledge bases, e.g. Google Knowledge Graph API, Dbpedia, etc.


## WikiData

Community project to create an open database of structured data

- Data curation model like WikiMedia
- Intended to support Wikipedia (InfoBoxes)
- Currently $16.5+$ million statements
- Multi-lingual
- Both API access and full databases dumps (JSON, RDF)

