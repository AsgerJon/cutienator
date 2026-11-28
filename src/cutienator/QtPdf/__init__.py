"""
The 'cutienator.QtPdf' package provides the cute classes of the part of
Qt named QtPdf, under the name PySide6 has for it.

  from cutienator.QtPdf import QPdfDocumentRenderOptions, QPdfLinkPrivate

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
    'QPdfDocumentRenderOptions',
    'QPdfLinkPrivate',
    'QPdfSelectionPrivate',
    'QPdfDocument',
    'QPdfBookmarkModel',
    'QPdfFile',
    'QPdfLink',
    'QPdfLinkModel',
    'QPdfPageRenderer',
    'QPdfSearchModel',
    'QPdfSelection',
    'QPdfLinkModelPrivate',
    'QPdfPageNavigator',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_pdf_document_render_options import QPdfDocumentRenderOptions
  from ._q_pdf_link_private import QPdfLinkPrivate
  from ._q_pdf_selection_private import QPdfSelectionPrivate
  from ._q_pdf_document import QPdfDocument
  from ._q_pdf_bookmark_model import QPdfBookmarkModel
  from ._q_pdf_file import QPdfFile
  from ._q_pdf_link import QPdfLink
  from ._q_pdf_link_model import QPdfLinkModel
  from ._q_pdf_page_renderer import QPdfPageRenderer
  from ._q_pdf_search_model import QPdfSearchModel
  from ._q_pdf_selection import QPdfSelection
  from ._q_pdf_link_model_private import QPdfLinkModelPrivate
  from ._q_pdf_page_navigator import QPdfPageNavigator
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QPdfDocumentRenderOptions': '_q_pdf_document_render_options',
      'QPdfLinkPrivate': '_q_pdf_link_private',
      'QPdfSelectionPrivate': '_q_pdf_selection_private',
      'QPdfDocument': '_q_pdf_document',
      'QPdfBookmarkModel': '_q_pdf_bookmark_model',
      'QPdfFile': '_q_pdf_file',
      'QPdfLink': '_q_pdf_link',
      'QPdfLinkModel': '_q_pdf_link_model',
      'QPdfPageRenderer': '_q_pdf_page_renderer',
      'QPdfSearchModel': '_q_pdf_search_model',
      'QPdfSelection': '_q_pdf_selection',
      'QPdfLinkModelPrivate': '_q_pdf_link_model_private',
      'QPdfPageNavigator': '_q_pdf_page_navigator',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtPdf import QPdfPageNavigator'. Python calls
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
