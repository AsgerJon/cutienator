"""
QtBluezPeripheralApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralapplication_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtBluezPeripheralApplication to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QtBluezPeripheralApplication(QObject):
  """
  The cute side of Qt's QtBluezPeripheralApplication: a plain Python object
  standing in front of one C++ QtBluezPeripheralApplication.

  It is built on the cute 'QObject', as Qt's QtBluezPeripheralApplication is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtBluezPeripheralApplication that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject',
  'registrationNeeded', 'errorOccurred', 'registered',
  'remoteDeviceAccessEvent', 'characteristicValueUpdatedByRemote',
  'descriptorValueUpdatedByRemote'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtBluezPeripheralApplication::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtBluezPeripheralApplication::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtBluezPeripheralApplication::~QtBluezPeripheralApplication()': the
    destructor: Python never removes a C++ QtBluezPeripheralApplication.
  - Qt's 'ManagedObjectList
    QtBluezPeripheralApplication::GetManagedObjects()': gives a type Python
    has no way to take yet.
  - Qt's 'QLowEnergyHandle
    QtBluezPeripheralApplication::handleForCharacteristic(QBluetoothUuid
    uuid, QSharedPointer<QLowEnergyServicePrivate> service)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QLowEnergyHandle
    QtBluezPeripheralApplication::handleForDescriptor(QBluetoothUuid uuid,
    QSharedPointer<QLowEnergyServicePrivate> service, QLowEnergyHandle
    characteristicHandle)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  12 of the 25 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QtBluezPeripheralApplication; 2 leans on
  'QtBluezPeripheralGattObject.

  What to expect
  --------------

  - The C++ QtBluezPeripheralApplication is created at the first use, not by
    'QtBluezPeripheralApplication(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtBluezPeripheralApplication.
  - Qt tells when it has removed the C++ QtBluezPeripheralApplication. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtBluezPeripheralApplication that has no cute function
    yet, 'GetManagedObjects', '__init__', 'addService',
    'handleForCharacteristic', 'handleForDescriptor',
    'localCharacteristicWrite', 'localDescriptorWrite',
    'registerApplication', 'registerServices', 'reset',
    'unregisterApplication', 'unregisterServices', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluezPeripheralApplication'

  #  A C++ QtBluezPeripheralApplication Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluezPeripheralApplication'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtBluezPeripheralApplication::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralapplication.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtBluezPeripheralApplication::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QtBluezPeripheralApplication10metaObjectEv',
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
    Qt's 'QtBluezPeripheralApplication::QtBluezPeripheralApplication(const
    QString &localAdapterPath, QObject *parent)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'OrgFreedesktopDBusObjectManagerAdaptor'; did you mean
    'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor'?.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.__init__' has no cute function yet. "
        "Qt's "
        "'QtBluezPeripheralApplication::QtBluezPeripheralApplication(const "
        "QString &localAdapterPath, QObject *parent)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name "
        "'OrgFreedesktopDBusObjectManagerAdaptor'; did you mean "
        "'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor'?.")

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

  def registrationNeeded(self) -> bool:
    """
    Calls Qt's 'bool QtBluezPeripheralApplication::registrationNeeded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralapplication.html
    """
    #  bool QtBluezPeripheralApplication::registrationNeeded()
    return self.uglySide.call(
        'ritual_ZN28QtBluezPeripheralApplication18registrationNeededEv',
    )

  def errorOccurred(self) -> None:
    """
    Calls Qt's 'void QtBluezPeripheralApplication::errorOccurred()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralapplication.html#errorOccurred
    """
    #  void QtBluezPeripheralApplication::errorOccurred()
    self.uglySide.call(
        'ritual_ZN28QtBluezPeripheralApplication13errorOccurredEv',
    )

  def registered(self) -> None:
    """
    Calls Qt's 'void QtBluezPeripheralApplication::registered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralapplication.html#registered
    """
    #  void QtBluezPeripheralApplication::registered()
    self.uglySide.call(
        'ritual_ZN28QtBluezPeripheralApplication10registeredEv',
    )

  @overload(str, int)
  def remoteDeviceAccessEvent(
      self,
      remoteDeviceObjectPath: str,
      mtu: int,
  ) -> None:
    """
    Calls Qt's 'void
    QtBluezPeripheralApplication::remoteDeviceAccessEvent(const QString
    &remoteDeviceObjectPath, quint16 mtu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralapplication.html

    Parameters
    ----------

    remoteDeviceObjectPath : str
      Passed on as it is: a QString is made of it for the call.

    mtu : int
      Passed on as it is.
    """
    #  void QtBluezPeripheralApplication::remoteDeviceAccessEvent(const
    #      QString &remoteDeviceObjectPath, quint16 mtu)
    self.uglySide.call(
        'ritual_ZN28QtBluezPeripheralApplication23remoteDeviceAccessEventER'
        'K7QStringt',
        remoteDeviceObjectPath, mtu,
    )

  @overload(int, QByteArray)
  def characteristicValueUpdatedByRemote(
      self,
      handle: int,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QtBluezPeripheralApplication::characteristicValueUpdatedByRemote(
    QLowEnergyHandle handle, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralapplication.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtBluezPeripheralApplication::characteristicValueUpdatedByRemote(
    #      QLowEnergyHandle handle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN28QtBluezPeripheralApplication34characteristicValueUpdate'
        'dByRemoteEtRK10QByteArray',
        handle, self._valueOf(value),
    )

  @overload(int, int, QByteArray)
  def descriptorValueUpdatedByRemote(
      self,
      characteristicHandle: int,
      descriptorHandle: int,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QtBluezPeripheralApplication::descriptorValueUpdatedByRemote(
    QLowEnergyHandle characteristicHandle, QLowEnergyHandle descriptorHandle,
    const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralapplication.html

    Parameters
    ----------

    characteristicHandle : int
      Passed on as it is.

    descriptorHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtBluezPeripheralApplication::descriptorValueUpdatedByRemote(
    #      QLowEnergyHandle characteristicHandle, QLowEnergyHandle
    #      descriptorHandle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN28QtBluezPeripheralApplication30descriptorValueUpdatedByR'
        'emoteEttRK10QByteArray',
        characteristicHandle, descriptorHandle, self._valueOf(value),
    )

  @staticmethod
  def GetManagedObjects(*__, **_) -> Never:
    """
    Qt's 'ManagedObjectList
    QtBluezPeripheralApplication::GetManagedObjects()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.GetManagedObjects' has no cute "
        "function yet. Qt's 'ManagedObjectList "
        "QtBluezPeripheralApplication::GetManagedObjects()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def addService(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralApplication::addService(const
    QLowEnergyServiceData &serviceData,
    QSharedPointer<QLowEnergyServicePrivate> servicePrivate, QLowEnergyHandle
    serviceHandle)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.addService' has no cute function "
        "yet. Qt's 'void QtBluezPeripheralApplication::addService(const "
        "QLowEnergyServiceData &serviceData, "
        "QSharedPointer<QLowEnergyServicePrivate> servicePrivate, "
        "QLowEnergyHandle serviceHandle)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def handleForCharacteristic(*__, **_) -> Never:
    """
    Qt's 'QLowEnergyHandle
    QtBluezPeripheralApplication::handleForCharacteristic(QBluetoothUuid
    uuid, QSharedPointer<QLowEnergyServicePrivate> service)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.handleForCharacteristic' has no cute "
        "function yet. Qt's 'QLowEnergyHandle "
        "QtBluezPeripheralApplication::handleForCharacteristic(QBluetoothUui"
        "d uuid, QSharedPointer<QLowEnergyServicePrivate> service)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def handleForDescriptor(*__, **_) -> Never:
    """
    Qt's 'QLowEnergyHandle
    QtBluezPeripheralApplication::handleForDescriptor(QBluetoothUuid uuid,
    QSharedPointer<QLowEnergyServicePrivate> service, QLowEnergyHandle
    characteristicHandle)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.handleForDescriptor' has no cute "
        "function yet. Qt's 'QLowEnergyHandle "
        "QtBluezPeripheralApplication::handleForDescriptor(QBluetoothUuid "
        "uuid, QSharedPointer<QLowEnergyServicePrivate> service, "
        "QLowEnergyHandle characteristicHandle)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def localCharacteristicWrite(*__, **_) -> Never:
    """
    Qt's 'bool
    QtBluezPeripheralApplication::localCharacteristicWrite(QLowEnergyHandle
    handle, const QByteArray &value)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.localCharacteristicWrite' has no "
        "cute function yet. Qt's 'bool "
        "QtBluezPeripheralApplication::localCharacteristicWrite(QLowEnergyHa"
        "ndle handle, const QByteArray &value)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def localDescriptorWrite(*__, **_) -> Never:
    """
    Qt's 'bool
    QtBluezPeripheralApplication::localDescriptorWrite(QLowEnergyHandle
    handle, const QByteArray &value)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.localDescriptorWrite' has no cute "
        "function yet. Qt's 'bool "
        "QtBluezPeripheralApplication::localDescriptorWrite(QLowEnergyHandle"
        " handle, const QByteArray &value)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def registerApplication(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralApplication::registerApplication()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.registerApplication' has no cute "
        "function yet. Qt's 'void "
        "QtBluezPeripheralApplication::registerApplication()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def registerServices(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralApplication::registerServices()': leans on
    'QtBluezPeripheralGattObject::registerObject()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.registerServices' has no cute "
        "function yet. Qt's 'void "
        "QtBluezPeripheralApplication::registerServices()': leans on "
        "'QtBluezPeripheralGattObject::registerObject()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def reset(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralApplication::reset()': leans on
    'QtBluezPeripheralApplication::unregisterApplication()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.reset' has no cute function yet. "
        "Qt's 'void QtBluezPeripheralApplication::reset()': leans on "
        "'QtBluezPeripheralApplication::unregisterApplication()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def unregisterApplication(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralApplication::unregisterApplication()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.unregisterApplication' has no cute "
        "function yet. Qt's 'void "
        "QtBluezPeripheralApplication::unregisterApplication()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QT_BT_BLUEZ'.")

  @staticmethod
  def unregisterServices(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralApplication::unregisterServices()': leans on
    'QtBluezPeripheralGattObject::unregisterObject()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralApplication.unregisterServices' has no cute "
        "function yet. Qt's 'void "
        "QtBluezPeripheralApplication::unregisterServices()': leans on "
        "'QtBluezPeripheralGattObject::unregisterObject()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
