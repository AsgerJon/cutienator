"""
The 'cutienator.QtQmlCompiler' package provides the cute classes of the
part of Qt named QtQmlCompiler, under the name PySide6 has for it.

  from cutienator.QtQmlCompiler import QQQmlJSDeprecation, QQmlJSAnnotation

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
    'QQQmlJSDeprecation',
    'QQmlJSAnnotation',
    'QQmlJSAotFunction',
    'QQmlJSDocumentEdit',
    'QQmlJSMetaSignalHandler',
    'QQmlJSTypeResolverDependencies',
    'Message',
    'QColorOutput',
    'QQmlJSCompileError',
    'IssueLocationWithContext',
    'QQmlJSFixSuggestion',
    'QQmlJSAOTIRBuilder',
    'QQmlJSLogger',
    'QQmlJSResourceFileMapper',
    'QQmlJSScope',
    'QQmlJSImporter',
    'QQmlJSMetaMethod',
    'QQmlJSMetaProperty',
    'QQmlJSRegisterContent',
    'QQmlJSImportVisitor',
    'QQmlJSTypeResolver',
    'QQmlJSMetaEnum',
    'QQmlJSMetaParameter',
    'QQmlJSMetaPropertyBinding',
    'QQmlJSAotCompiler',
    'QQmlJSCompilePass',
    'QQmlJSFunctionInitializer',
    'QQmlJSLookupSignaturesRecorder',
    'QQmlJSRegisterContentPool',
    'QQmlJSScopesById',
    'QQmlJSTypeDescriptionReader',
    'QQmlJSBasicBlocks',
    'QQmlJSCodeGenerator',
    'QQmlJSOptimizations',
    'QQmlJSShadowCheck',
    'QQmlJSStorageGeneralizer',
    'QQmlJSStorageInitializer',
    'QQmlJSTypePropagator',
    'QQmlJSUtils',
    'QQmlJS',
    'QQmlSA',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_q_qml_j_s_deprecation import QQQmlJSDeprecation
  from ._q_qml_j_s_annotation import QQmlJSAnnotation
  from ._q_qml_j_s_aot_function import QQmlJSAotFunction
  from ._q_qml_j_s_document_edit import QQmlJSDocumentEdit
  from ._q_qml_j_s_meta_signal_handler import QQmlJSMetaSignalHandler
  from ._q_qml_j_s_type_resolver_dependencies import QQmlJSTypeResolverDependencies
  from ._message import Message
  from ._q_color_output import QColorOutput
  from ._q_qml_j_s_compile_error import QQmlJSCompileError
  from ._issue_location_with_context import IssueLocationWithContext
  from ._q_qml_j_s_fix_suggestion import QQmlJSFixSuggestion
  from ._q_qml_j_s_a_o_t_i_r_builder import QQmlJSAOTIRBuilder
  from ._q_qml_j_s_logger import QQmlJSLogger
  from ._q_qml_j_s_resource_file_mapper import QQmlJSResourceFileMapper
  from ._q_qml_j_s_scope import QQmlJSScope
  from ._q_qml_j_s_importer import QQmlJSImporter
  from ._q_qml_j_s_meta_method import QQmlJSMetaMethod
  from ._q_qml_j_s_meta_property import QQmlJSMetaProperty
  from ._q_qml_j_s_register_content import QQmlJSRegisterContent
  from ._q_qml_j_s_import_visitor import QQmlJSImportVisitor
  from ._q_qml_j_s_type_resolver import QQmlJSTypeResolver
  from ._q_qml_j_s_meta_enum import QQmlJSMetaEnum
  from ._q_qml_j_s_meta_parameter import QQmlJSMetaParameter
  from ._q_qml_j_s_meta_property_binding import QQmlJSMetaPropertyBinding
  from ._q_qml_j_s_aot_compiler import QQmlJSAotCompiler
  from ._q_qml_j_s_compile_pass import QQmlJSCompilePass
  from ._q_qml_j_s_function_initializer import QQmlJSFunctionInitializer
  from ._q_qml_j_s_lookup_signatures_recorder import QQmlJSLookupSignaturesRecorder
  from ._q_qml_j_s_register_content_pool import QQmlJSRegisterContentPool
  from ._q_qml_j_s_scopes_by_id import QQmlJSScopesById
  from ._q_qml_j_s_type_description_reader import QQmlJSTypeDescriptionReader
  from ._q_qml_j_s_basic_blocks import QQmlJSBasicBlocks
  from ._q_qml_j_s_code_generator import QQmlJSCodeGenerator
  from ._q_qml_j_s_optimizations import QQmlJSOptimizations
  from ._q_qml_j_s_shadow_check import QQmlJSShadowCheck
  from ._q_qml_j_s_storage_generalizer import QQmlJSStorageGeneralizer
  from ._q_qml_j_s_storage_initializer import QQmlJSStorageInitializer
  from ._q_qml_j_s_type_propagator import QQmlJSTypePropagator
  from ._q_qml_j_s_utils import QQmlJSUtils
  from . import QQmlJS
  from . import QQmlSA
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQQmlJSDeprecation': '_q_q_qml_j_s_deprecation',
      'QQmlJSAnnotation': '_q_qml_j_s_annotation',
      'QQmlJSAotFunction': '_q_qml_j_s_aot_function',
      'QQmlJSDocumentEdit': '_q_qml_j_s_document_edit',
      'QQmlJSMetaSignalHandler': '_q_qml_j_s_meta_signal_handler',
      'QQmlJSTypeResolverDependencies': '_q_qml_j_s_type_resolver_dependencies',
      'Message': '_message',
      'QColorOutput': '_q_color_output',
      'QQmlJSCompileError': '_q_qml_j_s_compile_error',
      'IssueLocationWithContext': '_issue_location_with_context',
      'QQmlJSFixSuggestion': '_q_qml_j_s_fix_suggestion',
      'QQmlJSAOTIRBuilder': '_q_qml_j_s_a_o_t_i_r_builder',
      'QQmlJSLogger': '_q_qml_j_s_logger',
      'QQmlJSResourceFileMapper': '_q_qml_j_s_resource_file_mapper',
      'QQmlJSScope': '_q_qml_j_s_scope',
      'QQmlJSImporter': '_q_qml_j_s_importer',
      'QQmlJSMetaMethod': '_q_qml_j_s_meta_method',
      'QQmlJSMetaProperty': '_q_qml_j_s_meta_property',
      'QQmlJSRegisterContent': '_q_qml_j_s_register_content',
      'QQmlJSImportVisitor': '_q_qml_j_s_import_visitor',
      'QQmlJSTypeResolver': '_q_qml_j_s_type_resolver',
      'QQmlJSMetaEnum': '_q_qml_j_s_meta_enum',
      'QQmlJSMetaParameter': '_q_qml_j_s_meta_parameter',
      'QQmlJSMetaPropertyBinding': '_q_qml_j_s_meta_property_binding',
      'QQmlJSAotCompiler': '_q_qml_j_s_aot_compiler',
      'QQmlJSCompilePass': '_q_qml_j_s_compile_pass',
      'QQmlJSFunctionInitializer': '_q_qml_j_s_function_initializer',
      'QQmlJSLookupSignaturesRecorder': '_q_qml_j_s_lookup_signatures_recorder',
      'QQmlJSRegisterContentPool': '_q_qml_j_s_register_content_pool',
      'QQmlJSScopesById': '_q_qml_j_s_scopes_by_id',
      'QQmlJSTypeDescriptionReader': '_q_qml_j_s_type_description_reader',
      'QQmlJSBasicBlocks': '_q_qml_j_s_basic_blocks',
      'QQmlJSCodeGenerator': '_q_qml_j_s_code_generator',
      'QQmlJSOptimizations': '_q_qml_j_s_optimizations',
      'QQmlJSShadowCheck': '_q_qml_j_s_shadow_check',
      'QQmlJSStorageGeneralizer': '_q_qml_j_s_storage_generalizer',
      'QQmlJSStorageInitializer': '_q_qml_j_s_storage_initializer',
      'QQmlJSTypePropagator': '_q_qml_j_s_type_propagator',
      'QQmlJSUtils': '_q_qml_j_s_utils',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QQmlJS', 'QQmlSA',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQmlCompiler import QQmlJSUtils'. Python calls
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
