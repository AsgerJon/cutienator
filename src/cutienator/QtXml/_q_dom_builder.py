"""
QDomBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdomhelpers_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QDomBuilder to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QDomDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QXmlStreamReader
  from . import QDomDocumentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomDocumentPrivate = WAIT['QDomDocumentPrivate']
  QXmlStreamReader = WAIT['QXmlStreamReader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomBuilder: a plain Python object standing in front
  of one C++ QDomBuilder.

  C++ hands a QDomBuilder around as a copy, so every C++ QDomBuilder behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomBuilder that has a ritual and that Python can
  call so far, 10 names in all: 'endDocument', 'endElement', 'startEntity',
  'endEntity', 'startDTD', 'parseDTD', 'fatalError', 'result',
  'preserveSpacingOnlyNodes', 'dtdInternalSubset'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomBuilder::~QDomBuilder()': the destructor: Python removes its
    C++ QDomBuilder by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 20 functions Qt declares: 4 leans on 'QDomNodePrivate; 3 leans on
  'QDomDocumentPrivate; 1 leans on 'QDomImplementationPrivate.

  What to expect
  --------------

  - The C++ QDomBuilder is created at the first use, not by
    'QDomBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomBuilder back gives a copy the ritual made for
    Python, in a new cute QDomBuilder.
  - Each name of Qt's QDomBuilder that has no cute function yet,
    'characters', 'comment', 'externalEntityDecl', 'notationDecl',
    'processingInstruction', 'skippedEntity', 'startElement',
    'unparsedEntityDecl', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomBuilder'

  #  Qt's '~QDomBuilder()'. Naming it makes this a value class: Python owns
  #  every C++ QDomBuilder behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QDomBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def result(self) -> QDomDocument.ParseResult:
    """
    Calls Qt's 'QDomDocument::ParseResult QDomBuilder::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#result

    Returns
    -------

    QDomDocument.ParseResult
      A new cute QDomDocument::ParseResult around the copy Qt gave back.
      Python owns it.
    """
    #  QDomDocument::ParseResult QDomBuilder::result() const
    address = self.uglySide.call('ritual_ZNK11QDomBuilder6resultEv')
    return QDomDocument.ParseResult._cuteOwning(address)

  def preserveSpacingOnlyNodes(self) -> bool:
    """
    Calls Qt's 'bool QDomBuilder::preserveSpacingOnlyNodes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdombuilder.html#preserveSpacingOnlyNodes
    """
    #  bool QDomBuilder::preserveSpacingOnlyNodes() const
    return self.uglySide.call(
        'ritual_ZNK11QDomBuilder24preserveSpacingOnlyNodesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDomDocumentPrivate, QXmlStreamReader, QDomDocument.ParseOptions)
  @overload(QDomDocumentPrivate, NoneType, QDomDocument.ParseOptions)
  @overload(NoneType, QXmlStreamReader, QDomDocument.ParseOptions)
  @overload(NoneType, NoneType, QDomDocument.ParseOptions)
  def __init__(
      self,
      d: Optional[QDomDocumentPrivate],
      r: Optional[QXmlStreamReader],
      options: QDomDocument.ParseOptions,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDomBuilder::QDomBuilder(QDomDocumentPrivate *d, QXmlStreamReader *r,
    QDomDocument::ParseOptions options)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#QDomBuilder

    Parameters
    ----------

    d : Optional[QDomDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : QDomDocument.ParseOptions
      Passed on as its number.
    """
    #  QDomBuilder::QDomBuilder(QDomDocumentPrivate *d, QXmlStreamReader *r,
    #      QDomDocument::ParseOptions options)
    self._noteCreation(QDomBuilder, lambda: Rituals.call(
        'ritual_ZN11QDomBuilderC1EP19QDomDocumentPrivateP16QXmlStreamReader'
        '6QFlagsIN12QDomDocument11ParseOptionEE',
        self._addressOf(d), self._addressOf(r), options.value,
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

  def endDocument(self) -> bool:
    """
    Calls Qt's 'bool QDomBuilder::endDocument()'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#endDocument
    """
    #  bool QDomBuilder::endDocument()
    return self.uglySide.call('ritual_ZN11QDomBuilder11endDocumentEv')

  def endElement(self) -> bool:
    """
    Calls Qt's 'bool QDomBuilder::endElement()'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#endElement
    """
    #  bool QDomBuilder::endElement()
    return self.uglySide.call('ritual_ZN11QDomBuilder10endElementEv')

  @overload(str)
  def startEntity(self, name: str) -> bool:
    """
    Calls Qt's 'bool QDomBuilder::startEntity(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#startEntity

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomBuilder::startEntity(const QString &name)
    return self.uglySide.call(
        'ritual_ZN11QDomBuilder11startEntityERK7QString', name,
    )

  def endEntity(self) -> bool:
    """
    Calls Qt's 'bool QDomBuilder::endEntity()'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#endEntity
    """
    #  bool QDomBuilder::endEntity()
    return self.uglySide.call('ritual_ZN11QDomBuilder9endEntityEv')

  @overload(str, str, str)
  def startDTD(self, name: str, publicId: str, systemId: str) -> bool:
    """
    Calls Qt's 'bool QDomBuilder::startDTD(const QString &name, const QString
    &publicId, const QString &systemId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#startDTD

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomBuilder::startDTD(const QString &name, const QString
    #      &publicId, const QString &systemId)
    return self.uglySide.call(
        'ritual_ZN11QDomBuilder8startDTDERK7QStringS2_S2_',
        name, publicId, systemId,
    )

  @overload(str)
  def parseDTD(self, dtd: str) -> bool:
    """
    Calls Qt's 'bool QDomBuilder::parseDTD(const QString &dtd)'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#parseDTD

    Parameters
    ----------

    dtd : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomBuilder::parseDTD(const QString &dtd)
    return self.uglySide.call(
        'ritual_ZN11QDomBuilder8parseDTDERK7QString', dtd,
    )

  @overload(str)
  def fatalError(self, message: str) -> None:
    """
    Calls Qt's 'void QDomBuilder::fatalError(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#fatalError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomBuilder::fatalError(const QString &message)
    self.uglySide.call(
        'ritual_ZN11QDomBuilder10fatalErrorERK7QString', message,
    )

  @overload(str)
  def dtdInternalSubset(self, dtd: str) -> str:
    """
    Calls Qt's 'QString QDomBuilder::dtdInternalSubset(const QString &dtd)'.

    Qt's own words: https://doc.qt.io/qt-6/qdombuilder.html#dtdInternalSubset

    Parameters
    ----------

    dtd : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomBuilder::dtdInternalSubset(const QString &dtd)
    return self.uglySide.call(
        'ritual_ZN11QDomBuilder17dtdInternalSubsetERK7QString', dtd,
    )

  @staticmethod
  def characters(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::characters(const QString &characters, bool
    cdata)': leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.characters' has no cute function yet. Qt's 'bool "
        "QDomBuilder::characters(const QString &characters, bool cdata)': "
        "leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def comment(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::comment(const QString &characters)': leans on
    'QDomImplementationPrivate::invalidDataPolicy', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.comment' has no cute function yet. Qt's 'bool "
        "QDomBuilder::comment(const QString &characters)': leans on "
        "'QDomImplementationPrivate::invalidDataPolicy', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def externalEntityDecl(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::externalEntityDecl(const QString &name, const
    QString &publicId, const QString &systemId)': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.externalEntityDecl' has no cute function yet. Qt's "
        "'bool QDomBuilder::externalEntityDecl(const QString &name, const "
        "QString &publicId, const QString &systemId)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def notationDecl(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::notationDecl(const QString &name, const QString
    &publicId, const QString &systemId)': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.notationDecl' has no cute function yet. Qt's 'bool "
        "QDomBuilder::notationDecl(const QString &name, const QString "
        "&publicId, const QString &systemId)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def processingInstruction(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::processingInstruction(const QString &target,
    const QString &data)': leans on
    'QDomDocumentPrivate::createProcessingInstruction(QString const&, QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.processingInstruction' has no cute function yet. Qt's "
        "'bool QDomBuilder::processingInstruction(const QString &target, "
        "const QString &data)': leans on "
        "'QDomDocumentPrivate::createProcessingInstruction(QString const&, "
        "QString const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def skippedEntity(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::skippedEntity(const QString &name)': leans on
    'QDomDocumentPrivate::createEntityReference(QString const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.skippedEntity' has no cute function yet. Qt's 'bool "
        "QDomBuilder::skippedEntity(const QString &name)': leans on "
        "'QDomDocumentPrivate::createEntityReference(QString const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def startElement(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::startElement(const QString &nsURI, const QString
    &qName, const QXmlStreamAttributes &atts)': leans on
    'QDomDocumentPrivate::createElementNS(QString const&, QString const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.startElement' has no cute function yet. Qt's 'bool "
        "QDomBuilder::startElement(const QString &nsURI, const QString "
        "&qName, const QXmlStreamAttributes &atts)': leans on "
        "'QDomDocumentPrivate::createElementNS(QString const&, QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def unparsedEntityDecl(*__, **_) -> Never:
    """
    Qt's 'bool QDomBuilder::unparsedEntityDecl(const QString &name, const
    QString &publicId, const QString &systemId, const QString
    &notationName)': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomBuilder.unparsedEntityDecl' has no cute function yet. Qt's "
        "'bool QDomBuilder::unparsedEntityDecl(const QString &name, const "
        "QString &publicId, const QString &systemId, const QString "
        "&notationName)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
