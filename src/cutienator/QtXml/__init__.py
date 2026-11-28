"""
The 'cutienator.QtXml' package provides the cute classes of the part of
Qt named QtXml, under the name PySide6 has for it.

  from cutienator.QtXml import QDomImplementationPrivate, QDomNodePrivate

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
    'QDomImplementationPrivate',
    'QDomNodePrivate',
    'QDomNode',
    'QDomDocumentTypePrivate',
    'QDomDocumentType',
    'QDomDocument',
    'QDomDocumentPrivate',
    'QDomAttrPrivate',
    'QDomBuilder',
    'QDomCharacterDataPrivate',
    'QDomDocumentFragmentPrivate',
    'QDomEntityPrivate',
    'QDomEntityReferencePrivate',
    'QDomImplementation',
    'QDomNamedNodeMapPrivate',
    'QDomNodeListPrivate',
    'QDomNotationPrivate',
    'QDomParser',
    'QDomProcessingInstructionPrivate',
    'QDomAttr',
    'QDomCharacterData',
    'QDomCommentPrivate',
    'QDomDocumentFragment',
    'QDomElementPrivate',
    'QDomEntity',
    'QDomEntityReference',
    'QDomNamedNodeMap',
    'QDomNodeList',
    'QDomNotation',
    'QDomProcessingInstruction',
    'QDomTextPrivate',
    'QDomCDATASectionPrivate',
    'QDomComment',
    'QDomElement',
    'QDomText',
    'QDomCDATASection',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_dom_implementation_private import QDomImplementationPrivate
  from ._q_dom_node_private import QDomNodePrivate
  from ._q_dom_node import QDomNode
  from ._q_dom_document_type_private import QDomDocumentTypePrivate
  from ._q_dom_document_type import QDomDocumentType
  from ._q_dom_document import QDomDocument
  from ._q_dom_document_private import QDomDocumentPrivate
  from ._q_dom_attr_private import QDomAttrPrivate
  from ._q_dom_builder import QDomBuilder
  from ._q_dom_character_data_private import QDomCharacterDataPrivate
  from ._q_dom_document_fragment_private import QDomDocumentFragmentPrivate
  from ._q_dom_entity_private import QDomEntityPrivate
  from ._q_dom_entity_reference_private import QDomEntityReferencePrivate
  from ._q_dom_implementation import QDomImplementation
  from ._q_dom_named_node_map_private import QDomNamedNodeMapPrivate
  from ._q_dom_node_list_private import QDomNodeListPrivate
  from ._q_dom_notation_private import QDomNotationPrivate
  from ._q_dom_parser import QDomParser
  from ._q_dom_processing_instruction_private import QDomProcessingInstructionPrivate
  from ._q_dom_attr import QDomAttr
  from ._q_dom_character_data import QDomCharacterData
  from ._q_dom_comment_private import QDomCommentPrivate
  from ._q_dom_document_fragment import QDomDocumentFragment
  from ._q_dom_element_private import QDomElementPrivate
  from ._q_dom_entity import QDomEntity
  from ._q_dom_entity_reference import QDomEntityReference
  from ._q_dom_named_node_map import QDomNamedNodeMap
  from ._q_dom_node_list import QDomNodeList
  from ._q_dom_notation import QDomNotation
  from ._q_dom_processing_instruction import QDomProcessingInstruction
  from ._q_dom_text_private import QDomTextPrivate
  from ._q_dom_c_d_a_t_a_section_private import QDomCDATASectionPrivate
  from ._q_dom_comment import QDomComment
  from ._q_dom_element import QDomElement
  from ._q_dom_text import QDomText
  from ._q_dom_c_d_a_t_a_section import QDomCDATASection
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QDomImplementationPrivate': '_q_dom_implementation_private',
      'QDomNodePrivate': '_q_dom_node_private',
      'QDomNode': '_q_dom_node',
      'QDomDocumentTypePrivate': '_q_dom_document_type_private',
      'QDomDocumentType': '_q_dom_document_type',
      'QDomDocument': '_q_dom_document',
      'QDomDocumentPrivate': '_q_dom_document_private',
      'QDomAttrPrivate': '_q_dom_attr_private',
      'QDomBuilder': '_q_dom_builder',
      'QDomCharacterDataPrivate': '_q_dom_character_data_private',
      'QDomDocumentFragmentPrivate': '_q_dom_document_fragment_private',
      'QDomEntityPrivate': '_q_dom_entity_private',
      'QDomEntityReferencePrivate': '_q_dom_entity_reference_private',
      'QDomImplementation': '_q_dom_implementation',
      'QDomNamedNodeMapPrivate': '_q_dom_named_node_map_private',
      'QDomNodeListPrivate': '_q_dom_node_list_private',
      'QDomNotationPrivate': '_q_dom_notation_private',
      'QDomParser': '_q_dom_parser',
      'QDomProcessingInstructionPrivate': '_q_dom_processing_instruction_private',
      'QDomAttr': '_q_dom_attr',
      'QDomCharacterData': '_q_dom_character_data',
      'QDomCommentPrivate': '_q_dom_comment_private',
      'QDomDocumentFragment': '_q_dom_document_fragment',
      'QDomElementPrivate': '_q_dom_element_private',
      'QDomEntity': '_q_dom_entity',
      'QDomEntityReference': '_q_dom_entity_reference',
      'QDomNamedNodeMap': '_q_dom_named_node_map',
      'QDomNodeList': '_q_dom_node_list',
      'QDomNotation': '_q_dom_notation',
      'QDomProcessingInstruction': '_q_dom_processing_instruction',
      'QDomTextPrivate': '_q_dom_text_private',
      'QDomCDATASectionPrivate': '_q_dom_c_d_a_t_a_section_private',
      'QDomComment': '_q_dom_comment',
      'QDomElement': '_q_dom_element',
      'QDomText': '_q_dom_text',
      'QDomCDATASection': '_q_dom_c_d_a_t_a_section',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtXml import QDomCDATASection'. Python calls
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
