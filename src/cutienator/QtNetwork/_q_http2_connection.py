"""
QHttp2Connection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttp2connection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttp2Connection to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Http2, QHttp2Stream

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArrayView, QIODevice, QMetaObject, QUrl
  from . import QHttp2Configuration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QHttp2Configuration = WAIT['QHttp2Configuration']
  QIODevice = WAIT['QIODevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttp2Connection(QObject):
  """
  The cute side of Qt's QHttp2Connection: a plain Python object standing in
  front of one C++ QHttp2Connection.

  It is built on the cute 'QObject', as Qt's QHttp2Connection is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttp2Connection that has a ritual and that Python
  can call so far, 63 names in all: 'metaObject', 'tr',
  'createUpgradedConnection', 'createDirectConnection',
  'createDirectServerConnection', 'getStream', 'promisedStream', 'close',
  'isGoingAway', 'maxConcurrentStreams', 'peerMaxConcurrentStreams',
  'maxHeaderListSize', 'isUpgradedConnection', 'newIncomingStream',
  'newPromisedStream', 'errorReceived', 'connectionClosed',
  'settingsFrameReceived', 'pingFrameReceived', 'errorOccurred',
  'receivedGOAWAY', 'receivedEND_STREAM', 'incomingStreamErrorOccured',
  'sendPing', 'handleReadyRead', 'handleConnectionClosure', 'getSocket',
  'createStreamInternal_impl', 'isInvalidStream', 'streamWasResetLocally',
  'streamIsIgnored', 'connectionError', 'setH2Configuration', 'closeSession',
  'registerStreamAsResetLocally', 'numActiveStreamsImpl',
  'numActiveRemoteStreams', 'numActiveLocalStreams', 'sendClientPreface',
  'sendSETTINGS', 'sendServerPreface', 'serverCheckClientPreface',
  'sendWINDOW_UPDATE', 'sendClientGracefulShutdownGoaway',
  'sendInitialServerGracefulShutdownGoaway',
  'sendFinalServerGracefulShutdownGoaway', 'sendGOAWAYFrame',
  'maybeCloseOnGoingAway', 'sendSETTINGS_ACK', 'handleDATA', 'handleHEADERS',
  'handlePRIORITY', 'handleRST_STREAM', 'handleSETTINGS',
  'handlePUSH_PROMISE', 'handlePING', 'handleGOAWAY', 'handleWINDOW_UPDATE',
  'handleCONTINUATION', 'handleContinuedHEADERS', 'validateHeaderListSize',
  'acceptSetting', 'readClientPreface'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttp2Connection::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHttp2Connection::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHttp2Connection::~QHttp2Connection()': the destructor: Python
    never removes a C++ QHttp2Connection.
  - Qt's 'QH2Expected<QHttp2Stream *, CreateStreamError>
    QHttp2Connection::createStream()': gives a type Python has no way to take
    yet.
  - Qt's 'QH2Expected<QHttp2Stream *, CreateStreamError>
    QHttp2Connection::createStream(QHttp2Stream::Configuration config)':
    gives a type Python has no way to take yet.
  - Qt's 'std::optional<quint32> QHttp2Connection::lastGoAwayStreamID()
    const': gives a type Python has no way to take yet.
  - Qt's 'QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError>
    QHttp2Connection::createLocalStreamInternal(QHttp2Stream::Configuration
    a0)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 78 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QHttp2Connection is created at the first use, not by
    'QHttp2Connection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttp2Connection.
  - Qt tells when it has removed the C++ QHttp2Connection. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttp2Connection that has no cute function yet,
    'createLocalStreamInternal', 'createStream', 'lastGoAwayStreamID', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHttp2Connection, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CreateStreamError(CuteNum, scoped=True):
    """
    The enum 'QHttp2Connection::CreateStreamError' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    MaxConcurrentStreamsReached = Kee[int](0)
    StreamIdsExhausted = Kee[int](1)
    ReceivedGOAWAY = Kee[int](2)
    UnknownError = Kee[int](3)

  class PingState(CuteNum, scoped=True):
    """
    The enum 'QHttp2Connection::PingState' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Ping = Kee[int](0)
    PongSignatureIdentical = Kee[int](1)
    PongSignatureChanged = Kee[int](2)
    PongNoPingSent = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QHttp2Connection::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttp2Connection::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QHttp2Connection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QIODevice, QHttp2Configuration)
  @overload(NoneType, QHttp2Configuration)
  def createUpgradedConnection(
      socket: Optional[QIODevice],
      config: QHttp2Configuration,
  ) -> Optional[QHttp2Connection]:
    """
    Calls Qt's 'QHttp2Connection
    *QHttp2Connection::createUpgradedConnection(QIODevice *socket, const
    QHttp2Configuration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#createUpgradedConnection

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    config : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.

    Returns
    -------

    Optional[QHttp2Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2Connection *QHttp2Connection::createUpgradedConnection(QIODevice
    #      *socket, const QHttp2Configuration &config)
    address = Rituals.call(
        'ritual_ZN16QHttp2Connection24createUpgradedConnectionEP9QIODeviceR'
        'K19QHttp2Configuration',
        CuteMixin._addressOf(socket), CuteMixin._valueOf(config),
    )
    return QHttp2Connection._cuteAt(address)

  @staticmethod
  @overload(QIODevice, QHttp2Configuration)
  @overload(NoneType, QHttp2Configuration)
  def createDirectConnection(
      socket: Optional[QIODevice],
      config: QHttp2Configuration,
  ) -> Optional[QHttp2Connection]:
    """
    Calls Qt's 'QHttp2Connection
    *QHttp2Connection::createDirectConnection(QIODevice *socket, const
    QHttp2Configuration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#createDirectConnection

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    config : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.

    Returns
    -------

    Optional[QHttp2Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2Connection *QHttp2Connection::createDirectConnection(QIODevice
    #      *socket, const QHttp2Configuration &config)
    address = Rituals.call(
        'ritual_ZN16QHttp2Connection22createDirectConnectionEP9QIODeviceRK1'
        '9QHttp2Configuration',
        CuteMixin._addressOf(socket), CuteMixin._valueOf(config),
    )
    return QHttp2Connection._cuteAt(address)

  @staticmethod
  @overload(QIODevice, QHttp2Configuration)
  @overload(NoneType, QHttp2Configuration)
  def createDirectServerConnection(
      socket: Optional[QIODevice],
      config: QHttp2Configuration,
  ) -> Optional[QHttp2Connection]:
    """
    Calls Qt's 'QHttp2Connection
    *QHttp2Connection::createDirectServerConnection(QIODevice *socket, const
    QHttp2Configuration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#createDirectServerConnection

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    config : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.

    Returns
    -------

    Optional[QHttp2Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2Connection
    #      *QHttp2Connection::createDirectServerConnection(QIODevice *socket,
    #      const QHttp2Configuration &config)
    address = Rituals.call(
        'ritual_ZN16QHttp2Connection28createDirectServerConnectionEP9QIODev'
        'iceRK19QHttp2Configuration',
        CuteMixin._addressOf(socket), CuteMixin._valueOf(config),
    )
    return QHttp2Connection._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttp2Connection'

  #  A C++ QHttp2Connection Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttp2Connection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttp2Connection::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttp2Connection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QHttp2Connection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def getStream(self, streamId: int) -> Optional[QHttp2Stream]:
    """
    Calls Qt's 'QHttp2Stream *QHttp2Connection::getStream(quint32 streamId)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#getStream

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
    #  QHttp2Stream *QHttp2Connection::getStream(quint32 streamId) const
    address = self.uglySide.call(
        'ritual_ZNK16QHttp2Connection9getStreamEj', streamId,
    )
    return QHttp2Stream._cuteAt(address)

  @overload(QUrl)
  def promisedStream(self, streamKey: QUrl) -> Optional[QHttp2Stream]:
    """
    Calls Qt's 'QHttp2Stream *QHttp2Connection::promisedStream(const QUrl
    &streamKey) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#promisedStream

    Parameters
    ----------

    streamKey : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QHttp2Stream]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2Stream *QHttp2Connection::promisedStream(const QUrl &streamKey)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QHttp2Connection14promisedStreamERK4QUrl',
        self._valueOf(streamKey),
    )
    return QHttp2Stream._cuteAt(address)

  def isGoingAway(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::isGoingAway() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#isGoingAway
    """
    #  bool QHttp2Connection::isGoingAway() const
    return self.uglySide.call('ritual_ZNK16QHttp2Connection11isGoingAwayEv')

  def maxConcurrentStreams(self) -> int:
    """
    Calls Qt's 'quint32 QHttp2Connection::maxConcurrentStreams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#maxConcurrentStreams
    """
    #  quint32 QHttp2Connection::maxConcurrentStreams() const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection20maxConcurrentStreamsEv',
    )

  def peerMaxConcurrentStreams(self) -> int:
    """
    Calls Qt's 'quint32 QHttp2Connection::peerMaxConcurrentStreams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#peerMaxConcurrentStreams
    """
    #  quint32 QHttp2Connection::peerMaxConcurrentStreams() const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection24peerMaxConcurrentStreamsEv',
    )

  def maxHeaderListSize(self) -> int:
    """
    Calls Qt's 'quint32 QHttp2Connection::maxHeaderListSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#maxHeaderListSize
    """
    #  quint32 QHttp2Connection::maxHeaderListSize() const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection17maxHeaderListSizeEv',
    )

  def isUpgradedConnection(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::isUpgradedConnection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#isUpgradedConnection
    """
    #  bool QHttp2Connection::isUpgradedConnection() const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection20isUpgradedConnectionEv',
    )

  def getSocket(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QHttp2Connection::getSocket() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#getSocket

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QHttp2Connection::getSocket() const
    address = self.uglySide.call('ritual_ZNK16QHttp2Connection9getSocketEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  @overload(int)
  def streamIsIgnored(self, streamID: int) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::streamIsIgnored(quint32 streamID)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#streamIsIgnored

    Parameters
    ----------

    streamID : int
      Passed on as it is.
    """
    #  bool QHttp2Connection::streamIsIgnored(quint32 streamID) const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection15streamIsIgnoredEj', streamID,
    )

  @overload(int)
  def numActiveStreamsImpl(self, mask: int) -> int:
    """
    Calls Qt's 'qsizetype QHttp2Connection::numActiveStreamsImpl(quint32
    mask) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#numActiveStreamsImpl

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  qsizetype QHttp2Connection::numActiveStreamsImpl(quint32 mask) const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection20numActiveStreamsImplEj', mask,
    )

  def numActiveRemoteStreams(self) -> int:
    """
    Calls Qt's 'qsizetype QHttp2Connection::numActiveRemoteStreams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#numActiveRemoteStreams
    """
    #  qsizetype QHttp2Connection::numActiveRemoteStreams() const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection22numActiveRemoteStreamsEv',
    )

  def numActiveLocalStreams(self) -> int:
    """
    Calls Qt's 'qsizetype QHttp2Connection::numActiveLocalStreams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#numActiveLocalStreams
    """
    #  qsizetype QHttp2Connection::numActiveLocalStreams() const
    return self.uglySide.call(
        'ritual_ZNK16QHttp2Connection21numActiveLocalStreamsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHttp2Configuration)
  def setH2Configuration(self, config: QHttp2Configuration) -> None:
    """
    Calls Qt's 'void QHttp2Connection::setH2Configuration(QHttp2Configuration
    config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#setH2Configuration

    Parameters
    ----------

    config : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  void QHttp2Connection::setH2Configuration(QHttp2Configuration config)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection18setH2ConfigurationE19QHttp2Configurat'
        'ion',
        self._valueOf(config),
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

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, socket: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's
    'QHttp2Connection::QHttp2Connection(QIODevice *socket)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#QHttp2Connection

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHttp2Connection::QHttp2Connection(QIODevice *socket)
    self._noteCreation(QHttp2Connection, lambda: Rituals.call(
        'ritual_ZN16QHttp2ConnectionC1EP9QIODevice', self._addressOf(socket),
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

  @overload()
  @overload(Http2.Http2Error)
  def close(
      self,
      errorCode: Http2.Http2Error = Http2.Http2Error.HTTP2_NO_ERROR,
  ) -> None:
    """
    Calls Qt's 'void QHttp2Connection::close(Http2::Http2Error errorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#close

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number. May be left out, as in Qt: it is then
      Http2.Http2Error.HTTP2_NO_ERROR.
    """
    #  void QHttp2Connection::close(Http2::Http2Error errorCode)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection5closeEN5Http210Http2ErrorE',
        errorCode.value,
    )

  @overload(QHttp2Stream)
  @overload(NoneType)
  def newIncomingStream(self, stream: Optional[QHttp2Stream]) -> None:
    """
    Calls Qt's 'void QHttp2Connection::newIncomingStream(QHttp2Stream
    *stream)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#newIncomingStream

    Parameters
    ----------

    stream : Optional[QHttp2Stream]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttp2Connection::newIncomingStream(QHttp2Stream *stream)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection17newIncomingStreamEP12QHttp2Stream',
        self._addressOf(stream),
    )

  @overload(QHttp2Stream)
  @overload(NoneType)
  def newPromisedStream(self, stream: Optional[QHttp2Stream]) -> None:
    """
    Calls Qt's 'void QHttp2Connection::newPromisedStream(QHttp2Stream
    *stream)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#newPromisedStream

    Parameters
    ----------

    stream : Optional[QHttp2Stream]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttp2Connection::newPromisedStream(QHttp2Stream *stream)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection17newPromisedStreamEP12QHttp2Stream',
        self._addressOf(stream),
    )

  def errorReceived(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::errorReceived()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#errorReceived
    """
    #  void QHttp2Connection::errorReceived()
    self.uglySide.call('ritual_ZN16QHttp2Connection13errorReceivedEv')

  def connectionClosed(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::connectionClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#connectionClosed
    """
    #  void QHttp2Connection::connectionClosed()
    self.uglySide.call('ritual_ZN16QHttp2Connection16connectionClosedEv')

  def settingsFrameReceived(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::settingsFrameReceived()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#settingsFrameReceived
    """
    #  void QHttp2Connection::settingsFrameReceived()
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection21settingsFrameReceivedEv',
    )

  @overload(PingState)
  def pingFrameReceived(self, state: PingState) -> None:
    """
    Calls Qt's 'void
    QHttp2Connection::pingFrameReceived(QHttp2Connection::PingState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#pingFrameReceived

    Parameters
    ----------

    state : PingState
      Passed on as its number.
    """
    #  void QHttp2Connection::pingFrameReceived(QHttp2Connection::PingState
    #      state)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection17pingFrameReceivedENS_9PingStateE',
        state.value,
    )

  @overload(Http2.Http2Error, str)
  def errorOccurred(
      self,
      errorCode: Http2.Http2Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void QHttp2Connection::errorOccurred(Http2::Http2Error
    errorCode, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#errorOccurred

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttp2Connection::errorOccurred(Http2::Http2Error errorCode,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection13errorOccurredEN5Http210Http2ErrorERK7'
        'QString',
        errorCode.value, errorString,
    )

  @overload(Http2.Http2Error, int)
  def receivedGOAWAY(
      self,
      errorCode: Http2.Http2Error,
      lastStreamID: int,
  ) -> None:
    """
    Calls Qt's 'void QHttp2Connection::receivedGOAWAY(Http2::Http2Error
    errorCode, quint32 lastStreamID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#receivedGOAWAY

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.

    lastStreamID : int
      Passed on as it is.
    """
    #  void QHttp2Connection::receivedGOAWAY(Http2::Http2Error errorCode,
    #      quint32 lastStreamID)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection14receivedGOAWAYEN5Http210Http2ErrorEj',
        errorCode.value, lastStreamID,
    )

  @overload(int)
  def receivedEND_STREAM(self, streamID: int) -> None:
    """
    Calls Qt's 'void QHttp2Connection::receivedEND_STREAM(quint32 streamID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#receivedEND_STREAM

    Parameters
    ----------

    streamID : int
      Passed on as it is.
    """
    #  void QHttp2Connection::receivedEND_STREAM(quint32 streamID)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection18receivedEND_STREAMEj', streamID,
    )

  @overload(CreateStreamError)
  def incomingStreamErrorOccured(self, error: CreateStreamError) -> None:
    """
    Calls Qt's 'void
    QHttp2Connection::incomingStreamErrorOccured(CreateStreamError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#incomingStreamErrorOccured

    Parameters
    ----------

    error : CreateStreamError
      Passed on as its number.
    """
    #  void QHttp2Connection::incomingStreamErrorOccured(CreateStreamError
    #      error)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection26incomingStreamErrorOccuredENS_17Creat'
        'eStreamErrorE',
        error.value,
    )

  @overload()
  def sendPing(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendPing()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#sendPing
    """
    #  bool QHttp2Connection::sendPing()
    return self.uglySide.call('ritual_ZN16QHttp2Connection8sendPingEv')

  @overload(QByteArrayView)
  def sendPing(self, data: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendPing(QByteArrayView data)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#sendPing

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QHttp2Connection::sendPing(QByteArrayView data)
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection8sendPingE14QByteArrayView',
        self._valueOf(data),
    )

  def handleReadyRead(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleReadyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleReadyRead
    """
    #  void QHttp2Connection::handleReadyRead()
    self.uglySide.call('ritual_ZN16QHttp2Connection15handleReadyReadEv')

  def handleConnectionClosure(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleConnectionClosure()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleConnectionClosure
    """
    #  void QHttp2Connection::handleConnectionClosure()
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection23handleConnectionClosureEv',
    )

  @overload(int, QHttp2Stream.Configuration)
  def createStreamInternal_impl(
      self,
      streamID: int,
      a1: QHttp2Stream.Configuration,
  ) -> Optional[QHttp2Stream]:
    """
    Calls Qt's 'QHttp2Stream
    *QHttp2Connection::createStreamInternal_impl(quint32 streamID,
    QHttp2Stream::Configuration a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#createStreamInternal_impl

    Parameters
    ----------

    streamID : int
      Passed on as it is.

    a1 : QHttp2Stream.Configuration
      Passed on as a value: Qt reads the C++ QHttp2Stream::Configuration,
      which stays Python's own.

    Returns
    -------

    Optional[QHttp2Stream]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2Stream *QHttp2Connection::createStreamInternal_impl(quint32
    #      streamID, QHttp2Stream::Configuration a1)
    address = self.uglySide.call(
        'ritual_ZN16QHttp2Connection25createStreamInternal_implEjN12QHttp2S'
        'tream13ConfigurationE',
        streamID, self._valueOf(a1),
    )
    return QHttp2Stream._cuteAt(address)

  @overload(int)
  def isInvalidStream(self, streamID: int) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::isInvalidStream(quint32 streamID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#isInvalidStream

    Parameters
    ----------

    streamID : int
      Passed on as it is.
    """
    #  bool QHttp2Connection::isInvalidStream(quint32 streamID)
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection15isInvalidStreamEj', streamID,
    )

  @overload(int)
  def streamWasResetLocally(self, streamID: int) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::streamWasResetLocally(quint32
    streamID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#streamWasResetLocally

    Parameters
    ----------

    streamID : int
      Passed on as it is.
    """
    #  bool QHttp2Connection::streamWasResetLocally(quint32 streamID)
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection21streamWasResetLocallyEj', streamID,
    )

  @overload(Http2.Http2Error, str)
  @overload(Http2.Http2Error, str, bool)
  def connectionError(
      self,
      errorCode: Http2.Http2Error,
      message: str,
      logAsError: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QHttp2Connection::connectionError(Http2::Http2Error
    errorCode, const QString &message, bool logAsError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#connectionError

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.

    logAsError : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QHttp2Connection::connectionError(Http2::Http2Error errorCode,
    #      const QString &message, bool logAsError)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection15connectionErrorEN5Http210Http2ErrorER'
        'K7QStringb',
        errorCode.value, message, logAsError,
    )

  def closeSession(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::closeSession()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#closeSession
    """
    #  void QHttp2Connection::closeSession()
    self.uglySide.call('ritual_ZN16QHttp2Connection12closeSessionEv')

  @overload(int)
  def registerStreamAsResetLocally(self, streamID: int) -> None:
    """
    Calls Qt's 'void QHttp2Connection::registerStreamAsResetLocally(quint32
    streamID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#registerStreamAsResetLocally

    Parameters
    ----------

    streamID : int
      Passed on as it is.
    """
    #  void QHttp2Connection::registerStreamAsResetLocally(quint32 streamID)
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection28registerStreamAsResetLocallyEj',
        streamID,
    )

  def sendClientPreface(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendClientPreface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#sendClientPreface
    """
    #  bool QHttp2Connection::sendClientPreface()
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection17sendClientPrefaceEv',
    )

  def sendSETTINGS(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendSETTINGS()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#sendSETTINGS
    """
    #  bool QHttp2Connection::sendSETTINGS()
    return self.uglySide.call('ritual_ZN16QHttp2Connection12sendSETTINGSEv')

  def sendServerPreface(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendServerPreface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#sendServerPreface
    """
    #  bool QHttp2Connection::sendServerPreface()
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection17sendServerPrefaceEv',
    )

  def serverCheckClientPreface(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::serverCheckClientPreface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#serverCheckClientPreface
    """
    #  bool QHttp2Connection::serverCheckClientPreface()
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection24serverCheckClientPrefaceEv',
    )

  @overload(int, int)
  def sendWINDOW_UPDATE(self, streamID: int, delta: int) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendWINDOW_UPDATE(quint32 streamID,
    quint32 delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#sendWINDOW_UPDATE

    Parameters
    ----------

    streamID : int
      Passed on as it is.

    delta : int
      Passed on as it is.
    """
    #  bool QHttp2Connection::sendWINDOW_UPDATE(quint32 streamID, quint32
    #      delta)
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection17sendWINDOW_UPDATEEjj', streamID, delta,
    )

  def sendClientGracefulShutdownGoaway(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::sendClientGracefulShutdownGoaway()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html
    """
    #  void QHttp2Connection::sendClientGracefulShutdownGoaway()
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection32sendClientGracefulShutdownGoawayEv',
    )

  def sendInitialServerGracefulShutdownGoaway(self) -> None:
    """
    Calls Qt's 'void
    QHttp2Connection::sendInitialServerGracefulShutdownGoaway()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html
    """
    #  void QHttp2Connection::sendInitialServerGracefulShutdownGoaway()
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection39sendInitialServerGracefulShutdownGoaw'
        'ayEv',
    )

  def sendFinalServerGracefulShutdownGoaway(self) -> None:
    """
    Calls Qt's 'void
    QHttp2Connection::sendFinalServerGracefulShutdownGoaway()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html
    """
    #  void QHttp2Connection::sendFinalServerGracefulShutdownGoaway()
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection37sendFinalServerGracefulShutdownGoaway'
        'Ev',
    )

  @overload(Http2.Http2Error, int)
  def sendGOAWAYFrame(
      self,
      errorCode: Http2.Http2Error,
      lastSreamID: int,
  ) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendGOAWAYFrame(Http2::Http2Error
    errorCode, quint32 lastSreamID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#sendGOAWAYFrame

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.

    lastSreamID : int
      Passed on as it is.
    """
    #  bool QHttp2Connection::sendGOAWAYFrame(Http2::Http2Error errorCode,
    #      quint32 lastSreamID)
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection15sendGOAWAYFrameEN5Http210Http2ErrorEj',
        errorCode.value, lastSreamID,
    )

  def maybeCloseOnGoingAway(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::maybeCloseOnGoingAway()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#maybeCloseOnGoingAway
    """
    #  void QHttp2Connection::maybeCloseOnGoingAway()
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection21maybeCloseOnGoingAwayEv',
    )

  def sendSETTINGS_ACK(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::sendSETTINGS_ACK()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#sendSETTINGS_ACK
    """
    #  bool QHttp2Connection::sendSETTINGS_ACK()
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection16sendSETTINGS_ACKEv',
    )

  def handleDATA(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleDATA()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#handleDATA
    """
    #  void QHttp2Connection::handleDATA()
    self.uglySide.call('ritual_ZN16QHttp2Connection10handleDATAEv')

  def handleHEADERS(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleHEADERS()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleHEADERS
    """
    #  void QHttp2Connection::handleHEADERS()
    self.uglySide.call('ritual_ZN16QHttp2Connection13handleHEADERSEv')

  def handlePRIORITY(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handlePRIORITY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handlePRIORITY
    """
    #  void QHttp2Connection::handlePRIORITY()
    self.uglySide.call('ritual_ZN16QHttp2Connection14handlePRIORITYEv')

  def handleRST_STREAM(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleRST_STREAM()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleRST_STREAM
    """
    #  void QHttp2Connection::handleRST_STREAM()
    self.uglySide.call('ritual_ZN16QHttp2Connection16handleRST_STREAMEv')

  def handleSETTINGS(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleSETTINGS()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleSETTINGS
    """
    #  void QHttp2Connection::handleSETTINGS()
    self.uglySide.call('ritual_ZN16QHttp2Connection14handleSETTINGSEv')

  def handlePUSH_PROMISE(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handlePUSH_PROMISE()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handlePUSH_PROMISE
    """
    #  void QHttp2Connection::handlePUSH_PROMISE()
    self.uglySide.call('ritual_ZN16QHttp2Connection18handlePUSH_PROMISEEv')

  def handlePING(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handlePING()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#handlePING
    """
    #  void QHttp2Connection::handlePING()
    self.uglySide.call('ritual_ZN16QHttp2Connection10handlePINGEv')

  def handleGOAWAY(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleGOAWAY()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2connection.html#handleGOAWAY
    """
    #  void QHttp2Connection::handleGOAWAY()
    self.uglySide.call('ritual_ZN16QHttp2Connection12handleGOAWAYEv')

  def handleWINDOW_UPDATE(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleWINDOW_UPDATE()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleWINDOW_UPDATE
    """
    #  void QHttp2Connection::handleWINDOW_UPDATE()
    self.uglySide.call('ritual_ZN16QHttp2Connection19handleWINDOW_UPDATEEv')

  def handleCONTINUATION(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleCONTINUATION()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleCONTINUATION
    """
    #  void QHttp2Connection::handleCONTINUATION()
    self.uglySide.call('ritual_ZN16QHttp2Connection18handleCONTINUATIONEv')

  def handleContinuedHEADERS(self) -> None:
    """
    Calls Qt's 'void QHttp2Connection::handleContinuedHEADERS()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#handleContinuedHEADERS
    """
    #  void QHttp2Connection::handleContinuedHEADERS()
    self.uglySide.call(
        'ritual_ZN16QHttp2Connection22handleContinuedHEADERSEv',
    )

  @overload(WAIT['Http2.Frame'])
  def validateHeaderListSize(self, frame: Http2.Frame) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::validateHeaderListSize(const
    Http2::Frame &frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#validateHeaderListSize

    Parameters
    ----------

    frame : Http2.Frame
      Passed on as a value: Qt reads the C++ Http2::Frame, which stays
      Python's own.
    """
    #  bool QHttp2Connection::validateHeaderListSize(const Http2::Frame
    #      &frame)
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection22validateHeaderListSizeERKN5Http25Fram'
        'eE',
        self._valueOf(frame),
    )

  @overload(Http2.Settings, int)
  def acceptSetting(self, identifier: Http2.Settings, newValue: int) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::acceptSetting(Http2::Settings
    identifier, quint32 newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#acceptSetting

    Parameters
    ----------

    identifier : Http2.Settings
      Passed on as its number.

    newValue : int
      Passed on as it is.
    """
    #  bool QHttp2Connection::acceptSetting(Http2::Settings identifier,
    #      quint32 newValue)
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection13acceptSettingEN5Http28SettingsEj',
        identifier.value, newValue,
    )

  def readClientPreface(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Connection::readClientPreface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2connection.html#readClientPreface
    """
    #  bool QHttp2Connection::readClientPreface()
    return self.uglySide.call(
        'ritual_ZN16QHttp2Connection17readClientPrefaceEv',
    )

  @staticmethod
  def createLocalStreamInternal(*__, **_) -> Never:
    """
    Qt's 'QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError>
    QHttp2Connection::createLocalStreamInternal(QHttp2Stream::Configuration
    a0)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttp2Connection.createLocalStreamInternal' has no cute function "
        "yet. Qt's 'QH2Expected<QHttp2Stream *, "
        "QHttp2Connection::CreateStreamError> "
        "QHttp2Connection::createLocalStreamInternal(QHttp2Stream::Configura"
        "tion a0)': gives a type Python has no way to take yet.")

  @staticmethod
  def createStream(*__, **_) -> Never:
    """
    - Qt's 'QH2Expected<QHttp2Stream *, CreateStreamError>
      QHttp2Connection::createStream()': gives a type Python has no way to
      take yet.
    - Qt's 'QH2Expected<QHttp2Stream *, CreateStreamError>
      QHttp2Connection::createStream(QHttp2Stream::Configuration config)':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttp2Connection.createStream' has no cute function yet. Qt's "
        "'QH2Expected<QHttp2Stream *, CreateStreamError> "
        "QHttp2Connection::createStream()': gives a type Python has no way "
        "to take yet. Qt's 'QH2Expected<QHttp2Stream *, CreateStreamError> "
        "QHttp2Connection::createStream(QHttp2Stream::Configuration "
        "config)': gives a type Python has no way to take yet.")

  @staticmethod
  def lastGoAwayStreamID(*__, **_) -> Never:
    """
    Qt's 'std::optional<quint32> QHttp2Connection::lastGoAwayStreamID()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttp2Connection.lastGoAwayStreamID' has no cute function yet. "
        "Qt's 'std::optional<quint32> "
        "QHttp2Connection::lastGoAwayStreamID() const': gives a type Python "
        "has no way to take yet.")
