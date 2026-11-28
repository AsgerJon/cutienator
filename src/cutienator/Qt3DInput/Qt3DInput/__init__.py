"""
The namespace 'Qt3DInput' of Qt, a package of 'cutienator.Qt3DInput':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DInput import Qt3DInput
  Qt3DInput.QAbstractAxisInputData

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
    'QAbstractAxisInputData',
    'QAbstractPhysicalDeviceProxyData',
    'QActionData',
    'QActionInputData',
    'QAxisAccumulatorData',
    'QAxisData',
    'QAxisSettingData',
    'QInputChordData',
    'QInputSequenceData',
    'QInputSettingsData',
    'QKeyboardHandlerData',
    'QLogicalDeviceData',
    'QMouseDeviceData',
    'QMouseHandlerData',
    'QAbstractPhysicalDeviceBackendNodePrivate',
    'QAnalogAxisInputData',
    'QButtonAxisInputData',
    'QInputDeviceIntegrationFactory',
    'QInputDeviceIntegrationPrivate',
    'QInputDevicePlugin',
    'QAbstractActionInput',
    'QAbstractActionInputPrivate',
    'QAbstractAxisInput',
    'QAbstractAxisInputPrivate',
    'QAbstractPhysicalDevice',
    'QAbstractPhysicalDevicePrivate',
    'QAction',
    'QActionPrivate',
    'QAxis',
    'QAxisPrivate',
    'QAxisSetting',
    'QAxisSettingPrivate',
    'QInputAspect',
    'QInputAspectPrivate',
    'QAbstractPhysicalDeviceBackendNode',
    'QAbstractPhysicalDeviceProxy',
    'QAbstractPhysicalDeviceProxyPrivate',
    'QActionInput',
    'QActionInputPrivate',
    'QAnalogAxisInput',
    'QAnalogAxisInputPrivate',
    'QAxisAccumulator',
    'QAxisAccumulatorPrivate',
    'QButtonAxisInput',
    'QButtonAxisInputPrivate',
    'QGamepadInput',
    'QGenericInputDevice',
    'QInputChord',
    'QInputChordPrivate',
    'QInputDeviceIntegration',
    'QInputSequence',
    'QInputSequencePrivate',
    'QInputSettings',
    'QInputSettingsPrivate',
    'QKeyboardDevice',
    'QKeyboardDevicePrivate',
    'QLogicalDevicePrivate',
    'QMouseDevice',
    'QMouseDevicePrivate',
    'QMouseHandlerPrivate',
    'QKeyEvent',
    'QKeyboardHandlerPrivate',
    'QKeyboardHandler',
    'QMouseEvent',
    'QWheelEvent',
    'QMouseHandler',
    'QLogicalDevice',
    'Input',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt3_d_input__q_abstract_axis_input_data import QAbstractAxisInputData
  from .._qt3_d_input__q_abstract_physical_device_proxy_data import QAbstractPhysicalDeviceProxyData
  from .._qt3_d_input__q_action_data import QActionData
  from .._qt3_d_input__q_action_input_data import QActionInputData
  from .._qt3_d_input__q_axis_accumulator_data import QAxisAccumulatorData
  from .._qt3_d_input__q_axis_data import QAxisData
  from .._qt3_d_input__q_axis_setting_data import QAxisSettingData
  from .._qt3_d_input__q_input_chord_data import QInputChordData
  from .._qt3_d_input__q_input_sequence_data import QInputSequenceData
  from .._qt3_d_input__q_input_settings_data import QInputSettingsData
  from .._qt3_d_input__q_keyboard_handler_data import QKeyboardHandlerData
  from .._qt3_d_input__q_logical_device_data import QLogicalDeviceData
  from .._qt3_d_input__q_mouse_device_data import QMouseDeviceData
  from .._qt3_d_input__q_mouse_handler_data import QMouseHandlerData
  from .._qt3_d_input__q_abstract_physical_device_backend_node_private import QAbstractPhysicalDeviceBackendNodePrivate
  from .._qt3_d_input__q_analog_axis_input_data import QAnalogAxisInputData
  from .._qt3_d_input__q_button_axis_input_data import QButtonAxisInputData
  from .._qt3_d_input__q_input_device_integration_factory import QInputDeviceIntegrationFactory
  from .._qt3_d_input__q_input_device_integration_private import QInputDeviceIntegrationPrivate
  from .._qt3_d_input__q_input_device_plugin import QInputDevicePlugin
  from .._qt3_d_input__q_abstract_action_input import QAbstractActionInput
  from .._qt3_d_input__q_abstract_action_input_private import QAbstractActionInputPrivate
  from .._qt3_d_input__q_abstract_axis_input import QAbstractAxisInput
  from .._qt3_d_input__q_abstract_axis_input_private import QAbstractAxisInputPrivate
  from .._qt3_d_input__q_abstract_physical_device import QAbstractPhysicalDevice
  from .._qt3_d_input__q_abstract_physical_device_private import QAbstractPhysicalDevicePrivate
  from .._qt3_d_input__q_action import QAction
  from .._qt3_d_input__q_action_private import QActionPrivate
  from .._qt3_d_input__q_axis import QAxis
  from .._qt3_d_input__q_axis_private import QAxisPrivate
  from .._qt3_d_input__q_axis_setting import QAxisSetting
  from .._qt3_d_input__q_axis_setting_private import QAxisSettingPrivate
  from .._qt3_d_input__q_input_aspect import QInputAspect
  from .._qt3_d_input__q_input_aspect_private import QInputAspectPrivate
  from .._qt3_d_input__q_abstract_physical_device_backend_node import QAbstractPhysicalDeviceBackendNode
  from .._qt3_d_input__q_abstract_physical_device_proxy import QAbstractPhysicalDeviceProxy
  from .._qt3_d_input__q_abstract_physical_device_proxy_private import QAbstractPhysicalDeviceProxyPrivate
  from .._qt3_d_input__q_action_input import QActionInput
  from .._qt3_d_input__q_action_input_private import QActionInputPrivate
  from .._qt3_d_input__q_analog_axis_input import QAnalogAxisInput
  from .._qt3_d_input__q_analog_axis_input_private import QAnalogAxisInputPrivate
  from .._qt3_d_input__q_axis_accumulator import QAxisAccumulator
  from .._qt3_d_input__q_axis_accumulator_private import QAxisAccumulatorPrivate
  from .._qt3_d_input__q_button_axis_input import QButtonAxisInput
  from .._qt3_d_input__q_button_axis_input_private import QButtonAxisInputPrivate
  from .._qt3_d_input__q_gamepad_input import QGamepadInput
  from .._qt3_d_input__q_generic_input_device import QGenericInputDevice
  from .._qt3_d_input__q_input_chord import QInputChord
  from .._qt3_d_input__q_input_chord_private import QInputChordPrivate
  from .._qt3_d_input__q_input_device_integration import QInputDeviceIntegration
  from .._qt3_d_input__q_input_sequence import QInputSequence
  from .._qt3_d_input__q_input_sequence_private import QInputSequencePrivate
  from .._qt3_d_input__q_input_settings import QInputSettings
  from .._qt3_d_input__q_input_settings_private import QInputSettingsPrivate
  from .._qt3_d_input__q_keyboard_device import QKeyboardDevice
  from .._qt3_d_input__q_keyboard_device_private import QKeyboardDevicePrivate
  from .._qt3_d_input__q_logical_device_private import QLogicalDevicePrivate
  from .._qt3_d_input__q_mouse_device import QMouseDevice
  from .._qt3_d_input__q_mouse_device_private import QMouseDevicePrivate
  from .._qt3_d_input__q_mouse_handler_private import QMouseHandlerPrivate
  from .._qt3_d_input__q_key_event import QKeyEvent
  from .._qt3_d_input__q_keyboard_handler_private import QKeyboardHandlerPrivate
  from .._qt3_d_input__q_keyboard_handler import QKeyboardHandler
  from .._qt3_d_input__q_mouse_event import QMouseEvent
  from .._qt3_d_input__q_wheel_event import QWheelEvent
  from .._qt3_d_input__q_mouse_handler import QMouseHandler
  from .._qt3_d_input__q_logical_device import QLogicalDevice
  from . import Input
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QAbstractAxisInputData': '_qt3_d_input__q_abstract_axis_input_data',
      'QAbstractPhysicalDeviceProxyData': '_qt3_d_input__q_abstract_physical_device_proxy_data',
      'QActionData': '_qt3_d_input__q_action_data',
      'QActionInputData': '_qt3_d_input__q_action_input_data',
      'QAxisAccumulatorData': '_qt3_d_input__q_axis_accumulator_data',
      'QAxisData': '_qt3_d_input__q_axis_data',
      'QAxisSettingData': '_qt3_d_input__q_axis_setting_data',
      'QInputChordData': '_qt3_d_input__q_input_chord_data',
      'QInputSequenceData': '_qt3_d_input__q_input_sequence_data',
      'QInputSettingsData': '_qt3_d_input__q_input_settings_data',
      'QKeyboardHandlerData': '_qt3_d_input__q_keyboard_handler_data',
      'QLogicalDeviceData': '_qt3_d_input__q_logical_device_data',
      'QMouseDeviceData': '_qt3_d_input__q_mouse_device_data',
      'QMouseHandlerData': '_qt3_d_input__q_mouse_handler_data',
      'QAbstractPhysicalDeviceBackendNodePrivate': '_qt3_d_input__q_abstract_physical_device_backend_node_private',
      'QAnalogAxisInputData': '_qt3_d_input__q_analog_axis_input_data',
      'QButtonAxisInputData': '_qt3_d_input__q_button_axis_input_data',
      'QInputDeviceIntegrationFactory': '_qt3_d_input__q_input_device_integration_factory',
      'QInputDeviceIntegrationPrivate': '_qt3_d_input__q_input_device_integration_private',
      'QInputDevicePlugin': '_qt3_d_input__q_input_device_plugin',
      'QAbstractActionInput': '_qt3_d_input__q_abstract_action_input',
      'QAbstractActionInputPrivate': '_qt3_d_input__q_abstract_action_input_private',
      'QAbstractAxisInput': '_qt3_d_input__q_abstract_axis_input',
      'QAbstractAxisInputPrivate': '_qt3_d_input__q_abstract_axis_input_private',
      'QAbstractPhysicalDevice': '_qt3_d_input__q_abstract_physical_device',
      'QAbstractPhysicalDevicePrivate': '_qt3_d_input__q_abstract_physical_device_private',
      'QAction': '_qt3_d_input__q_action',
      'QActionPrivate': '_qt3_d_input__q_action_private',
      'QAxis': '_qt3_d_input__q_axis',
      'QAxisPrivate': '_qt3_d_input__q_axis_private',
      'QAxisSetting': '_qt3_d_input__q_axis_setting',
      'QAxisSettingPrivate': '_qt3_d_input__q_axis_setting_private',
      'QInputAspect': '_qt3_d_input__q_input_aspect',
      'QInputAspectPrivate': '_qt3_d_input__q_input_aspect_private',
      'QAbstractPhysicalDeviceBackendNode': '_qt3_d_input__q_abstract_physical_device_backend_node',
      'QAbstractPhysicalDeviceProxy': '_qt3_d_input__q_abstract_physical_device_proxy',
      'QAbstractPhysicalDeviceProxyPrivate': '_qt3_d_input__q_abstract_physical_device_proxy_private',
      'QActionInput': '_qt3_d_input__q_action_input',
      'QActionInputPrivate': '_qt3_d_input__q_action_input_private',
      'QAnalogAxisInput': '_qt3_d_input__q_analog_axis_input',
      'QAnalogAxisInputPrivate': '_qt3_d_input__q_analog_axis_input_private',
      'QAxisAccumulator': '_qt3_d_input__q_axis_accumulator',
      'QAxisAccumulatorPrivate': '_qt3_d_input__q_axis_accumulator_private',
      'QButtonAxisInput': '_qt3_d_input__q_button_axis_input',
      'QButtonAxisInputPrivate': '_qt3_d_input__q_button_axis_input_private',
      'QGamepadInput': '_qt3_d_input__q_gamepad_input',
      'QGenericInputDevice': '_qt3_d_input__q_generic_input_device',
      'QInputChord': '_qt3_d_input__q_input_chord',
      'QInputChordPrivate': '_qt3_d_input__q_input_chord_private',
      'QInputDeviceIntegration': '_qt3_d_input__q_input_device_integration',
      'QInputSequence': '_qt3_d_input__q_input_sequence',
      'QInputSequencePrivate': '_qt3_d_input__q_input_sequence_private',
      'QInputSettings': '_qt3_d_input__q_input_settings',
      'QInputSettingsPrivate': '_qt3_d_input__q_input_settings_private',
      'QKeyboardDevice': '_qt3_d_input__q_keyboard_device',
      'QKeyboardDevicePrivate': '_qt3_d_input__q_keyboard_device_private',
      'QLogicalDevicePrivate': '_qt3_d_input__q_logical_device_private',
      'QMouseDevice': '_qt3_d_input__q_mouse_device',
      'QMouseDevicePrivate': '_qt3_d_input__q_mouse_device_private',
      'QMouseHandlerPrivate': '_qt3_d_input__q_mouse_handler_private',
      'QKeyEvent': '_qt3_d_input__q_key_event',
      'QKeyboardHandlerPrivate': '_qt3_d_input__q_keyboard_handler_private',
      'QKeyboardHandler': '_qt3_d_input__q_keyboard_handler',
      'QMouseEvent': '_qt3_d_input__q_mouse_event',
      'QWheelEvent': '_qt3_d_input__q_wheel_event',
      'QMouseHandler': '_qt3_d_input__q_mouse_handler',
      'QLogicalDevice': '_qt3_d_input__q_logical_device',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('Input',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DInput.QAbstractAxisInputData'. Python calls this
    for a name the package does not hold yet, and what it gives is kept here
    for the next time.

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
