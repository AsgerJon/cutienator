"""
The 'cutienator.QtWidgets' package provides the cute classes of the part
of Qt named QtWidgets, under the name PySide6 has for it.

  from cutienator.QtWidgets import QEffects, QGraphicsItemCache

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
    'QEffects',
    'QGraphicsItemCache',
    'QIndexMapper',
    'QItemViewPaintPair',
    'QLayoutStruct',
    'QListViewLayoutInfo',
    'QPixmapStyleDescriptor',
    'QPixmapStylePixmap',
    'QScrollerPropertiesPrivate',
    'QSimplexConstraint',
    'QSimplexVariable',
    'QSpanCollection',
    'QStyleHintReturn',
    'QTLWExtra',
    'QTableWidgetSelectionRange',
    'QTileRules',
    'QToolBarAreaLayoutLine',
    'QTreeViewItem',
    'QWExtra',
    'QWidgetData',
    'QConcreteSimplexVariable',
    'QMatchData',
    'QSimplex',
    'QStyleHintReturnMask',
    'QStyleHintReturnVariant',
    'QSplitterLayoutStruct',
    'QBspTree',
    'QLayoutItem',
    'QListViewItem',
    'QStyleFactory',
    'QColormap',
    'QFileDialogArgs',
    'QToolBarAreaLayoutItem',
    'QButtonGroupPrivate',
    'QGesturePrivate',
    'QScrollerProperties',
    'QSizePolicy',
    'QStylePlugin',
    'QStyleSheetStyleCaches',
    'QTableWidgetMimeData',
    'QTreeModelPrivate',
    'QWidgetItemData',
    'QCompletionModelPrivate',
    'QFlickGesturePrivate',
    'QGesture',
    'QPanGesturePrivate',
    'QPinchGesturePrivate',
    'QScroller',
    'QSpacerItem',
    'QStyleAnimation',
    'QSwipeGesturePrivate',
    'QTapAndHoldGesturePrivate',
    'QTapGesturePrivate',
    'QBlendStyleAnimation',
    'QFlickGesture',
    'QGestureRecognizer',
    'QGraphicsEffect',
    'QGraphicsEffectSourcePrivate',
    'QGraphicsEffectSource',
    'QGraphicsEffectPrivate',
    'QNumberStyleAnimation',
    'QPanGesture',
    'QPinchGesture',
    'QPixmapFilter',
    'QProgressStyleAnimation',
    'QSwipeGesture',
    'QTapAndHoldGesture',
    'QTapGesture',
    'QUpdateLaterEvent',
    'QFlickGestureRecognizer',
    'QGraphicsBlurEffect',
    'QGraphicsBlurEffectPrivate',
    'QGraphicsColorizeEffect',
    'QGraphicsColorizeEffectPrivate',
    'QGraphicsDropShadowEffect',
    'QGraphicsDropShadowEffectPrivate',
    'QGraphicsOpacityEffect',
    'QGraphicsOpacityEffectPrivate',
    'QMacPanGestureRecognizer',
    'QMacPinchGestureRecognizer',
    'QMacSwipeGestureRecognizer',
    'QPanGestureRecognizer',
    'QPinchGestureRecognizer',
    'QPixmapColorizeFilter',
    'QPixmapConvolutionFilter',
    'QPixmapDropShadowFilter',
    'QScrollbarStyleAnimation',
    'QSwipeGestureRecognizer',
    'QTapAndHoldGestureRecognizer',
    'QTapGestureRecognizer',
    'QPixmapBlurFilter',
    'QFileIconProvider',
    'QPlainTextDocumentLayout',
    'QTextEditMimeData',
    'QTableWidgetItem',
    'QTableModelGreaterThan',
    'QTableModelLessThan',
    'QTableWidgetItemPrivate',
    'QUrlModel',
    'QtWidgetsActionPrivate',
    'QWidgetActionPrivate',
    'QWidget',
    'QStyleOption',
    'QStyle',
    'QWidgetRepaintManager',
    'QApplication',
    'QLayout',
    'QLayoutPrivate',
    'QStyleOptionComplex',
    'QStylePrivate',
    'QWidgetPrivate',
    'QAbstractButtonPrivate',
    'QAbstractItemDelegatePrivate',
    'QAbstractScrollAreaScrollBarContainer',
    'QAbstractSliderPrivate',
    'QAbstractSpinBoxPrivate',
    'QAccessibleMenuItem',
    'QAccessibleWidget',
    'QApplicationPrivate',
    'QBoxLayout',
    'QCachedPainter',
    'QCalendarWidget',
    'QColumnViewGripPrivate',
    'QDockWidgetLayout',
    'QDockWidgetPrivate',
    'QEditorInfo',
    'QFileIconProviderPrivate',
    'QFocusFrame',
    'QFormLayout',
    'QFramePrivate',
    'QGestureEvent',
    'QGraphicsSceneEvent',
    'QGridLayout',
    'QItemEditorCreatorBase',
    'QKeySequenceEditPrivate',
    'QLayoutStyleInfo',
    'QMenuBarPrivate',
    'QMovableTabWidget',
    'QPlaceHolderItem',
    'QRhiWidgetPrivate',
    'QScrollerPrivate',
    'QSizeGrip',
    'QSplashScreen',
    'QSplitterHandlePrivate',
    'QStackedLayout',
    'QStatusBar',
    'QStyleOptionButton',
    'QStyleOptionComboBox',
    'QStyleOptionDockWidget',
    'QStyleOptionFocusRect',
    'QStyleOptionFrame',
    'QStyleOptionGraphicsItem',
    'QStyleOptionGroupBox',
    'QStyleOptionHeader',
    'QStyleOptionMenuItem',
    'QStyleOptionProgressBar',
    'QStyleOptionRubberBand',
    'QStyleOptionSizeGrip',
    'QStyleOptionSlider',
    'QStyleOptionSpinBox',
    'QStyleOptionTab',
    'QStyleOptionTabBarBase',
    'QStyleOptionTabWidgetFrame',
    'QStyleOptionTitleBar',
    'QStyleOptionToolBar',
    'QStyleOptionToolBox',
    'QStyleOptionToolButton',
    'QStyleOptionViewItem',
    'QStylePainter',
    'QToolBarLayout',
    'QToolBarPrivate',
    'QToolTip',
    'QWellArray',
    'QWhatsThis',
    'QWidgetAction',
    'QWidgetEffectSourcePrivate',
    'QWidgetItem',
    'QWidgetPaintContext',
    'QWidgetResizeHandler',
    'QWidgetTextControl',
    'QWidgetTextControlPrivate',
    'QWidgetWindow',
    'QWindowContainer',
    'QAbstractButton',
    'QAbstractSlider',
    'QAccessibleWidgetV2',
    'QCalendarPopup',
    'QColorWell',
    'QColumnViewGrip',
    'QComboBoxPrivate',
    'QCommonStyle',
    'QCommonStylePrivate',
    'QDockWidget',
    'QFrame',
    'QGraphicsItemPaintInfo',
    'QGraphicsSceneContextMenuEvent',
    'QGraphicsSceneDragDropEvent',
    'QGraphicsSceneHelpEvent',
    'QGraphicsSceneHoverEvent',
    'QGraphicsSceneMouseEvent',
    'QGraphicsSceneMoveEvent',
    'QGraphicsSceneResizeEvent',
    'QGraphicsSceneWheelEvent',
    'QGroupBox',
    'QHBoxLayout',
    'QItemEditorFactory',
    'QKeySequenceEdit',
    'QLabelPrivate',
    'QMenu',
    'QMenuPrivate',
    'QProgressBar',
    'QRhiWidget',
    'QRubberBand',
    'QScrollBarPrivate',
    'QSplitterPrivate',
    'QStyleOptionHeaderV2',
    'QStyleOptionMenuItemV2',
    'QTabBar',
    'QToolBar',
    'QToolBarItem',
    'QVBoxLayout',
    'QWidgetItemV2',
    'QAccessibleAbstractScrollArea',
    'QAccessibleAbstractSlider',
    'QAccessibleAbstractSpinBox',
    'QAccessibleButton',
    'QAccessibleCalendarWidget',
    'QAccessibleColorWell',
    'QAccessibleComboBox',
    'QAccessibleDialogButtonBox',
    'QAccessibleDisplay',
    'QAccessibleDockWidget',
    'QAccessibleGroupBox',
    'QAccessibleLineEdit',
    'QAccessibleMainWindow',
    'QAccessibleMdiArea',
    'QAccessibleMdiSubWindow',
    'QAccessibleMenu',
    'QAccessibleMenuBar',
    'QAccessibleMessageBox',
    'QAccessibleStackedWidget',
    'QAccessibleTabBar',
    'QAccessibleTable',
    'QAccessibleTextWidget',
    'QAccessibleToolBox',
    'QAccessibleWindowContainer',
    'QButtonGroup',
    'QCheckBox',
    'QComboBoxPrivateScroller',
    'QDial',
    'QDialogButtonBox',
    'QDockWidgetGroupWindow',
    'QDockWidgetItem',
    'QFusionStylePrivate',
    'QGraphicsTransform',
    'QGraphicsItem',
    'QGraphicsItemGroup',
    'QGraphicsItemPrivate',
    'QGraphicsTransformPrivate',
    'QLCDNumber',
    'QLabel',
    'QMdiSubWindow',
    'QMenuBar',
    'QMenuSloppyState',
    'QPixmapStyle',
    'QPixmapStylePrivate',
    'QProxyStyle',
    'QProxyStylePrivate',
    'QPushButton',
    'QPushButtonPrivate',
    'QRadioButton',
    'QScrollBar',
    'QSlider',
    'QSplitter',
    'QStackedWidget',
    'QSystemTrayIcon',
    'QTabBarPrivate',
    'QTabWidget',
    'QToolBarAreaLayoutInfo',
    'QToolBarSeparator',
    'QToolBox',
    'QToolButton',
    'QUnicodeControlCharacterMenu',
    'QWindowsStylePrivate',
    'QAbstractGraphicsShapeItem',
    'QAbstractScrollAreaPrivate',
    'QAccessibleDial',
    'QAccessibleDoubleSpinBox',
    'QAccessibleList',
    'QAccessiblePlainTextEdit',
    'QAccessibleProgressBar',
    'QAccessibleScrollArea',
    'QAccessibleScrollBar',
    'QAccessibleSlider',
    'QAccessibleSpinBox',
    'QAccessibleTextEdit',
    'QAccessibleToolButton',
    'QAccessibleTree',
    'QBalloonTip',
    'QCommandLinkButton',
    'QDialog',
    'QDialogPrivate',
    'QDialogButtonBoxPrivate',
    'QDockWidgetGroupWindowItem',
    'QFusionStyle',
    'QGraphicsItemAnimation',
    'QGraphicsItemEffectSourcePrivate',
    'QGraphicsLayoutItem',
    'QGraphicsLayoutItemPrivate',
    'QGraphicsLineItem',
    'QGraphicsObject',
    'QGraphicsPixmapItem',
    'QGraphicsRotation',
    'QGraphicsScale',
    'QGraphicsSceneBspTree',
    'QLineEditIconButton',
    'QMainWindow',
    'QMdiSubWindowPrivate',
    'QSplitterHandle',
    'QSystemTrayIconPrivate',
    'QTipLabel',
    'QToolBarExtension',
    'QWindowsStyle',
    'QAbstractScrollArea',
    'QAbstractScrollAreaFilter',
    'QAccessibleTextBrowser',
    'QColorDialog',
    'QErrorMessage',
    'QFontDialog',
    'QGestureManager',
    'QGraphicsEllipseItem',
    'QGraphicsGridLayoutEngine',
    'QGraphicsGridLayoutEngineItem',
    'QGraphicsLayoutPrivate',
    'QGraphicsPathItem',
    'QGraphicsPolygonItem',
    'QGraphicsRectItem',
    'QGraphicsSimpleTextItem',
    'QGraphicsTextItem',
    'QMainWindowLayout',
    'QWidgetAnimator',
    'QMainWindowLayoutState',
    'QMessageBox',
    'QPlainTextEditPrivate',
    'QProgressDialog',
    'QScrollAreaPrivate',
    'QStyleSheetStyle',
    'QTextEditPrivate',
    'QWizard',
    'QWizardPage',
    'QAbstractItemDelegate',
    'QAbstractItemView',
    'QAbstractItemViewPrivate',
    'QDockAreaLayout',
    'QDockAreaLayoutInfo',
    'QFontDialogPrivate',
    'QGraphicsLayout',
    'QGraphicsLayoutStyleInfo',
    'QMdiArea',
    'QPlainTextEdit',
    'QScrollArea',
    'QTextEdit',
    'QToolBarAreaLayout',
    'QAccessibleTableCell',
    'QAccessibleTableCornerButton',
    'QAccessibleTableHeaderCell',
    'QColumnViewPreviewColumn',
    'QColumnViewPrivate',
    'QCompleter',
    'QDataWidgetMapper',
    'QDockAreaLayoutItem',
    'QFileDialog',
    'QGraphicsAnchorLayout',
    'QGraphicsGridLayout',
    'QGraphicsLinearLayout',
    'QGraphicsWidget',
    'QGraphicsScene',
    'QGraphicsWidgetPrivate',
    'QHeaderView',
    'QHeaderViewPrivate',
    'QItemDelegate',
    'QListView',
    'QListViewPrivate',
    'QMdiAreaPrivate',
    'QPlainTextEditControl',
    'QStyledItemDelegate',
    'QTextBrowser',
    'QTreeViewPrivate',
    'QColumnView',
    'QColumnViewDelegate',
    'QCommonListViewBase',
    'QCompleterItemDelegate',
    'QCompleterPrivate',
    'QFSCompleter',
    'QFileDialogPrivate',
    'QGraphicsAnchor',
    'QGraphicsAnchorLayoutPrivate',
    'QGraphicsProxyWidget',
    'QGraphicsProxyWidgetPrivate',
    'QGraphicsSceneIndexPrivate',
    'QGraphicsView',
    'QGraphicsViewPrivate',
    'QLineEdit',
    'QListWidget',
    'QListWidgetItem',
    'QListWidgetPrivate',
    'QSideBarDelegate',
    'QSidebar',
    'QTableViewPrivate',
    'QTreeView',
    'QUndoView',
    'QWidgetLineControl',
    'QAbstractSpinBox',
    'QComboBox',
    'QCompletionEngine',
    'QCompletionModel',
    'QExpandingLineEdit',
    'QFileDialogLineEdit',
    'QFileDialogListView',
    'QFileDialogTreeView',
    'QGraphicsAnchorPrivate',
    'QGraphicsSceneBspTreeIndexPrivate',
    'QGraphicsSceneIndex',
    'QGraphicsScenePrivate',
    'QIconModeViewBase',
    'QInputDialog',
    'QLineEditPrivate',
    'QListModeViewBase',
    'QListModel',
    'QListModelGreaterThan',
    'QListModelLessThan',
    'QListWidgetItemPrivate',
    'QTableView',
    'QTableWidgetPrivate',
    'QTreeWidget',
    'QTreeWidgetItem',
    'QComboBoxDelegate',
    'QComboBoxListView',
    'QComboBoxPrivateContainer',
    'QComboMenuDelegate',
    'QDateTimeEdit',
    'QDoubleSpinBox',
    'QFileDialogComboBox',
    'QFontComboBox',
    'QGraphicsSceneBspTreeIndex',
    'QGraphicsSceneLinearIndex',
    'QSortedModelEngine',
    'QSpinBox',
    'QSpinBoxValidator',
    'QTableWidget',
    'QTreeModel',
    'QTreeWidgetItemIterator',
    'QTreeWidgetItemPrivate',
    'QTreeWidgetPrivate',
    'QUnsortedModelEngine',
    'QDateEdit',
    'QDateTimeEditPrivate',
    'QItemEditorDateTimeEdit',
    'QTableModel',
    'QTimeEdit',
    'QTreeWidgetItemIteratorPrivate',
    'QItemViewPaintPairs',
    'QWidgetList',
    'QDrawBorderPixmap',
    'QMdi',
    'QStyleHelper',
    'QTest',
    'QtGraphicsAnchorLayout',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_effects import QEffects
  from ._q_graphics_item_cache import QGraphicsItemCache
  from ._q_index_mapper import QIndexMapper
  from ._q_item_view_paint_pair import QItemViewPaintPair
  from ._q_layout_struct import QLayoutStruct
  from ._q_list_view_layout_info import QListViewLayoutInfo
  from ._q_pixmap_style_descriptor import QPixmapStyleDescriptor
  from ._q_pixmap_style_pixmap import QPixmapStylePixmap
  from ._q_scroller_properties_private import QScrollerPropertiesPrivate
  from ._q_simplex_constraint import QSimplexConstraint
  from ._q_simplex_variable import QSimplexVariable
  from ._q_span_collection import QSpanCollection
  from ._q_style_hint_return import QStyleHintReturn
  from ._q_t_l_w_extra import QTLWExtra
  from ._q_table_widget_selection_range import QTableWidgetSelectionRange
  from ._q_tile_rules import QTileRules
  from ._q_tool_bar_area_layout_line import QToolBarAreaLayoutLine
  from ._q_tree_view_item import QTreeViewItem
  from ._q_w_extra import QWExtra
  from ._q_widget_data import QWidgetData
  from ._q_concrete_simplex_variable import QConcreteSimplexVariable
  from ._q_match_data import QMatchData
  from ._q_simplex import QSimplex
  from ._q_style_hint_return_mask import QStyleHintReturnMask
  from ._q_style_hint_return_variant import QStyleHintReturnVariant
  from ._q_splitter_layout_struct import QSplitterLayoutStruct
  from ._q_bsp_tree import QBspTree
  from ._q_layout_item import QLayoutItem
  from ._q_list_view_item import QListViewItem
  from ._q_style_factory import QStyleFactory
  from ._q_colormap import QColormap
  from ._q_file_dialog_args import QFileDialogArgs
  from ._q_tool_bar_area_layout_item import QToolBarAreaLayoutItem
  from ._q_button_group_private import QButtonGroupPrivate
  from ._q_gesture_private import QGesturePrivate
  from ._q_scroller_properties import QScrollerProperties
  from ._q_size_policy import QSizePolicy
  from ._q_style_plugin import QStylePlugin
  from ._q_style_sheet_style_caches import QStyleSheetStyleCaches
  from ._q_table_widget_mime_data import QTableWidgetMimeData
  from ._q_tree_model_private import QTreeModelPrivate
  from ._q_widget_item_data import QWidgetItemData
  from ._q_completion_model_private import QCompletionModelPrivate
  from ._q_flick_gesture_private import QFlickGesturePrivate
  from ._q_gesture import QGesture
  from ._q_pan_gesture_private import QPanGesturePrivate
  from ._q_pinch_gesture_private import QPinchGesturePrivate
  from ._q_scroller import QScroller
  from ._q_spacer_item import QSpacerItem
  from ._q_style_animation import QStyleAnimation
  from ._q_swipe_gesture_private import QSwipeGesturePrivate
  from ._q_tap_and_hold_gesture_private import QTapAndHoldGesturePrivate
  from ._q_tap_gesture_private import QTapGesturePrivate
  from ._q_blend_style_animation import QBlendStyleAnimation
  from ._q_flick_gesture import QFlickGesture
  from ._q_gesture_recognizer import QGestureRecognizer
  from ._q_graphics_effect import QGraphicsEffect
  from ._q_graphics_effect_source_private import QGraphicsEffectSourcePrivate
  from ._q_graphics_effect_source import QGraphicsEffectSource
  from ._q_graphics_effect_private import QGraphicsEffectPrivate
  from ._q_number_style_animation import QNumberStyleAnimation
  from ._q_pan_gesture import QPanGesture
  from ._q_pinch_gesture import QPinchGesture
  from ._q_pixmap_filter import QPixmapFilter
  from ._q_progress_style_animation import QProgressStyleAnimation
  from ._q_swipe_gesture import QSwipeGesture
  from ._q_tap_and_hold_gesture import QTapAndHoldGesture
  from ._q_tap_gesture import QTapGesture
  from ._q_update_later_event import QUpdateLaterEvent
  from ._q_flick_gesture_recognizer import QFlickGestureRecognizer
  from ._q_graphics_blur_effect import QGraphicsBlurEffect
  from ._q_graphics_blur_effect_private import QGraphicsBlurEffectPrivate
  from ._q_graphics_colorize_effect import QGraphicsColorizeEffect
  from ._q_graphics_colorize_effect_private import QGraphicsColorizeEffectPrivate
  from ._q_graphics_drop_shadow_effect import QGraphicsDropShadowEffect
  from ._q_graphics_drop_shadow_effect_private import QGraphicsDropShadowEffectPrivate
  from ._q_graphics_opacity_effect import QGraphicsOpacityEffect
  from ._q_graphics_opacity_effect_private import QGraphicsOpacityEffectPrivate
  from ._q_mac_pan_gesture_recognizer import QMacPanGestureRecognizer
  from ._q_mac_pinch_gesture_recognizer import QMacPinchGestureRecognizer
  from ._q_mac_swipe_gesture_recognizer import QMacSwipeGestureRecognizer
  from ._q_pan_gesture_recognizer import QPanGestureRecognizer
  from ._q_pinch_gesture_recognizer import QPinchGestureRecognizer
  from ._q_pixmap_colorize_filter import QPixmapColorizeFilter
  from ._q_pixmap_convolution_filter import QPixmapConvolutionFilter
  from ._q_pixmap_drop_shadow_filter import QPixmapDropShadowFilter
  from ._q_scrollbar_style_animation import QScrollbarStyleAnimation
  from ._q_swipe_gesture_recognizer import QSwipeGestureRecognizer
  from ._q_tap_and_hold_gesture_recognizer import QTapAndHoldGestureRecognizer
  from ._q_tap_gesture_recognizer import QTapGestureRecognizer
  from ._q_pixmap_blur_filter import QPixmapBlurFilter
  from ._q_file_icon_provider import QFileIconProvider
  from ._q_plain_text_document_layout import QPlainTextDocumentLayout
  from ._q_text_edit_mime_data import QTextEditMimeData
  from ._q_table_widget_item import QTableWidgetItem
  from ._q_table_model_greater_than import QTableModelGreaterThan
  from ._q_table_model_less_than import QTableModelLessThan
  from ._q_table_widget_item_private import QTableWidgetItemPrivate
  from ._q_url_model import QUrlModel
  from ._qt_widgets_action_private import QtWidgetsActionPrivate
  from ._q_widget_action_private import QWidgetActionPrivate
  from ._q_widget import QWidget
  from ._q_style_option import QStyleOption
  from ._q_style import QStyle
  from ._q_widget_repaint_manager import QWidgetRepaintManager
  from ._q_application import QApplication
  from ._q_layout import QLayout
  from ._q_layout_private import QLayoutPrivate
  from ._q_style_option_complex import QStyleOptionComplex
  from ._q_style_private import QStylePrivate
  from ._q_widget_private import QWidgetPrivate
  from ._q_abstract_button_private import QAbstractButtonPrivate
  from ._q_abstract_item_delegate_private import QAbstractItemDelegatePrivate
  from ._q_abstract_scroll_area_scroll_bar_container import QAbstractScrollAreaScrollBarContainer
  from ._q_abstract_slider_private import QAbstractSliderPrivate
  from ._q_abstract_spin_box_private import QAbstractSpinBoxPrivate
  from ._q_accessible_menu_item import QAccessibleMenuItem
  from ._q_accessible_widget import QAccessibleWidget
  from ._q_application_private import QApplicationPrivate
  from ._q_box_layout import QBoxLayout
  from ._q_cached_painter import QCachedPainter
  from ._q_calendar_widget import QCalendarWidget
  from ._q_column_view_grip_private import QColumnViewGripPrivate
  from ._q_dock_widget_layout import QDockWidgetLayout
  from ._q_dock_widget_private import QDockWidgetPrivate
  from ._q_editor_info import QEditorInfo
  from ._q_file_icon_provider_private import QFileIconProviderPrivate
  from ._q_focus_frame import QFocusFrame
  from ._q_form_layout import QFormLayout
  from ._q_frame_private import QFramePrivate
  from ._q_gesture_event import QGestureEvent
  from ._q_graphics_scene_event import QGraphicsSceneEvent
  from ._q_grid_layout import QGridLayout
  from ._q_item_editor_creator_base import QItemEditorCreatorBase
  from ._q_key_sequence_edit_private import QKeySequenceEditPrivate
  from ._q_layout_style_info import QLayoutStyleInfo
  from ._q_menu_bar_private import QMenuBarPrivate
  from ._q_movable_tab_widget import QMovableTabWidget
  from ._q_place_holder_item import QPlaceHolderItem
  from ._q_rhi_widget_private import QRhiWidgetPrivate
  from ._q_scroller_private import QScrollerPrivate
  from ._q_size_grip import QSizeGrip
  from ._q_splash_screen import QSplashScreen
  from ._q_splitter_handle_private import QSplitterHandlePrivate
  from ._q_stacked_layout import QStackedLayout
  from ._q_status_bar import QStatusBar
  from ._q_style_option_button import QStyleOptionButton
  from ._q_style_option_combo_box import QStyleOptionComboBox
  from ._q_style_option_dock_widget import QStyleOptionDockWidget
  from ._q_style_option_focus_rect import QStyleOptionFocusRect
  from ._q_style_option_frame import QStyleOptionFrame
  from ._q_style_option_graphics_item import QStyleOptionGraphicsItem
  from ._q_style_option_group_box import QStyleOptionGroupBox
  from ._q_style_option_header import QStyleOptionHeader
  from ._q_style_option_menu_item import QStyleOptionMenuItem
  from ._q_style_option_progress_bar import QStyleOptionProgressBar
  from ._q_style_option_rubber_band import QStyleOptionRubberBand
  from ._q_style_option_size_grip import QStyleOptionSizeGrip
  from ._q_style_option_slider import QStyleOptionSlider
  from ._q_style_option_spin_box import QStyleOptionSpinBox
  from ._q_style_option_tab import QStyleOptionTab
  from ._q_style_option_tab_bar_base import QStyleOptionTabBarBase
  from ._q_style_option_tab_widget_frame import QStyleOptionTabWidgetFrame
  from ._q_style_option_title_bar import QStyleOptionTitleBar
  from ._q_style_option_tool_bar import QStyleOptionToolBar
  from ._q_style_option_tool_box import QStyleOptionToolBox
  from ._q_style_option_tool_button import QStyleOptionToolButton
  from ._q_style_option_view_item import QStyleOptionViewItem
  from ._q_style_painter import QStylePainter
  from ._q_tool_bar_layout import QToolBarLayout
  from ._q_tool_bar_private import QToolBarPrivate
  from ._q_tool_tip import QToolTip
  from ._q_well_array import QWellArray
  from ._q_whats_this import QWhatsThis
  from ._q_widget_action import QWidgetAction
  from ._q_widget_effect_source_private import QWidgetEffectSourcePrivate
  from ._q_widget_item import QWidgetItem
  from ._q_widget_paint_context import QWidgetPaintContext
  from ._q_widget_resize_handler import QWidgetResizeHandler
  from ._q_widget_text_control import QWidgetTextControl
  from ._q_widget_text_control_private import QWidgetTextControlPrivate
  from ._q_widget_window import QWidgetWindow
  from ._q_window_container import QWindowContainer
  from ._q_abstract_button import QAbstractButton
  from ._q_abstract_slider import QAbstractSlider
  from ._q_accessible_widget_v2 import QAccessibleWidgetV2
  from ._q_calendar_popup import QCalendarPopup
  from ._q_color_well import QColorWell
  from ._q_column_view_grip import QColumnViewGrip
  from ._q_combo_box_private import QComboBoxPrivate
  from ._q_common_style import QCommonStyle
  from ._q_common_style_private import QCommonStylePrivate
  from ._q_dock_widget import QDockWidget
  from ._q_frame import QFrame
  from ._q_graphics_item_paint_info import QGraphicsItemPaintInfo
  from ._q_graphics_scene_context_menu_event import QGraphicsSceneContextMenuEvent
  from ._q_graphics_scene_drag_drop_event import QGraphicsSceneDragDropEvent
  from ._q_graphics_scene_help_event import QGraphicsSceneHelpEvent
  from ._q_graphics_scene_hover_event import QGraphicsSceneHoverEvent
  from ._q_graphics_scene_mouse_event import QGraphicsSceneMouseEvent
  from ._q_graphics_scene_move_event import QGraphicsSceneMoveEvent
  from ._q_graphics_scene_resize_event import QGraphicsSceneResizeEvent
  from ._q_graphics_scene_wheel_event import QGraphicsSceneWheelEvent
  from ._q_group_box import QGroupBox
  from ._q_h_box_layout import QHBoxLayout
  from ._q_item_editor_factory import QItemEditorFactory
  from ._q_key_sequence_edit import QKeySequenceEdit
  from ._q_label_private import QLabelPrivate
  from ._q_menu import QMenu
  from ._q_menu_private import QMenuPrivate
  from ._q_progress_bar import QProgressBar
  from ._q_rhi_widget import QRhiWidget
  from ._q_rubber_band import QRubberBand
  from ._q_scroll_bar_private import QScrollBarPrivate
  from ._q_splitter_private import QSplitterPrivate
  from ._q_style_option_header_v2 import QStyleOptionHeaderV2
  from ._q_style_option_menu_item_v2 import QStyleOptionMenuItemV2
  from ._q_tab_bar import QTabBar
  from ._q_tool_bar import QToolBar
  from ._q_tool_bar_item import QToolBarItem
  from ._q_v_box_layout import QVBoxLayout
  from ._q_widget_item_v2 import QWidgetItemV2
  from ._q_accessible_abstract_scroll_area import QAccessibleAbstractScrollArea
  from ._q_accessible_abstract_slider import QAccessibleAbstractSlider
  from ._q_accessible_abstract_spin_box import QAccessibleAbstractSpinBox
  from ._q_accessible_button import QAccessibleButton
  from ._q_accessible_calendar_widget import QAccessibleCalendarWidget
  from ._q_accessible_color_well import QAccessibleColorWell
  from ._q_accessible_combo_box import QAccessibleComboBox
  from ._q_accessible_dialog_button_box import QAccessibleDialogButtonBox
  from ._q_accessible_display import QAccessibleDisplay
  from ._q_accessible_dock_widget import QAccessibleDockWidget
  from ._q_accessible_group_box import QAccessibleGroupBox
  from ._q_accessible_line_edit import QAccessibleLineEdit
  from ._q_accessible_main_window import QAccessibleMainWindow
  from ._q_accessible_mdi_area import QAccessibleMdiArea
  from ._q_accessible_mdi_sub_window import QAccessibleMdiSubWindow
  from ._q_accessible_menu import QAccessibleMenu
  from ._q_accessible_menu_bar import QAccessibleMenuBar
  from ._q_accessible_message_box import QAccessibleMessageBox
  from ._q_accessible_stacked_widget import QAccessibleStackedWidget
  from ._q_accessible_tab_bar import QAccessibleTabBar
  from ._q_accessible_table import QAccessibleTable
  from ._q_accessible_text_widget import QAccessibleTextWidget
  from ._q_accessible_tool_box import QAccessibleToolBox
  from ._q_accessible_window_container import QAccessibleWindowContainer
  from ._q_button_group import QButtonGroup
  from ._q_check_box import QCheckBox
  from ._q_combo_box_private_scroller import QComboBoxPrivateScroller
  from ._q_dial import QDial
  from ._q_dialog_button_box import QDialogButtonBox
  from ._q_dock_widget_group_window import QDockWidgetGroupWindow
  from ._q_dock_widget_item import QDockWidgetItem
  from ._q_fusion_style_private import QFusionStylePrivate
  from ._q_graphics_transform import QGraphicsTransform
  from ._q_graphics_item import QGraphicsItem
  from ._q_graphics_item_group import QGraphicsItemGroup
  from ._q_graphics_item_private import QGraphicsItemPrivate
  from ._q_graphics_transform_private import QGraphicsTransformPrivate
  from ._q_l_c_d_number import QLCDNumber
  from ._q_label import QLabel
  from ._q_mdi_sub_window import QMdiSubWindow
  from ._q_menu_bar import QMenuBar
  from ._q_menu_sloppy_state import QMenuSloppyState
  from ._q_pixmap_style import QPixmapStyle
  from ._q_pixmap_style_private import QPixmapStylePrivate
  from ._q_proxy_style import QProxyStyle
  from ._q_proxy_style_private import QProxyStylePrivate
  from ._q_push_button import QPushButton
  from ._q_push_button_private import QPushButtonPrivate
  from ._q_radio_button import QRadioButton
  from ._q_scroll_bar import QScrollBar
  from ._q_slider import QSlider
  from ._q_splitter import QSplitter
  from ._q_stacked_widget import QStackedWidget
  from ._q_system_tray_icon import QSystemTrayIcon
  from ._q_tab_bar_private import QTabBarPrivate
  from ._q_tab_widget import QTabWidget
  from ._q_tool_bar_area_layout_info import QToolBarAreaLayoutInfo
  from ._q_tool_bar_separator import QToolBarSeparator
  from ._q_tool_box import QToolBox
  from ._q_tool_button import QToolButton
  from ._q_unicode_control_character_menu import QUnicodeControlCharacterMenu
  from ._q_windows_style_private import QWindowsStylePrivate
  from ._q_abstract_graphics_shape_item import QAbstractGraphicsShapeItem
  from ._q_abstract_scroll_area_private import QAbstractScrollAreaPrivate
  from ._q_accessible_dial import QAccessibleDial
  from ._q_accessible_double_spin_box import QAccessibleDoubleSpinBox
  from ._q_accessible_list import QAccessibleList
  from ._q_accessible_plain_text_edit import QAccessiblePlainTextEdit
  from ._q_accessible_progress_bar import QAccessibleProgressBar
  from ._q_accessible_scroll_area import QAccessibleScrollArea
  from ._q_accessible_scroll_bar import QAccessibleScrollBar
  from ._q_accessible_slider import QAccessibleSlider
  from ._q_accessible_spin_box import QAccessibleSpinBox
  from ._q_accessible_text_edit import QAccessibleTextEdit
  from ._q_accessible_tool_button import QAccessibleToolButton
  from ._q_accessible_tree import QAccessibleTree
  from ._q_balloon_tip import QBalloonTip
  from ._q_command_link_button import QCommandLinkButton
  from ._q_dialog import QDialog
  from ._q_dialog_private import QDialogPrivate
  from ._q_dialog_button_box_private import QDialogButtonBoxPrivate
  from ._q_dock_widget_group_window_item import QDockWidgetGroupWindowItem
  from ._q_fusion_style import QFusionStyle
  from ._q_graphics_item_animation import QGraphicsItemAnimation
  from ._q_graphics_item_effect_source_private import QGraphicsItemEffectSourcePrivate
  from ._q_graphics_layout_item import QGraphicsLayoutItem
  from ._q_graphics_layout_item_private import QGraphicsLayoutItemPrivate
  from ._q_graphics_line_item import QGraphicsLineItem
  from ._q_graphics_object import QGraphicsObject
  from ._q_graphics_pixmap_item import QGraphicsPixmapItem
  from ._q_graphics_rotation import QGraphicsRotation
  from ._q_graphics_scale import QGraphicsScale
  from ._q_graphics_scene_bsp_tree import QGraphicsSceneBspTree
  from ._q_line_edit_icon_button import QLineEditIconButton
  from ._q_main_window import QMainWindow
  from ._q_mdi_sub_window_private import QMdiSubWindowPrivate
  from ._q_splitter_handle import QSplitterHandle
  from ._q_system_tray_icon_private import QSystemTrayIconPrivate
  from ._q_tip_label import QTipLabel
  from ._q_tool_bar_extension import QToolBarExtension
  from ._q_windows_style import QWindowsStyle
  from ._q_abstract_scroll_area import QAbstractScrollArea
  from ._q_abstract_scroll_area_filter import QAbstractScrollAreaFilter
  from ._q_accessible_text_browser import QAccessibleTextBrowser
  from ._q_color_dialog import QColorDialog
  from ._q_error_message import QErrorMessage
  from ._q_font_dialog import QFontDialog
  from ._q_gesture_manager import QGestureManager
  from ._q_graphics_ellipse_item import QGraphicsEllipseItem
  from ._q_graphics_grid_layout_engine import QGraphicsGridLayoutEngine
  from ._q_graphics_grid_layout_engine_item import QGraphicsGridLayoutEngineItem
  from ._q_graphics_layout_private import QGraphicsLayoutPrivate
  from ._q_graphics_path_item import QGraphicsPathItem
  from ._q_graphics_polygon_item import QGraphicsPolygonItem
  from ._q_graphics_rect_item import QGraphicsRectItem
  from ._q_graphics_simple_text_item import QGraphicsSimpleTextItem
  from ._q_graphics_text_item import QGraphicsTextItem
  from ._q_main_window_layout import QMainWindowLayout
  from ._q_widget_animator import QWidgetAnimator
  from ._q_main_window_layout_state import QMainWindowLayoutState
  from ._q_message_box import QMessageBox
  from ._q_plain_text_edit_private import QPlainTextEditPrivate
  from ._q_progress_dialog import QProgressDialog
  from ._q_scroll_area_private import QScrollAreaPrivate
  from ._q_style_sheet_style import QStyleSheetStyle
  from ._q_text_edit_private import QTextEditPrivate
  from ._q_wizard import QWizard
  from ._q_wizard_page import QWizardPage
  from ._q_abstract_item_delegate import QAbstractItemDelegate
  from ._q_abstract_item_view import QAbstractItemView
  from ._q_abstract_item_view_private import QAbstractItemViewPrivate
  from ._q_dock_area_layout import QDockAreaLayout
  from ._q_dock_area_layout_info import QDockAreaLayoutInfo
  from ._q_font_dialog_private import QFontDialogPrivate
  from ._q_graphics_layout import QGraphicsLayout
  from ._q_graphics_layout_style_info import QGraphicsLayoutStyleInfo
  from ._q_mdi_area import QMdiArea
  from ._q_plain_text_edit import QPlainTextEdit
  from ._q_scroll_area import QScrollArea
  from ._q_text_edit import QTextEdit
  from ._q_tool_bar_area_layout import QToolBarAreaLayout
  from ._q_accessible_table_cell import QAccessibleTableCell
  from ._q_accessible_table_corner_button import QAccessibleTableCornerButton
  from ._q_accessible_table_header_cell import QAccessibleTableHeaderCell
  from ._q_column_view_preview_column import QColumnViewPreviewColumn
  from ._q_column_view_private import QColumnViewPrivate
  from ._q_completer import QCompleter
  from ._q_data_widget_mapper import QDataWidgetMapper
  from ._q_dock_area_layout_item import QDockAreaLayoutItem
  from ._q_file_dialog import QFileDialog
  from ._q_graphics_anchor_layout import QGraphicsAnchorLayout
  from ._q_graphics_grid_layout import QGraphicsGridLayout
  from ._q_graphics_linear_layout import QGraphicsLinearLayout
  from ._q_graphics_widget import QGraphicsWidget
  from ._q_graphics_scene import QGraphicsScene
  from ._q_graphics_widget_private import QGraphicsWidgetPrivate
  from ._q_header_view import QHeaderView
  from ._q_header_view_private import QHeaderViewPrivate
  from ._q_item_delegate import QItemDelegate
  from ._q_list_view import QListView
  from ._q_list_view_private import QListViewPrivate
  from ._q_mdi_area_private import QMdiAreaPrivate
  from ._q_plain_text_edit_control import QPlainTextEditControl
  from ._q_styled_item_delegate import QStyledItemDelegate
  from ._q_text_browser import QTextBrowser
  from ._q_tree_view_private import QTreeViewPrivate
  from ._q_column_view import QColumnView
  from ._q_column_view_delegate import QColumnViewDelegate
  from ._q_common_list_view_base import QCommonListViewBase
  from ._q_completer_item_delegate import QCompleterItemDelegate
  from ._q_completer_private import QCompleterPrivate
  from ._q_f_s_completer import QFSCompleter
  from ._q_file_dialog_private import QFileDialogPrivate
  from ._q_graphics_anchor import QGraphicsAnchor
  from ._q_graphics_anchor_layout_private import QGraphicsAnchorLayoutPrivate
  from ._q_graphics_proxy_widget import QGraphicsProxyWidget
  from ._q_graphics_proxy_widget_private import QGraphicsProxyWidgetPrivate
  from ._q_graphics_scene_index_private import QGraphicsSceneIndexPrivate
  from ._q_graphics_view import QGraphicsView
  from ._q_graphics_view_private import QGraphicsViewPrivate
  from ._q_line_edit import QLineEdit
  from ._q_list_widget import QListWidget
  from ._q_list_widget_item import QListWidgetItem
  from ._q_list_widget_private import QListWidgetPrivate
  from ._q_side_bar_delegate import QSideBarDelegate
  from ._q_sidebar import QSidebar
  from ._q_table_view_private import QTableViewPrivate
  from ._q_tree_view import QTreeView
  from ._q_undo_view import QUndoView
  from ._q_widget_line_control import QWidgetLineControl
  from ._q_abstract_spin_box import QAbstractSpinBox
  from ._q_combo_box import QComboBox
  from ._q_completion_engine import QCompletionEngine
  from ._q_completion_model import QCompletionModel
  from ._q_expanding_line_edit import QExpandingLineEdit
  from ._q_file_dialog_line_edit import QFileDialogLineEdit
  from ._q_file_dialog_list_view import QFileDialogListView
  from ._q_file_dialog_tree_view import QFileDialogTreeView
  from ._q_graphics_anchor_private import QGraphicsAnchorPrivate
  from ._q_graphics_scene_bsp_tree_index_private import QGraphicsSceneBspTreeIndexPrivate
  from ._q_graphics_scene_index import QGraphicsSceneIndex
  from ._q_graphics_scene_private import QGraphicsScenePrivate
  from ._q_icon_mode_view_base import QIconModeViewBase
  from ._q_input_dialog import QInputDialog
  from ._q_line_edit_private import QLineEditPrivate
  from ._q_list_mode_view_base import QListModeViewBase
  from ._q_list_model import QListModel
  from ._q_list_model_greater_than import QListModelGreaterThan
  from ._q_list_model_less_than import QListModelLessThan
  from ._q_list_widget_item_private import QListWidgetItemPrivate
  from ._q_table_view import QTableView
  from ._q_table_widget_private import QTableWidgetPrivate
  from ._q_tree_widget import QTreeWidget
  from ._q_tree_widget_item import QTreeWidgetItem
  from ._q_combo_box_delegate import QComboBoxDelegate
  from ._q_combo_box_list_view import QComboBoxListView
  from ._q_combo_box_private_container import QComboBoxPrivateContainer
  from ._q_combo_menu_delegate import QComboMenuDelegate
  from ._q_date_time_edit import QDateTimeEdit
  from ._q_double_spin_box import QDoubleSpinBox
  from ._q_file_dialog_combo_box import QFileDialogComboBox
  from ._q_font_combo_box import QFontComboBox
  from ._q_graphics_scene_bsp_tree_index import QGraphicsSceneBspTreeIndex
  from ._q_graphics_scene_linear_index import QGraphicsSceneLinearIndex
  from ._q_sorted_model_engine import QSortedModelEngine
  from ._q_spin_box import QSpinBox
  from ._q_spin_box_validator import QSpinBoxValidator
  from ._q_table_widget import QTableWidget
  from ._q_tree_model import QTreeModel
  from ._q_tree_widget_item_iterator import QTreeWidgetItemIterator
  from ._q_tree_widget_item_private import QTreeWidgetItemPrivate
  from ._q_tree_widget_private import QTreeWidgetPrivate
  from ._q_unsorted_model_engine import QUnsortedModelEngine
  from ._q_date_edit import QDateEdit
  from ._q_date_time_edit_private import QDateTimeEditPrivate
  from ._q_item_editor_date_time_edit import QItemEditorDateTimeEdit
  from ._q_table_model import QTableModel
  from ._q_time_edit import QTimeEdit
  from ._q_tree_widget_item_iterator_private import QTreeWidgetItemIteratorPrivate
  from ._q_item_view_paint_pair import QItemViewPaintPairs
  from ._q_widget import QWidgetList
  from . import QDrawBorderPixmap
  from . import QMdi
  from . import QStyleHelper
  from . import QTest
  from . import QtGraphicsAnchorLayout
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QEffects': '_q_effects',
      'QGraphicsItemCache': '_q_graphics_item_cache',
      'QIndexMapper': '_q_index_mapper',
      'QItemViewPaintPair': '_q_item_view_paint_pair',
      'QLayoutStruct': '_q_layout_struct',
      'QListViewLayoutInfo': '_q_list_view_layout_info',
      'QPixmapStyleDescriptor': '_q_pixmap_style_descriptor',
      'QPixmapStylePixmap': '_q_pixmap_style_pixmap',
      'QScrollerPropertiesPrivate': '_q_scroller_properties_private',
      'QSimplexConstraint': '_q_simplex_constraint',
      'QSimplexVariable': '_q_simplex_variable',
      'QSpanCollection': '_q_span_collection',
      'QStyleHintReturn': '_q_style_hint_return',
      'QTLWExtra': '_q_t_l_w_extra',
      'QTableWidgetSelectionRange': '_q_table_widget_selection_range',
      'QTileRules': '_q_tile_rules',
      'QToolBarAreaLayoutLine': '_q_tool_bar_area_layout_line',
      'QTreeViewItem': '_q_tree_view_item',
      'QWExtra': '_q_w_extra',
      'QWidgetData': '_q_widget_data',
      'QConcreteSimplexVariable': '_q_concrete_simplex_variable',
      'QMatchData': '_q_match_data',
      'QSimplex': '_q_simplex',
      'QStyleHintReturnMask': '_q_style_hint_return_mask',
      'QStyleHintReturnVariant': '_q_style_hint_return_variant',
      'QSplitterLayoutStruct': '_q_splitter_layout_struct',
      'QBspTree': '_q_bsp_tree',
      'QLayoutItem': '_q_layout_item',
      'QListViewItem': '_q_list_view_item',
      'QStyleFactory': '_q_style_factory',
      'QColormap': '_q_colormap',
      'QFileDialogArgs': '_q_file_dialog_args',
      'QToolBarAreaLayoutItem': '_q_tool_bar_area_layout_item',
      'QButtonGroupPrivate': '_q_button_group_private',
      'QGesturePrivate': '_q_gesture_private',
      'QScrollerProperties': '_q_scroller_properties',
      'QSizePolicy': '_q_size_policy',
      'QStylePlugin': '_q_style_plugin',
      'QStyleSheetStyleCaches': '_q_style_sheet_style_caches',
      'QTableWidgetMimeData': '_q_table_widget_mime_data',
      'QTreeModelPrivate': '_q_tree_model_private',
      'QWidgetItemData': '_q_widget_item_data',
      'QCompletionModelPrivate': '_q_completion_model_private',
      'QFlickGesturePrivate': '_q_flick_gesture_private',
      'QGesture': '_q_gesture',
      'QPanGesturePrivate': '_q_pan_gesture_private',
      'QPinchGesturePrivate': '_q_pinch_gesture_private',
      'QScroller': '_q_scroller',
      'QSpacerItem': '_q_spacer_item',
      'QStyleAnimation': '_q_style_animation',
      'QSwipeGesturePrivate': '_q_swipe_gesture_private',
      'QTapAndHoldGesturePrivate': '_q_tap_and_hold_gesture_private',
      'QTapGesturePrivate': '_q_tap_gesture_private',
      'QBlendStyleAnimation': '_q_blend_style_animation',
      'QFlickGesture': '_q_flick_gesture',
      'QGestureRecognizer': '_q_gesture_recognizer',
      'QGraphicsEffect': '_q_graphics_effect',
      'QGraphicsEffectSourcePrivate': '_q_graphics_effect_source_private',
      'QGraphicsEffectSource': '_q_graphics_effect_source',
      'QGraphicsEffectPrivate': '_q_graphics_effect_private',
      'QNumberStyleAnimation': '_q_number_style_animation',
      'QPanGesture': '_q_pan_gesture',
      'QPinchGesture': '_q_pinch_gesture',
      'QPixmapFilter': '_q_pixmap_filter',
      'QProgressStyleAnimation': '_q_progress_style_animation',
      'QSwipeGesture': '_q_swipe_gesture',
      'QTapAndHoldGesture': '_q_tap_and_hold_gesture',
      'QTapGesture': '_q_tap_gesture',
      'QUpdateLaterEvent': '_q_update_later_event',
      'QFlickGestureRecognizer': '_q_flick_gesture_recognizer',
      'QGraphicsBlurEffect': '_q_graphics_blur_effect',
      'QGraphicsBlurEffectPrivate': '_q_graphics_blur_effect_private',
      'QGraphicsColorizeEffect': '_q_graphics_colorize_effect',
      'QGraphicsColorizeEffectPrivate': '_q_graphics_colorize_effect_private',
      'QGraphicsDropShadowEffect': '_q_graphics_drop_shadow_effect',
      'QGraphicsDropShadowEffectPrivate': '_q_graphics_drop_shadow_effect_private',
      'QGraphicsOpacityEffect': '_q_graphics_opacity_effect',
      'QGraphicsOpacityEffectPrivate': '_q_graphics_opacity_effect_private',
      'QMacPanGestureRecognizer': '_q_mac_pan_gesture_recognizer',
      'QMacPinchGestureRecognizer': '_q_mac_pinch_gesture_recognizer',
      'QMacSwipeGestureRecognizer': '_q_mac_swipe_gesture_recognizer',
      'QPanGestureRecognizer': '_q_pan_gesture_recognizer',
      'QPinchGestureRecognizer': '_q_pinch_gesture_recognizer',
      'QPixmapColorizeFilter': '_q_pixmap_colorize_filter',
      'QPixmapConvolutionFilter': '_q_pixmap_convolution_filter',
      'QPixmapDropShadowFilter': '_q_pixmap_drop_shadow_filter',
      'QScrollbarStyleAnimation': '_q_scrollbar_style_animation',
      'QSwipeGestureRecognizer': '_q_swipe_gesture_recognizer',
      'QTapAndHoldGestureRecognizer': '_q_tap_and_hold_gesture_recognizer',
      'QTapGestureRecognizer': '_q_tap_gesture_recognizer',
      'QPixmapBlurFilter': '_q_pixmap_blur_filter',
      'QFileIconProvider': '_q_file_icon_provider',
      'QPlainTextDocumentLayout': '_q_plain_text_document_layout',
      'QTextEditMimeData': '_q_text_edit_mime_data',
      'QTableWidgetItem': '_q_table_widget_item',
      'QTableModelGreaterThan': '_q_table_model_greater_than',
      'QTableModelLessThan': '_q_table_model_less_than',
      'QTableWidgetItemPrivate': '_q_table_widget_item_private',
      'QUrlModel': '_q_url_model',
      'QtWidgetsActionPrivate': '_qt_widgets_action_private',
      'QWidgetActionPrivate': '_q_widget_action_private',
      'QWidget': '_q_widget',
      'QStyleOption': '_q_style_option',
      'QStyle': '_q_style',
      'QWidgetRepaintManager': '_q_widget_repaint_manager',
      'QApplication': '_q_application',
      'QLayout': '_q_layout',
      'QLayoutPrivate': '_q_layout_private',
      'QStyleOptionComplex': '_q_style_option_complex',
      'QStylePrivate': '_q_style_private',
      'QWidgetPrivate': '_q_widget_private',
      'QAbstractButtonPrivate': '_q_abstract_button_private',
      'QAbstractItemDelegatePrivate': '_q_abstract_item_delegate_private',
      'QAbstractScrollAreaScrollBarContainer': '_q_abstract_scroll_area_scroll_bar_container',
      'QAbstractSliderPrivate': '_q_abstract_slider_private',
      'QAbstractSpinBoxPrivate': '_q_abstract_spin_box_private',
      'QAccessibleMenuItem': '_q_accessible_menu_item',
      'QAccessibleWidget': '_q_accessible_widget',
      'QApplicationPrivate': '_q_application_private',
      'QBoxLayout': '_q_box_layout',
      'QCachedPainter': '_q_cached_painter',
      'QCalendarWidget': '_q_calendar_widget',
      'QColumnViewGripPrivate': '_q_column_view_grip_private',
      'QDockWidgetLayout': '_q_dock_widget_layout',
      'QDockWidgetPrivate': '_q_dock_widget_private',
      'QEditorInfo': '_q_editor_info',
      'QFileIconProviderPrivate': '_q_file_icon_provider_private',
      'QFocusFrame': '_q_focus_frame',
      'QFormLayout': '_q_form_layout',
      'QFramePrivate': '_q_frame_private',
      'QGestureEvent': '_q_gesture_event',
      'QGraphicsSceneEvent': '_q_graphics_scene_event',
      'QGridLayout': '_q_grid_layout',
      'QItemEditorCreatorBase': '_q_item_editor_creator_base',
      'QKeySequenceEditPrivate': '_q_key_sequence_edit_private',
      'QLayoutStyleInfo': '_q_layout_style_info',
      'QMenuBarPrivate': '_q_menu_bar_private',
      'QMovableTabWidget': '_q_movable_tab_widget',
      'QPlaceHolderItem': '_q_place_holder_item',
      'QRhiWidgetPrivate': '_q_rhi_widget_private',
      'QScrollerPrivate': '_q_scroller_private',
      'QSizeGrip': '_q_size_grip',
      'QSplashScreen': '_q_splash_screen',
      'QSplitterHandlePrivate': '_q_splitter_handle_private',
      'QStackedLayout': '_q_stacked_layout',
      'QStatusBar': '_q_status_bar',
      'QStyleOptionButton': '_q_style_option_button',
      'QStyleOptionComboBox': '_q_style_option_combo_box',
      'QStyleOptionDockWidget': '_q_style_option_dock_widget',
      'QStyleOptionFocusRect': '_q_style_option_focus_rect',
      'QStyleOptionFrame': '_q_style_option_frame',
      'QStyleOptionGraphicsItem': '_q_style_option_graphics_item',
      'QStyleOptionGroupBox': '_q_style_option_group_box',
      'QStyleOptionHeader': '_q_style_option_header',
      'QStyleOptionMenuItem': '_q_style_option_menu_item',
      'QStyleOptionProgressBar': '_q_style_option_progress_bar',
      'QStyleOptionRubberBand': '_q_style_option_rubber_band',
      'QStyleOptionSizeGrip': '_q_style_option_size_grip',
      'QStyleOptionSlider': '_q_style_option_slider',
      'QStyleOptionSpinBox': '_q_style_option_spin_box',
      'QStyleOptionTab': '_q_style_option_tab',
      'QStyleOptionTabBarBase': '_q_style_option_tab_bar_base',
      'QStyleOptionTabWidgetFrame': '_q_style_option_tab_widget_frame',
      'QStyleOptionTitleBar': '_q_style_option_title_bar',
      'QStyleOptionToolBar': '_q_style_option_tool_bar',
      'QStyleOptionToolBox': '_q_style_option_tool_box',
      'QStyleOptionToolButton': '_q_style_option_tool_button',
      'QStyleOptionViewItem': '_q_style_option_view_item',
      'QStylePainter': '_q_style_painter',
      'QToolBarLayout': '_q_tool_bar_layout',
      'QToolBarPrivate': '_q_tool_bar_private',
      'QToolTip': '_q_tool_tip',
      'QWellArray': '_q_well_array',
      'QWhatsThis': '_q_whats_this',
      'QWidgetAction': '_q_widget_action',
      'QWidgetEffectSourcePrivate': '_q_widget_effect_source_private',
      'QWidgetItem': '_q_widget_item',
      'QWidgetPaintContext': '_q_widget_paint_context',
      'QWidgetResizeHandler': '_q_widget_resize_handler',
      'QWidgetTextControl': '_q_widget_text_control',
      'QWidgetTextControlPrivate': '_q_widget_text_control_private',
      'QWidgetWindow': '_q_widget_window',
      'QWindowContainer': '_q_window_container',
      'QAbstractButton': '_q_abstract_button',
      'QAbstractSlider': '_q_abstract_slider',
      'QAccessibleWidgetV2': '_q_accessible_widget_v2',
      'QCalendarPopup': '_q_calendar_popup',
      'QColorWell': '_q_color_well',
      'QColumnViewGrip': '_q_column_view_grip',
      'QComboBoxPrivate': '_q_combo_box_private',
      'QCommonStyle': '_q_common_style',
      'QCommonStylePrivate': '_q_common_style_private',
      'QDockWidget': '_q_dock_widget',
      'QFrame': '_q_frame',
      'QGraphicsItemPaintInfo': '_q_graphics_item_paint_info',
      'QGraphicsSceneContextMenuEvent': '_q_graphics_scene_context_menu_event',
      'QGraphicsSceneDragDropEvent': '_q_graphics_scene_drag_drop_event',
      'QGraphicsSceneHelpEvent': '_q_graphics_scene_help_event',
      'QGraphicsSceneHoverEvent': '_q_graphics_scene_hover_event',
      'QGraphicsSceneMouseEvent': '_q_graphics_scene_mouse_event',
      'QGraphicsSceneMoveEvent': '_q_graphics_scene_move_event',
      'QGraphicsSceneResizeEvent': '_q_graphics_scene_resize_event',
      'QGraphicsSceneWheelEvent': '_q_graphics_scene_wheel_event',
      'QGroupBox': '_q_group_box',
      'QHBoxLayout': '_q_h_box_layout',
      'QItemEditorFactory': '_q_item_editor_factory',
      'QKeySequenceEdit': '_q_key_sequence_edit',
      'QLabelPrivate': '_q_label_private',
      'QMenu': '_q_menu',
      'QMenuPrivate': '_q_menu_private',
      'QProgressBar': '_q_progress_bar',
      'QRhiWidget': '_q_rhi_widget',
      'QRubberBand': '_q_rubber_band',
      'QScrollBarPrivate': '_q_scroll_bar_private',
      'QSplitterPrivate': '_q_splitter_private',
      'QStyleOptionHeaderV2': '_q_style_option_header_v2',
      'QStyleOptionMenuItemV2': '_q_style_option_menu_item_v2',
      'QTabBar': '_q_tab_bar',
      'QToolBar': '_q_tool_bar',
      'QToolBarItem': '_q_tool_bar_item',
      'QVBoxLayout': '_q_v_box_layout',
      'QWidgetItemV2': '_q_widget_item_v2',
      'QAccessibleAbstractScrollArea': '_q_accessible_abstract_scroll_area',
      'QAccessibleAbstractSlider': '_q_accessible_abstract_slider',
      'QAccessibleAbstractSpinBox': '_q_accessible_abstract_spin_box',
      'QAccessibleButton': '_q_accessible_button',
      'QAccessibleCalendarWidget': '_q_accessible_calendar_widget',
      'QAccessibleColorWell': '_q_accessible_color_well',
      'QAccessibleComboBox': '_q_accessible_combo_box',
      'QAccessibleDialogButtonBox': '_q_accessible_dialog_button_box',
      'QAccessibleDisplay': '_q_accessible_display',
      'QAccessibleDockWidget': '_q_accessible_dock_widget',
      'QAccessibleGroupBox': '_q_accessible_group_box',
      'QAccessibleLineEdit': '_q_accessible_line_edit',
      'QAccessibleMainWindow': '_q_accessible_main_window',
      'QAccessibleMdiArea': '_q_accessible_mdi_area',
      'QAccessibleMdiSubWindow': '_q_accessible_mdi_sub_window',
      'QAccessibleMenu': '_q_accessible_menu',
      'QAccessibleMenuBar': '_q_accessible_menu_bar',
      'QAccessibleMessageBox': '_q_accessible_message_box',
      'QAccessibleStackedWidget': '_q_accessible_stacked_widget',
      'QAccessibleTabBar': '_q_accessible_tab_bar',
      'QAccessibleTable': '_q_accessible_table',
      'QAccessibleTextWidget': '_q_accessible_text_widget',
      'QAccessibleToolBox': '_q_accessible_tool_box',
      'QAccessibleWindowContainer': '_q_accessible_window_container',
      'QButtonGroup': '_q_button_group',
      'QCheckBox': '_q_check_box',
      'QComboBoxPrivateScroller': '_q_combo_box_private_scroller',
      'QDial': '_q_dial',
      'QDialogButtonBox': '_q_dialog_button_box',
      'QDockWidgetGroupWindow': '_q_dock_widget_group_window',
      'QDockWidgetItem': '_q_dock_widget_item',
      'QFusionStylePrivate': '_q_fusion_style_private',
      'QGraphicsTransform': '_q_graphics_transform',
      'QGraphicsItem': '_q_graphics_item',
      'QGraphicsItemGroup': '_q_graphics_item_group',
      'QGraphicsItemPrivate': '_q_graphics_item_private',
      'QGraphicsTransformPrivate': '_q_graphics_transform_private',
      'QLCDNumber': '_q_l_c_d_number',
      'QLabel': '_q_label',
      'QMdiSubWindow': '_q_mdi_sub_window',
      'QMenuBar': '_q_menu_bar',
      'QMenuSloppyState': '_q_menu_sloppy_state',
      'QPixmapStyle': '_q_pixmap_style',
      'QPixmapStylePrivate': '_q_pixmap_style_private',
      'QProxyStyle': '_q_proxy_style',
      'QProxyStylePrivate': '_q_proxy_style_private',
      'QPushButton': '_q_push_button',
      'QPushButtonPrivate': '_q_push_button_private',
      'QRadioButton': '_q_radio_button',
      'QScrollBar': '_q_scroll_bar',
      'QSlider': '_q_slider',
      'QSplitter': '_q_splitter',
      'QStackedWidget': '_q_stacked_widget',
      'QSystemTrayIcon': '_q_system_tray_icon',
      'QTabBarPrivate': '_q_tab_bar_private',
      'QTabWidget': '_q_tab_widget',
      'QToolBarAreaLayoutInfo': '_q_tool_bar_area_layout_info',
      'QToolBarSeparator': '_q_tool_bar_separator',
      'QToolBox': '_q_tool_box',
      'QToolButton': '_q_tool_button',
      'QUnicodeControlCharacterMenu': '_q_unicode_control_character_menu',
      'QWindowsStylePrivate': '_q_windows_style_private',
      'QAbstractGraphicsShapeItem': '_q_abstract_graphics_shape_item',
      'QAbstractScrollAreaPrivate': '_q_abstract_scroll_area_private',
      'QAccessibleDial': '_q_accessible_dial',
      'QAccessibleDoubleSpinBox': '_q_accessible_double_spin_box',
      'QAccessibleList': '_q_accessible_list',
      'QAccessiblePlainTextEdit': '_q_accessible_plain_text_edit',
      'QAccessibleProgressBar': '_q_accessible_progress_bar',
      'QAccessibleScrollArea': '_q_accessible_scroll_area',
      'QAccessibleScrollBar': '_q_accessible_scroll_bar',
      'QAccessibleSlider': '_q_accessible_slider',
      'QAccessibleSpinBox': '_q_accessible_spin_box',
      'QAccessibleTextEdit': '_q_accessible_text_edit',
      'QAccessibleToolButton': '_q_accessible_tool_button',
      'QAccessibleTree': '_q_accessible_tree',
      'QBalloonTip': '_q_balloon_tip',
      'QCommandLinkButton': '_q_command_link_button',
      'QDialog': '_q_dialog',
      'QDialogPrivate': '_q_dialog_private',
      'QDialogButtonBoxPrivate': '_q_dialog_button_box_private',
      'QDockWidgetGroupWindowItem': '_q_dock_widget_group_window_item',
      'QFusionStyle': '_q_fusion_style',
      'QGraphicsItemAnimation': '_q_graphics_item_animation',
      'QGraphicsItemEffectSourcePrivate': '_q_graphics_item_effect_source_private',
      'QGraphicsLayoutItem': '_q_graphics_layout_item',
      'QGraphicsLayoutItemPrivate': '_q_graphics_layout_item_private',
      'QGraphicsLineItem': '_q_graphics_line_item',
      'QGraphicsObject': '_q_graphics_object',
      'QGraphicsPixmapItem': '_q_graphics_pixmap_item',
      'QGraphicsRotation': '_q_graphics_rotation',
      'QGraphicsScale': '_q_graphics_scale',
      'QGraphicsSceneBspTree': '_q_graphics_scene_bsp_tree',
      'QLineEditIconButton': '_q_line_edit_icon_button',
      'QMainWindow': '_q_main_window',
      'QMdiSubWindowPrivate': '_q_mdi_sub_window_private',
      'QSplitterHandle': '_q_splitter_handle',
      'QSystemTrayIconPrivate': '_q_system_tray_icon_private',
      'QTipLabel': '_q_tip_label',
      'QToolBarExtension': '_q_tool_bar_extension',
      'QWindowsStyle': '_q_windows_style',
      'QAbstractScrollArea': '_q_abstract_scroll_area',
      'QAbstractScrollAreaFilter': '_q_abstract_scroll_area_filter',
      'QAccessibleTextBrowser': '_q_accessible_text_browser',
      'QColorDialog': '_q_color_dialog',
      'QErrorMessage': '_q_error_message',
      'QFontDialog': '_q_font_dialog',
      'QGestureManager': '_q_gesture_manager',
      'QGraphicsEllipseItem': '_q_graphics_ellipse_item',
      'QGraphicsGridLayoutEngine': '_q_graphics_grid_layout_engine',
      'QGraphicsGridLayoutEngineItem': '_q_graphics_grid_layout_engine_item',
      'QGraphicsLayoutPrivate': '_q_graphics_layout_private',
      'QGraphicsPathItem': '_q_graphics_path_item',
      'QGraphicsPolygonItem': '_q_graphics_polygon_item',
      'QGraphicsRectItem': '_q_graphics_rect_item',
      'QGraphicsSimpleTextItem': '_q_graphics_simple_text_item',
      'QGraphicsTextItem': '_q_graphics_text_item',
      'QMainWindowLayout': '_q_main_window_layout',
      'QWidgetAnimator': '_q_widget_animator',
      'QMainWindowLayoutState': '_q_main_window_layout_state',
      'QMessageBox': '_q_message_box',
      'QPlainTextEditPrivate': '_q_plain_text_edit_private',
      'QProgressDialog': '_q_progress_dialog',
      'QScrollAreaPrivate': '_q_scroll_area_private',
      'QStyleSheetStyle': '_q_style_sheet_style',
      'QTextEditPrivate': '_q_text_edit_private',
      'QWizard': '_q_wizard',
      'QWizardPage': '_q_wizard_page',
      'QAbstractItemDelegate': '_q_abstract_item_delegate',
      'QAbstractItemView': '_q_abstract_item_view',
      'QAbstractItemViewPrivate': '_q_abstract_item_view_private',
      'QDockAreaLayout': '_q_dock_area_layout',
      'QDockAreaLayoutInfo': '_q_dock_area_layout_info',
      'QFontDialogPrivate': '_q_font_dialog_private',
      'QGraphicsLayout': '_q_graphics_layout',
      'QGraphicsLayoutStyleInfo': '_q_graphics_layout_style_info',
      'QMdiArea': '_q_mdi_area',
      'QPlainTextEdit': '_q_plain_text_edit',
      'QScrollArea': '_q_scroll_area',
      'QTextEdit': '_q_text_edit',
      'QToolBarAreaLayout': '_q_tool_bar_area_layout',
      'QAccessibleTableCell': '_q_accessible_table_cell',
      'QAccessibleTableCornerButton': '_q_accessible_table_corner_button',
      'QAccessibleTableHeaderCell': '_q_accessible_table_header_cell',
      'QColumnViewPreviewColumn': '_q_column_view_preview_column',
      'QColumnViewPrivate': '_q_column_view_private',
      'QCompleter': '_q_completer',
      'QDataWidgetMapper': '_q_data_widget_mapper',
      'QDockAreaLayoutItem': '_q_dock_area_layout_item',
      'QFileDialog': '_q_file_dialog',
      'QGraphicsAnchorLayout': '_q_graphics_anchor_layout',
      'QGraphicsGridLayout': '_q_graphics_grid_layout',
      'QGraphicsLinearLayout': '_q_graphics_linear_layout',
      'QGraphicsWidget': '_q_graphics_widget',
      'QGraphicsScene': '_q_graphics_scene',
      'QGraphicsWidgetPrivate': '_q_graphics_widget_private',
      'QHeaderView': '_q_header_view',
      'QHeaderViewPrivate': '_q_header_view_private',
      'QItemDelegate': '_q_item_delegate',
      'QListView': '_q_list_view',
      'QListViewPrivate': '_q_list_view_private',
      'QMdiAreaPrivate': '_q_mdi_area_private',
      'QPlainTextEditControl': '_q_plain_text_edit_control',
      'QStyledItemDelegate': '_q_styled_item_delegate',
      'QTextBrowser': '_q_text_browser',
      'QTreeViewPrivate': '_q_tree_view_private',
      'QColumnView': '_q_column_view',
      'QColumnViewDelegate': '_q_column_view_delegate',
      'QCommonListViewBase': '_q_common_list_view_base',
      'QCompleterItemDelegate': '_q_completer_item_delegate',
      'QCompleterPrivate': '_q_completer_private',
      'QFSCompleter': '_q_f_s_completer',
      'QFileDialogPrivate': '_q_file_dialog_private',
      'QGraphicsAnchor': '_q_graphics_anchor',
      'QGraphicsAnchorLayoutPrivate': '_q_graphics_anchor_layout_private',
      'QGraphicsProxyWidget': '_q_graphics_proxy_widget',
      'QGraphicsProxyWidgetPrivate': '_q_graphics_proxy_widget_private',
      'QGraphicsSceneIndexPrivate': '_q_graphics_scene_index_private',
      'QGraphicsView': '_q_graphics_view',
      'QGraphicsViewPrivate': '_q_graphics_view_private',
      'QLineEdit': '_q_line_edit',
      'QListWidget': '_q_list_widget',
      'QListWidgetItem': '_q_list_widget_item',
      'QListWidgetPrivate': '_q_list_widget_private',
      'QSideBarDelegate': '_q_side_bar_delegate',
      'QSidebar': '_q_sidebar',
      'QTableViewPrivate': '_q_table_view_private',
      'QTreeView': '_q_tree_view',
      'QUndoView': '_q_undo_view',
      'QWidgetLineControl': '_q_widget_line_control',
      'QAbstractSpinBox': '_q_abstract_spin_box',
      'QComboBox': '_q_combo_box',
      'QCompletionEngine': '_q_completion_engine',
      'QCompletionModel': '_q_completion_model',
      'QExpandingLineEdit': '_q_expanding_line_edit',
      'QFileDialogLineEdit': '_q_file_dialog_line_edit',
      'QFileDialogListView': '_q_file_dialog_list_view',
      'QFileDialogTreeView': '_q_file_dialog_tree_view',
      'QGraphicsAnchorPrivate': '_q_graphics_anchor_private',
      'QGraphicsSceneBspTreeIndexPrivate': '_q_graphics_scene_bsp_tree_index_private',
      'QGraphicsSceneIndex': '_q_graphics_scene_index',
      'QGraphicsScenePrivate': '_q_graphics_scene_private',
      'QIconModeViewBase': '_q_icon_mode_view_base',
      'QInputDialog': '_q_input_dialog',
      'QLineEditPrivate': '_q_line_edit_private',
      'QListModeViewBase': '_q_list_mode_view_base',
      'QListModel': '_q_list_model',
      'QListModelGreaterThan': '_q_list_model_greater_than',
      'QListModelLessThan': '_q_list_model_less_than',
      'QListWidgetItemPrivate': '_q_list_widget_item_private',
      'QTableView': '_q_table_view',
      'QTableWidgetPrivate': '_q_table_widget_private',
      'QTreeWidget': '_q_tree_widget',
      'QTreeWidgetItem': '_q_tree_widget_item',
      'QComboBoxDelegate': '_q_combo_box_delegate',
      'QComboBoxListView': '_q_combo_box_list_view',
      'QComboBoxPrivateContainer': '_q_combo_box_private_container',
      'QComboMenuDelegate': '_q_combo_menu_delegate',
      'QDateTimeEdit': '_q_date_time_edit',
      'QDoubleSpinBox': '_q_double_spin_box',
      'QFileDialogComboBox': '_q_file_dialog_combo_box',
      'QFontComboBox': '_q_font_combo_box',
      'QGraphicsSceneBspTreeIndex': '_q_graphics_scene_bsp_tree_index',
      'QGraphicsSceneLinearIndex': '_q_graphics_scene_linear_index',
      'QSortedModelEngine': '_q_sorted_model_engine',
      'QSpinBox': '_q_spin_box',
      'QSpinBoxValidator': '_q_spin_box_validator',
      'QTableWidget': '_q_table_widget',
      'QTreeModel': '_q_tree_model',
      'QTreeWidgetItemIterator': '_q_tree_widget_item_iterator',
      'QTreeWidgetItemPrivate': '_q_tree_widget_item_private',
      'QTreeWidgetPrivate': '_q_tree_widget_private',
      'QUnsortedModelEngine': '_q_unsorted_model_engine',
      'QDateEdit': '_q_date_edit',
      'QDateTimeEditPrivate': '_q_date_time_edit_private',
      'QItemEditorDateTimeEdit': '_q_item_editor_date_time_edit',
      'QTableModel': '_q_table_model',
      'QTimeEdit': '_q_time_edit',
      'QTreeWidgetItemIteratorPrivate': '_q_tree_widget_item_iterator_private',
      'QItemViewPaintPairs': '_q_item_view_paint_pair',
      'QWidgetList': '_q_widget',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QDrawBorderPixmap', 'QMdi', 'QStyleHelper', 'QTest', 'QtGraphicsAnchorLayout',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWidgets import QWidgetList'. Python calls
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
