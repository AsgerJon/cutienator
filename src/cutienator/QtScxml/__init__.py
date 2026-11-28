"""
The 'cutienator.QtScxml' package provides the cute classes of the part
of Qt named QtScxml, under the name PySide6 has for it.

  from cutienator.QtScxml import QScxmlTableData, QScxmlDataModelPlugin

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
    'QScxmlTableData',
    'QScxmlDataModelPlugin',
    'QScxmlError',
    'QScxmlEvent',
    'QScxmlInvokableServiceFactoryPrivate',
    'QScxmlCompiler',
    'QScxmlStateMachine',
    'QScxmlDataModelPrivate',
    'QScxmlDataModel',
    'QScxmlInvokableServiceFactory',
    'QScxmlStateMachineInfo',
    'QScxmlInvokableService',
    'QScxmlStateMachinePrivate',
    'QScxmlEventPrivate',
    'QScxmlStaticScxmlServiceFactoryPrivate',
    'QScxmlCompilerPrivate',
    'QScxmlCppDataModel',
    'QScxmlCppDataModelPrivate',
    'QScxmlDynamicScxmlServiceFactory',
    'QScxmlEventBuilder',
    'QScxmlExecutionEngine',
    'QScxmlInvokableServicePrivate',
    'QScxmlNullDataModel',
    'QScxmlScxmlService',
    'QScxmlStaticScxmlServiceFactory',
    'DocumentModel',
    'QScxmlExecutableContent',
    'QScxmlInternal',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_scxml_table_data import QScxmlTableData
  from ._q_scxml_data_model_plugin import QScxmlDataModelPlugin
  from ._q_scxml_error import QScxmlError
  from ._q_scxml_event import QScxmlEvent
  from ._q_scxml_invokable_service_factory_private import QScxmlInvokableServiceFactoryPrivate
  from ._q_scxml_compiler import QScxmlCompiler
  from ._q_scxml_state_machine import QScxmlStateMachine
  from ._q_scxml_data_model_private import QScxmlDataModelPrivate
  from ._q_scxml_data_model import QScxmlDataModel
  from ._q_scxml_invokable_service_factory import QScxmlInvokableServiceFactory
  from ._q_scxml_state_machine_info import QScxmlStateMachineInfo
  from ._q_scxml_invokable_service import QScxmlInvokableService
  from ._q_scxml_state_machine_private import QScxmlStateMachinePrivate
  from ._q_scxml_event_private import QScxmlEventPrivate
  from ._q_scxml_static_scxml_service_factory_private import QScxmlStaticScxmlServiceFactoryPrivate
  from ._q_scxml_compiler_private import QScxmlCompilerPrivate
  from ._q_scxml_cpp_data_model import QScxmlCppDataModel
  from ._q_scxml_cpp_data_model_private import QScxmlCppDataModelPrivate
  from ._q_scxml_dynamic_scxml_service_factory import QScxmlDynamicScxmlServiceFactory
  from ._q_scxml_event_builder import QScxmlEventBuilder
  from ._q_scxml_execution_engine import QScxmlExecutionEngine
  from ._q_scxml_invokable_service_private import QScxmlInvokableServicePrivate
  from ._q_scxml_null_data_model import QScxmlNullDataModel
  from ._q_scxml_scxml_service import QScxmlScxmlService
  from ._q_scxml_static_scxml_service_factory import QScxmlStaticScxmlServiceFactory
  from . import DocumentModel
  from . import QScxmlExecutableContent
  from . import QScxmlInternal
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QScxmlTableData': '_q_scxml_table_data',
      'QScxmlDataModelPlugin': '_q_scxml_data_model_plugin',
      'QScxmlError': '_q_scxml_error',
      'QScxmlEvent': '_q_scxml_event',
      'QScxmlInvokableServiceFactoryPrivate': '_q_scxml_invokable_service_factory_private',
      'QScxmlCompiler': '_q_scxml_compiler',
      'QScxmlStateMachine': '_q_scxml_state_machine',
      'QScxmlDataModelPrivate': '_q_scxml_data_model_private',
      'QScxmlDataModel': '_q_scxml_data_model',
      'QScxmlInvokableServiceFactory': '_q_scxml_invokable_service_factory',
      'QScxmlStateMachineInfo': '_q_scxml_state_machine_info',
      'QScxmlInvokableService': '_q_scxml_invokable_service',
      'QScxmlStateMachinePrivate': '_q_scxml_state_machine_private',
      'QScxmlEventPrivate': '_q_scxml_event_private',
      'QScxmlStaticScxmlServiceFactoryPrivate': '_q_scxml_static_scxml_service_factory_private',
      'QScxmlCompilerPrivate': '_q_scxml_compiler_private',
      'QScxmlCppDataModel': '_q_scxml_cpp_data_model',
      'QScxmlCppDataModelPrivate': '_q_scxml_cpp_data_model_private',
      'QScxmlDynamicScxmlServiceFactory': '_q_scxml_dynamic_scxml_service_factory',
      'QScxmlEventBuilder': '_q_scxml_event_builder',
      'QScxmlExecutionEngine': '_q_scxml_execution_engine',
      'QScxmlInvokableServicePrivate': '_q_scxml_invokable_service_private',
      'QScxmlNullDataModel': '_q_scxml_null_data_model',
      'QScxmlScxmlService': '_q_scxml_scxml_service',
      'QScxmlStaticScxmlServiceFactory': '_q_scxml_static_scxml_service_factory',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('DocumentModel', 'QScxmlExecutableContent', 'QScxmlInternal',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtScxml import QScxmlStaticScxmlServiceFactory'. Python calls
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
