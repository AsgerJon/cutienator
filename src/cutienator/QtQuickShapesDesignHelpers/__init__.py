"""
The 'cutienator.QtQuickShapesDesignHelpers' package provides the cute
classes of the part of Qt named QtQuickShapesDesignHelpers, under the
name PySide6 has for it.

  from cutienator.QtQuickShapesDesignHelpers import QQuickEllipseShape, QQuickEllipseShapePrivate

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
    'QQuickEllipseShape',
    'QQuickEllipseShapePrivate',
    'QQuickRectangleShape',
    'QQuickRegularPolygonShape',
    'QQuickRegularPolygonShapePrivate',
    'QQuickStarShape',
    'QQuickStarShapePrivate',
    'QQuickRectangleShapePrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_ellipse_shape import QQuickEllipseShape
  from ._q_quick_ellipse_shape_private import QQuickEllipseShapePrivate
  from ._q_quick_rectangle_shape import QQuickRectangleShape
  from ._q_quick_regular_polygon_shape import QQuickRegularPolygonShape
  from ._q_quick_regular_polygon_shape_private import QQuickRegularPolygonShapePrivate
  from ._q_quick_star_shape import QQuickStarShape
  from ._q_quick_star_shape_private import QQuickStarShapePrivate
  from ._q_quick_rectangle_shape_private import QQuickRectangleShapePrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickEllipseShape': '_q_quick_ellipse_shape',
      'QQuickEllipseShapePrivate': '_q_quick_ellipse_shape_private',
      'QQuickRectangleShape': '_q_quick_rectangle_shape',
      'QQuickRegularPolygonShape': '_q_quick_regular_polygon_shape',
      'QQuickRegularPolygonShapePrivate': '_q_quick_regular_polygon_shape_private',
      'QQuickStarShape': '_q_quick_star_shape',
      'QQuickStarShapePrivate': '_q_quick_star_shape_private',
      'QQuickRectangleShapePrivate': '_q_quick_rectangle_shape_private',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickShapesDesignHelpers import QQuickRectangleShapePrivate'. Python calls
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
