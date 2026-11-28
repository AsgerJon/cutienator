"""
The 'cutienator.QtSerialBus' package provides the cute classes of the
part of Qt named QtSerialBus, under the name PySide6 has for it.

  from cutienator.QtSerialBus import QModbusCommEvent, QModbusDataUnit

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
    'QModbusCommEvent',
    'QModbusDataUnit',
    'QCanBusDeviceInfoPrivate',
    'QCanUniqueIdDescription',
    'QCanBusDeviceInfo',
    'QCanUniqueIdDescriptionPrivate',
    'QModbusDeviceIdentification',
    'QModbusPdu',
    'QCanBusFactory',
    'QCanDbcFileParser',
    'QCanDbcFileParserPrivate',
    'QModbusRequest',
    'QModbusResponse',
    'QModbusSerialAdu',
    'QModbusExceptionResponse',
    'QCanBus',
    'QCanBusDevicePrivate',
    'QCanBusFrame',
    'QCanSignalDescription',
    'QModbusDevicePrivate',
    'Timer',
    'QCanBusDevice',
    'QCanMessageDescription',
    'QCanSignalDescriptionPrivate',
    'QModbusDevice',
    'QModbusServerPrivate',
    'QCanFrameProcessor',
    'QCanMessageDescriptionPrivate',
    'QModbusReply',
    'QModbusRtuSerialServerPrivate',
    'QModbusServer',
    'QModbusTcpServerPrivate',
    'QCanFrameProcessorPrivate',
    'QModbusClientPrivate',
    'QModbusRtuSerialServer',
    'QModbusClient',
    'QModbusRtuSerialClientPrivate',
    'QModbusTcpClientPrivate',
    'QModbusTcpConnectionObserver',
    'QModbusRtuSerialClient',
    'QModbusTcpClient',
    'QModbusTcpServer',
    'Diagnostics',
    'EncapsulatedInterfaceTransport',
    'QtCanBus',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_modbus_comm_event import QModbusCommEvent
  from ._q_modbus_data_unit import QModbusDataUnit
  from ._q_can_bus_device_info_private import QCanBusDeviceInfoPrivate
  from ._q_can_unique_id_description import QCanUniqueIdDescription
  from ._q_can_bus_device_info import QCanBusDeviceInfo
  from ._q_can_unique_id_description_private import QCanUniqueIdDescriptionPrivate
  from ._q_modbus_device_identification import QModbusDeviceIdentification
  from ._q_modbus_pdu import QModbusPdu
  from ._q_can_bus_factory import QCanBusFactory
  from ._q_can_dbc_file_parser import QCanDbcFileParser
  from ._q_can_dbc_file_parser_private import QCanDbcFileParserPrivate
  from ._q_modbus_request import QModbusRequest
  from ._q_modbus_response import QModbusResponse
  from ._q_modbus_serial_adu import QModbusSerialAdu
  from ._q_modbus_exception_response import QModbusExceptionResponse
  from ._q_can_bus import QCanBus
  from ._q_can_bus_device_private import QCanBusDevicePrivate
  from ._q_can_bus_frame import QCanBusFrame
  from ._q_can_signal_description import QCanSignalDescription
  from ._q_modbus_device_private import QModbusDevicePrivate
  from ._timer import Timer
  from ._q_can_bus_device import QCanBusDevice
  from ._q_can_message_description import QCanMessageDescription
  from ._q_can_signal_description_private import QCanSignalDescriptionPrivate
  from ._q_modbus_device import QModbusDevice
  from ._q_modbus_server_private import QModbusServerPrivate
  from ._q_can_frame_processor import QCanFrameProcessor
  from ._q_can_message_description_private import QCanMessageDescriptionPrivate
  from ._q_modbus_reply import QModbusReply
  from ._q_modbus_rtu_serial_server_private import QModbusRtuSerialServerPrivate
  from ._q_modbus_server import QModbusServer
  from ._q_modbus_tcp_server_private import QModbusTcpServerPrivate
  from ._q_can_frame_processor_private import QCanFrameProcessorPrivate
  from ._q_modbus_client_private import QModbusClientPrivate
  from ._q_modbus_rtu_serial_server import QModbusRtuSerialServer
  from ._q_modbus_client import QModbusClient
  from ._q_modbus_rtu_serial_client_private import QModbusRtuSerialClientPrivate
  from ._q_modbus_tcp_client_private import QModbusTcpClientPrivate
  from ._q_modbus_tcp_connection_observer import QModbusTcpConnectionObserver
  from ._q_modbus_rtu_serial_client import QModbusRtuSerialClient
  from ._q_modbus_tcp_client import QModbusTcpClient
  from ._q_modbus_tcp_server import QModbusTcpServer
  from . import Diagnostics
  from . import EncapsulatedInterfaceTransport
  from . import QtCanBus
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QModbusCommEvent': '_q_modbus_comm_event',
      'QModbusDataUnit': '_q_modbus_data_unit',
      'QCanBusDeviceInfoPrivate': '_q_can_bus_device_info_private',
      'QCanUniqueIdDescription': '_q_can_unique_id_description',
      'QCanBusDeviceInfo': '_q_can_bus_device_info',
      'QCanUniqueIdDescriptionPrivate': '_q_can_unique_id_description_private',
      'QModbusDeviceIdentification': '_q_modbus_device_identification',
      'QModbusPdu': '_q_modbus_pdu',
      'QCanBusFactory': '_q_can_bus_factory',
      'QCanDbcFileParser': '_q_can_dbc_file_parser',
      'QCanDbcFileParserPrivate': '_q_can_dbc_file_parser_private',
      'QModbusRequest': '_q_modbus_request',
      'QModbusResponse': '_q_modbus_response',
      'QModbusSerialAdu': '_q_modbus_serial_adu',
      'QModbusExceptionResponse': '_q_modbus_exception_response',
      'QCanBus': '_q_can_bus',
      'QCanBusDevicePrivate': '_q_can_bus_device_private',
      'QCanBusFrame': '_q_can_bus_frame',
      'QCanSignalDescription': '_q_can_signal_description',
      'QModbusDevicePrivate': '_q_modbus_device_private',
      'Timer': '_timer',
      'QCanBusDevice': '_q_can_bus_device',
      'QCanMessageDescription': '_q_can_message_description',
      'QCanSignalDescriptionPrivate': '_q_can_signal_description_private',
      'QModbusDevice': '_q_modbus_device',
      'QModbusServerPrivate': '_q_modbus_server_private',
      'QCanFrameProcessor': '_q_can_frame_processor',
      'QCanMessageDescriptionPrivate': '_q_can_message_description_private',
      'QModbusReply': '_q_modbus_reply',
      'QModbusRtuSerialServerPrivate': '_q_modbus_rtu_serial_server_private',
      'QModbusServer': '_q_modbus_server',
      'QModbusTcpServerPrivate': '_q_modbus_tcp_server_private',
      'QCanFrameProcessorPrivate': '_q_can_frame_processor_private',
      'QModbusClientPrivate': '_q_modbus_client_private',
      'QModbusRtuSerialServer': '_q_modbus_rtu_serial_server',
      'QModbusClient': '_q_modbus_client',
      'QModbusRtuSerialClientPrivate': '_q_modbus_rtu_serial_client_private',
      'QModbusTcpClientPrivate': '_q_modbus_tcp_client_private',
      'QModbusTcpConnectionObserver': '_q_modbus_tcp_connection_observer',
      'QModbusRtuSerialClient': '_q_modbus_rtu_serial_client',
      'QModbusTcpClient': '_q_modbus_tcp_client',
      'QModbusTcpServer': '_q_modbus_tcp_server',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('Diagnostics', 'EncapsulatedInterfaceTransport', 'QtCanBus',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtSerialBus import QModbusTcpServer'. Python calls
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
