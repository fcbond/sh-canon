This directory contains more metadata.


Canonical Abbreviations
=======================

Jay Finley Christ (1947) made a list of abbreviations for the stories.

Jay Finley Christ, *An Irregular Guide to Sherlock Holmes of Baker
Street*, New York: Argus Books, 1947.

See also here: http://faculty.winthrop.edu/kosterj/engl200/sherlock/abbreviations_canon.pdf

Abbreviations are built on a simple rule: take the 4 first letters of
the title, ignoring *The ... of*.

For example:
 - The Adventure of the Gloria Scott is ``GLOR``
 - The Disappearance of Lady Frances Carfax is ``LADY``
 - The Problem of Thor Bridge is ``THOR``

There are exceptions to this rule:
 - The Adventure of Charles Augustus Milverton is ``CHAS``
   because the firstname Charles is often reduced to Chas. in English.
 - The Adventure of the Engineer's Thumb is ``ENGR`` because *engr*
   is the usual abbreviation for *engineer* in USA.
 - The Adventure of the Three Gables is ``3GAB``
 - The Adventure of the Three Garridebs is ``3GAR``
 - The Adventure of the Three Students is ``3STU``

There are also three letter abbreviations for the collections::

  ADV	TITLE	The Adventures of Sherlock Holmes
  MEM	TITLE	The Memoirs of Sherlock Holmes
  RET	TITLE	The Return of Sherlock Holmes
  BOW	TITLE	His Last Bow
  CAS	TITLE	The Casebook of Sherlock Holmes



   
ABBR.tsv
--------
 
The meta-data file ``ABBR.tsv`` has three columns::

  Abbreviation<tab>TITLE<tab>Title

e.g.::
  
  SPEC␉TITLE␉The Adventure of the Speckled Band

If there is more than one way to write it (e.g. with or without "The
Adventure of" or with different punctuation, then the preferred one is
listed first.

e.g. ::
  
  ENGR␉TITLE␉The Adventure of the Engineer’s Thumb
  ENGR␉TITLE␉The Adventure of the Engineer's Thumb


In general I prefer unicode quotes.


META.tsv
========

This is for metadata that does not spoil the story.

The meta-data file ``META.tsv`` has three columns::

  Abbreviation<tab>Datatype<tab>Value

e.g.::
  
  FINA␉PUBLISHED␉various US newspapers on 26 November 1893 (US)
  FINA␉PUBLISHED␉The Strand Magazine (UK) in December 1893
  FINA␉ORDER␉26
  FINA␉COLLECTION␉The Memoirs of Sherlock Holmes

The datatypes are:

- PUBLISHED --- when and where first published (US) and (UK)
- ORDER --- the order it was published in
- COLLECTION --- which collection it was in

 
This data was mainly taken from ``The Conan Doyle Encyclopedia``_.

-``The Conan Doyle Encyclopedia``: https://www.arthur-conan-doyle.com/


LINKS.tsv
=========

This is for random links to other information.

The meta-data file ``LINKS.tsv`` has three columns::

  Abbreviation<tab>Title<tab>LINK


