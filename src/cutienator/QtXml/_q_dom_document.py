"""
QDomDocument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from . import QDomNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QXmlStreamReader
  from . import QDomAttr, QDomCDATASection, QDomComment, QDomDocumentFragment
  from . import QDomDocumentPrivate, QDomDocumentType, QDomElement
  from . import QDomEntityReference, QDomImplementation, QDomNodeList
  from . import QDomProcessingInstruction, QDomText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDomDocumentPrivate = WAIT['QDomDocumentPrivate']
  QDomDocumentType = WAIT['QDomDocumentType']
  QIODevice = WAIT['QIODevice']
  QXmlStreamReader = WAIT['QXmlStreamReader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomDocument(QDomNode):
  """
  The cute side of Qt's QDomDocument: a plain Python object standing in front
  of one C++ QDomDocument.

  It is built on the cute 'QDomNode', as Qt's QDomDocument is built on Qt's
  QDomNode, and has everything that class has.

  C++ hands a QDomDocument around as a copy, so every C++ QDomDocument behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomDocument that has a ritual and that Python can
  call so far, 22 names in all: 'createElement', 'createDocumentFragment',
  'createTextNode', 'createComment', 'createCDATASection',
  'createProcessingInstruction', 'createAttribute', 'createEntityReference',
  'elementsByTagName', 'importNode', 'createElementNS', 'createAttributeNS',
  'elementsByTagNameNS', 'elementById', 'doctype', 'implementation',
  'documentElement', 'nodeType', 'setContent', 'toString', 'toByteArray',
  'setContentImpl'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomDocument &QDomDocument::operator=(const QDomDocument &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDomDocument::~QDomDocument()': the destructor: Python removes its
    C++ QDomDocument by it, and has no other use for it.
  - Qt's 'bool QDomDocument::setContent(const QByteArray &text, bool
    namespaceProcessing, QString *errorMsg, int *errorLine, int
    *errorColumn)': takes a number to change where it is.
  - Qt's 'bool QDomDocument::setContent(const QString &text, bool
    namespaceProcessing, QString *errorMsg, int *errorLine, int
    *errorColumn)': takes a number to change where it is.
  - Qt's 'bool QDomDocument::setContent(QIODevice *dev, bool
    namespaceProcessing, QString *errorMsg, int *errorLine, int
    *errorColumn)': takes a number to change where it is.
  - Qt's 'bool QDomDocument::setContent(const QByteArray &text, QString
    *errorMsg, int *errorLine, int *errorColumn)': takes a number to change
    where it is.
  - Qt's 'bool QDomDocument::setContent(const QString &text, QString
    *errorMsg, int *errorLine, int *errorColumn)': takes a number to change
    where it is.
  - Qt's 'bool QDomDocument::setContent(QIODevice *dev, QString *errorMsg,
    int *errorLine, int *errorColumn)': takes a number to change where it is.
  - Qt's 'bool QDomDocument::setContent(QXmlStreamReader *reader, bool
    namespaceProcessing, QString *errorMsg, int *errorLine, int
    *errorColumn)': takes a number to change where it is.

  What has no ritual
  ------------------

  1 of the 39 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QDomDocument is created at the first use, not by
    'QDomDocument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomDocument back gives a copy the ritual made for
    Python, in a new cute QDomDocument.
  """

  #  The enums Qt writes inside QDomDocument, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ParseOption(CuteFlags, scoped=True):
    """
    The flags enum 'QDomDocument::ParseOption' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QDomDocument::ParseOptions'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    Default = 0x0
    UseNamespaceProcessing = 0x1
    PreserveSpacingOnlyNodes = 0x2

  ParseOptions = ParseOption

  #  The classes Qt writes inside QDomDocument, each a class in here as in
  #  C++.

  class ParseResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDomDocument::ParseResult: a plain Python object
    standing in front of one C++ QDomDocument::ParseResult.

    C++ hands a QDomDocument::ParseResult around as a copy, so every C++
    QDomDocument::ParseResult behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDomDocument::ParseResult that has a ritual and
    that Python can call so far, 1 name in all: '__bool__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDomDocument::ParseResult::~ParseResult()': the destructor:
      Python removes its C++ QDomDocument::ParseResult by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QDomDocument::ParseResult is created at the first use, not by
      'QDomDocument::ParseResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDomDocument::ParseResult back gives a copy the
      ritual made for Python, in a new cute QDomDocument::ParseResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDomDocument::ParseResult'

    #  Qt's '~QDomDocument::ParseResult()'. Naming it makes this a value
    #  class: Python owns every C++ QDomDocument::ParseResult behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QDomDocument11ParseResultD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def __bool__(self) -> bool:
      """
      Calls Qt's 'bool QDomDocument::ParseResult::operator bool() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdomdocument-parseresult.html#operator bool
      """
      #  bool QDomDocument::ParseResult::operator bool() const
      return self.uglySide.call('ritual_ZNK12QDomDocument11ParseResultcvbEv')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomDocument'

  #  Qt's '~QDomDocument()'. Naming it makes this a value class: Python owns
  #  every C++ QDomDocument behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QDomDocumentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def elementsByTagName(self, tagname: str) -> QDomNodeList:
    """
    Calls Qt's 'QDomNodeList QDomDocument::elementsByTagName(const QString
    &tagname) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocument.html#elementsByTagName

    Parameters
    ----------

    tagname : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNodeList
      A new cute QDomNodeList around the copy Qt gave back. Python owns it.
    """
    #  QDomNodeList QDomDocument::elementsByTagName(const QString &tagname)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QDomDocument17elementsByTagNameERK7QString', tagname,
    )
    from . import QDomNodeList
    return QDomNodeList._cuteOwning(address)

  def doctype(self) -> QDomDocumentType:
    """
    Calls Qt's 'QDomDocumentType QDomDocument::doctype() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#doctype

    Returns
    -------

    QDomDocumentType
      A new cute QDomDocumentType around the copy Qt gave back. Python owns
      it.
    """
    #  QDomDocumentType QDomDocument::doctype() const
    address = self.uglySide.call('ritual_ZNK12QDomDocument7doctypeEv')
    from . import QDomDocumentType
    return QDomDocumentType._cuteOwning(address)

  def implementation(self) -> QDomImplementation:
    """
    Calls Qt's 'QDomImplementation QDomDocument::implementation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#implementation

    Returns
    -------

    QDomImplementation
      A new cute QDomImplementation around the copy Qt gave back. Python owns
      it.
    """
    #  QDomImplementation QDomDocument::implementation() const
    address = self.uglySide.call(
        'ritual_ZNK12QDomDocument14implementationEv',
    )
    from . import QDomImplementation
    return QDomImplementation._cuteOwning(address)

  def documentElement(self) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomDocument::documentElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#documentElement

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomDocument::documentElement() const
    address = self.uglySide.call(
        'ritual_ZNK12QDomDocument15documentElementEv',
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomDocument::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomDocument::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK12QDomDocument8nodeTypeEv',
    ))

  @overload()
  @overload(int)
  def toString(self, indent: int = 1) -> str:
    """
    Calls Qt's 'QString QDomDocument::toString(int indent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#toString

    Parameters
    ----------

    indent : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomDocument::toString(int indent) const
    return self.uglySide.call('ritual_ZNK12QDomDocument8toStringEi', indent)

  @overload()
  @overload(int)
  def toByteArray(self, indent: int = 1) -> QByteArray:
    """
    Calls Qt's 'QByteArray QDomDocument::toByteArray(int indent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#toByteArray

    Parameters
    ----------

    indent : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDomDocument::toByteArray(int indent) const
    address = self.uglySide.call(
        'ritual_ZNK12QDomDocument11toByteArrayEi', indent,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, ParseOptions)
  def setContent(
      self,
      data: str,
      options: ParseOptions = ParseOptions.Default,
  ) -> ParseResult:
    """
    Calls Qt's 'ParseResult QDomDocument::setContent(QAnyStringView data,
    ParseOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#setContent

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    options : ParseOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ParseOptions.Default.

    Returns
    -------

    ParseResult
      A new cute QDomDocument::ParseResult around the copy Qt gave back.
      Python owns it.
    """
    #  ParseResult QDomDocument::setContent(QAnyStringView data, ParseOptions
    #      options)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument10setContentE14QAnyStringView6QFlagsINS_11P'
        'arseOptionEE',
        data, options.value,
    )
    return QDomDocument.ParseResult._cuteOwning(address)

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, ParseOptions)
  @overload(NoneType, ParseOptions)
  def setContent(
      self,
      device: Optional[QIODevice],
      options: ParseOptions = ParseOptions.Default,
  ) -> ParseResult:
    """
    Calls Qt's 'ParseResult QDomDocument::setContent(QIODevice *device,
    ParseOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#setContent

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : ParseOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ParseOptions.Default.

    Returns
    -------

    ParseResult
      A new cute QDomDocument::ParseResult around the copy Qt gave back.
      Python owns it.
    """
    #  ParseResult QDomDocument::setContent(QIODevice *device, ParseOptions
    #      options)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument10setContentEP9QIODevice6QFlagsINS_11ParseO'
        'ptionEE',
        self._addressOf(device), options.value,
    )
    return QDomDocument.ParseResult._cuteOwning(address)

  @overload(QXmlStreamReader)
  @overload(QXmlStreamReader, ParseOptions)
  def setContent(
      self,
      reader: Optional[QXmlStreamReader],
      options: ParseOptions = ParseOptions.Default,
  ) -> ParseResult:
    """
    Calls Qt's 'ParseResult QDomDocument::setContent(QXmlStreamReader
    *reader, ParseOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#setContent

    Parameters
    ----------

    reader : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : ParseOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ParseOptions.Default.

    Returns
    -------

    ParseResult
      A new cute QDomDocument::ParseResult around the copy Qt gave back.
      Python owns it.
    """
    #  ParseResult QDomDocument::setContent(QXmlStreamReader *reader,
    #      ParseOptions options)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument10setContentEP16QXmlStreamReader6QFlagsINS_'
        '11ParseOptionEE',
        self._addressOf(reader), options.value,
    )
    return QDomDocument.ParseResult._cuteOwning(address)

  @overload(QByteArray, ParseOptions)
  def setContentImpl(
      self,
      data: QByteArray,
      options: ParseOptions,
  ) -> ParseResult:
    """
    Calls Qt's 'ParseResult QDomDocument::setContentImpl(const QByteArray
    &data, ParseOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#setContentImpl

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    options : ParseOptions
      Passed on as its number.

    Returns
    -------

    ParseResult
      A new cute QDomDocument::ParseResult around the copy Qt gave back.
      Python owns it.
    """
    #  ParseResult QDomDocument::setContentImpl(const QByteArray &data,
    #      ParseOptions options)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument14setContentImplERK10QByteArray6QFlagsINS_1'
        '1ParseOptionEE',
        self._valueOf(data), options.value,
    )
    return QDomDocument.ParseResult._cuteOwning(address)

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
    Notes what was given, for Qt's 'QDomDocument::QDomDocument()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#QDomDocument
    """
    #  QDomDocument::QDomDocument()
    self._noteCreation(QDomDocument, lambda: Rituals.call(
        'ritual_ZN12QDomDocumentC1Ev',
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QDomDocument::QDomDocument(const QString
    &name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#QDomDocument

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QDomDocument::QDomDocument(const QString &name)
    self._noteCreation(QDomDocument, lambda: Rituals.call(
        'ritual_ZN12QDomDocumentC1ERK7QString', name,
    ))

  @overload(QDomDocumentType)
  def __init__(self, doctype: QDomDocumentType) -> None:
    """
    Notes what was given, for Qt's 'QDomDocument::QDomDocument(const
    QDomDocumentType &doctype)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#QDomDocument

    Parameters
    ----------

    doctype : QDomDocumentType
      Passed on as a value: Qt reads the C++ QDomDocumentType, which stays
      Python's own.
    """
    #  QDomDocument::QDomDocument(const QDomDocumentType &doctype)
    self._noteCreation(QDomDocument, lambda: Rituals.call(
        'ritual_ZN12QDomDocumentC1ERK16QDomDocumentType',
        self._valueOf(doctype),
    ))

  @overload(THIS)
  def __init__(self, document: QDomDocument) -> None:
    """
    Notes what was given, for Qt's 'QDomDocument::QDomDocument(const
    QDomDocument &document)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#QDomDocument

    Parameters
    ----------

    document : QDomDocument
      Passed on as a value: Qt reads the C++ QDomDocument, which stays
      Python's own.
    """
    #  QDomDocument::QDomDocument(const QDomDocument &document)
    self._noteCreation(QDomDocument, lambda: Rituals.call(
        'ritual_ZN12QDomDocumentC1ERKS_', self._valueOf(document),
    ))

  @overload(QDomDocumentPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomDocumentPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomDocument::QDomDocument(QDomDocumentPrivate *a0)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#QDomDocument

    Parameters
    ----------

    a0 : Optional[QDomDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomDocument::QDomDocument(QDomDocumentPrivate *a0)
    self._noteCreation(QDomDocument, lambda: Rituals.call(
        'ritual_ZN12QDomDocumentC1EP19QDomDocumentPrivate',
        self._addressOf(a0),
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
  def createElement(self, tagName: str) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomDocument::createElement(const QString
    &tagName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#createElement

    Parameters
    ----------

    tagName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomDocument::createElement(const QString &tagName)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument13createElementERK7QString', tagName,
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  def createDocumentFragment(self) -> QDomDocumentFragment:
    """
    Calls Qt's 'QDomDocumentFragment QDomDocument::createDocumentFragment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocument.html#createDocumentFragment

    Returns
    -------

    QDomDocumentFragment
      A new cute QDomDocumentFragment around the copy Qt gave back. Python
      owns it.
    """
    #  QDomDocumentFragment QDomDocument::createDocumentFragment()
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument22createDocumentFragmentEv',
    )
    from . import QDomDocumentFragment
    return QDomDocumentFragment._cuteOwning(address)

  @overload(str)
  def createTextNode(self, data: str) -> QDomText:
    """
    Calls Qt's 'QDomText QDomDocument::createTextNode(const QString &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#createTextNode

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomText
      A new cute QDomText around the copy Qt gave back. Python owns it.
    """
    #  QDomText QDomDocument::createTextNode(const QString &data)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument14createTextNodeERK7QString', data,
    )
    from . import QDomText
    return QDomText._cuteOwning(address)

  @overload(str)
  def createComment(self, data: str) -> QDomComment:
    """
    Calls Qt's 'QDomComment QDomDocument::createComment(const QString
    &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#createComment

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomComment
      A new cute QDomComment around the copy Qt gave back. Python owns it.
    """
    #  QDomComment QDomDocument::createComment(const QString &data)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument13createCommentERK7QString', data,
    )
    from . import QDomComment
    return QDomComment._cuteOwning(address)

  @overload(str)
  def createCDATASection(self, data: str) -> QDomCDATASection:
    """
    Calls Qt's 'QDomCDATASection QDomDocument::createCDATASection(const
    QString &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocument.html#createCDATASection

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomCDATASection
      A new cute QDomCDATASection around the copy Qt gave back. Python owns
      it.
    """
    #  QDomCDATASection QDomDocument::createCDATASection(const QString &data)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument18createCDATASectionERK7QString', data,
    )
    from . import QDomCDATASection
    return QDomCDATASection._cuteOwning(address)

  @overload(str, str)
  def createProcessingInstruction(
      self,
      target: str,
      data: str,
  ) -> QDomProcessingInstruction:
    """
    Calls Qt's 'QDomProcessingInstruction
    QDomDocument::createProcessingInstruction(const QString &target, const
    QString &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocument.html#createProcessingInstruction

    Parameters
    ----------

    target : str
      Passed on as it is: a QString is made of it for the call.

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomProcessingInstruction
      A new cute QDomProcessingInstruction around the copy Qt gave back.
      Python owns it.
    """
    #  QDomProcessingInstruction
    #      QDomDocument::createProcessingInstruction(const QString &target,
    #      const QString &data)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument27createProcessingInstructionERK7QStringS2_',
        target, data,
    )
    from . import QDomProcessingInstruction
    return QDomProcessingInstruction._cuteOwning(address)

  @overload(str)
  def createAttribute(self, name: str) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomDocument::createAttribute(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#createAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomDocument::createAttribute(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument15createAttributeERK7QString', name,
    )
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)

  @overload(str)
  def createEntityReference(self, name: str) -> QDomEntityReference:
    """
    Calls Qt's 'QDomEntityReference QDomDocument::createEntityReference(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocument.html#createEntityReference

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomEntityReference
      A new cute QDomEntityReference around the copy Qt gave back. Python
      owns it.
    """
    #  QDomEntityReference QDomDocument::createEntityReference(const QString
    #      &name)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument21createEntityReferenceERK7QString', name,
    )
    from . import QDomEntityReference
    return QDomEntityReference._cuteOwning(address)

  @overload(QDomNode, bool)
  def importNode(self, importedNode: QDomNode, deep: bool) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomDocument::importNode(const QDomNode
    &importedNode, bool deep)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#importNode

    Parameters
    ----------

    importedNode : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    deep : bool
      Passed on as it is.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomDocument::importNode(const QDomNode &importedNode, bool
    #      deep)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument10importNodeERK8QDomNodeb',
        self._valueOf(importedNode), deep,
    )
    return QDomNode._cuteOwning(address)

  @overload(str, str)
  def createElementNS(self, nsURI: str, qName: str) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomDocument::createElementNS(const QString
    &nsURI, const QString &qName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#createElementNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomDocument::createElementNS(const QString &nsURI, const
    #      QString &qName)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument15createElementNSERK7QStringS2_',
        nsURI, qName,
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  @overload(str, str)
  def createAttributeNS(self, nsURI: str, qName: str) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomDocument::createAttributeNS(const QString
    &nsURI, const QString &qName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocument.html#createAttributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomDocument::createAttributeNS(const QString &nsURI, const
    #      QString &qName)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument17createAttributeNSERK7QStringS2_',
        nsURI, qName,
    )
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)

  @overload(str, str)
  def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList:
    """
    Calls Qt's 'QDomNodeList QDomDocument::elementsByTagNameNS(const QString
    &nsURI, const QString &localName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocument.html#elementsByTagNameNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNodeList
      A new cute QDomNodeList around the copy Qt gave back. Python owns it.
    """
    #  QDomNodeList QDomDocument::elementsByTagNameNS(const QString &nsURI,
    #      const QString &localName)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument19elementsByTagNameNSERK7QStringS2_',
        nsURI, localName,
    )
    from . import QDomNodeList
    return QDomNodeList._cuteOwning(address)

  @overload(str)
  def elementById(self, elementId: str) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomDocument::elementById(const QString
    &elementId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocument.html#elementById

    Parameters
    ----------

    elementId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomDocument::elementById(const QString &elementId)
    address = self.uglySide.call(
        'ritual_ZN12QDomDocument11elementByIdERK7QString', elementId,
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)
