"""
The 'cutienator.QtOpcUa' package provides the cute classes of the part
of Qt named QtOpcUa, under the name PySide6 has for it.

  from cutienator.QtOpcUa import QOpcUaComplexNumber, QOpcUaConnectionSettings

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
    'QOpcUaComplexNumber',
    'QOpcUaConnectionSettings',
    'QOpcUaContentFilterElementResult',
    'QOpcUaDoubleComplexNumber',
    'QOpcUaElementOperand',
    'QOpcUaErrorState',
    'QOpcUaRange',
    'QOpcUaX509Extension',
    'QOpcUaXValue',
    'QOpcUaEventFilterResult',
    'QOpcUaMonitoringParametersPrivate',
    'QOpcUaNodeCreationAttributesPrivate',
    'QOpcUaX509ExtensionBasicConstraints',
    'QOpcUaX509ExtensionExtendedKeyUsage',
    'QOpcUaX509ExtensionKeyUsage',
    'QOpcUaBrowseRequest',
    'QOpcUaDiagnosticInfo',
    'QOpcUaExpandedNodeId',
    'QOpcUaExtensionObject',
    'QOpcUaHistoryEvent',
    'QOpcUaPkiConfiguration',
    'QOpcUaQualifiedName',
    'QOpcUaReadItem',
    'QOpcUaWriteResult',
    'QOpcUaX509DistinguishedName',
    'QOpcUaX509ExtensionSubjectAlternativeName',
    'QOpcUaAddReferenceItem',
    'QOpcUaBinaryDataEncoding',
    'QOpcUaBrowsePathTarget',
    'QOpcUaDeleteReferenceItem',
    'QOpcUaRelativePathElement',
    'QOpcUaSimpleAttributeOperand',
    'QOpcUaAttributeOperand',
    'QOpcUaAuthenticationInformation',
    'QOpcUaDataValue',
    'QOpcUaHistoryReadRawRequest',
    'QOpcUaKeyPair',
    'QOpcUaLiteralOperand',
    'QOpcUaLocalizedText',
    'QOpcUaMultiDimensionalArray',
    'QOpcUaPlugin',
    'QOpcUaProvider',
    'QOpcUaReadResult',
    'QOpcUaUserTokenPolicy',
    'QOpcUaVariant',
    'QOpcUaWriteItem',
    'QOpcUaApplicationDescription',
    'QOpcUaArgument',
    'QOpcUaContentFilterElement',
    'QOpcUaEUInformation',
    'QOpcUaEnumField',
    'QOpcUaHistoryData',
    'QOpcUaNodeCreationAttributes',
    'QOpcUaReferenceDescription',
    'QOpcUaStructureField',
    'QOpcUaX509CertificateSigningRequest',
    'QOpcUaAddNodeItem',
    'QOpcUaApplicationIdentity',
    'QOpcUaApplicationRecordDataType',
    'QOpcUaAxisInformation',
    'QOpcUaEndpointDescription',
    'QOpcUaEnumDefinition',
    'QOpcUaStructureDefinition',
    'QOpcUaGdsClient',
    'QOpcUaGenericStructValue',
    'QOpcUaHistoryReadEventRequest',
    'QOpcUaMonitoringParameters',
    'QOpcUaClient',
    'QOpcUaBackend',
    'QOpcUaNodeImpl',
    'QOpcUaClientImpl',
    'QOpcUaNode',
    'QOpcUaGdsClientPrivate',
    'QOpcUaHistoryReadResponse',
    'QOpcUaHistoryReadResponseImpl',
    'QOpcUaClientPrivate',
    'QOpcUaGenericStructHandler',
    'QOpcUaHistoryReadResponsePrivate',
    'QOpcUaInternalDataTypeNode',
    'QOpcUaNodePrivate',
    'QOpcUaGenericStructHandlerPrivate',
    'QOpcUa',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_opc_ua_complex_number import QOpcUaComplexNumber
  from ._q_opc_ua_connection_settings import QOpcUaConnectionSettings
  from ._q_opc_ua_content_filter_element_result import QOpcUaContentFilterElementResult
  from ._q_opc_ua_double_complex_number import QOpcUaDoubleComplexNumber
  from ._q_opc_ua_element_operand import QOpcUaElementOperand
  from ._q_opc_ua_error_state import QOpcUaErrorState
  from ._q_opc_ua_range import QOpcUaRange
  from ._q_opc_ua_x509_extension import QOpcUaX509Extension
  from ._q_opc_ua_x_value import QOpcUaXValue
  from ._q_opc_ua_event_filter_result import QOpcUaEventFilterResult
  from ._q_opc_ua_monitoring_parameters_private import QOpcUaMonitoringParametersPrivate
  from ._q_opc_ua_node_creation_attributes_private import QOpcUaNodeCreationAttributesPrivate
  from ._q_opc_ua_x509_extension_basic_constraints import QOpcUaX509ExtensionBasicConstraints
  from ._q_opc_ua_x509_extension_extended_key_usage import QOpcUaX509ExtensionExtendedKeyUsage
  from ._q_opc_ua_x509_extension_key_usage import QOpcUaX509ExtensionKeyUsage
  from ._q_opc_ua_browse_request import QOpcUaBrowseRequest
  from ._q_opc_ua_diagnostic_info import QOpcUaDiagnosticInfo
  from ._q_opc_ua_expanded_node_id import QOpcUaExpandedNodeId
  from ._q_opc_ua_extension_object import QOpcUaExtensionObject
  from ._q_opc_ua_history_event import QOpcUaHistoryEvent
  from ._q_opc_ua_pki_configuration import QOpcUaPkiConfiguration
  from ._q_opc_ua_qualified_name import QOpcUaQualifiedName
  from ._q_opc_ua_read_item import QOpcUaReadItem
  from ._q_opc_ua_write_result import QOpcUaWriteResult
  from ._q_opc_ua_x509_distinguished_name import QOpcUaX509DistinguishedName
  from ._q_opc_ua_x509_extension_subject_alternative_name import QOpcUaX509ExtensionSubjectAlternativeName
  from ._q_opc_ua_add_reference_item import QOpcUaAddReferenceItem
  from ._q_opc_ua_binary_data_encoding import QOpcUaBinaryDataEncoding
  from ._q_opc_ua_browse_path_target import QOpcUaBrowsePathTarget
  from ._q_opc_ua_delete_reference_item import QOpcUaDeleteReferenceItem
  from ._q_opc_ua_relative_path_element import QOpcUaRelativePathElement
  from ._q_opc_ua_simple_attribute_operand import QOpcUaSimpleAttributeOperand
  from ._q_opc_ua_attribute_operand import QOpcUaAttributeOperand
  from ._q_opc_ua_authentication_information import QOpcUaAuthenticationInformation
  from ._q_opc_ua_data_value import QOpcUaDataValue
  from ._q_opc_ua_history_read_raw_request import QOpcUaHistoryReadRawRequest
  from ._q_opc_ua_key_pair import QOpcUaKeyPair
  from ._q_opc_ua_literal_operand import QOpcUaLiteralOperand
  from ._q_opc_ua_localized_text import QOpcUaLocalizedText
  from ._q_opc_ua_multi_dimensional_array import QOpcUaMultiDimensionalArray
  from ._q_opc_ua_plugin import QOpcUaPlugin
  from ._q_opc_ua_provider import QOpcUaProvider
  from ._q_opc_ua_read_result import QOpcUaReadResult
  from ._q_opc_ua_user_token_policy import QOpcUaUserTokenPolicy
  from ._q_opc_ua_variant import QOpcUaVariant
  from ._q_opc_ua_write_item import QOpcUaWriteItem
  from ._q_opc_ua_application_description import QOpcUaApplicationDescription
  from ._q_opc_ua_argument import QOpcUaArgument
  from ._q_opc_ua_content_filter_element import QOpcUaContentFilterElement
  from ._q_opc_ua_e_u_information import QOpcUaEUInformation
  from ._q_opc_ua_enum_field import QOpcUaEnumField
  from ._q_opc_ua_history_data import QOpcUaHistoryData
  from ._q_opc_ua_node_creation_attributes import QOpcUaNodeCreationAttributes
  from ._q_opc_ua_reference_description import QOpcUaReferenceDescription
  from ._q_opc_ua_structure_field import QOpcUaStructureField
  from ._q_opc_ua_x509_certificate_signing_request import QOpcUaX509CertificateSigningRequest
  from ._q_opc_ua_add_node_item import QOpcUaAddNodeItem
  from ._q_opc_ua_application_identity import QOpcUaApplicationIdentity
  from ._q_opc_ua_application_record_data_type import QOpcUaApplicationRecordDataType
  from ._q_opc_ua_axis_information import QOpcUaAxisInformation
  from ._q_opc_ua_endpoint_description import QOpcUaEndpointDescription
  from ._q_opc_ua_enum_definition import QOpcUaEnumDefinition
  from ._q_opc_ua_structure_definition import QOpcUaStructureDefinition
  from ._q_opc_ua_gds_client import QOpcUaGdsClient
  from ._q_opc_ua_generic_struct_value import QOpcUaGenericStructValue
  from ._q_opc_ua_history_read_event_request import QOpcUaHistoryReadEventRequest
  from ._q_opc_ua_monitoring_parameters import QOpcUaMonitoringParameters
  from ._q_opc_ua_client import QOpcUaClient
  from ._q_opc_ua_backend import QOpcUaBackend
  from ._q_opc_ua_node_impl import QOpcUaNodeImpl
  from ._q_opc_ua_client_impl import QOpcUaClientImpl
  from ._q_opc_ua_node import QOpcUaNode
  from ._q_opc_ua_gds_client_private import QOpcUaGdsClientPrivate
  from ._q_opc_ua_history_read_response import QOpcUaHistoryReadResponse
  from ._q_opc_ua_history_read_response_impl import QOpcUaHistoryReadResponseImpl
  from ._q_opc_ua_client_private import QOpcUaClientPrivate
  from ._q_opc_ua_generic_struct_handler import QOpcUaGenericStructHandler
  from ._q_opc_ua_history_read_response_private import QOpcUaHistoryReadResponsePrivate
  from ._q_opc_ua_internal_data_type_node import QOpcUaInternalDataTypeNode
  from ._q_opc_ua_node_private import QOpcUaNodePrivate
  from ._q_opc_ua_generic_struct_handler_private import QOpcUaGenericStructHandlerPrivate
  from . import QOpcUa
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QOpcUaComplexNumber': '_q_opc_ua_complex_number',
      'QOpcUaConnectionSettings': '_q_opc_ua_connection_settings',
      'QOpcUaContentFilterElementResult': '_q_opc_ua_content_filter_element_result',
      'QOpcUaDoubleComplexNumber': '_q_opc_ua_double_complex_number',
      'QOpcUaElementOperand': '_q_opc_ua_element_operand',
      'QOpcUaErrorState': '_q_opc_ua_error_state',
      'QOpcUaRange': '_q_opc_ua_range',
      'QOpcUaX509Extension': '_q_opc_ua_x509_extension',
      'QOpcUaXValue': '_q_opc_ua_x_value',
      'QOpcUaEventFilterResult': '_q_opc_ua_event_filter_result',
      'QOpcUaMonitoringParametersPrivate': '_q_opc_ua_monitoring_parameters_private',
      'QOpcUaNodeCreationAttributesPrivate': '_q_opc_ua_node_creation_attributes_private',
      'QOpcUaX509ExtensionBasicConstraints': '_q_opc_ua_x509_extension_basic_constraints',
      'QOpcUaX509ExtensionExtendedKeyUsage': '_q_opc_ua_x509_extension_extended_key_usage',
      'QOpcUaX509ExtensionKeyUsage': '_q_opc_ua_x509_extension_key_usage',
      'QOpcUaBrowseRequest': '_q_opc_ua_browse_request',
      'QOpcUaDiagnosticInfo': '_q_opc_ua_diagnostic_info',
      'QOpcUaExpandedNodeId': '_q_opc_ua_expanded_node_id',
      'QOpcUaExtensionObject': '_q_opc_ua_extension_object',
      'QOpcUaHistoryEvent': '_q_opc_ua_history_event',
      'QOpcUaPkiConfiguration': '_q_opc_ua_pki_configuration',
      'QOpcUaQualifiedName': '_q_opc_ua_qualified_name',
      'QOpcUaReadItem': '_q_opc_ua_read_item',
      'QOpcUaWriteResult': '_q_opc_ua_write_result',
      'QOpcUaX509DistinguishedName': '_q_opc_ua_x509_distinguished_name',
      'QOpcUaX509ExtensionSubjectAlternativeName': '_q_opc_ua_x509_extension_subject_alternative_name',
      'QOpcUaAddReferenceItem': '_q_opc_ua_add_reference_item',
      'QOpcUaBinaryDataEncoding': '_q_opc_ua_binary_data_encoding',
      'QOpcUaBrowsePathTarget': '_q_opc_ua_browse_path_target',
      'QOpcUaDeleteReferenceItem': '_q_opc_ua_delete_reference_item',
      'QOpcUaRelativePathElement': '_q_opc_ua_relative_path_element',
      'QOpcUaSimpleAttributeOperand': '_q_opc_ua_simple_attribute_operand',
      'QOpcUaAttributeOperand': '_q_opc_ua_attribute_operand',
      'QOpcUaAuthenticationInformation': '_q_opc_ua_authentication_information',
      'QOpcUaDataValue': '_q_opc_ua_data_value',
      'QOpcUaHistoryReadRawRequest': '_q_opc_ua_history_read_raw_request',
      'QOpcUaKeyPair': '_q_opc_ua_key_pair',
      'QOpcUaLiteralOperand': '_q_opc_ua_literal_operand',
      'QOpcUaLocalizedText': '_q_opc_ua_localized_text',
      'QOpcUaMultiDimensionalArray': '_q_opc_ua_multi_dimensional_array',
      'QOpcUaPlugin': '_q_opc_ua_plugin',
      'QOpcUaProvider': '_q_opc_ua_provider',
      'QOpcUaReadResult': '_q_opc_ua_read_result',
      'QOpcUaUserTokenPolicy': '_q_opc_ua_user_token_policy',
      'QOpcUaVariant': '_q_opc_ua_variant',
      'QOpcUaWriteItem': '_q_opc_ua_write_item',
      'QOpcUaApplicationDescription': '_q_opc_ua_application_description',
      'QOpcUaArgument': '_q_opc_ua_argument',
      'QOpcUaContentFilterElement': '_q_opc_ua_content_filter_element',
      'QOpcUaEUInformation': '_q_opc_ua_e_u_information',
      'QOpcUaEnumField': '_q_opc_ua_enum_field',
      'QOpcUaHistoryData': '_q_opc_ua_history_data',
      'QOpcUaNodeCreationAttributes': '_q_opc_ua_node_creation_attributes',
      'QOpcUaReferenceDescription': '_q_opc_ua_reference_description',
      'QOpcUaStructureField': '_q_opc_ua_structure_field',
      'QOpcUaX509CertificateSigningRequest': '_q_opc_ua_x509_certificate_signing_request',
      'QOpcUaAddNodeItem': '_q_opc_ua_add_node_item',
      'QOpcUaApplicationIdentity': '_q_opc_ua_application_identity',
      'QOpcUaApplicationRecordDataType': '_q_opc_ua_application_record_data_type',
      'QOpcUaAxisInformation': '_q_opc_ua_axis_information',
      'QOpcUaEndpointDescription': '_q_opc_ua_endpoint_description',
      'QOpcUaEnumDefinition': '_q_opc_ua_enum_definition',
      'QOpcUaStructureDefinition': '_q_opc_ua_structure_definition',
      'QOpcUaGdsClient': '_q_opc_ua_gds_client',
      'QOpcUaGenericStructValue': '_q_opc_ua_generic_struct_value',
      'QOpcUaHistoryReadEventRequest': '_q_opc_ua_history_read_event_request',
      'QOpcUaMonitoringParameters': '_q_opc_ua_monitoring_parameters',
      'QOpcUaClient': '_q_opc_ua_client',
      'QOpcUaBackend': '_q_opc_ua_backend',
      'QOpcUaNodeImpl': '_q_opc_ua_node_impl',
      'QOpcUaClientImpl': '_q_opc_ua_client_impl',
      'QOpcUaNode': '_q_opc_ua_node',
      'QOpcUaGdsClientPrivate': '_q_opc_ua_gds_client_private',
      'QOpcUaHistoryReadResponse': '_q_opc_ua_history_read_response',
      'QOpcUaHistoryReadResponseImpl': '_q_opc_ua_history_read_response_impl',
      'QOpcUaClientPrivate': '_q_opc_ua_client_private',
      'QOpcUaGenericStructHandler': '_q_opc_ua_generic_struct_handler',
      'QOpcUaHistoryReadResponsePrivate': '_q_opc_ua_history_read_response_private',
      'QOpcUaInternalDataTypeNode': '_q_opc_ua_internal_data_type_node',
      'QOpcUaNodePrivate': '_q_opc_ua_node_private',
      'QOpcUaGenericStructHandlerPrivate': '_q_opc_ua_generic_struct_handler_private',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QOpcUa',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtOpcUa import QOpcUaGenericStructHandlerPrivate'. Python calls
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
