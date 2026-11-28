"""
QDBusServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDBusConnection, QDBusError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusServer(QObject):
  """
  The cute side of Qt's QDBusServer: a plain Python object standing in front
  of one C++ QDBusServer.

  It is built on the cute 'QObject', as Qt's QDBusServer is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusServer that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'isConnected',
  'lastError', 'address', 'setAnonymousAuthenticationAllowed',
  'isAnonymousAuthenticationAllowed', 'newConnection'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusServer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDBusServer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusServer::~QDBusServer()': the destructor: Python never removes
    a C++ QDBusServer.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDBusServer is created at the first use, not by
    'QDBusServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusServer.
  - Qt tells when it has removed the C++ QDBusServer. Every call on the cute
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
    Calls Qt's 'QString QDBusServer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#tr

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
    #  QString QDBusServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QDBusServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusServer'

  #  A C++ QDBusServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusServer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusServer::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QDBusServer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isConnected(self) -> bool:
    """
    Calls Qt's 'bool QDBusServer::isConnected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#isConnected
    """
    #  bool QDBusServer::isConnected() const
    return self.uglySide.call('ritual_ZNK11QDBusServer11isConnectedEv')

  def lastError(self) -> QDBusError:
    """
    Calls Qt's 'QDBusError QDBusServer::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#lastError

    Returns
    -------

    QDBusError
      A new cute QDBusError around the copy Qt gave back. Python owns it.
    """
    #  QDBusError QDBusServer::lastError() const
    address = self.uglySide.call('ritual_ZNK11QDBusServer9lastErrorEv')
    from . import QDBusError
    return QDBusError._cuteOwning(address)

  def address(self) -> str:
    """
    Calls Qt's 'QString QDBusServer::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#address

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusServer::address() const
    return self.uglySide.call('ritual_ZNK11QDBusServer7addressEv')

  def isAnonymousAuthenticationAllowed(self) -> bool:
    """
    Calls Qt's 'bool QDBusServer::isAnonymousAuthenticationAllowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusserver.html#isAnonymousAuthenticationAllowed
    """
    #  bool QDBusServer::isAnonymousAuthenticationAllowed() const
    return self.uglySide.call(
        'ritual_ZNK11QDBusServer32isAnonymousAuthenticationAllowedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAnonymousAuthenticationAllowed(self, value: bool) -> None:
    """
    Calls Qt's 'void QDBusServer::setAnonymousAuthenticationAllowed(bool
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusserver.html#setAnonymousAuthenticationAllowed

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QDBusServer::setAnonymousAuthenticationAllowed(bool value)
    self.uglySide.call(
        'ritual_ZN11QDBusServer33setAnonymousAuthenticationAllowedEb', value,
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

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, address: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QDBusServer::QDBusServer(const QString
    &address, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#QDBusServer

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDBusServer::QDBusServer(const QString &address, QObject *parent)
    self._noteCreation(QDBusServer, lambda: Rituals.call(
        'ritual_ZN11QDBusServerC1ERK7QStringP7QObject',
        address, self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QDBusServer::QDBusServer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#QDBusServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDBusServer::QDBusServer(QObject *parent)
    self._noteCreation(QDBusServer, lambda: Rituals.call(
        'ritual_ZN11QDBusServerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QDBusConnection)
  def newConnection(self, connection: QDBusConnection) -> None:
    """
    Calls Qt's 'void QDBusServer::newConnection(const QDBusConnection
    &connection)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusserver.html#newConnection

    Parameters
    ----------

    connection : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.
    """
    #  void QDBusServer::newConnection(const QDBusConnection &connection)
    self.uglySide.call(
        'ritual_ZN11QDBusServer13newConnectionERK15QDBusConnection',
        self._valueOf(connection),
    )
