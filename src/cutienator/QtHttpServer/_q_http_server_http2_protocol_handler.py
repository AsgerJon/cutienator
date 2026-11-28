"""
QHttpServerHttp2ProtocolHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QHttpServerHttp2ProtocolHandler to be private: it declares the
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
  from ..QtNetwork import QHttp2Stream, QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttp2Stream = WAIT['QHttp2Stream']
  QHttpHeaders = WAIT['QHttpHeaders']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerHttp2ProtocolHandler(QHttpServerStream):
  """
  The cute side of Qt's QHttpServerHttp2ProtocolHandler: a plain Python
  object standing in front of one C++ QHttpServerHttp2ProtocolHandler.

  It is built on the cute 'QHttpServerStream', as Qt's
  QHttpServerHttp2ProtocolHandler is built on Qt's QHttpServerStream, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpServerHttp2ProtocolHandler that has a ritual
  and that Python can call so far, 16 names in all: 'metaObject',
  'responderDestroyed', 'startHandlingRequest', 'socketDisconnected',
  'write', 'writeBeginChunked', 'writeChunk', 'writeEndChunked',
  'writeHeadersAndStatus', 'checkKeepAliveTimeout', 'onStreamCreated',
  'onStreamClosed', 'onStreamHalfClosed', 'sendToStream', 'onDataReceived',
  'getStream'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpServerHttp2ProtocolHandler::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QHttpServerHttp2ProtocolHandler::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QHttpServerHttp2ProtocolHandler::onHeadersReceived(quint32 id,
    const HPack::HttpHeader &headers)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  6 of the 26 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QHttpServerHttp2ProtocolHandler.

  What to expect
  --------------

  - The C++ QHttpServerHttp2ProtocolHandler is created at the first use, not
    by 'QHttpServerHttp2ProtocolHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerHttp2ProtocolHandler.
  - Qt tells when it has removed the C++ QHttpServerHttp2ProtocolHandler.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpServerHttp2ProtocolHandler that has no cute
    function yet, '__init__', 'enqueueChunk', 'onHeadersReceived', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerHttp2ProtocolHandler'

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
    *QHttpServerHttp2ProtocolHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpServerHttp2ProtocolHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QHttpServerHttp2ProtocolHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def getStream(self, streamId: int) -> Optional[QHttp2Stream]:
    """
    Calls Qt's 'QHttp2Stream
    *QHttpServerHttp2ProtocolHandler::getStream(quint32 streamId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html#getStream

    Parameters
    ----------

    streamId : int
      Passed on as it is.

    Returns
    -------

    Optional[QHttp2Stream]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2Stream *QHttpServerHttp2ProtocolHandler::getStream(quint32
    #      streamId) const
    address = self.uglySide.call(
        'ritual_ZNK31QHttpServerHttp2ProtocolHandler9getStreamEj', streamId,
    )
    from ..QtNetwork import QHttp2Stream
    return QHttp2Stream._cuteAt(address)

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
    Qt's 'QHttpServerHttp2ProtocolHandler::QHttpServerHttp2ProtocolHandler(
    QAbstractHttpServer *server, QIODevice *socket, QHttpServerRequestFilter
    *filter)': leans on 'QHttpServerHttp2ProtocolHandler::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerHttp2ProtocolHandler.__init__' has no cute function "
        "yet. Qt's "
        "'QHttpServerHttp2ProtocolHandler::QHttpServerHttp2ProtocolHandler(Q"
        "AbstractHttpServer *server, QIODevice *socket, "
        "QHttpServerRequestFilter *filter)': leans on "
        "'QHttpServerHttp2ProtocolHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(int)
  def responderDestroyed(self, streamId: int) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp2ProtocolHandler::responderDestroyed(quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

    Parameters
    ----------

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::responderDestroyed(quint32
    #      streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler18responderDestroyedEj',
        streamId,
    )

  def startHandlingRequest(self) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp2ProtocolHandler::startHandlingRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html
    """
    #  void QHttpServerHttp2ProtocolHandler::startHandlingRequest()
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler20startHandlingRequestEv',
    )

  def socketDisconnected(self) -> None:
    """
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::socketDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html
    """
    #  void QHttpServerHttp2ProtocolHandler::socketDisconnected()
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler18socketDisconnectedEv',
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
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::write(const QByteArray
    &body, const QHttpHeaders &headers, QHttpServerResponder::StatusCode
    status, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html#write

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
    #  void QHttpServerHttp2ProtocolHandler::write(const QByteArray &body,
    #      const QHttpHeaders &headers, QHttpServerResponder::StatusCode
    #      status, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler5writeERK10QByteArrayRK1'
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
    QHttpServerHttp2ProtocolHandler::write(QHttpServerResponder::StatusCode
    status, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html#write

    Parameters
    ----------

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::write(QHttpServerResponder::
    #      StatusCode status, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler5writeEN20QHttpServerRes'
        'ponder10StatusCodeEj',
        status.value, streamId,
    )

  @overload(QHttpHeaders, QHttpServerResponder.StatusCode, int)
  def writeBeginChunked(
      self,
      headers: QHttpHeaders,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::writeBeginChunked(const
    QHttpHeaders &headers, QHttpServerResponder::StatusCode status, quint32
    streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

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
    #  void QHttpServerHttp2ProtocolHandler::writeBeginChunked(const
    #      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
    #      quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler17writeBeginChunkedERK12'
        'QHttpHeadersN20QHttpServerResponder10StatusCodeEj',
        self._valueOf(headers), status.value, streamId,
    )

  @overload(QByteArray, int)
  def writeChunk(self, body: QByteArray, streamId: int) -> None:
    """
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::writeChunk(const
    QByteArray &body, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html#writeChunk

    Parameters
    ----------

    body : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::writeChunk(const QByteArray
    #      &body, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler10writeChunkERK10QByteAr'
        'rayj',
        self._valueOf(body), streamId,
    )

  @overload(QByteArray, QHttpHeaders, int)
  def writeEndChunked(
      self,
      data: QByteArray,
      trailers: QHttpHeaders,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::writeEndChunked(const
    QByteArray &data, const QHttpHeaders &trailers, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    trailers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::writeEndChunked(const QByteArray
    #      &data, const QHttpHeaders &trailers, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler15writeEndChunkedERK10QB'
        'yteArrayRK12QHttpHeadersj',
        self._valueOf(data), self._valueOf(trailers), streamId,
    )

  @overload(QHttpHeaders, QHttpServerResponder.StatusCode, bool, int)
  def writeHeadersAndStatus(
      self,
      headers: QHttpHeaders,
      status: QHttpServerResponder.StatusCode,
      endStream: bool,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp2ProtocolHandler::writeHeadersAndStatus(const QHttpHeaders
    &headers, QHttpServerResponder::StatusCode status, bool endStream,
    quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    endStream : bool
      Passed on as it is.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::writeHeadersAndStatus(const
    #      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
    #      bool endStream, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler21writeHeadersAndStatusE'
        'RK12QHttpHeadersN20QHttpServerResponder10StatusCodeEbj',
        self._valueOf(headers), status.value, endStream, streamId,
    )

  def checkKeepAliveTimeout(self) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp2ProtocolHandler::checkKeepAliveTimeout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html
    """
    #  void QHttpServerHttp2ProtocolHandler::checkKeepAliveTimeout()
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler21checkKeepAliveTimeoutE'
        'v',
    )

  @overload(QHttp2Stream)
  @overload(NoneType)
  def onStreamCreated(self, stream: Optional[QHttp2Stream]) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp2ProtocolHandler::onStreamCreated(QHttp2Stream *stream)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

    Parameters
    ----------

    stream : Optional[QHttp2Stream]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpServerHttp2ProtocolHandler::onStreamCreated(QHttp2Stream
    #      *stream)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler15onStreamCreatedEP12QHt'
        'tp2Stream',
        self._addressOf(stream),
    )

  @overload(int)
  def onStreamClosed(self, streamId: int) -> None:
    """
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::onStreamClosed(quint32
    streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

    Parameters
    ----------

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::onStreamClosed(quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler14onStreamClosedEj',
        streamId,
    )

  @overload(int)
  def onStreamHalfClosed(self, streamId: int) -> None:
    """
    Calls Qt's 'void
    QHttpServerHttp2ProtocolHandler::onStreamHalfClosed(quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

    Parameters
    ----------

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::onStreamHalfClosed(quint32
    #      streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler18onStreamHalfClosedEj',
        streamId,
    )

  @overload(int)
  def sendToStream(self, streamId: int) -> None:
    """
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::sendToStream(quint32
    streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html#sendToStream

    Parameters
    ----------

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::sendToStream(quint32 streamId)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler12sendToStreamEj',
        streamId,
    )

  @overload(int, int)
  def onDataReceived(self, id: int, size: int) -> None:
    """
    Calls Qt's 'void QHttpServerHttp2ProtocolHandler::onDataReceived(quint32
    id, qsizetype size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverhttp2protocolhandler.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QHttpServerHttp2ProtocolHandler::onDataReceived(quint32 id,
    #      qsizetype size)
    self.uglySide.call(
        'ritual_ZN31QHttpServerHttp2ProtocolHandler14onDataReceivedEjx',
        id, size,
    )

  @staticmethod
  def enqueueChunk(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerHttp2ProtocolHandler::enqueueChunk(const QByteArray
    &body, bool allEnqueued, const QHttpHeaders &trailers, quint32
    streamId)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'toHeaderPairs'.
    """
    raise NotImplementedError(
        "'QHttpServerHttp2ProtocolHandler.enqueueChunk' has no cute "
        "function yet. Qt's 'void "
        "QHttpServerHttp2ProtocolHandler::enqueueChunk(const QByteArray "
        "&body, bool allEnqueued, const QHttpHeaders &trailers, quint32 "
        "streamId)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'toHeaderPairs'.")

  @staticmethod
  def onHeadersReceived(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerHttp2ProtocolHandler::onHeadersReceived(quint32 id,
    const HPack::HttpHeader &headers)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerHttp2ProtocolHandler.onHeadersReceived' has no cute "
        "function yet. Qt's 'void "
        "QHttpServerHttp2ProtocolHandler::onHeadersReceived(quint32 id, "
        "const HPack::HttpHeader &headers)': takes a type Python has no way "
        "to hand over yet.")
