"""
QHttpServerHttp1ProtocolHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QHttpServerHttp1ProtocolHandler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QHttpServerResponder, QHttpServerStream

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtNetwork import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttpHeaders = WAIT['QHttpHeaders']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerHttp1ProtocolHandler(QHttpServerStream):
  """
  The cute side of Qt's QHttpServerHttp1ProtocolHandler: a plain Python
  object standing in front of one C++ QHttpServerHttp1ProtocolHandler.

  It is built on the cute 'QHttpServerStream', as Qt's
  QHttpServerHttp1ProtocolHandler is built on Qt's QHttpServerStream, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpServerHttp1ProtocolHandler that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject',
  'startHandlingRequest', 'socketDisconnected', 'write', 'writeBeginChunked',
  'writeHeader', 'checkKeepAliveTimeout', 'closeConnection'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpServerHttp1ProtocolHandler::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QHttpServerHttp1ProtocolHandler::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QHttpServerHttp1ProtocolHandler::addConnectionAndKeepAliveHeaders(
    QHttpHeaders &headers)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  12 of the 26 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 leans on
  'QHttpServerHttp1ProtocolHandler; 2 not a gap.

  What to expect
  --------------

  - The C++ QHttpServerHttp1ProtocolHandler is created at the first use, not
    by 'QHttpServerHttp1ProtocolHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerHttp1ProtocolHandler.
  - Qt tells when it has removed the C++ QHttpServerHttp1ProtocolHandler.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpServerHttp1ProtocolHandler that has no cute
    function yet, '__init__', 'addConnectionAndKeepAliveHeaders',
    'completeWriting', 'handleReadyRead', 'resumeListening',
    'writeStatusAndHeaders', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerHttp1ProtocolHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QHttpServerHttp1ProtocolHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpServerHttp1ProtocolHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QHttpServerHttp1ProtocolHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QHttpServerHttp1ProtocolHandler::QHttpServerHttp1ProtocolHandler(
    QAbstractHttpServer *server, QIODevice *socket, QHttpServerRequestFilter
    *filter, QHttpServerConfiguration *config)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'lcHttpServerHttp1Handler'.
    """
    raise NotImplementedError(
        "'QHttpServerHttp1ProtocolHandler.__init__' has no cute function "
        "yet. Qt's "
        "'QHttpServerHttp1ProtocolHandler::QHttpServerHttp1ProtocolHandler(Q"
        "AbstractHttpServer *server, QIODevice *socket, "
        "QHttpServerRequestFilter *filter, QHttpServerConfiguration "
        "*config)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'lcHttpServerHttp1Handler'.")

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

  def startHandlingRequest(self) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp1ProtocolHandler::startHandlingRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html
    """
    #  void QHttpServerHttp1ProtocolHandler::startHandlingRequest()
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler20startHandlingRequestEv',
    )

  def socketDisconnected(self) -> None:
    """
    Calls Qt's 'void QHttpServerHttp1ProtocolHandler::socketDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html
    """
    #  void QHttpServerHttp1ProtocolHandler::socketDisconnected()
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler18socketDisconnectedEv',
    )

  @overload(QByteArray, QHttpHeaders, QHttpServerResponder.StatusCode, int)
  def write(
      self,
      body: QByteArray,
      headers: QHttpHeaders,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerHttp1ProtocolHandler::write(const QByteArray
    &body, const QHttpHeaders &headers, QHttpServerResponder::StatusCode
    status, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html#write

    Parameters
    ----------

    body : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp1ProtocolHandler::write(const QByteArray &body,
    #      const QHttpHeaders &headers, QHttpServerResponder::StatusCode
    #      status, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArrayRK1'
        '2QHttpHeadersN20QHttpServerResponder10StatusCodeEj',
        self._valueOf(body), self._valueOf(headers), status.value, streamId,
    )

  @overload(QHttpServerResponder.StatusCode, int)
  def write(
      self,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp1ProtocolHandler::write(QHttpServerResponder::StatusCode
    status, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html#write

    Parameters
    ----------

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp1ProtocolHandler::write(QHttpServerResponder::
    #      StatusCode status, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler5writeEN20QHttpServerRes'
        'ponder10StatusCodeEj',
        status.value, streamId,
    )

  @overload(QByteArray)
  def write(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpServerHttp1ProtocolHandler::write(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html#write

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpServerHttp1ProtocolHandler::write(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArray',
        self._valueOf(data),
    )

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, body: Optional[str], size: int) -> None:
    """
    Calls Qt's 'void QHttpServerHttp1ProtocolHandler::write(const char *body,
    qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html#write

    Parameters
    ----------

    body : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.
    """
    #  void QHttpServerHttp1ProtocolHandler::write(const char *body, qint64
    #      size)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler5writeEPKcx',
        self._bytesOf(body), size,
    )

  @overload(QHttpHeaders, QHttpServerResponder.StatusCode, int)
  def writeBeginChunked(
      self,
      headers: QHttpHeaders,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerHttp1ProtocolHandler::writeBeginChunked(const
    QHttpHeaders &headers, QHttpServerResponder::StatusCode status, quint32
    streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp1ProtocolHandler::writeBeginChunked(const
    #      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
    #      quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler17writeBeginChunkedERK12'
        'QHttpHeadersN20QHttpServerResponder10StatusCodeEj',
        self._valueOf(headers), status.value, streamId,
    )

  @overload(QByteArray, QByteArray)
  def writeHeader(self, key: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpServerHttp1ProtocolHandler::writeHeader(const
    QByteArray &key, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html#writeHeader

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpServerHttp1ProtocolHandler::writeHeader(const QByteArray
    #      &key, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler11writeHeaderERK10QByteA'
        'rrayS2_',
        self._valueOf(key), self._valueOf(value),
    )

  def checkKeepAliveTimeout(self) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp1ProtocolHandler::checkKeepAliveTimeout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html
    """
    #  void QHttpServerHttp1ProtocolHandler::checkKeepAliveTimeout()
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler21checkKeepAliveTimeoutE'
        'v',
    )

  def closeConnection(self) -> None:
    """
    Calls Qt's 'void QHttpServerHttp1ProtocolHandler::closeConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp1protocolhandler.html
    """
    #  void QHttpServerHttp1ProtocolHandler::closeConnection()
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp1ProtocolHandler15closeConnectionEv',
    )

  @staticmethod
  def addConnectionAndKeepAliveHeaders(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpServerHttp1ProtocolHandler::addConnectionAndKeepAliveHeaders(
    QHttpHeaders &headers)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerHttp1ProtocolHandler.addConnectionAndKeepAliveHeaders' "
        "has no cute function yet. Qt's 'void "
        "QHttpServerHttp1ProtocolHandler::addConnectionAndKeepAliveHeaders(Q"
        "HttpHeaders &headers)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def completeWriting(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerHttp1ProtocolHandler::completeWriting()': leans on
    'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QHttpServerHttp1ProtocolHandler.completeWriting' has no cute "
        "function yet. Qt's 'void "
        "QHttpServerHttp1ProtocolHandler::completeWriting()': leans on "
        "'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def handleReadyRead(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerHttp1ProtocolHandler::handleReadyRead()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'lcHttpServerHttp1Handler'.
    """
    raise NotImplementedError(
        "'QHttpServerHttp1ProtocolHandler.handleReadyRead' has no cute "
        "function yet. Qt's 'void "
        "QHttpServerHttp1ProtocolHandler::handleReadyRead()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'lcHttpServerHttp1Handler'.")

  @staticmethod
  def resumeListening(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerHttp1ProtocolHandler::resumeListening()': leans on
    'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QHttpServerHttp1ProtocolHandler.resumeListening' has no cute "
        "function yet. Qt's 'void "
        "QHttpServerHttp1ProtocolHandler::resumeListening()': leans on "
        "'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def writeStatusAndHeaders(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerHttp1ProtocolHandler::writeStatusAndHeaders(
    QHttpServerResponder::StatusCode status, const QHttpHeaders &headers)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'statusString'.
    """
    raise NotImplementedError(
        "'QHttpServerHttp1ProtocolHandler.writeStatusAndHeaders' has no "
        "cute function yet. Qt's 'void "
        "QHttpServerHttp1ProtocolHandler::writeStatusAndHeaders(QHttpServerR"
        "esponder::StatusCode status, const QHttpHeaders &headers)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'statusString'.")
