"""
The 'cutienator.QtStateMachine' package provides the cute classes of the
part of Qt named QtStateMachine, under the name PySide6 has for it.

  from cutienator.QtStateMachine import QAbstractState, QAbstractTransition

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
    'QAbstractState',
    'QAbstractTransition',
    'QState',
    'QEventTransition',
    'QFinalState',
    'QHistoryState',
    'QSignalTransition',
    'QStateMachine',
    'QKeyEventTransition',
    'QMouseEventTransition',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_abstract_state import QAbstractState
  from ._q_abstract_transition import QAbstractTransition
  from ._q_state import QState
  from ._q_event_transition import QEventTransition
  from ._q_final_state import QFinalState
  from ._q_history_state import QHistoryState
  from ._q_signal_transition import QSignalTransition
  from ._q_state_machine import QStateMachine
  from ._q_key_event_transition import QKeyEventTransition
  from ._q_mouse_event_transition import QMouseEventTransition
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QAbstractState': '_q_abstract_state',
      'QAbstractTransition': '_q_abstract_transition',
      'QState': '_q_state',
      'QEventTransition': '_q_event_transition',
      'QFinalState': '_q_final_state',
      'QHistoryState': '_q_history_state',
      'QSignalTransition': '_q_signal_transition',
      'QStateMachine': '_q_state_machine',
      'QKeyEventTransition': '_q_key_event_transition',
      'QMouseEventTransition': '_q_mouse_event_transition',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtStateMachine import QMouseEventTransition'. Python calls
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
