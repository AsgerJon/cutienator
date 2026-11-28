"""
The 'cutienator.QtScxmlQml' package provides the cute classes of the
part of Qt named QtScxmlQml, under the name PySide6 has for it.

  from cutienator.QtScxmlQml import QScxmlEventForeign, QScxmlStateMachineExtended

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
    'QScxmlEventForeign',
    'QScxmlStateMachineExtended',
    'QScxmlStateMachineForeign',
    'QScxmlEventConnection',
    'QScxmlInvokedServices',
    'QScxmlStateMachineLoader',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_scxml_event_foreign import QScxmlEventForeign
  from ._q_scxml_state_machine_extended import QScxmlStateMachineExtended
  from ._q_scxml_state_machine_foreign import QScxmlStateMachineForeign
  from ._q_scxml_event_connection import QScxmlEventConnection
  from ._q_scxml_invoked_services import QScxmlInvokedServices
  from ._q_scxml_state_machine_loader import QScxmlStateMachineLoader
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QScxmlEventForeign': '_q_scxml_event_foreign',
      'QScxmlStateMachineExtended': '_q_scxml_state_machine_extended',
      'QScxmlStateMachineForeign': '_q_scxml_state_machine_foreign',
      'QScxmlEventConnection': '_q_scxml_event_connection',
      'QScxmlInvokedServices': '_q_scxml_invoked_services',
      'QScxmlStateMachineLoader': '_q_scxml_state_machine_loader',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtScxmlQml import QScxmlStateMachineLoader'. Python calls
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
