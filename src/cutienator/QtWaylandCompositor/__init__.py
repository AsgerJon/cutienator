"""
The 'cutienator.QtWaylandCompositor' package provides the cute classes
of the part of Qt named QtWaylandCompositor, under the name PySide6 has
for it.

  from cutienator.QtWaylandCompositor import QWaylandBufferRef, QWaylandOutputMode

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
    'QWaylandBufferRef',
    'QWaylandOutputMode',
    'QWaylandSurfaceRole',
    'QWaylandCompositorExtensionPrivate',
    'QWaylandObject',
    'QWaylandCompositorExtension',
    'QWaylandDestroyListener',
    'QWaylandKeymap',
    'QWaylandKeymapPrivate',
    'QWaylandQuickHardwareLayer',
    'QWaylandQuickShellIntegration',
    'QWaylandResource',
    'QWaylandShellPrivate',
    'QWaylandShellSurfacePrivate',
    'QWaylandShell',
    'QWaylandClient',
    'QWaylandSurface',
    'QWaylandOutput',
    'QWaylandSurfaceGrabber',
    'QWaylandView',
    'QWaylandSeat',
    'QWaylandCompositor',
    'QWaylandDrag',
    'QWaylandIdleInhibitManagerV1',
    'QWaylandInputMethodControl',
    'QWaylandInputMethodControlPrivate',
    'QWaylandKeyboard',
    'QWaylandPointer',
    'QWaylandQtTextInputMethod',
    'QWaylandQtTextInputMethodManager',
    'QWaylandQtWindowManager',
    'QWaylandQuickCompositor',
    'QWaylandQuickOutput',
    'QWaylandQuickShellEventFilter',
    'QWaylandQuickSurface',
    'QWaylandTextInput',
    'QWaylandTextInputManager',
    'QWaylandTextInputManagerV3',
    'QWaylandTextInputV3',
    'QWaylandTouch',
    'QWaylandViewPrivate',
    'QWaylandViewporter',
    'QWaylandXdgOutputManagerV1',
    'QWaylandIdleInhibitManagerV1QuickExtension',
    'QWaylandQtTextInputMethodManagerQuickExtension',
    'QWaylandQtWindowManagerQuickExtension',
    'QWaylandQuickCompositorQuickExtensionContainer',
    'QWaylandTextInputManagerQuickExtension',
    'QWaylandTextInputManagerV3QuickExtension',
    'QWaylandXdgOutputV1',
    'QWaylandMouseTracker',
    'QWaylandPresentationTime',
    'QWaylandQuickItem',
    'QWaylandQuickItemPrivate',
    'QWaylandQuickXdgOutputV1',
    'QWaylandBufferMaterial',
    'QWaylandShellSurface',
    'QWaylandQuickShellSurfaceItem',
    'QWaylandQuickShellSurfaceItemPrivate',
    'QWaylandBufferMaterialShader',
    'QWaylandIviApplication',
    'QWaylandIviSurface',
    'QWaylandWlShell',
    'QWaylandWlShellSurface',
    'QWaylandXdgSurface',
    'QWaylandXdgPopup',
    'QWaylandXdgToplevel',
    'QWaylandXdgShell',
    'QWaylandXdgDecorationManagerV1',
    'QtWayland',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_wayland_buffer_ref import QWaylandBufferRef
  from ._q_wayland_output_mode import QWaylandOutputMode
  from ._q_wayland_surface_role import QWaylandSurfaceRole
  from ._q_wayland_compositor_extension_private import QWaylandCompositorExtensionPrivate
  from ._q_wayland_object import QWaylandObject
  from ._q_wayland_compositor_extension import QWaylandCompositorExtension
  from ._q_wayland_destroy_listener import QWaylandDestroyListener
  from ._q_wayland_keymap import QWaylandKeymap
  from ._q_wayland_keymap_private import QWaylandKeymapPrivate
  from ._q_wayland_quick_hardware_layer import QWaylandQuickHardwareLayer
  from ._q_wayland_quick_shell_integration import QWaylandQuickShellIntegration
  from ._q_wayland_resource import QWaylandResource
  from ._q_wayland_shell_private import QWaylandShellPrivate
  from ._q_wayland_shell_surface_private import QWaylandShellSurfacePrivate
  from ._q_wayland_shell import QWaylandShell
  from ._q_wayland_client import QWaylandClient
  from ._q_wayland_surface import QWaylandSurface
  from ._q_wayland_output import QWaylandOutput
  from ._q_wayland_surface_grabber import QWaylandSurfaceGrabber
  from ._q_wayland_view import QWaylandView
  from ._q_wayland_seat import QWaylandSeat
  from ._q_wayland_compositor import QWaylandCompositor
  from ._q_wayland_drag import QWaylandDrag
  from ._q_wayland_idle_inhibit_manager_v1 import QWaylandIdleInhibitManagerV1
  from ._q_wayland_input_method_control import QWaylandInputMethodControl
  from ._q_wayland_input_method_control_private import QWaylandInputMethodControlPrivate
  from ._q_wayland_keyboard import QWaylandKeyboard
  from ._q_wayland_pointer import QWaylandPointer
  from ._q_wayland_qt_text_input_method import QWaylandQtTextInputMethod
  from ._q_wayland_qt_text_input_method_manager import QWaylandQtTextInputMethodManager
  from ._q_wayland_qt_window_manager import QWaylandQtWindowManager
  from ._q_wayland_quick_compositor import QWaylandQuickCompositor
  from ._q_wayland_quick_output import QWaylandQuickOutput
  from ._q_wayland_quick_shell_event_filter import QWaylandQuickShellEventFilter
  from ._q_wayland_quick_surface import QWaylandQuickSurface
  from ._q_wayland_text_input import QWaylandTextInput
  from ._q_wayland_text_input_manager import QWaylandTextInputManager
  from ._q_wayland_text_input_manager_v3 import QWaylandTextInputManagerV3
  from ._q_wayland_text_input_v3 import QWaylandTextInputV3
  from ._q_wayland_touch import QWaylandTouch
  from ._q_wayland_view_private import QWaylandViewPrivate
  from ._q_wayland_viewporter import QWaylandViewporter
  from ._q_wayland_xdg_output_manager_v1 import QWaylandXdgOutputManagerV1
  from ._q_wayland_idle_inhibit_manager_v1_quick_extension import QWaylandIdleInhibitManagerV1QuickExtension
  from ._q_wayland_qt_text_input_method_manager_quick_extension import QWaylandQtTextInputMethodManagerQuickExtension
  from ._q_wayland_qt_window_manager_quick_extension import QWaylandQtWindowManagerQuickExtension
  from ._q_wayland_quick_compositor_quick_extension_container import QWaylandQuickCompositorQuickExtensionContainer
  from ._q_wayland_text_input_manager_quick_extension import QWaylandTextInputManagerQuickExtension
  from ._q_wayland_text_input_manager_v3_quick_extension import QWaylandTextInputManagerV3QuickExtension
  from ._q_wayland_xdg_output_v1 import QWaylandXdgOutputV1
  from ._q_wayland_mouse_tracker import QWaylandMouseTracker
  from ._q_wayland_presentation_time import QWaylandPresentationTime
  from ._q_wayland_quick_item import QWaylandQuickItem
  from ._q_wayland_quick_item_private import QWaylandQuickItemPrivate
  from ._q_wayland_quick_xdg_output_v1 import QWaylandQuickXdgOutputV1
  from ._q_wayland_buffer_material import QWaylandBufferMaterial
  from ._q_wayland_shell_surface import QWaylandShellSurface
  from ._q_wayland_quick_shell_surface_item import QWaylandQuickShellSurfaceItem
  from ._q_wayland_quick_shell_surface_item_private import QWaylandQuickShellSurfaceItemPrivate
  from ._q_wayland_buffer_material_shader import QWaylandBufferMaterialShader
  from ._q_wayland_ivi_application import QWaylandIviApplication
  from ._q_wayland_ivi_surface import QWaylandIviSurface
  from ._q_wayland_wl_shell import QWaylandWlShell
  from ._q_wayland_wl_shell_surface import QWaylandWlShellSurface
  from ._q_wayland_xdg_surface import QWaylandXdgSurface
  from ._q_wayland_xdg_popup import QWaylandXdgPopup
  from ._q_wayland_xdg_toplevel import QWaylandXdgToplevel
  from ._q_wayland_xdg_shell import QWaylandXdgShell
  from ._q_wayland_xdg_decoration_manager_v1 import QWaylandXdgDecorationManagerV1
  from . import QtWayland
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QWaylandBufferRef': '_q_wayland_buffer_ref',
      'QWaylandOutputMode': '_q_wayland_output_mode',
      'QWaylandSurfaceRole': '_q_wayland_surface_role',
      'QWaylandCompositorExtensionPrivate': '_q_wayland_compositor_extension_private',
      'QWaylandObject': '_q_wayland_object',
      'QWaylandCompositorExtension': '_q_wayland_compositor_extension',
      'QWaylandDestroyListener': '_q_wayland_destroy_listener',
      'QWaylandKeymap': '_q_wayland_keymap',
      'QWaylandKeymapPrivate': '_q_wayland_keymap_private',
      'QWaylandQuickHardwareLayer': '_q_wayland_quick_hardware_layer',
      'QWaylandQuickShellIntegration': '_q_wayland_quick_shell_integration',
      'QWaylandResource': '_q_wayland_resource',
      'QWaylandShellPrivate': '_q_wayland_shell_private',
      'QWaylandShellSurfacePrivate': '_q_wayland_shell_surface_private',
      'QWaylandShell': '_q_wayland_shell',
      'QWaylandClient': '_q_wayland_client',
      'QWaylandSurface': '_q_wayland_surface',
      'QWaylandOutput': '_q_wayland_output',
      'QWaylandSurfaceGrabber': '_q_wayland_surface_grabber',
      'QWaylandView': '_q_wayland_view',
      'QWaylandSeat': '_q_wayland_seat',
      'QWaylandCompositor': '_q_wayland_compositor',
      'QWaylandDrag': '_q_wayland_drag',
      'QWaylandIdleInhibitManagerV1': '_q_wayland_idle_inhibit_manager_v1',
      'QWaylandInputMethodControl': '_q_wayland_input_method_control',
      'QWaylandInputMethodControlPrivate': '_q_wayland_input_method_control_private',
      'QWaylandKeyboard': '_q_wayland_keyboard',
      'QWaylandPointer': '_q_wayland_pointer',
      'QWaylandQtTextInputMethod': '_q_wayland_qt_text_input_method',
      'QWaylandQtTextInputMethodManager': '_q_wayland_qt_text_input_method_manager',
      'QWaylandQtWindowManager': '_q_wayland_qt_window_manager',
      'QWaylandQuickCompositor': '_q_wayland_quick_compositor',
      'QWaylandQuickOutput': '_q_wayland_quick_output',
      'QWaylandQuickShellEventFilter': '_q_wayland_quick_shell_event_filter',
      'QWaylandQuickSurface': '_q_wayland_quick_surface',
      'QWaylandTextInput': '_q_wayland_text_input',
      'QWaylandTextInputManager': '_q_wayland_text_input_manager',
      'QWaylandTextInputManagerV3': '_q_wayland_text_input_manager_v3',
      'QWaylandTextInputV3': '_q_wayland_text_input_v3',
      'QWaylandTouch': '_q_wayland_touch',
      'QWaylandViewPrivate': '_q_wayland_view_private',
      'QWaylandViewporter': '_q_wayland_viewporter',
      'QWaylandXdgOutputManagerV1': '_q_wayland_xdg_output_manager_v1',
      'QWaylandIdleInhibitManagerV1QuickExtension': '_q_wayland_idle_inhibit_manager_v1_quick_extension',
      'QWaylandQtTextInputMethodManagerQuickExtension': '_q_wayland_qt_text_input_method_manager_quick_extension',
      'QWaylandQtWindowManagerQuickExtension': '_q_wayland_qt_window_manager_quick_extension',
      'QWaylandQuickCompositorQuickExtensionContainer': '_q_wayland_quick_compositor_quick_extension_container',
      'QWaylandTextInputManagerQuickExtension': '_q_wayland_text_input_manager_quick_extension',
      'QWaylandTextInputManagerV3QuickExtension': '_q_wayland_text_input_manager_v3_quick_extension',
      'QWaylandXdgOutputV1': '_q_wayland_xdg_output_v1',
      'QWaylandMouseTracker': '_q_wayland_mouse_tracker',
      'QWaylandPresentationTime': '_q_wayland_presentation_time',
      'QWaylandQuickItem': '_q_wayland_quick_item',
      'QWaylandQuickItemPrivate': '_q_wayland_quick_item_private',
      'QWaylandQuickXdgOutputV1': '_q_wayland_quick_xdg_output_v1',
      'QWaylandBufferMaterial': '_q_wayland_buffer_material',
      'QWaylandShellSurface': '_q_wayland_shell_surface',
      'QWaylandQuickShellSurfaceItem': '_q_wayland_quick_shell_surface_item',
      'QWaylandQuickShellSurfaceItemPrivate': '_q_wayland_quick_shell_surface_item_private',
      'QWaylandBufferMaterialShader': '_q_wayland_buffer_material_shader',
      'QWaylandIviApplication': '_q_wayland_ivi_application',
      'QWaylandIviSurface': '_q_wayland_ivi_surface',
      'QWaylandWlShell': '_q_wayland_wl_shell',
      'QWaylandWlShellSurface': '_q_wayland_wl_shell_surface',
      'QWaylandXdgSurface': '_q_wayland_xdg_surface',
      'QWaylandXdgPopup': '_q_wayland_xdg_popup',
      'QWaylandXdgToplevel': '_q_wayland_xdg_toplevel',
      'QWaylandXdgShell': '_q_wayland_xdg_shell',
      'QWaylandXdgDecorationManagerV1': '_q_wayland_xdg_decoration_manager_v1',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtWayland',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWaylandCompositor import QWaylandXdgDecorationManagerV1'. Python calls
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
