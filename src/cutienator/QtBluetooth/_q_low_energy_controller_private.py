"""
QLowEnergyControllerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontrollerbase_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QLowEnergyControllerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QLowEnergyController, QLowEnergyService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QBluetoothUuid, QLowEnergyAdvertisingData
  from . import QLowEnergyAdvertisingParameters, QLowEnergyCharacteristic
  from . import QLowEnergyConnectionParameters, QLowEnergyDescriptor
  from . import QLowEnergyServiceData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QByteArray = WAIT['QByteArray']
  QLowEnergyAdvertisingData = WAIT['QLowEnergyAdvertisingData']
  QLowEnergyAdvertisingParameters = WAIT['QLowEnergyAdvertisingParameters']
  QLowEnergyConnectionParameters = WAIT['QLowEnergyConnectionParameters']
  QLowEnergyServiceData = WAIT['QLowEnergyServiceData']


class QLowEnergyControllerPrivate(QObject):
  """
  The cute side of Qt's QLowEnergyControllerPrivate: a plain Python object
  standing in front of one C++ QLowEnergyControllerPrivate.

  It is built on the cute 'QObject', as Qt's QLowEnergyControllerPrivate is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLowEnergyControllerPrivate that has a ritual and
  that Python can call so far, 20 names in all: 'metaObject', 'init',
  'connectToDevice', 'disconnectFromDevice', 'discoverServices',
  'discoverServiceDetails', 'startAdvertising', 'stopAdvertising',
  'requestConnectionUpdate', 'addToGenericAttributeList', 'mtu', 'readRssi',
  'addServiceHelper', 'isValidLocalAdapter', 'setError',
  'characteristicForHandle', 'descriptorForHandle',
  'updateValueOfCharacteristic', 'updateValueOfDescriptor', 'q_func'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLowEnergyControllerPrivate::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QLowEnergyControllerPrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QLowEnergyControllerPrivate::~QLowEnergyControllerPrivate()': the
    destructor: Python never removes a C++ QLowEnergyControllerPrivate.
  - Qt's 'void QLowEnergyControllerPrivate::readCharacteristic(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle)': takes a type Python has no way to hand over yet.
  - Qt's 'void QLowEnergyControllerPrivate::readDescriptor(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QLowEnergyHandle descriptorHandle)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QLowEnergyControllerPrivate::writeCharacteristic(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QByteArray &newValue, QLowEnergyService::WriteMode
    writeMode)': takes a type Python has no way to hand over yet.
  - Qt's 'void QLowEnergyControllerPrivate::writeDescriptor(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QLowEnergyHandle descriptorHandle, const QByteArray
    &newValue)': takes a type Python has no way to hand over yet.
  - Qt's 'QSharedPointer<QLowEnergyServicePrivate>
    QLowEnergyControllerPrivate::serviceForHandle(QLowEnergyHandle handle)':
    gives a type Python has no way to take yet.
  - Qt's 'const QLowEnergyController *QLowEnergyControllerPrivate::q_func()
    const': takes in Python what 'QLowEnergyController
    *QLowEnergyControllerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  6 of the 35 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file; 1 leans on
  'QLowEnergyControllerPrivate; 1 leans on 'QLowEnergyServicePrivate.

  What to expect
  --------------

  - The C++ QLowEnergyControllerPrivate is created at the first use, not by
    'QLowEnergyControllerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLowEnergyControllerPrivate.
  - Qt tells when it has removed the C++ QLowEnergyControllerPrivate. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QLowEnergyControllerPrivate that has no cute function
    yet, '__init__', 'invalidateServices', 'readCharacteristic',
    'readDescriptor', 'serviceForHandle', 'setState', 'writeCharacteristic',
    'writeDescriptor', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QLowEnergyControllerPrivate'

  #  A C++ QLowEnergyControllerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLowEnergyControllerPrivate'

  #  The functions Qt calls itself that QLowEnergyControllerPrivate is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'readCharacteristic': (
          'void QLowEnergyControllerPrivate::readCharacteristic(const '
          'QSharedPointer<QLowEnergyServicePrivate>, const '
          'QLowEnergyHandle)',
      ),
      'readDescriptor': (
          'void QLowEnergyControllerPrivate::readDescriptor(const '
          'QSharedPointer<QLowEnergyServicePrivate>, const '
          'QLowEnergyHandle, const QLowEnergyHandle)',
      ),
      'writeCharacteristic': (
          'void QLowEnergyControllerPrivate::writeCharacteristic(const '
          'QSharedPointer<QLowEnergyServicePrivate>, const '
          'QLowEnergyHandle, const QByteArray &, '
          'QLowEnergyService::WriteMode)',
      ),
      'writeDescriptor': (
          'void QLowEnergyControllerPrivate::writeDescriptor(const '
          'QSharedPointer<QLowEnergyServicePrivate>, const '
          'QLowEnergyHandle, const QLowEnergyHandle, const QByteArray &)',
      ),
  }

  #  The functions Qt calls itself that QLowEnergyControllerPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'init': (
          ('_ZN27QLowEnergyControllerPrivate4initEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'connectToDevice': (
          ('_ZN27QLowEnergyControllerPrivate15connectToDeviceEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'disconnectFromDevice': (
          ('_ZN27QLowEnergyControllerPrivate20disconnectFromDeviceEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'discoverServices': (
          ('_ZN27QLowEnergyControllerPrivate16discoverServicesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'discoverServiceDetails': (
          ('_ZN27QLowEnergyControllerPrivate22discoverServiceDetailsERK14QB'
           'luetoothUuidN17QLowEnergyService13DiscoveryModeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtBluetooth:QBluetoothUuid'),
               ('int', 'enum',
                'QtBluetooth:QLowEnergyService.DiscoveryMode'),
           )),
      ),
      'startAdvertising': (
          ('_ZN27QLowEnergyControllerPrivate16startAdvertisingERK31QLowEner'
           'gyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value',
                'QtBluetooth:QLowEnergyAdvertisingParameters'),
               ('address', 'value', 'QtBluetooth:QLowEnergyAdvertisingData'),
               ('address', 'value', 'QtBluetooth:QLowEnergyAdvertisingData'),
           )),
      ),
      'stopAdvertising': (
          ('_ZN27QLowEnergyControllerPrivate15stopAdvertisingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'requestConnectionUpdate': (
          ('_ZN27QLowEnergyControllerPrivate23requestConnectionUpdateERK30Q'
           'LowEnergyConnectionParameters',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value',
                'QtBluetooth:QLowEnergyConnectionParameters'),
           )),
      ),
      'addToGenericAttributeList': (
          ('_ZN27QLowEnergyControllerPrivate25addToGenericAttributeListERK2'
           '1QLowEnergyServiceDatat',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtBluetooth:QLowEnergyServiceData'),
               ('unsigned short', 'number', ''),
           )),
      ),
      'mtu': (
          ('_ZNK27QLowEnergyControllerPrivate3mtuEv',
           ('int', 'number', ''),
           ()),
      ),
      'readRssi': (
          ('_ZN27QLowEnergyControllerPrivate8readRssiEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addServiceHelper': (
          ('_ZN27QLowEnergyControllerPrivate16addServiceHelperERK21QLowEner'
           'gyServiceData',
           ('address', 'address', 'QtBluetooth:QLowEnergyService'),
           (
               ('address', 'value', 'QtBluetooth:QLowEnergyServiceData'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLowEnergyControllerPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLowEnergyControllerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QLowEnergyControllerPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mtu(self) -> int:
    """
    Calls Qt's 'int QLowEnergyControllerPrivate::mtu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#mtu
    """
    #  int QLowEnergyControllerPrivate::mtu() const
    return self.uglySide.call(
        'ritual_ZNK27QLowEnergyControllerPrivate3mtuEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLowEnergyController.Error)
  def setError(self, newError: QLowEnergyController.Error) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivate::setError(QLowEnergyController::Error
    newError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#setError

    Parameters
    ----------

    newError : QLowEnergyController.Error
      Passed on as its number.
    """
    #  void QLowEnergyControllerPrivate::setError(QLowEnergyController::Error
    #      newError)
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate8setErrorEN20QLowEnergyContr'
        'oller5ErrorE',
        newError.value,
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
    Qt's 'QLowEnergyControllerPrivate::QLowEnergyControllerPrivate()': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.__init__' has no cute function yet. "
        "Qt's 'QLowEnergyControllerPrivate::QLowEnergyControllerPrivate()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
    Calls Qt's 'void QLowEnergyControllerPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#init
    """
    #  void QLowEnergyControllerPrivate::init()
    self.uglySide.call('ritual_ZN27QLowEnergyControllerPrivate4initEv')

  def connectToDevice(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivate::connectToDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#connectToDevice
    """
    #  void QLowEnergyControllerPrivate::connectToDevice()
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate15connectToDeviceEv',
    )

  def disconnectFromDevice(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivate::disconnectFromDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html
    """
    #  void QLowEnergyControllerPrivate::disconnectFromDevice()
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate20disconnectFromDeviceEv',
    )

  def discoverServices(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivate::discoverServices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#discoverServices
    """
    #  void QLowEnergyControllerPrivate::discoverServices()
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate16discoverServicesEv',
    )

  @overload(QBluetoothUuid, QLowEnergyService.DiscoveryMode)
  def discoverServiceDetails(
      self,
      service: QBluetoothUuid,
      mode: QLowEnergyService.DiscoveryMode,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivate::discoverServiceDetails(const QBluetoothUuid
    &service, QLowEnergyService::DiscoveryMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html

    Parameters
    ----------

    service : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    mode : QLowEnergyService.DiscoveryMode
      Passed on as its number.
    """
    #  void QLowEnergyControllerPrivate::discoverServiceDetails(const
    #      QBluetoothUuid &service, QLowEnergyService::DiscoveryMode mode)
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate22discoverServiceDetailsERK1'
        '4QBluetoothUuidN17QLowEnergyService13DiscoveryModeE',
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
    Calls Qt's 'void QLowEnergyControllerPrivate::startAdvertising(const
    QLowEnergyAdvertisingParameters &params, const QLowEnergyAdvertisingData
    &advertisingData, const QLowEnergyAdvertisingData &scanResponseData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#startAdvertising

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
    #  void QLowEnergyControllerPrivate::startAdvertising(const
    #      QLowEnergyAdvertisingParameters &params, const
    #      QLowEnergyAdvertisingData &advertisingData, const
    #      QLowEnergyAdvertisingData &scanResponseData)
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate16startAdvertisingERK31QLowE'
        'nergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_',
        self._valueOf(params), self._valueOf(advertisingData),
        self._valueOf(scanResponseData),
    )

  def stopAdvertising(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivate::stopAdvertising()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#stopAdvertising
    """
    #  void QLowEnergyControllerPrivate::stopAdvertising()
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate15stopAdvertisingEv',
    )

  @overload(QLowEnergyConnectionParameters)
  def requestConnectionUpdate(
      self,
      params: QLowEnergyConnectionParameters,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyControllerPrivate::requestConnectionUpdate(const
    QLowEnergyConnectionParameters &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html

    Parameters
    ----------

    params : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  void QLowEnergyControllerPrivate::requestConnectionUpdate(const
    #      QLowEnergyConnectionParameters &params)
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate23requestConnectionUpdateERK'
        '30QLowEnergyConnectionParameters',
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
    QLowEnergyControllerPrivate::addToGenericAttributeList(const
    QLowEnergyServiceData &service, QLowEnergyHandle startHandle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html

    Parameters
    ----------

    service : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.

    startHandle : int
      Passed on as it is.
    """
    #  void QLowEnergyControllerPrivate::addToGenericAttributeList(const
    #      QLowEnergyServiceData &service, QLowEnergyHandle startHandle)
    self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate25addToGenericAttributeListE'
        'RK21QLowEnergyServiceDatat',
        self._valueOf(service), startHandle,
    )

  def readRssi(self) -> None:
    """
    Calls Qt's 'void QLowEnergyControllerPrivate::readRssi()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#readRssi
    """
    #  void QLowEnergyControllerPrivate::readRssi()
    self.uglySide.call('ritual_ZN27QLowEnergyControllerPrivate8readRssiEv')

  @overload(QLowEnergyServiceData)
  def addServiceHelper(
      self,
      service: QLowEnergyServiceData,
  ) -> Optional[QLowEnergyService]:
    """
    Calls Qt's 'QLowEnergyService
    *QLowEnergyControllerPrivate::addServiceHelper(const
    QLowEnergyServiceData &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#addServiceHelper

    Parameters
    ----------

    service : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.

    Returns
    -------

    Optional[QLowEnergyService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyService *QLowEnergyControllerPrivate::addServiceHelper(const
    #      QLowEnergyServiceData &service)
    address = self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate16addServiceHelperERK21QLowE'
        'nergyServiceData',
        self._valueOf(service),
    )
    return QLowEnergyService._cuteAt(address)

  def isValidLocalAdapter(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyControllerPrivate::isValidLocalAdapter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html
    """
    #  bool QLowEnergyControllerPrivate::isValidLocalAdapter()
    return self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate19isValidLocalAdapterEv',
    )

  @overload(int)
  def characteristicForHandle(self, handle: int) -> QLowEnergyCharacteristic:
    """
    Calls Qt's 'QLowEnergyCharacteristic
    QLowEnergyControllerPrivate::characteristicForHandle(QLowEnergyHandle
    handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    Returns
    -------

    QLowEnergyCharacteristic
      A new cute QLowEnergyCharacteristic around the copy Qt gave back.
      Python owns it.
    """
    #  QLowEnergyCharacteristic
    #      QLowEnergyControllerPrivate::characteristicForHandle(
    #      QLowEnergyHandle handle)
    address = self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate23characteristicForHandleEt',
        handle,
    )
    from . import QLowEnergyCharacteristic
    return QLowEnergyCharacteristic._cuteOwning(address)

  @overload(int)
  def descriptorForHandle(self, handle: int) -> QLowEnergyDescriptor:
    """
    Calls Qt's 'QLowEnergyDescriptor
    QLowEnergyControllerPrivate::descriptorForHandle(QLowEnergyHandle
    handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    Returns
    -------

    QLowEnergyDescriptor
      A new cute QLowEnergyDescriptor around the copy Qt gave back. Python
      owns it.
    """
    #  QLowEnergyDescriptor
    #      QLowEnergyControllerPrivate::descriptorForHandle(QLowEnergyHandle
    #      handle)
    address = self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate19descriptorForHandleEt',
        handle,
    )
    from . import QLowEnergyDescriptor
    return QLowEnergyDescriptor._cuteOwning(address)

  @overload(int, QByteArray, bool)
  def updateValueOfCharacteristic(
      self,
      charHandle: int,
      value: QByteArray,
      appendValue: bool,
  ) -> int:
    """
    Calls Qt's 'quint16
    QLowEnergyControllerPrivate::updateValueOfCharacteristic(QLowEnergyHandle
    charHandle, const QByteArray &value, bool appendValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html

    Parameters
    ----------

    charHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    appendValue : bool
      Passed on as it is.
    """
    #  quint16 QLowEnergyControllerPrivate::updateValueOfCharacteristic(
    #      QLowEnergyHandle charHandle, const QByteArray &value, bool
    #      appendValue)
    return self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate27updateValueOfCharacteristi'
        'cEtRK10QByteArrayb',
        charHandle, self._valueOf(value), appendValue,
    )

  @overload(int, int, QByteArray, bool)
  def updateValueOfDescriptor(
      self,
      charHandle: int,
      descriptorHandle: int,
      value: QByteArray,
      appendValue: bool,
  ) -> int:
    """
    Calls Qt's 'quint16
    QLowEnergyControllerPrivate::updateValueOfDescriptor(QLowEnergyHandle
    charHandle, QLowEnergyHandle descriptorHandle, const QByteArray &value,
    bool appendValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html

    Parameters
    ----------

    charHandle : int
      Passed on as it is.

    descriptorHandle : int
      Passed on as it is.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    appendValue : bool
      Passed on as it is.
    """
    #  quint16 QLowEnergyControllerPrivate::updateValueOfDescriptor(
    #      QLowEnergyHandle charHandle, QLowEnergyHandle descriptorHandle,
    #      const QByteArray &value, bool appendValue)
    return self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate23updateValueOfDescriptorEtt'
        'RK10QByteArrayb',
        charHandle, descriptorHandle, self._valueOf(value), appendValue,
    )

  def q_func(self) -> Optional[QLowEnergyController]:
    """
    Calls Qt's 'QLowEnergyController *QLowEnergyControllerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontrollerprivate.html#q_func

    Returns
    -------

    Optional[QLowEnergyController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyController *QLowEnergyControllerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QLowEnergyControllerPrivate6q_funcEv',
    )
    return QLowEnergyController._cuteAt(address)

  @staticmethod
  def invalidateServices(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivate::invalidateServices()': leans on
    'QLowEnergyServicePrivate::stateChanged(QLowEnergyService::
    ServiceState)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.invalidateServices' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyControllerPrivate::invalidateServices()': leans on "
        "'QLowEnergyServicePrivate::stateChanged(QLowEnergyService::ServiceS"
        "tate)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def readCharacteristic(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivate::readCharacteristic(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.readCharacteristic' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyControllerPrivate::readCharacteristic(const "
        "QSharedPointer<QLowEnergyServicePrivate> service, const "
        "QLowEnergyHandle charHandle)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def readDescriptor(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivate::readDescriptor(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QLowEnergyHandle descriptorHandle)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.readDescriptor' has no cute function "
        "yet. Qt's 'void QLowEnergyControllerPrivate::readDescriptor(const "
        "QSharedPointer<QLowEnergyServicePrivate> service, const "
        "QLowEnergyHandle charHandle, const QLowEnergyHandle "
        "descriptorHandle)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def serviceForHandle(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QLowEnergyServicePrivate>
    QLowEnergyControllerPrivate::serviceForHandle(QLowEnergyHandle handle)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.serviceForHandle' has no cute "
        "function yet. Qt's 'QSharedPointer<QLowEnergyServicePrivate> "
        "QLowEnergyControllerPrivate::serviceForHandle(QLowEnergyHandle "
        "handle)': gives a type Python has no way to take yet.")

  @staticmethod
  def setState(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivate::setState(QLowEnergyController::
    ControllerState newState)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'QT_BT'.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.setState' has no cute function yet. "
        "Qt's 'void "
        "QLowEnergyControllerPrivate::setState(QLowEnergyController::Control"
        "lerState newState)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QT_BT'.")

  @staticmethod
  def writeCharacteristic(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivate::writeCharacteristic(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QByteArray &newValue, QLowEnergyService::WriteMode
    writeMode)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.writeCharacteristic' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyControllerPrivate::writeCharacteristic(const "
        "QSharedPointer<QLowEnergyServicePrivate> service, const "
        "QLowEnergyHandle charHandle, const QByteArray &newValue, "
        "QLowEnergyService::WriteMode writeMode)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def writeDescriptor(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyControllerPrivate::writeDescriptor(const
    QSharedPointer<QLowEnergyServicePrivate> service, const QLowEnergyHandle
    charHandle, const QLowEnergyHandle descriptorHandle, const QByteArray
    &newValue)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyControllerPrivate.writeDescriptor' has no cute function "
        "yet. Qt's 'void QLowEnergyControllerPrivate::writeDescriptor(const "
        "QSharedPointer<QLowEnergyServicePrivate> service, const "
        "QLowEnergyHandle charHandle, const QLowEnergyHandle "
        "descriptorHandle, const QByteArray &newValue)': takes a type "
        "Python has no way to hand over yet.")
