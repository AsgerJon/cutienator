"""
QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/gattchar1_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface to be
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

  from ..QtCore import QByteArray, QMetaObject
  from ..QtDBus import QDBusObjectPath


class OrgBluezGattCharacteristic1Interface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface: a plain Python
  object standing in front of one C++
  QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface.

  What exists
  -----------

  Every function of Qt's
  QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface that has a ritual
  and that Python can call so far, 7 names in all: 'metaObject',
  'staticInterfaceName', 'flags', 'notifying', 'service', 'uUID', 'value'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::qt_metacast(
    const char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::
    ~OrgBluezGattCharacteristic1Interface()': the destructor: Python never
    removes a C++ QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface.
  - Qt's 'QDBusPendingReply<QByteArray>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::ReadValue(const
    QVariantMap &options)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StartNotify()':
    gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StopNotify()':
    gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::WriteValue(
    const QByteArray &value, const QVariantMap &options)': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface is
    created at the first use, not by
    'QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface that has no cute
    function yet, 'ReadValue', 'StartNotify', 'StopNotify', 'WriteValue',
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
    *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::
    staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattcharacteristic1interface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::
    #      staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interfac'
        'e19staticInterfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface'

  #  A C++ QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezGattCharacteristic1Interface'

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
    *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattcharacteristic1interface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interfa'
        'ce10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def flags(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattcharacteristic1interface.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::flags()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interfa'
        'ce5flagsEv',
    )
    return QStringList._cuteOwning(address)

  def notifying(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::notifying()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattcharacteristic1interface.html
    """
    #  bool QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::
    #      notifying() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interfa'
        'ce9notifyingEv',
    )

  def service(self) -> QDBusObjectPath:
    """
    Calls Qt's 'QDBusObjectPath
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::service()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattcharacteristic1interface.html

    Returns
    -------

    QDBusObjectPath
      A new cute QDBusObjectPath around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusObjectPath
    #      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::service(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interfa'
        'ce7serviceEv',
    )
    from ..QtDBus import QDBusObjectPath
    return QDBusObjectPath._cuteOwning(address)

  def uUID(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::uUID() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattcharacteristic1interface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::uUID()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interfa'
        'ce4uUIDEv',
    )

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattcharacteristic1interface.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::value()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interfa'
        'ce5valueEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
    Qt's 'QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::
    OrgBluezGattCharacteristic1Interface(const QString &service, const
    QString &path, const QDBusConnection &connection, QObject *parent)':
    leans on
    'QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezGattCharacteristic1Interface.__init__' "
        "has no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::OrgBluez"
        "GattCharacteristic1Interface(const QString &service, const QString "
        "&path, const QDBusConnection &connection, QObject *parent)': leans "
        "on "
        "'QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::qt_metac"
        "all(QMetaObject::Call, int, void**)', which Qt's source does not "
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
  def ReadValue(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<QByteArray>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::ReadValue(const
    QVariantMap &options)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezGattCharacteristic1Interface.ReadValue'"
        " has no cute function yet. Qt's 'QDBusPendingReply<QByteArray> "
        "QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::ReadValue"
        "(const QVariantMap &options)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def StartNotify(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StartNotify()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezGattCharacteristic1Interface.StartNotif"
        "y' has no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StartNoti"
        "fy()': gives a type Python has no way to take yet.")

  @staticmethod
  def StopNotify(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StopNotify()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezGattCharacteristic1Interface.StopNotify"
        "' has no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StopNotif"
        "y()': gives a type Python has no way to take yet.")

  @staticmethod
  def WriteValue(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::WriteValue(
    const QByteArray &value, const QVariantMap &options)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezGattCharacteristic1Interface.WriteValue"
        "' has no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::WriteValu"
        "e(const QByteArray &value, const QVariantMap &options)': gives a "
        "type Python has no way to take yet.")
