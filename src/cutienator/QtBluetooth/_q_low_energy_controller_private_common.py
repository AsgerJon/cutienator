"""
QLowEnergyControllerPrivateCommon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_dummy_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QLowEnergyControllerPrivateCommon to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QLowEnergyControllerPrivate, QLowEnergyService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QBluetoothUuid, QLowEnergyAdvertisingData
  from . import QLowEnergyAdvertisingParameters
  from . import QLowEnergyConnectionParameters, QLowEnergyServiceData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QLowEnergyAdvertisingData = WAIT['QLowEnergyAdvertisingData']
  QLowEnergyAdvertisingParameters = WAIT['QLowEnergyAdvertisingParameters']
  QLowEnergyConnectionParameters = WAIT['QLowEnergyConnectionParameters']
  QLowEnergyServiceData = WAIT['QLowEnergyServiceData']


class QLowEnergyControllerPrivateCommon(QLowEnergyControllerPrivate):
  """
  The cute side of Qt's QLowEnergyControllerPrivateCommon: a plain Python
  object standing in front of one C++ QLowEnergyControllerPrivateCommon.

  It is built on the cute 'QLowEnergyControllerPrivate', as Qt's
  QLowEnergyControllerPrivateCommon is built on Qt's
  QLowEnergyControllerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLowEnergyControllerPrivateCommon that has a ritual
  and that Python can call so far, 10 names in all: 'init',
  'connectToDevice', 'disconnectFromDevice', 'discoverServices',
  'discoverServiceDetails', 'startAdvertising', 'stopAdvertising',
  'requestConnectionUpdate', 'addToGenericAttributeList', 'mtu'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLowEnergyControllerPrivateCommon::readCharacteristic(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle)': takes a type Python has no way to hand over yet.
  - Qt's 'void QLowEnergyControllerPrivateCommon::readDescriptor(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QLowEnergyHandle descriptorHandle)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QLowEnergyControllerPrivateCommon::writeCharacteristic(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QByteArray &newValue, QLowEnergyService::WriteMode
    mode)': takes a type Python has no way to hand over yet.
  - Qt's 'void QLowEnergyControllerPrivateCommon::writeDescriptor(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QLowEnergyHandle descriptorHandle, const QByteArray
    &newValue)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 22 functions Qt declares: 4 leans on
  'QLowEnergyControllerPrivateCommon; 2 not a gap; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'vtable for QLowEnergyControllerPrivate', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QLowEnergyControllerPrivateCommon is created at the first use,
    not by 'QLowEnergyControllerPrivateCommon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLowEnergyControllerPrivateCommon.
  - Qt tells when it has removed the C++ QLowEnergyControllerPrivateCommon.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QLowEnergyControllerPrivateCommon that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QLowEnergyControllerPrivateCommon'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mtu(self) -> int:
    """
    Calls Qt's 'int QLowEnergyControllerPrivateCommon::mtu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html#mtu
    """
    #  int QLowEnergyControllerPrivateCommon::mtu() const
    return self.uglySide.call(
        'ritual_ZNK33QLowEnergyControllerPrivateCommon3mtuEv',
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
    Qt's
    'QLowEnergyControllerPrivateCommon::QLowEnergyControllerPrivateCommon()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'printDummyWarning'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivateCommon.__init__' has no cute function "
        "yet. Qt's "
        "'QLowEnergyControllerPrivateCommon::QLowEnergyControllerPrivateComm"
        "on()': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'printDummyWarning'.")

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

  def init(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivateCommon::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html#init
    """
    #  void QLowEnergyControllerPrivateCommon::init()
    self.uglySide.call('ritual_ZN33QLowEnergyControllerPrivateCommon4initEv')

  def connectToDevice(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivateCommon::connectToDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html
    """
    #  void QLowEnergyControllerPrivateCommon::connectToDevice()
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon15connectToDeviceEv',
    )

  def disconnectFromDevice(self) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivateCommon::disconnectFromDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html
    """
    #  void QLowEnergyControllerPrivateCommon::disconnectFromDevice()
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon20disconnectFromDevice'
        'Ev',
    )

  def discoverServices(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivateCommon::discoverServices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html
    """
    #  void QLowEnergyControllerPrivateCommon::discoverServices()
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon16discoverServicesEv',
    )

  @overload(QBluetoothUuid, QLowEnergyService.DiscoveryMode)
  def discoverServiceDetails(
      self,
      service: QBluetoothUuid,
      mode: QLowEnergyService.DiscoveryMode,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivateCommon::discoverServiceDetails(const
    QBluetoothUuid &service, QLowEnergyService::DiscoveryMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html

    Parameters
    ----------

    service : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    mode : QLowEnergyService.DiscoveryMode
      Passed on as its number.
    """
    #  void QLowEnergyControllerPrivateCommon::discoverServiceDetails(const
    #      QBluetoothUuid &service, QLowEnergyService::DiscoveryMode mode)
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon22discoverServiceDetai'
        'lsERK14QBluetoothUuidN17QLowEnergyService13DiscoveryModeE',
        self._valueOf(service), mode.value,
    )

  @overload(
      QLowEnergyAdvertisingParameters, QLowEnergyAdvertisingData,
      QLowEnergyAdvertisingData,
  )
  def startAdvertising(
      self,
      params: QLowEnergyAdvertisingParameters,
      advertisingData: QLowEnergyAdvertisingData,
      scanResponseData: QLowEnergyAdvertisingData,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivateCommon::startAdvertising(const
    QLowEnergyAdvertisingParameters &params, const QLowEnergyAdvertisingData
    &advertisingData, const QLowEnergyAdvertisingData &scanResponseData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html

    Parameters
    ----------

    params : QLowEnergyAdvertisingParameters
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingParameters,
      which stays Python's own.

    advertisingData : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.

    scanResponseData : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.
    """
    #  void QLowEnergyControllerPrivateCommon::startAdvertising(const
    #      QLowEnergyAdvertisingParameters &params, const
    #      QLowEnergyAdvertisingData &advertisingData, const
    #      QLowEnergyAdvertisingData &scanResponseData)
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon16startAdvertisingERK3'
        '1QLowEnergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_',
        self._valueOf(params), self._valueOf(advertisingData),
        self._valueOf(scanResponseData),
    )

  def stopAdvertising(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivateCommon::stopAdvertising()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html
    """
    #  void QLowEnergyControllerPrivateCommon::stopAdvertising()
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon15stopAdvertisingEv',
    )

  @overload(QLowEnergyConnectionParameters)
  def requestConnectionUpdate(
      self,
      params: QLowEnergyConnectionParameters,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivateCommon::requestConnectionUpdate(const
    QLowEnergyConnectionParameters &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html

    Parameters
    ----------

    params : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  void QLowEnergyControllerPrivateCommon::requestConnectionUpdate(const
    #      QLowEnergyConnectionParameters &params)
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon23requestConnectionUpd'
        'ateERK30QLowEnergyConnectionParameters',
        self._valueOf(params),
    )

  @overload(QLowEnergyServiceData, int)
  def addToGenericAttributeList(
      self,
      service: QLowEnergyServiceData,
      startHandle: int,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivateCommon::addToGenericAttributeList(const
    QLowEnergyServiceData &service, QLowEnergyHandle startHandle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivatecommon.html

    Parameters
    ----------

    service : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.

    startHandle : int
      Passed on as it is.
    """
    #  void
    #      QLowEnergyControllerPrivateCommon::addToGenericAttributeList(const
    #      QLowEnergyServiceData &service, QLowEnergyHandle startHandle)
    self.uglySide.call(
        'ritual_ZN33QLowEnergyControllerPrivateCommon25addToGenericAttribut'
        'eListERK21QLowEnergyServiceDatat',
        self._valueOf(service), startHandle,
    )
