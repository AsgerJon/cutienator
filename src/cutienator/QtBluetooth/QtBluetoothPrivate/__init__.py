"""
The namespace 'QtBluetoothPrivate' of Qt, a package of 'cutienator.QtBluetooth':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtBluetooth import QtBluetoothPrivate
  QtBluetoothPrivate.OrgBluezAdapter1Interface

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'OrgBluezAdapter1Interface',
    'OrgBluezBattery1Interface',
    'OrgBluezDevice1Interface',
    'OrgBluezGattCharacteristic1Adaptor',
    'OrgBluezGattCharacteristic1Interface',
    'OrgBluezGattDescriptor1Adaptor',
    'OrgBluezGattDescriptor1Interface',
    'OrgBluezGattManager1Interface',
    'OrgBluezGattService1Adaptor',
    'OrgBluezGattService1Interface',
    'OrgBluezLEAdvertisement1Adaptor',
    'OrgBluezLEAdvertisingManager1Interface',
    'OrgBluezProfile1Interface',
    'OrgBluezProfileManager1Interface',
    'OrgFreedesktopDBusObjectManagerAdaptor',
    'OrgFreedesktopDBusObjectManagerInterface',
    'OrgFreedesktopDBusPropertiesAdaptor',
    'OrgFreedesktopDBusPropertiesInterface',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_bluetooth_private__org_bluez_adapter1_interface import OrgBluezAdapter1Interface
  from .._qt_bluetooth_private__org_bluez_battery1_interface import OrgBluezBattery1Interface
  from .._qt_bluetooth_private__org_bluez_device1_interface import OrgBluezDevice1Interface
  from .._qt_bluetooth_private__org_bluez_gatt_characteristic1_adaptor import OrgBluezGattCharacteristic1Adaptor
  from .._qt_bluetooth_private__org_bluez_gatt_characteristic1_interface import OrgBluezGattCharacteristic1Interface
  from .._qt_bluetooth_private__org_bluez_gatt_descriptor1_adaptor import OrgBluezGattDescriptor1Adaptor
  from .._qt_bluetooth_private__org_bluez_gatt_descriptor1_interface import OrgBluezGattDescriptor1Interface
  from .._qt_bluetooth_private__org_bluez_gatt_manager1_interface import OrgBluezGattManager1Interface
  from .._qt_bluetooth_private__org_bluez_gatt_service1_adaptor import OrgBluezGattService1Adaptor
  from .._qt_bluetooth_private__org_bluez_gatt_service1_interface import OrgBluezGattService1Interface
  from .._qt_bluetooth_private__org_bluez_l_e_advertisement1_adaptor import OrgBluezLEAdvertisement1Adaptor
  from .._qt_bluetooth_private__org_bluez_l_e_advertising_manager1_interface import OrgBluezLEAdvertisingManager1Interface
  from .._qt_bluetooth_private__org_bluez_profile1_interface import OrgBluezProfile1Interface
  from .._qt_bluetooth_private__org_bluez_profile_manager1_interface import OrgBluezProfileManager1Interface
  from .._qt_bluetooth_private__org_freedesktop_d_bus_object_manager_adaptor import OrgFreedesktopDBusObjectManagerAdaptor
  from .._qt_bluetooth_private__org_freedesktop_d_bus_object_manager_interface import OrgFreedesktopDBusObjectManagerInterface
  from .._qt_bluetooth_private__org_freedesktop_d_bus_properties_adaptor import OrgFreedesktopDBusPropertiesAdaptor
  from .._qt_bluetooth_private__org_freedesktop_d_bus_properties_interface import OrgFreedesktopDBusPropertiesInterface
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'OrgBluezAdapter1Interface': '_qt_bluetooth_private__org_bluez_adapter1_interface',
      'OrgBluezBattery1Interface': '_qt_bluetooth_private__org_bluez_battery1_interface',
      'OrgBluezDevice1Interface': '_qt_bluetooth_private__org_bluez_device1_interface',
      'OrgBluezGattCharacteristic1Adaptor': '_qt_bluetooth_private__org_bluez_gatt_characteristic1_adaptor',
      'OrgBluezGattCharacteristic1Interface': '_qt_bluetooth_private__org_bluez_gatt_characteristic1_interface',
      'OrgBluezGattDescriptor1Adaptor': '_qt_bluetooth_private__org_bluez_gatt_descriptor1_adaptor',
      'OrgBluezGattDescriptor1Interface': '_qt_bluetooth_private__org_bluez_gatt_descriptor1_interface',
      'OrgBluezGattManager1Interface': '_qt_bluetooth_private__org_bluez_gatt_manager1_interface',
      'OrgBluezGattService1Adaptor': '_qt_bluetooth_private__org_bluez_gatt_service1_adaptor',
      'OrgBluezGattService1Interface': '_qt_bluetooth_private__org_bluez_gatt_service1_interface',
      'OrgBluezLEAdvertisement1Adaptor': '_qt_bluetooth_private__org_bluez_l_e_advertisement1_adaptor',
      'OrgBluezLEAdvertisingManager1Interface': '_qt_bluetooth_private__org_bluez_l_e_advertising_manager1_interface',
      'OrgBluezProfile1Interface': '_qt_bluetooth_private__org_bluez_profile1_interface',
      'OrgBluezProfileManager1Interface': '_qt_bluetooth_private__org_bluez_profile_manager1_interface',
      'OrgFreedesktopDBusObjectManagerAdaptor': '_qt_bluetooth_private__org_freedesktop_d_bus_object_manager_adaptor',
      'OrgFreedesktopDBusObjectManagerInterface': '_qt_bluetooth_private__org_freedesktop_d_bus_object_manager_interface',
      'OrgFreedesktopDBusPropertiesAdaptor': '_qt_bluetooth_private__org_freedesktop_d_bus_properties_adaptor',
      'OrgFreedesktopDBusPropertiesInterface': '_qt_bluetooth_private__org_freedesktop_d_bus_properties_interface',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtBluetoothPrivate.OrgBluezAdapter1Interface'. Python
    calls this for a name the package does not hold yet, and what it gives is
    kept here for the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
