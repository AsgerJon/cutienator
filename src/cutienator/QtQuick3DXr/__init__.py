"""
The 'cutienator.QtQuick3DXr' package provides the cute classes of the
part of Qt named QtQuick3DXr, under the name PySide6 has for it.

  from cutienator.QtQuick3DXr import QQuick3DXrAbstractHapticEffect, QQuick3DXrInputAction

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
    'QQuick3DXrAbstractHapticEffect',
    'QQuick3DXrInputAction',
    'QQuick3DXrHapticFeedback',
    'QQuick3DXrSimpleHapticEffect',
    'QQuick3DXrActionMapper',
    'QQuick3DXrAnimationDriver',
    'QQuick3DXrHandInput',
    'QQuick3DXrSpatialAnchor',
    'QQuick3DXrAnchorManager',
    'QQuick3DXrSpatialAnchorListModel',
    'QQuick3DXrCamera',
    'QQuick3DXrOrigin',
    'QQuick3DXrController',
    'QQuick3DXrItem',
    'QQuick3DXrEyeCamera',
    'QQuick3DXrInputManager',
    'QQuick3DXrManager',
    'QQuick3DXrRuntimeInfo',
    'QQuick3DXrHandModel',
    'QQuick3DXrView',
    'QQuick3DXrInputManagerPrivate',
    'QQuick3DXrViewPrivate',
    'QQuick3DXrVirtualMouse',
    'QtQuick3DXr',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick3_d_xr_abstract_haptic_effect import QQuick3DXrAbstractHapticEffect
  from ._q_quick3_d_xr_input_action import QQuick3DXrInputAction
  from ._q_quick3_d_xr_haptic_feedback import QQuick3DXrHapticFeedback
  from ._q_quick3_d_xr_simple_haptic_effect import QQuick3DXrSimpleHapticEffect
  from ._q_quick3_d_xr_action_mapper import QQuick3DXrActionMapper
  from ._q_quick3_d_xr_animation_driver import QQuick3DXrAnimationDriver
  from ._q_quick3_d_xr_hand_input import QQuick3DXrHandInput
  from ._q_quick3_d_xr_spatial_anchor import QQuick3DXrSpatialAnchor
  from ._q_quick3_d_xr_anchor_manager import QQuick3DXrAnchorManager
  from ._q_quick3_d_xr_spatial_anchor_list_model import QQuick3DXrSpatialAnchorListModel
  from ._q_quick3_d_xr_camera import QQuick3DXrCamera
  from ._q_quick3_d_xr_origin import QQuick3DXrOrigin
  from ._q_quick3_d_xr_controller import QQuick3DXrController
  from ._q_quick3_d_xr_item import QQuick3DXrItem
  from ._q_quick3_d_xr_eye_camera import QQuick3DXrEyeCamera
  from ._q_quick3_d_xr_input_manager import QQuick3DXrInputManager
  from ._q_quick3_d_xr_manager import QQuick3DXrManager
  from ._q_quick3_d_xr_runtime_info import QQuick3DXrRuntimeInfo
  from ._q_quick3_d_xr_hand_model import QQuick3DXrHandModel
  from ._q_quick3_d_xr_view import QQuick3DXrView
  from ._q_quick3_d_xr_input_manager_private import QQuick3DXrInputManagerPrivate
  from ._q_quick3_d_xr_view_private import QQuick3DXrViewPrivate
  from ._q_quick3_d_xr_virtual_mouse import QQuick3DXrVirtualMouse
  from . import QtQuick3DXr
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuick3DXrAbstractHapticEffect': '_q_quick3_d_xr_abstract_haptic_effect',
      'QQuick3DXrInputAction': '_q_quick3_d_xr_input_action',
      'QQuick3DXrHapticFeedback': '_q_quick3_d_xr_haptic_feedback',
      'QQuick3DXrSimpleHapticEffect': '_q_quick3_d_xr_simple_haptic_effect',
      'QQuick3DXrActionMapper': '_q_quick3_d_xr_action_mapper',
      'QQuick3DXrAnimationDriver': '_q_quick3_d_xr_animation_driver',
      'QQuick3DXrHandInput': '_q_quick3_d_xr_hand_input',
      'QQuick3DXrSpatialAnchor': '_q_quick3_d_xr_spatial_anchor',
      'QQuick3DXrAnchorManager': '_q_quick3_d_xr_anchor_manager',
      'QQuick3DXrSpatialAnchorListModel': '_q_quick3_d_xr_spatial_anchor_list_model',
      'QQuick3DXrCamera': '_q_quick3_d_xr_camera',
      'QQuick3DXrOrigin': '_q_quick3_d_xr_origin',
      'QQuick3DXrController': '_q_quick3_d_xr_controller',
      'QQuick3DXrItem': '_q_quick3_d_xr_item',
      'QQuick3DXrEyeCamera': '_q_quick3_d_xr_eye_camera',
      'QQuick3DXrInputManager': '_q_quick3_d_xr_input_manager',
      'QQuick3DXrManager': '_q_quick3_d_xr_manager',
      'QQuick3DXrRuntimeInfo': '_q_quick3_d_xr_runtime_info',
      'QQuick3DXrHandModel': '_q_quick3_d_xr_hand_model',
      'QQuick3DXrView': '_q_quick3_d_xr_view',
      'QQuick3DXrInputManagerPrivate': '_q_quick3_d_xr_input_manager_private',
      'QQuick3DXrViewPrivate': '_q_quick3_d_xr_view_private',
      'QQuick3DXrVirtualMouse': '_q_quick3_d_xr_virtual_mouse',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtQuick3DXr',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DXr import QQuick3DXrVirtualMouse'. Python calls
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
