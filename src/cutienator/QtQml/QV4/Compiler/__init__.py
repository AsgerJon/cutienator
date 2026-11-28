"""
The namespace 'QV4::Compiler' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QV4
  QV4.Compiler.Class

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from ..._q_v4__compiler import Compiler as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'Class',
    'ExportEntry',
    'ImportEntry',
    'TemplateObject',
    'ControlFlow',
    'Module',
    'StringTableGenerator',
    'CodegenWarningInterface',
    'Context',
    'ControlFlowUnwind',
    'ControlFlowBlock',
    'ControlFlowCatch',
    'ControlFlowFinally',
    'ControlFlowUnwindCleanup',
    'ControlFlowWith',
    'JSUnitGenerator',
    'Codegen',
    'ControlFlowLoop',
    'ScanFunctions',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._q_v4__compiler__class import Class
  from ..._q_v4__compiler__export_entry import ExportEntry
  from ..._q_v4__compiler__import_entry import ImportEntry
  from ..._q_v4__compiler__template_object import TemplateObject
  from ..._q_v4__compiler__control_flow import ControlFlow
  from ..._q_v4__compiler__module import Module
  from ..._q_v4__compiler__string_table_generator import StringTableGenerator
  from ..._q_v4__compiler__codegen_warning_interface import CodegenWarningInterface
  from ..._q_v4__compiler__context import Context
  from ..._q_v4__compiler__control_flow_unwind import ControlFlowUnwind
  from ..._q_v4__compiler__control_flow_block import ControlFlowBlock
  from ..._q_v4__compiler__control_flow_catch import ControlFlowCatch
  from ..._q_v4__compiler__control_flow_finally import ControlFlowFinally
  from ..._q_v4__compiler__control_flow_unwind_cleanup import ControlFlowUnwindCleanup
  from ..._q_v4__compiler__control_flow_with import ControlFlowWith
  from ..._q_v4__compiler__j_s_unit_generator import JSUnitGenerator
  from ..._q_v4__compiler__codegen import Codegen
  from ..._q_v4__compiler__control_flow_loop import ControlFlowLoop
  from ..._q_v4__compiler__scan_functions import ScanFunctions
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Class': '_q_v4__compiler__class',
      'ExportEntry': '_q_v4__compiler__export_entry',
      'ImportEntry': '_q_v4__compiler__import_entry',
      'TemplateObject': '_q_v4__compiler__template_object',
      'ControlFlow': '_q_v4__compiler__control_flow',
      'Module': '_q_v4__compiler__module',
      'StringTableGenerator': '_q_v4__compiler__string_table_generator',
      'CodegenWarningInterface': '_q_v4__compiler__codegen_warning_interface',
      'Context': '_q_v4__compiler__context',
      'ControlFlowUnwind': '_q_v4__compiler__control_flow_unwind',
      'ControlFlowBlock': '_q_v4__compiler__control_flow_block',
      'ControlFlowCatch': '_q_v4__compiler__control_flow_catch',
      'ControlFlowFinally': '_q_v4__compiler__control_flow_finally',
      'ControlFlowUnwindCleanup': '_q_v4__compiler__control_flow_unwind_cleanup',
      'ControlFlowWith': '_q_v4__compiler__control_flow_with',
      'JSUnitGenerator': '_q_v4__compiler__j_s_unit_generator',
      'Codegen': '_q_v4__compiler__codegen',
      'ControlFlowLoop': '_q_v4__compiler__control_flow_loop',
      'ScanFunctions': '_q_v4__compiler__scan_functions',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QV4.Compiler.Class'. Python calls this for a name the
    package does not hold yet, and what it gives is kept here for the next
    time.

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
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
