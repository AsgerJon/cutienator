"""
The namespace 'Qt3DInput::Input' of Qt, a package of 'cutienator.Qt3DInput':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DInput import Qt3DInput
  Qt3DInput.Input.ActionInputManager

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
    'ActionInputManager',
    'ActionManager',
    'AnalogAxisInputManager',
    'AxisAccumulatorManager',
    'AxisIdFilter',
    'AxisIdSetting',
    'AxisManager',
    'AxisSettingManager',
    'ButtonAxisInputManager',
    'GenericDeviceBackendNodeManager',
    'InputChordManager',
    'InputSequenceManager',
    'KeyboardDeviceManager',
    'KeyboardInputManager',
    'LogicalDeviceManager',
    'MouseDeviceManager',
    'MouseInputManager',
    'MovingAverage',
    'AssignKeyboardFocusJob',
    'AxisAccumulatorJob',
    'GenericDeviceBackendFunctor',
    'InputSettingsFunctor',
    'KeyboardDeviceFunctor',
    'KeyboardHandlerFunctor',
    'LoadProxyDeviceJob',
    'LogicalDeviceNodeFunctor',
    'MouseHandlerFunctor',
    'PhysicalDeviceProxyManager',
    'PhysicalDeviceProxyNodeFunctor',
    'UpdateAxisActionJob',
    'BackendNode',
    'AbstractActionInput',
    'AbstractAxisInput',
    'Action',
    'Axis',
    'AxisAccumulator',
    'AxisSetting',
    'InputHandler',
    'InputSettings',
    'KeyboardHandler',
    'LogicalDevice',
    'MouseDeviceFunctor',
    'MouseHandler',
    'PhysicalDeviceProxy',
    'ActionInput',
    'AnalogAxisInput',
    'ButtonAxisInput',
    'GenericDeviceBackendNode',
    'InputChord',
    'InputSequence',
    'KeyboardDevice',
    'KeyboardMouseGenericDeviceIntegration',
    'MouseDevice',
    'JobTypes',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._qt3_d_input__input__action_input_manager import ActionInputManager
  from ..._qt3_d_input__input__action_manager import ActionManager
  from ..._qt3_d_input__input__analog_axis_input_manager import AnalogAxisInputManager
  from ..._qt3_d_input__input__axis_accumulator_manager import AxisAccumulatorManager
  from ..._qt3_d_input__input__axis_id_filter import AxisIdFilter
  from ..._qt3_d_input__input__axis_id_setting import AxisIdSetting
  from ..._qt3_d_input__input__axis_manager import AxisManager
  from ..._qt3_d_input__input__axis_setting_manager import AxisSettingManager
  from ..._qt3_d_input__input__button_axis_input_manager import ButtonAxisInputManager
  from ..._qt3_d_input__input__generic_device_backend_node_manager import GenericDeviceBackendNodeManager
  from ..._qt3_d_input__input__input_chord_manager import InputChordManager
  from ..._qt3_d_input__input__input_sequence_manager import InputSequenceManager
  from ..._qt3_d_input__input__keyboard_device_manager import KeyboardDeviceManager
  from ..._qt3_d_input__input__keyboard_input_manager import KeyboardInputManager
  from ..._qt3_d_input__input__logical_device_manager import LogicalDeviceManager
  from ..._qt3_d_input__input__mouse_device_manager import MouseDeviceManager
  from ..._qt3_d_input__input__mouse_input_manager import MouseInputManager
  from ..._qt3_d_input__input__moving_average import MovingAverage
  from ..._qt3_d_input__input__assign_keyboard_focus_job import AssignKeyboardFocusJob
  from ..._qt3_d_input__input__axis_accumulator_job import AxisAccumulatorJob
  from ..._qt3_d_input__input__generic_device_backend_functor import GenericDeviceBackendFunctor
  from ..._qt3_d_input__input__input_settings_functor import InputSettingsFunctor
  from ..._qt3_d_input__input__keyboard_device_functor import KeyboardDeviceFunctor
  from ..._qt3_d_input__input__keyboard_handler_functor import KeyboardHandlerFunctor
  from ..._qt3_d_input__input__load_proxy_device_job import LoadProxyDeviceJob
  from ..._qt3_d_input__input__logical_device_node_functor import LogicalDeviceNodeFunctor
  from ..._qt3_d_input__input__mouse_handler_functor import MouseHandlerFunctor
  from ..._qt3_d_input__input__physical_device_proxy_manager import PhysicalDeviceProxyManager
  from ..._qt3_d_input__input__physical_device_proxy_node_functor import PhysicalDeviceProxyNodeFunctor
  from ..._qt3_d_input__input__update_axis_action_job import UpdateAxisActionJob
  from ..._qt3_d_input__input__backend_node import BackendNode
  from ..._qt3_d_input__input__abstract_action_input import AbstractActionInput
  from ..._qt3_d_input__input__abstract_axis_input import AbstractAxisInput
  from ..._qt3_d_input__input__action import Action
  from ..._qt3_d_input__input__axis import Axis
  from ..._qt3_d_input__input__axis_accumulator import AxisAccumulator
  from ..._qt3_d_input__input__axis_setting import AxisSetting
  from ..._qt3_d_input__input__input_handler import InputHandler
  from ..._qt3_d_input__input__input_settings import InputSettings
  from ..._qt3_d_input__input__keyboard_handler import KeyboardHandler
  from ..._qt3_d_input__input__logical_device import LogicalDevice
  from ..._qt3_d_input__input__mouse_device_functor import MouseDeviceFunctor
  from ..._qt3_d_input__input__mouse_handler import MouseHandler
  from ..._qt3_d_input__input__physical_device_proxy import PhysicalDeviceProxy
  from ..._qt3_d_input__input__action_input import ActionInput
  from ..._qt3_d_input__input__analog_axis_input import AnalogAxisInput
  from ..._qt3_d_input__input__button_axis_input import ButtonAxisInput
  from ..._qt3_d_input__input__generic_device_backend_node import GenericDeviceBackendNode
  from ..._qt3_d_input__input__input_chord import InputChord
  from ..._qt3_d_input__input__input_sequence import InputSequence
  from ..._qt3_d_input__input__keyboard_device import KeyboardDevice
  from ..._qt3_d_input__input__keyboard_mouse_generic_device_integration import KeyboardMouseGenericDeviceIntegration
  from ..._qt3_d_input__input__mouse_device import MouseDevice
  from . import JobTypes
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ActionInputManager': '_qt3_d_input__input__action_input_manager',
      'ActionManager': '_qt3_d_input__input__action_manager',
      'AnalogAxisInputManager': '_qt3_d_input__input__analog_axis_input_manager',
      'AxisAccumulatorManager': '_qt3_d_input__input__axis_accumulator_manager',
      'AxisIdFilter': '_qt3_d_input__input__axis_id_filter',
      'AxisIdSetting': '_qt3_d_input__input__axis_id_setting',
      'AxisManager': '_qt3_d_input__input__axis_manager',
      'AxisSettingManager': '_qt3_d_input__input__axis_setting_manager',
      'ButtonAxisInputManager': '_qt3_d_input__input__button_axis_input_manager',
      'GenericDeviceBackendNodeManager': '_qt3_d_input__input__generic_device_backend_node_manager',
      'InputChordManager': '_qt3_d_input__input__input_chord_manager',
      'InputSequenceManager': '_qt3_d_input__input__input_sequence_manager',
      'KeyboardDeviceManager': '_qt3_d_input__input__keyboard_device_manager',
      'KeyboardInputManager': '_qt3_d_input__input__keyboard_input_manager',
      'LogicalDeviceManager': '_qt3_d_input__input__logical_device_manager',
      'MouseDeviceManager': '_qt3_d_input__input__mouse_device_manager',
      'MouseInputManager': '_qt3_d_input__input__mouse_input_manager',
      'MovingAverage': '_qt3_d_input__input__moving_average',
      'AssignKeyboardFocusJob': '_qt3_d_input__input__assign_keyboard_focus_job',
      'AxisAccumulatorJob': '_qt3_d_input__input__axis_accumulator_job',
      'GenericDeviceBackendFunctor': '_qt3_d_input__input__generic_device_backend_functor',
      'InputSettingsFunctor': '_qt3_d_input__input__input_settings_functor',
      'KeyboardDeviceFunctor': '_qt3_d_input__input__keyboard_device_functor',
      'KeyboardHandlerFunctor': '_qt3_d_input__input__keyboard_handler_functor',
      'LoadProxyDeviceJob': '_qt3_d_input__input__load_proxy_device_job',
      'LogicalDeviceNodeFunctor': '_qt3_d_input__input__logical_device_node_functor',
      'MouseHandlerFunctor': '_qt3_d_input__input__mouse_handler_functor',
      'PhysicalDeviceProxyManager': '_qt3_d_input__input__physical_device_proxy_manager',
      'PhysicalDeviceProxyNodeFunctor': '_qt3_d_input__input__physical_device_proxy_node_functor',
      'UpdateAxisActionJob': '_qt3_d_input__input__update_axis_action_job',
      'BackendNode': '_qt3_d_input__input__backend_node',
      'AbstractActionInput': '_qt3_d_input__input__abstract_action_input',
      'AbstractAxisInput': '_qt3_d_input__input__abstract_axis_input',
      'Action': '_qt3_d_input__input__action',
      'Axis': '_qt3_d_input__input__axis',
      'AxisAccumulator': '_qt3_d_input__input__axis_accumulator',
      'AxisSetting': '_qt3_d_input__input__axis_setting',
      'InputHandler': '_qt3_d_input__input__input_handler',
      'InputSettings': '_qt3_d_input__input__input_settings',
      'KeyboardHandler': '_qt3_d_input__input__keyboard_handler',
      'LogicalDevice': '_qt3_d_input__input__logical_device',
      'MouseDeviceFunctor': '_qt3_d_input__input__mouse_device_functor',
      'MouseHandler': '_qt3_d_input__input__mouse_handler',
      'PhysicalDeviceProxy': '_qt3_d_input__input__physical_device_proxy',
      'ActionInput': '_qt3_d_input__input__action_input',
      'AnalogAxisInput': '_qt3_d_input__input__analog_axis_input',
      'ButtonAxisInput': '_qt3_d_input__input__button_axis_input',
      'GenericDeviceBackendNode': '_qt3_d_input__input__generic_device_backend_node',
      'InputChord': '_qt3_d_input__input__input_chord',
      'InputSequence': '_qt3_d_input__input__input_sequence',
      'KeyboardDevice': '_qt3_d_input__input__keyboard_device',
      'KeyboardMouseGenericDeviceIntegration': '_qt3_d_input__input__keyboard_mouse_generic_device_integration',
      'MouseDevice': '_qt3_d_input__input__mouse_device',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('JobTypes',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DInput.Input.ActionInputManager'. Python calls this
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
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
