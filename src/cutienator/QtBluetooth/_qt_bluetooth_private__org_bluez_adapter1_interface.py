"""
QtBluetoothPrivate::OrgBluezAdapter1Interface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/adapter1_bluez5_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezAdapter1Interface to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class OrgBluezAdapter1Interface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtBluetoothPrivate::OrgBluezAdapter1Interface: a
  plain Python object standing in front of one C++
  QtBluetoothPrivate::OrgBluezAdapter1Interface.

  What exists
  -----------

  Every function of Qt's QtBluetoothPrivate::OrgBluezAdapter1Interface that
  has a ritual and that Python can call so far, 20 names in all:
  'metaObject', 'staticInterfaceName', 'address', 'alias', 'setAlias',
  'classProperty', 'discoverable', 'setDiscoverable', 'discoverableTimeout',
  'setDiscoverableTimeout', 'discovering', 'modalias', 'name', 'pairable',
  'setPairable', 'pairableTimeout', 'setPairableTimeout', 'powered',
  'setPowered', 'uUIDs'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtBluetoothPrivate::OrgBluezAdapter1Interface::
    ~OrgBluezAdapter1Interface()': the destructor: Python never removes a C++
    QtBluetoothPrivate::OrgBluezAdapter1Interface.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::RemoveDevice(const
    QDBusObjectPath &device)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::SetDiscoveryFilter(const
    QVariantMap &properties)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::StartDiscovery()': gives a
    type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::StopDiscovery()': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 31 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezAdapter1Interface is created at the
    first use, not by 'QtBluetoothPrivate::OrgBluezAdapter1Interface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezAdapter1Interface.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezAdapter1Interface. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QtBluetoothPrivate::OrgBluezAdapter1Interface that has
    no cute function yet, 'RemoveDevice', 'SetDiscoveryFilter',
    'StartDiscovery', 'StopDiscovery', '__init__', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QtBluetoothPrivate::OrgBluezAdapter1Interface::staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtBluetoothPrivate::OrgBluezAdapter1Interface::
    #      staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface19staticIn'
        'terfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezAdapter1Interface'

  #  A C++ QtBluetoothPrivate::OrgBluezAdapter1Interface Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezAdapter1Interface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtBluetoothPrivate::OrgBluezAdapter1Interface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezAdapter1Interface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface10metaObj'
        'ectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def address(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezAdapter1Interface::address() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::address() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface7addressE'
        'v',
    )

  def alias(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezAdapter1Interface::alias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::alias() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface5aliasEv',
    )

  def classProperty(self) -> int:
    """
    Calls Qt's 'uint
    QtBluetoothPrivate::OrgBluezAdapter1Interface::classProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html
    """
    #  uint QtBluetoothPrivate::OrgBluezAdapter1Interface::classProperty()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface13classPr'
        'opertyEv',
    )

  def discoverable(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezAdapter1Interface::discoverable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::discoverable()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface12discove'
        'rableEv',
    )

  def discoverableTimeout(self) -> int:
    """
    Calls Qt's 'uint
    QtBluetoothPrivate::OrgBluezAdapter1Interface::discoverableTimeout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html
    """
    #  uint QtBluetoothPrivate::OrgBluezAdapter1Interface::
    #      discoverableTimeout() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface19discove'
        'rableTimeoutEv',
    )

  def discovering(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezAdapter1Interface::discovering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::discovering()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface11discove'
        'ringEv',
    )

  def modalias(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezAdapter1Interface::modalias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::modalias()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface8modalias'
        'Ev',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QtBluetoothPrivate::OrgBluezAdapter1Interface::name()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::name() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface4nameEv',
    )

  def pairable(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezAdapter1Interface::pairable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::pairable() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface8pairable'
        'Ev',
    )

  def pairableTimeout(self) -> int:
    """
    Calls Qt's 'uint
    QtBluetoothPrivate::OrgBluezAdapter1Interface::pairableTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html
    """
    #  uint QtBluetoothPrivate::OrgBluezAdapter1Interface::pairableTimeout()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface15pairabl'
        'eTimeoutEv',
    )

  def powered(self) -> bool:
    """
    Calls Qt's 'bool QtBluetoothPrivate::OrgBluezAdapter1Interface::powered()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::powered() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface7poweredE'
        'v',
    )

  def uUIDs(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QtBluetoothPrivate::OrgBluezAdapter1Interface::uUIDs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtBluetoothPrivate::OrgBluezAdapter1Interface::uUIDs()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface5uUIDsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAlias(self, value: str) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezAdapter1Interface::setAlias(const QString
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setAlias(const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface8setAliasE'
        'RK7QString',
        value,
    )

  @overload(bool)
  def setDiscoverable(self, value: bool) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezAdapter1Interface::setDiscoverable(bool
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setDiscoverable(
    #      bool value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface15setDisco'
        'verableEb',
        value,
    )

  @overload(int)
  def setDiscoverableTimeout(self, value: int) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezAdapter1Interface::setDiscoverableTimeout(
    uint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezAdapter1Interface::
    #      setDiscoverableTimeout(uint value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface22setDisco'
        'verableTimeoutEj',
        value,
    )

  @overload(bool)
  def setPairable(self, value: bool) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezAdapter1Interface::setPairable(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setPairable(bool
    #      value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface11setPaira'
        'bleEb',
        value,
    )

  @overload(int)
  def setPairableTimeout(self, value: int) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezAdapter1Interface::setPairableTimeout(uint
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void
    #      QtBluetoothPrivate::OrgBluezAdapter1Interface::setPairableTimeout(
    #      uint value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface18setPaira'
        'bleTimeoutEj',
        value,
    )

  @overload(bool)
  def setPowered(self, value: bool) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezAdapter1Interface::setPowered(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezadapter1interface.html

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setPowered(bool
    #      value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface10setPower'
        'edEb',
        value,
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
    Qt's 'QtBluetoothPrivate::OrgBluezAdapter1Interface::
    OrgBluezAdapter1Interface(const QString &service, const QString &path,
    const QDBusConnection &connection, QObject *parent)': leans on
    'QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezAdapter1Interface.__init__' has no "
        "cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezAdapter1Interface::OrgBluezAdapter1Int"
        "erface(const QString &service, const QString &path, const "
        "QDBusConnection &connection, QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacall(QMetaOb"
        "ject::Call, int, void**)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

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
  def RemoveDevice(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::RemoveDevice(const
    QDBusObjectPath &device)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezAdapter1Interface.RemoveDevice' has no "
        "cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezAdapter1Interface::RemoveDevice(const "
        "QDBusObjectPath &device)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def SetDiscoveryFilter(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::SetDiscoveryFilter(const
    QVariantMap &properties)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezAdapter1Interface.SetDiscoveryFilter' "
        "has no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezAdapter1Interface::SetDiscoveryFilter(c"
        "onst QVariantMap &properties)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def StartDiscovery(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::StartDiscovery()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezAdapter1Interface.StartDiscovery' has "
        "no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezAdapter1Interface::StartDiscovery()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def StopDiscovery(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezAdapter1Interface::StopDiscovery()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezAdapter1Interface.StopDiscovery' has "
        "no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezAdapter1Interface::StopDiscovery()': "
        "gives a type Python has no way to take yet.")
