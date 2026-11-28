"""
The 'cutienator.QtLottie' package provides the cute classes of the part
of Qt named QtLottie, under the name PySide6 has for it.

  from cutienator.QtLottie import QLottieGradientHolderContent, QBezierEasing

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
    'QLottieGradientHolderContent',
    'QBezierEasing',
    'QLottieLiteral',
    'QLottieSpatialProperty',
    'QLottieBase',
    'QLottieFillEffect',
    'QLottieGFill',
    'QLottieImage',
    'QLottieLayer',
    'QLottiePrecomposition',
    'QLottieRenderer',
    'QLottieSolidLayer',
    'QLottieTextLayer',
    'QLottieShape',
    'QLottieTrimPath',
    'QLottieBasicTransform',
    'QLottieEllipse',
    'QLottieFill',
    'QLottieFreeFormShape',
    'QLottieGroup',
    'QLottiePolyStar',
    'QLottieRect',
    'QLottieRepeater',
    'QLottieRound',
    'QLottieShapeTransform',
    'QLottieStroke',
    'QLottieGStroke',
    'QLottieImageLayer',
    'QLottieNullLayer',
    'QLottiePrecompLayer',
    'QLottieRasterRenderer',
    'QLottieRepeaterTransform',
    'QLottieRoot',
    'QLottieShapeLayer',
    'QLottieAnimation',
    'QBatchRenderer',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_lottie_gradient_holder_content import QLottieGradientHolderContent
  from ._q_bezier_easing import QBezierEasing
  from ._q_lottie_literal import QLottieLiteral
  from ._q_lottie_spatial_property import QLottieSpatialProperty
  from ._q_lottie_base import QLottieBase
  from ._q_lottie_fill_effect import QLottieFillEffect
  from ._q_lottie_g_fill import QLottieGFill
  from ._q_lottie_image import QLottieImage
  from ._q_lottie_layer import QLottieLayer
  from ._q_lottie_precomposition import QLottiePrecomposition
  from ._q_lottie_renderer import QLottieRenderer
  from ._q_lottie_solid_layer import QLottieSolidLayer
  from ._q_lottie_text_layer import QLottieTextLayer
  from ._q_lottie_shape import QLottieShape
  from ._q_lottie_trim_path import QLottieTrimPath
  from ._q_lottie_basic_transform import QLottieBasicTransform
  from ._q_lottie_ellipse import QLottieEllipse
  from ._q_lottie_fill import QLottieFill
  from ._q_lottie_free_form_shape import QLottieFreeFormShape
  from ._q_lottie_group import QLottieGroup
  from ._q_lottie_poly_star import QLottiePolyStar
  from ._q_lottie_rect import QLottieRect
  from ._q_lottie_repeater import QLottieRepeater
  from ._q_lottie_round import QLottieRound
  from ._q_lottie_shape_transform import QLottieShapeTransform
  from ._q_lottie_stroke import QLottieStroke
  from ._q_lottie_g_stroke import QLottieGStroke
  from ._q_lottie_image_layer import QLottieImageLayer
  from ._q_lottie_null_layer import QLottieNullLayer
  from ._q_lottie_precomp_layer import QLottiePrecompLayer
  from ._q_lottie_raster_renderer import QLottieRasterRenderer
  from ._q_lottie_repeater_transform import QLottieRepeaterTransform
  from ._q_lottie_root import QLottieRoot
  from ._q_lottie_shape_layer import QLottieShapeLayer
  from ._q_lottie_animation import QLottieAnimation
  from ._q_batch_renderer import QBatchRenderer
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QLottieGradientHolderContent': '_q_lottie_gradient_holder_content',
      'QBezierEasing': '_q_bezier_easing',
      'QLottieLiteral': '_q_lottie_literal',
      'QLottieSpatialProperty': '_q_lottie_spatial_property',
      'QLottieBase': '_q_lottie_base',
      'QLottieFillEffect': '_q_lottie_fill_effect',
      'QLottieGFill': '_q_lottie_g_fill',
      'QLottieImage': '_q_lottie_image',
      'QLottieLayer': '_q_lottie_layer',
      'QLottiePrecomposition': '_q_lottie_precomposition',
      'QLottieRenderer': '_q_lottie_renderer',
      'QLottieSolidLayer': '_q_lottie_solid_layer',
      'QLottieTextLayer': '_q_lottie_text_layer',
      'QLottieShape': '_q_lottie_shape',
      'QLottieTrimPath': '_q_lottie_trim_path',
      'QLottieBasicTransform': '_q_lottie_basic_transform',
      'QLottieEllipse': '_q_lottie_ellipse',
      'QLottieFill': '_q_lottie_fill',
      'QLottieFreeFormShape': '_q_lottie_free_form_shape',
      'QLottieGroup': '_q_lottie_group',
      'QLottiePolyStar': '_q_lottie_poly_star',
      'QLottieRect': '_q_lottie_rect',
      'QLottieRepeater': '_q_lottie_repeater',
      'QLottieRound': '_q_lottie_round',
      'QLottieShapeTransform': '_q_lottie_shape_transform',
      'QLottieStroke': '_q_lottie_stroke',
      'QLottieGStroke': '_q_lottie_g_stroke',
      'QLottieImageLayer': '_q_lottie_image_layer',
      'QLottieNullLayer': '_q_lottie_null_layer',
      'QLottiePrecompLayer': '_q_lottie_precomp_layer',
      'QLottieRasterRenderer': '_q_lottie_raster_renderer',
      'QLottieRepeaterTransform': '_q_lottie_repeater_transform',
      'QLottieRoot': '_q_lottie_root',
      'QLottieShapeLayer': '_q_lottie_shape_layer',
      'QLottieAnimation': '_q_lottie_animation',
      'QBatchRenderer': '_q_batch_renderer',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtLottie import QBatchRenderer'. Python calls
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
