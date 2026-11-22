"""
QXmlStreamReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QIODevice, QXmlStreamAttributes, QXmlStreamEntityDeclaration
  from . import QXmlStreamEntityResolver, QXmlStreamNamespaceDeclaration
  from . import QXmlStreamNotationDeclaration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QXmlStreamEntityResolver = WAIT['QXmlStreamEntityResolver']
  QXmlStreamNamespaceDeclaration = WAIT['QXmlStreamNamespaceDeclaration']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlStreamReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamReader: a plain Python object standing in
  front of one C++ QXmlStreamReader.

  What exists
  -----------

  Every function of Qt's QXmlStreamReader that has a ritual and that Python
  can call so far, 56 names in all: 'setDevice', 'device', 'addData',
  'clear', 'atEnd', 'readNext', 'readNextStartElement', 'skipCurrentElement',
  'readRawInnerData', 'tokenType', 'tokenString', 'setNamespaceProcessing',
  'namespaceProcessing', 'isStartDocument', 'isEndDocument',
  'isStartElement', 'isEndElement', 'isCharacters', 'isWhitespace',
  'isCDATA', 'isComment', 'isDTD', 'isEntityReference',
  'isProcessingInstruction', 'isStandaloneDocument',
  'hasStandaloneDeclaration', 'documentVersion', 'documentEncoding',
  'lineNumber', 'columnNumber', 'characterOffset', 'attributes',
  'readElementText', 'name', 'namespaceUri', 'qualifiedName', 'prefix',
  'processingInstructionTarget', 'processingInstructionData', 'text',
  'namespaceDeclarations', 'addExtraNamespaceDeclaration',
  'addExtraNamespaceDeclarations', 'notationDeclarations',
  'entityDeclarations', 'dtdName', 'dtdPublicId', 'dtdSystemId',
  'entityExpansionLimit', 'setEntityExpansionLimit', 'raiseError',
  'errorString', 'error', 'hasError', 'setEntityResolver', 'entityResolver'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamReader::~QXmlStreamReader()': the destructor: Python
    never removes a C++ QXmlStreamReader.

  What has no ritual
  ------------------

  8 of the 68 functions Qt declares: 4 private; 2 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QXmlStreamReader is created at the first use, not by
    'QXmlStreamReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlStreamReader.
  """

  #  The enums Qt writes inside QXmlStreamReader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QXmlStreamReader::Error' of Qt, with the 5 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    UnexpectedElementError = Kee[int](1)
    CustomError = Kee[int](2)
    NotWellFormedError = Kee[int](3)
    PrematureEndOfDocumentError = Kee[int](4)

  class ReadElementTextBehaviour(CuteNum):
    """
    The enum 'QXmlStreamReader::ReadElementTextBehaviour' of Qt, with the 3
    names Qt gives in it.
    """

    ErrorOnUnexpectedElement = Kee[int](0)
    IncludeChildElements = Kee[int](1)
    SkipChildElements = Kee[int](2)

  class TokenType(CuteNum):
    """
    The enum 'QXmlStreamReader::TokenType' of Qt, with the 11 names Qt gives
    in it.
    """

    NoToken = Kee[int](0)
    Invalid = Kee[int](1)
    StartDocument = Kee[int](2)
    EndDocument = Kee[int](3)
    StartElement = Kee[int](4)
    EndElement = Kee[int](5)
    Characters = Kee[int](6)
    Comment = Kee[int](7)
    DTD = Kee[int](8)
    EntityReference = Kee[int](9)
    ProcessingInstruction = Kee[int](10)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QXmlStreamReader::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QXmlStreamReader::device() const
    address = self.uglySide.call('ritual_ZNK16QXmlStreamReader6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#atEnd
    """
    #  bool QXmlStreamReader::atEnd() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader5atEndEv')

  def tokenType(self) -> TokenType:
    """
    Calls Qt's 'TokenType QXmlStreamReader::tokenType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#tokenType

    Returns
    -------

    TokenType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TokenType(number)' gives.
    """
    #  TokenType QXmlStreamReader::tokenType() const
    return QXmlStreamReader.TokenType(self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader9tokenTypeEv',
    ))

  def tokenString(self) -> str:
    """
    Calls Qt's 'QString QXmlStreamReader::tokenString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#tokenString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamReader::tokenString() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader11tokenStringEv')

  def namespaceProcessing(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::namespaceProcessing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#namespaceProcessing
    """
    #  bool QXmlStreamReader::namespaceProcessing() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader19namespaceProcessingEv',
    )

  def isStartDocument(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isStartDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#isStartDocument
    """
    #  bool QXmlStreamReader::isStartDocument() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader15isStartDocumentEv',
    )

  def isEndDocument(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isEndDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#isEndDocument
    """
    #  bool QXmlStreamReader::isEndDocument() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader13isEndDocumentEv',
    )

  def isStartElement(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isStartElement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#isStartElement
    """
    #  bool QXmlStreamReader::isStartElement() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader14isStartElementEv',
    )

  def isEndElement(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isEndElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#isEndElement
    """
    #  bool QXmlStreamReader::isEndElement() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader12isEndElementEv')

  def isCharacters(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isCharacters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#isCharacters
    """
    #  bool QXmlStreamReader::isCharacters() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader12isCharactersEv')

  def isWhitespace(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isWhitespace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#isWhitespace
    """
    #  bool QXmlStreamReader::isWhitespace() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader12isWhitespaceEv')

  def isCDATA(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isCDATA() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#isCDATA
    """
    #  bool QXmlStreamReader::isCDATA() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader7isCDATAEv')

  def isComment(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#isComment
    """
    #  bool QXmlStreamReader::isComment() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader9isCommentEv')

  def isDTD(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isDTD() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#isDTD
    """
    #  bool QXmlStreamReader::isDTD() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader5isDTDEv')

  def isEntityReference(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isEntityReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#isEntityReference
    """
    #  bool QXmlStreamReader::isEntityReference() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader17isEntityReferenceEv',
    )

  def isProcessingInstruction(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isProcessingInstruction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#isProcessingInstruction
    """
    #  bool QXmlStreamReader::isProcessingInstruction() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader23isProcessingInstructionEv',
    )

  def isStandaloneDocument(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::isStandaloneDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#isStandaloneDocument
    """
    #  bool QXmlStreamReader::isStandaloneDocument() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader20isStandaloneDocumentEv',
    )

  def hasStandaloneDeclaration(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::hasStandaloneDeclaration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#hasStandaloneDeclaration
    """
    #  bool QXmlStreamReader::hasStandaloneDeclaration() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader24hasStandaloneDeclarationEv',
    )

  def documentVersion(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::documentVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#documentVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::documentVersion() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader15documentVersionEv',
    )

  def documentEncoding(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::documentEncoding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#documentEncoding

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::documentEncoding() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader16documentEncodingEv',
    )

  def lineNumber(self) -> int:
    """
    Calls Qt's 'qint64 QXmlStreamReader::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#lineNumber
    """
    #  qint64 QXmlStreamReader::lineNumber() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader10lineNumberEv')

  def columnNumber(self) -> int:
    """
    Calls Qt's 'qint64 QXmlStreamReader::columnNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#columnNumber
    """
    #  qint64 QXmlStreamReader::columnNumber() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader12columnNumberEv')

  def characterOffset(self) -> int:
    """
    Calls Qt's 'qint64 QXmlStreamReader::characterOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#characterOffset
    """
    #  qint64 QXmlStreamReader::characterOffset() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader15characterOffsetEv',
    )

  def attributes(self) -> QXmlStreamAttributes:
    """
    Calls Qt's 'QXmlStreamAttributes QXmlStreamReader::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#attributes

    Returns
    -------

    QXmlStreamAttributes
      A new cute QXmlStreamAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  QXmlStreamAttributes QXmlStreamReader::attributes() const
    address = self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader10attributesEv',
    )
    from . import QXmlStreamAttributes
    return QXmlStreamAttributes._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::name() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader4nameEv')

  def namespaceUri(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::namespaceUri() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#namespaceUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::namespaceUri() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader12namespaceUriEv')

  def qualifiedName(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::qualifiedName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#qualifiedName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::qualifiedName() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader13qualifiedNameEv',
    )

  def prefix(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::prefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#prefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::prefix() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader6prefixEv')

  def processingInstructionTarget(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::processingInstructionTarget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#processingInstructionTarget

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::processingInstructionTarget() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader27processingInstructionTargetEv',
    )

  def processingInstructionData(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::processingInstructionData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#processingInstructionData

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::processingInstructionData() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader25processingInstructionDataEv',
    )

  def text(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::text() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader4textEv')

  def namespaceDeclarations(self) -> QList[QXmlStreamNamespaceDeclaration]:
    """
    Calls Qt's 'QXmlStreamNamespaceDeclarations
    QXmlStreamReader::namespaceDeclarations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#namespaceDeclarations

    Returns
    -------

    QList[QXmlStreamNamespaceDeclaration]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QXmlStreamNamespaceDeclarations
    #      QXmlStreamReader::namespaceDeclarations() const
    address = self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader21namespaceDeclarationsEv',
    )
    from . import QXmlStreamNamespaceDeclaration
    return QList[QXmlStreamNamespaceDeclaration]._cuteOwning(address)

  def notationDeclarations(self) -> QList[QXmlStreamNotationDeclaration]:
    """
    Calls Qt's 'QXmlStreamNotationDeclarations
    QXmlStreamReader::notationDeclarations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#notationDeclarations

    Returns
    -------

    QList[QXmlStreamNotationDeclaration]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QXmlStreamNotationDeclarations
    #      QXmlStreamReader::notationDeclarations() const
    address = self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader20notationDeclarationsEv',
    )
    from . import QXmlStreamNotationDeclaration
    return QList[QXmlStreamNotationDeclaration]._cuteOwning(address)

  def entityDeclarations(self) -> QList[QXmlStreamEntityDeclaration]:
    """
    Calls Qt's 'QXmlStreamEntityDeclarations
    QXmlStreamReader::entityDeclarations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#entityDeclarations

    Returns
    -------

    QList[QXmlStreamEntityDeclaration]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QXmlStreamEntityDeclarations QXmlStreamReader::entityDeclarations()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader18entityDeclarationsEv',
    )
    from . import QXmlStreamEntityDeclaration
    return QList[QXmlStreamEntityDeclaration]._cuteOwning(address)

  def dtdName(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::dtdName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#dtdName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::dtdName() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader7dtdNameEv')

  def dtdPublicId(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::dtdPublicId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#dtdPublicId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::dtdPublicId() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader11dtdPublicIdEv')

  def dtdSystemId(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReader::dtdSystemId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#dtdSystemId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReader::dtdSystemId() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader11dtdSystemIdEv')

  def entityExpansionLimit(self) -> int:
    """
    Calls Qt's 'int QXmlStreamReader::entityExpansionLimit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#entityExpansionLimit
    """
    #  int QXmlStreamReader::entityExpansionLimit() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader20entityExpansionLimitEv',
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QXmlStreamReader::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamReader::errorString() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader11errorStringEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QXmlStreamReader::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QXmlStreamReader::error() const
    return QXmlStreamReader.Error(self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader5errorEv',
    ))

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#hasError
    """
    #  bool QXmlStreamReader::hasError() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamReader8hasErrorEv')

  def entityResolver(self) -> Optional[QXmlStreamEntityResolver]:
    """
    Calls Qt's 'QXmlStreamEntityResolver *QXmlStreamReader::entityResolver()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#entityResolver

    Returns
    -------

    Optional[QXmlStreamEntityResolver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlStreamEntityResolver *QXmlStreamReader::entityResolver() const
    address = self.uglySide.call(
        'ritual_ZNK16QXmlStreamReader14entityResolverEv',
    )
    from . import QXmlStreamEntityResolver
    return QXmlStreamEntityResolver._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlStreamReader::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader9setDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(bool)
  def setNamespaceProcessing(self, a0: bool) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::setNamespaceProcessing(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#setNamespaceProcessing

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QXmlStreamReader::setNamespaceProcessing(bool a0)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader22setNamespaceProcessingEb', a0,
    )

  @overload(int)
  def setEntityExpansionLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::setEntityExpansionLimit(int limit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#setEntityExpansionLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QXmlStreamReader::setEntityExpansionLimit(int limit)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader23setEntityExpansionLimitEi', limit,
    )

  @overload(QXmlStreamEntityResolver)
  @overload(NoneType)
  def setEntityResolver(
      self,
      resolver: Optional[QXmlStreamEntityResolver],
  ) -> None:
    """
    Calls Qt's 'void
    QXmlStreamReader::setEntityResolver(QXmlStreamEntityResolver *resolver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#setEntityResolver

    Parameters
    ----------

    resolver : Optional[QXmlStreamEntityResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlStreamReader::setEntityResolver(QXmlStreamEntityResolver
    #      *resolver)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader17setEntityResolverEP24QXmlStreamEntity'
        'Resolver',
        self._addressOf(resolver),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QXmlStreamReader::QXmlStreamReader()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#QXmlStreamReader
    """
    #  QXmlStreamReader::QXmlStreamReader()
    self._noteCreation(QXmlStreamReader, lambda: Rituals.call(
        'ritual_ZN16QXmlStreamReaderC1Ev',
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamReader::QXmlStreamReader(QIODevice *device)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#QXmlStreamReader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXmlStreamReader::QXmlStreamReader(QIODevice *device)
    self._noteCreation(QXmlStreamReader, lambda: Rituals.call(
        'ritual_ZN16QXmlStreamReaderC1EP9QIODevice', self._addressOf(device),
    ))

  @overload(str)
  def __init__(self, data: str) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamReader::QXmlStreamReader(QAnyStringView data)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#QXmlStreamReader

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QXmlStreamReader::QXmlStreamReader(QAnyStringView data)
    self._noteCreation(QXmlStreamReader, lambda: Rituals.call(
        'ritual_ZN16QXmlStreamReaderC1E14QAnyStringView', data,
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

  @overload(str)
  def addData(self, data: str) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::addData(QAnyStringView data)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#addData

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamReader::addData(QAnyStringView data)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader7addDataE14QAnyStringView', data,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#clear
    """
    #  void QXmlStreamReader::clear()
    self.uglySide.call('ritual_ZN16QXmlStreamReader5clearEv')

  def readNext(self) -> TokenType:
    """
    Calls Qt's 'TokenType QXmlStreamReader::readNext()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#readNext

    Returns
    -------

    TokenType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TokenType(number)' gives.
    """
    #  TokenType QXmlStreamReader::readNext()
    return QXmlStreamReader.TokenType(self.uglySide.call(
        'ritual_ZN16QXmlStreamReader8readNextEv',
    ))

  def readNextStartElement(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReader::readNextStartElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#readNextStartElement
    """
    #  bool QXmlStreamReader::readNextStartElement()
    return self.uglySide.call(
        'ritual_ZN16QXmlStreamReader20readNextStartElementEv',
    )

  def skipCurrentElement(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::skipCurrentElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#skipCurrentElement
    """
    #  void QXmlStreamReader::skipCurrentElement()
    self.uglySide.call('ritual_ZN16QXmlStreamReader18skipCurrentElementEv')

  def readRawInnerData(self) -> str:
    """
    Calls Qt's 'QString QXmlStreamReader::readRawInnerData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#readRawInnerData

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamReader::readRawInnerData()
    return self.uglySide.call(
        'ritual_ZN16QXmlStreamReader16readRawInnerDataEv',
    )

  @overload()
  @overload(ReadElementTextBehaviour)
  def readElementText(
      self,
      behaviour: ReadElementTextBehaviour = (
          ReadElementTextBehaviour.ErrorOnUnexpectedElement),
  ) -> str:
    """
    Calls Qt's 'QString
    QXmlStreamReader::readElementText(ReadElementTextBehaviour behaviour)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#readElementText

    Parameters
    ----------

    behaviour : ReadElementTextBehaviour
      Passed on as its number. May be left out, as in Qt: it is then
      ReadElementTextBehaviour.ErrorOnUnexpectedElement.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamReader::readElementText(ReadElementTextBehaviour
    #      behaviour)
    return self.uglySide.call(
        'ritual_ZN16QXmlStreamReader15readElementTextENS_24ReadElementTextB'
        'ehaviourE',
        behaviour.value,
    )

  @overload(QXmlStreamNamespaceDeclaration)
  def addExtraNamespaceDeclaration(
      self,
      extraNamespaceDeclaraction: QXmlStreamNamespaceDeclaration,
  ) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::addExtraNamespaceDeclaration(const
    QXmlStreamNamespaceDeclaration &extraNamespaceDeclaraction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html#addExtraNamespaceDeclaration

    Parameters
    ----------

    extraNamespaceDeclaraction : QXmlStreamNamespaceDeclaration
      Passed on as a value: Qt reads the C++ QXmlStreamNamespaceDeclaration,
      which stays Python's own.
    """
    #  void QXmlStreamReader::addExtraNamespaceDeclaration(const
    #      QXmlStreamNamespaceDeclaration &extraNamespaceDeclaraction)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader28addExtraNamespaceDeclarationERK30QXml'
        'StreamNamespaceDeclaration',
        self._valueOf(extraNamespaceDeclaraction),
    )

  @overload(QList[QXmlStreamNamespaceDeclaration])
  def addExtraNamespaceDeclarations(
      self,
      extraNamespaceDeclaractions: QList[QXmlStreamNamespaceDeclaration],
  ) -> None:
    """
    Calls Qt's 'void QXmlStreamReader::addExtraNamespaceDeclarations(const
    QXmlStreamNamespaceDeclarations &extraNamespaceDeclaractions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreader.html

    Parameters
    ----------

    extraNamespaceDeclaractions : QList[QXmlStreamNamespaceDeclaration]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QXmlStreamReader::addExtraNamespaceDeclarations(const
    #      QXmlStreamNamespaceDeclarations &extraNamespaceDeclaractions)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader29addExtraNamespaceDeclarationsERK5QLis'
        'tI30QXmlStreamNamespaceDeclarationE',
        self._valueOf(extraNamespaceDeclaractions),
    )

  @overload()
  @overload(str)
  def raiseError(self, message: str = '') -> None:
    """
    Calls Qt's 'void QXmlStreamReader::raiseError(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreader.html#raiseError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QXmlStreamReader::raiseError(const QString &message)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamReader10raiseErrorERK7QString', message,
    )
