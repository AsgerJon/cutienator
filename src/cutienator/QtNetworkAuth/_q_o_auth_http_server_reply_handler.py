"""
QOAuthHttpServerReplyHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qoauthhttpserverreplyhandler.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QOAuthOobReplyHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtNetwork import QHostAddress, QSslConfiguration
  from . import QOAuthHttpServerReplyHandlerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QSslConfiguration = WAIT['QSslConfiguration']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuthHttpServerReplyHandler(QOAuthOobReplyHandler):
  """
  The cute side of Qt's QOAuthHttpServerReplyHandler: a plain Python object
  standing in front of one C++ QOAuthHttpServerReplyHandler.

  It is built on the cute 'QOAuthOobReplyHandler', as Qt's
  QOAuthHttpServerReplyHandler is built on Qt's QOAuthOobReplyHandler, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuthHttpServerReplyHandler that has a ritual and
  that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'callback', 'callbackPath', 'setCallbackPath', 'callbackHost',
  'setCallbackHost', 'callbackText', 'setCallbackText', 'port', 'listen',
  'close', 'isListening', 'd_func'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOAuthHttpServerReplyHandler::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QOAuthHttpServerReplyHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QOAuthHttpServerReplyHandler::~QOAuthHttpServerReplyHandler()': the
    destructor: Python never removes a C++ QOAuthHttpServerReplyHandler.
  - Qt's 'const QOAuthHttpServerReplyHandlerPrivate
    *QOAuthHttpServerReplyHandler::d_func() const': takes in Python what
    'QOAuthHttpServerReplyHandlerPrivate
    *QOAuthHttpServerReplyHandler::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QOAuthHttpServerReplyHandler is created at the first use, not by
    'QOAuthHttpServerReplyHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuthHttpServerReplyHandler.
  - Qt tells when it has removed the C++ QOAuthHttpServerReplyHandler. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QOAuthHttpServerReplyHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#tr

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
    #  QString QOAuthHttpServerReplyHandler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QOAuthHttpServerReplyHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuthHttpServerReplyHandler'

  #  A C++ QOAuthHttpServerReplyHandler Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOAuthHttpServerReplyHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOAuthHttpServerReplyHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOAuthHttpServerReplyHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QOAuthHttpServerReplyHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def callback(self) -> str:
    """
    Calls Qt's 'QString QOAuthHttpServerReplyHandler::callback() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#callback

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuthHttpServerReplyHandler::callback() const
    ritual = 'ritual_ZNK28QOAuthHttpServerReplyHandler8callbackEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QOAuthHttpServerReplyHandler8callbackEv'
    return self.uglySide.call(ritual)

  def callbackPath(self) -> str:
    """
    Calls Qt's 'QString QOAuthHttpServerReplyHandler::callbackPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#callbackPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuthHttpServerReplyHandler::callbackPath() const
    return self.uglySide.call(
        'ritual_ZNK28QOAuthHttpServerReplyHandler12callbackPathEv',
    )

  def callbackHost(self) -> str:
    """
    Calls Qt's 'QString QOAuthHttpServerReplyHandler::callbackHost() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#callbackHost

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuthHttpServerReplyHandler::callbackHost() const
    return self.uglySide.call(
        'ritual_ZNK28QOAuthHttpServerReplyHandler12callbackHostEv',
    )

  def callbackText(self) -> str:
    """
    Calls Qt's 'QString QOAuthHttpServerReplyHandler::callbackText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#callbackText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuthHttpServerReplyHandler::callbackText() const
    return self.uglySide.call(
        'ritual_ZNK28QOAuthHttpServerReplyHandler12callbackTextEv',
    )

  def port(self) -> int:
    """
    Calls Qt's 'quint16 QOAuthHttpServerReplyHandler::port() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#port
    """
    #  quint16 QOAuthHttpServerReplyHandler::port() const
    return self.uglySide.call(
        'ritual_ZNK28QOAuthHttpServerReplyHandler4portEv',
    )

  def isListening(self) -> bool:
    """
    Calls Qt's 'bool QOAuthHttpServerReplyHandler::isListening() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#isListening
    """
    #  bool QOAuthHttpServerReplyHandler::isListening() const
    return self.uglySide.call(
        'ritual_ZNK28QOAuthHttpServerReplyHandler11isListeningEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCallbackPath(self, path: str) -> None:
    """
    Calls Qt's 'void QOAuthHttpServerReplyHandler::setCallbackPath(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#setCallbackPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuthHttpServerReplyHandler::setCallbackPath(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN28QOAuthHttpServerReplyHandler15setCallbackPathERK7QStrin'
        'g',
        path,
    )

  @overload(str)
  def setCallbackHost(self, path: str) -> None:
    """
    Calls Qt's 'void QOAuthHttpServerReplyHandler::setCallbackHost(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#setCallbackHost

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuthHttpServerReplyHandler::setCallbackHost(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN28QOAuthHttpServerReplyHandler15setCallbackHostERK7QStrin'
        'g',
        path,
    )

  @overload(str)
  def setCallbackText(self, text: str) -> None:
    """
    Calls Qt's 'void QOAuthHttpServerReplyHandler::setCallbackText(const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#setCallbackText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuthHttpServerReplyHandler::setCallbackText(const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN28QOAuthHttpServerReplyHandler15setCallbackTextERK7QStrin'
        'g',
        text,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(QObject
    #      *parent)
    self._noteCreation(QOAuthHttpServerReplyHandler, lambda: Rituals.call(
        'ritual_ZN28QOAuthHttpServerReplyHandlerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  def __init__(self, port: int, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(quint16 port,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html

    Parameters
    ----------

    port : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(quint16
    #      port, QObject *parent)
    self._noteCreation(QOAuthHttpServerReplyHandler, lambda: Rituals.call(
        'ritual_ZN28QOAuthHttpServerReplyHandlerC1EtP7QObject',
        port, self._addressOf(parent, 'QObject'),
    ))

  @overload(QHostAddress, int)
  @overload(QHostAddress, int, QObject)
  @overload(QHostAddress, int, NoneType)
  def __init__(
      self,
      address: QHostAddress,
      port: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(const
    QHostAddress &address, quint16 port, QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuthHttpServerReplyHandler::QOAuthHttpServerReplyHandler(const
    #      QHostAddress &address, quint16 port, QObject *parent)
    self._noteCreation(QOAuthHttpServerReplyHandler, lambda: Rituals.call(
        'ritual_ZN28QOAuthHttpServerReplyHandlerC1ERK12QHostAddresstP7QObje'
        'ct',
        self._valueOf(address), port, self._addressOf(parent, 'QObject'),
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

  @overload(QHostAddress)
  @overload(QHostAddress, int)
  def listen(self, address: QHostAddress, port: int = 0) -> bool:
    """
    Calls Qt's 'bool QOAuthHttpServerReplyHandler::listen(const QHostAddress
    &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#listen

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QOAuthHttpServerReplyHandler::listen(const QHostAddress &address,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN28QOAuthHttpServerReplyHandler6listenERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(QSslConfiguration, QHostAddress)
  @overload(QSslConfiguration, QHostAddress, int)
  def listen(
      self,
      configuration: QSslConfiguration,
      address: QHostAddress,
      port: int = 0,
  ) -> bool:
    """
    Calls Qt's 'bool QOAuthHttpServerReplyHandler::listen(const
    QSslConfiguration &configuration, const QHostAddress &address, quint16
    port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#listen

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QOAuthHttpServerReplyHandler::listen(const QSslConfiguration
    #      &configuration, const QHostAddress &address, quint16 port)
    return self.uglySide.call(
        'ritual_ZN28QOAuthHttpServerReplyHandler6listenERK17QSslConfigurati'
        'onRK12QHostAddresst',
        self._valueOf(configuration), self._valueOf(address), port,
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QOAuthHttpServerReplyHandler::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#close
    """
    #  void QOAuthHttpServerReplyHandler::close()
    self.uglySide.call('ritual_ZN28QOAuthHttpServerReplyHandler5closeEv')

  def d_func(self) -> Optional[QOAuthHttpServerReplyHandlerPrivate]:
    """
    Calls Qt's 'QOAuthHttpServerReplyHandlerPrivate
    *QOAuthHttpServerReplyHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandler.html#d_func

    Returns
    -------

    Optional[QOAuthHttpServerReplyHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuthHttpServerReplyHandlerPrivate
    #      *QOAuthHttpServerReplyHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN28QOAuthHttpServerReplyHandler6d_funcEv',
    )
    from . import QOAuthHttpServerReplyHandlerPrivate
    return QOAuthHttpServerReplyHandlerPrivate._cuteAt(address)
