"""
The 'cutienator.QtQuickShapes' package provides the cute classes of the
part of Qt named QtQuickShapes, under the name PySide6 has for it.

  from cutienator.QtQuickShapes import QQuickShapeStrokeFillParams, QQuickShapesModule

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
    'QQuickShapeStrokeFillParams',
    'QQuickShapesModule',
    'QQuickShapeGenericNode',
    'QQuickShapeCurveRunnable',
    'QQuickShapeFillRunnable',
    'QQuickShapeStrokeRunnable',
    'QQuickShapeTrim',
    'QQuickShapeGradient',
    'QQuickShapeConicalGradient',
    'QQuickShapeLinearGradient',
    'QQuickShapeRadialGradient',
    'QQuickShape',
    'QQuickShapePrivate',
    'QQuickShapePath',
    'QQuickAbstractPathRenderer',
    'QQuickShapePathPrivate',
    'QQuickShapeSoftwareRenderNode',
    'QQuickShapeConicalGradientRhiShader',
    'QQuickShapeCurveRenderer',
    'QQuickShapeGenericStrokeFillNode',
    'QQuickShapeLinearGradientRhiShader',
    'QQuickShapeRadialGradientRhiShader',
    'QQuickShapeSoftwareRenderer',
    'QQuickShapeTextureFillRhiShader',
    'QQuickShapeConicalGradientMaterial',
    'QQuickShapeGenericMaterialFactory',
    'QQuickShapeGenericRenderer',
    'QQuickShapeLinearGradientMaterial',
    'QQuickShapeRadialGradientMaterial',
    'QQuickShapeTextureFillMaterial',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_shape_stroke_fill_params import QQuickShapeStrokeFillParams
  from ._q_quick_shapes_module import QQuickShapesModule
  from ._q_quick_shape_generic_node import QQuickShapeGenericNode
  from ._q_quick_shape_curve_runnable import QQuickShapeCurveRunnable
  from ._q_quick_shape_fill_runnable import QQuickShapeFillRunnable
  from ._q_quick_shape_stroke_runnable import QQuickShapeStrokeRunnable
  from ._q_quick_shape_trim import QQuickShapeTrim
  from ._q_quick_shape_gradient import QQuickShapeGradient
  from ._q_quick_shape_conical_gradient import QQuickShapeConicalGradient
  from ._q_quick_shape_linear_gradient import QQuickShapeLinearGradient
  from ._q_quick_shape_radial_gradient import QQuickShapeRadialGradient
  from ._q_quick_shape import QQuickShape
  from ._q_quick_shape_private import QQuickShapePrivate
  from ._q_quick_shape_path import QQuickShapePath
  from ._q_quick_abstract_path_renderer import QQuickAbstractPathRenderer
  from ._q_quick_shape_path_private import QQuickShapePathPrivate
  from ._q_quick_shape_software_render_node import QQuickShapeSoftwareRenderNode
  from ._q_quick_shape_conical_gradient_rhi_shader import QQuickShapeConicalGradientRhiShader
  from ._q_quick_shape_curve_renderer import QQuickShapeCurveRenderer
  from ._q_quick_shape_generic_stroke_fill_node import QQuickShapeGenericStrokeFillNode
  from ._q_quick_shape_linear_gradient_rhi_shader import QQuickShapeLinearGradientRhiShader
  from ._q_quick_shape_radial_gradient_rhi_shader import QQuickShapeRadialGradientRhiShader
  from ._q_quick_shape_software_renderer import QQuickShapeSoftwareRenderer
  from ._q_quick_shape_texture_fill_rhi_shader import QQuickShapeTextureFillRhiShader
  from ._q_quick_shape_conical_gradient_material import QQuickShapeConicalGradientMaterial
  from ._q_quick_shape_generic_material_factory import QQuickShapeGenericMaterialFactory
  from ._q_quick_shape_generic_renderer import QQuickShapeGenericRenderer
  from ._q_quick_shape_linear_gradient_material import QQuickShapeLinearGradientMaterial
  from ._q_quick_shape_radial_gradient_material import QQuickShapeRadialGradientMaterial
  from ._q_quick_shape_texture_fill_material import QQuickShapeTextureFillMaterial
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickShapeStrokeFillParams': '_q_quick_shape_stroke_fill_params',
      'QQuickShapesModule': '_q_quick_shapes_module',
      'QQuickShapeGenericNode': '_q_quick_shape_generic_node',
      'QQuickShapeCurveRunnable': '_q_quick_shape_curve_runnable',
      'QQuickShapeFillRunnable': '_q_quick_shape_fill_runnable',
      'QQuickShapeStrokeRunnable': '_q_quick_shape_stroke_runnable',
      'QQuickShapeTrim': '_q_quick_shape_trim',
      'QQuickShapeGradient': '_q_quick_shape_gradient',
      'QQuickShapeConicalGradient': '_q_quick_shape_conical_gradient',
      'QQuickShapeLinearGradient': '_q_quick_shape_linear_gradient',
      'QQuickShapeRadialGradient': '_q_quick_shape_radial_gradient',
      'QQuickShape': '_q_quick_shape',
      'QQuickShapePrivate': '_q_quick_shape_private',
      'QQuickShapePath': '_q_quick_shape_path',
      'QQuickAbstractPathRenderer': '_q_quick_abstract_path_renderer',
      'QQuickShapePathPrivate': '_q_quick_shape_path_private',
      'QQuickShapeSoftwareRenderNode': '_q_quick_shape_software_render_node',
      'QQuickShapeConicalGradientRhiShader': '_q_quick_shape_conical_gradient_rhi_shader',
      'QQuickShapeCurveRenderer': '_q_quick_shape_curve_renderer',
      'QQuickShapeGenericStrokeFillNode': '_q_quick_shape_generic_stroke_fill_node',
      'QQuickShapeLinearGradientRhiShader': '_q_quick_shape_linear_gradient_rhi_shader',
      'QQuickShapeRadialGradientRhiShader': '_q_quick_shape_radial_gradient_rhi_shader',
      'QQuickShapeSoftwareRenderer': '_q_quick_shape_software_renderer',
      'QQuickShapeTextureFillRhiShader': '_q_quick_shape_texture_fill_rhi_shader',
      'QQuickShapeConicalGradientMaterial': '_q_quick_shape_conical_gradient_material',
      'QQuickShapeGenericMaterialFactory': '_q_quick_shape_generic_material_factory',
      'QQuickShapeGenericRenderer': '_q_quick_shape_generic_renderer',
      'QQuickShapeLinearGradientMaterial': '_q_quick_shape_linear_gradient_material',
      'QQuickShapeRadialGradientMaterial': '_q_quick_shape_radial_gradient_material',
      'QQuickShapeTextureFillMaterial': '_q_quick_shape_texture_fill_material',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickShapes import QQuickShapeTextureFillMaterial'. Python calls
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
