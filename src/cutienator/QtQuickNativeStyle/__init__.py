"""
The 'cutienator.QtQuickNativeStyle' package provides the cute classes of
the part of Qt named QtQuickNativeStyle, under the name PySide6 has for
it.

  from cutienator.QtQuickNativeStyle import QQuickFocusFrameDescription, StyleItemGeometry

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
    'QQuickFocusFrameDescription',
    'StyleItemGeometry',
    'QQuickStyleConstants',
    'QQuickStyleMargins',
    'QQuickFocusFrame',
    'QQuickMacFocusFrame',
    'QQuickWindowsFocusFrame',
    'QQuickStyleItem',
    'QQuickStyleItemButton',
    'QQuickStyleItemCheckBox',
    'QQuickStyleItemComboBox',
    'QQuickStyleItemDial',
    'QQuickStyleItemDoubleSpinBox',
    'QQuickStyleItemFrame',
    'QQuickStyleItemGroupBox',
    'QQuickStyleItemProgressBar',
    'QQuickStyleItemRadioButton',
    'QQuickStyleItemScrollBar',
    'QQuickStyleItemScrollViewCorner',
    'QQuickStyleItemSearchField',
    'QQuickStyleItemSlider',
    'QQuickStyleItemSpinBox',
    'QQuickStyleItemTextField',
    'QQuickStyleItemTreeIndicator',
    'QQuickStyleItemCheckDelegate',
    'QQuickStyleItemDelayButton',
    'QQuickStyleItemRadioDelegate',
    'QQC2',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_focus_frame_description import QQuickFocusFrameDescription
  from ._style_item_geometry import StyleItemGeometry
  from ._q_quick_style_constants import QQuickStyleConstants
  from ._q_quick_style_margins import QQuickStyleMargins
  from ._q_quick_focus_frame import QQuickFocusFrame
  from ._q_quick_mac_focus_frame import QQuickMacFocusFrame
  from ._q_quick_windows_focus_frame import QQuickWindowsFocusFrame
  from ._q_quick_style_item import QQuickStyleItem
  from ._q_quick_style_item_button import QQuickStyleItemButton
  from ._q_quick_style_item_check_box import QQuickStyleItemCheckBox
  from ._q_quick_style_item_combo_box import QQuickStyleItemComboBox
  from ._q_quick_style_item_dial import QQuickStyleItemDial
  from ._q_quick_style_item_double_spin_box import QQuickStyleItemDoubleSpinBox
  from ._q_quick_style_item_frame import QQuickStyleItemFrame
  from ._q_quick_style_item_group_box import QQuickStyleItemGroupBox
  from ._q_quick_style_item_progress_bar import QQuickStyleItemProgressBar
  from ._q_quick_style_item_radio_button import QQuickStyleItemRadioButton
  from ._q_quick_style_item_scroll_bar import QQuickStyleItemScrollBar
  from ._q_quick_style_item_scroll_view_corner import QQuickStyleItemScrollViewCorner
  from ._q_quick_style_item_search_field import QQuickStyleItemSearchField
  from ._q_quick_style_item_slider import QQuickStyleItemSlider
  from ._q_quick_style_item_spin_box import QQuickStyleItemSpinBox
  from ._q_quick_style_item_text_field import QQuickStyleItemTextField
  from ._q_quick_style_item_tree_indicator import QQuickStyleItemTreeIndicator
  from ._q_quick_style_item_check_delegate import QQuickStyleItemCheckDelegate
  from ._q_quick_style_item_delay_button import QQuickStyleItemDelayButton
  from ._q_quick_style_item_radio_delegate import QQuickStyleItemRadioDelegate
  from . import QQC2
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickFocusFrameDescription': '_q_quick_focus_frame_description',
      'StyleItemGeometry': '_style_item_geometry',
      'QQuickStyleConstants': '_q_quick_style_constants',
      'QQuickStyleMargins': '_q_quick_style_margins',
      'QQuickFocusFrame': '_q_quick_focus_frame',
      'QQuickMacFocusFrame': '_q_quick_mac_focus_frame',
      'QQuickWindowsFocusFrame': '_q_quick_windows_focus_frame',
      'QQuickStyleItem': '_q_quick_style_item',
      'QQuickStyleItemButton': '_q_quick_style_item_button',
      'QQuickStyleItemCheckBox': '_q_quick_style_item_check_box',
      'QQuickStyleItemComboBox': '_q_quick_style_item_combo_box',
      'QQuickStyleItemDial': '_q_quick_style_item_dial',
      'QQuickStyleItemDoubleSpinBox': '_q_quick_style_item_double_spin_box',
      'QQuickStyleItemFrame': '_q_quick_style_item_frame',
      'QQuickStyleItemGroupBox': '_q_quick_style_item_group_box',
      'QQuickStyleItemProgressBar': '_q_quick_style_item_progress_bar',
      'QQuickStyleItemRadioButton': '_q_quick_style_item_radio_button',
      'QQuickStyleItemScrollBar': '_q_quick_style_item_scroll_bar',
      'QQuickStyleItemScrollViewCorner': '_q_quick_style_item_scroll_view_corner',
      'QQuickStyleItemSearchField': '_q_quick_style_item_search_field',
      'QQuickStyleItemSlider': '_q_quick_style_item_slider',
      'QQuickStyleItemSpinBox': '_q_quick_style_item_spin_box',
      'QQuickStyleItemTextField': '_q_quick_style_item_text_field',
      'QQuickStyleItemTreeIndicator': '_q_quick_style_item_tree_indicator',
      'QQuickStyleItemCheckDelegate': '_q_quick_style_item_check_delegate',
      'QQuickStyleItemDelayButton': '_q_quick_style_item_delay_button',
      'QQuickStyleItemRadioDelegate': '_q_quick_style_item_radio_delegate',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QQC2',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickNativeStyle import QQuickStyleItemRadioDelegate'. Python calls
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
