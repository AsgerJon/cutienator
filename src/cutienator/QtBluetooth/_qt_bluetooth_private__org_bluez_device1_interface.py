"""
QtBluetoothPrivate::OrgBluezDevice1Interface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/device1_bluez5_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezDevice1Interface to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtDBus import QDBusObjectPath


class OrgBluezDevice1Interface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtBluetoothPrivate::OrgBluezDevice1Interface: a plain
  Python object standing in front of one C++
  QtBluetoothPrivate::OrgBluezDevice1Interface.

  What exists
  -----------

  Every function of Qt's QtBluetoothPrivate::OrgBluezDevice1Interface that
  has a ritual and that Python can call so far, 22 names in all:
  'metaObject', 'staticInterfaceName', 'adapter', 'address', 'alias',
  'setAlias', 'appearance', 'blocked', 'setBlocked', 'classProperty',
  'connected', 'icon', 'legacyPairing', 'modalias', 'name', 'paired', 'rSSI',
  'servicesResolved', 'trusted', 'setTrusted', 'txPower', 'uUIDs'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezDevice1Interface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgBluezDevice1Interface::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QtBluetoothPrivate::OrgBluezDevice1Interface::~OrgBluezDevice1Interface(
    )': the destructor: Python never removes a C++
    QtBluetoothPrivate::OrgBluezDevice1Interface.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::CancelPairing()': gives a
    type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::Connect()': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::ConnectProfile(const
    QString &UUID)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::Disconnect()': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::DisconnectProfile(const
    QString &UUID)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::Pair()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 37 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate; 1 leans on
  'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray const&)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken; 1 leans on
  'qRegisterNormalizedMetaType_ServiceDataList(QByteArray const&)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezDevice1Interface is created at the
    first use, not by 'QtBluetoothPrivate::OrgBluezDevice1Interface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezDevice1Interface.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezDevice1Interface. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QtBluetoothPrivate::OrgBluezDevice1Interface that has
    no cute function yet, 'CancelPairing', 'Connect', 'ConnectProfile',
    'Disconnect', 'DisconnectProfile', 'Pair', '__init__',
    'manufacturerData', 'serviceData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QtBluetoothPrivate::OrgBluezDevice1Interface::staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtBluetoothPrivate::OrgBluezDevice1Interface::
    #      staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface19staticInt'
        'erfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezDevice1Interface'

  #  A C++ QtBluetoothPrivate::OrgBluezDevice1Interface Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezDevice1Interface'

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
    *QtBluetoothPrivate::OrgBluezDevice1Interface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezDevice1Interface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface10metaObje'
        'ctEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def adapter(self) -> QDBusObjectPath:
    """
    Calls Qt's 'QDBusObjectPath
    QtBluetoothPrivate::OrgBluezDevice1Interface::adapter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    QDBusObjectPath
      A new cute QDBusObjectPath around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusObjectPath
    #      QtBluetoothPrivate::OrgBluezDevice1Interface::adapter() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7adapterEv',
    )
    from ..QtDBus import QDBusObjectPath
    return QDBusObjectPath._cuteOwning(address)

  def address(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezDevice1Interface::address() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezDevice1Interface::address() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7addressEv',
    )

  def alias(self) -> str:
    """
    Calls Qt's 'QString QtBluetoothPrivate::OrgBluezDevice1Interface::alias()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezDevice1Interface::alias() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface5aliasEv',
    )

  def appearance(self) -> int:
    """
    Calls Qt's 'ushort
    QtBluetoothPrivate::OrgBluezDevice1Interface::appearance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  ushort QtBluetoothPrivate::OrgBluezDevice1Interface::appearance()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface10appearan'
        'ceEv',
    )

  def blocked(self) -> bool:
    """
    Calls Qt's 'bool QtBluetoothPrivate::OrgBluezDevice1Interface::blocked()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezDevice1Interface::blocked() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7blockedEv',
    )

  def classProperty(self) -> int:
    """
    Calls Qt's 'uint
    QtBluetoothPrivate::OrgBluezDevice1Interface::classProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  uint QtBluetoothPrivate::OrgBluezDevice1Interface::classProperty()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface13classPro'
        'pertyEv',
    )

  def connected(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezDevice1Interface::connected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezDevice1Interface::connected() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface9connected'
        'Ev',
    )

  def icon(self) -> str:
    """
    Calls Qt's 'QString QtBluetoothPrivate::OrgBluezDevice1Interface::icon()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezDevice1Interface::icon() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface4iconEv',
    )

  def legacyPairing(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezDevice1Interface::legacyPairing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezDevice1Interface::legacyPairing()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface13legacyPa'
        'iringEv',
    )

  def modalias(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezDevice1Interface::modalias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezDevice1Interface::modalias() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface8modaliasE'
        'v',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QtBluetoothPrivate::OrgBluezDevice1Interface::name()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezDevice1Interface::name() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface4nameEv',
    )

  def paired(self) -> bool:
    """
    Calls Qt's 'bool QtBluetoothPrivate::OrgBluezDevice1Interface::paired()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezDevice1Interface::paired() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface6pairedEv',
    )

  def rSSI(self) -> int:
    """
    Calls Qt's 'short QtBluetoothPrivate::OrgBluezDevice1Interface::rSSI()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  short QtBluetoothPrivate::OrgBluezDevice1Interface::rSSI() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface4rSSIEv',
    )

  def servicesResolved(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezDevice1Interface::servicesResolved() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezDevice1Interface::servicesResolved()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface16services'
        'ResolvedEv',
    )

  def trusted(self) -> bool:
    """
    Calls Qt's 'bool QtBluetoothPrivate::OrgBluezDevice1Interface::trusted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezDevice1Interface::trusted() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7trustedEv',
    )

  def txPower(self) -> int:
    """
    Calls Qt's 'short QtBluetoothPrivate::OrgBluezDevice1Interface::txPower()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html
    """
    #  short QtBluetoothPrivate::OrgBluezDevice1Interface::txPower() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7txPowerEv',
    )

  def uUIDs(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QtBluetoothPrivate::OrgBluezDevice1Interface::uUIDs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtBluetoothPrivate::OrgBluezDevice1Interface::uUIDs()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface5uUIDsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAlias(self, value: str) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezDevice1Interface::setAlias(const QString
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtBluetoothPrivate::OrgBluezDevice1Interface::setAlias(const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface8setAliasER'
        'K7QString',
        value,
    )

  @overload(bool)
  def setBlocked(self, value: bool) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezDevice1Interface::setBlocked(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezDevice1Interface::setBlocked(bool
    #      value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface10setBlocke'
        'dEb',
        value,
    )

  @overload(bool)
  def setTrusted(self, value: bool) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezDevice1Interface::setTrusted(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezdevice1interface.html

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezDevice1Interface::setTrusted(bool
    #      value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface10setTruste'
        'dEb',
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
    Qt's
    'QtBluetoothPrivate::OrgBluezDevice1Interface::OrgBluezDevice1Interface(
    const QString &service, const QString &path, const QDBusConnection
    &connection, QObject *parent)': leans on
    'QtBluetoothPrivate::OrgBluezDevice1Interface::qt_metacall(QMetaObject::
    Call, int, void**)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.__init__' has no cute "
        "function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezDevice1Interface::OrgBluezDevice1Inter"
        "face(const QString &service, const QString &path, const "
        "QDBusConnection &connection, QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgBluezDevice1Interface::qt_metacall(QMetaObj"
        "ect::Call, int, void**)', which Qt's source does not mark for use "
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
  def CancelPairing(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::CancelPairing()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.CancelPairing' has no "
        "cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::CancelPairing()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def Connect(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::Connect()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.Connect' has no cute "
        "function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::Connect()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def ConnectProfile(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::ConnectProfile(const
    QString &UUID)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.ConnectProfile' has "
        "no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::ConnectProfile(const "
        "QString &UUID)': gives a type Python has no way to take yet.")

  @staticmethod
  def Disconnect(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::Disconnect()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.Disconnect' has no "
        "cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::Disconnect()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def DisconnectProfile(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::DisconnectProfile(const
    QString &UUID)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.DisconnectProfile' "
        "has no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::DisconnectProfile(con"
        "st QString &UUID)': gives a type Python has no way to take yet.")

  @staticmethod
  def Pair(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezDevice1Interface::Pair()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.Pair' has no cute "
        "function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::Pair()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def manufacturerData(*__, **_) -> Never:
    """
    Qt's 'ManufacturerDataList
    QtBluetoothPrivate::OrgBluezDevice1Interface::manufacturerData() const':
    leans on 'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.manufacturerData' has "
        "no cute function yet. Qt's 'ManufacturerDataList "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::manufacturerData() "
        "const': leans on "
        "'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def serviceData(*__, **_) -> Never:
    """
    Qt's 'ServiceDataList
    QtBluetoothPrivate::OrgBluezDevice1Interface::serviceData() const': leans
    on 'qRegisterNormalizedMetaType_ServiceDataList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezDevice1Interface.serviceData' has no "
        "cute function yet. Qt's 'ServiceDataList "
        "QtBluetoothPrivate::OrgBluezDevice1Interface::serviceData() "
        "const': leans on "
        "'qRegisterNormalizedMetaType_ServiceDataList(QByteArray const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
