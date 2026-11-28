"""
QAbstractHttpServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qabstracthttpserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtNetwork import QHttp2Configuration, QLocalServer, QTcpServer
  from . import QAbstractHttpServerPrivate, QHttpServerConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttp2Configuration = WAIT['QHttp2Configuration']
  QHttpServerConfiguration = WAIT['QHttpServerConfiguration']
  QLocalServer = WAIT['QLocalServer']
  QTcpServer = WAIT['QTcpServer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractHttpServer(QObject):
  """
  The cute side of Qt's QAbstractHttpServer: a plain Python object standing
  in front of one C++ QAbstractHttpServer.

  It is built on the cute 'QObject', as Qt's QAbstractHttpServer is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractHttpServer that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'bind',
  'servers', 'localServers', 'http2Configuration', 'setHttp2Configuration',
  'setConfiguration', 'configuration', 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractHttpServer::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractHttpServer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractHttpServer::~QAbstractHttpServer()': the destructor:
    Python never removes a C++ QAbstractHttpServer.
  - Qt's 'QList<quint16> QAbstractHttpServer::serverPorts() const': gives a
    type Python has no way to take yet.
  - Qt's 'bool QAbstractHttpServer::handleRequest(const QHttpServerRequest
    &request, QHttpServerResponder &responder)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QAbstractHttpServer::missingHandler(const QHttpServerRequest
    &request, QHttpServerResponder &responder)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QAbstractHttpServerPrivate *QAbstractHttpServer::d_func()
    const': takes in Python what 'QAbstractHttpServerPrivate
    *QAbstractHttpServer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractHttpServer is created at the first use, not by
    'QAbstractHttpServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractHttpServer.
  - Qt tells when it has removed the C++ QAbstractHttpServer. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractHttpServer that has no cute function yet,
    '__init__', 'handleRequest', 'missingHandler', 'serverPorts', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QAbstractHttpServer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracthttpserver.html#tr

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
    #  QString QAbstractHttpServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QAbstractHttpServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractHttpServer'

  #  A C++ QAbstractHttpServer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractHttpServer'

  #  The functions Qt calls itself that QAbstractHttpServer is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'handleRequest': (
          'bool QAbstractHttpServer::handleRequest(const '
          'QHttpServerRequest &, QHttpServerResponder &)',
      ),
      'missingHandler': (
          'void QAbstractHttpServer::missingHandler(const '
          'QHttpServerRequest &, QHttpServerResponder &)',
      ),
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
    Calls Qt's 'const QMetaObject *QAbstractHttpServer::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractHttpServer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractHttpServer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def servers(self) -> QList[QTcpServer]:
    """
    Calls Qt's 'QList<QTcpServer *> QAbstractHttpServer::servers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracthttpserver.html#servers

    Returns
    -------

    QList[QTcpServer]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTcpServer *> QAbstractHttpServer::servers() const
    address = self.uglySide.call('ritual_ZNK19QAbstractHttpServer7serversEv')
    from ..QtNetwork import QTcpServer
    return QList[QTcpServer]._cuteOwning(address)

  def localServers(self) -> QList[QLocalServer]:
    """
    Calls Qt's 'QList<QLocalServer *> QAbstractHttpServer::localServers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserver.html#localServers

    Returns
    -------

    QList[QLocalServer]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLocalServer *> QAbstractHttpServer::localServers() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractHttpServer12localServersEv',
    )
    from ..QtNetwork import QLocalServer
    return QList[QLocalServer]._cuteOwning(address)

  def http2Configuration(self) -> QHttp2Configuration:
    """
    Calls Qt's 'QHttp2Configuration QAbstractHttpServer::http2Configuration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserver.html#http2Configuration

    Returns
    -------

    QHttp2Configuration
      A new cute QHttp2Configuration around the copy Qt gave back. Python
      owns it.
    """
    #  QHttp2Configuration QAbstractHttpServer::http2Configuration() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractHttpServer18http2ConfigurationEv',
    )
    from ..QtNetwork import QHttp2Configuration
    return QHttp2Configuration._cuteOwning(address)

  def configuration(self) -> QHttpServerConfiguration:
    """
    Calls Qt's 'QHttpServerConfiguration QAbstractHttpServer::configuration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserver.html#configuration

    Returns
    -------

    QHttpServerConfiguration
      A new cute QHttpServerConfiguration around the copy Qt gave back.
      Python owns it.
    """
    #  QHttpServerConfiguration QAbstractHttpServer::configuration() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractHttpServer13configurationEv',
    )
    from . import QHttpServerConfiguration
    return QHttpServerConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHttp2Configuration)
  def setHttp2Configuration(
      self,
      configuration: QHttp2Configuration,
  ) -> None:
    """
    Calls Qt's 'void QAbstractHttpServer::setHttp2Configuration(const
    QHttp2Configuration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserver.html#setHttp2Configuration

    Parameters
    ----------

    configuration : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  void QAbstractHttpServer::setHttp2Configuration(const
    #      QHttp2Configuration &configuration)
    self.uglySide.call(
        'ritual_ZN19QAbstractHttpServer21setHttp2ConfigurationERK19QHttp2Co'
        'nfiguration',
        self._valueOf(configuration),
    )

  @overload(QHttpServerConfiguration)
  def setConfiguration(self, config: QHttpServerConfiguration) -> None:
    """
    Calls Qt's 'void QAbstractHttpServer::setConfiguration(const
    QHttpServerConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserver.html#setConfiguration

    Parameters
    ----------

    config : QHttpServerConfiguration
      Passed on as a value: Qt reads the C++ QHttpServerConfiguration, which
      stays Python's own.
    """
    #  void QAbstractHttpServer::setConfiguration(const
    #      QHttpServerConfiguration &config)
    self.uglySide.call(
        'ritual_ZN19QAbstractHttpServer16setConfigurationERK24QHttpServerCo'
        'nfiguration',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QAbstractHttpServer::QAbstractHttpServer(QObject *parent)': the
      class is abstract, so C++ cannot make one, and the C++ class of ours
      does not fill in every function it leaves open.
    - Qt's
      'QAbstractHttpServer::QAbstractHttpServer(QAbstractHttpServerPrivate
      &dd, QObject *parent)': the class is abstract, so C++ cannot make one,
      and the C++ class of ours does not fill in every function it leaves
      open.
    """
    raise NotImplementedError(
        "'QAbstractHttpServer.__init__' has no cute function yet. Qt's "
        "'QAbstractHttpServer::QAbstractHttpServer(QObject *parent)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open. Qt's "
        "'QAbstractHttpServer::QAbstractHttpServer(QAbstractHttpServerPrivat"
        "e &dd, QObject *parent)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  @overload(QTcpServer)
  @overload(NoneType)
  def bind(self, server: Optional[QTcpServer]) -> bool:
    """
    Calls Qt's 'bool QAbstractHttpServer::bind(QTcpServer *server)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracthttpserver.html#bind

    Parameters
    ----------

    server : Optional[QTcpServer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractHttpServer::bind(QTcpServer *server)
    return self.uglySide.call(
        'ritual_ZN19QAbstractHttpServer4bindEP10QTcpServer',
        self._addressOf(server),
    )

  @overload(QLocalServer)
  def bind(self, server: Optional[QLocalServer]) -> bool:
    """
    Calls Qt's 'bool QAbstractHttpServer::bind(QLocalServer *server)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracthttpserver.html#bind

    Parameters
    ----------

    server : Optional[QLocalServer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractHttpServer::bind(QLocalServer *server)
    return self.uglySide.call(
        'ritual_ZN19QAbstractHttpServer4bindEP12QLocalServer',
        self._addressOf(server),
    )

  def d_func(self) -> Optional[QAbstractHttpServerPrivate]:
    """
    Calls Qt's 'QAbstractHttpServerPrivate *QAbstractHttpServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracthttpserver.html#d_func

    Returns
    -------

    Optional[QAbstractHttpServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractHttpServerPrivate *QAbstractHttpServer::d_func()
    address = self.uglySide.call('ritual_ZN19QAbstractHttpServer6d_funcEv')
    from . import QAbstractHttpServerPrivate
    return QAbstractHttpServerPrivate._cuteAt(address)

  @staticmethod
  def handleRequest(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractHttpServer::handleRequest(const QHttpServerRequest
    &request, QHttpServerResponder &responder)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractHttpServer.handleRequest' has no cute function yet. Qt's "
        "'bool QAbstractHttpServer::handleRequest(const QHttpServerRequest "
        "&request, QHttpServerResponder &responder)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def missingHandler(*__, **_) -> Never:
    """
    Qt's 'void QAbstractHttpServer::missingHandler(const QHttpServerRequest
    &request, QHttpServerResponder &responder)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractHttpServer.missingHandler' has no cute function yet. "
        "Qt's 'void QAbstractHttpServer::missingHandler(const "
        "QHttpServerRequest &request, QHttpServerResponder &responder)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def serverPorts(*__, **_) -> Never:
    """
    Qt's 'QList<quint16> QAbstractHttpServer::serverPorts() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractHttpServer.serverPorts' has no cute function yet. Qt's "
        "'QList<quint16> QAbstractHttpServer::serverPorts() const': gives a "
        "type Python has no way to take yet.")
