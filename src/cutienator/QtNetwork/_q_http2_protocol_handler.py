"""
QHttp2ProtocolHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttp2protocolhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttp2ProtocolHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QAbstractProtocolHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHttp2Stream, QHttpNetworkReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttp2Stream = WAIT['QHttp2Stream']
  QHttpNetworkReply = WAIT['QHttpNetworkReply']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttp2ProtocolHandler(QObject, QAbstractProtocolHandler):
  """
  The cute side of Qt's QHttp2ProtocolHandler: a plain Python object standing
  in front of one C++ QHttp2ProtocolHandler.

  It is built on the cute 'QObject', as Qt's QHttp2ProtocolHandler is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QAbstractProtocolHandler' as well, as Qt's QHttp2ProtocolHandler is built
  on Qt's QAbstractProtocolHandler too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttp2ProtocolHandler that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject',
  'handleConnectionClosure', 'isGoingAway', '_q_uploadDataDestroyed',
  '_q_readyRead', '_q_receiveReply', 'sendRequest', 'tryRemoveReply',
  'sendDATA', 'clearStreamState', 'closeSession'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttp2ProtocolHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHttp2ProtocolHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  22 of the 35 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 not a gap;
  4 forbidden; 4 leans on 'QHttp2ProtocolHandler; 1 leans on 'HPack; 1 leans
  on 'QHttpNetworkConnectionChannel.

  What to expect
  --------------

  - The C++ QHttp2ProtocolHandler is created at the first use, not by
    'QHttp2ProtocolHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttp2ProtocolHandler.
  - Qt tells when it has removed the C++ QHttp2ProtocolHandler. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttp2ProtocolHandler that has no cute function yet,
    '__init__', 'connectStream', 'connectionError', 'createNewStream',
    'finishStream', 'finishStreamWithError', 'handleAuthorization',
    'handleDataReceived', 'handleGOAWAY', 'handleHeadersReceived',
    'initReplyFromPushPromise', 'sendHEADERS', holds a function that raises
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
  __qt_class__ = 'QHttp2ProtocolHandler'

  #  Qt's QHttp2ProtocolHandler is built on more than one class. The part of
  #  a C++ QHttp2ProtocolHandler that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractProtocolHandler':
          'ritual_cast_QHttp2ProtocolHandler_QAbstractProtocolHandler',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttp2ProtocolHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttp2ProtocolHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QHttp2ProtocolHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isGoingAway(self) -> bool:
    """
    Calls Qt's 'bool QHttp2ProtocolHandler::isGoingAway() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#isGoingAway
    """
    #  bool QHttp2ProtocolHandler::isGoingAway() const
    return self.uglySide.call(
        'ritual_ZNK21QHttp2ProtocolHandler11isGoingAwayEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QHttp2ProtocolHandler::QHttp2ProtocolHandler(
    QHttpNetworkConnectionChannel *channel)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'REFUSE_STREAM'; did you mean
    'Http2::REFUSE_STREAM'?.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.__init__' has no cute function yet. Qt's "
        "'QHttp2ProtocolHandler::QHttp2ProtocolHandler(QHttpNetworkConnectio"
        "nChannel *channel)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'REFUSE_STREAM'; did you mean "
        "'Http2::REFUSE_STREAM'?.")

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

  def handleConnectionClosure(self) -> None:
    """
    Calls Qt's 'void QHttp2ProtocolHandler::handleConnectionClosure()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#handleConnectionClosure
    """
    #  void QHttp2ProtocolHandler::handleConnectionClosure()
    self.uglySide.call(
        'ritual_ZN21QHttp2ProtocolHandler23handleConnectionClosureEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def _q_uploadDataDestroyed(self, uploadData: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QHttp2ProtocolHandler::_q_uploadDataDestroyed(QObject
    *uploadData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#_q_uploadDataDestroyed

    Parameters
    ----------

    uploadData : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttp2ProtocolHandler::_q_uploadDataDestroyed(QObject
    #      *uploadData)
    self.uglySide.call(
        'ritual_ZN21QHttp2ProtocolHandler22_q_uploadDataDestroyedEP7QObject',
        self._addressOf(uploadData, 'QObject'),
    )

  def _q_readyRead(self) -> None:
    """
    Calls Qt's 'void QHttp2ProtocolHandler::_q_readyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#_q_readyRead
    """
    #  void QHttp2ProtocolHandler::_q_readyRead()
    ritual = 'ritual_ZN21QHttp2ProtocolHandler12_q_readyReadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QHttp2ProtocolHandler12_q_readyReadEv'
    self.uglySide.call(ritual)

  def _q_receiveReply(self) -> None:
    """
    Calls Qt's 'void QHttp2ProtocolHandler::_q_receiveReply()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#_q_receiveReply
    """
    #  void QHttp2ProtocolHandler::_q_receiveReply()
    ritual = 'ritual_ZN21QHttp2ProtocolHandler15_q_receiveReplyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QHttp2ProtocolHandler15_q_receiveReplyEv'
    self.uglySide.call(ritual)

  def sendRequest(self) -> bool:
    """
    Calls Qt's 'bool QHttp2ProtocolHandler::sendRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#sendRequest
    """
    #  bool QHttp2ProtocolHandler::sendRequest()
    return self.uglySide.call(
        'ritual_ZN21QHttp2ProtocolHandler11sendRequestEv',
    )

  @overload(QHttpNetworkReply)
  @overload(NoneType)
  def tryRemoveReply(self, reply: Optional[QHttpNetworkReply]) -> bool:
    """
    Calls Qt's 'bool QHttp2ProtocolHandler::tryRemoveReply(QHttpNetworkReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#tryRemoveReply

    Parameters
    ----------

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHttp2ProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)
    ritual = (
        'ritual_ZN21QHttp2ProtocolHandler14tryRemoveReplyEP17QHttpNetworkRe'
        'ply')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QHttp2ProtocolHandler14tryRemoveReplyEP17QHttpNet'
          'workReply')
    return self.uglySide.call(ritual, self._addressOf(reply))

  @overload(QHttp2Stream, QHttpNetworkReply)
  @overload(QHttp2Stream, NoneType)
  @overload(NoneType, QHttpNetworkReply)
  @overload(NoneType, NoneType)
  def sendDATA(
      self,
      stream: Optional[QHttp2Stream],
      reply: Optional[QHttpNetworkReply],
  ) -> bool:
    """
    Calls Qt's 'bool QHttp2ProtocolHandler::sendDATA(QHttp2Stream *stream,
    QHttpNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#sendDATA

    Parameters
    ----------

    stream : Optional[QHttp2Stream]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHttp2ProtocolHandler::sendDATA(QHttp2Stream *stream,
    #      QHttpNetworkReply *reply)
    return self.uglySide.call(
        'ritual_ZN21QHttp2ProtocolHandler8sendDATAEP12QHttp2StreamP17QHttpN'
        'etworkReply',
        self._addressOf(stream), self._addressOf(reply),
    )

  @overload(QHttp2Stream)
  @overload(NoneType)
  def clearStreamState(self, stream: Optional[QHttp2Stream]) -> None:
    """
    Calls Qt's 'void QHttp2ProtocolHandler::clearStreamState(QHttp2Stream
    *stream)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#clearStreamState

    Parameters
    ----------

    stream : Optional[QHttp2Stream]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttp2ProtocolHandler::clearStreamState(QHttp2Stream *stream)
    self.uglySide.call(
        'ritual_ZN21QHttp2ProtocolHandler16clearStreamStateEP12QHttp2Stream',
        self._addressOf(stream),
    )

  def closeSession(self) -> None:
    """
    Calls Qt's 'void QHttp2ProtocolHandler::closeSession()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2protocolhandler.html#closeSession
    """
    #  void QHttp2ProtocolHandler::closeSession()
    self.uglySide.call('ritual_ZN21QHttp2ProtocolHandler12closeSessionEv')

  @staticmethod
  def connectStream(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::connectStream(const HttpMessagePair
    &message, QHttp2Stream *stream)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: unknown
    type name 'Http2Error'; did you mean 'Http2::Http2Error'?.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.connectStream' has no cute function yet. "
        "Qt's 'void QHttp2ProtocolHandler::connectStream(const "
        "HttpMessagePair &message, QHttp2Stream *stream)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'Http2Error'; did you mean "
        "'Http2::Http2Error'?.")

  @staticmethod
  def connectionError(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::connectionError(Http2::Http2Error
    errorCode, const QString &message)': leans on
    'QHttpNetworkConnectionChannel::emitFinishedWithError(QNetworkReply::
    NetworkError, QString const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.connectionError' has no cute function yet. "
        "Qt's 'void "
        "QHttp2ProtocolHandler::connectionError(Http2::Http2Error "
        "errorCode, const QString &message)': leans on "
        "'QHttpNetworkConnectionChannel::emitFinishedWithError(QNetworkReply"
        "::NetworkError, QString const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def createNewStream(*__, **_) -> Never:
    """
    Qt's 'QHttp2Stream *QHttp2ProtocolHandler::createNewStream(const
    HttpMessagePair &message, bool uploadDone)': leans on
    'QHttp2ProtocolHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.createNewStream' has no cute function yet. "
        "Qt's 'QHttp2Stream *QHttp2ProtocolHandler::createNewStream(const "
        "HttpMessagePair &message, bool uploadDone)': leans on "
        "'QHttp2ProtocolHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def finishStream(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::finishStream(QHttp2Stream *stream,
    Qt::ConnectionType connectionType)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'CANCEL'; did you mean 'Http2::CANCEL'?.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.finishStream' has no cute function yet. "
        "Qt's 'void QHttp2ProtocolHandler::finishStream(QHttp2Stream "
        "*stream, Qt::ConnectionType connectionType)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'CANCEL'; did you mean "
        "'Http2::CANCEL'?.")

  @staticmethod
  def finishStreamWithError(*__, **_) -> Never:
    """
    - Qt's 'void QHttp2ProtocolHandler::finishStreamWithError(QHttp2Stream
      *stream, Http2::Http2Error errorCode)': Qt's library has no name for
      it, and its code in Qt's source does not compile apart from its file:
      unknown type name 'Http2Error'; did you mean 'Http2::Http2Error'?.
    - Qt's 'void QHttp2ProtocolHandler::finishStreamWithError(QHttp2Stream
      *stream, QNetworkReply::NetworkError error, const QString &message)':
      Qt's library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier 'CANCEL'; did
      you mean 'Http2::CANCEL'?.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.finishStreamWithError' has no cute function "
        "yet. Qt's 'void "
        "QHttp2ProtocolHandler::finishStreamWithError(QHttp2Stream *stream, "
        "Http2::Http2Error errorCode)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'Http2Error'; did you mean 'Http2::Http2Error'?. "
        "Qt's 'void "
        "QHttp2ProtocolHandler::finishStreamWithError(QHttp2Stream *stream, "
        "QNetworkReply::NetworkError error, const QString &message)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'CANCEL'; did you mean 'Http2::CANCEL'?.")

  @staticmethod
  def handleAuthorization(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::handleAuthorization(QHttp2Stream
    *stream)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'CANCEL'; did you mean 'Http2::CANCEL'?.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.handleAuthorization' has no cute function "
        "yet. Qt's 'void "
        "QHttp2ProtocolHandler::handleAuthorization(QHttp2Stream *stream)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'CANCEL'; did you mean 'Http2::CANCEL'?.")

  @staticmethod
  def handleDataReceived(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::handleDataReceived(const QByteArray
    &data, bool endStream)': leans on
    'QHttp2ProtocolHandler::finishStream(QHttp2Stream*, Qt::ConnectionType)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.handleDataReceived' has no cute function "
        "yet. Qt's 'void QHttp2ProtocolHandler::handleDataReceived(const "
        "QByteArray &data, bool endStream)': leans on "
        "'QHttp2ProtocolHandler::finishStream(QHttp2Stream*, "
        "Qt::ConnectionType)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def handleGOAWAY(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::handleGOAWAY(Http2::Http2Error
    errorCode, quint32 lastStreamID)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: unknown
    type name 'Http2Error'; did you mean 'Http2::Http2Error'?.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.handleGOAWAY' has no cute function yet. "
        "Qt's 'void QHttp2ProtocolHandler::handleGOAWAY(Http2::Http2Error "
        "errorCode, quint32 lastStreamID)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: unknown type name 'Http2Error'; did you mean "
        "'Http2::Http2Error'?.")

  @staticmethod
  def handleHeadersReceived(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::handleHeadersReceived(const
    HPack::HttpHeader &headers, bool endStream)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'INTERNAL_ERROR'; did you mean
    'Http2::INTERNAL_ERROR'?.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.handleHeadersReceived' has no cute function "
        "yet. Qt's 'void QHttp2ProtocolHandler::handleHeadersReceived(const "
        "HPack::HttpHeader &headers, bool endStream)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'INTERNAL_ERROR'; did "
        "you mean 'Http2::INTERNAL_ERROR'?.")

  @staticmethod
  def initReplyFromPushPromise(*__, **_) -> Never:
    """
    Qt's 'void QHttp2ProtocolHandler::initReplyFromPushPromise(const
    HttpMessagePair &message, const QUrl &cacheKey)': leans on
    'QHttp2ProtocolHandler::connectStream(std::pair<QHttpNetworkRequest,
    QHttpNetworkReply*> const&, QHttp2Stream*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.initReplyFromPushPromise' has no cute "
        "function yet. Qt's 'void "
        "QHttp2ProtocolHandler::initReplyFromPushPromise(const "
        "HttpMessagePair &message, const QUrl &cacheKey)': leans on "
        "'QHttp2ProtocolHandler::connectStream(std::pair<QHttpNetworkRequest"
        ", QHttpNetworkReply*> const&, QHttp2Stream*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def sendHEADERS(*__, **_) -> Never:
    """
    Qt's 'bool QHttp2ProtocolHandler::sendHEADERS(QHttp2Stream *stream,
    QHttpNetworkRequest &request)': leans on
    'HPack::entry_size(QByteArrayView, QByteArrayView)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QHttp2ProtocolHandler.sendHEADERS' has no cute function yet. Qt's "
        "'bool QHttp2ProtocolHandler::sendHEADERS(QHttp2Stream *stream, "
        "QHttpNetworkRequest &request)': leans on "
        "'HPack::entry_size(QByteArrayView, QByteArrayView)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
