"""
The 'cutienator.QtSvg' package provides the cute classes of the part of
Qt named QtSvg, under the name PySide6 has for it.

  from cutienator.QtSvg import QSvgAnimationProperty, QSvgEasingInterface

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
    'QSvgAnimationProperty',
    'QSvgEasingInterface',
    'QSvgOffsetProperty',
    'QSvgStyleState',
    'QSvgCssEasing',
    'QSvgLinearEasing',
    'QSvgCssCubicBezierEasing',
    'QSvgCssStepsEasing',
    'QSvgAbstractAnimatedProperty',
    'QSvgAbstractAnimation',
    'QSvgAnimatedPropertyColor',
    'QSvgAnimatedPropertyFloat',
    'QSvgAnimatedPropertyTransform',
    'QSvgCssProperties',
    'QSvgRectF',
    'QSvgCssAnimation',
    'QSvgExtraStates',
    'QSvgNode',
    'QSvgStyleProperty',
    'QSvgStructureNode',
    'QSvgDocument',
    'QSvgGenerator',
    'QSvgGlyph',
    'QSvgRenderer',
    'QSvgAbstractAnimator',
    'QSvgAnimateNode',
    'QSvgAnimatedStyle',
    'QSvgCompOpStyle',
    'QSvgDefs',
    'QSvgDummyNode',
    'QSvgEllipse',
    'QSvgFeFilterPrimitive',
    'QSvgFillStyle',
    'QSvgFilterContainer',
    'QSvgFont',
    'QSvgFontStyle',
    'QSvgG',
    'QSvgHandler',
    'QSvgImage',
    'QSvgLine',
    'QSvgMask',
    'QSvgOffsetStyle',
    'QSvgOpacityStyle',
    'QSvgPaintServer',
    'QSvgPath',
    'QSvgPattern',
    'QSvgPolygon',
    'QSvgPolyline',
    'QSvgQualityStyle',
    'QSvgRect',
    'QSvgStaticStyle',
    'QSvgStrokeStyle',
    'QSvgStyleSelector',
    'QSvgSwitch',
    'QSvgSymbolLike',
    'QSvgText',
    'QSvgTspan',
    'QSvgTransformStyle',
    'QSvgUse',
    'QSvgVideo',
    'QSvgViewportFillStyle',
    'QSvgAnimateColor',
    'QSvgAnimateTransform',
    'QSvgAnimationController',
    'QSvgAnimator',
    'QSvgCircle',
    'QSvgCssHandler',
    'QSvgFeBlend',
    'QSvgFeColorMatrix',
    'QSvgFeComposite',
    'QSvgFeFlood',
    'QSvgFeGaussianBlur',
    'QSvgFeMerge',
    'QSvgFeMergeNode',
    'QSvgFeOffset',
    'QSvgFeUnsupported',
    'QSvgGradientPaint',
    'QSvgMarker',
    'QSvgPatternPaint',
    'QSvgSolidColorPaint',
    'QSvgSymbol',
    'QSvgVisitor',
    'QSvgCssValues',
    'QtSvg',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_svg_animation_property import QSvgAnimationProperty
  from ._q_svg_easing_interface import QSvgEasingInterface
  from ._q_svg_offset_property import QSvgOffsetProperty
  from ._q_svg_style_state import QSvgStyleState
  from ._q_svg_css_easing import QSvgCssEasing
  from ._q_svg_linear_easing import QSvgLinearEasing
  from ._q_svg_css_cubic_bezier_easing import QSvgCssCubicBezierEasing
  from ._q_svg_css_steps_easing import QSvgCssStepsEasing
  from ._q_svg_abstract_animated_property import QSvgAbstractAnimatedProperty
  from ._q_svg_abstract_animation import QSvgAbstractAnimation
  from ._q_svg_animated_property_color import QSvgAnimatedPropertyColor
  from ._q_svg_animated_property_float import QSvgAnimatedPropertyFloat
  from ._q_svg_animated_property_transform import QSvgAnimatedPropertyTransform
  from ._q_svg_css_properties import QSvgCssProperties
  from ._q_svg_rect_f import QSvgRectF
  from ._q_svg_css_animation import QSvgCssAnimation
  from ._q_svg_extra_states import QSvgExtraStates
  from ._q_svg_node import QSvgNode
  from ._q_svg_style_property import QSvgStyleProperty
  from ._q_svg_structure_node import QSvgStructureNode
  from ._q_svg_document import QSvgDocument
  from ._q_svg_generator import QSvgGenerator
  from ._q_svg_glyph import QSvgGlyph
  from ._q_svg_renderer import QSvgRenderer
  from ._q_svg_abstract_animator import QSvgAbstractAnimator
  from ._q_svg_animate_node import QSvgAnimateNode
  from ._q_svg_animated_style import QSvgAnimatedStyle
  from ._q_svg_comp_op_style import QSvgCompOpStyle
  from ._q_svg_defs import QSvgDefs
  from ._q_svg_dummy_node import QSvgDummyNode
  from ._q_svg_ellipse import QSvgEllipse
  from ._q_svg_fe_filter_primitive import QSvgFeFilterPrimitive
  from ._q_svg_fill_style import QSvgFillStyle
  from ._q_svg_filter_container import QSvgFilterContainer
  from ._q_svg_font import QSvgFont
  from ._q_svg_font_style import QSvgFontStyle
  from ._q_svg_g import QSvgG
  from ._q_svg_handler import QSvgHandler
  from ._q_svg_image import QSvgImage
  from ._q_svg_line import QSvgLine
  from ._q_svg_mask import QSvgMask
  from ._q_svg_offset_style import QSvgOffsetStyle
  from ._q_svg_opacity_style import QSvgOpacityStyle
  from ._q_svg_paint_server import QSvgPaintServer
  from ._q_svg_path import QSvgPath
  from ._q_svg_pattern import QSvgPattern
  from ._q_svg_polygon import QSvgPolygon
  from ._q_svg_polyline import QSvgPolyline
  from ._q_svg_quality_style import QSvgQualityStyle
  from ._q_svg_rect import QSvgRect
  from ._q_svg_static_style import QSvgStaticStyle
  from ._q_svg_stroke_style import QSvgStrokeStyle
  from ._q_svg_style_selector import QSvgStyleSelector
  from ._q_svg_switch import QSvgSwitch
  from ._q_svg_symbol_like import QSvgSymbolLike
  from ._q_svg_text import QSvgText
  from ._q_svg_tspan import QSvgTspan
  from ._q_svg_transform_style import QSvgTransformStyle
  from ._q_svg_use import QSvgUse
  from ._q_svg_video import QSvgVideo
  from ._q_svg_viewport_fill_style import QSvgViewportFillStyle
  from ._q_svg_animate_color import QSvgAnimateColor
  from ._q_svg_animate_transform import QSvgAnimateTransform
  from ._q_svg_animation_controller import QSvgAnimationController
  from ._q_svg_animator import QSvgAnimator
  from ._q_svg_circle import QSvgCircle
  from ._q_svg_css_handler import QSvgCssHandler
  from ._q_svg_fe_blend import QSvgFeBlend
  from ._q_svg_fe_color_matrix import QSvgFeColorMatrix
  from ._q_svg_fe_composite import QSvgFeComposite
  from ._q_svg_fe_flood import QSvgFeFlood
  from ._q_svg_fe_gaussian_blur import QSvgFeGaussianBlur
  from ._q_svg_fe_merge import QSvgFeMerge
  from ._q_svg_fe_merge_node import QSvgFeMergeNode
  from ._q_svg_fe_offset import QSvgFeOffset
  from ._q_svg_fe_unsupported import QSvgFeUnsupported
  from ._q_svg_gradient_paint import QSvgGradientPaint
  from ._q_svg_marker import QSvgMarker
  from ._q_svg_pattern_paint import QSvgPatternPaint
  from ._q_svg_solid_color_paint import QSvgSolidColorPaint
  from ._q_svg_symbol import QSvgSymbol
  from ._q_svg_visitor import QSvgVisitor
  from . import QSvgCssValues
  from . import QtSvg
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QSvgAnimationProperty': '_q_svg_animation_property',
      'QSvgEasingInterface': '_q_svg_easing_interface',
      'QSvgOffsetProperty': '_q_svg_offset_property',
      'QSvgStyleState': '_q_svg_style_state',
      'QSvgCssEasing': '_q_svg_css_easing',
      'QSvgLinearEasing': '_q_svg_linear_easing',
      'QSvgCssCubicBezierEasing': '_q_svg_css_cubic_bezier_easing',
      'QSvgCssStepsEasing': '_q_svg_css_steps_easing',
      'QSvgAbstractAnimatedProperty': '_q_svg_abstract_animated_property',
      'QSvgAbstractAnimation': '_q_svg_abstract_animation',
      'QSvgAnimatedPropertyColor': '_q_svg_animated_property_color',
      'QSvgAnimatedPropertyFloat': '_q_svg_animated_property_float',
      'QSvgAnimatedPropertyTransform': '_q_svg_animated_property_transform',
      'QSvgCssProperties': '_q_svg_css_properties',
      'QSvgRectF': '_q_svg_rect_f',
      'QSvgCssAnimation': '_q_svg_css_animation',
      'QSvgExtraStates': '_q_svg_extra_states',
      'QSvgNode': '_q_svg_node',
      'QSvgStyleProperty': '_q_svg_style_property',
      'QSvgStructureNode': '_q_svg_structure_node',
      'QSvgDocument': '_q_svg_document',
      'QSvgGenerator': '_q_svg_generator',
      'QSvgGlyph': '_q_svg_glyph',
      'QSvgRenderer': '_q_svg_renderer',
      'QSvgAbstractAnimator': '_q_svg_abstract_animator',
      'QSvgAnimateNode': '_q_svg_animate_node',
      'QSvgAnimatedStyle': '_q_svg_animated_style',
      'QSvgCompOpStyle': '_q_svg_comp_op_style',
      'QSvgDefs': '_q_svg_defs',
      'QSvgDummyNode': '_q_svg_dummy_node',
      'QSvgEllipse': '_q_svg_ellipse',
      'QSvgFeFilterPrimitive': '_q_svg_fe_filter_primitive',
      'QSvgFillStyle': '_q_svg_fill_style',
      'QSvgFilterContainer': '_q_svg_filter_container',
      'QSvgFont': '_q_svg_font',
      'QSvgFontStyle': '_q_svg_font_style',
      'QSvgG': '_q_svg_g',
      'QSvgHandler': '_q_svg_handler',
      'QSvgImage': '_q_svg_image',
      'QSvgLine': '_q_svg_line',
      'QSvgMask': '_q_svg_mask',
      'QSvgOffsetStyle': '_q_svg_offset_style',
      'QSvgOpacityStyle': '_q_svg_opacity_style',
      'QSvgPaintServer': '_q_svg_paint_server',
      'QSvgPath': '_q_svg_path',
      'QSvgPattern': '_q_svg_pattern',
      'QSvgPolygon': '_q_svg_polygon',
      'QSvgPolyline': '_q_svg_polyline',
      'QSvgQualityStyle': '_q_svg_quality_style',
      'QSvgRect': '_q_svg_rect',
      'QSvgStaticStyle': '_q_svg_static_style',
      'QSvgStrokeStyle': '_q_svg_stroke_style',
      'QSvgStyleSelector': '_q_svg_style_selector',
      'QSvgSwitch': '_q_svg_switch',
      'QSvgSymbolLike': '_q_svg_symbol_like',
      'QSvgText': '_q_svg_text',
      'QSvgTspan': '_q_svg_tspan',
      'QSvgTransformStyle': '_q_svg_transform_style',
      'QSvgUse': '_q_svg_use',
      'QSvgVideo': '_q_svg_video',
      'QSvgViewportFillStyle': '_q_svg_viewport_fill_style',
      'QSvgAnimateColor': '_q_svg_animate_color',
      'QSvgAnimateTransform': '_q_svg_animate_transform',
      'QSvgAnimationController': '_q_svg_animation_controller',
      'QSvgAnimator': '_q_svg_animator',
      'QSvgCircle': '_q_svg_circle',
      'QSvgCssHandler': '_q_svg_css_handler',
      'QSvgFeBlend': '_q_svg_fe_blend',
      'QSvgFeColorMatrix': '_q_svg_fe_color_matrix',
      'QSvgFeComposite': '_q_svg_fe_composite',
      'QSvgFeFlood': '_q_svg_fe_flood',
      'QSvgFeGaussianBlur': '_q_svg_fe_gaussian_blur',
      'QSvgFeMerge': '_q_svg_fe_merge',
      'QSvgFeMergeNode': '_q_svg_fe_merge_node',
      'QSvgFeOffset': '_q_svg_fe_offset',
      'QSvgFeUnsupported': '_q_svg_fe_unsupported',
      'QSvgGradientPaint': '_q_svg_gradient_paint',
      'QSvgMarker': '_q_svg_marker',
      'QSvgPatternPaint': '_q_svg_pattern_paint',
      'QSvgSolidColorPaint': '_q_svg_solid_color_paint',
      'QSvgSymbol': '_q_svg_symbol',
      'QSvgVisitor': '_q_svg_visitor',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QSvgCssValues', 'QtSvg',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtSvg import QSvgVisitor'. Python calls
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
