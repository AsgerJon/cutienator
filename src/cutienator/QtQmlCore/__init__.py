"""
The 'cutienator.QtQmlCore' package provides the cute classes of the part
of Qt named QtQmlCore, under the name PySide6 has for it.

  from cutienator.QtQmlCore import QQmlCameraPermission, QQmlMicrophonePermission

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
    'QQmlCameraPermission',
    'QQmlMicrophonePermission',
    'QQmlSettings',
    'QQmlSystemInformation',
    'QQmlBluetoothPermission',
    'QQmlCalendarPermission',
    'QQmlContactsPermission',
    'QQmlQLocationPermission',
    'QQmlStandardPaths',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_qml_camera_permission import QQmlCameraPermission
  from ._q_qml_microphone_permission import QQmlMicrophonePermission
  from ._q_qml_settings import QQmlSettings
  from ._q_qml_system_information import QQmlSystemInformation
  from ._q_qml_bluetooth_permission import QQmlBluetoothPermission
  from ._q_qml_calendar_permission import QQmlCalendarPermission
  from ._q_qml_contacts_permission import QQmlContactsPermission
  from ._q_qml_q_location_permission import QQmlQLocationPermission
  from ._q_qml_standard_paths import QQmlStandardPaths
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQmlCameraPermission': '_q_qml_camera_permission',
      'QQmlMicrophonePermission': '_q_qml_microphone_permission',
      'QQmlSettings': '_q_qml_settings',
      'QQmlSystemInformation': '_q_qml_system_information',
      'QQmlBluetoothPermission': '_q_qml_bluetooth_permission',
      'QQmlCalendarPermission': '_q_qml_calendar_permission',
      'QQmlContactsPermission': '_q_qml_contacts_permission',
      'QQmlQLocationPermission': '_q_qml_q_location_permission',
      'QQmlStandardPaths': '_q_qml_standard_paths',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQmlCore import QQmlStandardPaths'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
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
