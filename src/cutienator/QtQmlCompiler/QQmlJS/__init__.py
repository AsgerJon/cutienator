"""
The namespace 'QQmlJS' of Qt, a package of 'cutienator.QtQmlCompiler':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQmlCompiler import QQmlJS
  QQmlJS.AotStatsEntry

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._q_qml_j_s import QQmlJS as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'AotStatsEntry',
    'FileSelectedType',
    'FileSelectorInfo',
    'Export',
    'Import',
    'LoggerCategory',
    'LoggerCategoryPrivate',
    'QQmlJSAotCompilerStats',
    'AotStats',
    'AotStatsReporter',
    'ContextualType',
    'ContextualTypes',
    'LoggingUtils',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_qml_j_s__aot_stats_entry import AotStatsEntry
  from .._q_qml_j_s__file_selected_type import FileSelectedType
  from .._q_qml_j_s__file_selector_info import FileSelectorInfo
  from .._q_qml_j_s__export import Export
  from .._q_qml_j_s__import import Import
  from .._q_qml_j_s__logger_category import LoggerCategory
  from .._q_qml_j_s__logger_category_private import LoggerCategoryPrivate
  from .._q_qml_j_s__q_qml_j_s_aot_compiler_stats import QQmlJSAotCompilerStats
  from .._q_qml_j_s__aot_stats import AotStats
  from .._q_qml_j_s__aot_stats_reporter import AotStatsReporter
  from .._q_qml_j_s__contextual_type import ContextualType
  from .._q_qml_j_s__contextual_types import ContextualTypes
  from . import LoggingUtils
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AotStatsEntry': '_q_qml_j_s__aot_stats_entry',
      'FileSelectedType': '_q_qml_j_s__file_selected_type',
      'FileSelectorInfo': '_q_qml_j_s__file_selector_info',
      'Export': '_q_qml_j_s__export',
      'Import': '_q_qml_j_s__import',
      'LoggerCategory': '_q_qml_j_s__logger_category',
      'LoggerCategoryPrivate': '_q_qml_j_s__logger_category_private',
      'QQmlJSAotCompilerStats': '_q_qml_j_s__q_qml_j_s_aot_compiler_stats',
      'AotStats': '_q_qml_j_s__aot_stats',
      'AotStatsReporter': '_q_qml_j_s__aot_stats_reporter',
      'ContextualType': '_q_qml_j_s__contextual_type',
      'ContextualTypes': '_q_qml_j_s__contextual_types',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('LoggingUtils',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QQmlJS.AotStatsEntry'. Python calls this for a name the
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
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
