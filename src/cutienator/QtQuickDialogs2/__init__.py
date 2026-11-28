"""
The 'cutienator.QtQuickDialogs2' package provides the cute classes of
the part of Qt named QtQuickDialogs2, under the name PySide6 has for it.

  from cutienator.QtQuickDialogs2 import QQuickFileNameFilterQuickDialogs2Foreign, QQuickAbstractDialog

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
    'QQuickFileNameFilterQuickDialogs2Foreign',
    'QQuickAbstractDialog',
    'QQuickColorDialog',
    'QQuickFileDialog',
    'QQuickFolderDialog',
    'QQuickFontDialog',
    'QQuickMessageDialog',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_file_name_filter_quick_dialogs2_foreign import QQuickFileNameFilterQuickDialogs2Foreign
  from ._q_quick_abstract_dialog import QQuickAbstractDialog
  from ._q_quick_color_dialog import QQuickColorDialog
  from ._q_quick_file_dialog import QQuickFileDialog
  from ._q_quick_folder_dialog import QQuickFolderDialog
  from ._q_quick_font_dialog import QQuickFontDialog
  from ._q_quick_message_dialog import QQuickMessageDialog
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickFileNameFilterQuickDialogs2Foreign': '_q_quick_file_name_filter_quick_dialogs2_foreign',
      'QQuickAbstractDialog': '_q_quick_abstract_dialog',
      'QQuickColorDialog': '_q_quick_color_dialog',
      'QQuickFileDialog': '_q_quick_file_dialog',
      'QQuickFolderDialog': '_q_quick_folder_dialog',
      'QQuickFontDialog': '_q_quick_font_dialog',
      'QQuickMessageDialog': '_q_quick_message_dialog',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickDialogs2 import QQuickMessageDialog'. Python calls
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
