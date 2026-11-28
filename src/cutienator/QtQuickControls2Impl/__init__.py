"""
The 'cutienator.QtQuickControls2Impl' package provides the cute classes
of the part of Qt named QtQuickControls2Impl, under the name PySide6 has
for it.

  from cutienator.QtQuickControls2Impl import QQuickTextForeign, QQuickPlatformTheme

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
    'QQuickTextForeign',
    'QQuickPlatformTheme',
    'QQuickImageSelector',
    'QQuickAnimatedImageSelector',
    'QQuickAnimatedNode',
    'QQuickIconLabelPrivate',
    'QQuickNinePatchImageSelector',
    'QQuickTumblerView',
    'QQuickIconLabel',
    'QQuickMenuItemIconLabelPrivate',
    'QQuickPaddedRectangle',
    'QQuickItemGroup',
    'QQuickCheckLabel',
    'QQuickClippedText',
    'QQuickMenuItemIconLabel',
    'QQuickMnemonicLabel',
    'QQuickPlaceholderText',
    'QQuickIconImagePrivate',
    'QQuickColorImage',
    'QQuickIconImage',
    'QQuickNinePatchImage',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_text_foreign import QQuickTextForeign
  from ._q_quick_platform_theme import QQuickPlatformTheme
  from ._q_quick_image_selector import QQuickImageSelector
  from ._q_quick_animated_image_selector import QQuickAnimatedImageSelector
  from ._q_quick_animated_node import QQuickAnimatedNode
  from ._q_quick_icon_label_private import QQuickIconLabelPrivate
  from ._q_quick_nine_patch_image_selector import QQuickNinePatchImageSelector
  from ._q_quick_tumbler_view import QQuickTumblerView
  from ._q_quick_icon_label import QQuickIconLabel
  from ._q_quick_menu_item_icon_label_private import QQuickMenuItemIconLabelPrivate
  from ._q_quick_padded_rectangle import QQuickPaddedRectangle
  from ._q_quick_item_group import QQuickItemGroup
  from ._q_quick_check_label import QQuickCheckLabel
  from ._q_quick_clipped_text import QQuickClippedText
  from ._q_quick_menu_item_icon_label import QQuickMenuItemIconLabel
  from ._q_quick_mnemonic_label import QQuickMnemonicLabel
  from ._q_quick_placeholder_text import QQuickPlaceholderText
  from ._q_quick_icon_image_private import QQuickIconImagePrivate
  from ._q_quick_color_image import QQuickColorImage
  from ._q_quick_icon_image import QQuickIconImage
  from ._q_quick_nine_patch_image import QQuickNinePatchImage
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickTextForeign': '_q_quick_text_foreign',
      'QQuickPlatformTheme': '_q_quick_platform_theme',
      'QQuickImageSelector': '_q_quick_image_selector',
      'QQuickAnimatedImageSelector': '_q_quick_animated_image_selector',
      'QQuickAnimatedNode': '_q_quick_animated_node',
      'QQuickIconLabelPrivate': '_q_quick_icon_label_private',
      'QQuickNinePatchImageSelector': '_q_quick_nine_patch_image_selector',
      'QQuickTumblerView': '_q_quick_tumbler_view',
      'QQuickIconLabel': '_q_quick_icon_label',
      'QQuickMenuItemIconLabelPrivate': '_q_quick_menu_item_icon_label_private',
      'QQuickPaddedRectangle': '_q_quick_padded_rectangle',
      'QQuickItemGroup': '_q_quick_item_group',
      'QQuickCheckLabel': '_q_quick_check_label',
      'QQuickClippedText': '_q_quick_clipped_text',
      'QQuickMenuItemIconLabel': '_q_quick_menu_item_icon_label',
      'QQuickMnemonicLabel': '_q_quick_mnemonic_label',
      'QQuickPlaceholderText': '_q_quick_placeholder_text',
      'QQuickIconImagePrivate': '_q_quick_icon_image_private',
      'QQuickColorImage': '_q_quick_color_image',
      'QQuickIconImage': '_q_quick_icon_image',
      'QQuickNinePatchImage': '_q_quick_nine_patch_image',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickControls2Impl import QQuickNinePatchImage'. Python calls
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
