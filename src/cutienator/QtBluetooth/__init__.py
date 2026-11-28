"""
The 'cutienator.QtBluetooth' package provides the cute classes of the
part of Qt named QtBluetooth, under the name PySide6 has for it.

  from cutienator.QtBluetooth import AclData, L2CapHeader

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'AclData',
    'L2CapHeader',
    'QBluetoothDeviceInfoPrivate',
    'QBluetoothHostInfoPrivate',
    'QLowEnergyAdvertisingParameters',
    'QLowEnergyConnectionParameters',
    'QPrivateLinearBuffer',
    'bt_security',
    'evt_cmd_complete',
    'hci_command_hdr',
    'hci_conn_info',
    'hci_conn_list_req',
    'hci_dev_info',
    'hci_dev_list_req',
    'hci_dev_req',
    'hci_dev_stats',
    'hci_filter',
    'quint128',
    'sockaddr_hci',
    'sockaddr_l2',
    'sockaddr_rc',
    'LeCmacCalculator',
    'QBluetoothUuid',
    'QBluetoothAddress',
    'QLowEnergyAdvertisingData',
    'QLowEnergyDescriptorData',
    'QtBluezPeripheralGattObject',
    'QBluetoothDeviceInfo',
    'QBluetoothHostInfo',
    'QBluetoothLocalDevice',
    'QBluetoothServiceInfoPrivate',
    'QLeDBusAdvertiser',
    'QtBluezDiscoveryManager',
    'QtBluezPeripheralConnectionManager',
    'QtBluezPeripheralDescriptor',
    'RemoteDeviceManager',
    'OrgBluezProfile1ContextInterface',
    'QBluetoothDeviceDiscoveryAgent',
    'QBluetoothServiceInfo',
    'QLowEnergyCharacteristic',
    'QLowEnergyCharacteristicData',
    'QLowEnergyDescriptor',
    'QLowEnergyService',
    'QLowEnergyServiceData',
    'QLowEnergyController',
    'QLowEnergyControllerPrivate',
    'QLowEnergyServicePrivate',
    'QBluetoothServer',
    'QBluetoothServiceDiscoveryAgent',
    'QBluetoothSocket',
    'QBluetoothSocketBasePrivate',
    'QLowEnergyControllerPrivateBluezDBus',
    'QLowEnergyControllerPrivateCommon',
    'QtBluezPeripheralApplication',
    'QtBluezPeripheralCharacteristic',
    'QtBluezPeripheralService',
    'QBluetoothServerPrivate',
    'QBluetoothServiceDiscoveryAgentPrivate',
    'QBluetoothSocketPrivateBluez',
    'QBluetoothSocketPrivateBluezDBus',
    'QBluetoothSocketPrivateDummy',
    'DarwinBluetooth',
    'QBluetooth',
    'QBluezConst',
    'QtBluetoothPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._acl_data import AclData
  from ._l2_cap_header import L2CapHeader
  from ._q_bluetooth_device_info_private import QBluetoothDeviceInfoPrivate
  from ._q_bluetooth_host_info_private import QBluetoothHostInfoPrivate
  from ._q_low_energy_advertising_parameters import QLowEnergyAdvertisingParameters
  from ._q_low_energy_connection_parameters import QLowEnergyConnectionParameters
  from ._q_private_linear_buffer import QPrivateLinearBuffer
  from ._bt_security import bt_security
  from ._evt_cmd_complete import evt_cmd_complete
  from ._hci_command_hdr import hci_command_hdr
  from ._hci_conn_info import hci_conn_info
  from ._hci_conn_list_req import hci_conn_list_req
  from ._hci_dev_info import hci_dev_info
  from ._hci_dev_list_req import hci_dev_list_req
  from ._hci_dev_req import hci_dev_req
  from ._hci_dev_stats import hci_dev_stats
  from ._hci_filter import hci_filter
  from ._quint128 import quint128
  from ._sockaddr_hci import sockaddr_hci
  from ._sockaddr_l2 import sockaddr_l2
  from ._sockaddr_rc import sockaddr_rc
  from ._le_cmac_calculator import LeCmacCalculator
  from ._q_bluetooth_uuid import QBluetoothUuid
  from ._q_bluetooth_address import QBluetoothAddress
  from ._q_low_energy_advertising_data import QLowEnergyAdvertisingData
  from ._q_low_energy_descriptor_data import QLowEnergyDescriptorData
  from ._qt_bluez_peripheral_gatt_object import QtBluezPeripheralGattObject
  from ._q_bluetooth_device_info import QBluetoothDeviceInfo
  from ._q_bluetooth_host_info import QBluetoothHostInfo
  from ._q_bluetooth_local_device import QBluetoothLocalDevice
  from ._q_bluetooth_service_info_private import QBluetoothServiceInfoPrivate
  from ._q_le_d_bus_advertiser import QLeDBusAdvertiser
  from ._qt_bluez_discovery_manager import QtBluezDiscoveryManager
  from ._qt_bluez_peripheral_connection_manager import QtBluezPeripheralConnectionManager
  from ._qt_bluez_peripheral_descriptor import QtBluezPeripheralDescriptor
  from ._remote_device_manager import RemoteDeviceManager
  from ._org_bluez_profile1_context_interface import OrgBluezProfile1ContextInterface
  from ._q_bluetooth_device_discovery_agent import QBluetoothDeviceDiscoveryAgent
  from ._q_bluetooth_service_info import QBluetoothServiceInfo
  from ._q_low_energy_characteristic import QLowEnergyCharacteristic
  from ._q_low_energy_characteristic_data import QLowEnergyCharacteristicData
  from ._q_low_energy_descriptor import QLowEnergyDescriptor
  from ._q_low_energy_service import QLowEnergyService
  from ._q_low_energy_service_data import QLowEnergyServiceData
  from ._q_low_energy_controller import QLowEnergyController
  from ._q_low_energy_controller_private import QLowEnergyControllerPrivate
  from ._q_low_energy_service_private import QLowEnergyServicePrivate
  from ._q_bluetooth_server import QBluetoothServer
  from ._q_bluetooth_service_discovery_agent import QBluetoothServiceDiscoveryAgent
  from ._q_bluetooth_socket import QBluetoothSocket
  from ._q_bluetooth_socket_base_private import QBluetoothSocketBasePrivate
  from ._q_low_energy_controller_private_bluez_d_bus import QLowEnergyControllerPrivateBluezDBus
  from ._q_low_energy_controller_private_common import QLowEnergyControllerPrivateCommon
  from ._qt_bluez_peripheral_application import QtBluezPeripheralApplication
  from ._qt_bluez_peripheral_characteristic import QtBluezPeripheralCharacteristic
  from ._qt_bluez_peripheral_service import QtBluezPeripheralService
  from ._q_bluetooth_server_private import QBluetoothServerPrivate
  from ._q_bluetooth_service_discovery_agent_private import QBluetoothServiceDiscoveryAgentPrivate
  from ._q_bluetooth_socket_private_bluez import QBluetoothSocketPrivateBluez
  from ._q_bluetooth_socket_private_bluez_d_bus import QBluetoothSocketPrivateBluezDBus
  from ._q_bluetooth_socket_private_dummy import QBluetoothSocketPrivateDummy
  from . import DarwinBluetooth
  from . import QBluetooth
  from . import QBluezConst
  from . import QtBluetoothPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'AclData': '_acl_data',
      'L2CapHeader': '_l2_cap_header',
      'QBluetoothDeviceInfoPrivate': '_q_bluetooth_device_info_private',
      'QBluetoothHostInfoPrivate': '_q_bluetooth_host_info_private',
      'QLowEnergyAdvertisingParameters': '_q_low_energy_advertising_parameters',
      'QLowEnergyConnectionParameters': '_q_low_energy_connection_parameters',
      'QPrivateLinearBuffer': '_q_private_linear_buffer',
      'bt_security': '_bt_security',
      'evt_cmd_complete': '_evt_cmd_complete',
      'hci_command_hdr': '_hci_command_hdr',
      'hci_conn_info': '_hci_conn_info',
      'hci_conn_list_req': '_hci_conn_list_req',
      'hci_dev_info': '_hci_dev_info',
      'hci_dev_list_req': '_hci_dev_list_req',
      'hci_dev_req': '_hci_dev_req',
      'hci_dev_stats': '_hci_dev_stats',
      'hci_filter': '_hci_filter',
      'quint128': '_quint128',
      'sockaddr_hci': '_sockaddr_hci',
      'sockaddr_l2': '_sockaddr_l2',
      'sockaddr_rc': '_sockaddr_rc',
      'LeCmacCalculator': '_le_cmac_calculator',
      'QBluetoothUuid': '_q_bluetooth_uuid',
      'QBluetoothAddress': '_q_bluetooth_address',
      'QLowEnergyAdvertisingData': '_q_low_energy_advertising_data',
      'QLowEnergyDescriptorData': '_q_low_energy_descriptor_data',
      'QtBluezPeripheralGattObject': '_qt_bluez_peripheral_gatt_object',
      'QBluetoothDeviceInfo': '_q_bluetooth_device_info',
      'QBluetoothHostInfo': '_q_bluetooth_host_info',
      'QBluetoothLocalDevice': '_q_bluetooth_local_device',
      'QBluetoothServiceInfoPrivate': '_q_bluetooth_service_info_private',
      'QLeDBusAdvertiser': '_q_le_d_bus_advertiser',
      'QtBluezDiscoveryManager': '_qt_bluez_discovery_manager',
      'QtBluezPeripheralConnectionManager': '_qt_bluez_peripheral_connection_manager',
      'QtBluezPeripheralDescriptor': '_qt_bluez_peripheral_descriptor',
      'RemoteDeviceManager': '_remote_device_manager',
      'OrgBluezProfile1ContextInterface': '_org_bluez_profile1_context_interface',
      'QBluetoothDeviceDiscoveryAgent': '_q_bluetooth_device_discovery_agent',
      'QBluetoothServiceInfo': '_q_bluetooth_service_info',
      'QLowEnergyCharacteristic': '_q_low_energy_characteristic',
      'QLowEnergyCharacteristicData': '_q_low_energy_characteristic_data',
      'QLowEnergyDescriptor': '_q_low_energy_descriptor',
      'QLowEnergyService': '_q_low_energy_service',
      'QLowEnergyServiceData': '_q_low_energy_service_data',
      'QLowEnergyController': '_q_low_energy_controller',
      'QLowEnergyControllerPrivate': '_q_low_energy_controller_private',
      'QLowEnergyServicePrivate': '_q_low_energy_service_private',
      'QBluetoothServer': '_q_bluetooth_server',
      'QBluetoothServiceDiscoveryAgent': '_q_bluetooth_service_discovery_agent',
      'QBluetoothSocket': '_q_bluetooth_socket',
      'QBluetoothSocketBasePrivate': '_q_bluetooth_socket_base_private',
      'QLowEnergyControllerPrivateBluezDBus': '_q_low_energy_controller_private_bluez_d_bus',
      'QLowEnergyControllerPrivateCommon': '_q_low_energy_controller_private_common',
      'QtBluezPeripheralApplication': '_qt_bluez_peripheral_application',
      'QtBluezPeripheralCharacteristic': '_qt_bluez_peripheral_characteristic',
      'QtBluezPeripheralService': '_qt_bluez_peripheral_service',
      'QBluetoothServerPrivate': '_q_bluetooth_server_private',
      'QBluetoothServiceDiscoveryAgentPrivate': '_q_bluetooth_service_discovery_agent_private',
      'QBluetoothSocketPrivateBluez': '_q_bluetooth_socket_private_bluez',
      'QBluetoothSocketPrivateBluezDBus': '_q_bluetooth_socket_private_bluez_d_bus',
      'QBluetoothSocketPrivateDummy': '_q_bluetooth_socket_private_dummy',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('DarwinBluetooth', 'QBluetooth', 'QBluezConst', 'QtBluetoothPrivate',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtBluetooth import QBluetoothSocketPrivateDummy'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
