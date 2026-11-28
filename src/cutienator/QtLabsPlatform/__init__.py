"""
The 'cutienator.QtLabsPlatform' package provides the cute classes of the
part of Qt named QtLabsPlatform, under the name PySide6 has for it.

  from cutienator.QtLabsPlatform import QQuickLabsPlatformIcon, QQuickLabsPlatformFileNameFilter

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
    'QQuickLabsPlatformIcon',
    'QQuickLabsPlatformFileNameFilter',
    'QQuickLabsPlatformDialog',
    'QQuickLabsPlatformStandardPaths',
    'QQuickLabsPlatformColorDialog',
    'QQuickLabsPlatformFileDialog',
    'QQuickLabsPlatformFolderDialog',
    'QQuickLabsPlatformFontDialog',
    'QQuickLabsPlatformIconLoader',
    'QQuickLabsPlatformMessageDialog',
    'QQuickLabsPlatformMenu',
    'QQuickLabsPlatformMenuBar',
    'QQuickLabsPlatformMenuItem',
    'QQuickLabsPlatformMenuItemGroup',
    'QQuickLabsPlatformSystemTrayIcon',
    'QQuickLabsPlatformMenuSeparator',
    'QWidgetPlatformDialog',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_labs_platform_icon import QQuickLabsPlatformIcon
  from ._q_quick_labs_platform_file_name_filter import QQuickLabsPlatformFileNameFilter
  from ._q_quick_labs_platform_dialog import QQuickLabsPlatformDialog
  from ._q_quick_labs_platform_standard_paths import QQuickLabsPlatformStandardPaths
  from ._q_quick_labs_platform_color_dialog import QQuickLabsPlatformColorDialog
  from ._q_quick_labs_platform_file_dialog import QQuickLabsPlatformFileDialog
  from ._q_quick_labs_platform_folder_dialog import QQuickLabsPlatformFolderDialog
  from ._q_quick_labs_platform_font_dialog import QQuickLabsPlatformFontDialog
  from ._q_quick_labs_platform_icon_loader import QQuickLabsPlatformIconLoader
  from ._q_quick_labs_platform_message_dialog import QQuickLabsPlatformMessageDialog
  from ._q_quick_labs_platform_menu import QQuickLabsPlatformMenu
  from ._q_quick_labs_platform_menu_bar import QQuickLabsPlatformMenuBar
  from ._q_quick_labs_platform_menu_item import QQuickLabsPlatformMenuItem
  from ._q_quick_labs_platform_menu_item_group import QQuickLabsPlatformMenuItemGroup
  from ._q_quick_labs_platform_system_tray_icon import QQuickLabsPlatformSystemTrayIcon
  from ._q_quick_labs_platform_menu_separator import QQuickLabsPlatformMenuSeparator
  from ._q_widget_platform_dialog import QWidgetPlatformDialog
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickLabsPlatformIcon': '_q_quick_labs_platform_icon',
      'QQuickLabsPlatformFileNameFilter': '_q_quick_labs_platform_file_name_filter',
      'QQuickLabsPlatformDialog': '_q_quick_labs_platform_dialog',
      'QQuickLabsPlatformStandardPaths': '_q_quick_labs_platform_standard_paths',
      'QQuickLabsPlatformColorDialog': '_q_quick_labs_platform_color_dialog',
      'QQuickLabsPlatformFileDialog': '_q_quick_labs_platform_file_dialog',
      'QQuickLabsPlatformFolderDialog': '_q_quick_labs_platform_folder_dialog',
      'QQuickLabsPlatformFontDialog': '_q_quick_labs_platform_font_dialog',
      'QQuickLabsPlatformIconLoader': '_q_quick_labs_platform_icon_loader',
      'QQuickLabsPlatformMessageDialog': '_q_quick_labs_platform_message_dialog',
      'QQuickLabsPlatformMenu': '_q_quick_labs_platform_menu',
      'QQuickLabsPlatformMenuBar': '_q_quick_labs_platform_menu_bar',
      'QQuickLabsPlatformMenuItem': '_q_quick_labs_platform_menu_item',
      'QQuickLabsPlatformMenuItemGroup': '_q_quick_labs_platform_menu_item_group',
      'QQuickLabsPlatformSystemTrayIcon': '_q_quick_labs_platform_system_tray_icon',
      'QQuickLabsPlatformMenuSeparator': '_q_quick_labs_platform_menu_separator',
      'QWidgetPlatformDialog': '_q_widget_platform_dialog',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtLabsPlatform import QWidgetPlatformDialog'. Python calls
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
