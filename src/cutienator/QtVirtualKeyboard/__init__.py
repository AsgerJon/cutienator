"""
The 'cutienator.QtVirtualKeyboard' package provides the cute classes of
the part of Qt named QtVirtualKeyboard, under the name PySide6 has for
it.

  from cutienator.QtVirtualKeyboard import QVirtualKeyboardAbstractInputMethodPrivate, QVirtualKeyboardDictionary

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
    'QVirtualKeyboardAbstractInputMethodPrivate',
    'QVirtualKeyboardDictionary',
    'QVirtualKeyboardDictionaryManager',
    'QVirtualKeyboardObserver',
    'QVirtualKeyboardTrace',
    'QVirtualKeyboardInputContext',
    'QVirtualKeyboardAbstractInputMethod',
    'QVirtualKeyboardInputEngine',
    'QVirtualKeyboardSelectionListModel',
    'QVirtualKeyboardInputContextPrivate',
    'QVirtualKeyboardScopedState',
    'QVirtualKeyboardFeatures',
    'QtVirtualKeyboard',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_virtual_keyboard_abstract_input_method_private import QVirtualKeyboardAbstractInputMethodPrivate
  from ._q_virtual_keyboard_dictionary import QVirtualKeyboardDictionary
  from ._q_virtual_keyboard_dictionary_manager import QVirtualKeyboardDictionaryManager
  from ._q_virtual_keyboard_observer import QVirtualKeyboardObserver
  from ._q_virtual_keyboard_trace import QVirtualKeyboardTrace
  from ._q_virtual_keyboard_input_context import QVirtualKeyboardInputContext
  from ._q_virtual_keyboard_abstract_input_method import QVirtualKeyboardAbstractInputMethod
  from ._q_virtual_keyboard_input_engine import QVirtualKeyboardInputEngine
  from ._q_virtual_keyboard_selection_list_model import QVirtualKeyboardSelectionListModel
  from ._q_virtual_keyboard_input_context_private import QVirtualKeyboardInputContextPrivate
  from ._q_virtual_keyboard_scoped_state import QVirtualKeyboardScopedState
  from . import QVirtualKeyboardFeatures
  from . import QtVirtualKeyboard
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QVirtualKeyboardAbstractInputMethodPrivate': '_q_virtual_keyboard_abstract_input_method_private',
      'QVirtualKeyboardDictionary': '_q_virtual_keyboard_dictionary',
      'QVirtualKeyboardDictionaryManager': '_q_virtual_keyboard_dictionary_manager',
      'QVirtualKeyboardObserver': '_q_virtual_keyboard_observer',
      'QVirtualKeyboardTrace': '_q_virtual_keyboard_trace',
      'QVirtualKeyboardInputContext': '_q_virtual_keyboard_input_context',
      'QVirtualKeyboardAbstractInputMethod': '_q_virtual_keyboard_abstract_input_method',
      'QVirtualKeyboardInputEngine': '_q_virtual_keyboard_input_engine',
      'QVirtualKeyboardSelectionListModel': '_q_virtual_keyboard_selection_list_model',
      'QVirtualKeyboardInputContextPrivate': '_q_virtual_keyboard_input_context_private',
      'QVirtualKeyboardScopedState': '_q_virtual_keyboard_scoped_state',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QVirtualKeyboardFeatures', 'QtVirtualKeyboard',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtVirtualKeyboard import QVirtualKeyboardScopedState'. Python calls
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
