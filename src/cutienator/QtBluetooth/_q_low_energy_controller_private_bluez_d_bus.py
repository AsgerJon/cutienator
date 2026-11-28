"""
QLowEnergyControllerPrivateBluezDBus binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_bluezdbus_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QLowEnergyControllerPrivateBluezDBus to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QLowEnergyControllerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QBluetoothAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']


class QLowEnergyControllerPrivateBluezDBus(QLowEnergyControllerPrivate):
  """
  The cute side of Qt's QLowEnergyControllerPrivateBluezDBus: a plain Python
  object standing in front of one C++ QLowEnergyControllerPrivateBluezDBus.

  It is built on the cute 'QLowEnergyControllerPrivate', as Qt's
  QLowEnergyControllerPrivateBluezDBus is built on Qt's
  QLowEnergyControllerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLowEnergyControllerPrivateBluezDBus that has a
  ritual and that Python can call so far, 2 names in all: 'mtu',
  'handlePeripheralRemoteDeviceChanged'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  40 of the 42 functions Qt declares: 22 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 12 leans on
  'QLowEnergyControllerPrivateBluezDBus; 2 not a gap; 1 leans on 'vtable for
  QLowEnergyControllerPrivateBluezDBus', which Qt's source does not mark for
  use from outside Qt and has no code for that could be taken; 1 leans on
  'QLowEnergyServicePrivate; 1 leans on 'QLeDBusAdvertiser; 1 leans on
  'QLowEnergyControllerPrivate.

  What to expect
  --------------

  - The C++ QLowEnergyControllerPrivateBluezDBus is created at the first use,
    not by 'QLowEnergyControllerPrivateBluezDBus(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLowEnergyControllerPrivateBluezDBus.
  - Qt tells when it has removed the C++
    QLowEnergyControllerPrivateBluezDBus. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's QLowEnergyControllerPrivateBluezDBus that has no cute
    function yet, '__init__', 'characteristicPropertiesChanged',
    'connectToDeviceHelper', 'devicePropertiesChanged',
    'discoverBatteryServiceDetails', 'executeClose',
    'handleAdvertisingError', 'handlePeripheralApplicationError',
    'handlePeripheralApplicationRegistered',
    'handlePeripheralCharacteristicValueUpdate',
    'handlePeripheralConnectivityChanged',
    'handlePeripheralDescriptorValueUpdate', 'interfacesRemoved',
    'onCharReadFinished', 'onCharWriteFinished', 'onDescReadFinished',
    'onDescWriteFinished', 'prepareNextJob', 'resetController',
    'scheduleNextJob', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyControllerPrivateBluezDBus'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mtu(self) -> int:
    """
    Calls Qt's 'int QLowEnergyControllerPrivateBluezDBus::mtu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatebluezdbus.html#mtu
    """
    #  int QLowEnergyControllerPrivateBluezDBus::mtu() const
    return self.uglySide.call(
        'ritual_ZNK36QLowEnergyControllerPrivateBluezDBus3mtuEv',
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
    Qt's 'QLowEnergyControllerPrivateBluezDBus::
    QLowEnergyControllerPrivateBluezDBus(const QString
    &adapterPathWithPeripheralSupport)': leans on 'vtable for
    QLowEnergyControllerPrivateBluezDBus', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.__init__' has no cute "
        "function yet. Qt's "
        "'QLowEnergyControllerPrivateBluezDBus::QLowEnergyControllerPrivateB"
        "luezDBus(const QString &adapterPathWithPeripheralSupport)': leans "
        "on 'vtable for QLowEnergyControllerPrivateBluezDBus', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QBluetoothAddress, str, int)
  def handlePeripheralRemoteDeviceChanged(
      self,
      address: QBluetoothAddress,
      name: str,
      mtu: int,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivateBluezDBus::
    handlePeripheralRemoteDeviceChanged(const QBluetoothAddress &address,
    const QString &name, quint16 mtu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatebluezdbus.html

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    mtu : int
      Passed on as it is.
    """
    #  void QLowEnergyControllerPrivateBluezDBus::
    #      handlePeripheralRemoteDeviceChanged(const QBluetoothAddress
    #      &address, const QString &name, quint16 mtu)
    self.uglySide.call(
        'ritual_ZN36QLowEnergyControllerPrivateBluezDBus35handlePeripheralR'
        'emoteDeviceChangedERK17QBluetoothAddressRK7QStringt',
        self._valueOf(address), name, mtu,
    )

  @staticmethod
  def characteristicPropertiesChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyControllerPrivateBluezDBus::characteristicPropertiesChanged(
    QLowEnergyHandle charHandle, const QString &interface, const QVariantMap
    &changedProperties, const QStringList &invalidatedProperties)': leans on
    'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.characteristicPropertiesChang"
        "ed' has no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::characteristicPropertiesChang"
        "ed(QLowEnergyHandle charHandle, const QString &interface, const "
        "QVariantMap &changedProperties, const QStringList "
        "&invalidatedProperties)': leans on "
        "'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def connectToDeviceHelper(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyControllerPrivateBluezDBus::connectToDeviceHelper()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'findAdapterForAddress'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.connectToDeviceHelper' has "
        "no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::connectToDeviceHelper()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'findAdapterForAddress'.")

  @staticmethod
  def devicePropertiesChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyControllerPrivateBluezDBus::devicePropertiesChanged(const
    QString &interface, const QVariantMap &changedProperties, const
    QStringList &invalidatedProperties)': leans on
    'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.devicePropertiesChanged' has "
        "no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::devicePropertiesChanged(const"
        " QString &interface, const QVariantMap &changedProperties, const "
        "QStringList &invalidatedProperties)': leans on "
        "'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def discoverBatteryServiceDetails(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyControllerPrivateBluezDBus::discoverBatteryServiceDetails(
    GattService &dbusData, QSharedPointer<QLowEnergyServicePrivate>
    serviceData)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'OrgBluezBattery1Interface'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.discoverBatteryServiceDetails"
        "' has no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::discoverBatteryServiceDetails"
        "(GattService &dbusData, QSharedPointer<QLowEnergyServicePrivate> "
        "serviceData)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'OrgBluezBattery1Interface'.")

  @staticmethod
  def executeClose(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::executeClose(
    QLowEnergyController::Error newError)': leans on
    'QLowEnergyControllerPrivate::setState(QLowEnergyController::
    ControllerState)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.executeClose' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::executeClose(QLowEnergyContro"
        "ller::Error newError)': leans on "
        "'QLowEnergyControllerPrivate::setState(QLowEnergyController::Contro"
        "llerState)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def handleAdvertisingError(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyControllerPrivateBluezDBus::handleAdvertisingError()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.handleAdvertisingError' has "
        "no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::handleAdvertisingError()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QT_BT_BLUEZ'.")

  @staticmethod
  def handlePeripheralApplicationError(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyControllerPrivateBluezDBus::handlePeripheralApplicationError(
    )': Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.handlePeripheralApplicationEr"
        "ror' has no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::handlePeripheralApplicationEr"
        "ror()': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def handlePeripheralApplicationRegistered(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::
    handlePeripheralApplicationRegistered()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QtBluezPeripheralApplication'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.handlePeripheralApplicationRe"
        "gistered' has no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::handlePeripheralApplicationRe"
        "gistered()': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QtBluezPeripheralApplication'.")

  @staticmethod
  def handlePeripheralCharacteristicValueUpdate(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::
    handlePeripheralCharacteristicValueUpdate(QLowEnergyHandle handle, const
    QByteArray &value)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.handlePeripheralCharacteristi"
        "cValueUpdate' has no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::handlePeripheralCharacteristi"
        "cValueUpdate(QLowEnergyHandle handle, const QByteArray &value)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QT_BT_BLUEZ'.")

  @staticmethod
  def handlePeripheralConnectivityChanged(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::
    handlePeripheralConnectivityChanged(bool connected)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.handlePeripheralConnectivityC"
        "hanged' has no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::handlePeripheralConnectivityC"
        "hanged(bool connected)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def handlePeripheralDescriptorValueUpdate(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::
    handlePeripheralDescriptorValueUpdate(QLowEnergyHandle
    characteristicHandle, QLowEnergyHandle descriptorHandle, const QByteArray
    &value)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.handlePeripheralDescriptorVal"
        "ueUpdate' has no cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::handlePeripheralDescriptorVal"
        "ueUpdate(QLowEnergyHandle characteristicHandle, QLowEnergyHandle "
        "descriptorHandle, const QByteArray &value)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def interfacesRemoved(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::interfacesRemoved(const
    QDBusObjectPath &objectPath, const QStringList &interfaces)': leans on
    'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.interfacesRemoved' has no "
        "cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::interfacesRemoved(const "
        "QDBusObjectPath &objectPath, const QStringList &interfaces)': "
        "leans on "
        "'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def onCharReadFinished(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::onCharReadFinished(
    QDBusPendingCallWatcher *call)': leans on
    'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.onCharReadFinished' has no "
        "cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::onCharReadFinished(QDBusPendi"
        "ngCallWatcher *call)': leans on "
        "'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def onCharWriteFinished(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::onCharWriteFinished(
    QDBusPendingCallWatcher *call)': leans on
    'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.onCharWriteFinished' has no "
        "cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::onCharWriteFinished(QDBusPend"
        "ingCallWatcher *call)': leans on "
        "'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def onDescReadFinished(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::onDescReadFinished(
    QDBusPendingCallWatcher *call)': leans on
    'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.onDescReadFinished' has no "
        "cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::onDescReadFinished(QDBusPendi"
        "ngCallWatcher *call)': leans on "
        "'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def onDescWriteFinished(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::onDescWriteFinished(
    QDBusPendingCallWatcher *call)': leans on
    'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.onDescWriteFinished' has no "
        "cute function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::onDescWriteFinished(QDBusPend"
        "ingCallWatcher *call)': leans on "
        "'QLowEnergyControllerPrivateBluezDBus::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def prepareNextJob(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::prepareNextJob()': leans
    on 'QLowEnergyControllerPrivateBluezDBus::scheduleNextJob()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.prepareNextJob' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::prepareNextJob()': leans on "
        "'QLowEnergyControllerPrivateBluezDBus::scheduleNextJob()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def resetController(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::resetController()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QtBluezPeripheralApplication'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.resetController' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::resetController()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QtBluezPeripheralApplication'.")

  @staticmethod
  def scheduleNextJob(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivateBluezDBus::scheduleNextJob()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateBluezDBus.scheduleNextJob' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyControllerPrivateBluezDBus::scheduleNextJob()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QT_BT_BLUEZ'.")
