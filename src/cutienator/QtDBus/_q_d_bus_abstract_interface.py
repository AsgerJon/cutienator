"""
QDBusAbstractInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusabstractinterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QDBus, QDBusAbstractInterfaceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaMethod, QMetaObject, QVariant
  from . import QDBusAbstractInterfacePrivate, QDBusConnection, QDBusError
  from . import QDBusMessage, QDBusPendingCall
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']
  QMetaMethod = WAIT['QMetaMethod']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusAbstractInterface(QDBusAbstractInterfaceBase):
  """
  The cute side of Qt's QDBusAbstractInterface: a plain Python object
  standing in front of one C++ QDBusAbstractInterface.

  It is built on the cute 'QDBusAbstractInterfaceBase', as Qt's
  QDBusAbstractInterface is built on Qt's QDBusAbstractInterfaceBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusAbstractInterface that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'isValid',
  'connection', 'service', 'path', 'interface', 'lastError', 'setTimeout',
  'timeout', 'setInteractiveAuthorizationAllowed',
  'isInteractiveAuthorizationAllowed', 'call', 'callWithArgumentList',
  'callWithCallback', 'asyncCall', 'asyncCallWithArgumentList',
  'connectNotify', 'disconnectNotify', 'internalPropGet', 'internalPropSet',
  'internalConstCall', 'doCall', 'doAsyncCall', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusAbstractInterface::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusAbstractInterface::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusAbstractInterface::~QDBusAbstractInterface()': the destructor:
    Python never removes a C++ QDBusAbstractInterface.
  - Qt's 'QDBusAbstractInterface::QDBusAbstractInterface(
    QDBusAbstractInterfacePrivate &a0, QObject *parent)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QDBusAbstractInterfacePrivate
    *QDBusAbstractInterface::d_func() const': takes in Python what
    'QDBusAbstractInterfacePrivate *QDBusAbstractInterface::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 38 functions Qt declares: 3 a template; 2 not a gap.

  What to expect
  --------------

  - The C++ QDBusAbstractInterface is created at the first use, not by
    'QDBusAbstractInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusAbstractInterface.
  - Qt tells when it has removed the C++ QDBusAbstractInterface. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QDBusAbstractInterface::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractinterface.html#tr

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
    #  QString QDBusAbstractInterface::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QDBusAbstractInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusAbstractInterface'

  #  A C++ QDBusAbstractInterface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusAbstractInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusAbstractInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusAbstractInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusAbstractInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDBusAbstractInterface::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#isValid
    """
    #  bool QDBusAbstractInterface::isValid() const
    return self.uglySide.call('ritual_ZNK22QDBusAbstractInterface7isValidEv')

  def connection(self) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusAbstractInterface::connection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#connection

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusAbstractInterface::connection() const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusAbstractInterface10connectionEv',
    )
    from . import QDBusConnection
    return QDBusConnection._cuteOwning(address)

  def service(self) -> str:
    """
    Calls Qt's 'QString QDBusAbstractInterface::service() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#service

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusAbstractInterface::service() const
    return self.uglySide.call('ritual_ZNK22QDBusAbstractInterface7serviceEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QDBusAbstractInterface::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractinterface.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusAbstractInterface::path() const
    return self.uglySide.call('ritual_ZNK22QDBusAbstractInterface4pathEv')

  def interface(self) -> str:
    """
    Calls Qt's 'QString QDBusAbstractInterface::interface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#interface

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusAbstractInterface::interface() const
    return self.uglySide.call(
        'ritual_ZNK22QDBusAbstractInterface9interfaceEv',
    )

  def lastError(self) -> QDBusError:
    """
    Calls Qt's 'QDBusError QDBusAbstractInterface::lastError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#lastError

    Returns
    -------

    QDBusError
      A new cute QDBusError around the copy Qt gave back. Python owns it.
    """
    #  QDBusError QDBusAbstractInterface::lastError() const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusAbstractInterface9lastErrorEv',
    )
    from . import QDBusError
    return QDBusError._cuteOwning(address)

  def timeout(self) -> int:
    """
    Calls Qt's 'int QDBusAbstractInterface::timeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#timeout
    """
    #  int QDBusAbstractInterface::timeout() const
    return self.uglySide.call('ritual_ZNK22QDBusAbstractInterface7timeoutEv')

  def isInteractiveAuthorizationAllowed(self) -> bool:
    """
    Calls Qt's 'bool
    QDBusAbstractInterface::isInteractiveAuthorizationAllowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html
    """
    #  bool QDBusAbstractInterface::isInteractiveAuthorizationAllowed() const
    return self.uglySide.call(
        'ritual_ZNK22QDBusAbstractInterface33isInteractiveAuthorizationAllo'
        'wedEv',
    )

  @overload(str)
  @overload(NoneType)
  def internalPropGet(self, propname: Optional[str]) -> QVariant:
    """
    Calls Qt's 'QVariant QDBusAbstractInterface::internalPropGet(const char
    *propname) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#internalPropGet

    Parameters
    ----------

    propname : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDBusAbstractInterface::internalPropGet(const char *propname)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusAbstractInterface15internalPropGetEPKc',
        self._bytesOf(propname),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QDBus.CallMode, str, QList[QVariant])
  def internalConstCall(
      self,
      mode: QDBus.CallMode,
      method: str,
      args: QList[QVariant],
  ) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage
    QDBusAbstractInterface::internalConstCall(QDBus::CallMode mode, const
    QString &method, const QList<QVariant> &args) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#internalConstCall

    Parameters
    ----------

    mode : QDBus.CallMode
      Passed on as its number.

    method : str
      Passed on as it is: a QString is made of it for the call.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusAbstractInterface::internalConstCall(QDBus::CallMode
    #      mode, const QString &method, const QList<QVariant> &args) const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusAbstractInterface17internalConstCallEN5QDBus8Call'
        'ModeERK7QStringRK5QListI8QVariantE',
        mode.value, method, self._valueOf(args),
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void QDBusAbstractInterface::setTimeout(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QDBusAbstractInterface::setTimeout(int timeout)
    self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface10setTimeoutEi', timeout,
    )

  @overload(bool)
  def setInteractiveAuthorizationAllowed(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QDBusAbstractInterface::setInteractiveAuthorizationAllowed(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusAbstractInterface::setInteractiveAuthorizationAllowed(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface34setInteractiveAuthorizationAllo'
        'wedEb',
        enable,
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

  @overload(str, str, str, QDBusConnection, QObject)
  @overload(str, str, str, QDBusConnection, NoneType)
  @overload(str, str, NoneType, QDBusConnection, QObject)
  @overload(str, str, NoneType, QDBusConnection, NoneType)
  def __init__(
      self,
      service: str,
      path: str,
      interface: Optional[str],
      connection: QDBusConnection,
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDBusAbstractInterface::QDBusAbstractInterface(const QString &service,
    const QString &path, const char *interface, const QDBusConnection
    &connection, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#QDBusAbstractInterface

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    connection : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusAbstractInterface::QDBusAbstractInterface(const QString &service,
    #      const QString &path, const char *interface, const QDBusConnection
    #      &connection, QObject *parent)
    self._noteCreation(QDBusAbstractInterface, lambda: Rituals.call(
        'ritual_ZN22QDBusAbstractInterfaceC1ERK7QStringS2_PKcRK15QDBusConne'
        'ctionP7QObject',
        service, path, self._bytesOf(interface), self._valueOf(connection),
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

  @overload(str)
  def call(self, method: str) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusAbstractInterface::call(const QString
    &method)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractinterface.html#call

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusAbstractInterface::call(const QString &method)
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface4callERK7QString', method,
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

  @overload(QDBus.CallMode, str)
  def call(self, mode: QDBus.CallMode, method: str) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusAbstractInterface::call(QDBus::CallMode
    mode, const QString &method)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractinterface.html#call

    Parameters
    ----------

    mode : QDBus.CallMode
      Passed on as its number.

    method : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusAbstractInterface::call(QDBus::CallMode mode, const
    #      QString &method)
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface4callEN5QDBus8CallModeERK7QString',
        mode.value, method,
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

  @overload(QDBus.CallMode, str, QList[QVariant])
  def callWithArgumentList(
      self,
      mode: QDBus.CallMode,
      method: str,
      args: QList[QVariant],
  ) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage
    QDBusAbstractInterface::callWithArgumentList(QDBus::CallMode mode, const
    QString &method, const QList<QVariant> &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#callWithArgumentList

    Parameters
    ----------

    mode : QDBus.CallMode
      Passed on as its number.

    method : str
      Passed on as it is: a QString is made of it for the call.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage
    #      QDBusAbstractInterface::callWithArgumentList(QDBus::CallMode mode,
    #      const QString &method, const QList<QVariant> &args)
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface20callWithArgumentListEN5QDBus8Ca'
        'llModeERK7QStringRK5QListI8QVariantE',
        mode.value, method, self._valueOf(args),
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

  @overload(str, QList[QVariant], QObject, str, str)
  @overload(str, QList[QVariant], QObject, str, NoneType)
  @overload(str, QList[QVariant], QObject, NoneType, str)
  @overload(str, QList[QVariant], QObject, NoneType, NoneType)
  @overload(str, QList[QVariant], NoneType, str, str)
  @overload(str, QList[QVariant], NoneType, str, NoneType)
  @overload(str, QList[QVariant], NoneType, NoneType, str)
  @overload(str, QList[QVariant], NoneType, NoneType, NoneType)
  def callWithCallback(
      self,
      method: str,
      args: QList[QVariant],
      receiver: Optional[QObject],
      member: Optional[str],
      errorSlot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusAbstractInterface::callWithCallback(const QString
    &method, const QList<QVariant> &args, QObject *receiver, const char
    *member, const char *errorSlot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#callWithCallback

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    errorSlot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusAbstractInterface::callWithCallback(const QString &method,
    #      const QList<QVariant> &args, QObject *receiver, const char
    #      *member, const char *errorSlot)
    return self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface16callWithCallbackERK7QStringRK5Q'
        'ListI8QVariantEP7QObjectPKcSB_',
        method, self._valueOf(args), self._addressOf(receiver, 'QObject'),
        self._bytesOf(member), self._bytesOf(errorSlot),
    )

  @overload(str, QList[QVariant], QObject, str)
  @overload(str, QList[QVariant], QObject, NoneType)
  @overload(str, QList[QVariant], NoneType, str)
  @overload(str, QList[QVariant], NoneType, NoneType)
  def callWithCallback(
      self,
      method: str,
      args: QList[QVariant],
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusAbstractInterface::callWithCallback(const QString
    &method, const QList<QVariant> &args, QObject *receiver, const char
    *member)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#callWithCallback

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusAbstractInterface::callWithCallback(const QString &method,
    #      const QList<QVariant> &args, QObject *receiver, const char
    #      *member)
    return self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface16callWithCallbackERK7QStringRK5Q'
        'ListI8QVariantEP7QObjectPKc',
        method, self._valueOf(args), self._addressOf(receiver, 'QObject'),
        self._bytesOf(member),
    )

  @overload(str)
  def asyncCall(self, method: str) -> QDBusPendingCall:
    """
    Calls Qt's 'QDBusPendingCall QDBusAbstractInterface::asyncCall(const
    QString &method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#asyncCall

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusPendingCall
      A new cute QDBusPendingCall around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusPendingCall QDBusAbstractInterface::asyncCall(const QString
    #      &method)
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface9asyncCallERK7QString', method,
    )
    from . import QDBusPendingCall
    return QDBusPendingCall._cuteOwning(address)

  @overload(str, QList[QVariant])
  def asyncCallWithArgumentList(
      self,
      method: str,
      args: QList[QVariant],
  ) -> QDBusPendingCall:
    """
    Calls Qt's 'QDBusPendingCall
    QDBusAbstractInterface::asyncCallWithArgumentList(const QString &method,
    const QList<QVariant> &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QDBusPendingCall
      A new cute QDBusPendingCall around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusPendingCall
    #      QDBusAbstractInterface::asyncCallWithArgumentList(const QString
    #      &method, const QList<QVariant> &args)
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface25asyncCallWithArgumentListERK7QS'
        'tringRK5QListI8QVariantE',
        method, self._valueOf(args),
    )
    from . import QDBusPendingCall
    return QDBusPendingCall._cuteOwning(address)

  @overload(QMetaMethod)
  def connectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QDBusAbstractInterface::connectNotify(const QMetaMethod
    &signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#connectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QDBusAbstractInterface::connectNotify(const QMetaMethod &signal)
    ritual = (
        'ritual_ZN22QDBusAbstractInterface13connectNotifyERK11QMetaMethod')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QDBusAbstractInterface13connectNotifyERK11QMetaMe'
          'thod')
    self.uglySide.call(ritual, self._valueOf(signal))

  @overload(QMetaMethod)
  def disconnectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QDBusAbstractInterface::disconnectNotify(const
    QMetaMethod &signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#disconnectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QDBusAbstractInterface::disconnectNotify(const QMetaMethod
    #      &signal)
    ritual = (
        'ritual_ZN22QDBusAbstractInterface16disconnectNotifyERK11QMetaMetho'
        'd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QDBusAbstractInterface16disconnectNotifyERK11QMet'
          'aMethod')
    self.uglySide.call(ritual, self._valueOf(signal))

  @overload(str, QVariant)
  @overload(NoneType, QVariant)
  def internalPropSet(
      self,
      propname: Optional[str],
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QDBusAbstractInterface::internalPropSet(const char
    *propname, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#internalPropSet

    Parameters
    ----------

    propname : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDBusAbstractInterface::internalPropSet(const char *propname,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface15internalPropSetEPKcRK8QVariant',
        self._bytesOf(propname), self._valueOf(value),
    )

  @overload(QDBus.CallMode, str, QVariant, int)
  @overload(QDBus.CallMode, str, NoneType, int)
  def doCall(
      self,
      mode: QDBus.CallMode,
      method: str,
      args: Optional[QVariant],
      numArgs: int,
  ) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusAbstractInterface::doCall(QDBus::CallMode
    mode, const QString &method, const QVariant *args, size_t numArgs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractinterface.html#doCall

    Parameters
    ----------

    mode : QDBus.CallMode
      Passed on as its number.

    method : str
      Passed on as it is: a QString is made of it for the call.

    args : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    numArgs : int
      Passed on as it is.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusAbstractInterface::doCall(QDBus::CallMode mode,
    #      const QString &method, const QVariant *args, size_t numArgs)
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface6doCallEN5QDBus8CallModeERK7QStri'
        'ngPK8QVariantm',
        mode.value, method, self._addressOf(args), numArgs,
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

  @overload(str, QVariant, int)
  @overload(str, NoneType, int)
  def doAsyncCall(
      self,
      method: str,
      args: Optional[QVariant],
      numArgs: int,
  ) -> QDBusPendingCall:
    """
    Calls Qt's 'QDBusPendingCall QDBusAbstractInterface::doAsyncCall(const
    QString &method, const QVariant *args, size_t numArgs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterface.html#doAsyncCall

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.

    args : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    numArgs : int
      Passed on as it is.

    Returns
    -------

    QDBusPendingCall
      A new cute QDBusPendingCall around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusPendingCall QDBusAbstractInterface::doAsyncCall(const QString
    #      &method, const QVariant *args, size_t numArgs)
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface11doAsyncCallERK7QStringPK8QVaria'
        'ntm',
        method, self._addressOf(args), numArgs,
    )
    from . import QDBusPendingCall
    return QDBusPendingCall._cuteOwning(address)

  def d_func(self) -> Optional[QDBusAbstractInterfacePrivate]:
    """
    Calls Qt's 'QDBusAbstractInterfacePrivate
    *QDBusAbstractInterface::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractinterface.html#d_func

    Returns
    -------

    Optional[QDBusAbstractInterfacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusAbstractInterfacePrivate *QDBusAbstractInterface::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QDBusAbstractInterface6d_funcEv',
    )
    from . import QDBusAbstractInterfacePrivate
    return QDBusAbstractInterfacePrivate._cuteAt(address)
