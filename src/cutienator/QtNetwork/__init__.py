"""
The 'cutienator.QtNetwork' package provides the cute classes of the part
of Qt named QtNetwork, under the name PySide6 has for it.

  from cutienator.QtNetwork import QDnsDomainNameRecord, QDnsHostAddressRecord

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
    'QDnsDomainNameRecord',
    'QDnsHostAddressRecord',
    'QDnsMailExchangeRecord',
    'QDnsServiceRecord',
    'QDnsTextRecord',
    'QHttp1Configuration',
    'QHttp2Configuration',
    'QHttpHeaderRangeSpec',
    'QIPv6Address',
    'QNetworkAddressEntryPrivate',
    'QNetworkAuthenticationCredential',
    'QOcspResponse',
    'QSslCertificateExtension',
    'QSslCipherPrivate',
    'QTcpKeepAliveConfiguration',
    'qt_sockaddr',
    'QDnsRecordPrivate',
    'QHttp2ConfigurationPrivate',
    'QHttpHeaderRangeSet',
    'QNetworkCookiePrivate',
    'QOcspResponsePrivate',
    'QSslCertificateExtensionPrivate',
    'QSslPreSharedKeyAuthenticatorPrivate',
    'QByteDataBuffer',
    'QDnsDomainNameRecordPrivate',
    'QDnsHostAddressRecordPrivate',
    'QDnsMailExchangeRecordPrivate',
    'QDnsServiceRecordPrivate',
    'QDnsTextRecordPrivate',
    'QDnsTlsAssociationRecordPrivate',
    'QSslDiffieHellmanParametersPrivate',
    'QSslKeyPrivate',
    'QSslKeyingMaterial',
    'QDecompressHelper',
    'QFormDataBuilder',
    'QHttpHeaderParser',
    'QNetworkInterfaceManager',
    'QSslCipher',
    'QSslEllipticCurve',
    'QHttpNetworkHeader',
    'QHttpNetworkHeaderPrivate',
    'QNetworkRequestFactoryPrivate',
    'QAbstractNetworkCachePrivate',
    'QAbstractSocketEnginePrivate',
    'QAuthenticator',
    'QDnsLookupPrivate',
    'QDnsTlsAssociationRecord',
    'QDtlsClientVerifierPrivate',
    'QDtlsPrivate',
    'QHostAddress',
    'QHostInfoPrivate',
    'QHostInfoRunnable',
    'QHstsPolicy',
    'QHttpHeaders',
    'QHttpNetworkReplyPrivate',
    'QLocalServerPrivate',
    'QLocalSocket',
    'QNetworkAccessCache',
    'QNetworkCookie',
    'QNetworkCookieJarPrivate',
    'QNetworkInformation',
    'QNetworkInformationBackend',
    'QNetworkInformationBackendFactory',
    'QNetworkInterface',
    'QNetworkProxyQuery',
    'QSslDiffieHellmanParameters',
    'QSslKey',
    'QSslPreSharedKeyAuthenticator',
    'QAuthenticatorPrivate',
    'QCacheItem',
    'QFormDataPartBuilder',
    'QHostAddressPrivate',
    'QHostInfo',
    'QHostInfoAgent',
    'QHostInfoLookupManager',
    'QHstsHeaderParser',
    'QHstsStore',
    'QHttpSocketEnginePrivate',
    'QIpPacketHeader',
    'QLocalServer',
    'QNetworkAddressEntry',
    'QNetworkCacheMetaData',
    'QNetworkCookieJar',
    'QNetworkProxyFactory',
    'QNonContiguousByteDeviceThreadForwardImpl',
    'QSslCertificate',
    'QAbstractNetworkCache',
    'QHostInfoCache',
    'QHostInfoResult',
    'QHstsCache',
    'QNetworkDatagramPrivate',
    'QNetworkDiskCachePrivate',
    'QNetworkInterfacePrivate',
    'QSslCertificatePrivate',
    'QSslError',
    'QNetworkProxy',
    'QAbstractSocket',
    'QSslConfiguration',
    'QAbstractSocketEngineReceiver',
    'QAbstractSocketPrivate',
    'QTcpSocketPrivate',
    'QNetworkRequest',
    'QSslConfigurationPrivate',
    'QTcpSocket',
    'QSslSocket',
    'QHttp2Connection',
    'QHttp2Stream',
    'QNetworkDatagram',
    'QNetworkDiskCache',
    'QAbstractSocketEngine',
    'QDnsLookup',
    'QHttpNetworkRequest',
    'QHttpPart',
    'QLocalSocketPrivate',
    'QLocalUnixSocket',
    'QNetmask',
    'QNetworkAccessAuthenticationManager',
    'QNetworkHeadersPrivate',
    'QNetworkRequestFactory',
    'QSctpSocket',
    'QSctpSocketPrivate',
    'QSocketEngineHandler',
    'QSocks5Authenticator',
    'QSocks5SocketEnginePrivate',
    'QSslSocketPrivate',
    'QTcpServerPrivate',
    'QUdpSocket',
    'QDnsLookupReply',
    'QDtls',
    'QDtlsClientVerifier',
    'QHttpMultiPart',
    'QHttpNetworkConnection',
    'QHttpNetworkRequestPrivate',
    'QHttpPartPrivate',
    'QHttpSocketEngine',
    'QHttpSocketEngineHandler',
    'QNativeSocketEngine',
    'QSctpServerPrivate',
    'QSocks5PasswordAuthenticator',
    'QSocks5SocketEngine',
    'QSocks5SocketEngineHandler',
    'QSslServerPrivate',
    'QTcpServer',
    'QDnsLookupRunnable',
    'QHttpMultiPartPrivate',
    'QNativeSocketEnginePrivate',
    'QNetworkAccessManager',
    'QNetworkReply',
    'QNetworkReplyPrivate',
    'QSctpServer',
    'QSslServer',
    'QTlsBackend',
    'QHttpMultiPartIODevice',
    'QHttpNetworkConnectionChannel',
    'QHttpNetworkReply',
    'QHttpThreadDelegate',
    'QNetworkAccessBackendFactory',
    'QNetworkAccessManagerPrivate',
    'QNetworkFile',
    'QNetworkReplyDataImpl',
    'QNetworkReplyDataImplPrivate',
    'QNetworkReplyFileImpl',
    'QNetworkReplyFileImplPrivate',
    'QNetworkReplyHttpImpl',
    'QNetworkReplyHttpImplPrivate',
    'QNetworkReplyImpl',
    'QNetworkReplyImplPrivate',
    'QRestAccessManager',
    'QRestAccessManagerPrivate',
    'QRestReply',
    'QRestReplyPrivate',
    'QAbstractProtocolHandler',
    'QHttpNetworkConnectionPrivate',
    'QNetworkAccessBackend',
    'QNetworkAccessFileBackendFactory',
    'QHttp2ProtocolHandler',
    'QHttpProtocolHandler',
    'QNetworkAccessCacheBackend',
    'QNetworkAccessFileBackend',
    'HPack',
    'Http2',
    'QSsl',
    'QTlsPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_dns_domain_name_record import QDnsDomainNameRecord
  from ._q_dns_host_address_record import QDnsHostAddressRecord
  from ._q_dns_mail_exchange_record import QDnsMailExchangeRecord
  from ._q_dns_service_record import QDnsServiceRecord
  from ._q_dns_text_record import QDnsTextRecord
  from ._q_http1_configuration import QHttp1Configuration
  from ._q_http2_configuration import QHttp2Configuration
  from ._q_http_header_range_spec import QHttpHeaderRangeSpec
  from ._q_i_pv6_address import QIPv6Address
  from ._q_network_address_entry_private import QNetworkAddressEntryPrivate
  from ._q_network_authentication_credential import QNetworkAuthenticationCredential
  from ._q_ocsp_response import QOcspResponse
  from ._q_ssl_certificate_extension import QSslCertificateExtension
  from ._q_ssl_cipher_private import QSslCipherPrivate
  from ._q_tcp_keep_alive_configuration import QTcpKeepAliveConfiguration
  from ._qt_sockaddr import qt_sockaddr
  from ._q_dns_record_private import QDnsRecordPrivate
  from ._q_http2_configuration_private import QHttp2ConfigurationPrivate
  from ._q_http_header_range_set import QHttpHeaderRangeSet
  from ._q_network_cookie_private import QNetworkCookiePrivate
  from ._q_ocsp_response_private import QOcspResponsePrivate
  from ._q_ssl_certificate_extension_private import QSslCertificateExtensionPrivate
  from ._q_ssl_pre_shared_key_authenticator_private import QSslPreSharedKeyAuthenticatorPrivate
  from ._q_byte_data_buffer import QByteDataBuffer
  from ._q_dns_domain_name_record_private import QDnsDomainNameRecordPrivate
  from ._q_dns_host_address_record_private import QDnsHostAddressRecordPrivate
  from ._q_dns_mail_exchange_record_private import QDnsMailExchangeRecordPrivate
  from ._q_dns_service_record_private import QDnsServiceRecordPrivate
  from ._q_dns_text_record_private import QDnsTextRecordPrivate
  from ._q_dns_tls_association_record_private import QDnsTlsAssociationRecordPrivate
  from ._q_ssl_diffie_hellman_parameters_private import QSslDiffieHellmanParametersPrivate
  from ._q_ssl_key_private import QSslKeyPrivate
  from ._q_ssl_keying_material import QSslKeyingMaterial
  from ._q_decompress_helper import QDecompressHelper
  from ._q_form_data_builder import QFormDataBuilder
  from ._q_http_header_parser import QHttpHeaderParser
  from ._q_network_interface_manager import QNetworkInterfaceManager
  from ._q_ssl_cipher import QSslCipher
  from ._q_ssl_elliptic_curve import QSslEllipticCurve
  from ._q_http_network_header import QHttpNetworkHeader
  from ._q_http_network_header_private import QHttpNetworkHeaderPrivate
  from ._q_network_request_factory_private import QNetworkRequestFactoryPrivate
  from ._q_abstract_network_cache_private import QAbstractNetworkCachePrivate
  from ._q_abstract_socket_engine_private import QAbstractSocketEnginePrivate
  from ._q_authenticator import QAuthenticator
  from ._q_dns_lookup_private import QDnsLookupPrivate
  from ._q_dns_tls_association_record import QDnsTlsAssociationRecord
  from ._q_dtls_client_verifier_private import QDtlsClientVerifierPrivate
  from ._q_dtls_private import QDtlsPrivate
  from ._q_host_address import QHostAddress
  from ._q_host_info_private import QHostInfoPrivate
  from ._q_host_info_runnable import QHostInfoRunnable
  from ._q_hsts_policy import QHstsPolicy
  from ._q_http_headers import QHttpHeaders
  from ._q_http_network_reply_private import QHttpNetworkReplyPrivate
  from ._q_local_server_private import QLocalServerPrivate
  from ._q_local_socket import QLocalSocket
  from ._q_network_access_cache import QNetworkAccessCache
  from ._q_network_cookie import QNetworkCookie
  from ._q_network_cookie_jar_private import QNetworkCookieJarPrivate
  from ._q_network_information import QNetworkInformation
  from ._q_network_information_backend import QNetworkInformationBackend
  from ._q_network_information_backend_factory import QNetworkInformationBackendFactory
  from ._q_network_interface import QNetworkInterface
  from ._q_network_proxy_query import QNetworkProxyQuery
  from ._q_ssl_diffie_hellman_parameters import QSslDiffieHellmanParameters
  from ._q_ssl_key import QSslKey
  from ._q_ssl_pre_shared_key_authenticator import QSslPreSharedKeyAuthenticator
  from ._q_authenticator_private import QAuthenticatorPrivate
  from ._q_cache_item import QCacheItem
  from ._q_form_data_part_builder import QFormDataPartBuilder
  from ._q_host_address_private import QHostAddressPrivate
  from ._q_host_info import QHostInfo
  from ._q_host_info_agent import QHostInfoAgent
  from ._q_host_info_lookup_manager import QHostInfoLookupManager
  from ._q_hsts_header_parser import QHstsHeaderParser
  from ._q_hsts_store import QHstsStore
  from ._q_http_socket_engine_private import QHttpSocketEnginePrivate
  from ._q_ip_packet_header import QIpPacketHeader
  from ._q_local_server import QLocalServer
  from ._q_network_address_entry import QNetworkAddressEntry
  from ._q_network_cache_meta_data import QNetworkCacheMetaData
  from ._q_network_cookie_jar import QNetworkCookieJar
  from ._q_network_proxy_factory import QNetworkProxyFactory
  from ._q_non_contiguous_byte_device_thread_forward_impl import QNonContiguousByteDeviceThreadForwardImpl
  from ._q_ssl_certificate import QSslCertificate
  from ._q_abstract_network_cache import QAbstractNetworkCache
  from ._q_host_info_cache import QHostInfoCache
  from ._q_host_info_result import QHostInfoResult
  from ._q_hsts_cache import QHstsCache
  from ._q_network_datagram_private import QNetworkDatagramPrivate
  from ._q_network_disk_cache_private import QNetworkDiskCachePrivate
  from ._q_network_interface_private import QNetworkInterfacePrivate
  from ._q_ssl_certificate_private import QSslCertificatePrivate
  from ._q_ssl_error import QSslError
  from ._q_network_proxy import QNetworkProxy
  from ._q_abstract_socket import QAbstractSocket
  from ._q_ssl_configuration import QSslConfiguration
  from ._q_abstract_socket_engine_receiver import QAbstractSocketEngineReceiver
  from ._q_abstract_socket_private import QAbstractSocketPrivate
  from ._q_tcp_socket_private import QTcpSocketPrivate
  from ._q_network_request import QNetworkRequest
  from ._q_ssl_configuration_private import QSslConfigurationPrivate
  from ._q_tcp_socket import QTcpSocket
  from ._q_ssl_socket import QSslSocket
  from ._q_http2_connection import QHttp2Connection
  from ._q_http2_stream import QHttp2Stream
  from ._q_network_datagram import QNetworkDatagram
  from ._q_network_disk_cache import QNetworkDiskCache
  from ._q_abstract_socket_engine import QAbstractSocketEngine
  from ._q_dns_lookup import QDnsLookup
  from ._q_http_network_request import QHttpNetworkRequest
  from ._q_http_part import QHttpPart
  from ._q_local_socket_private import QLocalSocketPrivate
  from ._q_local_unix_socket import QLocalUnixSocket
  from ._q_netmask import QNetmask
  from ._q_network_access_authentication_manager import QNetworkAccessAuthenticationManager
  from ._q_network_headers_private import QNetworkHeadersPrivate
  from ._q_network_request_factory import QNetworkRequestFactory
  from ._q_sctp_socket import QSctpSocket
  from ._q_sctp_socket_private import QSctpSocketPrivate
  from ._q_socket_engine_handler import QSocketEngineHandler
  from ._q_socks5_authenticator import QSocks5Authenticator
  from ._q_socks5_socket_engine_private import QSocks5SocketEnginePrivate
  from ._q_ssl_socket_private import QSslSocketPrivate
  from ._q_tcp_server_private import QTcpServerPrivate
  from ._q_udp_socket import QUdpSocket
  from ._q_dns_lookup_reply import QDnsLookupReply
  from ._q_dtls import QDtls
  from ._q_dtls_client_verifier import QDtlsClientVerifier
  from ._q_http_multi_part import QHttpMultiPart
  from ._q_http_network_connection import QHttpNetworkConnection
  from ._q_http_network_request_private import QHttpNetworkRequestPrivate
  from ._q_http_part_private import QHttpPartPrivate
  from ._q_http_socket_engine import QHttpSocketEngine
  from ._q_http_socket_engine_handler import QHttpSocketEngineHandler
  from ._q_native_socket_engine import QNativeSocketEngine
  from ._q_sctp_server_private import QSctpServerPrivate
  from ._q_socks5_password_authenticator import QSocks5PasswordAuthenticator
  from ._q_socks5_socket_engine import QSocks5SocketEngine
  from ._q_socks5_socket_engine_handler import QSocks5SocketEngineHandler
  from ._q_ssl_server_private import QSslServerPrivate
  from ._q_tcp_server import QTcpServer
  from ._q_dns_lookup_runnable import QDnsLookupRunnable
  from ._q_http_multi_part_private import QHttpMultiPartPrivate
  from ._q_native_socket_engine_private import QNativeSocketEnginePrivate
  from ._q_network_access_manager import QNetworkAccessManager
  from ._q_network_reply import QNetworkReply
  from ._q_network_reply_private import QNetworkReplyPrivate
  from ._q_sctp_server import QSctpServer
  from ._q_ssl_server import QSslServer
  from ._q_tls_backend import QTlsBackend
  from ._q_http_multi_part_i_o_device import QHttpMultiPartIODevice
  from ._q_http_network_connection_channel import QHttpNetworkConnectionChannel
  from ._q_http_network_reply import QHttpNetworkReply
  from ._q_http_thread_delegate import QHttpThreadDelegate
  from ._q_network_access_backend_factory import QNetworkAccessBackendFactory
  from ._q_network_access_manager_private import QNetworkAccessManagerPrivate
  from ._q_network_file import QNetworkFile
  from ._q_network_reply_data_impl import QNetworkReplyDataImpl
  from ._q_network_reply_data_impl_private import QNetworkReplyDataImplPrivate
  from ._q_network_reply_file_impl import QNetworkReplyFileImpl
  from ._q_network_reply_file_impl_private import QNetworkReplyFileImplPrivate
  from ._q_network_reply_http_impl import QNetworkReplyHttpImpl
  from ._q_network_reply_http_impl_private import QNetworkReplyHttpImplPrivate
  from ._q_network_reply_impl import QNetworkReplyImpl
  from ._q_network_reply_impl_private import QNetworkReplyImplPrivate
  from ._q_rest_access_manager import QRestAccessManager
  from ._q_rest_access_manager_private import QRestAccessManagerPrivate
  from ._q_rest_reply import QRestReply
  from ._q_rest_reply_private import QRestReplyPrivate
  from ._q_abstract_protocol_handler import QAbstractProtocolHandler
  from ._q_http_network_connection_private import QHttpNetworkConnectionPrivate
  from ._q_network_access_backend import QNetworkAccessBackend
  from ._q_network_access_file_backend_factory import QNetworkAccessFileBackendFactory
  from ._q_http2_protocol_handler import QHttp2ProtocolHandler
  from ._q_http_protocol_handler import QHttpProtocolHandler
  from ._q_network_access_cache_backend import QNetworkAccessCacheBackend
  from ._q_network_access_file_backend import QNetworkAccessFileBackend
  from . import HPack
  from . import Http2
  from . import QSsl
  from . import QTlsPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QDnsDomainNameRecord': '_q_dns_domain_name_record',
      'QDnsHostAddressRecord': '_q_dns_host_address_record',
      'QDnsMailExchangeRecord': '_q_dns_mail_exchange_record',
      'QDnsServiceRecord': '_q_dns_service_record',
      'QDnsTextRecord': '_q_dns_text_record',
      'QHttp1Configuration': '_q_http1_configuration',
      'QHttp2Configuration': '_q_http2_configuration',
      'QHttpHeaderRangeSpec': '_q_http_header_range_spec',
      'QIPv6Address': '_q_i_pv6_address',
      'QNetworkAddressEntryPrivate': '_q_network_address_entry_private',
      'QNetworkAuthenticationCredential': '_q_network_authentication_credential',
      'QOcspResponse': '_q_ocsp_response',
      'QSslCertificateExtension': '_q_ssl_certificate_extension',
      'QSslCipherPrivate': '_q_ssl_cipher_private',
      'QTcpKeepAliveConfiguration': '_q_tcp_keep_alive_configuration',
      'qt_sockaddr': '_qt_sockaddr',
      'QDnsRecordPrivate': '_q_dns_record_private',
      'QHttp2ConfigurationPrivate': '_q_http2_configuration_private',
      'QHttpHeaderRangeSet': '_q_http_header_range_set',
      'QNetworkCookiePrivate': '_q_network_cookie_private',
      'QOcspResponsePrivate': '_q_ocsp_response_private',
      'QSslCertificateExtensionPrivate': '_q_ssl_certificate_extension_private',
      'QSslPreSharedKeyAuthenticatorPrivate': '_q_ssl_pre_shared_key_authenticator_private',
      'QByteDataBuffer': '_q_byte_data_buffer',
      'QDnsDomainNameRecordPrivate': '_q_dns_domain_name_record_private',
      'QDnsHostAddressRecordPrivate': '_q_dns_host_address_record_private',
      'QDnsMailExchangeRecordPrivate': '_q_dns_mail_exchange_record_private',
      'QDnsServiceRecordPrivate': '_q_dns_service_record_private',
      'QDnsTextRecordPrivate': '_q_dns_text_record_private',
      'QDnsTlsAssociationRecordPrivate': '_q_dns_tls_association_record_private',
      'QSslDiffieHellmanParametersPrivate': '_q_ssl_diffie_hellman_parameters_private',
      'QSslKeyPrivate': '_q_ssl_key_private',
      'QSslKeyingMaterial': '_q_ssl_keying_material',
      'QDecompressHelper': '_q_decompress_helper',
      'QFormDataBuilder': '_q_form_data_builder',
      'QHttpHeaderParser': '_q_http_header_parser',
      'QNetworkInterfaceManager': '_q_network_interface_manager',
      'QSslCipher': '_q_ssl_cipher',
      'QSslEllipticCurve': '_q_ssl_elliptic_curve',
      'QHttpNetworkHeader': '_q_http_network_header',
      'QHttpNetworkHeaderPrivate': '_q_http_network_header_private',
      'QNetworkRequestFactoryPrivate': '_q_network_request_factory_private',
      'QAbstractNetworkCachePrivate': '_q_abstract_network_cache_private',
      'QAbstractSocketEnginePrivate': '_q_abstract_socket_engine_private',
      'QAuthenticator': '_q_authenticator',
      'QDnsLookupPrivate': '_q_dns_lookup_private',
      'QDnsTlsAssociationRecord': '_q_dns_tls_association_record',
      'QDtlsClientVerifierPrivate': '_q_dtls_client_verifier_private',
      'QDtlsPrivate': '_q_dtls_private',
      'QHostAddress': '_q_host_address',
      'QHostInfoPrivate': '_q_host_info_private',
      'QHostInfoRunnable': '_q_host_info_runnable',
      'QHstsPolicy': '_q_hsts_policy',
      'QHttpHeaders': '_q_http_headers',
      'QHttpNetworkReplyPrivate': '_q_http_network_reply_private',
      'QLocalServerPrivate': '_q_local_server_private',
      'QLocalSocket': '_q_local_socket',
      'QNetworkAccessCache': '_q_network_access_cache',
      'QNetworkCookie': '_q_network_cookie',
      'QNetworkCookieJarPrivate': '_q_network_cookie_jar_private',
      'QNetworkInformation': '_q_network_information',
      'QNetworkInformationBackend': '_q_network_information_backend',
      'QNetworkInformationBackendFactory': '_q_network_information_backend_factory',
      'QNetworkInterface': '_q_network_interface',
      'QNetworkProxyQuery': '_q_network_proxy_query',
      'QSslDiffieHellmanParameters': '_q_ssl_diffie_hellman_parameters',
      'QSslKey': '_q_ssl_key',
      'QSslPreSharedKeyAuthenticator': '_q_ssl_pre_shared_key_authenticator',
      'QAuthenticatorPrivate': '_q_authenticator_private',
      'QCacheItem': '_q_cache_item',
      'QFormDataPartBuilder': '_q_form_data_part_builder',
      'QHostAddressPrivate': '_q_host_address_private',
      'QHostInfo': '_q_host_info',
      'QHostInfoAgent': '_q_host_info_agent',
      'QHostInfoLookupManager': '_q_host_info_lookup_manager',
      'QHstsHeaderParser': '_q_hsts_header_parser',
      'QHstsStore': '_q_hsts_store',
      'QHttpSocketEnginePrivate': '_q_http_socket_engine_private',
      'QIpPacketHeader': '_q_ip_packet_header',
      'QLocalServer': '_q_local_server',
      'QNetworkAddressEntry': '_q_network_address_entry',
      'QNetworkCacheMetaData': '_q_network_cache_meta_data',
      'QNetworkCookieJar': '_q_network_cookie_jar',
      'QNetworkProxyFactory': '_q_network_proxy_factory',
      'QNonContiguousByteDeviceThreadForwardImpl': '_q_non_contiguous_byte_device_thread_forward_impl',
      'QSslCertificate': '_q_ssl_certificate',
      'QAbstractNetworkCache': '_q_abstract_network_cache',
      'QHostInfoCache': '_q_host_info_cache',
      'QHostInfoResult': '_q_host_info_result',
      'QHstsCache': '_q_hsts_cache',
      'QNetworkDatagramPrivate': '_q_network_datagram_private',
      'QNetworkDiskCachePrivate': '_q_network_disk_cache_private',
      'QNetworkInterfacePrivate': '_q_network_interface_private',
      'QSslCertificatePrivate': '_q_ssl_certificate_private',
      'QSslError': '_q_ssl_error',
      'QNetworkProxy': '_q_network_proxy',
      'QAbstractSocket': '_q_abstract_socket',
      'QSslConfiguration': '_q_ssl_configuration',
      'QAbstractSocketEngineReceiver': '_q_abstract_socket_engine_receiver',
      'QAbstractSocketPrivate': '_q_abstract_socket_private',
      'QTcpSocketPrivate': '_q_tcp_socket_private',
      'QNetworkRequest': '_q_network_request',
      'QSslConfigurationPrivate': '_q_ssl_configuration_private',
      'QTcpSocket': '_q_tcp_socket',
      'QSslSocket': '_q_ssl_socket',
      'QHttp2Connection': '_q_http2_connection',
      'QHttp2Stream': '_q_http2_stream',
      'QNetworkDatagram': '_q_network_datagram',
      'QNetworkDiskCache': '_q_network_disk_cache',
      'QAbstractSocketEngine': '_q_abstract_socket_engine',
      'QDnsLookup': '_q_dns_lookup',
      'QHttpNetworkRequest': '_q_http_network_request',
      'QHttpPart': '_q_http_part',
      'QLocalSocketPrivate': '_q_local_socket_private',
      'QLocalUnixSocket': '_q_local_unix_socket',
      'QNetmask': '_q_netmask',
      'QNetworkAccessAuthenticationManager': '_q_network_access_authentication_manager',
      'QNetworkHeadersPrivate': '_q_network_headers_private',
      'QNetworkRequestFactory': '_q_network_request_factory',
      'QSctpSocket': '_q_sctp_socket',
      'QSctpSocketPrivate': '_q_sctp_socket_private',
      'QSocketEngineHandler': '_q_socket_engine_handler',
      'QSocks5Authenticator': '_q_socks5_authenticator',
      'QSocks5SocketEnginePrivate': '_q_socks5_socket_engine_private',
      'QSslSocketPrivate': '_q_ssl_socket_private',
      'QTcpServerPrivate': '_q_tcp_server_private',
      'QUdpSocket': '_q_udp_socket',
      'QDnsLookupReply': '_q_dns_lookup_reply',
      'QDtls': '_q_dtls',
      'QDtlsClientVerifier': '_q_dtls_client_verifier',
      'QHttpMultiPart': '_q_http_multi_part',
      'QHttpNetworkConnection': '_q_http_network_connection',
      'QHttpNetworkRequestPrivate': '_q_http_network_request_private',
      'QHttpPartPrivate': '_q_http_part_private',
      'QHttpSocketEngine': '_q_http_socket_engine',
      'QHttpSocketEngineHandler': '_q_http_socket_engine_handler',
      'QNativeSocketEngine': '_q_native_socket_engine',
      'QSctpServerPrivate': '_q_sctp_server_private',
      'QSocks5PasswordAuthenticator': '_q_socks5_password_authenticator',
      'QSocks5SocketEngine': '_q_socks5_socket_engine',
      'QSocks5SocketEngineHandler': '_q_socks5_socket_engine_handler',
      'QSslServerPrivate': '_q_ssl_server_private',
      'QTcpServer': '_q_tcp_server',
      'QDnsLookupRunnable': '_q_dns_lookup_runnable',
      'QHttpMultiPartPrivate': '_q_http_multi_part_private',
      'QNativeSocketEnginePrivate': '_q_native_socket_engine_private',
      'QNetworkAccessManager': '_q_network_access_manager',
      'QNetworkReply': '_q_network_reply',
      'QNetworkReplyPrivate': '_q_network_reply_private',
      'QSctpServer': '_q_sctp_server',
      'QSslServer': '_q_ssl_server',
      'QTlsBackend': '_q_tls_backend',
      'QHttpMultiPartIODevice': '_q_http_multi_part_i_o_device',
      'QHttpNetworkConnectionChannel': '_q_http_network_connection_channel',
      'QHttpNetworkReply': '_q_http_network_reply',
      'QHttpThreadDelegate': '_q_http_thread_delegate',
      'QNetworkAccessBackendFactory': '_q_network_access_backend_factory',
      'QNetworkAccessManagerPrivate': '_q_network_access_manager_private',
      'QNetworkFile': '_q_network_file',
      'QNetworkReplyDataImpl': '_q_network_reply_data_impl',
      'QNetworkReplyDataImplPrivate': '_q_network_reply_data_impl_private',
      'QNetworkReplyFileImpl': '_q_network_reply_file_impl',
      'QNetworkReplyFileImplPrivate': '_q_network_reply_file_impl_private',
      'QNetworkReplyHttpImpl': '_q_network_reply_http_impl',
      'QNetworkReplyHttpImplPrivate': '_q_network_reply_http_impl_private',
      'QNetworkReplyImpl': '_q_network_reply_impl',
      'QNetworkReplyImplPrivate': '_q_network_reply_impl_private',
      'QRestAccessManager': '_q_rest_access_manager',
      'QRestAccessManagerPrivate': '_q_rest_access_manager_private',
      'QRestReply': '_q_rest_reply',
      'QRestReplyPrivate': '_q_rest_reply_private',
      'QAbstractProtocolHandler': '_q_abstract_protocol_handler',
      'QHttpNetworkConnectionPrivate': '_q_http_network_connection_private',
      'QNetworkAccessBackend': '_q_network_access_backend',
      'QNetworkAccessFileBackendFactory': '_q_network_access_file_backend_factory',
      'QHttp2ProtocolHandler': '_q_http2_protocol_handler',
      'QHttpProtocolHandler': '_q_http_protocol_handler',
      'QNetworkAccessCacheBackend': '_q_network_access_cache_backend',
      'QNetworkAccessFileBackend': '_q_network_access_file_backend',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('HPack', 'Http2', 'QSsl', 'QTlsPrivate',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtNetwork import QNetworkAccessFileBackend'. Python calls
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
