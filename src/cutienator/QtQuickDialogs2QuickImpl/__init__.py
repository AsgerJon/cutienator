"""
The 'cutienator.QtQuickDialogs2QuickImpl' package provides the cute
classes of the part of Qt named QtQuickDialogs2QuickImpl, under the name
PySide6 has for it.

  from cutienator.QtQuickDialogs2QuickImpl import HSVA, QQuickAbstractButtonForeign

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
    'HSVA',
    'QQuickAbstractButtonForeign',
    'QQuickColorDialogImplAttachedPrivate',
    'QQuickControlForeign',
    'QQuickDialogForeign',
    'QQuickDialogImplFactory',
    'QQuickEyeDropperEventFilter',
    'QQuickFileDialogImplAttachedPrivate',
    'QQuickFileNameFilterQuickDialogs2QuickImplForeign',
    'QQuickFolderDialogImplAttachedPrivate',
    'QQuickIconForeign',
    'QQuickMessageDialogImplAttachedPrivate',
    'QQuickPopupForeign',
    'QQuickFontDialogImplAttachedPrivate',
    'QQuickPlatformColorDialog',
    'QQuickPlatformFileDialog',
    'QQuickPlatformFolderDialog',
    'QQuickPlatformFontDialog',
    'QQuickPlatformMessageDialog',
    'QQuickSaturationLightnessPickerCanvas',
    'QQuickAbstractColorPicker',
    'QQuickAbstractColorPickerPrivate',
    'QQuickColorInputs',
    'QQuickFolderBreadcrumbBarPrivate',
    'QQuickSaturationLightnessPicker',
    'QQuickColorDialogImpl',
    'QQuickColorDialogImplAttached',
    'QQuickFileDialogImpl',
    'QQuickFileDialogTapHandler',
    'QQuickFolderDialogImpl',
    'QQuickFontDialogImpl',
    'QQuickMessageDialogImpl',
    'QQuickSideBar',
    'QQuickColorDialogImplPrivate',
    'QQuickFileDialogDelegate',
    'QQuickFileDialogImplPrivate',
    'QQuickFolderBreadcrumbBar',
    'QQuickFolderDialogImplPrivate',
    'QQuickFontDialogImplPrivate',
    'QQuickMessageDialogImplAttached',
    'QQuickMessageDialogImplPrivate',
    'QQuickSideBarPrivate',
    'QQuickFileDialogDelegatePrivate',
    'QQuickFileDialogImplAttached',
    'QQuickFolderDialogImplAttached',
    'QQuickFontDialogImplAttached',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._h_s_v_a import HSVA
  from ._q_quick_abstract_button_foreign import QQuickAbstractButtonForeign
  from ._q_quick_color_dialog_impl_attached_private import QQuickColorDialogImplAttachedPrivate
  from ._q_quick_control_foreign import QQuickControlForeign
  from ._q_quick_dialog_foreign import QQuickDialogForeign
  from ._q_quick_dialog_impl_factory import QQuickDialogImplFactory
  from ._q_quick_eye_dropper_event_filter import QQuickEyeDropperEventFilter
  from ._q_quick_file_dialog_impl_attached_private import QQuickFileDialogImplAttachedPrivate
  from ._q_quick_file_name_filter_quick_dialogs2_quick_impl_foreign import QQuickFileNameFilterQuickDialogs2QuickImplForeign
  from ._q_quick_folder_dialog_impl_attached_private import QQuickFolderDialogImplAttachedPrivate
  from ._q_quick_icon_foreign import QQuickIconForeign
  from ._q_quick_message_dialog_impl_attached_private import QQuickMessageDialogImplAttachedPrivate
  from ._q_quick_popup_foreign import QQuickPopupForeign
  from ._q_quick_font_dialog_impl_attached_private import QQuickFontDialogImplAttachedPrivate
  from ._q_quick_platform_color_dialog import QQuickPlatformColorDialog
  from ._q_quick_platform_file_dialog import QQuickPlatformFileDialog
  from ._q_quick_platform_folder_dialog import QQuickPlatformFolderDialog
  from ._q_quick_platform_font_dialog import QQuickPlatformFontDialog
  from ._q_quick_platform_message_dialog import QQuickPlatformMessageDialog
  from ._q_quick_saturation_lightness_picker_canvas import QQuickSaturationLightnessPickerCanvas
  from ._q_quick_abstract_color_picker import QQuickAbstractColorPicker
  from ._q_quick_abstract_color_picker_private import QQuickAbstractColorPickerPrivate
  from ._q_quick_color_inputs import QQuickColorInputs
  from ._q_quick_folder_breadcrumb_bar_private import QQuickFolderBreadcrumbBarPrivate
  from ._q_quick_saturation_lightness_picker import QQuickSaturationLightnessPicker
  from ._q_quick_color_dialog_impl import QQuickColorDialogImpl
  from ._q_quick_color_dialog_impl_attached import QQuickColorDialogImplAttached
  from ._q_quick_file_dialog_impl import QQuickFileDialogImpl
  from ._q_quick_file_dialog_tap_handler import QQuickFileDialogTapHandler
  from ._q_quick_folder_dialog_impl import QQuickFolderDialogImpl
  from ._q_quick_font_dialog_impl import QQuickFontDialogImpl
  from ._q_quick_message_dialog_impl import QQuickMessageDialogImpl
  from ._q_quick_side_bar import QQuickSideBar
  from ._q_quick_color_dialog_impl_private import QQuickColorDialogImplPrivate
  from ._q_quick_file_dialog_delegate import QQuickFileDialogDelegate
  from ._q_quick_file_dialog_impl_private import QQuickFileDialogImplPrivate
  from ._q_quick_folder_breadcrumb_bar import QQuickFolderBreadcrumbBar
  from ._q_quick_folder_dialog_impl_private import QQuickFolderDialogImplPrivate
  from ._q_quick_font_dialog_impl_private import QQuickFontDialogImplPrivate
  from ._q_quick_message_dialog_impl_attached import QQuickMessageDialogImplAttached
  from ._q_quick_message_dialog_impl_private import QQuickMessageDialogImplPrivate
  from ._q_quick_side_bar_private import QQuickSideBarPrivate
  from ._q_quick_file_dialog_delegate_private import QQuickFileDialogDelegatePrivate
  from ._q_quick_file_dialog_impl_attached import QQuickFileDialogImplAttached
  from ._q_quick_folder_dialog_impl_attached import QQuickFolderDialogImplAttached
  from ._q_quick_font_dialog_impl_attached import QQuickFontDialogImplAttached
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'HSVA': '_h_s_v_a',
      'QQuickAbstractButtonForeign': '_q_quick_abstract_button_foreign',
      'QQuickColorDialogImplAttachedPrivate': '_q_quick_color_dialog_impl_attached_private',
      'QQuickControlForeign': '_q_quick_control_foreign',
      'QQuickDialogForeign': '_q_quick_dialog_foreign',
      'QQuickDialogImplFactory': '_q_quick_dialog_impl_factory',
      'QQuickEyeDropperEventFilter': '_q_quick_eye_dropper_event_filter',
      'QQuickFileDialogImplAttachedPrivate': '_q_quick_file_dialog_impl_attached_private',
      'QQuickFileNameFilterQuickDialogs2QuickImplForeign': '_q_quick_file_name_filter_quick_dialogs2_quick_impl_foreign',
      'QQuickFolderDialogImplAttachedPrivate': '_q_quick_folder_dialog_impl_attached_private',
      'QQuickIconForeign': '_q_quick_icon_foreign',
      'QQuickMessageDialogImplAttachedPrivate': '_q_quick_message_dialog_impl_attached_private',
      'QQuickPopupForeign': '_q_quick_popup_foreign',
      'QQuickFontDialogImplAttachedPrivate': '_q_quick_font_dialog_impl_attached_private',
      'QQuickPlatformColorDialog': '_q_quick_platform_color_dialog',
      'QQuickPlatformFileDialog': '_q_quick_platform_file_dialog',
      'QQuickPlatformFolderDialog': '_q_quick_platform_folder_dialog',
      'QQuickPlatformFontDialog': '_q_quick_platform_font_dialog',
      'QQuickPlatformMessageDialog': '_q_quick_platform_message_dialog',
      'QQuickSaturationLightnessPickerCanvas': '_q_quick_saturation_lightness_picker_canvas',
      'QQuickAbstractColorPicker': '_q_quick_abstract_color_picker',
      'QQuickAbstractColorPickerPrivate': '_q_quick_abstract_color_picker_private',
      'QQuickColorInputs': '_q_quick_color_inputs',
      'QQuickFolderBreadcrumbBarPrivate': '_q_quick_folder_breadcrumb_bar_private',
      'QQuickSaturationLightnessPicker': '_q_quick_saturation_lightness_picker',
      'QQuickColorDialogImpl': '_q_quick_color_dialog_impl',
      'QQuickColorDialogImplAttached': '_q_quick_color_dialog_impl_attached',
      'QQuickFileDialogImpl': '_q_quick_file_dialog_impl',
      'QQuickFileDialogTapHandler': '_q_quick_file_dialog_tap_handler',
      'QQuickFolderDialogImpl': '_q_quick_folder_dialog_impl',
      'QQuickFontDialogImpl': '_q_quick_font_dialog_impl',
      'QQuickMessageDialogImpl': '_q_quick_message_dialog_impl',
      'QQuickSideBar': '_q_quick_side_bar',
      'QQuickColorDialogImplPrivate': '_q_quick_color_dialog_impl_private',
      'QQuickFileDialogDelegate': '_q_quick_file_dialog_delegate',
      'QQuickFileDialogImplPrivate': '_q_quick_file_dialog_impl_private',
      'QQuickFolderBreadcrumbBar': '_q_quick_folder_breadcrumb_bar',
      'QQuickFolderDialogImplPrivate': '_q_quick_folder_dialog_impl_private',
      'QQuickFontDialogImplPrivate': '_q_quick_font_dialog_impl_private',
      'QQuickMessageDialogImplAttached': '_q_quick_message_dialog_impl_attached',
      'QQuickMessageDialogImplPrivate': '_q_quick_message_dialog_impl_private',
      'QQuickSideBarPrivate': '_q_quick_side_bar_private',
      'QQuickFileDialogDelegatePrivate': '_q_quick_file_dialog_delegate_private',
      'QQuickFileDialogImplAttached': '_q_quick_file_dialog_impl_attached',
      'QQuickFolderDialogImplAttached': '_q_quick_folder_dialog_impl_attached',
      'QQuickFontDialogImplAttached': '_q_quick_font_dialog_impl_attached',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickDialogs2QuickImpl import QQuickFontDialogImplAttached'. Python calls
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
