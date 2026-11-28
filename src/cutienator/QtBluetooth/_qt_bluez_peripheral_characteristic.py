"""
QtBluezPeripheralCharacteristic binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralobjects_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtBluezPeripheralCharacteristic to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QtBluezPeripheralGattObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QtBluezPeripheralCharacteristic(QtBluezPeripheralGattObject):
  """
  The cute side of Qt's QtBluezPeripheralCharacteristic: a plain Python
  object standing in front of one C++ QtBluezPeripheralCharacteristic.

  It is built on the cute 'QtBluezPeripheralGattObject', as Qt's
  QtBluezPeripheralCharacteristic is built on Qt's
  QtBluezPeripheralGattObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtBluezPeripheralCharacteristic that has a ritual
  and that Python can call so far, 4 names in all: 'metaObject',
  'StartNotify', 'StopNotify', 'valueUpdatedByRemote'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtBluezPeripheralCharacteristic::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtBluezPeripheralCharacteristic::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'InterfaceList QtBluezPeripheralCharacteristic::properties() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  9 of the 16 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QtBluezPeripheralCharacteristic.

  What to expect
  --------------

  - The C++ QtBluezPeripheralCharacteristic is created at the first use, not
    by 'QtBluezPeripheralCharacteristic(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtBluezPeripheralCharacteristic.
  - Qt tells when it has removed the C++ QtBluezPeripheralCharacteristic.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtBluezPeripheralCharacteristic that has no cute
    function yet, 'ReadValue', 'WriteValue', '__init__', 'initializeFlags',
    'initializeValue', 'localValueUpdate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluezPeripheralCharacteristic'

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
    *QtBluezPeripheralCharacteristic::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralcharacteristic.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtBluezPeripheralCharacteristic::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QtBluezPeripheralCharacteristic10metaObjectEv',
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
    Qt's
    'QtBluezPeripheralCharacteristic::QtBluezPeripheralCharacteristic(const
    QLowEnergyCharacteristicData &characteristicData, const QString
    &servicePath, quint16 ordinal, QLowEnergyHandle handle, QObject
    *parent)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'maximumAttributeLength'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralCharacteristic.__init__' has no cute function "
        "yet. Qt's "
        "'QtBluezPeripheralCharacteristic::QtBluezPeripheralCharacteristic(c"
        "onst QLowEnergyCharacteristicData &characteristicData, const "
        "QString &servicePath, quint16 ordinal, QLowEnergyHandle handle, "
        "QObject *parent)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'maximumAttributeLength'.")

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

  def StartNotify(self) -> None:
    """
    Calls Qt's 'void QtBluezPeripheralCharacteristic::StartNotify()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralcharacteristic.html#StartNotify
    """
    #  void QtBluezPeripheralCharacteristic::StartNotify()
    self.uglySide.call(
        'ritual_ZN31QtBluezPeripheralCharacteristic11StartNotifyEv',
    )

  def StopNotify(self) -> None:
    """
    Calls Qt's 'void QtBluezPeripheralCharacteristic::StopNotify()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralcharacteristic.html#StopNotify
    """
    #  void QtBluezPeripheralCharacteristic::StopNotify()
    self.uglySide.call(
        'ritual_ZN31QtBluezPeripheralCharacteristic10StopNotifyEv',
    )

  @overload(int, QByteArray)
  def valueUpdatedByRemote(self, handle: int, value: QByteArray) -> None:
    """
    Calls Qt's 'void
    QtBluezPeripheralCharacteristic::valueUpdatedByRemote(QLowEnergyHandle
    handle, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralcharacteristic.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtBluezPeripheralCharacteristic::valueUpdatedByRemote(
    #      QLowEnergyHandle handle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN31QtBluezPeripheralCharacteristic20valueUpdatedByRemoteEt'
        'RK10QByteArray',
        handle, self._valueOf(value),
    )

  @staticmethod
  def ReadValue(*__, **_) -> Never:
    """
    Qt's 'QByteArray QtBluezPeripheralCharacteristic::ReadValue(const
    QVariantMap &options, QString &error)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralCharacteristic.ReadValue' has no cute function "
        "yet. Qt's 'QByteArray "
        "QtBluezPeripheralCharacteristic::ReadValue(const QVariantMap "
        "&options, QString &error)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def WriteValue(*__, **_) -> Never:
    """
    Qt's 'QString QtBluezPeripheralCharacteristic::WriteValue(const
    QByteArray &value, const QVariantMap &options)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralCharacteristic.WriteValue' has no cute function "
        "yet. Qt's 'QString "
        "QtBluezPeripheralCharacteristic::WriteValue(const QByteArray "
        "&value, const QVariantMap &options)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def initializeFlags(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralCharacteristic::initializeFlags(const
    QLowEnergyCharacteristicData &data)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralCharacteristic.initializeFlags' has no cute "
        "function yet. Qt's 'void "
        "QtBluezPeripheralCharacteristic::initializeFlags(const "
        "QLowEnergyCharacteristicData &data)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def initializeValue(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralCharacteristic::initializeValue(const
    QByteArray &value)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralCharacteristic.initializeValue' has no cute "
        "function yet. Qt's 'void "
        "QtBluezPeripheralCharacteristic::initializeValue(const QByteArray "
        "&value)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def localValueUpdate(*__, **_) -> Never:
    """
    Qt's 'bool QtBluezPeripheralCharacteristic::localValueUpdate(const
    QByteArray &value)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralCharacteristic.localValueUpdate' has no cute "
        "function yet. Qt's 'bool "
        "QtBluezPeripheralCharacteristic::localValueUpdate(const QByteArray "
        "&value)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QT_BT_BLUEZ'.")
