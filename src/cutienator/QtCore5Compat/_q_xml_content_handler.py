"""
QXmlContentHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QXmlAttributes, QXmlLocator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QXmlAttributes = WAIT['QXmlAttributes']
  QXmlLocator = WAIT['QXmlLocator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlContentHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlContentHandler: a plain Python object standing in
  front of one C++ QXmlContentHandler.

  What exists
  -----------

  Every function of Qt's QXmlContentHandler that has a ritual and that Python
  can call so far, 12 names in all: 'setDocumentLocator', 'startDocument',
  'endDocument', 'startPrefixMapping', 'endPrefixMapping', 'startElement',
  'endElement', 'characters', 'ignorableWhitespace', 'processingInstruction',
  'skippedEntity', 'errorString'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlContentHandler::~QXmlContentHandler()': the destructor: Python
    never removes a C++ QXmlContentHandler.

  What to expect
  --------------

  - The C++ QXmlContentHandler is created at the first use, not by
    'QXmlContentHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlContentHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlContentHandler'

  #  A C++ QXmlContentHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlContentHandler'

  #  The functions Qt calls itself that QXmlContentHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setDocumentLocator': (
          ('_ZN18QXmlContentHandler18setDocumentLocatorEP11QXmlLocator',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlLocator'),
           )),
      ),
      'startDocument': (
          ('_ZN18QXmlContentHandler13startDocumentEv',
           ('bool', 'number', ''),
           ()),
      ),
      'endDocument': (
          ('_ZN18QXmlContentHandler11endDocumentEv',
           ('bool', 'number', ''),
           ()),
      ),
      'startPrefixMapping': (
          ('_ZN18QXmlContentHandler18startPrefixMappingERK7QStringS2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'endPrefixMapping': (
          ('_ZN18QXmlContentHandler16endPrefixMappingERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'startElement': (
          ('_ZN18QXmlContentHandler12startElementERK7QStringS2_S2_RK14QXmlA'
           'ttributes',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore5Compat:QXmlAttributes'),
           )),
      ),
      'endElement': (
          ('_ZN18QXmlContentHandler10endElementERK7QStringS2_S2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'characters': (
          ('_ZN18QXmlContentHandler10charactersERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'ignorableWhitespace': (
          ('_ZN18QXmlContentHandler19ignorableWhitespaceERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'processingInstruction': (
          ('_ZN18QXmlContentHandler21processingInstructionERK7QStringS2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'skippedEntity': (
          ('_ZN18QXmlContentHandler13skippedEntityERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'errorString': (
          ('_ZNK18QXmlContentHandler11errorStringEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QXmlContentHandler::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlContentHandler::errorString() const
    return self.uglySide.call(
        'ritual_ZNK18QXmlContentHandler11errorStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QXmlLocator)
  @overload(NoneType)
  def setDocumentLocator(self, locator: Optional[QXmlLocator]) -> None:
    """
    Calls Qt's 'void QXmlContentHandler::setDocumentLocator(QXmlLocator
    *locator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#setDocumentLocator

    Parameters
    ----------

    locator : Optional[QXmlLocator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlContentHandler::setDocumentLocator(QXmlLocator *locator)
    self.uglySide.call(
        'ritual_ZN18QXmlContentHandler18setDocumentLocatorEP11QXmlLocator',
        self._addressOf(locator),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def startDocument(self) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::startDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#startDocument
    """
    #  bool QXmlContentHandler::startDocument()
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler13startDocumentEv',
    )

  def endDocument(self) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::endDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#endDocument
    """
    #  bool QXmlContentHandler::endDocument()
    return self.uglySide.call('ritual_ZN18QXmlContentHandler11endDocumentEv')

  @overload(str, str)
  def startPrefixMapping(self, prefix: str, uri: str) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::startPrefixMapping(const QString
    &prefix, const QString &uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#startPrefixMapping

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    uri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlContentHandler::startPrefixMapping(const QString &prefix,
    #      const QString &uri)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler18startPrefixMappingERK7QStringS2_',
        prefix, uri,
    )

  @overload(str)
  def endPrefixMapping(self, prefix: str) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::endPrefixMapping(const QString
    &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#endPrefixMapping

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlContentHandler::endPrefixMapping(const QString &prefix)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler16endPrefixMappingERK7QString', prefix,
    )

  @overload(str, str, str, QXmlAttributes)
  def startElement(
      self,
      namespaceURI: str,
      localName: str,
      qName: str,
      atts: QXmlAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::startElement(const QString
    &namespaceURI, const QString &localName, const QString &qName, const
    QXmlAttributes &atts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#startElement

    Parameters
    ----------

    namespaceURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.

    atts : QXmlAttributes
      Passed on as a value: Qt reads the C++ QXmlAttributes, which stays
      Python's own.
    """
    #  bool QXmlContentHandler::startElement(const QString &namespaceURI,
    #      const QString &localName, const QString &qName, const
    #      QXmlAttributes &atts)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler12startElementERK7QStringS2_S2_RK14QX'
        'mlAttributes',
        namespaceURI, localName, qName, self._valueOf(atts),
    )

  @overload(str, str, str)
  def endElement(
      self,
      namespaceURI: str,
      localName: str,
      qName: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::endElement(const QString
    &namespaceURI, const QString &localName, const QString &qName)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlcontenthandler.html#endElement

    Parameters
    ----------

    namespaceURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlContentHandler::endElement(const QString &namespaceURI, const
    #      QString &localName, const QString &qName)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler10endElementERK7QStringS2_S2_',
        namespaceURI, localName, qName,
    )

  @overload(str)
  def characters(self, ch: str) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::characters(const QString &ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlcontenthandler.html#characters

    Parameters
    ----------

    ch : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlContentHandler::characters(const QString &ch)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler10charactersERK7QString', ch,
    )

  @overload(str)
  def ignorableWhitespace(self, ch: str) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::ignorableWhitespace(const QString
    &ch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#ignorableWhitespace

    Parameters
    ----------

    ch : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlContentHandler::ignorableWhitespace(const QString &ch)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler19ignorableWhitespaceERK7QString', ch,
    )

  @overload(str, str)
  def processingInstruction(self, target: str, data: str) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::processingInstruction(const QString
    &target, const QString &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#processingInstruction

    Parameters
    ----------

    target : str
      Passed on as it is: a QString is made of it for the call.

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlContentHandler::processingInstruction(const QString &target,
    #      const QString &data)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler21processingInstructionERK7QStringS2_',
        target, data,
    )

  @overload(str)
  def skippedEntity(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlContentHandler::skippedEntity(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlcontenthandler.html#skippedEntity

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlContentHandler::skippedEntity(const QString &name)
    return self.uglySide.call(
        'ritual_ZN18QXmlContentHandler13skippedEntityERK7QString', name,
    )
