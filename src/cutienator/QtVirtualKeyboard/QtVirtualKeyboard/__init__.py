"""
The namespace 'QtVirtualKeyboard' of Qt, a package of 'cutienator.QtVirtualKeyboard':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtVirtualKeyboard import QtVirtualKeyboard
  QtVirtualKeyboard.RecursiveMethodGuard

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._qt_virtual_keyboard import QtVirtualKeyboard as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'RecursiveMethodGuard',
    'AbstractInputPanel',
    'AppInputPanelPrivate',
    'EnterKeyAction',
    'EnterKeyActionAttachedType',
    'Settings',
    'VirtualKeyboard',
    'VirtualKeyboardAttachedType',
    'AppInputPanel',
    'GestureRecognizer',
    'InputMethodPrivate',
    'UnipenTrace',
    'DesktopInputSelectionControl',
    'HandwritingGestureRecognizer',
    'ShadowInputContext',
    'ShiftHandler',
    'FallbackInputMethod',
    'InputMethod',
    'PlainInputMethod',
    'PlatformInputContext',
    'DesktopInputPanel',
    'InputSelectionHandle',
    'InputView',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_virtual_keyboard__recursive_method_guard import RecursiveMethodGuard
  from .._qt_virtual_keyboard__abstract_input_panel import AbstractInputPanel
  from .._qt_virtual_keyboard__app_input_panel_private import AppInputPanelPrivate
  from .._qt_virtual_keyboard__enter_key_action import EnterKeyAction
  from .._qt_virtual_keyboard__enter_key_action_attached_type import EnterKeyActionAttachedType
  from .._qt_virtual_keyboard__settings import Settings
  from .._qt_virtual_keyboard__virtual_keyboard import VirtualKeyboard
  from .._qt_virtual_keyboard__virtual_keyboard_attached_type import VirtualKeyboardAttachedType
  from .._qt_virtual_keyboard__app_input_panel import AppInputPanel
  from .._qt_virtual_keyboard__gesture_recognizer import GestureRecognizer
  from .._qt_virtual_keyboard__input_method_private import InputMethodPrivate
  from .._qt_virtual_keyboard__unipen_trace import UnipenTrace
  from .._qt_virtual_keyboard__desktop_input_selection_control import DesktopInputSelectionControl
  from .._qt_virtual_keyboard__handwriting_gesture_recognizer import HandwritingGestureRecognizer
  from .._qt_virtual_keyboard__shadow_input_context import ShadowInputContext
  from .._qt_virtual_keyboard__shift_handler import ShiftHandler
  from .._qt_virtual_keyboard__fallback_input_method import FallbackInputMethod
  from .._qt_virtual_keyboard__input_method import InputMethod
  from .._qt_virtual_keyboard__plain_input_method import PlainInputMethod
  from .._qt_virtual_keyboard__platform_input_context import PlatformInputContext
  from .._qt_virtual_keyboard__desktop_input_panel import DesktopInputPanel
  from .._qt_virtual_keyboard__input_selection_handle import InputSelectionHandle
  from .._qt_virtual_keyboard__input_view import InputView
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'RecursiveMethodGuard': '_qt_virtual_keyboard__recursive_method_guard',
      'AbstractInputPanel': '_qt_virtual_keyboard__abstract_input_panel',
      'AppInputPanelPrivate': '_qt_virtual_keyboard__app_input_panel_private',
      'EnterKeyAction': '_qt_virtual_keyboard__enter_key_action',
      'EnterKeyActionAttachedType': '_qt_virtual_keyboard__enter_key_action_attached_type',
      'Settings': '_qt_virtual_keyboard__settings',
      'VirtualKeyboard': '_qt_virtual_keyboard__virtual_keyboard',
      'VirtualKeyboardAttachedType': '_qt_virtual_keyboard__virtual_keyboard_attached_type',
      'AppInputPanel': '_qt_virtual_keyboard__app_input_panel',
      'GestureRecognizer': '_qt_virtual_keyboard__gesture_recognizer',
      'InputMethodPrivate': '_qt_virtual_keyboard__input_method_private',
      'UnipenTrace': '_qt_virtual_keyboard__unipen_trace',
      'DesktopInputSelectionControl': '_qt_virtual_keyboard__desktop_input_selection_control',
      'HandwritingGestureRecognizer': '_qt_virtual_keyboard__handwriting_gesture_recognizer',
      'ShadowInputContext': '_qt_virtual_keyboard__shadow_input_context',
      'ShiftHandler': '_qt_virtual_keyboard__shift_handler',
      'FallbackInputMethod': '_qt_virtual_keyboard__fallback_input_method',
      'InputMethod': '_qt_virtual_keyboard__input_method',
      'PlainInputMethod': '_qt_virtual_keyboard__plain_input_method',
      'PlatformInputContext': '_qt_virtual_keyboard__platform_input_context',
      'DesktopInputPanel': '_qt_virtual_keyboard__desktop_input_panel',
      'InputSelectionHandle': '_qt_virtual_keyboard__input_selection_handle',
      'InputView': '_qt_virtual_keyboard__input_view',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtVirtualKeyboard.RecursiveMethodGuard'. Python calls
    this for a name the package does not hold yet, and what it gives is kept
    here for the next time.

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
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
