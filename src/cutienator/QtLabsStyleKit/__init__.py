"""
The 'cutienator.QtLabsStyleKit' package provides the cute classes of the
part of Qt named QtLabsStyleKit, under the name PySide6 has for it.

  from cutienator.QtLabsStyleKit import QQStyleKitPropertyGroupSpace, QQSK

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
    'QQStyleKitPropertyGroupSpace',
    'QQSK',
    'QQStyleKit',
    'QQStyleKitVariationAttached',
    'PropertyPathId',
    'QQStyleKitPropertyGroup',
    'QQStyleKitFont',
    'QQStyleKitPalette',
    'QQStyleKitCustomTheme',
    'QQStyleKitControlProperties',
    'QQStyleKitDelegateProperties',
    'QQStyleKitBorderProperties',
    'QQStyleKitControlState',
    'QQStyleKitDelegate',
    'QQStyleKitHandleProperties',
    'QQStyleKitIndicatorProperties',
    'QQStyleKitIndicatorWithSubTypes',
    'QQStyleKitShadowProperties',
    'QQStyleKitTextProperties',
    'QQStyleKitControl',
    'QQStyleKitControls',
    'QQStyleKitCustomControl',
    'QQStyleKitImageProperties',
    'QQStyleKitStyleAndThemeBase',
    'QQStyleKitStyle',
    'QQStyleKitTheme',
    'QQStyleKitAttached',
    'QQStyleKitReader',
    'QQStyleKitVariation',
    'QStyleKitStyle',
    'QQStyleKitDebug',
    'QQStyleKitPropertyResolver',
    'QStyleKitStylePrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_q_style_kit_property_group_space import QQStyleKitPropertyGroupSpace
  from ._q_q_s_k import QQSK
  from ._q_q_style_kit import QQStyleKit
  from ._q_q_style_kit_variation_attached import QQStyleKitVariationAttached
  from ._property_path_id import PropertyPathId
  from ._q_q_style_kit_property_group import QQStyleKitPropertyGroup
  from ._q_q_style_kit_font import QQStyleKitFont
  from ._q_q_style_kit_palette import QQStyleKitPalette
  from ._q_q_style_kit_custom_theme import QQStyleKitCustomTheme
  from ._q_q_style_kit_control_properties import QQStyleKitControlProperties
  from ._q_q_style_kit_delegate_properties import QQStyleKitDelegateProperties
  from ._q_q_style_kit_border_properties import QQStyleKitBorderProperties
  from ._q_q_style_kit_control_state import QQStyleKitControlState
  from ._q_q_style_kit_delegate import QQStyleKitDelegate
  from ._q_q_style_kit_handle_properties import QQStyleKitHandleProperties
  from ._q_q_style_kit_indicator_properties import QQStyleKitIndicatorProperties
  from ._q_q_style_kit_indicator_with_sub_types import QQStyleKitIndicatorWithSubTypes
  from ._q_q_style_kit_shadow_properties import QQStyleKitShadowProperties
  from ._q_q_style_kit_text_properties import QQStyleKitTextProperties
  from ._q_q_style_kit_control import QQStyleKitControl
  from ._q_q_style_kit_controls import QQStyleKitControls
  from ._q_q_style_kit_custom_control import QQStyleKitCustomControl
  from ._q_q_style_kit_image_properties import QQStyleKitImageProperties
  from ._q_q_style_kit_style_and_theme_base import QQStyleKitStyleAndThemeBase
  from ._q_q_style_kit_style import QQStyleKitStyle
  from ._q_q_style_kit_theme import QQStyleKitTheme
  from ._q_q_style_kit_attached import QQStyleKitAttached
  from ._q_q_style_kit_reader import QQStyleKitReader
  from ._q_q_style_kit_variation import QQStyleKitVariation
  from ._q_style_kit_style import QStyleKitStyle
  from ._q_q_style_kit_debug import QQStyleKitDebug
  from ._q_q_style_kit_property_resolver import QQStyleKitPropertyResolver
  from ._q_style_kit_style_private import QStyleKitStylePrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQStyleKitPropertyGroupSpace': '_q_q_style_kit_property_group_space',
      'QQSK': '_q_q_s_k',
      'QQStyleKit': '_q_q_style_kit',
      'QQStyleKitVariationAttached': '_q_q_style_kit_variation_attached',
      'PropertyPathId': '_property_path_id',
      'QQStyleKitPropertyGroup': '_q_q_style_kit_property_group',
      'QQStyleKitFont': '_q_q_style_kit_font',
      'QQStyleKitPalette': '_q_q_style_kit_palette',
      'QQStyleKitCustomTheme': '_q_q_style_kit_custom_theme',
      'QQStyleKitControlProperties': '_q_q_style_kit_control_properties',
      'QQStyleKitDelegateProperties': '_q_q_style_kit_delegate_properties',
      'QQStyleKitBorderProperties': '_q_q_style_kit_border_properties',
      'QQStyleKitControlState': '_q_q_style_kit_control_state',
      'QQStyleKitDelegate': '_q_q_style_kit_delegate',
      'QQStyleKitHandleProperties': '_q_q_style_kit_handle_properties',
      'QQStyleKitIndicatorProperties': '_q_q_style_kit_indicator_properties',
      'QQStyleKitIndicatorWithSubTypes': '_q_q_style_kit_indicator_with_sub_types',
      'QQStyleKitShadowProperties': '_q_q_style_kit_shadow_properties',
      'QQStyleKitTextProperties': '_q_q_style_kit_text_properties',
      'QQStyleKitControl': '_q_q_style_kit_control',
      'QQStyleKitControls': '_q_q_style_kit_controls',
      'QQStyleKitCustomControl': '_q_q_style_kit_custom_control',
      'QQStyleKitImageProperties': '_q_q_style_kit_image_properties',
      'QQStyleKitStyleAndThemeBase': '_q_q_style_kit_style_and_theme_base',
      'QQStyleKitStyle': '_q_q_style_kit_style',
      'QQStyleKitTheme': '_q_q_style_kit_theme',
      'QQStyleKitAttached': '_q_q_style_kit_attached',
      'QQStyleKitReader': '_q_q_style_kit_reader',
      'QQStyleKitVariation': '_q_q_style_kit_variation',
      'QStyleKitStyle': '_q_style_kit_style',
      'QQStyleKitDebug': '_q_q_style_kit_debug',
      'QQStyleKitPropertyResolver': '_q_q_style_kit_property_resolver',
      'QStyleKitStylePrivate': '_q_style_kit_style_private',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtLabsStyleKit import QStyleKitStylePrivate'. Python calls
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
