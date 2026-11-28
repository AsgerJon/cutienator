"""
The namespace 'qdesigner_internal' of Qt, a package of 'cutienator.QtDesigner':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtDesigner import qdesigner_internal
  qdesigner_internal.ActionData

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._qdesigner_internal import qdesigner_internal as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'ActionData',
    'CETypes',
    'CssHighlightColors',
    'PropertySheetEnumValue',
    'PropertySheetFlagValue',
    'QDesignerWidgetItemInstaller',
    'Selection',
    'SignalSlotDialogData',
    'DesignerMetaEnum',
    'DesignerMetaFlags',
    'PropertySheetTranslatableData',
    'CECommand',
    'PropertySheetStringListValue',
    'PropertySheetStringValue',
    'AddConnectionCommand',
    'DeleteConnectionsCommand',
    'DesignerIconCache',
    'DesignerPixmapCache',
    'PreviewConfiguration',
    'PropertySheetKeySequenceValue',
    'QDesignerIntrospection',
    'Connection',
    'CssHighlighter',
    'PropertySheetIconValue',
    'ActionRepositoryMimeData',
    'SignatureModel',
    'SpecialMenuAction',
    'WidgetDataBaseItem',
    'FormBuilderClipboard',
    'Grid',
    'GridPanel',
    'IconThemeEditor',
    'IconThemeEnumEditor',
    'InvisibleWidget',
    'QDesignerDnDItem',
    'QDesignerMimeData',
    'TextPropertyEditor',
    'UpdateBlocker',
    'MetaDataBaseItem',
    'QDesignerWidgetBox',
    'ConnectionEdit',
    'CursorSelectionState',
    'FormLayoutMenu',
    'Layout',
    'ManageWidgetCommandHelper',
    'MorphMenu',
    'NewPromotedClassPanel',
    'PreviewManager',
    'QDesignerFormWindowCommand',
    'QLayoutSupport',
    'ToolBarEventFilter',
    'ZoomMenu',
    'ActionInsertionCommand',
    'AddActionCommand',
    'AdjustWidgetSizeCommand',
    'BreakLayoutCommand',
    'ChangeCurrentPageCommand',
    'ChangeLayoutItemGeometry',
    'ChangeZOrderCommand',
    'ContainerWidgetCommand',
    'CreateSubmenuCommand',
    'DeleteMenuBarCommand',
    'DeleteStatusBarCommand',
    'DeleteToolBarCommand',
    'DeleteWidgetCommand',
    'DemoteFromCustomWidgetCommand',
    'DockWidgetCommand',
    'InsertWidgetCommand',
    'LayoutCommand',
    'MenuActionCommand',
    'PromoteToCustomWidgetCommand',
    'QDesignerFormWindowManager',
    'QDesignerObjectInspector',
    'RemoveActionCommand',
    'ReparentWidgetCommand',
    'StackedWidgetCommand',
    'TabOrderCommand',
    'TabWidgetCommand',
    'ToolBoxCommand',
    'AddContainerWidgetPageCommand',
    'AddDockWidgetCommand',
    'AddMenuActionCommand',
    'AddStackedWidgetPageCommand',
    'AddTabPageCommand',
    'AddToolBarCommand',
    'AddToolBoxPageCommand',
    'CodeDialog',
    'CreateMenuBarCommand',
    'CreateStatusBarCommand',
    'DeleteContainerWidgetPageCommand',
    'DeleteStackedWidgetPageCommand',
    'DeleteTabPageCommand',
    'DeleteToolBoxPageCommand',
    'InsertActionIntoCommand',
    'LowerWidgetCommand',
    'MoveStackedWidgetCommand',
    'MoveTabPageCommand',
    'MoveToolBoxPageCommand',
    'NewActionDialog',
    'RaiseWidgetCommand',
    'RemoveActionFromCommand',
    'RemoveMenuActionCommand',
    'HtmlHighlighter',
    'StyleSheetEditor',
    'ActionListView',
    'SignaturePanel',
    'ActionTreeView',
    'DialogGui',
    'MenuActionLineEdit',
    'PropertyLineEdit',
    'SheetDelegate',
    'ZoomProxyWidget',
    'ZoomView',
    'ActionEditor',
    'ActionModel',
    'ActionView',
    'ChangeFormLayoutItemRoleCommand',
    'ChangeListContentsCommand',
    'ChangeTreeContentsCommand',
    'DeviceProfile',
    'FormWindowBase',
    'IconSelector',
    'ItemData',
    'LanguageResourceDialog',
    'LayoutAlignmentCommand',
    'LayoutHelper',
    'LayoutInfo',
    'LayoutProperties',
    'ListContents',
    'MetaDataBase',
    'MorphLayoutCommand',
    'OrderDialog',
    'PlainTextEditorDialog',
    'PreviewConfigurationWidget',
    'PromotionModel',
    'PromotionTaskMenu',
    'PropertySheetPixmapValue',
    'QDesignerFormEditorCommand',
    'QDesignerPromotion',
    'QDesignerPromotionDialog',
    'QDesignerPropertyEditor',
    'QDesignerSharedSettings',
    'QDesignerTaskMenu',
    'QDesignerWidgetItem',
    'RichTextEditorDialog',
    'SelectSignalDialog',
    'SignalSlotDialog',
    'SimplifyLayoutCommand',
    'StyleSheetEditorDialog',
    'TreeWidgetContents',
    'WidgetDataBase',
    'WidgetFactory',
    'ZoomWidget',
    'ChangeTableContentsCommand',
    'NewFormWidget',
    'StyleSheetPropertyEditorDialog',
    'TableWidgetContents',
    'QSimpleResource',
    'QDesignerFormBuilder',
    'QEditorFormBuilder',
    'NewFormWidgetFormBuilder',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qdesigner_internal__action_data import ActionData
  from .._qdesigner_internal__c_e_types import CETypes
  from .._qdesigner_internal__css_highlight_colors import CssHighlightColors
  from .._qdesigner_internal__property_sheet_enum_value import PropertySheetEnumValue
  from .._qdesigner_internal__property_sheet_flag_value import PropertySheetFlagValue
  from .._qdesigner_internal__q_designer_widget_item_installer import QDesignerWidgetItemInstaller
  from .._qdesigner_internal__selection import Selection
  from .._qdesigner_internal__signal_slot_dialog_data import SignalSlotDialogData
  from .._qdesigner_internal__designer_meta_enum import DesignerMetaEnum
  from .._qdesigner_internal__designer_meta_flags import DesignerMetaFlags
  from .._qdesigner_internal__property_sheet_translatable_data import PropertySheetTranslatableData
  from .._qdesigner_internal__c_e_command import CECommand
  from .._qdesigner_internal__property_sheet_string_list_value import PropertySheetStringListValue
  from .._qdesigner_internal__property_sheet_string_value import PropertySheetStringValue
  from .._qdesigner_internal__add_connection_command import AddConnectionCommand
  from .._qdesigner_internal__delete_connections_command import DeleteConnectionsCommand
  from .._qdesigner_internal__designer_icon_cache import DesignerIconCache
  from .._qdesigner_internal__designer_pixmap_cache import DesignerPixmapCache
  from .._qdesigner_internal__preview_configuration import PreviewConfiguration
  from .._qdesigner_internal__property_sheet_key_sequence_value import PropertySheetKeySequenceValue
  from .._qdesigner_internal__q_designer_introspection import QDesignerIntrospection
  from .._qdesigner_internal__connection import Connection
  from .._qdesigner_internal__css_highlighter import CssHighlighter
  from .._qdesigner_internal__property_sheet_icon_value import PropertySheetIconValue
  from .._qdesigner_internal__action_repository_mime_data import ActionRepositoryMimeData
  from .._qdesigner_internal__signature_model import SignatureModel
  from .._qdesigner_internal__special_menu_action import SpecialMenuAction
  from .._qdesigner_internal__widget_data_base_item import WidgetDataBaseItem
  from .._qdesigner_internal__form_builder_clipboard import FormBuilderClipboard
  from .._qdesigner_internal__grid import Grid
  from .._qdesigner_internal__grid_panel import GridPanel
  from .._qdesigner_internal__icon_theme_editor import IconThemeEditor
  from .._qdesigner_internal__icon_theme_enum_editor import IconThemeEnumEditor
  from .._qdesigner_internal__invisible_widget import InvisibleWidget
  from .._qdesigner_internal__q_designer_dn_d_item import QDesignerDnDItem
  from .._qdesigner_internal__q_designer_mime_data import QDesignerMimeData
  from .._qdesigner_internal__text_property_editor import TextPropertyEditor
  from .._qdesigner_internal__update_blocker import UpdateBlocker
  from .._qdesigner_internal__meta_data_base_item import MetaDataBaseItem
  from .._qdesigner_internal__q_designer_widget_box import QDesignerWidgetBox
  from .._qdesigner_internal__connection_edit import ConnectionEdit
  from .._qdesigner_internal__cursor_selection_state import CursorSelectionState
  from .._qdesigner_internal__form_layout_menu import FormLayoutMenu
  from .._qdesigner_internal__layout import Layout
  from .._qdesigner_internal__manage_widget_command_helper import ManageWidgetCommandHelper
  from .._qdesigner_internal__morph_menu import MorphMenu
  from .._qdesigner_internal__new_promoted_class_panel import NewPromotedClassPanel
  from .._qdesigner_internal__preview_manager import PreviewManager
  from .._qdesigner_internal__q_designer_form_window_command import QDesignerFormWindowCommand
  from .._qdesigner_internal__q_layout_support import QLayoutSupport
  from .._qdesigner_internal__tool_bar_event_filter import ToolBarEventFilter
  from .._qdesigner_internal__zoom_menu import ZoomMenu
  from .._qdesigner_internal__action_insertion_command import ActionInsertionCommand
  from .._qdesigner_internal__add_action_command import AddActionCommand
  from .._qdesigner_internal__adjust_widget_size_command import AdjustWidgetSizeCommand
  from .._qdesigner_internal__break_layout_command import BreakLayoutCommand
  from .._qdesigner_internal__change_current_page_command import ChangeCurrentPageCommand
  from .._qdesigner_internal__change_layout_item_geometry import ChangeLayoutItemGeometry
  from .._qdesigner_internal__change_z_order_command import ChangeZOrderCommand
  from .._qdesigner_internal__container_widget_command import ContainerWidgetCommand
  from .._qdesigner_internal__create_submenu_command import CreateSubmenuCommand
  from .._qdesigner_internal__delete_menu_bar_command import DeleteMenuBarCommand
  from .._qdesigner_internal__delete_status_bar_command import DeleteStatusBarCommand
  from .._qdesigner_internal__delete_tool_bar_command import DeleteToolBarCommand
  from .._qdesigner_internal__delete_widget_command import DeleteWidgetCommand
  from .._qdesigner_internal__demote_from_custom_widget_command import DemoteFromCustomWidgetCommand
  from .._qdesigner_internal__dock_widget_command import DockWidgetCommand
  from .._qdesigner_internal__insert_widget_command import InsertWidgetCommand
  from .._qdesigner_internal__layout_command import LayoutCommand
  from .._qdesigner_internal__menu_action_command import MenuActionCommand
  from .._qdesigner_internal__promote_to_custom_widget_command import PromoteToCustomWidgetCommand
  from .._qdesigner_internal__q_designer_form_window_manager import QDesignerFormWindowManager
  from .._qdesigner_internal__q_designer_object_inspector import QDesignerObjectInspector
  from .._qdesigner_internal__remove_action_command import RemoveActionCommand
  from .._qdesigner_internal__reparent_widget_command import ReparentWidgetCommand
  from .._qdesigner_internal__stacked_widget_command import StackedWidgetCommand
  from .._qdesigner_internal__tab_order_command import TabOrderCommand
  from .._qdesigner_internal__tab_widget_command import TabWidgetCommand
  from .._qdesigner_internal__tool_box_command import ToolBoxCommand
  from .._qdesigner_internal__add_container_widget_page_command import AddContainerWidgetPageCommand
  from .._qdesigner_internal__add_dock_widget_command import AddDockWidgetCommand
  from .._qdesigner_internal__add_menu_action_command import AddMenuActionCommand
  from .._qdesigner_internal__add_stacked_widget_page_command import AddStackedWidgetPageCommand
  from .._qdesigner_internal__add_tab_page_command import AddTabPageCommand
  from .._qdesigner_internal__add_tool_bar_command import AddToolBarCommand
  from .._qdesigner_internal__add_tool_box_page_command import AddToolBoxPageCommand
  from .._qdesigner_internal__code_dialog import CodeDialog
  from .._qdesigner_internal__create_menu_bar_command import CreateMenuBarCommand
  from .._qdesigner_internal__create_status_bar_command import CreateStatusBarCommand
  from .._qdesigner_internal__delete_container_widget_page_command import DeleteContainerWidgetPageCommand
  from .._qdesigner_internal__delete_stacked_widget_page_command import DeleteStackedWidgetPageCommand
  from .._qdesigner_internal__delete_tab_page_command import DeleteTabPageCommand
  from .._qdesigner_internal__delete_tool_box_page_command import DeleteToolBoxPageCommand
  from .._qdesigner_internal__insert_action_into_command import InsertActionIntoCommand
  from .._qdesigner_internal__lower_widget_command import LowerWidgetCommand
  from .._qdesigner_internal__move_stacked_widget_command import MoveStackedWidgetCommand
  from .._qdesigner_internal__move_tab_page_command import MoveTabPageCommand
  from .._qdesigner_internal__move_tool_box_page_command import MoveToolBoxPageCommand
  from .._qdesigner_internal__new_action_dialog import NewActionDialog
  from .._qdesigner_internal__raise_widget_command import RaiseWidgetCommand
  from .._qdesigner_internal__remove_action_from_command import RemoveActionFromCommand
  from .._qdesigner_internal__remove_menu_action_command import RemoveMenuActionCommand
  from .._qdesigner_internal__html_highlighter import HtmlHighlighter
  from .._qdesigner_internal__style_sheet_editor import StyleSheetEditor
  from .._qdesigner_internal__action_list_view import ActionListView
  from .._qdesigner_internal__signature_panel import SignaturePanel
  from .._qdesigner_internal__action_tree_view import ActionTreeView
  from .._qdesigner_internal__dialog_gui import DialogGui
  from .._qdesigner_internal__menu_action_line_edit import MenuActionLineEdit
  from .._qdesigner_internal__property_line_edit import PropertyLineEdit
  from .._qdesigner_internal__sheet_delegate import SheetDelegate
  from .._qdesigner_internal__zoom_proxy_widget import ZoomProxyWidget
  from .._qdesigner_internal__zoom_view import ZoomView
  from .._qdesigner_internal__action_editor import ActionEditor
  from .._qdesigner_internal__action_model import ActionModel
  from .._qdesigner_internal__action_view import ActionView
  from .._qdesigner_internal__change_form_layout_item_role_command import ChangeFormLayoutItemRoleCommand
  from .._qdesigner_internal__change_list_contents_command import ChangeListContentsCommand
  from .._qdesigner_internal__change_tree_contents_command import ChangeTreeContentsCommand
  from .._qdesigner_internal__device_profile import DeviceProfile
  from .._qdesigner_internal__form_window_base import FormWindowBase
  from .._qdesigner_internal__icon_selector import IconSelector
  from .._qdesigner_internal__item_data import ItemData
  from .._qdesigner_internal__language_resource_dialog import LanguageResourceDialog
  from .._qdesigner_internal__layout_alignment_command import LayoutAlignmentCommand
  from .._qdesigner_internal__layout_helper import LayoutHelper
  from .._qdesigner_internal__layout_info import LayoutInfo
  from .._qdesigner_internal__layout_properties import LayoutProperties
  from .._qdesigner_internal__list_contents import ListContents
  from .._qdesigner_internal__meta_data_base import MetaDataBase
  from .._qdesigner_internal__morph_layout_command import MorphLayoutCommand
  from .._qdesigner_internal__order_dialog import OrderDialog
  from .._qdesigner_internal__plain_text_editor_dialog import PlainTextEditorDialog
  from .._qdesigner_internal__preview_configuration_widget import PreviewConfigurationWidget
  from .._qdesigner_internal__promotion_model import PromotionModel
  from .._qdesigner_internal__promotion_task_menu import PromotionTaskMenu
  from .._qdesigner_internal__property_sheet_pixmap_value import PropertySheetPixmapValue
  from .._qdesigner_internal__q_designer_form_editor_command import QDesignerFormEditorCommand
  from .._qdesigner_internal__q_designer_promotion import QDesignerPromotion
  from .._qdesigner_internal__q_designer_promotion_dialog import QDesignerPromotionDialog
  from .._qdesigner_internal__q_designer_property_editor import QDesignerPropertyEditor
  from .._qdesigner_internal__q_designer_shared_settings import QDesignerSharedSettings
  from .._qdesigner_internal__q_designer_task_menu import QDesignerTaskMenu
  from .._qdesigner_internal__q_designer_widget_item import QDesignerWidgetItem
  from .._qdesigner_internal__rich_text_editor_dialog import RichTextEditorDialog
  from .._qdesigner_internal__select_signal_dialog import SelectSignalDialog
  from .._qdesigner_internal__signal_slot_dialog import SignalSlotDialog
  from .._qdesigner_internal__simplify_layout_command import SimplifyLayoutCommand
  from .._qdesigner_internal__style_sheet_editor_dialog import StyleSheetEditorDialog
  from .._qdesigner_internal__tree_widget_contents import TreeWidgetContents
  from .._qdesigner_internal__widget_data_base import WidgetDataBase
  from .._qdesigner_internal__widget_factory import WidgetFactory
  from .._qdesigner_internal__zoom_widget import ZoomWidget
  from .._qdesigner_internal__change_table_contents_command import ChangeTableContentsCommand
  from .._qdesigner_internal__new_form_widget import NewFormWidget
  from .._qdesigner_internal__style_sheet_property_editor_dialog import StyleSheetPropertyEditorDialog
  from .._qdesigner_internal__table_widget_contents import TableWidgetContents
  from .._qdesigner_internal__q_simple_resource import QSimpleResource
  from .._qdesigner_internal__q_designer_form_builder import QDesignerFormBuilder
  from .._qdesigner_internal__q_editor_form_builder import QEditorFormBuilder
  from .._qdesigner_internal__new_form_widget_form_builder import NewFormWidgetFormBuilder
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ActionData': '_qdesigner_internal__action_data',
      'CETypes': '_qdesigner_internal__c_e_types',
      'CssHighlightColors': '_qdesigner_internal__css_highlight_colors',
      'PropertySheetEnumValue': '_qdesigner_internal__property_sheet_enum_value',
      'PropertySheetFlagValue': '_qdesigner_internal__property_sheet_flag_value',
      'QDesignerWidgetItemInstaller': '_qdesigner_internal__q_designer_widget_item_installer',
      'Selection': '_qdesigner_internal__selection',
      'SignalSlotDialogData': '_qdesigner_internal__signal_slot_dialog_data',
      'DesignerMetaEnum': '_qdesigner_internal__designer_meta_enum',
      'DesignerMetaFlags': '_qdesigner_internal__designer_meta_flags',
      'PropertySheetTranslatableData': '_qdesigner_internal__property_sheet_translatable_data',
      'CECommand': '_qdesigner_internal__c_e_command',
      'PropertySheetStringListValue': '_qdesigner_internal__property_sheet_string_list_value',
      'PropertySheetStringValue': '_qdesigner_internal__property_sheet_string_value',
      'AddConnectionCommand': '_qdesigner_internal__add_connection_command',
      'DeleteConnectionsCommand': '_qdesigner_internal__delete_connections_command',
      'DesignerIconCache': '_qdesigner_internal__designer_icon_cache',
      'DesignerPixmapCache': '_qdesigner_internal__designer_pixmap_cache',
      'PreviewConfiguration': '_qdesigner_internal__preview_configuration',
      'PropertySheetKeySequenceValue': '_qdesigner_internal__property_sheet_key_sequence_value',
      'QDesignerIntrospection': '_qdesigner_internal__q_designer_introspection',
      'Connection': '_qdesigner_internal__connection',
      'CssHighlighter': '_qdesigner_internal__css_highlighter',
      'PropertySheetIconValue': '_qdesigner_internal__property_sheet_icon_value',
      'ActionRepositoryMimeData': '_qdesigner_internal__action_repository_mime_data',
      'SignatureModel': '_qdesigner_internal__signature_model',
      'SpecialMenuAction': '_qdesigner_internal__special_menu_action',
      'WidgetDataBaseItem': '_qdesigner_internal__widget_data_base_item',
      'FormBuilderClipboard': '_qdesigner_internal__form_builder_clipboard',
      'Grid': '_qdesigner_internal__grid',
      'GridPanel': '_qdesigner_internal__grid_panel',
      'IconThemeEditor': '_qdesigner_internal__icon_theme_editor',
      'IconThemeEnumEditor': '_qdesigner_internal__icon_theme_enum_editor',
      'InvisibleWidget': '_qdesigner_internal__invisible_widget',
      'QDesignerDnDItem': '_qdesigner_internal__q_designer_dn_d_item',
      'QDesignerMimeData': '_qdesigner_internal__q_designer_mime_data',
      'TextPropertyEditor': '_qdesigner_internal__text_property_editor',
      'UpdateBlocker': '_qdesigner_internal__update_blocker',
      'MetaDataBaseItem': '_qdesigner_internal__meta_data_base_item',
      'QDesignerWidgetBox': '_qdesigner_internal__q_designer_widget_box',
      'ConnectionEdit': '_qdesigner_internal__connection_edit',
      'CursorSelectionState': '_qdesigner_internal__cursor_selection_state',
      'FormLayoutMenu': '_qdesigner_internal__form_layout_menu',
      'Layout': '_qdesigner_internal__layout',
      'ManageWidgetCommandHelper': '_qdesigner_internal__manage_widget_command_helper',
      'MorphMenu': '_qdesigner_internal__morph_menu',
      'NewPromotedClassPanel': '_qdesigner_internal__new_promoted_class_panel',
      'PreviewManager': '_qdesigner_internal__preview_manager',
      'QDesignerFormWindowCommand': '_qdesigner_internal__q_designer_form_window_command',
      'QLayoutSupport': '_qdesigner_internal__q_layout_support',
      'ToolBarEventFilter': '_qdesigner_internal__tool_bar_event_filter',
      'ZoomMenu': '_qdesigner_internal__zoom_menu',
      'ActionInsertionCommand': '_qdesigner_internal__action_insertion_command',
      'AddActionCommand': '_qdesigner_internal__add_action_command',
      'AdjustWidgetSizeCommand': '_qdesigner_internal__adjust_widget_size_command',
      'BreakLayoutCommand': '_qdesigner_internal__break_layout_command',
      'ChangeCurrentPageCommand': '_qdesigner_internal__change_current_page_command',
      'ChangeLayoutItemGeometry': '_qdesigner_internal__change_layout_item_geometry',
      'ChangeZOrderCommand': '_qdesigner_internal__change_z_order_command',
      'ContainerWidgetCommand': '_qdesigner_internal__container_widget_command',
      'CreateSubmenuCommand': '_qdesigner_internal__create_submenu_command',
      'DeleteMenuBarCommand': '_qdesigner_internal__delete_menu_bar_command',
      'DeleteStatusBarCommand': '_qdesigner_internal__delete_status_bar_command',
      'DeleteToolBarCommand': '_qdesigner_internal__delete_tool_bar_command',
      'DeleteWidgetCommand': '_qdesigner_internal__delete_widget_command',
      'DemoteFromCustomWidgetCommand': '_qdesigner_internal__demote_from_custom_widget_command',
      'DockWidgetCommand': '_qdesigner_internal__dock_widget_command',
      'InsertWidgetCommand': '_qdesigner_internal__insert_widget_command',
      'LayoutCommand': '_qdesigner_internal__layout_command',
      'MenuActionCommand': '_qdesigner_internal__menu_action_command',
      'PromoteToCustomWidgetCommand': '_qdesigner_internal__promote_to_custom_widget_command',
      'QDesignerFormWindowManager': '_qdesigner_internal__q_designer_form_window_manager',
      'QDesignerObjectInspector': '_qdesigner_internal__q_designer_object_inspector',
      'RemoveActionCommand': '_qdesigner_internal__remove_action_command',
      'ReparentWidgetCommand': '_qdesigner_internal__reparent_widget_command',
      'StackedWidgetCommand': '_qdesigner_internal__stacked_widget_command',
      'TabOrderCommand': '_qdesigner_internal__tab_order_command',
      'TabWidgetCommand': '_qdesigner_internal__tab_widget_command',
      'ToolBoxCommand': '_qdesigner_internal__tool_box_command',
      'AddContainerWidgetPageCommand': '_qdesigner_internal__add_container_widget_page_command',
      'AddDockWidgetCommand': '_qdesigner_internal__add_dock_widget_command',
      'AddMenuActionCommand': '_qdesigner_internal__add_menu_action_command',
      'AddStackedWidgetPageCommand': '_qdesigner_internal__add_stacked_widget_page_command',
      'AddTabPageCommand': '_qdesigner_internal__add_tab_page_command',
      'AddToolBarCommand': '_qdesigner_internal__add_tool_bar_command',
      'AddToolBoxPageCommand': '_qdesigner_internal__add_tool_box_page_command',
      'CodeDialog': '_qdesigner_internal__code_dialog',
      'CreateMenuBarCommand': '_qdesigner_internal__create_menu_bar_command',
      'CreateStatusBarCommand': '_qdesigner_internal__create_status_bar_command',
      'DeleteContainerWidgetPageCommand': '_qdesigner_internal__delete_container_widget_page_command',
      'DeleteStackedWidgetPageCommand': '_qdesigner_internal__delete_stacked_widget_page_command',
      'DeleteTabPageCommand': '_qdesigner_internal__delete_tab_page_command',
      'DeleteToolBoxPageCommand': '_qdesigner_internal__delete_tool_box_page_command',
      'InsertActionIntoCommand': '_qdesigner_internal__insert_action_into_command',
      'LowerWidgetCommand': '_qdesigner_internal__lower_widget_command',
      'MoveStackedWidgetCommand': '_qdesigner_internal__move_stacked_widget_command',
      'MoveTabPageCommand': '_qdesigner_internal__move_tab_page_command',
      'MoveToolBoxPageCommand': '_qdesigner_internal__move_tool_box_page_command',
      'NewActionDialog': '_qdesigner_internal__new_action_dialog',
      'RaiseWidgetCommand': '_qdesigner_internal__raise_widget_command',
      'RemoveActionFromCommand': '_qdesigner_internal__remove_action_from_command',
      'RemoveMenuActionCommand': '_qdesigner_internal__remove_menu_action_command',
      'HtmlHighlighter': '_qdesigner_internal__html_highlighter',
      'StyleSheetEditor': '_qdesigner_internal__style_sheet_editor',
      'ActionListView': '_qdesigner_internal__action_list_view',
      'SignaturePanel': '_qdesigner_internal__signature_panel',
      'ActionTreeView': '_qdesigner_internal__action_tree_view',
      'DialogGui': '_qdesigner_internal__dialog_gui',
      'MenuActionLineEdit': '_qdesigner_internal__menu_action_line_edit',
      'PropertyLineEdit': '_qdesigner_internal__property_line_edit',
      'SheetDelegate': '_qdesigner_internal__sheet_delegate',
      'ZoomProxyWidget': '_qdesigner_internal__zoom_proxy_widget',
      'ZoomView': '_qdesigner_internal__zoom_view',
      'ActionEditor': '_qdesigner_internal__action_editor',
      'ActionModel': '_qdesigner_internal__action_model',
      'ActionView': '_qdesigner_internal__action_view',
      'ChangeFormLayoutItemRoleCommand': '_qdesigner_internal__change_form_layout_item_role_command',
      'ChangeListContentsCommand': '_qdesigner_internal__change_list_contents_command',
      'ChangeTreeContentsCommand': '_qdesigner_internal__change_tree_contents_command',
      'DeviceProfile': '_qdesigner_internal__device_profile',
      'FormWindowBase': '_qdesigner_internal__form_window_base',
      'IconSelector': '_qdesigner_internal__icon_selector',
      'ItemData': '_qdesigner_internal__item_data',
      'LanguageResourceDialog': '_qdesigner_internal__language_resource_dialog',
      'LayoutAlignmentCommand': '_qdesigner_internal__layout_alignment_command',
      'LayoutHelper': '_qdesigner_internal__layout_helper',
      'LayoutInfo': '_qdesigner_internal__layout_info',
      'LayoutProperties': '_qdesigner_internal__layout_properties',
      'ListContents': '_qdesigner_internal__list_contents',
      'MetaDataBase': '_qdesigner_internal__meta_data_base',
      'MorphLayoutCommand': '_qdesigner_internal__morph_layout_command',
      'OrderDialog': '_qdesigner_internal__order_dialog',
      'PlainTextEditorDialog': '_qdesigner_internal__plain_text_editor_dialog',
      'PreviewConfigurationWidget': '_qdesigner_internal__preview_configuration_widget',
      'PromotionModel': '_qdesigner_internal__promotion_model',
      'PromotionTaskMenu': '_qdesigner_internal__promotion_task_menu',
      'PropertySheetPixmapValue': '_qdesigner_internal__property_sheet_pixmap_value',
      'QDesignerFormEditorCommand': '_qdesigner_internal__q_designer_form_editor_command',
      'QDesignerPromotion': '_qdesigner_internal__q_designer_promotion',
      'QDesignerPromotionDialog': '_qdesigner_internal__q_designer_promotion_dialog',
      'QDesignerPropertyEditor': '_qdesigner_internal__q_designer_property_editor',
      'QDesignerSharedSettings': '_qdesigner_internal__q_designer_shared_settings',
      'QDesignerTaskMenu': '_qdesigner_internal__q_designer_task_menu',
      'QDesignerWidgetItem': '_qdesigner_internal__q_designer_widget_item',
      'RichTextEditorDialog': '_qdesigner_internal__rich_text_editor_dialog',
      'SelectSignalDialog': '_qdesigner_internal__select_signal_dialog',
      'SignalSlotDialog': '_qdesigner_internal__signal_slot_dialog',
      'SimplifyLayoutCommand': '_qdesigner_internal__simplify_layout_command',
      'StyleSheetEditorDialog': '_qdesigner_internal__style_sheet_editor_dialog',
      'TreeWidgetContents': '_qdesigner_internal__tree_widget_contents',
      'WidgetDataBase': '_qdesigner_internal__widget_data_base',
      'WidgetFactory': '_qdesigner_internal__widget_factory',
      'ZoomWidget': '_qdesigner_internal__zoom_widget',
      'ChangeTableContentsCommand': '_qdesigner_internal__change_table_contents_command',
      'NewFormWidget': '_qdesigner_internal__new_form_widget',
      'StyleSheetPropertyEditorDialog': '_qdesigner_internal__style_sheet_property_editor_dialog',
      'TableWidgetContents': '_qdesigner_internal__table_widget_contents',
      'QSimpleResource': '_qdesigner_internal__q_simple_resource',
      'QDesignerFormBuilder': '_qdesigner_internal__q_designer_form_builder',
      'QEditorFormBuilder': '_qdesigner_internal__q_editor_form_builder',
      'NewFormWidgetFormBuilder': '_qdesigner_internal__new_form_widget_form_builder',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'qdesigner_internal.ActionData'. Python calls this for a
    name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
