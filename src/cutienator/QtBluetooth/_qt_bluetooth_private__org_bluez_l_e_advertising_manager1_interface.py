"""
QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/leadvertisingmanager1_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class OrgBluezLEAdvertisingManager1Interface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface: a plain Python
  object standing in front of one C++
  QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface.

  What exists
  -----------

  Every function of Qt's
  QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject',
  'staticInterfaceName', 'activeInstances', 'supportedIncludes',
  'supportedInstances'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_metacast(
    const char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    ~OrgBluezLEAdvertisingManager1Interface()': the destructor: Python never
    removes a C++ QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    RegisterAdvertisement(const QDBusObjectPath &advertisement, const
    QVariantMap &options)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    UnregisterAdvertisement(const QDBusObjectPath &advertisement)': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface is
    created at the first use, not by
    'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface that has no
    cute function yet, 'RegisterAdvertisement', 'UnregisterAdvertisement',
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisingmanager1interface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    #      staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interf'
        'ace19staticInterfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface'

  #  A C++ QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface'

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
    *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisingmanager1interface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Inter'
        'face10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeInstances(self) -> int:
    """
    Calls Qt's 'uchar
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    activeInstances() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisingmanager1interface.html
    """
    #  uchar QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    #      activeInstances() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Inter'
        'face15activeInstancesEv',
    )

  def supportedIncludes(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    supportedIncludes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisingmanager1interface.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    #      supportedIncludes() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Inter'
        'face17supportedIncludesEv',
    )
    return QStringList._cuteOwning(address)

  def supportedInstances(self) -> int:
    """
    Calls Qt's 'uchar
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    supportedInstances() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisingmanager1interface.html
    """
    #  uchar QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    #      supportedInstances() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Inter'
        'face18supportedInstancesEv',
    )

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
    Qt's 'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    OrgBluezLEAdvertisingManager1Interface(const QString &service, const
    QString &path, const QDBusConnection &connection, QObject *parent)':
    leans on
    'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezLEAdvertisingManager1Interface.__init__"
        "' has no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::OrgBlu"
        "ezLEAdvertisingManager1Interface(const QString &service, const "
        "QString &path, const QDBusConnection &connection, QObject "
        "*parent)': leans on "
        "'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_met"
        "acall(QMetaObject::Call, int, void**)', which Qt's source does not "
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

  @staticmethod
  def RegisterAdvertisement(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    RegisterAdvertisement(const QDBusObjectPath &advertisement, const
    QVariantMap &options)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezLEAdvertisingManager1Interface.Register"
        "Advertisement' has no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::Registe"
        "rAdvertisement(const QDBusObjectPath &advertisement, const "
        "QVariantMap &options)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def UnregisterAdvertisement(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::
    UnregisterAdvertisement(const QDBusObjectPath &advertisement)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezLEAdvertisingManager1Interface.Unregist"
        "erAdvertisement' has no cute function yet. Qt's "
        "'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::Unregis"
        "terAdvertisement(const QDBusObjectPath &advertisement)': gives a "
        "type Python has no way to take yet.")
