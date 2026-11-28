"""
DarwinBluetooth::LECBManagerNotifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means DarwinBluetooth::LECBManagerNotifier to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QBluetoothDeviceDiscoveryAgent, QLowEnergyController
from . import QLowEnergyService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QBluetoothDeviceInfo, QBluetoothUuid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothDeviceInfo = WAIT['QBluetoothDeviceInfo']
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QByteArray = WAIT['QByteArray']


class LECBManagerNotifier(QObject):
  """
  The cute side of Qt's DarwinBluetooth::LECBManagerNotifier: a plain Python
  object standing in front of one C++ DarwinBluetooth::LECBManagerNotifier.

  It is built on the cute 'QObject', as Qt's
  DarwinBluetooth::LECBManagerNotifier is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's DarwinBluetooth::LECBManagerNotifier that has a
  ritual and that Python can call so far, 17 names in all: 'metaObject',
  'deviceDiscovered', 'discoveryFinished', 'connected', 'disconnected',
  'mtuChanged', 'serviceDiscoveryFinished', 'characteristicRead',
  'characteristicWritten', 'characteristicUpdated', 'descriptorRead',
  'descriptorWritten', 'notificationEnabled', 'servicesWereModified',
  'rssiUpdated', 'LEnotSupported', 'CBManagerError'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DarwinBluetooth::LECBManagerNotifier::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    DarwinBluetooth::LECBManagerNotifier::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::serviceDetailsDiscoveryFinished(
    QSharedPointer<QLowEnergyServicePrivate> service)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 2 not a gap; 1 leans on
  'DarwinBluetooth.

  What to expect
  --------------

  - The C++ DarwinBluetooth::LECBManagerNotifier is created at the first use,
    not by 'DarwinBluetooth::LECBManagerNotifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DarwinBluetooth::LECBManagerNotifier.
  - Qt tells when it has removed the C++
    DarwinBluetooth::LECBManagerNotifier. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's DarwinBluetooth::LECBManagerNotifier that has no cute
    function yet, 'serviceDetailsDiscoveryFinished', holds a function that
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
  __qt_class__ = 'DarwinBluetooth::LECBManagerNotifier'

  #  A C++ DarwinBluetooth::LECBManagerNotifier Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DarwinBluetooth_LECBManagerNotifier'

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
    *DarwinBluetooth::LECBManagerNotifier::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DarwinBluetooth::LECBManagerNotifier::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15DarwinBluetooth19LECBManagerNotifier10metaObjectEv',
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

  @overload(QBluetoothDeviceInfo)
  def deviceDiscovered(self, deviceInfo: QBluetoothDeviceInfo) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::deviceDiscovered(
    QBluetoothDeviceInfo deviceInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    deviceInfo : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::deviceDiscovered(
    #      QBluetoothDeviceInfo deviceInfo)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier16deviceDiscoveredE'
        '20QBluetoothDeviceInfo',
        self._valueOf(deviceInfo),
    )

  def discoveryFinished(self) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::discoveryFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html
    """
    #  void DarwinBluetooth::LECBManagerNotifier::discoveryFinished()
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier17discoveryFinished'
        'Ev',
    )

  def connected(self) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::connected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html#connected
    """
    #  void DarwinBluetooth::LECBManagerNotifier::connected()
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier9connectedEv',
    )

  def disconnected(self) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::disconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html
    """
    #  void DarwinBluetooth::LECBManagerNotifier::disconnected()
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier12disconnectedEv',
    )

  @overload(int)
  def mtuChanged(self, newValue: int) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::mtuChanged(int
    newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    newValue : int
      Passed on as it is.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::mtuChanged(int newValue)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier10mtuChangedEi',
        newValue,
    )

  def serviceDiscoveryFinished(self) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::serviceDiscoveryFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html
    """
    #  void DarwinBluetooth::LECBManagerNotifier::serviceDiscoveryFinished()
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier24serviceDiscoveryF'
        'inishedEv',
    )

  @overload(int, QByteArray)
  def characteristicRead(self, charHandle: int, value: QByteArray) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::characteristicRead(QLowEnergyHandle
    charHandle, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    charHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::characteristicRead(
    #      QLowEnergyHandle charHandle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier18characteristicRea'
        'dEtRK10QByteArray',
        charHandle, self._valueOf(value),
    )

  @overload(int, QByteArray)
  def characteristicWritten(
      self,
      charHandle: int,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::characteristicWritten(
    QLowEnergyHandle charHandle, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    charHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::characteristicWritten(
    #      QLowEnergyHandle charHandle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier21characteristicWri'
        'ttenEtRK10QByteArray',
        charHandle, self._valueOf(value),
    )

  @overload(int, QByteArray)
  def characteristicUpdated(
      self,
      charHandle: int,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::characteristicUpdated(
    QLowEnergyHandle charHandle, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    charHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::characteristicUpdated(
    #      QLowEnergyHandle charHandle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier21characteristicUpd'
        'atedEtRK10QByteArray',
        charHandle, self._valueOf(value),
    )

  @overload(int, QByteArray)
  def descriptorRead(self, descHandle: int, value: QByteArray) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::descriptorRead(QLowEnergyHandle
    descHandle, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    descHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::descriptorRead(
    #      QLowEnergyHandle descHandle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier14descriptorReadEtR'
        'K10QByteArray',
        descHandle, self._valueOf(value),
    )

  @overload(int, QByteArray)
  def descriptorWritten(self, descHandle: int, value: QByteArray) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::descriptorWritten(QLowEnergyHandle
    descHandle, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    descHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::descriptorWritten(
    #      QLowEnergyHandle descHandle, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier17descriptorWritten'
        'EtRK10QByteArray',
        descHandle, self._valueOf(value),
    )

  @overload(int, bool)
  def notificationEnabled(self, charHandle: int, enabled: bool) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::notificationEnabled(
    QLowEnergyHandle charHandle, bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    charHandle : int
      Passed on as it is.

    enabled : bool
      Passed on as it is.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::notificationEnabled(
    #      QLowEnergyHandle charHandle, bool enabled)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier19notificationEnabl'
        'edEtb',
        charHandle, enabled,
    )

  def servicesWereModified(self) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::servicesWereModified()'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html
    """
    #  void DarwinBluetooth::LECBManagerNotifier::servicesWereModified()
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier20servicesWereModif'
        'iedEv',
    )

  @overload(int)
  def rssiUpdated(self, newValue: int) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::rssiUpdated(qint16
    newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    newValue : int
      Passed on as it is.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::rssiUpdated(qint16
    #      newValue)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier11rssiUpdatedEs',
        newValue,
    )

  def LEnotSupported(self) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::LEnotSupported()'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html
    """
    #  void DarwinBluetooth::LECBManagerNotifier::LEnotSupported()
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier14LEnotSupportedEv',
    )

  @overload(QBluetoothDeviceDiscoveryAgent.Error)
  def CBManagerError(
      self,
      error: QBluetoothDeviceDiscoveryAgent.Error,
  ) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::CBManagerError(
    QBluetoothDeviceDiscoveryAgent::Error error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    error : QBluetoothDeviceDiscoveryAgent.Error
      Passed on as its number.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(
    #      QBluetoothDeviceDiscoveryAgent::Error error)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorEN3'
        '0QBluetoothDeviceDiscoveryAgent5ErrorE',
        error.value,
    )

  @overload(QLowEnergyController.Error)
  def CBManagerError(self, error: QLowEnergyController.Error) -> None:
    """
    Calls Qt's 'void DarwinBluetooth::LECBManagerNotifier::CBManagerError(
    QLowEnergyController::Error error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    error : QLowEnergyController.Error
      Passed on as its number.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(
    #      QLowEnergyController::Error error)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorEN2'
        '0QLowEnergyController5ErrorE',
        error.value,
    )

  @overload(QBluetoothUuid, QLowEnergyController.Error)
  def CBManagerError(
      self,
      serviceUuid: QBluetoothUuid,
      error: QLowEnergyController.Error,
  ) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::CBManagerError(const QBluetoothUuid
    &serviceUuid, QLowEnergyController::Error error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    serviceUuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    error : QLowEnergyController.Error
      Passed on as its number.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const
    #      QBluetoothUuid &serviceUuid, QLowEnergyController::Error error)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorERK'
        '14QBluetoothUuidN20QLowEnergyController5ErrorE',
        self._valueOf(serviceUuid), error.value,
    )

  @overload(QBluetoothUuid, QLowEnergyService.ServiceError)
  def CBManagerError(
      self,
      serviceUuid: QBluetoothUuid,
      error: QLowEnergyService.ServiceError,
  ) -> None:
    """
    Calls Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::CBManagerError(const QBluetoothUuid
    &serviceUuid, QLowEnergyService::ServiceError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-lecbmanagernotifier.html

    Parameters
    ----------

    serviceUuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    error : QLowEnergyService.ServiceError
      Passed on as its number.
    """
    #  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const
    #      QBluetoothUuid &serviceUuid, QLowEnergyService::ServiceError
    #      error)
    self.uglySide.call(
        'ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorERK'
        '14QBluetoothUuidN17QLowEnergyService12ServiceErrorE',
        self._valueOf(serviceUuid), error.value,
    )

  @staticmethod
  def serviceDetailsDiscoveryFinished(*__, **_) -> Never:
    """
    Qt's 'void
    DarwinBluetooth::LECBManagerNotifier::serviceDetailsDiscoveryFinished(
    QSharedPointer<QLowEnergyServicePrivate> service)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DarwinBluetooth.LECBManagerNotifier.serviceDetailsDiscoveryFinishe"
        "d' has no cute function yet. Qt's 'void "
        "DarwinBluetooth::LECBManagerNotifier::serviceDetailsDiscoveryFinish"
        "ed(QSharedPointer<QLowEnergyServicePrivate> service)': takes a "
        "type Python has no way to hand over yet.")
