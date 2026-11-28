"""
QCoapClient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapclient.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtNetwork import QAbstractSocket
from . import QtCoap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject, QUrl, QVariant
  from ..QtNetwork import QHostAddress, QNetworkInterface
  from . import QCoapClientPrivate, QCoapMessage, QCoapReply, QCoapRequest
  from . import QCoapResourceDiscoveryReply, QCoapSecurityConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapMessage = WAIT['QCoapMessage']
  QCoapReply = WAIT['QCoapReply']
  QCoapRequest = WAIT['QCoapRequest']
  QCoapSecurityConfiguration = WAIT['QCoapSecurityConfiguration']
  QHostAddress = WAIT['QHostAddress']
  QIODevice = WAIT['QIODevice']
  QNetworkInterface = WAIT['QNetworkInterface']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapClient(QObject):
  """
  The cute side of Qt's QCoapClient: a plain Python object standing in front
  of one C++ QCoapClient.

  It is built on the cute 'QObject', as Qt's QCoapClient is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapClient that has a ritual and that Python can
  call so far, 25 names in all: 'metaObject', 'tr', 'get', 'put', 'post',
  'deleteResource', 'observe', 'cancelObserve', 'disconnect', 'discover',
  'setSecurityConfiguration', 'setBlockSize', 'setSocketOption',
  'setMaximumServerResponseDelay', 'setAckTimeout', 'setAckRandomFactor',
  'setMaximumRetransmitCount', 'setMinimumTokenSize', 'setBindInterface',
  'bindInterface', 'finished', 'responseToMulticastReceived', 'error',
  'bindInterfaceChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapClient::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCoapClient::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCoapClient::~QCoapClient()': the destructor: Python never removes
    a C++ QCoapClient.
  - Qt's 'const QCoapClientPrivate *QCoapClient::d_func() const': takes in
    Python what 'QCoapClientPrivate *QCoapClient::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 41 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCoapClient is created at the first use, not by
    'QCoapClient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapClient.
  - Qt tells when it has removed the C++ QCoapClient. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

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
    Calls Qt's 'QString QCoapClient::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#tr

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
    #  QString QCoapClient::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QCoapClient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapClient'

  #  A C++ QCoapClient Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapClient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapClient::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapClient::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QCoapClient10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bindInterface(self) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QCoapClient::bindInterface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#bindInterface

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QCoapClient::bindInterface() const
    address = self.uglySide.call('ritual_ZNK11QCoapClient13bindInterfaceEv')
    from ..QtNetwork import QNetworkInterface
    return QNetworkInterface._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCoapSecurityConfiguration)
  def setSecurityConfiguration(
      self,
      configuration: QCoapSecurityConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QCoapClient::setSecurityConfiguration(const
    QCoapSecurityConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclient.html#setSecurityConfiguration

    Parameters
    ----------

    configuration : QCoapSecurityConfiguration
      Passed on as a value: Qt reads the C++ QCoapSecurityConfiguration,
      which stays Python's own.
    """
    #  void QCoapClient::setSecurityConfiguration(const
    #      QCoapSecurityConfiguration &configuration)
    self.uglySide.call(
        'ritual_ZN11QCoapClient24setSecurityConfigurationERK26QCoapSecurity'
        'Configuration',
        self._valueOf(configuration),
    )

  @overload(int)
  def setBlockSize(self, blockSize: int) -> None:
    """
    Calls Qt's 'void QCoapClient::setBlockSize(quint16 blockSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#setBlockSize

    Parameters
    ----------

    blockSize : int
      Passed on as it is.
    """
    #  void QCoapClient::setBlockSize(quint16 blockSize)
    self.uglySide.call('ritual_ZN11QCoapClient12setBlockSizeEt', blockSize)

  @overload(QAbstractSocket.SocketOption, QVariant)
  def setSocketOption(
      self,
      option: QAbstractSocket.SocketOption,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QCoapClient::setSocketOption(QAbstractSocket::SocketOption option, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#setSocketOption

    Parameters
    ----------

    option : QAbstractSocket.SocketOption
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QCoapClient::setSocketOption(QAbstractSocket::SocketOption
    #      option, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN11QCoapClient15setSocketOptionEN15QAbstractSocket12Socket'
        'OptionERK8QVariant',
        option.value, self._valueOf(value),
    )

  @overload(int)
  def setMaximumServerResponseDelay(self, responseDelay: int) -> None:
    """
    Calls Qt's 'void QCoapClient::setMaximumServerResponseDelay(uint
    responseDelay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclient.html#setMaximumServerResponseDelay

    Parameters
    ----------

    responseDelay : int
      Passed on as it is.
    """
    #  void QCoapClient::setMaximumServerResponseDelay(uint responseDelay)
    self.uglySide.call(
        'ritual_ZN11QCoapClient29setMaximumServerResponseDelayEj',
        responseDelay,
    )

  @overload(int)
  def setAckTimeout(self, ackTimeout: int) -> None:
    """
    Calls Qt's 'void QCoapClient::setAckTimeout(uint ackTimeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#setAckTimeout

    Parameters
    ----------

    ackTimeout : int
      Passed on as it is.
    """
    #  void QCoapClient::setAckTimeout(uint ackTimeout)
    self.uglySide.call('ritual_ZN11QCoapClient13setAckTimeoutEj', ackTimeout)

  @overload(float)
  def setAckRandomFactor(self, ackRandomFactor: float) -> None:
    """
    Calls Qt's 'void QCoapClient::setAckRandomFactor(double
    ackRandomFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclient.html#setAckRandomFactor

    Parameters
    ----------

    ackRandomFactor : float
      Passed on as it is.
    """
    #  void QCoapClient::setAckRandomFactor(double ackRandomFactor)
    self.uglySide.call(
        'ritual_ZN11QCoapClient18setAckRandomFactorEd', ackRandomFactor,
    )

  @overload(int)
  def setMaximumRetransmitCount(self, maximumRetransmitCount: int) -> None:
    """
    Calls Qt's 'void QCoapClient::setMaximumRetransmitCount(uint
    maximumRetransmitCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclient.html#setMaximumRetransmitCount

    Parameters
    ----------

    maximumRetransmitCount : int
      Passed on as it is.
    """
    #  void QCoapClient::setMaximumRetransmitCount(uint
    #      maximumRetransmitCount)
    self.uglySide.call(
        'ritual_ZN11QCoapClient25setMaximumRetransmitCountEj',
        maximumRetransmitCount,
    )

  @overload(int)
  def setMinimumTokenSize(self, tokenSize: int) -> None:
    """
    Calls Qt's 'void QCoapClient::setMinimumTokenSize(int tokenSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclient.html#setMinimumTokenSize

    Parameters
    ----------

    tokenSize : int
      Passed on as it is.
    """
    #  void QCoapClient::setMinimumTokenSize(int tokenSize)
    self.uglySide.call(
        'ritual_ZN11QCoapClient19setMinimumTokenSizeEi', tokenSize,
    )

  @overload(QNetworkInterface)
  def setBindInterface(self, iface: QNetworkInterface) -> None:
    """
    Calls Qt's 'void QCoapClient::setBindInterface(const QNetworkInterface
    &iface)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#setBindInterface

    Parameters
    ----------

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  void QCoapClient::setBindInterface(const QNetworkInterface &iface)
    self.uglySide.call(
        'ritual_ZN11QCoapClient16setBindInterfaceERK17QNetworkInterface',
        self._valueOf(iface),
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
  @overload(QtCoap.SecurityMode)
  @overload(QtCoap.SecurityMode, QObject)
  @overload(QtCoap.SecurityMode, NoneType)
  def __init__(
      self,
      securityMode: QtCoap.SecurityMode = QtCoap.SecurityMode.NoSecurity,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCoapClient::QCoapClient(QtCoap::SecurityMode securityMode, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#QCoapClient

    Parameters
    ----------

    securityMode : QtCoap.SecurityMode
      Passed on as its number. May be left out, as in Qt: it is then
      QtCoap.SecurityMode.NoSecurity.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCoapClient::QCoapClient(QtCoap::SecurityMode securityMode, QObject
    #      *parent)
    self._noteCreation(QCoapClient, lambda: Rituals.call(
        'ritual_ZN11QCoapClientC1EN6QtCoap12SecurityModeEP7QObject',
        securityMode.value, self._addressOf(parent, 'QObject'),
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

  @overload(QCoapRequest)
  def get(self, request: QCoapRequest) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::get(const QCoapRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#get

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::get(const QCoapRequest &request)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient3getERK12QCoapRequest',
        self._valueOf(request),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QUrl)
  def get(self, url: QUrl) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::get(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#get

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::get(const QUrl &url)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient3getERK4QUrl', self._valueOf(url),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QCoapRequest)
  @overload(QCoapRequest, QByteArray)
  def put(
      self,
      request: QCoapRequest,
      data: Optional[QByteArray] = None,
  ) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::put(const QCoapRequest &request,
    const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#put

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::put(const QCoapRequest &request, const
    #      QByteArray &data)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient3putERK12QCoapRequestRK10QByteArray',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QCoapRequest, QIODevice)
  @overload(QCoapRequest, NoneType)
  def put(
      self,
      request: QCoapRequest,
      device: Optional[QIODevice],
  ) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::put(const QCoapRequest &request,
    QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#put

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::put(const QCoapRequest &request, QIODevice
    #      *device)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient3putERK12QCoapRequestP9QIODevice',
        self._valueOf(request), self._addressOf(device),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QUrl)
  @overload(QUrl, QByteArray)
  def put(
      self,
      url: QUrl,
      data: Optional[QByteArray] = None,
  ) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::put(const QUrl &url, const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#put

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::put(const QUrl &url, const QByteArray &data)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient3putERK4QUrlRK10QByteArray',
        self._valueOf(url), self._valueOf(data),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QCoapRequest)
  @overload(QCoapRequest, QByteArray)
  def post(
      self,
      request: QCoapRequest,
      data: Optional[QByteArray] = None,
  ) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::post(const QCoapRequest &request,
    const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#post

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::post(const QCoapRequest &request, const
    #      QByteArray &data)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient4postERK12QCoapRequestRK10QByteArray',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QCoapRequest, QIODevice)
  @overload(QCoapRequest, NoneType)
  def post(
      self,
      request: QCoapRequest,
      device: Optional[QIODevice],
  ) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::post(const QCoapRequest &request,
    QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#post

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::post(const QCoapRequest &request, QIODevice
    #      *device)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient4postERK12QCoapRequestP9QIODevice',
        self._valueOf(request), self._addressOf(device),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QUrl)
  @overload(QUrl, QByteArray)
  def post(
      self,
      url: QUrl,
      data: Optional[QByteArray] = None,
  ) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::post(const QUrl &url, const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#post

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::post(const QUrl &url, const QByteArray &data)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient4postERK4QUrlRK10QByteArray',
        self._valueOf(url), self._valueOf(data),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QCoapRequest)
  def deleteResource(self, request: QCoapRequest) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::deleteResource(const QCoapRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#deleteResource

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::deleteResource(const QCoapRequest &request)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient14deleteResourceERK12QCoapRequest',
        self._valueOf(request),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QUrl)
  def deleteResource(self, url: QUrl) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::deleteResource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#deleteResource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::deleteResource(const QUrl &url)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient14deleteResourceERK4QUrl', self._valueOf(url),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QCoapRequest)
  def observe(self, request: QCoapRequest) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::observe(const QCoapRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#observe

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::observe(const QCoapRequest &request)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient7observeERK12QCoapRequest',
        self._valueOf(request),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QUrl)
  def observe(self, request: QUrl) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapClient::observe(const QUrl &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#observe

    Parameters
    ----------

    request : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapClient::observe(const QUrl &request)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient7observeERK4QUrl', self._valueOf(request),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  @overload(QCoapReply)
  @overload(NoneType)
  def cancelObserve(self, notifiedReply: Optional[QCoapReply]) -> None:
    """
    Calls Qt's 'void QCoapClient::cancelObserve(QCoapReply *notifiedReply)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#cancelObserve

    Parameters
    ----------

    notifiedReply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapClient::cancelObserve(QCoapReply *notifiedReply)
    self.uglySide.call(
        'ritual_ZN11QCoapClient13cancelObserveEP10QCoapReply',
        self._addressOf(notifiedReply),
    )

  @overload(QUrl)
  def cancelObserve(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QCoapClient::cancelObserve(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#cancelObserve

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QCoapClient::cancelObserve(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN11QCoapClient13cancelObserveERK4QUrl', self._valueOf(url),
    )

  def disconnect(self) -> None:
    """
    Calls Qt's 'void QCoapClient::disconnect()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#disconnect
    """
    #  void QCoapClient::disconnect()
    self.uglySide.call('ritual_ZN11QCoapClient10disconnectEv')

  @overload(QtCoap.MulticastGroup, int, str)
  def discover(
      self,
      group: QtCoap.MulticastGroup,
      port: int,
      discoveryPath: str,
  ) -> Optional[QCoapResourceDiscoveryReply]:
    """
    Calls Qt's 'QCoapResourceDiscoveryReply
    *QCoapClient::discover(QtCoap::MulticastGroup group, int port, const
    QString &discoveryPath)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#discover

    Parameters
    ----------

    group : QtCoap.MulticastGroup
      Passed on as its number.

    port : int
      Passed on as it is.

    discoveryPath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QCoapResourceDiscoveryReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapResourceDiscoveryReply
    #      *QCoapClient::discover(QtCoap::MulticastGroup group, int port,
    #      const QString &discoveryPath)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient8discoverEN6QtCoap14MulticastGroupEiRK7QStri'
        'ng',
        group.value, port, discoveryPath,
    )
    from . import QCoapResourceDiscoveryReply
    return QCoapResourceDiscoveryReply._cuteAt(address)

  @overload(QUrl, str)
  def discover(
      self,
      baseUrl: QUrl,
      discoveryPath: str,
  ) -> Optional[QCoapResourceDiscoveryReply]:
    """
    Calls Qt's 'QCoapResourceDiscoveryReply *QCoapClient::discover(const QUrl
    &baseUrl, const QString &discoveryPath)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#discover

    Parameters
    ----------

    baseUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    discoveryPath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QCoapResourceDiscoveryReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapResourceDiscoveryReply *QCoapClient::discover(const QUrl
    #      &baseUrl, const QString &discoveryPath)
    address = self.uglySide.call(
        'ritual_ZN11QCoapClient8discoverERK4QUrlRK7QString',
        self._valueOf(baseUrl), discoveryPath,
    )
    from . import QCoapResourceDiscoveryReply
    return QCoapResourceDiscoveryReply._cuteAt(address)

  @overload(QCoapReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QCoapReply]) -> None:
    """
    Calls Qt's 'void QCoapClient::finished(QCoapReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#finished

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapClient::finished(QCoapReply *reply)
    self.uglySide.call(
        'ritual_ZN11QCoapClient8finishedEP10QCoapReply',
        self._addressOf(reply),
    )

  @overload(QCoapReply, QCoapMessage, QHostAddress)
  @overload(NoneType, QCoapMessage, QHostAddress)
  def responseToMulticastReceived(
      self,
      reply: Optional[QCoapReply],
      message: QCoapMessage,
      sender: QHostAddress,
  ) -> None:
    """
    Calls Qt's 'void QCoapClient::responseToMulticastReceived(QCoapReply
    *reply, const QCoapMessage &message, const QHostAddress &sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclient.html#responseToMulticastReceived

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    message : QCoapMessage
      Passed on as a value: Qt reads the C++ QCoapMessage, which stays
      Python's own.

    sender : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QCoapClient::responseToMulticastReceived(QCoapReply *reply, const
    #      QCoapMessage &message, const QHostAddress &sender)
    self.uglySide.call(
        'ritual_ZN11QCoapClient27responseToMulticastReceivedEP10QCoapReplyR'
        'K12QCoapMessageRK12QHostAddress',
        self._addressOf(reply), self._valueOf(message),
        self._valueOf(sender),
    )

  @overload(QCoapReply, QtCoap.Error)
  @overload(NoneType, QtCoap.Error)
  def error(self, reply: Optional[QCoapReply], error: QtCoap.Error) -> None:
    """
    Calls Qt's 'void QCoapClient::error(QCoapReply *reply, QtCoap::Error
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#error

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QtCoap.Error
      Passed on as its number.
    """
    #  void QCoapClient::error(QCoapReply *reply, QtCoap::Error error)
    self.uglySide.call(
        'ritual_ZN11QCoapClient5errorEP10QCoapReplyN6QtCoap5ErrorE',
        self._addressOf(reply), error.value,
    )

  @overload(QNetworkInterface)
  def bindInterfaceChanged(self, iface: QNetworkInterface) -> None:
    """
    Calls Qt's 'void QCoapClient::bindInterfaceChanged(const
    QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclient.html#bindInterfaceChanged

    Parameters
    ----------

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  void QCoapClient::bindInterfaceChanged(const QNetworkInterface &iface)
    self.uglySide.call(
        'ritual_ZN11QCoapClient20bindInterfaceChangedERK17QNetworkInterface',
        self._valueOf(iface),
    )

  def d_func(self) -> Optional[QCoapClientPrivate]:
    """
    Calls Qt's 'QCoapClientPrivate *QCoapClient::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclient.html#d_func

    Returns
    -------

    Optional[QCoapClientPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapClientPrivate *QCoapClient::d_func()
    address = self.uglySide.call('ritual_ZN11QCoapClient6d_funcEv')
    from . import QCoapClientPrivate
    return QCoapClientPrivate._cuteAt(address)
