"""
CommunicationMode stands for the flags enum
'QBluetoothPermission::CommunicationMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class CommunicationMode(CuteFlags, number='unsigned char'):
  """
  The flags enum 'QBluetoothPermission::CommunicationMode' of Qt, with the 3
  names Qt gives in it. Qt names the type of its combinations
  'QBluetoothPermission::CommunicationModes'.
  """

  Access = 0x1
  Advertise = 0x2
  Default = 0x3
