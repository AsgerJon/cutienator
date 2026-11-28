"""
The 'cutienator.QtDesigner' package provides the cute classes of the
part of Qt named QtDesigner, under the name PySide6 has for it.

  from cutienator.QtDesigner import QDesignerDnDItemInterface, QDesignerMetaMethodInterface

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
    'QDesignerDnDItemInterface',
    'QDesignerMetaMethodInterface',
    'QDesignerTaskMenuExtension',
    'QFormBuilderStrings',
    'QDesignerCustomWidgetData',
    'QDesignerMemberSheetExtension',
    'QDesignerMetaEnumInterface',
    'QDesignerMetaObjectInterface',
    'QDesignerPromotionInterface',
    'QAbstractExtensionFactory',
    'QDesignerDynamicPropertySheetExtension',
    'QDesignerIntrospectionInterface',
    'QDesignerMemberSheet',
    'QDesignerMetaDataBaseInterface',
    'QDesignerMetaPropertyInterface',
    'QDesignerPropertySheetExtension',
    'QDesignerSettingsInterface',
    'QtResourceModel',
    'QtResourceSet',
    'RCCResourceLibrary',
    'QAbstractExtensionManager',
    'QDesignerPropertySheet',
    'QDesignerQSettings',
    'DomActionRef',
    'DomChar',
    'DomColor',
    'DomConnectionHint',
    'DomDate',
    'DomDateTime',
    'DomFont',
    'DomHeader',
    'DomInclude',
    'DomLayoutDefault',
    'DomLayoutFunction',
    'DomLocale',
    'DomPoint',
    'DomPointF',
    'DomPropertyToolTip',
    'DomRect',
    'DomRectF',
    'DomResource',
    'DomResourcePixmap',
    'DomSize',
    'DomSizeF',
    'DomSizePolicy',
    'DomSlots',
    'DomString',
    'DomStringList',
    'DomStringPropertySpecification',
    'DomTabStops',
    'DomTime',
    'QDockWidgetPropertySheet',
    'QExtensionManager',
    'DomConnectionHints',
    'DomGradientStop',
    'DomIncludes',
    'DomPropertySpecifications',
    'DomResourceIcon',
    'DomResources',
    'DomUrl',
    'QExtensionFactory',
    'DomConnection',
    'DomCustomWidget',
    'DomGradient',
    'QDesignerAbstractPropertySheetFactory',
    'QDesignerMemberSheetFactory',
    'DomBrush',
    'DomColorRole',
    'DomColorGroup',
    'DomPalette',
    'DomProperty',
    'DomConnections',
    'DomCustomWidgets',
    'DomAction',
    'DomButtonGroup',
    'DomColumn',
    'DomDesignerData',
    'DomItem',
    'DomRow',
    'DomSpacer',
    'QResourceBuilder',
    'QTextBuilder',
    'DomActionGroup',
    'DomButtonGroups',
    'QDesignerWidgetDataBaseItemInterface',
    'DomLayout',
    'DomWidget',
    'DomLayoutItem',
    'QDesignerActionProviderExtension',
    'QDesignerWidgetDataBaseInterface',
    'DomUI',
    'QDesignerExtraInfoExtension',
    'QAbstractFormBuilderGadget',
    'QDesignerContainerExtension',
    'QDesignerFormWindowCursorInterface',
    'QDesignerFormWindowToolInterface',
    'QDesignerLayoutDecorationExtension',
    'QDesignerMetaDataBaseItemInterface',
    'QDesignerOptionsPageInterface',
    'QDesignerPropertyEditorInterface',
    'QDesignerResourceBrowserInterface',
    'QDesignerWidgetBoxInterface',
    'QDesignerWidgetFactoryInterface',
    'Spacer',
    'QDesignerFormWindowInterface',
    'Line',
    'QDesignerActionEditorInterface',
    'QDesignerDockWidget',
    'QDesignerFormWindowManagerInterface',
    'QDesignerMenu',
    'QDesignerObjectInspectorInterface',
    'QDesignerWidget',
    'QLayoutWidget',
    'QDesignerMenuBar',
    'QFormBuilderExtra',
    'QStackedWidgetPreviewEventFilter',
    'QStackedWidgetPropertySheet',
    'QTabWidgetEventFilter',
    'QTabWidgetPropertySheet',
    'QToolBoxHelper',
    'QToolBoxWidgetPropertySheet',
    'QDesignerDialog',
    'QStackedWidgetEventFilter',
    'QDesignerDialogGuiInterface',
    'QDesignerFormEditorInterface',
    'QDesignerIntegrationInterface',
    'QDesignerPluginManager',
    'QDesignerComponents',
    'QDesignerFormEditorPluginInterface',
    'QDesignerIntegration',
    'QDesignerLanguageExtension',
    'QDesignerNewFormWidgetInterface',
    'QtResourceEditorDialog',
    'QtResourceView',
    'QtResourceViewDialog',
    'QAbstractFormBuilder',
    'QFormBuilder',
    'qdesigner_internal',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_designer_dn_d_item_interface import QDesignerDnDItemInterface
  from ._q_designer_meta_method_interface import QDesignerMetaMethodInterface
  from ._q_designer_task_menu_extension import QDesignerTaskMenuExtension
  from ._q_form_builder_strings import QFormBuilderStrings
  from ._q_designer_custom_widget_data import QDesignerCustomWidgetData
  from ._q_designer_member_sheet_extension import QDesignerMemberSheetExtension
  from ._q_designer_meta_enum_interface import QDesignerMetaEnumInterface
  from ._q_designer_meta_object_interface import QDesignerMetaObjectInterface
  from ._q_designer_promotion_interface import QDesignerPromotionInterface
  from ._q_abstract_extension_factory import QAbstractExtensionFactory
  from ._q_designer_dynamic_property_sheet_extension import QDesignerDynamicPropertySheetExtension
  from ._q_designer_introspection_interface import QDesignerIntrospectionInterface
  from ._q_designer_member_sheet import QDesignerMemberSheet
  from ._q_designer_meta_data_base_interface import QDesignerMetaDataBaseInterface
  from ._q_designer_meta_property_interface import QDesignerMetaPropertyInterface
  from ._q_designer_property_sheet_extension import QDesignerPropertySheetExtension
  from ._q_designer_settings_interface import QDesignerSettingsInterface
  from ._qt_resource_model import QtResourceModel
  from ._qt_resource_set import QtResourceSet
  from ._r_c_c_resource_library import RCCResourceLibrary
  from ._q_abstract_extension_manager import QAbstractExtensionManager
  from ._q_designer_property_sheet import QDesignerPropertySheet
  from ._q_designer_q_settings import QDesignerQSettings
  from ._dom_action_ref import DomActionRef
  from ._dom_char import DomChar
  from ._dom_color import DomColor
  from ._dom_connection_hint import DomConnectionHint
  from ._dom_date import DomDate
  from ._dom_date_time import DomDateTime
  from ._dom_font import DomFont
  from ._dom_header import DomHeader
  from ._dom_include import DomInclude
  from ._dom_layout_default import DomLayoutDefault
  from ._dom_layout_function import DomLayoutFunction
  from ._dom_locale import DomLocale
  from ._dom_point import DomPoint
  from ._dom_point_f import DomPointF
  from ._dom_property_tool_tip import DomPropertyToolTip
  from ._dom_rect import DomRect
  from ._dom_rect_f import DomRectF
  from ._dom_resource import DomResource
  from ._dom_resource_pixmap import DomResourcePixmap
  from ._dom_size import DomSize
  from ._dom_size_f import DomSizeF
  from ._dom_size_policy import DomSizePolicy
  from ._dom_slots import DomSlots
  from ._dom_string import DomString
  from ._dom_string_list import DomStringList
  from ._dom_string_property_specification import DomStringPropertySpecification
  from ._dom_tab_stops import DomTabStops
  from ._dom_time import DomTime
  from ._q_dock_widget_property_sheet import QDockWidgetPropertySheet
  from ._q_extension_manager import QExtensionManager
  from ._dom_connection_hints import DomConnectionHints
  from ._dom_gradient_stop import DomGradientStop
  from ._dom_includes import DomIncludes
  from ._dom_property_specifications import DomPropertySpecifications
  from ._dom_resource_icon import DomResourceIcon
  from ._dom_resources import DomResources
  from ._dom_url import DomUrl
  from ._q_extension_factory import QExtensionFactory
  from ._dom_connection import DomConnection
  from ._dom_custom_widget import DomCustomWidget
  from ._dom_gradient import DomGradient
  from ._q_designer_abstract_property_sheet_factory import QDesignerAbstractPropertySheetFactory
  from ._q_designer_member_sheet_factory import QDesignerMemberSheetFactory
  from ._dom_brush import DomBrush
  from ._dom_color_role import DomColorRole
  from ._dom_color_group import DomColorGroup
  from ._dom_palette import DomPalette
  from ._dom_property import DomProperty
  from ._dom_connections import DomConnections
  from ._dom_custom_widgets import DomCustomWidgets
  from ._dom_action import DomAction
  from ._dom_button_group import DomButtonGroup
  from ._dom_column import DomColumn
  from ._dom_designer_data import DomDesignerData
  from ._dom_item import DomItem
  from ._dom_row import DomRow
  from ._dom_spacer import DomSpacer
  from ._q_resource_builder import QResourceBuilder
  from ._q_text_builder import QTextBuilder
  from ._dom_action_group import DomActionGroup
  from ._dom_button_groups import DomButtonGroups
  from ._q_designer_widget_data_base_item_interface import QDesignerWidgetDataBaseItemInterface
  from ._dom_layout import DomLayout
  from ._dom_widget import DomWidget
  from ._dom_layout_item import DomLayoutItem
  from ._q_designer_action_provider_extension import QDesignerActionProviderExtension
  from ._q_designer_widget_data_base_interface import QDesignerWidgetDataBaseInterface
  from ._dom_u_i import DomUI
  from ._q_designer_extra_info_extension import QDesignerExtraInfoExtension
  from ._q_abstract_form_builder_gadget import QAbstractFormBuilderGadget
  from ._q_designer_container_extension import QDesignerContainerExtension
  from ._q_designer_form_window_cursor_interface import QDesignerFormWindowCursorInterface
  from ._q_designer_form_window_tool_interface import QDesignerFormWindowToolInterface
  from ._q_designer_layout_decoration_extension import QDesignerLayoutDecorationExtension
  from ._q_designer_meta_data_base_item_interface import QDesignerMetaDataBaseItemInterface
  from ._q_designer_options_page_interface import QDesignerOptionsPageInterface
  from ._q_designer_property_editor_interface import QDesignerPropertyEditorInterface
  from ._q_designer_resource_browser_interface import QDesignerResourceBrowserInterface
  from ._q_designer_widget_box_interface import QDesignerWidgetBoxInterface
  from ._q_designer_widget_factory_interface import QDesignerWidgetFactoryInterface
  from ._spacer import Spacer
  from ._q_designer_form_window_interface import QDesignerFormWindowInterface
  from ._line import Line
  from ._q_designer_action_editor_interface import QDesignerActionEditorInterface
  from ._q_designer_dock_widget import QDesignerDockWidget
  from ._q_designer_form_window_manager_interface import QDesignerFormWindowManagerInterface
  from ._q_designer_menu import QDesignerMenu
  from ._q_designer_object_inspector_interface import QDesignerObjectInspectorInterface
  from ._q_designer_widget import QDesignerWidget
  from ._q_layout_widget import QLayoutWidget
  from ._q_designer_menu_bar import QDesignerMenuBar
  from ._q_form_builder_extra import QFormBuilderExtra
  from ._q_stacked_widget_preview_event_filter import QStackedWidgetPreviewEventFilter
  from ._q_stacked_widget_property_sheet import QStackedWidgetPropertySheet
  from ._q_tab_widget_event_filter import QTabWidgetEventFilter
  from ._q_tab_widget_property_sheet import QTabWidgetPropertySheet
  from ._q_tool_box_helper import QToolBoxHelper
  from ._q_tool_box_widget_property_sheet import QToolBoxWidgetPropertySheet
  from ._q_designer_dialog import QDesignerDialog
  from ._q_stacked_widget_event_filter import QStackedWidgetEventFilter
  from ._q_designer_dialog_gui_interface import QDesignerDialogGuiInterface
  from ._q_designer_form_editor_interface import QDesignerFormEditorInterface
  from ._q_designer_integration_interface import QDesignerIntegrationInterface
  from ._q_designer_plugin_manager import QDesignerPluginManager
  from ._q_designer_components import QDesignerComponents
  from ._q_designer_form_editor_plugin_interface import QDesignerFormEditorPluginInterface
  from ._q_designer_integration import QDesignerIntegration
  from ._q_designer_language_extension import QDesignerLanguageExtension
  from ._q_designer_new_form_widget_interface import QDesignerNewFormWidgetInterface
  from ._qt_resource_editor_dialog import QtResourceEditorDialog
  from ._qt_resource_view import QtResourceView
  from ._qt_resource_view_dialog import QtResourceViewDialog
  from ._q_abstract_form_builder import QAbstractFormBuilder
  from ._q_form_builder import QFormBuilder
  from . import qdesigner_internal
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QDesignerDnDItemInterface': '_q_designer_dn_d_item_interface',
      'QDesignerMetaMethodInterface': '_q_designer_meta_method_interface',
      'QDesignerTaskMenuExtension': '_q_designer_task_menu_extension',
      'QFormBuilderStrings': '_q_form_builder_strings',
      'QDesignerCustomWidgetData': '_q_designer_custom_widget_data',
      'QDesignerMemberSheetExtension': '_q_designer_member_sheet_extension',
      'QDesignerMetaEnumInterface': '_q_designer_meta_enum_interface',
      'QDesignerMetaObjectInterface': '_q_designer_meta_object_interface',
      'QDesignerPromotionInterface': '_q_designer_promotion_interface',
      'QAbstractExtensionFactory': '_q_abstract_extension_factory',
      'QDesignerDynamicPropertySheetExtension': '_q_designer_dynamic_property_sheet_extension',
      'QDesignerIntrospectionInterface': '_q_designer_introspection_interface',
      'QDesignerMemberSheet': '_q_designer_member_sheet',
      'QDesignerMetaDataBaseInterface': '_q_designer_meta_data_base_interface',
      'QDesignerMetaPropertyInterface': '_q_designer_meta_property_interface',
      'QDesignerPropertySheetExtension': '_q_designer_property_sheet_extension',
      'QDesignerSettingsInterface': '_q_designer_settings_interface',
      'QtResourceModel': '_qt_resource_model',
      'QtResourceSet': '_qt_resource_set',
      'RCCResourceLibrary': '_r_c_c_resource_library',
      'QAbstractExtensionManager': '_q_abstract_extension_manager',
      'QDesignerPropertySheet': '_q_designer_property_sheet',
      'QDesignerQSettings': '_q_designer_q_settings',
      'DomActionRef': '_dom_action_ref',
      'DomChar': '_dom_char',
      'DomColor': '_dom_color',
      'DomConnectionHint': '_dom_connection_hint',
      'DomDate': '_dom_date',
      'DomDateTime': '_dom_date_time',
      'DomFont': '_dom_font',
      'DomHeader': '_dom_header',
      'DomInclude': '_dom_include',
      'DomLayoutDefault': '_dom_layout_default',
      'DomLayoutFunction': '_dom_layout_function',
      'DomLocale': '_dom_locale',
      'DomPoint': '_dom_point',
      'DomPointF': '_dom_point_f',
      'DomPropertyToolTip': '_dom_property_tool_tip',
      'DomRect': '_dom_rect',
      'DomRectF': '_dom_rect_f',
      'DomResource': '_dom_resource',
      'DomResourcePixmap': '_dom_resource_pixmap',
      'DomSize': '_dom_size',
      'DomSizeF': '_dom_size_f',
      'DomSizePolicy': '_dom_size_policy',
      'DomSlots': '_dom_slots',
      'DomString': '_dom_string',
      'DomStringList': '_dom_string_list',
      'DomStringPropertySpecification': '_dom_string_property_specification',
      'DomTabStops': '_dom_tab_stops',
      'DomTime': '_dom_time',
      'QDockWidgetPropertySheet': '_q_dock_widget_property_sheet',
      'QExtensionManager': '_q_extension_manager',
      'DomConnectionHints': '_dom_connection_hints',
      'DomGradientStop': '_dom_gradient_stop',
      'DomIncludes': '_dom_includes',
      'DomPropertySpecifications': '_dom_property_specifications',
      'DomResourceIcon': '_dom_resource_icon',
      'DomResources': '_dom_resources',
      'DomUrl': '_dom_url',
      'QExtensionFactory': '_q_extension_factory',
      'DomConnection': '_dom_connection',
      'DomCustomWidget': '_dom_custom_widget',
      'DomGradient': '_dom_gradient',
      'QDesignerAbstractPropertySheetFactory': '_q_designer_abstract_property_sheet_factory',
      'QDesignerMemberSheetFactory': '_q_designer_member_sheet_factory',
      'DomBrush': '_dom_brush',
      'DomColorRole': '_dom_color_role',
      'DomColorGroup': '_dom_color_group',
      'DomPalette': '_dom_palette',
      'DomProperty': '_dom_property',
      'DomConnections': '_dom_connections',
      'DomCustomWidgets': '_dom_custom_widgets',
      'DomAction': '_dom_action',
      'DomButtonGroup': '_dom_button_group',
      'DomColumn': '_dom_column',
      'DomDesignerData': '_dom_designer_data',
      'DomItem': '_dom_item',
      'DomRow': '_dom_row',
      'DomSpacer': '_dom_spacer',
      'QResourceBuilder': '_q_resource_builder',
      'QTextBuilder': '_q_text_builder',
      'DomActionGroup': '_dom_action_group',
      'DomButtonGroups': '_dom_button_groups',
      'QDesignerWidgetDataBaseItemInterface': '_q_designer_widget_data_base_item_interface',
      'DomLayout': '_dom_layout',
      'DomWidget': '_dom_widget',
      'DomLayoutItem': '_dom_layout_item',
      'QDesignerActionProviderExtension': '_q_designer_action_provider_extension',
      'QDesignerWidgetDataBaseInterface': '_q_designer_widget_data_base_interface',
      'DomUI': '_dom_u_i',
      'QDesignerExtraInfoExtension': '_q_designer_extra_info_extension',
      'QAbstractFormBuilderGadget': '_q_abstract_form_builder_gadget',
      'QDesignerContainerExtension': '_q_designer_container_extension',
      'QDesignerFormWindowCursorInterface': '_q_designer_form_window_cursor_interface',
      'QDesignerFormWindowToolInterface': '_q_designer_form_window_tool_interface',
      'QDesignerLayoutDecorationExtension': '_q_designer_layout_decoration_extension',
      'QDesignerMetaDataBaseItemInterface': '_q_designer_meta_data_base_item_interface',
      'QDesignerOptionsPageInterface': '_q_designer_options_page_interface',
      'QDesignerPropertyEditorInterface': '_q_designer_property_editor_interface',
      'QDesignerResourceBrowserInterface': '_q_designer_resource_browser_interface',
      'QDesignerWidgetBoxInterface': '_q_designer_widget_box_interface',
      'QDesignerWidgetFactoryInterface': '_q_designer_widget_factory_interface',
      'Spacer': '_spacer',
      'QDesignerFormWindowInterface': '_q_designer_form_window_interface',
      'Line': '_line',
      'QDesignerActionEditorInterface': '_q_designer_action_editor_interface',
      'QDesignerDockWidget': '_q_designer_dock_widget',
      'QDesignerFormWindowManagerInterface': '_q_designer_form_window_manager_interface',
      'QDesignerMenu': '_q_designer_menu',
      'QDesignerObjectInspectorInterface': '_q_designer_object_inspector_interface',
      'QDesignerWidget': '_q_designer_widget',
      'QLayoutWidget': '_q_layout_widget',
      'QDesignerMenuBar': '_q_designer_menu_bar',
      'QFormBuilderExtra': '_q_form_builder_extra',
      'QStackedWidgetPreviewEventFilter': '_q_stacked_widget_preview_event_filter',
      'QStackedWidgetPropertySheet': '_q_stacked_widget_property_sheet',
      'QTabWidgetEventFilter': '_q_tab_widget_event_filter',
      'QTabWidgetPropertySheet': '_q_tab_widget_property_sheet',
      'QToolBoxHelper': '_q_tool_box_helper',
      'QToolBoxWidgetPropertySheet': '_q_tool_box_widget_property_sheet',
      'QDesignerDialog': '_q_designer_dialog',
      'QStackedWidgetEventFilter': '_q_stacked_widget_event_filter',
      'QDesignerDialogGuiInterface': '_q_designer_dialog_gui_interface',
      'QDesignerFormEditorInterface': '_q_designer_form_editor_interface',
      'QDesignerIntegrationInterface': '_q_designer_integration_interface',
      'QDesignerPluginManager': '_q_designer_plugin_manager',
      'QDesignerComponents': '_q_designer_components',
      'QDesignerFormEditorPluginInterface': '_q_designer_form_editor_plugin_interface',
      'QDesignerIntegration': '_q_designer_integration',
      'QDesignerLanguageExtension': '_q_designer_language_extension',
      'QDesignerNewFormWidgetInterface': '_q_designer_new_form_widget_interface',
      'QtResourceEditorDialog': '_qt_resource_editor_dialog',
      'QtResourceView': '_qt_resource_view',
      'QtResourceViewDialog': '_qt_resource_view_dialog',
      'QAbstractFormBuilder': '_q_abstract_form_builder',
      'QFormBuilder': '_q_form_builder',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('qdesigner_internal',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtDesigner import QFormBuilder'. Python calls
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
