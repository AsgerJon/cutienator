"""
The 'cutienator.QtCore5Compat' package provides the cute classes of the
part of Qt named QtCore5Compat, under the name PySide6 has for it.

  from cutienator.QtCore5Compat import QJpUnicodeConv, QLinkedListData

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
    'QJpUnicodeConv',
    'QLinkedListData',
    'QTextCodecData',
    'QXmlLocator',
    'QRegExp',
    'QTextCodec',
    'QXmlDTDHandler',
    'QXmlDeclHandler',
    'QXmlLexicalHandler',
    'QXmlNamespaceSupport',
    'QXmlParseException',
    'QBig5Codec',
    'QBig5hkscsCodec',
    'QCP949Codec',
    'QEucJpCodec',
    'QEucKrCodec',
    'QGb18030Codec',
    'QIconvCodec',
    'QIcuCodec',
    'QIsciiCodec',
    'QJisCodec',
    'QLatin15Codec',
    'QLatin1Codec',
    'QSimpleTextCodec',
    'QSjisCodec',
    'QStringRef',
    'QTextDecoder',
    'QTextEncoder',
    'QTsciiCodec',
    'QUtf16Codec',
    'QUtf32Codec',
    'QUtf8Codec',
    'QWindowsLocalCodec',
    'QXmlAttributes',
    'QXmlErrorHandler',
    'QGb2312Codec',
    'QGbkCodec',
    'QUtf16BECodec',
    'QUtf16LECodec',
    'QUtf32BECodec',
    'QUtf32LECodec',
    'QXmlContentHandler',
    'QXmlInputSource',
    'QBinaryJsonArray',
    'QBinaryJsonObject',
    'QBinaryJsonValue',
    'QXmlEntityResolver',
    'QXmlDefaultHandler',
    'QXmlReader',
    'QXmlSimpleReader',
    'QXmlSimpleReaderPrivate',
    'QBinaryJson',
    'QBinaryJsonPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_jp_unicode_conv import QJpUnicodeConv
  from ._q_linked_list_data import QLinkedListData
  from ._q_text_codec_data import QTextCodecData
  from ._q_xml_locator import QXmlLocator
  from ._q_reg_exp import QRegExp
  from ._q_text_codec import QTextCodec
  from ._q_xml_d_t_d_handler import QXmlDTDHandler
  from ._q_xml_decl_handler import QXmlDeclHandler
  from ._q_xml_lexical_handler import QXmlLexicalHandler
  from ._q_xml_namespace_support import QXmlNamespaceSupport
  from ._q_xml_parse_exception import QXmlParseException
  from ._q_big5_codec import QBig5Codec
  from ._q_big5hkscs_codec import QBig5hkscsCodec
  from ._q_c_p949_codec import QCP949Codec
  from ._q_euc_jp_codec import QEucJpCodec
  from ._q_euc_kr_codec import QEucKrCodec
  from ._q_gb18030_codec import QGb18030Codec
  from ._q_iconv_codec import QIconvCodec
  from ._q_icu_codec import QIcuCodec
  from ._q_iscii_codec import QIsciiCodec
  from ._q_jis_codec import QJisCodec
  from ._q_latin15_codec import QLatin15Codec
  from ._q_latin1_codec import QLatin1Codec
  from ._q_simple_text_codec import QSimpleTextCodec
  from ._q_sjis_codec import QSjisCodec
  from ._q_string_ref import QStringRef
  from ._q_text_decoder import QTextDecoder
  from ._q_text_encoder import QTextEncoder
  from ._q_tscii_codec import QTsciiCodec
  from ._q_utf16_codec import QUtf16Codec
  from ._q_utf32_codec import QUtf32Codec
  from ._q_utf8_codec import QUtf8Codec
  from ._q_windows_local_codec import QWindowsLocalCodec
  from ._q_xml_attributes import QXmlAttributes
  from ._q_xml_error_handler import QXmlErrorHandler
  from ._q_gb2312_codec import QGb2312Codec
  from ._q_gbk_codec import QGbkCodec
  from ._q_utf16_b_e_codec import QUtf16BECodec
  from ._q_utf16_l_e_codec import QUtf16LECodec
  from ._q_utf32_b_e_codec import QUtf32BECodec
  from ._q_utf32_l_e_codec import QUtf32LECodec
  from ._q_xml_content_handler import QXmlContentHandler
  from ._q_xml_input_source import QXmlInputSource
  from ._q_binary_json_array import QBinaryJsonArray
  from ._q_binary_json_object import QBinaryJsonObject
  from ._q_binary_json_value import QBinaryJsonValue
  from ._q_xml_entity_resolver import QXmlEntityResolver
  from ._q_xml_default_handler import QXmlDefaultHandler
  from ._q_xml_reader import QXmlReader
  from ._q_xml_simple_reader import QXmlSimpleReader
  from ._q_xml_simple_reader_private import QXmlSimpleReaderPrivate
  from . import QBinaryJson
  from . import QBinaryJsonPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QJpUnicodeConv': '_q_jp_unicode_conv',
      'QLinkedListData': '_q_linked_list_data',
      'QTextCodecData': '_q_text_codec_data',
      'QXmlLocator': '_q_xml_locator',
      'QRegExp': '_q_reg_exp',
      'QTextCodec': '_q_text_codec',
      'QXmlDTDHandler': '_q_xml_d_t_d_handler',
      'QXmlDeclHandler': '_q_xml_decl_handler',
      'QXmlLexicalHandler': '_q_xml_lexical_handler',
      'QXmlNamespaceSupport': '_q_xml_namespace_support',
      'QXmlParseException': '_q_xml_parse_exception',
      'QBig5Codec': '_q_big5_codec',
      'QBig5hkscsCodec': '_q_big5hkscs_codec',
      'QCP949Codec': '_q_c_p949_codec',
      'QEucJpCodec': '_q_euc_jp_codec',
      'QEucKrCodec': '_q_euc_kr_codec',
      'QGb18030Codec': '_q_gb18030_codec',
      'QIconvCodec': '_q_iconv_codec',
      'QIcuCodec': '_q_icu_codec',
      'QIsciiCodec': '_q_iscii_codec',
      'QJisCodec': '_q_jis_codec',
      'QLatin15Codec': '_q_latin15_codec',
      'QLatin1Codec': '_q_latin1_codec',
      'QSimpleTextCodec': '_q_simple_text_codec',
      'QSjisCodec': '_q_sjis_codec',
      'QStringRef': '_q_string_ref',
      'QTextDecoder': '_q_text_decoder',
      'QTextEncoder': '_q_text_encoder',
      'QTsciiCodec': '_q_tscii_codec',
      'QUtf16Codec': '_q_utf16_codec',
      'QUtf32Codec': '_q_utf32_codec',
      'QUtf8Codec': '_q_utf8_codec',
      'QWindowsLocalCodec': '_q_windows_local_codec',
      'QXmlAttributes': '_q_xml_attributes',
      'QXmlErrorHandler': '_q_xml_error_handler',
      'QGb2312Codec': '_q_gb2312_codec',
      'QGbkCodec': '_q_gbk_codec',
      'QUtf16BECodec': '_q_utf16_b_e_codec',
      'QUtf16LECodec': '_q_utf16_l_e_codec',
      'QUtf32BECodec': '_q_utf32_b_e_codec',
      'QUtf32LECodec': '_q_utf32_l_e_codec',
      'QXmlContentHandler': '_q_xml_content_handler',
      'QXmlInputSource': '_q_xml_input_source',
      'QBinaryJsonArray': '_q_binary_json_array',
      'QBinaryJsonObject': '_q_binary_json_object',
      'QBinaryJsonValue': '_q_binary_json_value',
      'QXmlEntityResolver': '_q_xml_entity_resolver',
      'QXmlDefaultHandler': '_q_xml_default_handler',
      'QXmlReader': '_q_xml_reader',
      'QXmlSimpleReader': '_q_xml_simple_reader',
      'QXmlSimpleReaderPrivate': '_q_xml_simple_reader_private',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QBinaryJson', 'QBinaryJsonPrivate',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtCore5Compat import QXmlSimpleReaderPrivate'. Python calls
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
