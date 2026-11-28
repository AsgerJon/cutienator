"""
QHttpServerParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverparser_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpServerParser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QHttpServerResponder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QIODevice
  from ..QtNetwork import QHostAddress
  from . import QHttpServerRequestFilter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QHostAddress = WAIT['QHostAddress']
  QHttpServerRequestFilter = WAIT['QHttpServerRequestFilter']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerParser: a plain Python object standing in
  front of one C++ QHttpServerParser.

  C++ hands a QHttpServerParser around as a copy, so every C++
  QHttpServerParser behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpServerParser that has a ritual and that Python
  can call so far, 10 names in all: 'parseRequestLine', 'sendContinue',
  'readBodyFast', 'readRequestBodyRaw', 'sendError', 'isUrlSizeAllowed',
  'clear', 'contentLength', 'headerField', 'getClientIpAddressAndPort'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qsizetype QHttpServerParser::getChunkSize(QIODevice *socket,
    qsizetype *chunkSize)': takes a number to change where it is.
  - Qt's 'QHttpServerParser::~QHttpServerParser()': the destructor: Python
    removes its C++ QHttpServerParser by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QHttpServerParser.

  What to expect
  --------------

  - The C++ QHttpServerParser is created at the first use, not by
    'QHttpServerParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpServerParser back gives a copy the ritual made
    for Python, in a new cute QHttpServerParser.
  - Each name of Qt's QHttpServerParser that has no cute function yet,
    'getChunkSize', 'parse', 'readHeader', 'readRequestBodyChunked',
    'readRequestLine', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QHttpServerParser, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum, scoped=True):
    """
    The enum 'QHttpServerParser::State' of Qt, with the 6 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NothingDone = Kee[int](0)
    ReadingRequestLine = Kee[int](1)
    ReadingHeader = Kee[int](2)
    ExpectContinue = Kee[int](3)
    ReadingData = Kee[int](4)
    AllDone = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerParser'

  #  Qt's '~QHttpServerParser()'. Naming it makes this a value class: Python
  #  owns every C++ QHttpServerParser behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QHttpServerParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentLength(self) -> int:
    """
    Calls Qt's 'qint64 QHttpServerParser::contentLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#contentLength
    """
    #  qint64 QHttpServerParser::contentLength() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpServerParser13contentLengthEv',
    )

  @overload(QByteArray)
  def headerField(self, name: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpServerParser::headerField(const QByteArray
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverparser.html#headerField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpServerParser::headerField(const QByteArray &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QHttpServerParser11headerFieldERK10QByteArray',
        self._valueOf(name),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def getClientIpAddressAndPort(self) -> str:
    """
    Calls Qt's 'QString QHttpServerParser::getClientIpAddressAndPort()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#getClientIpAddressAndPort

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpServerParser::getClientIpAddressAndPort() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpServerParser25getClientIpAddressAndPortEv',
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

  @overload(QHostAddress, int, QHostAddress, int, QHttpServerRequestFilter)
  @overload(QHostAddress, int, QHostAddress, int, NoneType)
  def __init__(
      self,
      remoteAddress: QHostAddress,
      remotePort: int,
      localAddress: QHostAddress,
      localPort: int,
      filter: Optional[QHttpServerRequestFilter],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerParser::QHttpServerParser(const QHostAddress &remoteAddress,
    quint16 remotePort, const QHostAddress &localAddress, quint16 localPort,
    QHttpServerRequestFilter *filter)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#QHttpServerParser

    Parameters
    ----------

    remoteAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    remotePort : int
      Passed on as it is.

    localAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    localPort : int
      Passed on as it is.

    filter : Optional[QHttpServerRequestFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHttpServerParser::QHttpServerParser(const QHostAddress
    #      &remoteAddress, quint16 remotePort, const QHostAddress
    #      &localAddress, quint16 localPort, QHttpServerRequestFilter
    #      *filter)
    self._noteCreation(QHttpServerParser, lambda: Rituals.call(
        'ritual_ZN17QHttpServerParserC1ERK12QHostAddresstS2_tP24QHttpServer'
        'RequestFilter',
        self._valueOf(remoteAddress), remotePort,
        self._valueOf(localAddress), localPort, self._addressOf(filter),
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

  @overload(QByteArrayView)
  def parseRequestLine(self, line: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QHttpServerParser::parseRequestLine(QByteArrayView
    line)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#parseRequestLine

    Parameters
    ----------

    line : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QHttpServerParser::parseRequestLine(QByteArrayView line)
    return self.uglySide.call(
        'ritual_ZN17QHttpServerParser16parseRequestLineE14QByteArrayView',
        self._valueOf(line),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def sendContinue(self, socket: Optional[QIODevice]) -> int:
    """
    Calls Qt's 'qsizetype QHttpServerParser::sendContinue(QIODevice
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#sendContinue

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype QHttpServerParser::sendContinue(QIODevice *socket)
    return self.uglySide.call(
        'ritual_ZN17QHttpServerParser12sendContinueEP9QIODevice',
        self._addressOf(socket),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def readBodyFast(self, socket: Optional[QIODevice]) -> int:
    """
    Calls Qt's 'qsizetype QHttpServerParser::readBodyFast(QIODevice
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#readBodyFast

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype QHttpServerParser::readBodyFast(QIODevice *socket)
    return self.uglySide.call(
        'ritual_ZN17QHttpServerParser12readBodyFastEP9QIODevice',
        self._addressOf(socket),
    )

  @overload(QIODevice, int)
  @overload(NoneType, int)
  def readRequestBodyRaw(
      self,
      socket: Optional[QIODevice],
      size: int,
  ) -> int:
    """
    Calls Qt's 'qsizetype QHttpServerParser::readRequestBodyRaw(QIODevice
    *socket, qsizetype size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#readRequestBodyRaw

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.
    """
    #  qsizetype QHttpServerParser::readRequestBodyRaw(QIODevice *socket,
    #      qsizetype size)
    return self.uglySide.call(
        'ritual_ZN17QHttpServerParser18readRequestBodyRawEP9QIODevicex',
        self._addressOf(socket), size,
    )

  @overload(QIODevice, QHttpServerResponder.StatusCode)
  @overload(NoneType, QHttpServerResponder.StatusCode)
  def sendError(
      self,
      socket: Optional[QIODevice],
      error: QHttpServerResponder.StatusCode,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerParser::sendError(QIODevice *socket,
    QHttpServerResponder::StatusCode error)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverparser.html#sendError

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QHttpServerResponder.StatusCode
      Passed on as its number.
    """
    #  void QHttpServerParser::sendError(QIODevice *socket,
    #      QHttpServerResponder::StatusCode error)
    self.uglySide.call(
        'ritual_ZN17QHttpServerParser9sendErrorEP9QIODeviceN20QHttpServerRe'
        'sponder10StatusCodeE',
        self._addressOf(socket), error.value,
    )

  @overload(QByteArrayView)
  def isUrlSizeAllowed(self, requestLine: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QHttpServerParser::isUrlSizeAllowed(QByteArrayView
    requestLine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverparser.html#isUrlSizeAllowed

    Parameters
    ----------

    requestLine : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QHttpServerParser::isUrlSizeAllowed(QByteArrayView requestLine)
    return self.uglySide.call(
        'ritual_ZN17QHttpServerParser16isUrlSizeAllowedE14QByteArrayView',
        self._valueOf(requestLine),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QHttpServerParser::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverparser.html#clear
    """
    #  void QHttpServerParser::clear()
    self.uglySide.call('ritual_ZN17QHttpServerParser5clearEv')

  @staticmethod
  def getChunkSize(*__, **_) -> Never:
    """
    Qt's 'qsizetype QHttpServerParser::getChunkSize(QIODevice *socket,
    qsizetype *chunkSize)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QHttpServerParser.getChunkSize' has no cute function yet. Qt's "
        "'qsizetype QHttpServerParser::getChunkSize(QIODevice *socket, "
        "qsizetype *chunkSize)': takes a number to change where it is.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    - Qt's 'bool QHttpServerParser::parse(QHttp2Stream *socket)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'parseRequestMethod'; did you mean 'parseRequestLine'?.
    - Qt's 'bool QHttpServerParser::parse(QIODevice *socket)': leans on
      'QHttpServerParser::readHeader(QIODevice*)', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerParser.parse' has no cute function yet. Qt's 'bool "
        "QHttpServerParser::parse(QHttp2Stream *socket)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'parseRequestMethod'; "
        "did you mean 'parseRequestLine'?. Qt's 'bool "
        "QHttpServerParser::parse(QIODevice *socket)': leans on "
        "'QHttpServerParser::readHeader(QIODevice*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def readHeader(*__, **_) -> Never:
    """
    Qt's 'qsizetype QHttpServerParser::readHeader(QIODevice *socket)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcHttpServerParser'; did you mean
    'QHttpServerParser'?.
    """
    raise NotImplementedError(
        "'QHttpServerParser.readHeader' has no cute function yet. Qt's "
        "'qsizetype QHttpServerParser::readHeader(QIODevice *socket)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name "
        "'lcHttpServerParser'; did you mean 'QHttpServerParser'?.")

  @staticmethod
  def readRequestBodyChunked(*__, **_) -> Never:
    """
    Qt's 'qsizetype QHttpServerParser::readRequestBodyChunked(QIODevice
    *socket)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name
    'lcHttpServerParser'; did you mean 'QHttpServerParser'?.
    """
    raise NotImplementedError(
        "'QHttpServerParser.readRequestBodyChunked' has no cute function "
        "yet. Qt's 'qsizetype "
        "QHttpServerParser::readRequestBodyChunked(QIODevice *socket)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name "
        "'lcHttpServerParser'; did you mean 'QHttpServerParser'?.")

  @staticmethod
  def readRequestLine(*__, **_) -> Never:
    """
    Qt's 'qsizetype QHttpServerParser::readRequestLine(QIODevice *socket)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'lcHttpServerParser'; did
    you mean 'QHttpServerParser'?.
    """
    raise NotImplementedError(
        "'QHttpServerParser.readRequestLine' has no cute function yet. Qt's "
        "'qsizetype QHttpServerParser::readRequestLine(QIODevice *socket)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name "
        "'lcHttpServerParser'; did you mean 'QHttpServerParser'?.")
