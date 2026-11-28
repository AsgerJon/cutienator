"""
QXmlDefaultHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QXmlContentHandler, QXmlDTDHandler, QXmlDeclHandler
from . import QXmlEntityResolver, QXmlErrorHandler, QXmlLexicalHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QXmlAttributes, QXmlLocator, QXmlParseException
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QXmlAttributes = WAIT['QXmlAttributes']
  QXmlLocator = WAIT['QXmlLocator']
  QXmlParseException = WAIT['QXmlParseException']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
  """
  The cute side of Qt's QXmlDefaultHandler: a plain Python object standing in
  front of one C++ QXmlDefaultHandler.

  It is built on the cute 'QXmlContentHandler', as Qt's QXmlDefaultHandler is
  built on Qt's QXmlContentHandler, and has everything that class has. It is
  built on the cute 'QXmlErrorHandler' as well, as Qt's QXmlDefaultHandler is
  built on Qt's QXmlErrorHandler too, and has everything that class has. It
  is built on the cute 'QXmlDTDHandler' as well, as Qt's QXmlDefaultHandler
  is built on Qt's QXmlDTDHandler too, and has everything that class has. It
  is built on the cute 'QXmlEntityResolver' as well, as Qt's
  QXmlDefaultHandler is built on Qt's QXmlEntityResolver too, and has
  everything that class has. It is built on the cute 'QXmlLexicalHandler' as
  well, as Qt's QXmlDefaultHandler is built on Qt's QXmlLexicalHandler too,
  and has everything that class has. It is built on the cute
  'QXmlDeclHandler' as well, as Qt's QXmlDefaultHandler is built on Qt's
  QXmlDeclHandler too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXmlDefaultHandler that has a ritual and that Python
  can call so far, 27 names in all: 'setDocumentLocator', 'startDocument',
  'endDocument', 'startPrefixMapping', 'endPrefixMapping', 'startElement',
  'endElement', 'characters', 'ignorableWhitespace', 'processingInstruction',
  'skippedEntity', 'warning', 'error', 'fatalError', 'notationDecl',
  'unparsedEntityDecl', 'startDTD', 'endDTD', 'startEntity', 'endEntity',
  'startCDATA', 'endCDATA', 'comment', 'attributeDecl', 'internalEntityDecl',
  'externalEntityDecl', 'errorString'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlDefaultHandler::~QXmlDefaultHandler()': the destructor: Python
    never removes a C++ QXmlDefaultHandler.

  What has no ritual
  ------------------

  3 of the 32 functions Qt declares: 2 forbidden; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QXmlDefaultHandler is created at the first use, not by
    'QXmlDefaultHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlDefaultHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlDefaultHandler'

  #  Qt's QXmlDefaultHandler is built on more than one class. The part of a
  #  C++ QXmlDefaultHandler that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QXmlErrorHandler': 'ritual_cast_QXmlDefaultHandler_QXmlErrorHandler',
      'QXmlDTDHandler': 'ritual_cast_QXmlDefaultHandler_QXmlDTDHandler',
      'QXmlEntityResolver':
          'ritual_cast_QXmlDefaultHandler_QXmlEntityResolver',
      'QXmlLexicalHandler':
          'ritual_cast_QXmlDefaultHandler_QXmlLexicalHandler',
      'QXmlDeclHandler': 'ritual_cast_QXmlDefaultHandler_QXmlDeclHandler',
  }

  #  A C++ QXmlDefaultHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlDefaultHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QXmlDefaultHandler::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlDefaultHandler::errorString() const
    ritual = 'ritual_ZNK18QXmlDefaultHandler11errorStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QXmlDefaultHandler11errorStringEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QXmlLocator)
  @overload(NoneType)
  def setDocumentLocator(self, locator: Optional[QXmlLocator]) -> None:
    """
    Calls Qt's 'void QXmlDefaultHandler::setDocumentLocator(QXmlLocator
    *locator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#setDocumentLocator

    Parameters
    ----------

    locator : Optional[QXmlLocator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlDefaultHandler::setDocumentLocator(QXmlLocator *locator)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler18setDocumentLocatorEP11QXmlLocator')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler18setDocumentLocatorEP11QXmlLoc'
          'ator')
    self.uglySide.call(ritual, self._addressOf(locator))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QXmlDefaultHandler::QXmlDefaultHandler()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#QXmlDefaultHandler
    """
    #  QXmlDefaultHandler::QXmlDefaultHandler()
    self._noteCreation(QXmlDefaultHandler, lambda: Rituals.call(
        'ritual_ZN18QXmlDefaultHandlerC1Ev',
    ))

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
    Calls Qt's 'bool QXmlDefaultHandler::startDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#startDocument
    """
    #  bool QXmlDefaultHandler::startDocument()
    ritual = 'ritual_ZN18QXmlDefaultHandler13startDocumentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler13startDocumentEv'
    return self.uglySide.call(ritual)

  def endDocument(self) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::endDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#endDocument
    """
    #  bool QXmlDefaultHandler::endDocument()
    ritual = 'ritual_ZN18QXmlDefaultHandler11endDocumentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler11endDocumentEv'
    return self.uglySide.call(ritual)

  @overload(str, str)
  def startPrefixMapping(self, prefix: str, uri: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::startPrefixMapping(const QString
    &prefix, const QString &uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#startPrefixMapping

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    uri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::startPrefixMapping(const QString &prefix,
    #      const QString &uri)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler18startPrefixMappingERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler18startPrefixMappingERK7QString'
          'S2_')
    return self.uglySide.call(ritual, prefix, uri)

  @overload(str)
  def endPrefixMapping(self, prefix: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::endPrefixMapping(const QString
    &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#endPrefixMapping

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::endPrefixMapping(const QString &prefix)
    ritual = 'ritual_ZN18QXmlDefaultHandler16endPrefixMappingERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler16endPrefixMappingERK7QString')
    return self.uglySide.call(ritual, prefix)

  @overload(str, str, str, QXmlAttributes)
  def startElement(
      self,
      namespaceURI: str,
      localName: str,
      qName: str,
      atts: QXmlAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::startElement(const QString
    &namespaceURI, const QString &localName, const QString &qName, const
    QXmlAttributes &atts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#startElement

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
    #  bool QXmlDefaultHandler::startElement(const QString &namespaceURI,
    #      const QString &localName, const QString &qName, const
    #      QXmlAttributes &atts)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler12startElementERK7QStringS2_S2_RK14QX'
        'mlAttributes')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler12startElementERK7QStringS2_S2_'
          'RK14QXmlAttributes')
    return self.uglySide.call(
        ritual, namespaceURI, localName, qName, self._valueOf(atts),
    )

  @overload(str, str, str)
  def endElement(
      self,
      namespaceURI: str,
      localName: str,
      qName: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::endElement(const QString
    &namespaceURI, const QString &localName, const QString &qName)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#endElement

    Parameters
    ----------

    namespaceURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::endElement(const QString &namespaceURI, const
    #      QString &localName, const QString &qName)
    ritual = 'ritual_ZN18QXmlDefaultHandler10endElementERK7QStringS2_S2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler10endElementERK7QStringS2_S2_')
    return self.uglySide.call(ritual, namespaceURI, localName, qName)

  @overload(str)
  def characters(self, ch: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::characters(const QString &ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#characters

    Parameters
    ----------

    ch : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::characters(const QString &ch)
    ritual = 'ritual_ZN18QXmlDefaultHandler10charactersERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler10charactersERK7QString'
    return self.uglySide.call(ritual, ch)

  @overload(str)
  def ignorableWhitespace(self, ch: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::ignorableWhitespace(const QString
    &ch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#ignorableWhitespace

    Parameters
    ----------

    ch : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::ignorableWhitespace(const QString &ch)
    ritual = 'ritual_ZN18QXmlDefaultHandler19ignorableWhitespaceERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler19ignorableWhitespaceERK7QStrin'
          'g')
    return self.uglySide.call(ritual, ch)

  @overload(str, str)
  def processingInstruction(self, target: str, data: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::processingInstruction(const QString
    &target, const QString &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#processingInstruction

    Parameters
    ----------

    target : str
      Passed on as it is: a QString is made of it for the call.

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::processingInstruction(const QString &target,
    #      const QString &data)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler21processingInstructionERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler21processingInstructionERK7QStr'
          'ingS2_')
    return self.uglySide.call(ritual, target, data)

  @overload(str)
  def skippedEntity(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::skippedEntity(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#skippedEntity

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::skippedEntity(const QString &name)
    ritual = 'ritual_ZN18QXmlDefaultHandler13skippedEntityERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler13skippedEntityERK7QString'
    return self.uglySide.call(ritual, name)

  @overload(QXmlParseException)
  def warning(self, exception: QXmlParseException) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::warning(const QXmlParseException
    &exception)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#warning

    Parameters
    ----------

    exception : QXmlParseException
      Passed on as a value: Qt reads the C++ QXmlParseException, which stays
      Python's own.
    """
    #  bool QXmlDefaultHandler::warning(const QXmlParseException &exception)
    ritual = 'ritual_ZN18QXmlDefaultHandler7warningERK18QXmlParseException'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler7warningERK18QXmlParseException')
    return self.uglySide.call(ritual, self._valueOf(exception))

  @overload(QXmlParseException)
  def error(self, exception: QXmlParseException) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::error(const QXmlParseException
    &exception)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#error

    Parameters
    ----------

    exception : QXmlParseException
      Passed on as a value: Qt reads the C++ QXmlParseException, which stays
      Python's own.
    """
    #  bool QXmlDefaultHandler::error(const QXmlParseException &exception)
    ritual = 'ritual_ZN18QXmlDefaultHandler5errorERK18QXmlParseException'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler5errorERK18QXmlParseException')
    return self.uglySide.call(ritual, self._valueOf(exception))

  @overload(QXmlParseException)
  def fatalError(self, exception: QXmlParseException) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::fatalError(const QXmlParseException
    &exception)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#fatalError

    Parameters
    ----------

    exception : QXmlParseException
      Passed on as a value: Qt reads the C++ QXmlParseException, which stays
      Python's own.
    """
    #  bool QXmlDefaultHandler::fatalError(const QXmlParseException
    #      &exception)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler10fatalErrorERK18QXmlParseException')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler10fatalErrorERK18QXmlParseExcep'
          'tion')
    return self.uglySide.call(ritual, self._valueOf(exception))

  @overload(str, str, str)
  def notationDecl(self, name: str, publicId: str, systemId: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::notationDecl(const QString &name,
    const QString &publicId, const QString &systemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#notationDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::notationDecl(const QString &name, const
    #      QString &publicId, const QString &systemId)
    ritual = 'ritual_ZN18QXmlDefaultHandler12notationDeclERK7QStringS2_S2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler12notationDeclERK7QStringS2_S2_')
    return self.uglySide.call(ritual, name, publicId, systemId)

  @overload(str, str, str, str)
  def unparsedEntityDecl(
      self,
      name: str,
      publicId: str,
      systemId: str,
      notationName: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::unparsedEntityDecl(const QString
    &name, const QString &publicId, const QString &systemId, const QString
    &notationName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#unparsedEntityDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.

    notationName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::unparsedEntityDecl(const QString &name, const
    #      QString &publicId, const QString &systemId, const QString
    #      &notationName)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler18unparsedEntityDeclERK7QStringS2_S2_'
        'S2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler18unparsedEntityDeclERK7QString'
          'S2_S2_S2_')
    return self.uglySide.call(ritual, name, publicId, systemId, notationName)

  @overload(str, str, str)
  def startDTD(self, name: str, publicId: str, systemId: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::startDTD(const QString &name, const
    QString &publicId, const QString &systemId)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#startDTD

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::startDTD(const QString &name, const QString
    #      &publicId, const QString &systemId)
    ritual = 'ritual_ZN18QXmlDefaultHandler8startDTDERK7QStringS2_S2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler8startDTDERK7QStringS2_S2_'
    return self.uglySide.call(ritual, name, publicId, systemId)

  def endDTD(self) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::endDTD()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#endDTD
    """
    #  bool QXmlDefaultHandler::endDTD()
    ritual = 'ritual_ZN18QXmlDefaultHandler6endDTDEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler6endDTDEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def startEntity(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::startEntity(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#startEntity

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::startEntity(const QString &name)
    ritual = 'ritual_ZN18QXmlDefaultHandler11startEntityERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler11startEntityERK7QString'
    return self.uglySide.call(ritual, name)

  @overload(str)
  def endEntity(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::endEntity(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#endEntity

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::endEntity(const QString &name)
    ritual = 'ritual_ZN18QXmlDefaultHandler9endEntityERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler9endEntityERK7QString'
    return self.uglySide.call(ritual, name)

  def startCDATA(self) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::startCDATA()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#startCDATA
    """
    #  bool QXmlDefaultHandler::startCDATA()
    ritual = 'ritual_ZN18QXmlDefaultHandler10startCDATAEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler10startCDATAEv'
    return self.uglySide.call(ritual)

  def endCDATA(self) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::endCDATA()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#endCDATA
    """
    #  bool QXmlDefaultHandler::endCDATA()
    ritual = 'ritual_ZN18QXmlDefaultHandler8endCDATAEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler8endCDATAEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def comment(self, ch: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::comment(const QString &ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmldefaulthandler.html#comment

    Parameters
    ----------

    ch : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::comment(const QString &ch)
    ritual = 'ritual_ZN18QXmlDefaultHandler7commentERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QXmlDefaultHandler7commentERK7QString'
    return self.uglySide.call(ritual, ch)

  @overload(str, str, str, str, str)
  def attributeDecl(
      self,
      eName: str,
      aName: str,
      type: str,
      valueDefault: str,
      value: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::attributeDecl(const QString &eName,
    const QString &aName, const QString &type, const QString &valueDefault,
    const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#attributeDecl

    Parameters
    ----------

    eName : str
      Passed on as it is: a QString is made of it for the call.

    aName : str
      Passed on as it is: a QString is made of it for the call.

    type : str
      Passed on as it is: a QString is made of it for the call.

    valueDefault : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::attributeDecl(const QString &eName, const
    #      QString &aName, const QString &type, const QString &valueDefault,
    #      const QString &value)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler13attributeDeclERK7QStringS2_S2_S2_S2'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler13attributeDeclERK7QStringS2_S2'
          '_S2_S2_')
    return self.uglySide.call(
        ritual, eName, aName, type, valueDefault, value,
    )

  @overload(str, str)
  def internalEntityDecl(self, name: str, value: str) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::internalEntityDecl(const QString
    &name, const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#internalEntityDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::internalEntityDecl(const QString &name, const
    #      QString &value)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler18internalEntityDeclERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler18internalEntityDeclERK7QString'
          'S2_')
    return self.uglySide.call(ritual, name, value)

  @overload(str, str, str)
  def externalEntityDecl(
      self,
      name: str,
      publicId: str,
      systemId: str,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlDefaultHandler::externalEntityDecl(const QString
    &name, const QString &publicId, const QString &systemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmldefaulthandler.html#externalEntityDecl

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlDefaultHandler::externalEntityDecl(const QString &name, const
    #      QString &publicId, const QString &systemId)
    ritual = (
        'ritual_ZN18QXmlDefaultHandler18externalEntityDeclERK7QStringS2_S2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QXmlDefaultHandler18externalEntityDeclERK7QString'
          'S2_S2_')
    return self.uglySide.call(ritual, name, publicId, systemId)
