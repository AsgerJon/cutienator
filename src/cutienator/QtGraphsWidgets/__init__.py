"""
The 'cutienator.QtGraphsWidgets' package provides the cute classes of
the part of Qt named QtGraphsWidgets, under the name PySide6 has for it.

  from cutienator.QtGraphsWidgets import Q3DGraphsWidgetItemPrivate, Q3DBarsWidgetItemPrivate

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
    'Q3DGraphsWidgetItemPrivate',
    'Q3DBarsWidgetItemPrivate',
    'Q3DScatterWidgetItemPrivate',
    'Q3DSurfaceWidgetItemPrivate',
    'Q3DGraphsWidgetItem',
    'Q3DBarsWidgetItem',
    'Q3DScatterWidgetItem',
    'Q3DSurfaceWidgetItem',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q3_d_graphs_widget_item_private import Q3DGraphsWidgetItemPrivate
  from ._q3_d_bars_widget_item_private import Q3DBarsWidgetItemPrivate
  from ._q3_d_scatter_widget_item_private import Q3DScatterWidgetItemPrivate
  from ._q3_d_surface_widget_item_private import Q3DSurfaceWidgetItemPrivate
  from ._q3_d_graphs_widget_item import Q3DGraphsWidgetItem
  from ._q3_d_bars_widget_item import Q3DBarsWidgetItem
  from ._q3_d_scatter_widget_item import Q3DScatterWidgetItem
  from ._q3_d_surface_widget_item import Q3DSurfaceWidgetItem
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Q3DGraphsWidgetItemPrivate': '_q3_d_graphs_widget_item_private',
      'Q3DBarsWidgetItemPrivate': '_q3_d_bars_widget_item_private',
      'Q3DScatterWidgetItemPrivate': '_q3_d_scatter_widget_item_private',
      'Q3DSurfaceWidgetItemPrivate': '_q3_d_surface_widget_item_private',
      'Q3DGraphsWidgetItem': '_q3_d_graphs_widget_item',
      'Q3DBarsWidgetItem': '_q3_d_bars_widget_item',
      'Q3DScatterWidgetItem': '_q3_d_scatter_widget_item',
      'Q3DSurfaceWidgetItem': '_q3_d_surface_widget_item',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtGraphsWidgets import Q3DSurfaceWidgetItem'. Python calls
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
