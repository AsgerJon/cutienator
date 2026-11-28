"""
The 'cutienator.QtCanvasPainter' package provides the cute classes of
the part of Qt named QtCanvasPainter, under the name PySide6 has for it.

  from cutienator.QtCanvasPainter import QCCachedPath, QCCachedPathFillProperties

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
    'QCCachedPath',
    'QCCachedPathFillProperties',
    'QCCachedPathStrokeProperties',
    'QCClip',
    'QCColor',
    'QCContext',
    'QCDebugCounters',
    'QCPaint',
    'QCPath',
    'QCPoint',
    'QCRHITexture',
    'QCRhiCachedPathDrawArgs',
    'QCRhiCanvas',
    'QCRhiCanvasGrab',
    'QCRhiUncachedPathDrawArgs',
    'QCState',
    'QCVertex',
    'QCanvasGradientStop',
    'QCAreaAllocator',
    'QCanvasBrush',
    'QCanvasImage',
    'QCanvasOffscreenCanvas',
    'QCanvasGradient',
    'QCanvasImagePrivate',
    'QCanvasImageTracker',
    'QCanvasBoxGradient',
    'QCanvasConicalGradient',
    'QCanvasLinearGradient',
    'QCanvasRadialGradient',
    'QCRhiDistanceFieldGlyphCache',
    'QCanvasBoxShadow',
    'QCanvasPainter',
    'QCanvasBrushPrivate',
    'QCanvasBoxShadowPrivate',
    'QCanvasPath',
    'QCanvasPainterFactory',
    'QCanvasRhiPaintDriver',
    'QCDistanceFieldGlyphCache',
    'QCRhiColorGlyphCache',
    'QCTextLayout',
    'QCanvasCustomBrush',
    'QCanvasCustomBrushPrivate',
    'QCanvasGradientBrushPrivate',
    'QCanvasGridPattern',
    'QCanvasGridPatternPrivate',
    'QCanvasImagePattern',
    'QCanvasImagePatternPrivate',
    'QCanvasPainterPrivate',
    'QCPainterRhiRenderer',
    'QCanvasBoxGradientBrushPrivate',
    'QCanvasConicalGradientBrushPrivate',
    'QCanvasLinearGradientBrushPrivate',
    'QCanvasRadialGradientBrushPrivate',
    'QCPainterEngine',
    'QCanvasPainterItemPrivate',
    'QCanvasPainterItem',
    'QCanvasPainterItemRenderer',
    'QCanvasPainterWidget',
    'QCanvasGradientStops',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_c_cached_path import QCCachedPath
  from ._q_c_cached_path_fill_properties import QCCachedPathFillProperties
  from ._q_c_cached_path_stroke_properties import QCCachedPathStrokeProperties
  from ._q_c_clip import QCClip
  from ._q_c_color import QCColor
  from ._q_c_context import QCContext
  from ._q_c_debug_counters import QCDebugCounters
  from ._q_c_paint import QCPaint
  from ._q_c_path import QCPath
  from ._q_c_point import QCPoint
  from ._q_c_r_h_i_texture import QCRHITexture
  from ._q_c_rhi_cached_path_draw_args import QCRhiCachedPathDrawArgs
  from ._q_c_rhi_canvas import QCRhiCanvas
  from ._q_c_rhi_canvas_grab import QCRhiCanvasGrab
  from ._q_c_rhi_uncached_path_draw_args import QCRhiUncachedPathDrawArgs
  from ._q_c_state import QCState
  from ._q_c_vertex import QCVertex
  from ._q_canvas_gradient_stop import QCanvasGradientStop
  from ._q_c_area_allocator import QCAreaAllocator
  from ._q_canvas_brush import QCanvasBrush
  from ._q_canvas_image import QCanvasImage
  from ._q_canvas_offscreen_canvas import QCanvasOffscreenCanvas
  from ._q_canvas_gradient import QCanvasGradient
  from ._q_canvas_image_private import QCanvasImagePrivate
  from ._q_canvas_image_tracker import QCanvasImageTracker
  from ._q_canvas_box_gradient import QCanvasBoxGradient
  from ._q_canvas_conical_gradient import QCanvasConicalGradient
  from ._q_canvas_linear_gradient import QCanvasLinearGradient
  from ._q_canvas_radial_gradient import QCanvasRadialGradient
  from ._q_c_rhi_distance_field_glyph_cache import QCRhiDistanceFieldGlyphCache
  from ._q_canvas_box_shadow import QCanvasBoxShadow
  from ._q_canvas_painter import QCanvasPainter
  from ._q_canvas_brush_private import QCanvasBrushPrivate
  from ._q_canvas_box_shadow_private import QCanvasBoxShadowPrivate
  from ._q_canvas_path import QCanvasPath
  from ._q_canvas_painter_factory import QCanvasPainterFactory
  from ._q_canvas_rhi_paint_driver import QCanvasRhiPaintDriver
  from ._q_c_distance_field_glyph_cache import QCDistanceFieldGlyphCache
  from ._q_c_rhi_color_glyph_cache import QCRhiColorGlyphCache
  from ._q_c_text_layout import QCTextLayout
  from ._q_canvas_custom_brush import QCanvasCustomBrush
  from ._q_canvas_custom_brush_private import QCanvasCustomBrushPrivate
  from ._q_canvas_gradient_brush_private import QCanvasGradientBrushPrivate
  from ._q_canvas_grid_pattern import QCanvasGridPattern
  from ._q_canvas_grid_pattern_private import QCanvasGridPatternPrivate
  from ._q_canvas_image_pattern import QCanvasImagePattern
  from ._q_canvas_image_pattern_private import QCanvasImagePatternPrivate
  from ._q_canvas_painter_private import QCanvasPainterPrivate
  from ._q_c_painter_rhi_renderer import QCPainterRhiRenderer
  from ._q_canvas_box_gradient_brush_private import QCanvasBoxGradientBrushPrivate
  from ._q_canvas_conical_gradient_brush_private import QCanvasConicalGradientBrushPrivate
  from ._q_canvas_linear_gradient_brush_private import QCanvasLinearGradientBrushPrivate
  from ._q_canvas_radial_gradient_brush_private import QCanvasRadialGradientBrushPrivate
  from ._q_c_painter_engine import QCPainterEngine
  from ._q_canvas_painter_item_private import QCanvasPainterItemPrivate
  from ._q_canvas_painter_item import QCanvasPainterItem
  from ._q_canvas_painter_item_renderer import QCanvasPainterItemRenderer
  from ._q_canvas_painter_widget import QCanvasPainterWidget
  from ._q_canvas_gradient_stop import QCanvasGradientStops
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QCCachedPath': '_q_c_cached_path',
      'QCCachedPathFillProperties': '_q_c_cached_path_fill_properties',
      'QCCachedPathStrokeProperties': '_q_c_cached_path_stroke_properties',
      'QCClip': '_q_c_clip',
      'QCColor': '_q_c_color',
      'QCContext': '_q_c_context',
      'QCDebugCounters': '_q_c_debug_counters',
      'QCPaint': '_q_c_paint',
      'QCPath': '_q_c_path',
      'QCPoint': '_q_c_point',
      'QCRHITexture': '_q_c_r_h_i_texture',
      'QCRhiCachedPathDrawArgs': '_q_c_rhi_cached_path_draw_args',
      'QCRhiCanvas': '_q_c_rhi_canvas',
      'QCRhiCanvasGrab': '_q_c_rhi_canvas_grab',
      'QCRhiUncachedPathDrawArgs': '_q_c_rhi_uncached_path_draw_args',
      'QCState': '_q_c_state',
      'QCVertex': '_q_c_vertex',
      'QCanvasGradientStop': '_q_canvas_gradient_stop',
      'QCAreaAllocator': '_q_c_area_allocator',
      'QCanvasBrush': '_q_canvas_brush',
      'QCanvasImage': '_q_canvas_image',
      'QCanvasOffscreenCanvas': '_q_canvas_offscreen_canvas',
      'QCanvasGradient': '_q_canvas_gradient',
      'QCanvasImagePrivate': '_q_canvas_image_private',
      'QCanvasImageTracker': '_q_canvas_image_tracker',
      'QCanvasBoxGradient': '_q_canvas_box_gradient',
      'QCanvasConicalGradient': '_q_canvas_conical_gradient',
      'QCanvasLinearGradient': '_q_canvas_linear_gradient',
      'QCanvasRadialGradient': '_q_canvas_radial_gradient',
      'QCRhiDistanceFieldGlyphCache': '_q_c_rhi_distance_field_glyph_cache',
      'QCanvasBoxShadow': '_q_canvas_box_shadow',
      'QCanvasPainter': '_q_canvas_painter',
      'QCanvasBrushPrivate': '_q_canvas_brush_private',
      'QCanvasBoxShadowPrivate': '_q_canvas_box_shadow_private',
      'QCanvasPath': '_q_canvas_path',
      'QCanvasPainterFactory': '_q_canvas_painter_factory',
      'QCanvasRhiPaintDriver': '_q_canvas_rhi_paint_driver',
      'QCDistanceFieldGlyphCache': '_q_c_distance_field_glyph_cache',
      'QCRhiColorGlyphCache': '_q_c_rhi_color_glyph_cache',
      'QCTextLayout': '_q_c_text_layout',
      'QCanvasCustomBrush': '_q_canvas_custom_brush',
      'QCanvasCustomBrushPrivate': '_q_canvas_custom_brush_private',
      'QCanvasGradientBrushPrivate': '_q_canvas_gradient_brush_private',
      'QCanvasGridPattern': '_q_canvas_grid_pattern',
      'QCanvasGridPatternPrivate': '_q_canvas_grid_pattern_private',
      'QCanvasImagePattern': '_q_canvas_image_pattern',
      'QCanvasImagePatternPrivate': '_q_canvas_image_pattern_private',
      'QCanvasPainterPrivate': '_q_canvas_painter_private',
      'QCPainterRhiRenderer': '_q_c_painter_rhi_renderer',
      'QCanvasBoxGradientBrushPrivate': '_q_canvas_box_gradient_brush_private',
      'QCanvasConicalGradientBrushPrivate': '_q_canvas_conical_gradient_brush_private',
      'QCanvasLinearGradientBrushPrivate': '_q_canvas_linear_gradient_brush_private',
      'QCanvasRadialGradientBrushPrivate': '_q_canvas_radial_gradient_brush_private',
      'QCPainterEngine': '_q_c_painter_engine',
      'QCanvasPainterItemPrivate': '_q_canvas_painter_item_private',
      'QCanvasPainterItem': '_q_canvas_painter_item',
      'QCanvasPainterItemRenderer': '_q_canvas_painter_item_renderer',
      'QCanvasPainterWidget': '_q_canvas_painter_widget',
      'QCanvasGradientStops': '_q_canvas_gradient_stop',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtCanvasPainter import QCanvasGradientStops'. Python calls
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
