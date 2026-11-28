"""
The namespace 'DocumentModel' of Qt, a package of 'cutienator.QtScxml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtScxml import DocumentModel
  DocumentModel.Node

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
    'Node',
    'StateContainer',
    'XmlLocation',
    'AbstractState',
    'DataElement',
    'DoneData',
    'Instruction',
    'Param',
    'Scxml',
    'StateOrTransition',
    'Assign',
    'Cancel',
    'Foreach',
    'HistoryState',
    'If',
    'Invoke',
    'Log',
    'Raise',
    'Script',
    'Send',
    'State',
    'Transition',
    'NodeVisitor',
    'ScxmlDocument',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._document_model__node import Node
  from .._document_model__state_container import StateContainer
  from .._document_model__xml_location import XmlLocation
  from .._document_model__abstract_state import AbstractState
  from .._document_model__data_element import DataElement
  from .._document_model__done_data import DoneData
  from .._document_model__instruction import Instruction
  from .._document_model__param import Param
  from .._document_model__scxml import Scxml
  from .._document_model__state_or_transition import StateOrTransition
  from .._document_model__assign import Assign
  from .._document_model__cancel import Cancel
  from .._document_model__foreach import Foreach
  from .._document_model__history_state import HistoryState
  from .._document_model__if import If
  from .._document_model__invoke import Invoke
  from .._document_model__log import Log
  from .._document_model__raise import Raise
  from .._document_model__script import Script
  from .._document_model__send import Send
  from .._document_model__state import State
  from .._document_model__transition import Transition
  from .._document_model__node_visitor import NodeVisitor
  from .._document_model__scxml_document import ScxmlDocument
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Node': '_document_model__node',
      'StateContainer': '_document_model__state_container',
      'XmlLocation': '_document_model__xml_location',
      'AbstractState': '_document_model__abstract_state',
      'DataElement': '_document_model__data_element',
      'DoneData': '_document_model__done_data',
      'Instruction': '_document_model__instruction',
      'Param': '_document_model__param',
      'Scxml': '_document_model__scxml',
      'StateOrTransition': '_document_model__state_or_transition',
      'Assign': '_document_model__assign',
      'Cancel': '_document_model__cancel',
      'Foreach': '_document_model__foreach',
      'HistoryState': '_document_model__history_state',
      'If': '_document_model__if',
      'Invoke': '_document_model__invoke',
      'Log': '_document_model__log',
      'Raise': '_document_model__raise',
      'Script': '_document_model__script',
      'Send': '_document_model__send',
      'State': '_document_model__state',
      'Transition': '_document_model__transition',
      'NodeVisitor': '_document_model__node_visitor',
      'ScxmlDocument': '_document_model__scxml_document',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'DocumentModel.Node'. Python calls this for a name the
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
    return [*__all__]
