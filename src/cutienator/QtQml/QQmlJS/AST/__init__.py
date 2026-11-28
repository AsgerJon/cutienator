"""
The namespace 'QQmlJS::AST' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QQmlJS
  QQmlJS.AST.BaseVisitor

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from ..._q_qml_j_s__a_s_t import AST as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'BaseVisitor',
    'JSVisitor',
    'Node',
    'Visitor',
    'ArgumentList',
    'CaseBlock',
    'CaseClause',
    'CaseClauses',
    'Catch',
    'ClassElementList',
    'DefaultClause',
    'ESModule',
    'Elision',
    'ExportClause',
    'ExportsList',
    'ExpressionNode',
    'Finally',
    'ImportsList',
    'NamedImports',
    'PatternElementList',
    'PatternPropertyList',
    'Program',
    'PropertyName',
    'Statement',
    'StatementList',
    'TypeAnnotation',
    'UiAnnotation',
    'UiAnnotationList',
    'UiArrayMemberList',
    'UiHeaderItemList',
    'UiObjectInitializer',
    'UiObjectMember',
    'UiObjectMemberList',
    'UiProgram',
    'UiPropertyAttributes',
    'UiVersionSpecifier',
    'VariableDeclarationList',
    'BinaryExpression',
    'Block',
    'BoundNames',
    'BreakStatement',
    'ClassExpression',
    'CommaExpression',
    'ComputedPropertyName',
    'ConditionalExpression',
    'ContinueStatement',
    'DebuggerStatement',
    'DeleteExpression',
    'DoWhileStatement',
    'EmptyStatement',
    'ExportDeclaration',
    'ExportSpecifier',
    'ExpressionStatement',
    'ForEachStatement',
    'ForStatement',
    'FormalParameterList',
    'FromClause',
    'FunctionExpression',
    'IdentifierPropertyName',
    'IfStatement',
    'ImportClause',
    'ImportDeclaration',
    'ImportSpecifier',
    'InitializerExpression',
    'LabelledStatement',
    'LeftHandSideExpression',
    'NameSpaceImport',
    'NotExpression',
    'NumericLiteralPropertyName',
    'PatternElement',
    'PostDecrementExpression',
    'PostIncrementExpression',
    'PreDecrementExpression',
    'PreIncrementExpression',
    'ReturnStatement',
    'StringLiteralPropertyName',
    'SwitchStatement',
    'ThrowStatement',
    'TildeExpression',
    'TryStatement',
    'Type',
    'TypeExpression',
    'TypeOfExpression',
    'UiArrayBinding',
    'UiEnumDeclaration',
    'UiEnumMemberList',
    'UiImport',
    'UiInlineComponent',
    'UiObjectBinding',
    'UiObjectDefinition',
    'UiParameterList',
    'UiPragma',
    'UiPragmaValueList',
    'UiPublicMember',
    'UiQualifiedId',
    'UiRequired',
    'UiScriptBinding',
    'UiSourceElement',
    'UnaryMinusExpression',
    'UnaryPlusExpression',
    'VariableStatement',
    'VoidExpression',
    'WhileStatement',
    'WithStatement',
    'YieldExpression',
    'ArrayMemberExpression',
    'BoundName',
    'CallExpression',
    'ClassDeclaration',
    'FalseLiteral',
    'FieldMemberExpression',
    'FunctionDeclaration',
    'IdentifierExpression',
    'NestedExpression',
    'NewExpression',
    'NewMemberExpression',
    'NullExpression',
    'NumericLiteral',
    'Pattern',
    'PatternProperty',
    'RegExpLiteral',
    'StringLiteral',
    'SuperLiteral',
    'TaggedTemplate',
    'TemplateLiteral',
    'ThisExpression',
    'TrueLiteral',
    'ArrayPattern',
    'ObjectPattern',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._q_qml_j_s__a_s_t__base_visitor import BaseVisitor
  from ..._q_qml_j_s__a_s_t__j_s_visitor import JSVisitor
  from ..._q_qml_j_s__a_s_t__node import Node
  from ..._q_qml_j_s__a_s_t__visitor import Visitor
  from ..._q_qml_j_s__a_s_t__argument_list import ArgumentList
  from ..._q_qml_j_s__a_s_t__case_block import CaseBlock
  from ..._q_qml_j_s__a_s_t__case_clause import CaseClause
  from ..._q_qml_j_s__a_s_t__case_clauses import CaseClauses
  from ..._q_qml_j_s__a_s_t__catch import Catch
  from ..._q_qml_j_s__a_s_t__class_element_list import ClassElementList
  from ..._q_qml_j_s__a_s_t__default_clause import DefaultClause
  from ..._q_qml_j_s__a_s_t__e_s_module import ESModule
  from ..._q_qml_j_s__a_s_t__elision import Elision
  from ..._q_qml_j_s__a_s_t__export_clause import ExportClause
  from ..._q_qml_j_s__a_s_t__exports_list import ExportsList
  from ..._q_qml_j_s__a_s_t__expression_node import ExpressionNode
  from ..._q_qml_j_s__a_s_t__finally import Finally
  from ..._q_qml_j_s__a_s_t__imports_list import ImportsList
  from ..._q_qml_j_s__a_s_t__named_imports import NamedImports
  from ..._q_qml_j_s__a_s_t__pattern_element_list import PatternElementList
  from ..._q_qml_j_s__a_s_t__pattern_property_list import PatternPropertyList
  from ..._q_qml_j_s__a_s_t__program import Program
  from ..._q_qml_j_s__a_s_t__property_name import PropertyName
  from ..._q_qml_j_s__a_s_t__statement import Statement
  from ..._q_qml_j_s__a_s_t__statement_list import StatementList
  from ..._q_qml_j_s__a_s_t__type_annotation import TypeAnnotation
  from ..._q_qml_j_s__a_s_t__ui_annotation import UiAnnotation
  from ..._q_qml_j_s__a_s_t__ui_annotation_list import UiAnnotationList
  from ..._q_qml_j_s__a_s_t__ui_array_member_list import UiArrayMemberList
  from ..._q_qml_j_s__a_s_t__ui_header_item_list import UiHeaderItemList
  from ..._q_qml_j_s__a_s_t__ui_object_initializer import UiObjectInitializer
  from ..._q_qml_j_s__a_s_t__ui_object_member import UiObjectMember
  from ..._q_qml_j_s__a_s_t__ui_object_member_list import UiObjectMemberList
  from ..._q_qml_j_s__a_s_t__ui_program import UiProgram
  from ..._q_qml_j_s__a_s_t__ui_property_attributes import UiPropertyAttributes
  from ..._q_qml_j_s__a_s_t__ui_version_specifier import UiVersionSpecifier
  from ..._q_qml_j_s__a_s_t__variable_declaration_list import VariableDeclarationList
  from ..._q_qml_j_s__a_s_t__binary_expression import BinaryExpression
  from ..._q_qml_j_s__a_s_t__block import Block
  from ..._q_qml_j_s__a_s_t__bound_names import BoundNames
  from ..._q_qml_j_s__a_s_t__break_statement import BreakStatement
  from ..._q_qml_j_s__a_s_t__class_expression import ClassExpression
  from ..._q_qml_j_s__a_s_t__comma_expression import CommaExpression
  from ..._q_qml_j_s__a_s_t__computed_property_name import ComputedPropertyName
  from ..._q_qml_j_s__a_s_t__conditional_expression import ConditionalExpression
  from ..._q_qml_j_s__a_s_t__continue_statement import ContinueStatement
  from ..._q_qml_j_s__a_s_t__debugger_statement import DebuggerStatement
  from ..._q_qml_j_s__a_s_t__delete_expression import DeleteExpression
  from ..._q_qml_j_s__a_s_t__do_while_statement import DoWhileStatement
  from ..._q_qml_j_s__a_s_t__empty_statement import EmptyStatement
  from ..._q_qml_j_s__a_s_t__export_declaration import ExportDeclaration
  from ..._q_qml_j_s__a_s_t__export_specifier import ExportSpecifier
  from ..._q_qml_j_s__a_s_t__expression_statement import ExpressionStatement
  from ..._q_qml_j_s__a_s_t__for_each_statement import ForEachStatement
  from ..._q_qml_j_s__a_s_t__for_statement import ForStatement
  from ..._q_qml_j_s__a_s_t__formal_parameter_list import FormalParameterList
  from ..._q_qml_j_s__a_s_t__from_clause import FromClause
  from ..._q_qml_j_s__a_s_t__function_expression import FunctionExpression
  from ..._q_qml_j_s__a_s_t__identifier_property_name import IdentifierPropertyName
  from ..._q_qml_j_s__a_s_t__if_statement import IfStatement
  from ..._q_qml_j_s__a_s_t__import_clause import ImportClause
  from ..._q_qml_j_s__a_s_t__import_declaration import ImportDeclaration
  from ..._q_qml_j_s__a_s_t__import_specifier import ImportSpecifier
  from ..._q_qml_j_s__a_s_t__initializer_expression import InitializerExpression
  from ..._q_qml_j_s__a_s_t__labelled_statement import LabelledStatement
  from ..._q_qml_j_s__a_s_t__left_hand_side_expression import LeftHandSideExpression
  from ..._q_qml_j_s__a_s_t__name_space_import import NameSpaceImport
  from ..._q_qml_j_s__a_s_t__not_expression import NotExpression
  from ..._q_qml_j_s__a_s_t__numeric_literal_property_name import NumericLiteralPropertyName
  from ..._q_qml_j_s__a_s_t__pattern_element import PatternElement
  from ..._q_qml_j_s__a_s_t__post_decrement_expression import PostDecrementExpression
  from ..._q_qml_j_s__a_s_t__post_increment_expression import PostIncrementExpression
  from ..._q_qml_j_s__a_s_t__pre_decrement_expression import PreDecrementExpression
  from ..._q_qml_j_s__a_s_t__pre_increment_expression import PreIncrementExpression
  from ..._q_qml_j_s__a_s_t__return_statement import ReturnStatement
  from ..._q_qml_j_s__a_s_t__string_literal_property_name import StringLiteralPropertyName
  from ..._q_qml_j_s__a_s_t__switch_statement import SwitchStatement
  from ..._q_qml_j_s__a_s_t__throw_statement import ThrowStatement
  from ..._q_qml_j_s__a_s_t__tilde_expression import TildeExpression
  from ..._q_qml_j_s__a_s_t__try_statement import TryStatement
  from ..._q_qml_j_s__a_s_t__type import Type
  from ..._q_qml_j_s__a_s_t__type_expression import TypeExpression
  from ..._q_qml_j_s__a_s_t__type_of_expression import TypeOfExpression
  from ..._q_qml_j_s__a_s_t__ui_array_binding import UiArrayBinding
  from ..._q_qml_j_s__a_s_t__ui_enum_declaration import UiEnumDeclaration
  from ..._q_qml_j_s__a_s_t__ui_enum_member_list import UiEnumMemberList
  from ..._q_qml_j_s__a_s_t__ui_import import UiImport
  from ..._q_qml_j_s__a_s_t__ui_inline_component import UiInlineComponent
  from ..._q_qml_j_s__a_s_t__ui_object_binding import UiObjectBinding
  from ..._q_qml_j_s__a_s_t__ui_object_definition import UiObjectDefinition
  from ..._q_qml_j_s__a_s_t__ui_parameter_list import UiParameterList
  from ..._q_qml_j_s__a_s_t__ui_pragma import UiPragma
  from ..._q_qml_j_s__a_s_t__ui_pragma_value_list import UiPragmaValueList
  from ..._q_qml_j_s__a_s_t__ui_public_member import UiPublicMember
  from ..._q_qml_j_s__a_s_t__ui_qualified_id import UiQualifiedId
  from ..._q_qml_j_s__a_s_t__ui_required import UiRequired
  from ..._q_qml_j_s__a_s_t__ui_script_binding import UiScriptBinding
  from ..._q_qml_j_s__a_s_t__ui_source_element import UiSourceElement
  from ..._q_qml_j_s__a_s_t__unary_minus_expression import UnaryMinusExpression
  from ..._q_qml_j_s__a_s_t__unary_plus_expression import UnaryPlusExpression
  from ..._q_qml_j_s__a_s_t__variable_statement import VariableStatement
  from ..._q_qml_j_s__a_s_t__void_expression import VoidExpression
  from ..._q_qml_j_s__a_s_t__while_statement import WhileStatement
  from ..._q_qml_j_s__a_s_t__with_statement import WithStatement
  from ..._q_qml_j_s__a_s_t__yield_expression import YieldExpression
  from ..._q_qml_j_s__a_s_t__array_member_expression import ArrayMemberExpression
  from ..._q_qml_j_s__a_s_t__bound_name import BoundName
  from ..._q_qml_j_s__a_s_t__call_expression import CallExpression
  from ..._q_qml_j_s__a_s_t__class_declaration import ClassDeclaration
  from ..._q_qml_j_s__a_s_t__false_literal import FalseLiteral
  from ..._q_qml_j_s__a_s_t__field_member_expression import FieldMemberExpression
  from ..._q_qml_j_s__a_s_t__function_declaration import FunctionDeclaration
  from ..._q_qml_j_s__a_s_t__identifier_expression import IdentifierExpression
  from ..._q_qml_j_s__a_s_t__nested_expression import NestedExpression
  from ..._q_qml_j_s__a_s_t__new_expression import NewExpression
  from ..._q_qml_j_s__a_s_t__new_member_expression import NewMemberExpression
  from ..._q_qml_j_s__a_s_t__null_expression import NullExpression
  from ..._q_qml_j_s__a_s_t__numeric_literal import NumericLiteral
  from ..._q_qml_j_s__a_s_t__pattern import Pattern
  from ..._q_qml_j_s__a_s_t__pattern_property import PatternProperty
  from ..._q_qml_j_s__a_s_t__reg_exp_literal import RegExpLiteral
  from ..._q_qml_j_s__a_s_t__string_literal import StringLiteral
  from ..._q_qml_j_s__a_s_t__super_literal import SuperLiteral
  from ..._q_qml_j_s__a_s_t__tagged_template import TaggedTemplate
  from ..._q_qml_j_s__a_s_t__template_literal import TemplateLiteral
  from ..._q_qml_j_s__a_s_t__this_expression import ThisExpression
  from ..._q_qml_j_s__a_s_t__true_literal import TrueLiteral
  from ..._q_qml_j_s__a_s_t__array_pattern import ArrayPattern
  from ..._q_qml_j_s__a_s_t__object_pattern import ObjectPattern
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'BaseVisitor': '_q_qml_j_s__a_s_t__base_visitor',
      'JSVisitor': '_q_qml_j_s__a_s_t__j_s_visitor',
      'Node': '_q_qml_j_s__a_s_t__node',
      'Visitor': '_q_qml_j_s__a_s_t__visitor',
      'ArgumentList': '_q_qml_j_s__a_s_t__argument_list',
      'CaseBlock': '_q_qml_j_s__a_s_t__case_block',
      'CaseClause': '_q_qml_j_s__a_s_t__case_clause',
      'CaseClauses': '_q_qml_j_s__a_s_t__case_clauses',
      'Catch': '_q_qml_j_s__a_s_t__catch',
      'ClassElementList': '_q_qml_j_s__a_s_t__class_element_list',
      'DefaultClause': '_q_qml_j_s__a_s_t__default_clause',
      'ESModule': '_q_qml_j_s__a_s_t__e_s_module',
      'Elision': '_q_qml_j_s__a_s_t__elision',
      'ExportClause': '_q_qml_j_s__a_s_t__export_clause',
      'ExportsList': '_q_qml_j_s__a_s_t__exports_list',
      'ExpressionNode': '_q_qml_j_s__a_s_t__expression_node',
      'Finally': '_q_qml_j_s__a_s_t__finally',
      'ImportsList': '_q_qml_j_s__a_s_t__imports_list',
      'NamedImports': '_q_qml_j_s__a_s_t__named_imports',
      'PatternElementList': '_q_qml_j_s__a_s_t__pattern_element_list',
      'PatternPropertyList': '_q_qml_j_s__a_s_t__pattern_property_list',
      'Program': '_q_qml_j_s__a_s_t__program',
      'PropertyName': '_q_qml_j_s__a_s_t__property_name',
      'Statement': '_q_qml_j_s__a_s_t__statement',
      'StatementList': '_q_qml_j_s__a_s_t__statement_list',
      'TypeAnnotation': '_q_qml_j_s__a_s_t__type_annotation',
      'UiAnnotation': '_q_qml_j_s__a_s_t__ui_annotation',
      'UiAnnotationList': '_q_qml_j_s__a_s_t__ui_annotation_list',
      'UiArrayMemberList': '_q_qml_j_s__a_s_t__ui_array_member_list',
      'UiHeaderItemList': '_q_qml_j_s__a_s_t__ui_header_item_list',
      'UiObjectInitializer': '_q_qml_j_s__a_s_t__ui_object_initializer',
      'UiObjectMember': '_q_qml_j_s__a_s_t__ui_object_member',
      'UiObjectMemberList': '_q_qml_j_s__a_s_t__ui_object_member_list',
      'UiProgram': '_q_qml_j_s__a_s_t__ui_program',
      'UiPropertyAttributes': '_q_qml_j_s__a_s_t__ui_property_attributes',
      'UiVersionSpecifier': '_q_qml_j_s__a_s_t__ui_version_specifier',
      'VariableDeclarationList': '_q_qml_j_s__a_s_t__variable_declaration_list',
      'BinaryExpression': '_q_qml_j_s__a_s_t__binary_expression',
      'Block': '_q_qml_j_s__a_s_t__block',
      'BoundNames': '_q_qml_j_s__a_s_t__bound_names',
      'BreakStatement': '_q_qml_j_s__a_s_t__break_statement',
      'ClassExpression': '_q_qml_j_s__a_s_t__class_expression',
      'CommaExpression': '_q_qml_j_s__a_s_t__comma_expression',
      'ComputedPropertyName': '_q_qml_j_s__a_s_t__computed_property_name',
      'ConditionalExpression': '_q_qml_j_s__a_s_t__conditional_expression',
      'ContinueStatement': '_q_qml_j_s__a_s_t__continue_statement',
      'DebuggerStatement': '_q_qml_j_s__a_s_t__debugger_statement',
      'DeleteExpression': '_q_qml_j_s__a_s_t__delete_expression',
      'DoWhileStatement': '_q_qml_j_s__a_s_t__do_while_statement',
      'EmptyStatement': '_q_qml_j_s__a_s_t__empty_statement',
      'ExportDeclaration': '_q_qml_j_s__a_s_t__export_declaration',
      'ExportSpecifier': '_q_qml_j_s__a_s_t__export_specifier',
      'ExpressionStatement': '_q_qml_j_s__a_s_t__expression_statement',
      'ForEachStatement': '_q_qml_j_s__a_s_t__for_each_statement',
      'ForStatement': '_q_qml_j_s__a_s_t__for_statement',
      'FormalParameterList': '_q_qml_j_s__a_s_t__formal_parameter_list',
      'FromClause': '_q_qml_j_s__a_s_t__from_clause',
      'FunctionExpression': '_q_qml_j_s__a_s_t__function_expression',
      'IdentifierPropertyName': '_q_qml_j_s__a_s_t__identifier_property_name',
      'IfStatement': '_q_qml_j_s__a_s_t__if_statement',
      'ImportClause': '_q_qml_j_s__a_s_t__import_clause',
      'ImportDeclaration': '_q_qml_j_s__a_s_t__import_declaration',
      'ImportSpecifier': '_q_qml_j_s__a_s_t__import_specifier',
      'InitializerExpression': '_q_qml_j_s__a_s_t__initializer_expression',
      'LabelledStatement': '_q_qml_j_s__a_s_t__labelled_statement',
      'LeftHandSideExpression': '_q_qml_j_s__a_s_t__left_hand_side_expression',
      'NameSpaceImport': '_q_qml_j_s__a_s_t__name_space_import',
      'NotExpression': '_q_qml_j_s__a_s_t__not_expression',
      'NumericLiteralPropertyName': '_q_qml_j_s__a_s_t__numeric_literal_property_name',
      'PatternElement': '_q_qml_j_s__a_s_t__pattern_element',
      'PostDecrementExpression': '_q_qml_j_s__a_s_t__post_decrement_expression',
      'PostIncrementExpression': '_q_qml_j_s__a_s_t__post_increment_expression',
      'PreDecrementExpression': '_q_qml_j_s__a_s_t__pre_decrement_expression',
      'PreIncrementExpression': '_q_qml_j_s__a_s_t__pre_increment_expression',
      'ReturnStatement': '_q_qml_j_s__a_s_t__return_statement',
      'StringLiteralPropertyName': '_q_qml_j_s__a_s_t__string_literal_property_name',
      'SwitchStatement': '_q_qml_j_s__a_s_t__switch_statement',
      'ThrowStatement': '_q_qml_j_s__a_s_t__throw_statement',
      'TildeExpression': '_q_qml_j_s__a_s_t__tilde_expression',
      'TryStatement': '_q_qml_j_s__a_s_t__try_statement',
      'Type': '_q_qml_j_s__a_s_t__type',
      'TypeExpression': '_q_qml_j_s__a_s_t__type_expression',
      'TypeOfExpression': '_q_qml_j_s__a_s_t__type_of_expression',
      'UiArrayBinding': '_q_qml_j_s__a_s_t__ui_array_binding',
      'UiEnumDeclaration': '_q_qml_j_s__a_s_t__ui_enum_declaration',
      'UiEnumMemberList': '_q_qml_j_s__a_s_t__ui_enum_member_list',
      'UiImport': '_q_qml_j_s__a_s_t__ui_import',
      'UiInlineComponent': '_q_qml_j_s__a_s_t__ui_inline_component',
      'UiObjectBinding': '_q_qml_j_s__a_s_t__ui_object_binding',
      'UiObjectDefinition': '_q_qml_j_s__a_s_t__ui_object_definition',
      'UiParameterList': '_q_qml_j_s__a_s_t__ui_parameter_list',
      'UiPragma': '_q_qml_j_s__a_s_t__ui_pragma',
      'UiPragmaValueList': '_q_qml_j_s__a_s_t__ui_pragma_value_list',
      'UiPublicMember': '_q_qml_j_s__a_s_t__ui_public_member',
      'UiQualifiedId': '_q_qml_j_s__a_s_t__ui_qualified_id',
      'UiRequired': '_q_qml_j_s__a_s_t__ui_required',
      'UiScriptBinding': '_q_qml_j_s__a_s_t__ui_script_binding',
      'UiSourceElement': '_q_qml_j_s__a_s_t__ui_source_element',
      'UnaryMinusExpression': '_q_qml_j_s__a_s_t__unary_minus_expression',
      'UnaryPlusExpression': '_q_qml_j_s__a_s_t__unary_plus_expression',
      'VariableStatement': '_q_qml_j_s__a_s_t__variable_statement',
      'VoidExpression': '_q_qml_j_s__a_s_t__void_expression',
      'WhileStatement': '_q_qml_j_s__a_s_t__while_statement',
      'WithStatement': '_q_qml_j_s__a_s_t__with_statement',
      'YieldExpression': '_q_qml_j_s__a_s_t__yield_expression',
      'ArrayMemberExpression': '_q_qml_j_s__a_s_t__array_member_expression',
      'BoundName': '_q_qml_j_s__a_s_t__bound_name',
      'CallExpression': '_q_qml_j_s__a_s_t__call_expression',
      'ClassDeclaration': '_q_qml_j_s__a_s_t__class_declaration',
      'FalseLiteral': '_q_qml_j_s__a_s_t__false_literal',
      'FieldMemberExpression': '_q_qml_j_s__a_s_t__field_member_expression',
      'FunctionDeclaration': '_q_qml_j_s__a_s_t__function_declaration',
      'IdentifierExpression': '_q_qml_j_s__a_s_t__identifier_expression',
      'NestedExpression': '_q_qml_j_s__a_s_t__nested_expression',
      'NewExpression': '_q_qml_j_s__a_s_t__new_expression',
      'NewMemberExpression': '_q_qml_j_s__a_s_t__new_member_expression',
      'NullExpression': '_q_qml_j_s__a_s_t__null_expression',
      'NumericLiteral': '_q_qml_j_s__a_s_t__numeric_literal',
      'Pattern': '_q_qml_j_s__a_s_t__pattern',
      'PatternProperty': '_q_qml_j_s__a_s_t__pattern_property',
      'RegExpLiteral': '_q_qml_j_s__a_s_t__reg_exp_literal',
      'StringLiteral': '_q_qml_j_s__a_s_t__string_literal',
      'SuperLiteral': '_q_qml_j_s__a_s_t__super_literal',
      'TaggedTemplate': '_q_qml_j_s__a_s_t__tagged_template',
      'TemplateLiteral': '_q_qml_j_s__a_s_t__template_literal',
      'ThisExpression': '_q_qml_j_s__a_s_t__this_expression',
      'TrueLiteral': '_q_qml_j_s__a_s_t__true_literal',
      'ArrayPattern': '_q_qml_j_s__a_s_t__array_pattern',
      'ObjectPattern': '_q_qml_j_s__a_s_t__object_pattern',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QQmlJS.AST.BaseVisitor'. Python calls this for a name
    the package does not hold yet, and what it gives is kept here for the
    next time.

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
