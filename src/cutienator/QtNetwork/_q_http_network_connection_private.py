"""
QHttpNetworkConnectionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkConnectionPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QAbstractSocket, QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QUrl
  from . import QAuthenticator, QHttpNetworkConnection
  from . import QHttpNetworkConnectionChannel, QHttpNetworkReply
  from . import QHttpNetworkRequest, QNetworkProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QHttpNetworkConnectionChannel = WAIT['QHttpNetworkConnectionChannel']
  QHttpNetworkReply = WAIT['QHttpNetworkReply']
  QIODevice = WAIT['QIODevice']
  QNetworkProxy = WAIT['QNetworkProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpNetworkConnectionPrivate(QObjectPrivate):
  """
  The cute side of Qt's QHttpNetworkConnectionPrivate: a plain Python object
  standing in front of one C++ QHttpNetworkConnectionPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QHttpNetworkConnectionPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpNetworkConnectionPrivate that has a ritual and
  that Python can call so far, 17 names in all: 'q_func', 'init',
  'pauseConnection', 'resumeConnection', 'indexOf', 'fillHttp2Queue',
  'dequeueRequest', 'predictNextRequest', 'predictNextRequestsReply',
  'readMoreLater', 'copyCredentials', 'networkLayerDetected', 'errorDetail',
  'removeReply', 'emitReplyError', 'parseRedirectResponse',
  'emitProxyAuthenticationRequired'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHttpNetworkConnection
    *QHttpNetworkConnectionPrivate::q_func() const': takes in Python what
    'QHttpNetworkConnection *QHttpNetworkConnectionPrivate::q_func()' takes.
  - Qt's 'QHttpNetworkConnectionPrivate::~QHttpNetworkConnectionPrivate()':
    the destructor: Python never removes a C++ QHttpNetworkConnectionPrivate.
  - Qt's 'void QHttpNetworkConnectionPrivate::requeueRequest(const
    HttpMessagePair &pair)': takes a type Python has no way to hand over yet.
  - Qt's 'void QHttpNetworkConnectionPrivate::prepareRequest(HttpMessagePair
    &request)': takes a type Python has no way to hand over yet.
  - Qt's 'void QHttpNetworkConnectionPrivate::updateChannel(int i, const
    HttpMessagePair &messagePair)': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool
    QHttpNetworkConnectionPrivate::fillPipeline(QList<HttpMessagePair>
    &queue, QHttpNetworkConnectionChannel &channel)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QHttpNetworkConnectionPrivate::createAuthorization(QIODevice
    *socket, QHttpNetworkRequest &request)': takes a type Python has no way
    to hand over yet.
  - Qt's 'qint64
    QHttpNetworkConnectionPrivate::uncompressedBytesAvailable(const
    QHttpNetworkReply &reply) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'qint64
    QHttpNetworkConnectionPrivate::uncompressedBytesAvailableNextBlock(const
    QHttpNetworkReply &reply) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool
    QHttpNetworkConnectionPrivate::handleAuthenticateChallenge(QIODevice
    *socket, QHttpNetworkReply *reply, bool isProxy, bool &resend)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  13 of the 41 functions Qt declares: 5 leans on
  'QHttpNetworkConnectionChannel; 4 forbidden; 3 leans on
  'QHttpNetworkConnectionPrivate; 1 leans on 'vtable for
  QHttpNetworkConnectionChannel', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QHttpNetworkConnectionPrivate is created at the first use, not by
    'QHttpNetworkConnectionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpNetworkConnectionPrivate.
  - Each name of Qt's QHttpNetworkConnectionPrivate that has no cute function
    yet, '__init__', '_q_connectDelayedChannel', '_q_hostLookupFinished',
    '_q_startNextRequest', 'createAuthorization', 'fillPipeline',
    'handleAuthenticateChallenge', 'prepareRequest', 'queueRequest',
    'requeueRequest', 'shouldEmitChannelError', 'startHostInfoLookup',
    'startNetworkLayerStateLookup', 'uncompressedBytesAvailable',
    'uncompressedBytesAvailableNextBlock', 'updateChannel', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHttpNetworkConnectionPrivate, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class ConnectionState(CuteNum):
    """
    The enum 'QHttpNetworkConnectionPrivate::ConnectionState' of Qt, with the
    2 names Qt gives in it.
    """

    RunningState = Kee[int](0)
    PausedState = Kee[int](1)

  class NetworkLayerPreferenceState(CuteNum):
    """
    The enum 'QHttpNetworkConnectionPrivate::NetworkLayerPreferenceState' of
    Qt, with the 5 names Qt gives in it.
    """

    Unknown = Kee[int](0)
    HostLookupPending = Kee[int](1)
    IPv4 = Kee[int](2)
    IPv6 = Kee[int](3)
    IPv4or6 = Kee[int](4)

  #  The classes Qt writes inside QHttpNetworkConnectionPrivate, each a class
  #  in here as in C++.

  class ParseRedirectResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHttpNetworkConnectionPrivate::ParseRedirectResult:
    a plain Python object standing in front of one C++
    QHttpNetworkConnectionPrivate::ParseRedirectResult.

    C++ hands a QHttpNetworkConnectionPrivate::ParseRedirectResult around as
    a copy, so every C++ QHttpNetworkConnectionPrivate::ParseRedirectResult
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QHttpNetworkConnectionPrivate::ParseRedirectResult
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHttpNetworkConnectionPrivate::ParseRedirectResult::
      ~ParseRedirectResult()': the destructor: Python removes its C++
      QHttpNetworkConnectionPrivate::ParseRedirectResult by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QHttpNetworkConnectionPrivate::ParseRedirectResult is created
      at the first use, not by
      'QHttpNetworkConnectionPrivate::ParseRedirectResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHttpNetworkConnectionPrivate::ParseRedirectResult
      back gives a copy the ritual made for Python, in a new cute
      QHttpNetworkConnectionPrivate::ParseRedirectResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHttpNetworkConnectionPrivate::ParseRedirectResult'

    #  Qt's '~QHttpNetworkConnectionPrivate::ParseRedirectResult()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QHttpNetworkConnectionPrivate::ParseRedirectResult behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QHttpNetworkConnectionPrivate19ParseRedirectResultD1Ev')

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
  @overload(QHttpNetworkReply)
  @overload(NoneType)
  def parseRedirectResponse(
      reply: Optional[QHttpNetworkReply],
  ) -> ParseRedirectResult:
    """
    Calls Qt's 'ParseRedirectResult
    QHttpNetworkConnectionPrivate::parseRedirectResponse(QHttpNetworkReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html

    Parameters
    ----------

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ParseRedirectResult
      A new cute QHttpNetworkConnectionPrivate::ParseRedirectResult around
      the copy Qt gave back. Python owns it.
    """
    #  ParseRedirectResult
    #      QHttpNetworkConnectionPrivate::parseRedirectResponse(
    #      QHttpNetworkReply *reply)
    address = Rituals.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate21parseRedirectResponseEP1'
        '7QHttpNetworkReply',
        CuteMixin._addressOf(reply),
    )
    return QHttpNetworkConnectionPrivate.ParseRedirectResult._cuteOwning(address)

  @overload(QIODevice, QHttpNetworkReply)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QHttpNetworkReply)
  @overload(NoneType, NoneType)
  def parseRedirectResponse(
      self,
      socket: Optional[QIODevice],
      reply: Optional[QHttpNetworkReply],
  ) -> QUrl:
    """
    Calls Qt's 'QUrl
    QHttpNetworkConnectionPrivate::parseRedirectResponse(QIODevice *socket,
    QHttpNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHttpNetworkConnectionPrivate::parseRedirectResponse(QIODevice
    #      *socket, QHttpNetworkReply *reply)
    address = self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate21parseRedirectResponseEP9'
        'QIODeviceP17QHttpNetworkReply',
        self._addressOf(socket), self._addressOf(reply),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkConnectionPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def indexOf(self, socket: Optional[QIODevice]) -> int:
    """
    Calls Qt's 'int QHttpNetworkConnectionPrivate::indexOf(QIODevice *socket)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#indexOf

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QHttpNetworkConnectionPrivate::indexOf(QIODevice *socket) const
    return self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionPrivate7indexOfEP9QIODevice',
        self._addressOf(socket),
    )

  def predictNextRequest(self) -> QHttpNetworkRequest:
    """
    Calls Qt's 'QHttpNetworkRequest
    QHttpNetworkConnectionPrivate::predictNextRequest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html

    Returns
    -------

    QHttpNetworkRequest
      A new cute QHttpNetworkRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QHttpNetworkRequest
    #      QHttpNetworkConnectionPrivate::predictNextRequest() const
    address = self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionPrivate18predictNextRequestEv',
    )
    from . import QHttpNetworkRequest
    return QHttpNetworkRequest._cuteOwning(address)

  def predictNextRequestsReply(self) -> Optional[QHttpNetworkReply]:
    """
    Calls Qt's 'QHttpNetworkReply
    *QHttpNetworkConnectionPrivate::predictNextRequestsReply() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html

    Returns
    -------

    Optional[QHttpNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkReply
    #      *QHttpNetworkConnectionPrivate::predictNextRequestsReply() const
    address = self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionPrivate24predictNextRequestsRepl'
        'yEv',
    )
    from . import QHttpNetworkReply
    return QHttpNetworkReply._cuteAt(address)

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
    Qt's
    'QHttpNetworkConnectionPrivate::QHttpNetworkConnectionPrivate(quint16
    connectionCount, const QString &hostName, quint16 port, bool encrypt,
    bool isLocalSocket, QHttpNetworkConnection::ConnectionType type)': leans
    on 'vtable for QHttpNetworkConnectionChannel', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QHttpNetworkConnectionPrivate::QHttpNetworkConnectionPrivate(quint"
        "16 connectionCount, const QString &hostName, quint16 port, bool "
        "encrypt, bool isLocalSocket, "
        "QHttpNetworkConnection::ConnectionType type)': leans on 'vtable "
        "for QHttpNetworkConnectionChannel', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def q_func(self) -> Optional[QHttpNetworkConnection]:
    """
    Calls Qt's 'QHttpNetworkConnection
    *QHttpNetworkConnectionPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#q_func

    Returns
    -------

    Optional[QHttpNetworkConnection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkConnection *QHttpNetworkConnectionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate6q_funcEv',
    )
    from . import QHttpNetworkConnection
    return QHttpNetworkConnection._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#init
    """
    #  void QHttpNetworkConnectionPrivate::init()
    self.uglySide.call('ritual_ZN29QHttpNetworkConnectionPrivate4initEv')

  def pauseConnection(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionPrivate::pauseConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#pauseConnection
    """
    #  void QHttpNetworkConnectionPrivate::pauseConnection()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate15pauseConnectionEv',
    )

  def resumeConnection(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionPrivate::resumeConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html
    """
    #  void QHttpNetworkConnectionPrivate::resumeConnection()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate16resumeConnectionEv',
    )

  def fillHttp2Queue(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionPrivate::fillHttp2Queue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#fillHttp2Queue
    """
    #  void QHttpNetworkConnectionPrivate::fillHttp2Queue()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate14fillHttp2QueueEv',
    )

  @overload(QIODevice)
  @overload(NoneType)
  def dequeueRequest(self, socket: Optional[QIODevice]) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionPrivate::dequeueRequest(QIODevice
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#dequeueRequest

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHttpNetworkConnectionPrivate::dequeueRequest(QIODevice *socket)
    return self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate14dequeueRequestEP9QIODevi'
        'ce',
        self._addressOf(socket),
    )

  @overload(QHttpNetworkReply)
  @overload(NoneType)
  def readMoreLater(self, reply: Optional[QHttpNetworkReply]) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionPrivate::readMoreLater(QHttpNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#readMoreLater

    Parameters
    ----------

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkConnectionPrivate::readMoreLater(QHttpNetworkReply
    #      *reply)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate13readMoreLaterEP17QHttpNe'
        'tworkReply',
        self._addressOf(reply),
    )

  @overload(int, QAuthenticator, bool)
  @overload(int, NoneType, bool)
  def copyCredentials(
      self,
      fromChannel: int,
      auth: Optional[QAuthenticator],
      isProxy: bool,
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionPrivate::copyCredentials(int
    fromChannel, QAuthenticator *auth, bool isProxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#copyCredentials

    Parameters
    ----------

    fromChannel : int
      Passed on as it is.

    auth : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isProxy : bool
      Passed on as it is.
    """
    #  void QHttpNetworkConnectionPrivate::copyCredentials(int fromChannel,
    #      QAuthenticator *auth, bool isProxy)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate15copyCredentialsEiP14QAut'
        'henticatorb',
        fromChannel, self._addressOf(auth), isProxy,
    )

  @overload(QAbstractSocket.NetworkLayerProtocol)
  def networkLayerDetected(
      self,
      protocol: QAbstractSocket.NetworkLayerProtocol,
  ) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionPrivate::networkLayerDetected(QAbstractSocket::
    NetworkLayerProtocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html

    Parameters
    ----------

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number.
    """
    #  void QHttpNetworkConnectionPrivate::networkLayerDetected(
    #      QAbstractSocket::NetworkLayerProtocol protocol)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate20networkLayerDetectedEN15'
        'QAbstractSocket20NetworkLayerProtocolE',
        protocol.value,
    )

  @overload(QNetworkReply.NetworkError, QIODevice)
  @overload(QNetworkReply.NetworkError, NoneType)
  @overload(QNetworkReply.NetworkError, QIODevice, str)
  @overload(QNetworkReply.NetworkError, NoneType, str)
  def errorDetail(
      self,
      errorCode: QNetworkReply.NetworkError,
      socket: Optional[QIODevice],
      extraDetail: str = '',
  ) -> str:
    """
    Calls Qt's 'QString
    QHttpNetworkConnectionPrivate::errorDetail(QNetworkReply::NetworkError
    errorCode, QIODevice *socket, const QString &extraDetail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#errorDetail

    Parameters
    ----------

    errorCode : QNetworkReply.NetworkError
      Passed on as its number.

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    extraDetail : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpNetworkConnectionPrivate::errorDetail(QNetworkReply::
    #      NetworkError errorCode, QIODevice *socket, const QString
    #      &extraDetail)
    return self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate11errorDetailEN13QNetworkR'
        'eply12NetworkErrorEP9QIODeviceRK7QString',
        errorCode.value, self._addressOf(socket), extraDetail,
    )

  @overload(QHttpNetworkReply)
  @overload(NoneType)
  def removeReply(self, reply: Optional[QHttpNetworkReply]) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionPrivate::removeReply(QHttpNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#removeReply

    Parameters
    ----------

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkConnectionPrivate::removeReply(QHttpNetworkReply
    #      *reply)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate11removeReplyEP17QHttpNetw'
        'orkReply',
        self._addressOf(reply),
    )

  @overload(QIODevice, QHttpNetworkReply, QNetworkReply.NetworkError)
  @overload(QIODevice, NoneType, QNetworkReply.NetworkError)
  @overload(NoneType, QHttpNetworkReply, QNetworkReply.NetworkError)
  @overload(NoneType, NoneType, QNetworkReply.NetworkError)
  def emitReplyError(
      self,
      socket: Optional[QIODevice],
      reply: Optional[QHttpNetworkReply],
      errorCode: QNetworkReply.NetworkError,
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionPrivate::emitReplyError(QIODevice
    *socket, QHttpNetworkReply *reply, QNetworkReply::NetworkError
    errorCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html#emitReplyError

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorCode : QNetworkReply.NetworkError
      Passed on as its number.
    """
    #  void QHttpNetworkConnectionPrivate::emitReplyError(QIODevice *socket,
    #      QHttpNetworkReply *reply, QNetworkReply::NetworkError errorCode)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate14emitReplyErrorEP9QIODevi'
        'ceP17QHttpNetworkReplyN13QNetworkReply12NetworkErrorE',
        self._addressOf(socket), self._addressOf(reply), errorCode.value,
    )

  @overload(QHttpNetworkConnectionChannel, QNetworkProxy, QAuthenticator)
  @overload(QHttpNetworkConnectionChannel, QNetworkProxy, NoneType)
  @overload(NoneType, QNetworkProxy, QAuthenticator)
  @overload(NoneType, QNetworkProxy, NoneType)
  def emitProxyAuthenticationRequired(
      self,
      chan: Optional[QHttpNetworkConnectionChannel],
      proxy: QNetworkProxy,
      auth: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionPrivate::emitProxyAuthenticationRequired(const
    QHttpNetworkConnectionChannel *chan, const QNetworkProxy &proxy,
    QAuthenticator *auth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionprivate.html

    Parameters
    ----------

    chan : Optional[QHttpNetworkConnectionChannel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    auth : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkConnectionPrivate::emitProxyAuthenticationRequired(
    #      const QHttpNetworkConnectionChannel *chan, const QNetworkProxy
    #      &proxy, QAuthenticator *auth)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionPrivate31emitProxyAuthenticationR'
        'equiredEPK29QHttpNetworkConnectionChannelRK13QNetworkProxyP14QAuth'
        'enticator',
        self._addressOf(chan), self._valueOf(proxy), self._addressOf(auth),
    )

  @staticmethod
  def _q_connectDelayedChannel(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::_q_connectDelayedChannel()':
    leans on 'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate._q_connectDelayedChannel' has no "
        "cute function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::_q_connectDelayedChannel()': leans "
        "on 'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def _q_hostLookupFinished(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::_q_hostLookupFinished(const
    QHostInfo &info)': leans on
    'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate._q_hostLookupFinished' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::_q_hostLookupFinished(const "
        "QHostInfo &info)': leans on "
        "'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def _q_startNextRequest(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::_q_startNextRequest()': leans
    on 'QHttpNetworkConnectionPrivate::defaultPipelineLength', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate._q_startNextRequest' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::_q_startNextRequest()': leans on "
        "'QHttpNetworkConnectionPrivate::defaultPipelineLength', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def createAuthorization(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::createAuthorization(QIODevice
    *socket, QHttpNetworkRequest &request)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.createAuthorization' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::createAuthorization(QIODevice "
        "*socket, QHttpNetworkRequest &request)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def fillPipeline(*__, **_) -> Never:
    """
    - Qt's 'bool
      QHttpNetworkConnectionPrivate::fillPipeline(QList<HttpMessagePair>
      &queue, QHttpNetworkConnectionChannel &channel)': takes a type Python
      has no way to hand over yet.
    - Qt's 'void QHttpNetworkConnectionPrivate::fillPipeline(QIODevice
      *socket)': leans on
      'QHttpNetworkConnectionPrivate::defaultPipelineLength', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.fillPipeline' has no cute function "
        "yet. Qt's 'bool "
        "QHttpNetworkConnectionPrivate::fillPipeline(QList<HttpMessagePair> "
        "&queue, QHttpNetworkConnectionChannel &channel)': takes a type "
        "Python has no way to hand over yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::fillPipeline(QIODevice *socket)': "
        "leans on 'QHttpNetworkConnectionPrivate::defaultPipelineLength', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def handleAuthenticateChallenge(*__, **_) -> Never:
    """
    Qt's 'bool
    QHttpNetworkConnectionPrivate::handleAuthenticateChallenge(QIODevice
    *socket, QHttpNetworkReply *reply, bool isProxy, bool &resend)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.handleAuthenticateChallenge' has no "
        "cute function yet. Qt's 'bool "
        "QHttpNetworkConnectionPrivate::handleAuthenticateChallenge(QIODevic"
        "e *socket, QHttpNetworkReply *reply, bool isProxy, bool &resend)': "
        "takes a number to change where it is.")

  @staticmethod
  def prepareRequest(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::prepareRequest(HttpMessagePair
    &request)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.prepareRequest' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::prepareRequest(HttpMessagePair "
        "&request)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def queueRequest(*__, **_) -> Never:
    """
    Qt's 'QHttpNetworkReply
    *QHttpNetworkConnectionPrivate::queueRequest(const QHttpNetworkRequest
    &request)': leans on
    'QHttpNetworkConnectionPrivate::defaultPipelineLength', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.queueRequest' has no cute function "
        "yet. Qt's 'QHttpNetworkReply "
        "*QHttpNetworkConnectionPrivate::queueRequest(const "
        "QHttpNetworkRequest &request)': leans on "
        "'QHttpNetworkConnectionPrivate::defaultPipelineLength', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def requeueRequest(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::requeueRequest(const
    HttpMessagePair &pair)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.requeueRequest' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::requeueRequest(const "
        "HttpMessagePair &pair)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def shouldEmitChannelError(*__, **_) -> Never:
    """
    Qt's 'bool
    QHttpNetworkConnectionPrivate::shouldEmitChannelError(QIODevice
    *socket)': leans on 'QHttpNetworkConnectionChannel::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.shouldEmitChannelError' has no cute "
        "function yet. Qt's 'bool "
        "QHttpNetworkConnectionPrivate::shouldEmitChannelError(QIODevice "
        "*socket)': leans on "
        "'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def startHostInfoLookup(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::startHostInfoLookup()': leans
    on 'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.startHostInfoLookup' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::startHostInfoLookup()': leans on "
        "'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def startNetworkLayerStateLookup(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpNetworkConnectionPrivate::startNetworkLayerStateLookup()': leans on
    'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.startNetworkLayerStateLookup' has "
        "no cute function yet. Qt's 'void "
        "QHttpNetworkConnectionPrivate::startNetworkLayerStateLookup()': "
        "leans on 'QHttpNetworkConnectionChannel::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def uncompressedBytesAvailable(*__, **_) -> Never:
    """
    Qt's 'qint64
    QHttpNetworkConnectionPrivate::uncompressedBytesAvailable(const
    QHttpNetworkReply &reply) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.uncompressedBytesAvailable' has no "
        "cute function yet. Qt's 'qint64 "
        "QHttpNetworkConnectionPrivate::uncompressedBytesAvailable(const "
        "QHttpNetworkReply &reply) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def uncompressedBytesAvailableNextBlock(*__, **_) -> Never:
    """
    Qt's 'qint64
    QHttpNetworkConnectionPrivate::uncompressedBytesAvailableNextBlock(const
    QHttpNetworkReply &reply) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.uncompressedBytesAvailableNextBlock'"
        " has no cute function yet. Qt's 'qint64 "
        "QHttpNetworkConnectionPrivate::uncompressedBytesAvailableNextBlock("
        "const QHttpNetworkReply &reply) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def updateChannel(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionPrivate::updateChannel(int i, const
    HttpMessagePair &messagePair)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionPrivate.updateChannel' has no cute function "
        "yet. Qt's 'void QHttpNetworkConnectionPrivate::updateChannel(int "
        "i, const HttpMessagePair &messagePair)': takes a type Python has "
        "no way to hand over yet.")
