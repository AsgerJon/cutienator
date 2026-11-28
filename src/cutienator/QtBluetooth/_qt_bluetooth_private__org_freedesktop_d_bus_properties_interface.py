"""
QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/properties_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtDBus import QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusMessage = WAIT['QDBusMessage']
  QVariant = WAIT['QVariant']


class OrgFreedesktopDBusPropertiesInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface: a plain Python
  object standing in front of one C++
  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface.

  What exists
  -----------

  Every function of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject',
  'staticInterfaceName', 'PropertiesChanged'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::qt_metacast(
    const char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::
    ~OrgFreedesktopDBusPropertiesInterface()': the destructor: Python never
    removes a C++ QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface.
  - Qt's 'QDBusPendingReply<QDBusVariant>
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Get(const
    QString &interface, const QString &name)': gives a type Python has no way
    to take yet.
  - Qt's 'QDBusPendingReply<QVariantMap>
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::GetAll(const
    QString &interface)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Set(const
    QString &interface, const QString &name, const QDBusVariant &value)':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface is
    created at the first use, not by
    'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface that has no
    cute function yet, 'Get', 'GetAll', 'Set', '__init__', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::
    staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesinterface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::
    #      staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterfa'
        'ce19staticInterfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface'

  #  A C++ QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface'

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
    *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesinterface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterf'
        'ace10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::
    OrgFreedesktopDBusPropertiesInterface(const QString &service, const
    QString &path, const QDBusConnection &connection, QObject *parent)':
    leans on
    'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusPropertiesInterface.__init__'"
        " has no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::OrgFree"
        "desktopDBusPropertiesInterface(const QString &service, const "
        "QString &path, const QDBusConnection &connection, QObject "
        "*parent)': leans on "
        "'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::qt_meta"
        "call(QMetaObject::Call, int, void**)', which Qt's source does not "
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

  @overload(str, QMap[str, QVariant], QStringList, QDBusMessage)
  def PropertiesChanged(
      self,
      interface: str,
      changed_properties: QMap[str, QVariant],
      invalidated_properties: QStringList,
      msg: QDBusMessage,
  ) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::
    PropertiesChanged(const QString &interface, const QVariantMap
    &changed_properties, const QStringList &invalidated_properties, const
    QDBusMessage &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesinterface.html

    Parameters
    ----------

    interface : str
      Passed on as it is: a QString is made of it for the call.

    changed_properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    invalidated_properties : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::
    #      PropertiesChanged(const QString &interface, const QVariantMap
    #      &changed_properties, const QStringList &invalidated_properties,
    #      const QDBusMessage &msg)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterfa'
        'ce17PropertiesChangedERK7QStringRK4QMapIS1_8QVariantERK5QListIS1_E'
        'RK12QDBusMessage',
        interface, self._valueOf(changed_properties),
        self._valueOf(invalidated_properties), self._valueOf(msg),
    )

  @staticmethod
  def Get(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<QDBusVariant>
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Get(const
    QString &interface, const QString &name)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusPropertiesInterface.Get' has "
        "no cute function yet. Qt's 'QDBusPendingReply<QDBusVariant> "
        "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Get(cons"
        "t QString &interface, const QString &name)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def GetAll(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<QVariantMap>
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::GetAll(const
    QString &interface)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusPropertiesInterface.GetAll' "
        "has no cute function yet. Qt's 'QDBusPendingReply<QVariantMap> "
        "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::GetAll(c"
        "onst QString &interface)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def Set(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Set(const
    QString &interface, const QString &name, const QDBusVariant &value)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusPropertiesInterface.Set' has "
        "no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Set(cons"
        "t QString &interface, const QString &name, const QDBusVariant "
        "&value)': gives a type Python has no way to take yet.")
