"""
The 'cutienator.QtPrintSupport' package provides the cute classes of the
part of Qt named QtPrintSupport, under the name PySide6 has for it.

  from cutienator.QtPrintSupport import QPlatformPrinterSupportPlugin, QPrintEngine

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
    'QPlatformPrinterSupportPlugin',
    'QPrintEngine',
    'QAlphaPaintEnginePrivate',
    'QPreviewPaintEngine',
    'QPrinter',
    'QPrinterInfo',
    'QAlphaPaintEngine',
    'QPlatformPrinterSupport',
    'QPrinterPrivate',
    'QCocoaPrinterSupport',
    'QWindowsPrinterSupport',
    'QPrintPreviewWidget',
    'QAbstractPrintDialogPrivate',
    'QPageSetupDialog',
    'QPageSetupDialogPrivate',
    'QPrintPreviewDialog',
    'QAbstractPrintDialog',
    'QPrintDialog',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_platform_printer_support_plugin import QPlatformPrinterSupportPlugin
  from ._q_print_engine import QPrintEngine
  from ._q_alpha_paint_engine_private import QAlphaPaintEnginePrivate
  from ._q_preview_paint_engine import QPreviewPaintEngine
  from ._q_printer import QPrinter
  from ._q_printer_info import QPrinterInfo
  from ._q_alpha_paint_engine import QAlphaPaintEngine
  from ._q_platform_printer_support import QPlatformPrinterSupport
  from ._q_printer_private import QPrinterPrivate
  from ._q_cocoa_printer_support import QCocoaPrinterSupport
  from ._q_windows_printer_support import QWindowsPrinterSupport
  from ._q_print_preview_widget import QPrintPreviewWidget
  from ._q_abstract_print_dialog_private import QAbstractPrintDialogPrivate
  from ._q_page_setup_dialog import QPageSetupDialog
  from ._q_page_setup_dialog_private import QPageSetupDialogPrivate
  from ._q_print_preview_dialog import QPrintPreviewDialog
  from ._q_abstract_print_dialog import QAbstractPrintDialog
  from ._q_print_dialog import QPrintDialog
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QPlatformPrinterSupportPlugin': '_q_platform_printer_support_plugin',
      'QPrintEngine': '_q_print_engine',
      'QAlphaPaintEnginePrivate': '_q_alpha_paint_engine_private',
      'QPreviewPaintEngine': '_q_preview_paint_engine',
      'QPrinter': '_q_printer',
      'QPrinterInfo': '_q_printer_info',
      'QAlphaPaintEngine': '_q_alpha_paint_engine',
      'QPlatformPrinterSupport': '_q_platform_printer_support',
      'QPrinterPrivate': '_q_printer_private',
      'QCocoaPrinterSupport': '_q_cocoa_printer_support',
      'QWindowsPrinterSupport': '_q_windows_printer_support',
      'QPrintPreviewWidget': '_q_print_preview_widget',
      'QAbstractPrintDialogPrivate': '_q_abstract_print_dialog_private',
      'QPageSetupDialog': '_q_page_setup_dialog',
      'QPageSetupDialogPrivate': '_q_page_setup_dialog_private',
      'QPrintPreviewDialog': '_q_print_preview_dialog',
      'QAbstractPrintDialog': '_q_abstract_print_dialog',
      'QPrintDialog': '_q_print_dialog',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtPrintSupport import QPrintDialog'. Python calls
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
