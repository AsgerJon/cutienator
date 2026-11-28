"""
The namespace 'QQC2' of Qt, a package of 'cutienator.QtQuickNativeStyle':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQuickNativeStyle import QQC2
  QQC2.QStyleHintReturn

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
    'QStyleHintReturn',
    'QTileRules',
    'QStyleHintReturnMask',
    'QStyleHintReturnVariant',
    'QStylePrivate',
    'QStyle',
    'QStyleOption',
    'QStyleOptionComplex',
    'QStyleOptionSearchField',
    'QCommonStylePrivate',
    'QStyleOptionButton',
    'QStyleOptionComboBox',
    'QStyleOptionDockWidget',
    'QStyleOptionFocusRect',
    'QStyleOptionFrame',
    'QStyleOptionGraphicsItem',
    'QStyleOptionGroupBox',
    'QStyleOptionHeader',
    'QStyleOptionMenuItem',
    'QStyleOptionProgressBar',
    'QStyleOptionRubberBand',
    'QStyleOptionSizeGrip',
    'QStyleOptionSlider',
    'QStyleOptionSpinBox',
    'QStyleOptionTab',
    'QStyleOptionTabBarBase',
    'QStyleOptionTabV4',
    'QStyleOptionTabWidgetFrame',
    'QStyleOptionTitleBar',
    'QStyleOptionToolBar',
    'QStyleOptionToolBox',
    'QStyleOptionToolButton',
    'QStyleOptionViewItem',
    'QCommonStyle',
    'QMacStyle',
    'QWindowsStylePrivate',
    'QWindowsStyle',
    'QWindowsXPStyle',
    'QDrawBorderPixmap',
    'QStyleHelper',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_q_c2__q_style_hint_return import QStyleHintReturn
  from .._q_q_c2__q_tile_rules import QTileRules
  from .._q_q_c2__q_style_hint_return_mask import QStyleHintReturnMask
  from .._q_q_c2__q_style_hint_return_variant import QStyleHintReturnVariant
  from .._q_q_c2__q_style_private import QStylePrivate
  from .._q_q_c2__q_style import QStyle
  from .._q_q_c2__q_style_option import QStyleOption
  from .._q_q_c2__q_style_option_complex import QStyleOptionComplex
  from .._q_q_c2__q_style_option_search_field import QStyleOptionSearchField
  from .._q_q_c2__q_common_style_private import QCommonStylePrivate
  from .._q_q_c2__q_style_option_button import QStyleOptionButton
  from .._q_q_c2__q_style_option_combo_box import QStyleOptionComboBox
  from .._q_q_c2__q_style_option_dock_widget import QStyleOptionDockWidget
  from .._q_q_c2__q_style_option_focus_rect import QStyleOptionFocusRect
  from .._q_q_c2__q_style_option_frame import QStyleOptionFrame
  from .._q_q_c2__q_style_option_graphics_item import QStyleOptionGraphicsItem
  from .._q_q_c2__q_style_option_group_box import QStyleOptionGroupBox
  from .._q_q_c2__q_style_option_header import QStyleOptionHeader
  from .._q_q_c2__q_style_option_menu_item import QStyleOptionMenuItem
  from .._q_q_c2__q_style_option_progress_bar import QStyleOptionProgressBar
  from .._q_q_c2__q_style_option_rubber_band import QStyleOptionRubberBand
  from .._q_q_c2__q_style_option_size_grip import QStyleOptionSizeGrip
  from .._q_q_c2__q_style_option_slider import QStyleOptionSlider
  from .._q_q_c2__q_style_option_spin_box import QStyleOptionSpinBox
  from .._q_q_c2__q_style_option_tab import QStyleOptionTab
  from .._q_q_c2__q_style_option_tab_bar_base import QStyleOptionTabBarBase
  from .._q_q_c2__q_style_option_tab_v4 import QStyleOptionTabV4
  from .._q_q_c2__q_style_option_tab_widget_frame import QStyleOptionTabWidgetFrame
  from .._q_q_c2__q_style_option_title_bar import QStyleOptionTitleBar
  from .._q_q_c2__q_style_option_tool_bar import QStyleOptionToolBar
  from .._q_q_c2__q_style_option_tool_box import QStyleOptionToolBox
  from .._q_q_c2__q_style_option_tool_button import QStyleOptionToolButton
  from .._q_q_c2__q_style_option_view_item import QStyleOptionViewItem
  from .._q_q_c2__q_common_style import QCommonStyle
  from .._q_q_c2__q_mac_style import QMacStyle
  from .._q_q_c2__q_windows_style_private import QWindowsStylePrivate
  from .._q_q_c2__q_windows_style import QWindowsStyle
  from .._q_q_c2__q_windows_x_p_style import QWindowsXPStyle
  from . import QDrawBorderPixmap
  from . import QStyleHelper
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QStyleHintReturn': '_q_q_c2__q_style_hint_return',
      'QTileRules': '_q_q_c2__q_tile_rules',
      'QStyleHintReturnMask': '_q_q_c2__q_style_hint_return_mask',
      'QStyleHintReturnVariant': '_q_q_c2__q_style_hint_return_variant',
      'QStylePrivate': '_q_q_c2__q_style_private',
      'QStyle': '_q_q_c2__q_style',
      'QStyleOption': '_q_q_c2__q_style_option',
      'QStyleOptionComplex': '_q_q_c2__q_style_option_complex',
      'QStyleOptionSearchField': '_q_q_c2__q_style_option_search_field',
      'QCommonStylePrivate': '_q_q_c2__q_common_style_private',
      'QStyleOptionButton': '_q_q_c2__q_style_option_button',
      'QStyleOptionComboBox': '_q_q_c2__q_style_option_combo_box',
      'QStyleOptionDockWidget': '_q_q_c2__q_style_option_dock_widget',
      'QStyleOptionFocusRect': '_q_q_c2__q_style_option_focus_rect',
      'QStyleOptionFrame': '_q_q_c2__q_style_option_frame',
      'QStyleOptionGraphicsItem': '_q_q_c2__q_style_option_graphics_item',
      'QStyleOptionGroupBox': '_q_q_c2__q_style_option_group_box',
      'QStyleOptionHeader': '_q_q_c2__q_style_option_header',
      'QStyleOptionMenuItem': '_q_q_c2__q_style_option_menu_item',
      'QStyleOptionProgressBar': '_q_q_c2__q_style_option_progress_bar',
      'QStyleOptionRubberBand': '_q_q_c2__q_style_option_rubber_band',
      'QStyleOptionSizeGrip': '_q_q_c2__q_style_option_size_grip',
      'QStyleOptionSlider': '_q_q_c2__q_style_option_slider',
      'QStyleOptionSpinBox': '_q_q_c2__q_style_option_spin_box',
      'QStyleOptionTab': '_q_q_c2__q_style_option_tab',
      'QStyleOptionTabBarBase': '_q_q_c2__q_style_option_tab_bar_base',
      'QStyleOptionTabV4': '_q_q_c2__q_style_option_tab_v4',
      'QStyleOptionTabWidgetFrame': '_q_q_c2__q_style_option_tab_widget_frame',
      'QStyleOptionTitleBar': '_q_q_c2__q_style_option_title_bar',
      'QStyleOptionToolBar': '_q_q_c2__q_style_option_tool_bar',
      'QStyleOptionToolBox': '_q_q_c2__q_style_option_tool_box',
      'QStyleOptionToolButton': '_q_q_c2__q_style_option_tool_button',
      'QStyleOptionViewItem': '_q_q_c2__q_style_option_view_item',
      'QCommonStyle': '_q_q_c2__q_common_style',
      'QMacStyle': '_q_q_c2__q_mac_style',
      'QWindowsStylePrivate': '_q_q_c2__q_windows_style_private',
      'QWindowsStyle': '_q_q_c2__q_windows_style',
      'QWindowsXPStyle': '_q_q_c2__q_windows_x_p_style',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('QDrawBorderPixmap', 'QStyleHelper',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QQC2.QStyleHintReturn'. Python calls this for a name
    the package does not hold yet, and what it gives is kept here for the
    next time.

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
