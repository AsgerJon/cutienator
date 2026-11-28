"""
QHttp2Stream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttp2connection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttp2Stream to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Http2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject
  from ..QtCore import QNonContiguousByteDevice
  from . import QByteDataBuffer, QHttp2Connection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttp2Connection = WAIT['QHttp2Connection']
  QIODevice = WAIT['QIODevice']
  QNonContiguousByteDevice = WAIT['QNonContiguousByteDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttp2Stream(QObject):
  """
  The cute side of Qt's QHttp2Stream: a plain Python object standing in front
  of one C++ QHttp2Stream.

  It is built on the cute 'QObject', as Qt's QHttp2Stream is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttp2Stream that has a ritual and that Python can
  call so far, 41 names in all: 'metaObject', 'tr', 'streamID',
  'isUploadBlocked', 'isUploadingDATA', 'state', 'isActive',
  'isPromisedStream', 'wasReset', 'wasResetbyPeer', 'RST_STREAMCodeReceived',
  'RST_STREAMCodeSent', 'downloadBuffer', 'takeDownloadBuffer',
  'clearDownloadBuffer', 'configuration', 'headersUpdated', 'errorOccurred',
  'stateChanged', 'promisedStreamReceived', 'uploadBlocked', 'dataReceived',
  'rstFrameReceived', 'bytesWritten', 'uploadDeviceError', 'uploadFinished',
  'sendRST_STREAM', 'sendDATA', 'sendWINDOW_UPDATE', 'maybeResumeUpload',
  'uploadDeviceReadChannelFinished', 'uploadDeviceDestroyed',
  'getConnection', 'setState', 'internalSendDATA', 'finishSendDATA',
  'handleDATA', 'handleRST_STREAM', 'handleWINDOW_UPDATE', 'finishWithError',
  'streamError'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttp2Stream::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QHttp2Stream::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QHttp2Stream::~QHttp2Stream()': the destructor: Python never
    removes a C++ QHttp2Stream.
  - Qt's 'HPack::HttpHeader QHttp2Stream::receivedHeaders() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QHttp2Stream::headersReceived(const HPack::HttpHeader
    &headers, bool endStream)': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool QHttp2Stream::sendHEADERS(const HPack::HttpHeader &headers,
    bool endStream, quint8 priority)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QHttp2Stream::transitionState(StateTransition transition)':
    names the enum 'QHttp2Stream::StateTransition', whose class cannot be
    named here.
  - Qt's 'void QHttp2Stream::handleHEADERS(Http2::FrameFlags frameFlags,
    const HPack::HttpHeader &headers)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  6 of the 59 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QHttp2Stream is created at the first use, not by
    'QHttp2Stream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttp2Stream.
  - Qt tells when it has removed the C++ QHttp2Stream. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QHttp2Stream that has no cute function yet,
    'handleHEADERS', 'headersReceived', 'receivedHeaders', 'sendHEADERS',
    'transitionState', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QHttp2Stream, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class State(CuteNum, scoped=True):
    """
    The enum 'QHttp2Stream::State' of Qt, with the 6 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Idle = Kee[int](0)
    ReservedRemote = Kee[int](1)
    Open = Kee[int](2)
    HalfClosedLocal = Kee[int](3)
    HalfClosedRemote = Kee[int](4)
    Closed = Kee[int](5)

  #  The classes Qt writes inside QHttp2Stream, each a class in here as in
  #  C++.

  class Configuration(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHttp2Stream::Configuration: a plain Python object
    standing in front of one C++ QHttp2Stream::Configuration.

    C++ hands a QHttp2Stream::Configuration around as a copy, so every C++
    QHttp2Stream::Configuration behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QHttp2Stream::Configuration yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHttp2Stream::Configuration::~Configuration()': the destructor:
      Python removes its C++ QHttp2Stream::Configuration by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QHttp2Stream::Configuration is created at the first use, not by
      'QHttp2Stream::Configuration(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHttp2Stream::Configuration back gives a copy the
      ritual made for Python, in a new cute QHttp2Stream::Configuration.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHttp2Stream::Configuration'

    #  Qt's '~QHttp2Stream::Configuration()'. Naming it makes this a value
    #  class: Python owns every C++ QHttp2Stream::Configuration behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QHttp2Stream13ConfigurationD1Ev'

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
    Calls Qt's 'QString QHttp2Stream::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#tr

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
    #  QString QHttp2Stream::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QHttp2Stream2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttp2Stream'

  #  A C++ QHttp2Stream Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttp2Stream'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttp2Stream::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttp2Stream::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QHttp2Stream10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def streamID(self) -> int:
    """
    Calls Qt's 'quint32 QHttp2Stream::streamID() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#streamID
    """
    #  quint32 QHttp2Stream::streamID() const
    return self.uglySide.call('ritual_ZNK12QHttp2Stream8streamIDEv')

  def isUploadBlocked(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::isUploadBlocked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#isUploadBlocked
    """
    #  bool QHttp2Stream::isUploadBlocked() const
    return self.uglySide.call('ritual_ZNK12QHttp2Stream15isUploadBlockedEv')

  def isUploadingDATA(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::isUploadingDATA() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#isUploadingDATA
    """
    #  bool QHttp2Stream::isUploadingDATA() const
    return self.uglySide.call('ritual_ZNK12QHttp2Stream15isUploadingDATAEv')

  def state(self) -> State:
    """
    Calls Qt's 'State QHttp2Stream::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QHttp2Stream::state() const
    return QHttp2Stream.State(self.uglySide.call(
        'ritual_ZNK12QHttp2Stream5stateEv',
    ))

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#isActive
    """
    #  bool QHttp2Stream::isActive() const
    return self.uglySide.call('ritual_ZNK12QHttp2Stream8isActiveEv')

  def isPromisedStream(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::isPromisedStream() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#isPromisedStream
    """
    #  bool QHttp2Stream::isPromisedStream() const
    return self.uglySide.call('ritual_ZNK12QHttp2Stream16isPromisedStreamEv')

  def wasReset(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::wasReset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#wasReset
    """
    #  bool QHttp2Stream::wasReset() const
    return self.uglySide.call('ritual_ZNK12QHttp2Stream8wasResetEv')

  def wasResetbyPeer(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::wasResetbyPeer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#wasResetbyPeer
    """
    #  bool QHttp2Stream::wasResetbyPeer() const
    return self.uglySide.call('ritual_ZNK12QHttp2Stream14wasResetbyPeerEv')

  def RST_STREAMCodeReceived(self) -> int:
    """
    Calls Qt's 'quint32 QHttp2Stream::RST_STREAMCodeReceived() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#RST_STREAMCodeReceived
    """
    #  quint32 QHttp2Stream::RST_STREAMCodeReceived() const
    return self.uglySide.call(
        'ritual_ZNK12QHttp2Stream22RST_STREAMCodeReceivedEv',
    )

  def RST_STREAMCodeSent(self) -> int:
    """
    Calls Qt's 'quint32 QHttp2Stream::RST_STREAMCodeSent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#RST_STREAMCodeSent
    """
    #  quint32 QHttp2Stream::RST_STREAMCodeSent() const
    return self.uglySide.call(
        'ritual_ZNK12QHttp2Stream18RST_STREAMCodeSentEv',
    )

  def downloadBuffer(self) -> QByteDataBuffer:
    """
    Calls Qt's 'QByteDataBuffer QHttp2Stream::downloadBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#downloadBuffer

    Returns
    -------

    QByteDataBuffer
      A new cute QByteDataBuffer around the copy Qt gave back. Python owns
      it.
    """
    #  QByteDataBuffer QHttp2Stream::downloadBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK12QHttp2Stream14downloadBufferEv',
    )
    from . import QByteDataBuffer
    return QByteDataBuffer._cuteOwning(address)

  def configuration(self) -> Configuration:
    """
    Calls Qt's 'Configuration QHttp2Stream::configuration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#configuration

    Returns
    -------

    Configuration
      A new cute QHttp2Stream::Configuration around the copy Qt gave back.
      Python owns it.
    """
    #  Configuration QHttp2Stream::configuration() const
    address = self.uglySide.call('ritual_ZNK12QHttp2Stream13configurationEv')
    return QHttp2Stream.Configuration._cuteOwning(address)

  def getConnection(self) -> Optional[QHttp2Connection]:
    """
    Calls Qt's 'QHttp2Connection *QHttp2Stream::getConnection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#getConnection

    Returns
    -------

    Optional[QHttp2Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2Connection *QHttp2Stream::getConnection() const
    address = self.uglySide.call('ritual_ZNK12QHttp2Stream13getConnectionEv')
    from . import QHttp2Connection
    return QHttp2Connection._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(State)
  def setState(self, newState: State) -> None:
    """
    Calls Qt's 'void QHttp2Stream::setState(State newState)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#setState

    Parameters
    ----------

    newState : State
      Passed on as its number.
    """
    #  void QHttp2Stream::setState(State newState)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream8setStateENS_5StateE', newState.value,
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

  @overload(QHttp2Connection, int, Configuration)
  @overload(NoneType, int, Configuration)
  def __init__(
      self,
      connection: Optional[QHttp2Connection],
      streamID: int,
      configuration: Configuration,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttp2Stream::QHttp2Stream(QHttp2Connection *connection, quint32
    streamID, Configuration configuration)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#QHttp2Stream

    Parameters
    ----------

    connection : Optional[QHttp2Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    streamID : int
      Passed on as it is.

    configuration : Configuration
      Passed on as a value: Qt reads the C++ QHttp2Stream::Configuration,
      which stays Python's own.
    """
    #  QHttp2Stream::QHttp2Stream(QHttp2Connection *connection, quint32
    #      streamID, Configuration configuration)
    self._noteCreation(QHttp2Stream, lambda: Rituals.call(
        'ritual_ZN12QHttp2StreamC1EP16QHttp2ConnectionjNS_13ConfigurationE',
        self._addressOf(connection), streamID, self._valueOf(configuration),
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

  def takeDownloadBuffer(self) -> QByteDataBuffer:
    """
    Calls Qt's 'QByteDataBuffer QHttp2Stream::takeDownloadBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#takeDownloadBuffer

    Returns
    -------

    QByteDataBuffer
      A new cute QByteDataBuffer around the copy Qt gave back. Python owns
      it.
    """
    #  QByteDataBuffer QHttp2Stream::takeDownloadBuffer()
    address = self.uglySide.call(
        'ritual_ZN12QHttp2Stream18takeDownloadBufferEv',
    )
    from . import QByteDataBuffer
    return QByteDataBuffer._cuteOwning(address)

  def clearDownloadBuffer(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::clearDownloadBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#clearDownloadBuffer
    """
    #  void QHttp2Stream::clearDownloadBuffer()
    self.uglySide.call('ritual_ZN12QHttp2Stream19clearDownloadBufferEv')

  def headersUpdated(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::headersUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#headersUpdated
    """
    #  void QHttp2Stream::headersUpdated()
    self.uglySide.call('ritual_ZN12QHttp2Stream14headersUpdatedEv')

  @overload(Http2.Http2Error, str)
  def errorOccurred(
      self,
      errorCode: Http2.Http2Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void QHttp2Stream::errorOccurred(Http2::Http2Error errorCode,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#errorOccurred

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttp2Stream::errorOccurred(Http2::Http2Error errorCode, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream13errorOccurredEN5Http210Http2ErrorERK7QStr'
        'ing',
        errorCode.value, errorString,
    )

  @overload(State)
  def stateChanged(self, newState: State) -> None:
    """
    Calls Qt's 'void QHttp2Stream::stateChanged(QHttp2Stream::State
    newState)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#stateChanged

    Parameters
    ----------

    newState : State
      Passed on as its number.
    """
    #  void QHttp2Stream::stateChanged(QHttp2Stream::State newState)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream12stateChangedENS_5StateE', newState.value,
    )

  @overload(int)
  def promisedStreamReceived(self, newStreamID: int) -> None:
    """
    Calls Qt's 'void QHttp2Stream::promisedStreamReceived(quint32
    newStreamID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#promisedStreamReceived

    Parameters
    ----------

    newStreamID : int
      Passed on as it is.
    """
    #  void QHttp2Stream::promisedStreamReceived(quint32 newStreamID)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream22promisedStreamReceivedEj', newStreamID,
    )

  def uploadBlocked(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::uploadBlocked()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#uploadBlocked
    """
    #  void QHttp2Stream::uploadBlocked()
    self.uglySide.call('ritual_ZN12QHttp2Stream13uploadBlockedEv')

  @overload(QByteArray, bool)
  def dataReceived(self, data: QByteArray, endStream: bool) -> None:
    """
    Calls Qt's 'void QHttp2Stream::dataReceived(const QByteArray &data, bool
    endStream)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#dataReceived

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    endStream : bool
      Passed on as it is.
    """
    #  void QHttp2Stream::dataReceived(const QByteArray &data, bool
    #      endStream)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream12dataReceivedERK10QByteArrayb',
        self._valueOf(data), endStream,
    )

  @overload(int)
  def rstFrameReceived(self, errorCode: int) -> None:
    """
    Calls Qt's 'void QHttp2Stream::rstFrameReceived(quint32 errorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#rstFrameReceived

    Parameters
    ----------

    errorCode : int
      Passed on as it is.
    """
    #  void QHttp2Stream::rstFrameReceived(quint32 errorCode)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream16rstFrameReceivedEj', errorCode,
    )

  @overload(int)
  def bytesWritten(self, bytesWritten: int) -> None:
    """
    Calls Qt's 'void QHttp2Stream::bytesWritten(qint64 bytesWritten)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#bytesWritten

    Parameters
    ----------

    bytesWritten : int
      Passed on as it is.
    """
    #  void QHttp2Stream::bytesWritten(qint64 bytesWritten)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream12bytesWrittenEx', bytesWritten,
    )

  @overload(str)
  def uploadDeviceError(self, errorString: str) -> None:
    """
    Calls Qt's 'void QHttp2Stream::uploadDeviceError(const QString
    &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#uploadDeviceError

    Parameters
    ----------

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttp2Stream::uploadDeviceError(const QString &errorString)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream17uploadDeviceErrorERK7QString', errorString,
    )

  def uploadFinished(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::uploadFinished()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#uploadFinished
    """
    #  void QHttp2Stream::uploadFinished()
    self.uglySide.call('ritual_ZN12QHttp2Stream14uploadFinishedEv')

  @overload(Http2.Http2Error)
  def sendRST_STREAM(self, errorCode: Http2.Http2Error) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::sendRST_STREAM(Http2::Http2Error
    errorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#sendRST_STREAM

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.
    """
    #  bool QHttp2Stream::sendRST_STREAM(Http2::Http2Error errorCode)
    return self.uglySide.call(
        'ritual_ZN12QHttp2Stream14sendRST_STREAMEN5Http210Http2ErrorE',
        errorCode.value,
    )

  @overload(QByteArray, bool)
  def sendDATA(self, payload: QByteArray, endStream: bool) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::sendDATA(const QByteArray &payload, bool
    endStream)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#sendDATA

    Parameters
    ----------

    payload : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    endStream : bool
      Passed on as it is.
    """
    #  bool QHttp2Stream::sendDATA(const QByteArray &payload, bool endStream)
    return self.uglySide.call(
        'ritual_ZN12QHttp2Stream8sendDATAERK10QByteArrayb',
        self._valueOf(payload), endStream,
    )

  @overload(QIODevice, bool)
  @overload(NoneType, bool)
  def sendDATA(self, device: Optional[QIODevice], endStream: bool) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::sendDATA(QIODevice *device, bool
    endStream)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#sendDATA

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    endStream : bool
      Passed on as it is.
    """
    #  bool QHttp2Stream::sendDATA(QIODevice *device, bool endStream)
    return self.uglySide.call(
        'ritual_ZN12QHttp2Stream8sendDATAEP9QIODeviceb',
        self._addressOf(device), endStream,
    )

  @overload(QNonContiguousByteDevice, bool)
  def sendDATA(
      self,
      device: Optional[QNonContiguousByteDevice],
      endStream: bool,
  ) -> bool:
    """
    Calls Qt's 'bool QHttp2Stream::sendDATA(QNonContiguousByteDevice *device,
    bool endStream)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#sendDATA

    Parameters
    ----------

    device : Optional[QNonContiguousByteDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    endStream : bool
      Passed on as it is.
    """
    #  bool QHttp2Stream::sendDATA(QNonContiguousByteDevice *device, bool
    #      endStream)
    return self.uglySide.call(
        'ritual_ZN12QHttp2Stream8sendDATAEP24QNonContiguousByteDeviceb',
        self._addressOf(device), endStream,
    )

  @overload(int)
  def sendWINDOW_UPDATE(self, delta: int) -> None:
    """
    Calls Qt's 'void QHttp2Stream::sendWINDOW_UPDATE(quint32 delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#sendWINDOW_UPDATE

    Parameters
    ----------

    delta : int
      Passed on as it is.
    """
    #  void QHttp2Stream::sendWINDOW_UPDATE(quint32 delta)
    self.uglySide.call('ritual_ZN12QHttp2Stream17sendWINDOW_UPDATEEj', delta)

  def maybeResumeUpload(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::maybeResumeUpload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#maybeResumeUpload
    """
    #  void QHttp2Stream::maybeResumeUpload()
    self.uglySide.call('ritual_ZN12QHttp2Stream17maybeResumeUploadEv')

  def uploadDeviceReadChannelFinished(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::uploadDeviceReadChannelFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#uploadDeviceReadChannelFinished
    """
    #  void QHttp2Stream::uploadDeviceReadChannelFinished()
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream31uploadDeviceReadChannelFinishedEv',
    )

  def uploadDeviceDestroyed(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::uploadDeviceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#uploadDeviceDestroyed
    """
    #  void QHttp2Stream::uploadDeviceDestroyed()
    self.uglySide.call('ritual_ZN12QHttp2Stream21uploadDeviceDestroyedEv')

  def internalSendDATA(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::internalSendDATA()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#internalSendDATA
    """
    #  void QHttp2Stream::internalSendDATA()
    self.uglySide.call('ritual_ZN12QHttp2Stream16internalSendDATAEv')

  def finishSendDATA(self) -> None:
    """
    Calls Qt's 'void QHttp2Stream::finishSendDATA()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#finishSendDATA
    """
    #  void QHttp2Stream::finishSendDATA()
    self.uglySide.call('ritual_ZN12QHttp2Stream14finishSendDATAEv')

  @overload(WAIT['Http2.Frame'])
  def handleDATA(self, inboundFrame: Http2.Frame) -> None:
    """
    Calls Qt's 'void QHttp2Stream::handleDATA(const Http2::Frame
    &inboundFrame)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#handleDATA

    Parameters
    ----------

    inboundFrame : Http2.Frame
      Passed on as a value: Qt reads the C++ Http2::Frame, which stays
      Python's own.
    """
    #  void QHttp2Stream::handleDATA(const Http2::Frame &inboundFrame)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream10handleDATAERKN5Http25FrameE',
        self._valueOf(inboundFrame),
    )

  @overload(WAIT['Http2.Frame'])
  def handleRST_STREAM(self, inboundFrame: Http2.Frame) -> None:
    """
    Calls Qt's 'void QHttp2Stream::handleRST_STREAM(const Http2::Frame
    &inboundFrame)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#handleRST_STREAM

    Parameters
    ----------

    inboundFrame : Http2.Frame
      Passed on as a value: Qt reads the C++ Http2::Frame, which stays
      Python's own.
    """
    #  void QHttp2Stream::handleRST_STREAM(const Http2::Frame &inboundFrame)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream16handleRST_STREAMERKN5Http25FrameE',
        self._valueOf(inboundFrame),
    )

  @overload(WAIT['Http2.Frame'])
  def handleWINDOW_UPDATE(self, inboundFrame: Http2.Frame) -> None:
    """
    Calls Qt's 'void QHttp2Stream::handleWINDOW_UPDATE(const Http2::Frame
    &inboundFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2stream.html#handleWINDOW_UPDATE

    Parameters
    ----------

    inboundFrame : Http2.Frame
      Passed on as a value: Qt reads the C++ Http2::Frame, which stays
      Python's own.
    """
    #  void QHttp2Stream::handleWINDOW_UPDATE(const Http2::Frame
    #      &inboundFrame)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream19handleWINDOW_UPDATEERKN5Http25FrameE',
        self._valueOf(inboundFrame),
    )

  @overload(Http2.Http2Error, str)
  def finishWithError(
      self,
      errorCode: Http2.Http2Error,
      message: str,
  ) -> None:
    """
    Calls Qt's 'void QHttp2Stream::finishWithError(Http2::Http2Error
    errorCode, const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#finishWithError

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttp2Stream::finishWithError(Http2::Http2Error errorCode, const
    #      QString &message)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream15finishWithErrorEN5Http210Http2ErrorERK7QS'
        'tring',
        errorCode.value, message,
    )

  @overload(Http2.Http2Error)
  def finishWithError(self, errorCode: Http2.Http2Error) -> None:
    """
    Calls Qt's 'void QHttp2Stream::finishWithError(Http2::Http2Error
    errorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#finishWithError

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.
    """
    #  void QHttp2Stream::finishWithError(Http2::Http2Error errorCode)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream15finishWithErrorEN5Http210Http2ErrorE',
        errorCode.value,
    )

  @overload(Http2.Http2Error, str)
  def streamError(self, errorCode: Http2.Http2Error, message: str) -> None:
    """
    Calls Qt's 'void QHttp2Stream::streamError(Http2::Http2Error errorCode,
    const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2stream.html#streamError

    Parameters
    ----------

    errorCode : Http2.Http2Error
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttp2Stream::streamError(Http2::Http2Error errorCode, const
    #      QString &message)
    self.uglySide.call(
        'ritual_ZN12QHttp2Stream11streamErrorEN5Http210Http2ErrorERK7QStrin'
        'g',
        errorCode.value, message,
    )

  @staticmethod
  def handleHEADERS(*__, **_) -> Never:
    """
    Qt's 'void QHttp2Stream::handleHEADERS(Http2::FrameFlags frameFlags,
    const HPack::HttpHeader &headers)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QHttp2Stream.handleHEADERS' has no cute function yet. Qt's 'void "
        "QHttp2Stream::handleHEADERS(Http2::FrameFlags frameFlags, const "
        "HPack::HttpHeader &headers)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def headersReceived(*__, **_) -> Never:
    """
    Qt's 'void QHttp2Stream::headersReceived(const HPack::HttpHeader
    &headers, bool endStream)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QHttp2Stream.headersReceived' has no cute function yet. Qt's "
        "'void QHttp2Stream::headersReceived(const HPack::HttpHeader "
        "&headers, bool endStream)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def receivedHeaders(*__, **_) -> Never:
    """
    Qt's 'HPack::HttpHeader QHttp2Stream::receivedHeaders() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttp2Stream.receivedHeaders' has no cute function yet. Qt's "
        "'HPack::HttpHeader QHttp2Stream::receivedHeaders() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def sendHEADERS(*__, **_) -> Never:
    """
    Qt's 'bool QHttp2Stream::sendHEADERS(const HPack::HttpHeader &headers,
    bool endStream, quint8 priority)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QHttp2Stream.sendHEADERS' has no cute function yet. Qt's 'bool "
        "QHttp2Stream::sendHEADERS(const HPack::HttpHeader &headers, bool "
        "endStream, quint8 priority)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def transitionState(*__, **_) -> Never:
    """
    Qt's 'void QHttp2Stream::transitionState(StateTransition transition)':
    names the enum 'QHttp2Stream::StateTransition', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QHttp2Stream.transitionState' has no cute function yet. Qt's "
        "'void QHttp2Stream::transitionState(StateTransition transition)': "
        "names the enum 'QHttp2Stream::StateTransition', whose class cannot "
        "be named here.")
