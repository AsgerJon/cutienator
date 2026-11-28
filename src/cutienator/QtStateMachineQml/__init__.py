"""
The 'cutienator.QtStateMachineQml' package provides the cute classes of
the part of Qt named QtStateMachineQml, under the name PySide6 has for
it.

  from cutienator.QtStateMachineQml import QAbstractStateForeign, QHistoryStateForeign

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
    'QAbstractStateForeign',
    'QHistoryStateForeign',
    'QSignalTransitionForeign',
    'QStateForeign',
    'State',
    'FinalState',
    'StateMachine',
    'TimeoutTransition',
    'SignalTransition',
    'SignalTransitionParser',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_abstract_state_foreign import QAbstractStateForeign
  from ._q_history_state_foreign import QHistoryStateForeign
  from ._q_signal_transition_foreign import QSignalTransitionForeign
  from ._q_state_foreign import QStateForeign
  from ._state import State
  from ._final_state import FinalState
  from ._state_machine import StateMachine
  from ._timeout_transition import TimeoutTransition
  from ._signal_transition import SignalTransition
  from ._signal_transition_parser import SignalTransitionParser
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QAbstractStateForeign': '_q_abstract_state_foreign',
      'QHistoryStateForeign': '_q_history_state_foreign',
      'QSignalTransitionForeign': '_q_signal_transition_foreign',
      'QStateForeign': '_q_state_foreign',
      'State': '_state',
      'FinalState': '_final_state',
      'StateMachine': '_state_machine',
      'TimeoutTransition': '_timeout_transition',
      'SignalTransition': '_signal_transition',
      'SignalTransitionParser': '_signal_transition_parser',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtStateMachineQml import SignalTransitionParser'. Python calls
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
