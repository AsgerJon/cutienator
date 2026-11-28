"""
The 'cutienator.QtHelp' package provides the cute classes of the part of
Qt named QtHelp, under the name PySide6 has for it.

  from cutienator.QtHelp import QHelpLink, QHelpSearchQuery

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
    'QHelpLink',
    'QHelpSearchQuery',
    'QCompressedHelpInfo',
    'QHelpGlobal',
    'QHelpContentItem',
    'QHelpFilterData',
    'QHelpSearchResult',
    'QHelpDBReader',
    'QHelpEngineCore',
    'QHelpContentModel',
    'QHelpEngine',
    'QHelpSearchEngine',
    'QHelpSearchEngineCore',
    'QHelpIndexModel',
    'QHelpCollectionHandler',
    'QHelpFilterEngine',
    'QHelpFilterSettingsWidget',
    'QHelpSearchQueryWidget',
    'QHelpSearchResultWidget',
    'QHelpIndexWidget',
    'QHelpContentWidget',
    'QOptionsWidget',
    'fulltextsearch',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_help_link import QHelpLink
  from ._q_help_search_query import QHelpSearchQuery
  from ._q_compressed_help_info import QCompressedHelpInfo
  from ._q_help_global import QHelpGlobal
  from ._q_help_content_item import QHelpContentItem
  from ._q_help_filter_data import QHelpFilterData
  from ._q_help_search_result import QHelpSearchResult
  from ._q_help_d_b_reader import QHelpDBReader
  from ._q_help_engine_core import QHelpEngineCore
  from ._q_help_content_model import QHelpContentModel
  from ._q_help_engine import QHelpEngine
  from ._q_help_search_engine import QHelpSearchEngine
  from ._q_help_search_engine_core import QHelpSearchEngineCore
  from ._q_help_index_model import QHelpIndexModel
  from ._q_help_collection_handler import QHelpCollectionHandler
  from ._q_help_filter_engine import QHelpFilterEngine
  from ._q_help_filter_settings_widget import QHelpFilterSettingsWidget
  from ._q_help_search_query_widget import QHelpSearchQueryWidget
  from ._q_help_search_result_widget import QHelpSearchResultWidget
  from ._q_help_index_widget import QHelpIndexWidget
  from ._q_help_content_widget import QHelpContentWidget
  from ._q_options_widget import QOptionsWidget
  from . import fulltextsearch
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QHelpLink': '_q_help_link',
      'QHelpSearchQuery': '_q_help_search_query',
      'QCompressedHelpInfo': '_q_compressed_help_info',
      'QHelpGlobal': '_q_help_global',
      'QHelpContentItem': '_q_help_content_item',
      'QHelpFilterData': '_q_help_filter_data',
      'QHelpSearchResult': '_q_help_search_result',
      'QHelpDBReader': '_q_help_d_b_reader',
      'QHelpEngineCore': '_q_help_engine_core',
      'QHelpContentModel': '_q_help_content_model',
      'QHelpEngine': '_q_help_engine',
      'QHelpSearchEngine': '_q_help_search_engine',
      'QHelpSearchEngineCore': '_q_help_search_engine_core',
      'QHelpIndexModel': '_q_help_index_model',
      'QHelpCollectionHandler': '_q_help_collection_handler',
      'QHelpFilterEngine': '_q_help_filter_engine',
      'QHelpFilterSettingsWidget': '_q_help_filter_settings_widget',
      'QHelpSearchQueryWidget': '_q_help_search_query_widget',
      'QHelpSearchResultWidget': '_q_help_search_result_widget',
      'QHelpIndexWidget': '_q_help_index_widget',
      'QHelpContentWidget': '_q_help_content_widget',
      'QOptionsWidget': '_q_options_widget',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('fulltextsearch',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtHelp import QOptionsWidget'. Python calls
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
