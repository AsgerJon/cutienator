"""
The namespace 'QScxmlExecutableContent' of Qt, a package of 'cutienator.QtScxml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtScxml import QScxmlExecutableContent
  QScxmlExecutableContent.AssignmentInfo

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
    'AssignmentInfo',
    'EvaluatorInfo',
    'ForeachInfo',
    'Instruction',
    'InvokeInfo',
    'ParameterInfo',
    'StateTable',
    'Assign',
    'Cancel',
    'DoneData',
    'Foreach',
    'If',
    'Initialize',
    'InstructionSequence',
    'InstructionSequences',
    'JavaScript',
    'Log',
    'Raise',
    'Send',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_scxml_executable_content__assignment_info import AssignmentInfo
  from .._q_scxml_executable_content__evaluator_info import EvaluatorInfo
  from .._q_scxml_executable_content__foreach_info import ForeachInfo
  from .._q_scxml_executable_content__instruction import Instruction
  from .._q_scxml_executable_content__invoke_info import InvokeInfo
  from .._q_scxml_executable_content__parameter_info import ParameterInfo
  from .._q_scxml_executable_content__state_table import StateTable
  from .._q_scxml_executable_content__assign import Assign
  from .._q_scxml_executable_content__cancel import Cancel
  from .._q_scxml_executable_content__done_data import DoneData
  from .._q_scxml_executable_content__foreach import Foreach
  from .._q_scxml_executable_content__if import If
  from .._q_scxml_executable_content__initialize import Initialize
  from .._q_scxml_executable_content__instruction_sequence import InstructionSequence
  from .._q_scxml_executable_content__instruction_sequences import InstructionSequences
  from .._q_scxml_executable_content__java_script import JavaScript
  from .._q_scxml_executable_content__log import Log
  from .._q_scxml_executable_content__raise import Raise
  from .._q_scxml_executable_content__send import Send
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AssignmentInfo': '_q_scxml_executable_content__assignment_info',
      'EvaluatorInfo': '_q_scxml_executable_content__evaluator_info',
      'ForeachInfo': '_q_scxml_executable_content__foreach_info',
      'Instruction': '_q_scxml_executable_content__instruction',
      'InvokeInfo': '_q_scxml_executable_content__invoke_info',
      'ParameterInfo': '_q_scxml_executable_content__parameter_info',
      'StateTable': '_q_scxml_executable_content__state_table',
      'Assign': '_q_scxml_executable_content__assign',
      'Cancel': '_q_scxml_executable_content__cancel',
      'DoneData': '_q_scxml_executable_content__done_data',
      'Foreach': '_q_scxml_executable_content__foreach',
      'If': '_q_scxml_executable_content__if',
      'Initialize': '_q_scxml_executable_content__initialize',
      'InstructionSequence': '_q_scxml_executable_content__instruction_sequence',
      'InstructionSequences': '_q_scxml_executable_content__instruction_sequences',
      'JavaScript': '_q_scxml_executable_content__java_script',
      'Log': '_q_scxml_executable_content__log',
      'Raise': '_q_scxml_executable_content__raise',
      'Send': '_q_scxml_executable_content__send',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QScxmlExecutableContent.AssignmentInfo'. Python calls
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
    return [*__all__]
