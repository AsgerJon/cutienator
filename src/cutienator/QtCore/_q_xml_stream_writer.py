"""
QXmlStreamWriter binding of the Qt C++
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

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIODevice, QString, QXmlStreamAttribute
  from . import QXmlStreamAttributes
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QString = WAIT['QString']
  QXmlStreamAttribute = WAIT['QXmlStreamAttribute']
  QXmlStreamAttributes = WAIT['QXmlStreamAttributes']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlStreamWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamWriter: a plain Python object standing in
  front of one C++ QXmlStreamWriter.

  What exists
  -----------

  Every function of Qt's QXmlStreamWriter that has a ritual and that Python
  can call so far, 28 names in all: 'setDevice', 'device',
  'setAutoFormatting', 'autoFormatting', 'setAutoFormattingIndent',
  'autoFormattingIndent', 'setStopWritingOnError', 'stopWritingOnError',
  'writeAttribute', 'writeAttributes', 'writeCDATA', 'writeCharacters',
  'writeComment', 'writeDTD', 'writeEmptyElement', 'writeTextElement',
  'writeEndDocument', 'writeEndElement', 'writeEntityReference',
  'writeNamespace', 'writeDefaultNamespace', 'writeProcessingInstruction',
  'writeStartDocument', 'writeStartElement', 'raiseError', 'errorString',
  'error', 'hasError'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamWriter::~QXmlStreamWriter()': the destructor: Python
    never removes a C++ QXmlStreamWriter.
  - Qt's 'void QXmlStreamWriter::writeCurrentToken(const QXmlStreamReader
    &reader)': takes a type Python has no way to hand over yet.
  - Qt's 'QXmlStreamWriterPrivate *QXmlStreamWriter::d_func()': gives
    'QXmlStreamWriterPrivate', which has no cute class yet.
  - Qt's 'const QXmlStreamWriterPrivate *QXmlStreamWriter::d_func() const':
    gives 'QXmlStreamWriterPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 45 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QXmlStreamWriter is created at the first use, not by
    'QXmlStreamWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlStreamWriter.
  - Each name of Qt's QXmlStreamWriter that has no cute function yet,
    'd_func', 'writeCurrentToken', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QXmlStreamWriter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QXmlStreamWriter::Error' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    IO = Kee[int](1)
    Encoding = Kee[int](2)
    InvalidCharacter = Kee[int](3)
    Custom = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamWriter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QXmlStreamWriter::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QXmlStreamWriter::device() const
    address = self.uglySide.call('ritual_ZNK16QXmlStreamWriter6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  def autoFormatting(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamWriter::autoFormatting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#autoFormatting
    """
    #  bool QXmlStreamWriter::autoFormatting() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamWriter14autoFormattingEv',
    )

  def autoFormattingIndent(self) -> int:
    """
    Calls Qt's 'int QXmlStreamWriter::autoFormattingIndent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#autoFormattingIndent
    """
    #  int QXmlStreamWriter::autoFormattingIndent() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamWriter20autoFormattingIndentEv',
    )

  def stopWritingOnError(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamWriter::stopWritingOnError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#stopWritingOnError
    """
    #  bool QXmlStreamWriter::stopWritingOnError() const
    return self.uglySide.call(
        'ritual_ZNK16QXmlStreamWriter18stopWritingOnErrorEv',
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QXmlStreamWriter::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamWriter::errorString() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamWriter11errorStringEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QXmlStreamWriter::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QXmlStreamWriter::error() const
    return QXmlStreamWriter.Error(self.uglySide.call(
        'ritual_ZNK16QXmlStreamWriter5errorEv',
    ))

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamWriter::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#hasError
    """
    #  bool QXmlStreamWriter::hasError() const
    return self.uglySide.call('ritual_ZNK16QXmlStreamWriter8hasErrorEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlStreamWriter::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter9setDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(bool)
  def setAutoFormatting(self, a0: bool) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::setAutoFormatting(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#setAutoFormatting

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QXmlStreamWriter::setAutoFormatting(bool a0)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter17setAutoFormattingEb', a0,
    )

  @overload(int)
  def setAutoFormattingIndent(self, spacesOrTabs: int) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::setAutoFormattingIndent(int
    spacesOrTabs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#setAutoFormattingIndent

    Parameters
    ----------

    spacesOrTabs : int
      Passed on as it is.
    """
    #  void QXmlStreamWriter::setAutoFormattingIndent(int spacesOrTabs)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter23setAutoFormattingIndentEi',
        spacesOrTabs,
    )

  @overload(bool)
  def setStopWritingOnError(self, stop: bool) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::setStopWritingOnError(bool stop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#setStopWritingOnError

    Parameters
    ----------

    stop : bool
      Passed on as it is.
    """
    #  void QXmlStreamWriter::setStopWritingOnError(bool stop)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter21setStopWritingOnErrorEb', stop,
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
    Notes what was given, for Qt's 'QXmlStreamWriter::QXmlStreamWriter()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#QXmlStreamWriter
    """
    #  QXmlStreamWriter::QXmlStreamWriter()
    self._noteCreation(QXmlStreamWriter, lambda: Rituals.call(
        'ritual_ZN16QXmlStreamWriterC1Ev',
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamWriter::QXmlStreamWriter(QIODevice *device)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#QXmlStreamWriter

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXmlStreamWriter::QXmlStreamWriter(QIODevice *device)
    self._noteCreation(QXmlStreamWriter, lambda: Rituals.call(
        'ritual_ZN16QXmlStreamWriterC1EP9QIODevice', self._addressOf(device),
    ))

  @overload(QByteArray)
  def __init__(self, array: Optional[QByteArray]) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamWriter::QXmlStreamWriter(QByteArray *array)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#QXmlStreamWriter

    Parameters
    ----------

    array : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXmlStreamWriter::QXmlStreamWriter(QByteArray *array)
    self._noteCreation(QXmlStreamWriter, lambda: Rituals.call(
        'ritual_ZN16QXmlStreamWriterC1EP10QByteArray',
        self._addressOf(array),
    ))

  @overload(QString)
  def __init__(self, string: Optional[QString]) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamWriter::QXmlStreamWriter(QString *string)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#QXmlStreamWriter

    Parameters
    ----------

    string : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXmlStreamWriter::QXmlStreamWriter(QString *string)
    self._noteCreation(QXmlStreamWriter, lambda: Rituals.call(
        'ritual_ZN16QXmlStreamWriterC1EP7QString', self._addressOf(string),
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

  @overload(str, str)
  def writeAttribute(self, qualifiedName: str, value: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeAttribute(QAnyStringView
    qualifiedName, QAnyStringView value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeAttribute

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeAttribute(QAnyStringView qualifiedName,
    #      QAnyStringView value)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter14writeAttributeE14QAnyStringViewS0_',
        qualifiedName, value,
    )

  @overload(str, str, str)
  def writeAttribute(self, namespaceUri: str, name: str, value: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeAttribute(QAnyStringView
    namespaceUri, QAnyStringView name, QAnyStringView value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeAttribute

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeAttribute(QAnyStringView namespaceUri,
    #      QAnyStringView name, QAnyStringView value)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter14writeAttributeE14QAnyStringViewS0_S0_',
        namespaceUri, name, value,
    )

  @overload(QXmlStreamAttribute)
  def writeAttribute(self, attribute: QXmlStreamAttribute) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeAttribute(const
    QXmlStreamAttribute &attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeAttribute

    Parameters
    ----------

    attribute : QXmlStreamAttribute
      Passed on as a value: Qt reads the C++ QXmlStreamAttribute, which stays
      Python's own.
    """
    #  void QXmlStreamWriter::writeAttribute(const QXmlStreamAttribute
    #      &attribute)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter14writeAttributeERK19QXmlStreamAttribut'
        'e',
        self._valueOf(attribute),
    )

  @overload(QXmlStreamAttributes)
  def writeAttributes(self, attributes: QXmlStreamAttributes) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeAttributes(const
    QXmlStreamAttributes &attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeAttributes

    Parameters
    ----------

    attributes : QXmlStreamAttributes
      Passed on as a value: Qt reads the C++ QXmlStreamAttributes, which
      stays Python's own.
    """
    #  void QXmlStreamWriter::writeAttributes(const QXmlStreamAttributes
    #      &attributes)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter15writeAttributesERK20QXmlStreamAttribu'
        'tes',
        self._valueOf(attributes),
    )

  @overload(str)
  def writeCDATA(self, text: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeCDATA(QAnyStringView text)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeCDATA

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeCDATA(QAnyStringView text)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter10writeCDATAE14QAnyStringView', text,
    )

  @overload(str)
  def writeCharacters(self, text: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeCharacters(QAnyStringView text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeCharacters

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeCharacters(QAnyStringView text)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter15writeCharactersE14QAnyStringView',
        text,
    )

  @overload(str)
  def writeComment(self, text: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeComment(QAnyStringView text)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeComment

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeComment(QAnyStringView text)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter12writeCommentE14QAnyStringView', text,
    )

  @overload(str)
  def writeDTD(self, dtd: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeDTD(QAnyStringView dtd)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeDTD

    Parameters
    ----------

    dtd : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeDTD(QAnyStringView dtd)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter8writeDTDE14QAnyStringView', dtd,
    )

  @overload(str)
  def writeEmptyElement(self, qualifiedName: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeEmptyElement(QAnyStringView
    qualifiedName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeEmptyElement

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeEmptyElement(QAnyStringView qualifiedName)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter17writeEmptyElementE14QAnyStringView',
        qualifiedName,
    )

  @overload(str, str)
  def writeEmptyElement(self, namespaceUri: str, name: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeEmptyElement(QAnyStringView
    namespaceUri, QAnyStringView name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeEmptyElement

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeEmptyElement(QAnyStringView namespaceUri,
    #      QAnyStringView name)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter17writeEmptyElementE14QAnyStringViewS0_',
        namespaceUri, name,
    )

  @overload(str, str)
  def writeTextElement(self, qualifiedName: str, text: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeTextElement(QAnyStringView
    qualifiedName, QAnyStringView text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeTextElement

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeTextElement(QAnyStringView qualifiedName,
    #      QAnyStringView text)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter16writeTextElementE14QAnyStringViewS0_',
        qualifiedName, text,
    )

  @overload(str, str, str)
  def writeTextElement(
      self,
      namespaceUri: str,
      name: str,
      text: str,
  ) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeTextElement(QAnyStringView
    namespaceUri, QAnyStringView name, QAnyStringView text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeTextElement

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeTextElement(QAnyStringView namespaceUri,
    #      QAnyStringView name, QAnyStringView text)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter16writeTextElementE14QAnyStringViewS0_S'
        '0_',
        namespaceUri, name, text,
    )

  def writeEndDocument(self) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeEndDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeEndDocument
    """
    #  void QXmlStreamWriter::writeEndDocument()
    self.uglySide.call('ritual_ZN16QXmlStreamWriter16writeEndDocumentEv')

  def writeEndElement(self) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeEndElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeEndElement
    """
    #  void QXmlStreamWriter::writeEndElement()
    self.uglySide.call('ritual_ZN16QXmlStreamWriter15writeEndElementEv')

  @overload(str)
  def writeEntityReference(self, name: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeEntityReference(QAnyStringView
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeEntityReference

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeEntityReference(QAnyStringView name)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter20writeEntityReferenceE14QAnyStringView',
        name,
    )

  @overload(str)
  @overload(str, str)
  def writeNamespace(self, namespaceUri: str, prefix: str = '') -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeNamespace(QAnyStringView
    namespaceUri, QAnyStringView prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeNamespace

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    prefix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QXmlStreamWriter::writeNamespace(QAnyStringView namespaceUri,
    #      QAnyStringView prefix)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter14writeNamespaceE14QAnyStringViewS0_',
        namespaceUri, prefix,
    )

  @overload(str)
  def writeDefaultNamespace(self, namespaceUri: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeDefaultNamespace(QAnyStringView
    namespaceUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeDefaultNamespace

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeDefaultNamespace(QAnyStringView
    #      namespaceUri)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter21writeDefaultNamespaceE14QAnyStringVie'
        'w',
        namespaceUri,
    )

  @overload(str)
  @overload(str, str)
  def writeProcessingInstruction(self, target: str, data: str = '') -> None:
    """
    Calls Qt's 'void
    QXmlStreamWriter::writeProcessingInstruction(QAnyStringView target,
    QAnyStringView data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeProcessingInstruction

    Parameters
    ----------

    target : str
      Passed on as it is: a QString is made of it for the call.

    data : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QXmlStreamWriter::writeProcessingInstruction(QAnyStringView
    #      target, QAnyStringView data)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter26writeProcessingInstructionE14QAnyStri'
        'ngViewS0_',
        target, data,
    )

  @overload()
  def writeStartDocument(self) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeStartDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeStartDocument
    """
    #  void QXmlStreamWriter::writeStartDocument()
    self.uglySide.call('ritual_ZN16QXmlStreamWriter18writeStartDocumentEv')

  @overload(str)
  def writeStartDocument(self, version: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeStartDocument(QAnyStringView
    version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeStartDocument

    Parameters
    ----------

    version : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeStartDocument(QAnyStringView version)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter18writeStartDocumentE14QAnyStringView',
        version,
    )

  @overload(str, bool)
  def writeStartDocument(self, version: str, standalone: bool) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeStartDocument(QAnyStringView
    version, bool standalone)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeStartDocument

    Parameters
    ----------

    version : str
      Passed on as it is: a QString is made of it for the call.

    standalone : bool
      Passed on as it is.
    """
    #  void QXmlStreamWriter::writeStartDocument(QAnyStringView version, bool
    #      standalone)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter18writeStartDocumentE14QAnyStringViewb',
        version, standalone,
    )

  @overload(str)
  def writeStartElement(self, qualifiedName: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeStartElement(QAnyStringView
    qualifiedName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeStartElement

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeStartElement(QAnyStringView qualifiedName)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter17writeStartElementE14QAnyStringView',
        qualifiedName,
    )

  @overload(str, str)
  def writeStartElement(self, namespaceUri: str, name: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::writeStartElement(QAnyStringView
    namespaceUri, QAnyStringView name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamwriter.html#writeStartElement

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::writeStartElement(QAnyStringView namespaceUri,
    #      QAnyStringView name)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter17writeStartElementE14QAnyStringViewS0_',
        namespaceUri, name,
    )

  @overload(str)
  def raiseError(self, message: str) -> None:
    """
    Calls Qt's 'void QXmlStreamWriter::raiseError(QAnyStringView message)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamwriter.html#raiseError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamWriter::raiseError(QAnyStringView message)
    self.uglySide.call(
        'ritual_ZN16QXmlStreamWriter10raiseErrorE14QAnyStringView', message,
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QXmlStreamWriterPrivate *QXmlStreamWriter::d_func()': gives
      'QXmlStreamWriterPrivate', which has no cute class yet.
    - Qt's 'const QXmlStreamWriterPrivate *QXmlStreamWriter::d_func() const':
      gives 'QXmlStreamWriterPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QXmlStreamWriter.d_func' has no cute function yet. Qt's "
        "'QXmlStreamWriterPrivate *QXmlStreamWriter::d_func()': gives "
        "'QXmlStreamWriterPrivate', which has no cute class yet. Qt's "
        "'const QXmlStreamWriterPrivate *QXmlStreamWriter::d_func() const': "
        "gives 'QXmlStreamWriterPrivate', which has no cute class yet.")

  @staticmethod
  def writeCurrentToken(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamWriter::writeCurrentToken(const QXmlStreamReader
    &reader)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXmlStreamWriter.writeCurrentToken' has no cute function yet. "
        "Qt's 'void QXmlStreamWriter::writeCurrentToken(const "
        "QXmlStreamReader &reader)': takes a type Python has no way to hand "
        "over yet.")
