"""
The namespace 'QQmlSA' of Qt, a package of 'cutienator.QtQmlCompiler':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQmlCompiler import QQmlSA
  QQmlSA.Binding

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._q_qml_s_a import QQmlSA as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'Binding',
    'LintPlugin',
    'Method',
    'Property',
    'PropertyPassInvocation',
    'DocumentEdit',
    'DocumentEditPrivate',
    'Element',
    'LoggerWarningId',
    'PassManager',
    'PropertyPassBuilder',
    'SourceLocation',
    'FixSuggestion',
    'SourceLocationPrivate',
    'FixSuggestionPrivate',
    'GenericPass',
    'ElementPass',
    'PropertyPass',
    'GenericPropertyPass',
    'BindingPrivate',
    'BindingsPrivate',
    'MethodPrivate',
    'MethodsPrivate',
    'PassManagerPrivate',
    'PropertyPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_qml_s_a__binding import Binding
  from .._q_qml_s_a__lint_plugin import LintPlugin
  from .._q_qml_s_a__method import Method
  from .._q_qml_s_a__property import Property
  from .._q_qml_s_a__property_pass_invocation import PropertyPassInvocation
  from .._q_qml_s_a__document_edit import DocumentEdit
  from .._q_qml_s_a__document_edit_private import DocumentEditPrivate
  from .._q_qml_s_a__element import Element
  from .._q_qml_s_a__logger_warning_id import LoggerWarningId
  from .._q_qml_s_a__pass_manager import PassManager
  from .._q_qml_s_a__property_pass_builder import PropertyPassBuilder
  from .._q_qml_s_a__source_location import SourceLocation
  from .._q_qml_s_a__fix_suggestion import FixSuggestion
  from .._q_qml_s_a__source_location_private import SourceLocationPrivate
  from .._q_qml_s_a__fix_suggestion_private import FixSuggestionPrivate
  from .._q_qml_s_a__generic_pass import GenericPass
  from .._q_qml_s_a__element_pass import ElementPass
  from .._q_qml_s_a__property_pass import PropertyPass
  from .._q_qml_s_a__generic_property_pass import GenericPropertyPass
  from .._q_qml_s_a__binding_private import BindingPrivate
  from .._q_qml_s_a__bindings_private import BindingsPrivate
  from .._q_qml_s_a__method_private import MethodPrivate
  from .._q_qml_s_a__methods_private import MethodsPrivate
  from .._q_qml_s_a__pass_manager_private import PassManagerPrivate
  from .._q_qml_s_a__property_private import PropertyPrivate
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Binding': '_q_qml_s_a__binding',
      'LintPlugin': '_q_qml_s_a__lint_plugin',
      'Method': '_q_qml_s_a__method',
      'Property': '_q_qml_s_a__property',
      'PropertyPassInvocation': '_q_qml_s_a__property_pass_invocation',
      'DocumentEdit': '_q_qml_s_a__document_edit',
      'DocumentEditPrivate': '_q_qml_s_a__document_edit_private',
      'Element': '_q_qml_s_a__element',
      'LoggerWarningId': '_q_qml_s_a__logger_warning_id',
      'PassManager': '_q_qml_s_a__pass_manager',
      'PropertyPassBuilder': '_q_qml_s_a__property_pass_builder',
      'SourceLocation': '_q_qml_s_a__source_location',
      'FixSuggestion': '_q_qml_s_a__fix_suggestion',
      'SourceLocationPrivate': '_q_qml_s_a__source_location_private',
      'FixSuggestionPrivate': '_q_qml_s_a__fix_suggestion_private',
      'GenericPass': '_q_qml_s_a__generic_pass',
      'ElementPass': '_q_qml_s_a__element_pass',
      'PropertyPass': '_q_qml_s_a__property_pass',
      'GenericPropertyPass': '_q_qml_s_a__generic_property_pass',
      'BindingPrivate': '_q_qml_s_a__binding_private',
      'BindingsPrivate': '_q_qml_s_a__bindings_private',
      'MethodPrivate': '_q_qml_s_a__method_private',
      'MethodsPrivate': '_q_qml_s_a__methods_private',
      'PassManagerPrivate': '_q_qml_s_a__pass_manager_private',
      'PropertyPrivate': '_q_qml_s_a__property_private',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QQmlSA.Binding'. Python calls this for a name the
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
