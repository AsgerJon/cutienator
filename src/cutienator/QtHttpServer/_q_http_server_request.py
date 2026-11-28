"""
QHttpServerRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserverrequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QDebug, QUrl, QUrlQuery
  from ..QtNetwork import QHostAddress, QHttpHeaders, QSslConfiguration
  from . import QHttpServerParser
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QHostAddress = WAIT['QHostAddress']
  QHttpServerParser = WAIT['QHttpServerParser']
  QSslConfiguration = WAIT['QSslConfiguration']


class QHttpServerRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerRequest: a plain Python object standing in
  front of one C++ QHttpServerRequest.

  C++ hands a QHttpServerRequest around as a copy, so every C++
  QHttpServerRequest behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpServerRequest that has a ritual and that Python
  can call so far, 13 names in all: 'value', 'url', 'query', 'method',
  'headers', 'body', 'remoteAddress', 'remotePort', 'localAddress',
  'localPort', 'sslConfiguration', '__rlshift__', 'create'. It can be made
  from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpServerRequest &QHttpServerRequest::operator=(const
    QHttpServerRequest &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QHttpServerRequest::QHttpServerRequest(QHttpServerRequest
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpServerRequest
    &QHttpServerRequest::operator=(QHttpServerRequest &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QHttpServerRequest::~QHttpServerRequest()': the destructor: Python
    removes its C++ QHttpServerRequest by it, and has no other use for it.
  - Qt's 'void QHttpServerRequest::swap(QHttpServerRequest &other)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 4 not a gap.

  What to expect
  --------------

  - The C++ QHttpServerRequest is created at the first use, not by
    'QHttpServerRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpServerRequest back gives a copy the ritual made
    for Python, in a new cute QHttpServerRequest.
  - Each name of Qt's QHttpServerRequest that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QHttpServerRequest, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Method(CuteFlags, scoped=True):
    """
    The flags enum 'QHttpServerRequest::Method' of Qt, with the 11 names Qt
    gives in it. Qt names the type of its combinations
    'QHttpServerRequest::Methods'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    Unknown = 0x0
    Get = 0x1
    Put = 0x2
    Delete = 0x4
    Post = 0x8
    Head = 0x10
    Options = 0x20
    Patch = 0x40
    Connect = 0x80
    Trace = 0x100
    AnyKnown = 0x1ff

  Methods = Method

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QHttpServerParser)
  def create(parser: QHttpServerParser) -> QHttpServerRequest:
    """
    Calls Qt's 'QHttpServerRequest QHttpServerRequest::create(const
    QHttpServerParser &parser)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#create

    Parameters
    ----------

    parser : QHttpServerParser
      Passed on as a value: Qt reads the C++ QHttpServerParser, which stays
      Python's own.

    Returns
    -------

    QHttpServerRequest
      A new cute QHttpServerRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QHttpServerRequest QHttpServerRequest::create(const QHttpServerParser
    #      &parser)
    address = Rituals.call(
        'ritual_ZN18QHttpServerRequest6createERK17QHttpServerParser',
        CuteMixin._valueOf(parser),
    )
    return QHttpServerRequest._cuteOwning(address)

  @staticmethod
  @overload(QHttpServerParser, QSslConfiguration)
  def create(
      parser: QHttpServerParser,
      configuration: QSslConfiguration,
  ) -> QHttpServerRequest:
    """
    Calls Qt's 'QHttpServerRequest QHttpServerRequest::create(const
    QHttpServerParser &parser, const QSslConfiguration &configuration)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#create

    Parameters
    ----------

    parser : QHttpServerParser
      Passed on as a value: Qt reads the C++ QHttpServerParser, which stays
      Python's own.

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.

    Returns
    -------

    QHttpServerRequest
      A new cute QHttpServerRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QHttpServerRequest QHttpServerRequest::create(const QHttpServerParser
    #      &parser, const QSslConfiguration &configuration)
    address = Rituals.call(
        'ritual_ZN18QHttpServerRequest6createERK17QHttpServerParserRK17QSsl'
        'Configuration',
        CuteMixin._valueOf(parser), CuteMixin._valueOf(configuration),
    )
    return QHttpServerRequest._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerRequest'

  #  Qt's '~QHttpServerRequest()'. Naming it makes this a value class: Python
  #  owns every C++ QHttpServerRequest behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QHttpServerRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def value(self, key: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpServerRequest::value(const QByteArray &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#value

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpServerRequest::value(const QByteArray &key) const
    address = self.uglySide.call(
        'ritual_ZNK18QHttpServerRequest5valueERK10QByteArray',
        self._valueOf(key),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QHttpServerRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHttpServerRequest::url() const
    address = self.uglySide.call('ritual_ZNK18QHttpServerRequest3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def query(self) -> QUrlQuery:
    """
    Calls Qt's 'QUrlQuery QHttpServerRequest::query() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#query

    Returns
    -------

    QUrlQuery
      A new cute QUrlQuery around the copy Qt gave back. Python owns it.
    """
    #  QUrlQuery QHttpServerRequest::query() const
    address = self.uglySide.call('ritual_ZNK18QHttpServerRequest5queryEv')
    from ..QtCore import QUrlQuery
    return QUrlQuery._cuteOwning(address)

  def method(self) -> Method:
    """
    Calls Qt's 'Method QHttpServerRequest::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#method

    Returns
    -------

    Method
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Method(number)' gives.
    """
    #  Method QHttpServerRequest::method() const
    return QHttpServerRequest.Method(self.uglySide.call(
        'ritual_ZNK18QHttpServerRequest6methodEv',
    ))

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'const QHttpHeaders &QHttpServerRequest::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  const QHttpHeaders &QHttpServerRequest::headers() const
    address = self.uglySide.call('ritual_ZNKR18QHttpServerRequest7headersEv')
    from ..QtNetwork import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  def body(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpServerRequest::body() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#body

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpServerRequest::body() const
    address = self.uglySide.call('ritual_ZNK18QHttpServerRequest4bodyEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def remoteAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QHttpServerRequest::remoteAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequest.html#remoteAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QHttpServerRequest::remoteAddress() const
    address = self.uglySide.call(
        'ritual_ZNK18QHttpServerRequest13remoteAddressEv',
    )
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  def remotePort(self) -> int:
    """
    Calls Qt's 'quint16 QHttpServerRequest::remotePort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#remotePort
    """
    #  quint16 QHttpServerRequest::remotePort() const
    return self.uglySide.call('ritual_ZNK18QHttpServerRequest10remotePortEv')

  def localAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QHttpServerRequest::localAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequest.html#localAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QHttpServerRequest::localAddress() const
    address = self.uglySide.call(
        'ritual_ZNK18QHttpServerRequest12localAddressEv',
    )
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  def localPort(self) -> int:
    """
    Calls Qt's 'quint16 QHttpServerRequest::localPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#localPort
    """
    #  quint16 QHttpServerRequest::localPort() const
    return self.uglySide.call('ritual_ZNK18QHttpServerRequest9localPortEv')

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QHttpServerRequest::sslConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequest.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QHttpServerRequest::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK18QHttpServerRequest16sslConfigurationEv',
    )
    from ..QtNetwork import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QHttpServerRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrequest.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QHttpServerRequest &request)
    address = Rituals.call(
        'ritual_Zls6QDebugRK18QHttpServerRequest',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequest::QHttpServerRequest()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequest.html#QHttpServerRequest
    """
    #  QHttpServerRequest::QHttpServerRequest()
    self._noteCreation(QHttpServerRequest, lambda: Rituals.call(
        'ritual_ZN18QHttpServerRequestC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttpServerRequest) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequest::QHttpServerRequest(const QHttpServerRequest
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequest.html#QHttpServerRequest

    Parameters
    ----------

    other : QHttpServerRequest
      Passed on as a value: Qt reads the C++ QHttpServerRequest, which stays
      Python's own.
    """
    #  QHttpServerRequest::QHttpServerRequest(const QHttpServerRequest
    #      &other)
    self._noteCreation(QHttpServerRequest, lambda: Rituals.call(
        'ritual_ZN18QHttpServerRequestC1ERKS_', self._valueOf(other),
    ))

  @overload(QHostAddress, int, QHostAddress, int)
  def __init__(
      self,
      remoteAddress: QHostAddress,
      remotePort: int,
      localAddress: QHostAddress,
      localPort: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequest::QHttpServerRequest(const QHostAddress
    &remoteAddress, quint16 remotePort, const QHostAddress &localAddress,
    quint16 localPort)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequest.html#QHttpServerRequest

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
    """
    #  QHttpServerRequest::QHttpServerRequest(const QHostAddress
    #      &remoteAddress, quint16 remotePort, const QHostAddress
    #      &localAddress, quint16 localPort)
    self._noteCreation(QHttpServerRequest, lambda: Rituals.call(
        'ritual_ZN18QHttpServerRequestC1ERK12QHostAddresstS2_t',
        self._valueOf(remoteAddress), remotePort,
        self._valueOf(localAddress), localPort,
    ))

  @overload(QHostAddress, int, QHostAddress, int, QSslConfiguration)
  def __init__(
      self,
      remoteAddress: QHostAddress,
      remotePort: int,
      localAddress: QHostAddress,
      localPort: int,
      sslConfiguration: QSslConfiguration,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequest::QHttpServerRequest(const QHostAddress
    &remoteAddress, quint16 remotePort, const QHostAddress &localAddress,
    quint16 localPort, const QSslConfiguration &sslConfiguration)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequest.html#QHttpServerRequest

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

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  QHttpServerRequest::QHttpServerRequest(const QHostAddress
    #      &remoteAddress, quint16 remotePort, const QHostAddress
    #      &localAddress, quint16 localPort, const QSslConfiguration
    #      &sslConfiguration)
    self._noteCreation(QHttpServerRequest, lambda: Rituals.call(
        'ritual_ZN18QHttpServerRequestC1ERK12QHostAddresstS2_tRK17QSslConfi'
        'guration',
        self._valueOf(remoteAddress), remotePort,
        self._valueOf(localAddress), localPort,
        self._valueOf(sslConfiguration),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerRequest::swap(QHttpServerRequest &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerRequest.swap' has no cute function yet. Qt's 'void "
        "QHttpServerRequest::swap(QHttpServerRequest &other)': takes a type "
        "Python has no way to hand over yet.")
