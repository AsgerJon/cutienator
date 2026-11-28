"""
The 'cutienator.QtQuickLayouts' package provides the cute classes of the
part of Qt named QtQuickLayouts, under the name PySide6 has for it.

  from cutienator.QtQuickLayouts import QQuickLayoutStyleInfo, QQuickGridLayoutEngine

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
    'QQuickLayoutStyleInfo',
    'QQuickGridLayoutEngine',
    'QQuickGridLayoutItem',
    'QQuickLayoutItemProxy',
    'QQuickLayoutItemProxyPrivate',
    'QQuickLayoutPrivate',
    'QQuickGridLayoutBasePrivate',
    'QQuickLayout',
    'QQuickLayoutAttached',
    'QQuickLayoutItemProxyAttachedData',
    'QQuickStackLayoutPrivate',
    'QQuickFlexboxLayout',
    'QQuickGridLayoutBase',
    'QQuickGridLayoutPrivate',
    'QQuickLinearLayoutPrivate',
    'QQuickStackLayout',
    'QQuickFlexboxLayoutAttached',
    'QQuickGridLayout',
    'QQuickLinearLayout',
    'QQuickStackLayoutAttached',
    'QQuickColumnLayout',
    'QQuickRowLayout',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_layout_style_info import QQuickLayoutStyleInfo
  from ._q_quick_grid_layout_engine import QQuickGridLayoutEngine
  from ._q_quick_grid_layout_item import QQuickGridLayoutItem
  from ._q_quick_layout_item_proxy import QQuickLayoutItemProxy
  from ._q_quick_layout_item_proxy_private import QQuickLayoutItemProxyPrivate
  from ._q_quick_layout_private import QQuickLayoutPrivate
  from ._q_quick_grid_layout_base_private import QQuickGridLayoutBasePrivate
  from ._q_quick_layout import QQuickLayout
  from ._q_quick_layout_attached import QQuickLayoutAttached
  from ._q_quick_layout_item_proxy_attached_data import QQuickLayoutItemProxyAttachedData
  from ._q_quick_stack_layout_private import QQuickStackLayoutPrivate
  from ._q_quick_flexbox_layout import QQuickFlexboxLayout
  from ._q_quick_grid_layout_base import QQuickGridLayoutBase
  from ._q_quick_grid_layout_private import QQuickGridLayoutPrivate
  from ._q_quick_linear_layout_private import QQuickLinearLayoutPrivate
  from ._q_quick_stack_layout import QQuickStackLayout
  from ._q_quick_flexbox_layout_attached import QQuickFlexboxLayoutAttached
  from ._q_quick_grid_layout import QQuickGridLayout
  from ._q_quick_linear_layout import QQuickLinearLayout
  from ._q_quick_stack_layout_attached import QQuickStackLayoutAttached
  from ._q_quick_column_layout import QQuickColumnLayout
  from ._q_quick_row_layout import QQuickRowLayout
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickLayoutStyleInfo': '_q_quick_layout_style_info',
      'QQuickGridLayoutEngine': '_q_quick_grid_layout_engine',
      'QQuickGridLayoutItem': '_q_quick_grid_layout_item',
      'QQuickLayoutItemProxy': '_q_quick_layout_item_proxy',
      'QQuickLayoutItemProxyPrivate': '_q_quick_layout_item_proxy_private',
      'QQuickLayoutPrivate': '_q_quick_layout_private',
      'QQuickGridLayoutBasePrivate': '_q_quick_grid_layout_base_private',
      'QQuickLayout': '_q_quick_layout',
      'QQuickLayoutAttached': '_q_quick_layout_attached',
      'QQuickLayoutItemProxyAttachedData': '_q_quick_layout_item_proxy_attached_data',
      'QQuickStackLayoutPrivate': '_q_quick_stack_layout_private',
      'QQuickFlexboxLayout': '_q_quick_flexbox_layout',
      'QQuickGridLayoutBase': '_q_quick_grid_layout_base',
      'QQuickGridLayoutPrivate': '_q_quick_grid_layout_private',
      'QQuickLinearLayoutPrivate': '_q_quick_linear_layout_private',
      'QQuickStackLayout': '_q_quick_stack_layout',
      'QQuickFlexboxLayoutAttached': '_q_quick_flexbox_layout_attached',
      'QQuickGridLayout': '_q_quick_grid_layout',
      'QQuickLinearLayout': '_q_quick_linear_layout',
      'QQuickStackLayoutAttached': '_q_quick_stack_layout_attached',
      'QQuickColumnLayout': '_q_quick_column_layout',
      'QQuickRowLayout': '_q_quick_row_layout',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickLayouts import QQuickRowLayout'. Python calls
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
