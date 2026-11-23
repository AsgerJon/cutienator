"""
QStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QIcon, QPalette
from . import QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QFontMetrics, QPainter, QPixmap
  from . import QApplication, QStyleHintReturn, QStyleOption
  from . import QStyleOptionComplex, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QFontMetrics = WAIT['QFontMetrics']
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleHintReturn = WAIT['QStyleHintReturn']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyle(QObject):
  """
  The cute side of Qt's QStyle: a plain Python object standing in front of
  one C++ QStyle.

  It is built on the cute 'QObject', as Qt's QStyle is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStyle that has a ritual and that Python can call so
  far, 33 names in all: 'metaObject', 'tr', 'name', 'polish', 'unpolish',
  'itemTextRect', 'itemPixmapRect', 'drawItemText', 'drawItemPixmap',
  'standardPalette', 'drawPrimitive', 'drawControl', 'subElementRect',
  'drawComplexControl', 'hitTestComplexControl', 'subControlRect',
  'pixelMetric', 'sizeFromContents', 'styleHint', 'standardPixmap',
  'standardIcon', 'generatedIconPixmap', 'visualRect', 'visualPos',
  'sliderPositionFromValue', 'sliderValueFromPosition', 'visualAlignment',
  'alignedRect', 'layoutSpacing', 'combinedLayoutSpacing', 'proxy',
  'setName', 'setProxy'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyle::~QStyle()': the destructor: Python never removes a C++
    QStyle.

  What has no ritual
  ------------------

  11 of the 47 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 the class is abstract, so C++ cannot make one; 2 forbidden; 1
  a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QStyle is created at the first use, not by 'QStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyle.
  - Qt tells when it has removed the C++ QStyle. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QStyle, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ComplexControl(CuteNum):
    """
    The enum 'QStyle::ComplexControl' of Qt, with the 10 names Qt gives in
    it.
    """

    CC_SpinBox = Kee[int](0)
    CC_ComboBox = Kee[int](1)
    CC_ScrollBar = Kee[int](2)
    CC_Slider = Kee[int](3)
    CC_ToolButton = Kee[int](4)
    CC_TitleBar = Kee[int](5)
    CC_Dial = Kee[int](6)
    CC_GroupBox = Kee[int](7)
    CC_MdiControls = Kee[int](8)
    CC_CustomBase = Kee[int](4026531840)

  class ContentsType(CuteNum):
    """
    The enum 'QStyle::ContentsType' of Qt, with the 24 names Qt gives in it.
    """

    CT_PushButton = Kee[int](0)
    CT_CheckBox = Kee[int](1)
    CT_RadioButton = Kee[int](2)
    CT_ToolButton = Kee[int](3)
    CT_ComboBox = Kee[int](4)
    CT_Splitter = Kee[int](5)
    CT_ProgressBar = Kee[int](6)
    CT_MenuItem = Kee[int](7)
    CT_MenuBarItem = Kee[int](8)
    CT_MenuBar = Kee[int](9)
    CT_Menu = Kee[int](10)
    CT_TabBarTab = Kee[int](11)
    CT_Slider = Kee[int](12)
    CT_ScrollBar = Kee[int](13)
    CT_LineEdit = Kee[int](14)
    CT_SpinBox = Kee[int](15)
    CT_SizeGrip = Kee[int](16)
    CT_TabWidget = Kee[int](17)
    CT_DialogButtons = Kee[int](18)
    CT_HeaderSection = Kee[int](19)
    CT_GroupBox = Kee[int](20)
    CT_MdiControls = Kee[int](21)
    CT_ItemViewItem = Kee[int](22)
    CT_CustomBase = Kee[int](4026531840)

  class ControlElement(CuteNum):
    """
    The enum 'QStyle::ControlElement' of Qt, with the 48 names Qt gives in
    it.
    """

    CE_PushButton = Kee[int](0)
    CE_PushButtonBevel = Kee[int](1)
    CE_PushButtonLabel = Kee[int](2)
    CE_CheckBox = Kee[int](3)
    CE_CheckBoxLabel = Kee[int](4)
    CE_RadioButton = Kee[int](5)
    CE_RadioButtonLabel = Kee[int](6)
    CE_TabBarTab = Kee[int](7)
    CE_TabBarTabShape = Kee[int](8)
    CE_TabBarTabLabel = Kee[int](9)
    CE_ProgressBar = Kee[int](10)
    CE_ProgressBarGroove = Kee[int](11)
    CE_ProgressBarContents = Kee[int](12)
    CE_ProgressBarLabel = Kee[int](13)
    CE_MenuItem = Kee[int](14)
    CE_MenuScroller = Kee[int](15)
    CE_MenuVMargin = Kee[int](16)
    CE_MenuHMargin = Kee[int](17)
    CE_MenuTearoff = Kee[int](18)
    CE_MenuEmptyArea = Kee[int](19)
    CE_MenuBarItem = Kee[int](20)
    CE_MenuBarEmptyArea = Kee[int](21)
    CE_ToolButtonLabel = Kee[int](22)
    CE_Header = Kee[int](23)
    CE_HeaderSection = Kee[int](24)
    CE_HeaderLabel = Kee[int](25)
    CE_ToolBoxTab = Kee[int](26)
    CE_SizeGrip = Kee[int](27)
    CE_Splitter = Kee[int](28)
    CE_RubberBand = Kee[int](29)
    CE_DockWidgetTitle = Kee[int](30)
    CE_ScrollBarAddLine = Kee[int](31)
    CE_ScrollBarSubLine = Kee[int](32)
    CE_ScrollBarAddPage = Kee[int](33)
    CE_ScrollBarSubPage = Kee[int](34)
    CE_ScrollBarSlider = Kee[int](35)
    CE_ScrollBarFirst = Kee[int](36)
    CE_ScrollBarLast = Kee[int](37)
    CE_FocusFrame = Kee[int](38)
    CE_ComboBoxLabel = Kee[int](39)
    CE_ToolBar = Kee[int](40)
    CE_ToolBoxTabShape = Kee[int](41)
    CE_ToolBoxTabLabel = Kee[int](42)
    CE_HeaderEmptyArea = Kee[int](43)
    CE_ColumnViewGrip = Kee[int](44)
    CE_ItemViewItem = Kee[int](45)
    CE_ShapedFrame = Kee[int](46)
    CE_CustomBase = Kee[int](4026531840)

  class PixelMetric(CuteNum):
    """
    The enum 'QStyle::PixelMetric' of Qt, with the 96 names Qt gives in it.
    """

    PM_ButtonMargin = Kee[int](0)
    PM_ButtonDefaultIndicator = Kee[int](1)
    PM_MenuButtonIndicator = Kee[int](2)
    PM_ButtonShiftHorizontal = Kee[int](3)
    PM_ButtonShiftVertical = Kee[int](4)
    PM_DefaultFrameWidth = Kee[int](5)
    PM_SpinBoxFrameWidth = Kee[int](6)
    PM_ComboBoxFrameWidth = Kee[int](7)
    PM_MaximumDragDistance = Kee[int](8)
    PM_ScrollBarExtent = Kee[int](9)
    PM_ScrollBarSliderMin = Kee[int](10)
    PM_SliderThickness = Kee[int](11)
    PM_SliderControlThickness = Kee[int](12)
    PM_SliderLength = Kee[int](13)
    PM_SliderTickmarkOffset = Kee[int](14)
    PM_SliderSpaceAvailable = Kee[int](15)
    PM_DockWidgetSeparatorExtent = Kee[int](16)
    PM_DockWidgetHandleExtent = Kee[int](17)
    PM_DockWidgetFrameWidth = Kee[int](18)
    PM_TabBarTabOverlap = Kee[int](19)
    PM_TabBarTabHSpace = Kee[int](20)
    PM_TabBarTabVSpace = Kee[int](21)
    PM_TabBarBaseHeight = Kee[int](22)
    PM_TabBarBaseOverlap = Kee[int](23)
    PM_ProgressBarChunkWidth = Kee[int](24)
    PM_SplitterWidth = Kee[int](25)
    PM_TitleBarHeight = Kee[int](26)
    PM_MenuScrollerHeight = Kee[int](27)
    PM_MenuHMargin = Kee[int](28)
    PM_MenuVMargin = Kee[int](29)
    PM_MenuPanelWidth = Kee[int](30)
    PM_MenuTearoffHeight = Kee[int](31)
    PM_MenuDesktopFrameWidth = Kee[int](32)
    PM_MenuBarPanelWidth = Kee[int](33)
    PM_MenuBarItemSpacing = Kee[int](34)
    PM_MenuBarVMargin = Kee[int](35)
    PM_MenuBarHMargin = Kee[int](36)
    PM_IndicatorWidth = Kee[int](37)
    PM_IndicatorHeight = Kee[int](38)
    PM_ExclusiveIndicatorWidth = Kee[int](39)
    PM_ExclusiveIndicatorHeight = Kee[int](40)
    PM_DialogButtonsSeparator = Kee[int](41)
    PM_DialogButtonsButtonWidth = Kee[int](42)
    PM_DialogButtonsButtonHeight = Kee[int](43)
    PM_MdiSubWindowFrameWidth = Kee[int](44)
    PM_MdiSubWindowMinimizedWidth = Kee[int](45)
    PM_HeaderMargin = Kee[int](46)
    PM_HeaderMarkSize = Kee[int](47)
    PM_HeaderGripMargin = Kee[int](48)
    PM_TabBarTabShiftHorizontal = Kee[int](49)
    PM_TabBarTabShiftVertical = Kee[int](50)
    PM_TabBarScrollButtonWidth = Kee[int](51)
    PM_ToolBarFrameWidth = Kee[int](52)
    PM_ToolBarHandleExtent = Kee[int](53)
    PM_ToolBarItemSpacing = Kee[int](54)
    PM_ToolBarItemMargin = Kee[int](55)
    PM_ToolBarSeparatorExtent = Kee[int](56)
    PM_ToolBarExtensionExtent = Kee[int](57)
    PM_SpinBoxSliderHeight = Kee[int](58)
    PM_ToolBarIconSize = Kee[int](59)
    PM_ListViewIconSize = Kee[int](60)
    PM_IconViewIconSize = Kee[int](61)
    PM_SmallIconSize = Kee[int](62)
    PM_LargeIconSize = Kee[int](63)
    PM_FocusFrameVMargin = Kee[int](64)
    PM_FocusFrameHMargin = Kee[int](65)
    PM_ToolTipLabelFrameWidth = Kee[int](66)
    PM_CheckBoxLabelSpacing = Kee[int](67)
    PM_TabBarIconSize = Kee[int](68)
    PM_SizeGripSize = Kee[int](69)
    PM_DockWidgetTitleMargin = Kee[int](70)
    PM_MessageBoxIconSize = Kee[int](71)
    PM_ButtonIconSize = Kee[int](72)
    PM_DockWidgetTitleBarButtonMargin = Kee[int](73)
    PM_RadioButtonLabelSpacing = Kee[int](74)
    PM_LayoutLeftMargin = Kee[int](75)
    PM_LayoutTopMargin = Kee[int](76)
    PM_LayoutRightMargin = Kee[int](77)
    PM_LayoutBottomMargin = Kee[int](78)
    PM_LayoutHorizontalSpacing = Kee[int](79)
    PM_LayoutVerticalSpacing = Kee[int](80)
    PM_TabBar_ScrollButtonOverlap = Kee[int](81)
    PM_TextCursorWidth = Kee[int](82)
    PM_TabCloseIndicatorWidth = Kee[int](83)
    PM_TabCloseIndicatorHeight = Kee[int](84)
    PM_ScrollView_ScrollBarSpacing = Kee[int](85)
    PM_ScrollView_ScrollBarOverlap = Kee[int](86)
    PM_SubMenuOverlap = Kee[int](87)
    PM_TreeViewIndentation = Kee[int](88)
    PM_HeaderDefaultSectionSizeHorizontal = Kee[int](89)
    PM_HeaderDefaultSectionSizeVertical = Kee[int](90)
    PM_TitleBarButtonIconSize = Kee[int](91)
    PM_TitleBarButtonSize = Kee[int](92)
    PM_LineEditIconSize = Kee[int](93)
    PM_LineEditIconMargin = Kee[int](94)
    PM_CustomBase = Kee[int](4026531840)

  class PrimitiveElement(CuteNum):
    """
    The enum 'QStyle::PrimitiveElement' of Qt, with the 52 names Qt gives in
    it.
    """

    PE_Frame = Kee[int](0)
    PE_FrameDefaultButton = Kee[int](1)
    PE_FrameDockWidget = Kee[int](2)
    PE_FrameFocusRect = Kee[int](3)
    PE_FrameGroupBox = Kee[int](4)
    PE_FrameLineEdit = Kee[int](5)
    PE_FrameMenu = Kee[int](6)
    PE_FrameStatusBarItem = Kee[int](7)
    PE_FrameTabWidget = Kee[int](8)
    PE_FrameWindow = Kee[int](9)
    PE_FrameButtonBevel = Kee[int](10)
    PE_FrameButtonTool = Kee[int](11)
    PE_FrameTabBarBase = Kee[int](12)
    PE_PanelButtonCommand = Kee[int](13)
    PE_PanelButtonBevel = Kee[int](14)
    PE_PanelButtonTool = Kee[int](15)
    PE_PanelMenuBar = Kee[int](16)
    PE_PanelToolBar = Kee[int](17)
    PE_PanelLineEdit = Kee[int](18)
    PE_IndicatorArrowDown = Kee[int](19)
    PE_IndicatorArrowLeft = Kee[int](20)
    PE_IndicatorArrowRight = Kee[int](21)
    PE_IndicatorArrowUp = Kee[int](22)
    PE_IndicatorBranch = Kee[int](23)
    PE_IndicatorButtonDropDown = Kee[int](24)
    PE_IndicatorItemViewItemCheck = Kee[int](25)
    PE_IndicatorCheckBox = Kee[int](26)
    PE_IndicatorDockWidgetResizeHandle = Kee[int](27)
    PE_IndicatorHeaderArrow = Kee[int](28)
    PE_IndicatorMenuCheckMark = Kee[int](29)
    PE_IndicatorProgressChunk = Kee[int](30)
    PE_IndicatorRadioButton = Kee[int](31)
    PE_IndicatorSpinDown = Kee[int](32)
    PE_IndicatorSpinMinus = Kee[int](33)
    PE_IndicatorSpinPlus = Kee[int](34)
    PE_IndicatorSpinUp = Kee[int](35)
    PE_IndicatorToolBarHandle = Kee[int](36)
    PE_IndicatorToolBarSeparator = Kee[int](37)
    PE_PanelTipLabel = Kee[int](38)
    PE_IndicatorTabTear = Kee[int](39)
    PE_IndicatorTabTearLeft = Kee[int](39)
    PE_PanelScrollAreaCorner = Kee[int](40)
    PE_Widget = Kee[int](41)
    PE_IndicatorColumnViewArrow = Kee[int](42)
    PE_IndicatorItemViewItemDrop = Kee[int](43)
    PE_PanelItemViewItem = Kee[int](44)
    PE_PanelItemViewRow = Kee[int](45)
    PE_PanelStatusBar = Kee[int](46)
    PE_IndicatorTabClose = Kee[int](47)
    PE_PanelMenu = Kee[int](48)
    PE_IndicatorTabTearRight = Kee[int](49)
    PE_CustomBase = Kee[int](251658240)

  class RequestSoftwareInputPanel(CuteNum):
    """
    The enum 'QStyle::RequestSoftwareInputPanel' of Qt, with the 2 names Qt
    gives in it.
    """

    RSIP_OnMouseClickAndAlreadyFocused = Kee[int](0)
    RSIP_OnMouseClick = Kee[int](1)

  class StandardPixmap(CuteNum):
    """
    The enum 'QStyle::StandardPixmap' of Qt, with the 85 names Qt gives in
    it.
    """

    SP_TitleBarMenuButton = Kee[int](0)
    SP_TitleBarMinButton = Kee[int](1)
    SP_TitleBarMaxButton = Kee[int](2)
    SP_TitleBarCloseButton = Kee[int](3)
    SP_TitleBarNormalButton = Kee[int](4)
    SP_TitleBarShadeButton = Kee[int](5)
    SP_TitleBarUnshadeButton = Kee[int](6)
    SP_TitleBarContextHelpButton = Kee[int](7)
    SP_DockWidgetCloseButton = Kee[int](8)
    SP_MessageBoxInformation = Kee[int](9)
    SP_MessageBoxWarning = Kee[int](10)
    SP_MessageBoxCritical = Kee[int](11)
    SP_MessageBoxQuestion = Kee[int](12)
    SP_DesktopIcon = Kee[int](13)
    SP_TrashIcon = Kee[int](14)
    SP_ComputerIcon = Kee[int](15)
    SP_DriveFDIcon = Kee[int](16)
    SP_DriveHDIcon = Kee[int](17)
    SP_DriveCDIcon = Kee[int](18)
    SP_DriveDVDIcon = Kee[int](19)
    SP_DriveNetIcon = Kee[int](20)
    SP_DirOpenIcon = Kee[int](21)
    SP_DirClosedIcon = Kee[int](22)
    SP_DirLinkIcon = Kee[int](23)
    SP_DirLinkOpenIcon = Kee[int](24)
    SP_FileIcon = Kee[int](25)
    SP_FileLinkIcon = Kee[int](26)
    SP_ToolBarHorizontalExtensionButton = Kee[int](27)
    SP_ToolBarVerticalExtensionButton = Kee[int](28)
    SP_FileDialogStart = Kee[int](29)
    SP_FileDialogEnd = Kee[int](30)
    SP_FileDialogToParent = Kee[int](31)
    SP_FileDialogNewFolder = Kee[int](32)
    SP_FileDialogDetailedView = Kee[int](33)
    SP_FileDialogInfoView = Kee[int](34)
    SP_FileDialogContentsView = Kee[int](35)
    SP_FileDialogListView = Kee[int](36)
    SP_FileDialogBack = Kee[int](37)
    SP_DirIcon = Kee[int](38)
    SP_DialogOkButton = Kee[int](39)
    SP_DialogCancelButton = Kee[int](40)
    SP_DialogHelpButton = Kee[int](41)
    SP_DialogOpenButton = Kee[int](42)
    SP_DialogSaveButton = Kee[int](43)
    SP_DialogCloseButton = Kee[int](44)
    SP_DialogApplyButton = Kee[int](45)
    SP_DialogResetButton = Kee[int](46)
    SP_DialogDiscardButton = Kee[int](47)
    SP_DialogYesButton = Kee[int](48)
    SP_DialogNoButton = Kee[int](49)
    SP_ArrowUp = Kee[int](50)
    SP_ArrowDown = Kee[int](51)
    SP_ArrowLeft = Kee[int](52)
    SP_ArrowRight = Kee[int](53)
    SP_ArrowBack = Kee[int](54)
    SP_ArrowForward = Kee[int](55)
    SP_DirHomeIcon = Kee[int](56)
    SP_CommandLink = Kee[int](57)
    SP_VistaShield = Kee[int](58)
    SP_BrowserReload = Kee[int](59)
    SP_BrowserStop = Kee[int](60)
    SP_MediaPlay = Kee[int](61)
    SP_MediaStop = Kee[int](62)
    SP_MediaPause = Kee[int](63)
    SP_MediaSkipForward = Kee[int](64)
    SP_MediaSkipBackward = Kee[int](65)
    SP_MediaSeekForward = Kee[int](66)
    SP_MediaSeekBackward = Kee[int](67)
    SP_MediaVolume = Kee[int](68)
    SP_MediaVolumeMuted = Kee[int](69)
    SP_LineEditClearButton = Kee[int](70)
    SP_DialogYesToAllButton = Kee[int](71)
    SP_DialogNoToAllButton = Kee[int](72)
    SP_DialogSaveAllButton = Kee[int](73)
    SP_DialogAbortButton = Kee[int](74)
    SP_DialogRetryButton = Kee[int](75)
    SP_DialogIgnoreButton = Kee[int](76)
    SP_RestoreDefaultsButton = Kee[int](77)
    SP_TabCloseButton = Kee[int](78)
    SP_TabScrollLeftButton = Kee[int](79)
    SP_TabScrollRightButton = Kee[int](80)
    SP_TabScrollUpButton = Kee[int](81)
    SP_TabScrollDownButton = Kee[int](82)
    NStandardPixmap = Kee[int](83)
    SP_CustomBase = Kee[int](4026531840)

  class StateFlag(CuteFlags):
    """
    The flags enum 'QStyle::StateFlag' of Qt, with the 28 names Qt gives in
    it. Qt names the type of its combinations 'QStyle::State'.
    """

    State_None = 0x0
    State_Enabled = 0x1
    State_Raised = 0x2
    State_Sunken = 0x4
    State_Off = 0x8
    State_NoChange = 0x10
    State_On = 0x20
    State_DownArrow = 0x40
    State_Horizontal = 0x80
    State_HasFocus = 0x100
    State_Top = 0x200
    State_Bottom = 0x400
    State_FocusAtBorder = 0x800
    State_AutoRaise = 0x1000
    State_MouseOver = 0x2000
    State_UpArrow = 0x4000
    State_Selected = 0x8000
    State_Active = 0x10000
    State_Window = 0x20000
    State_Open = 0x40000
    State_Children = 0x80000
    State_Item = 0x100000
    State_Sibling = 0x200000
    State_Editing = 0x400000
    State_KeyboardFocusChange = 0x800000
    State_ReadOnly = 0x2000000
    State_Small = 0x4000000
    State_Mini = 0x8000000

  State = StateFlag

  class StyleHint(CuteNum):
    """
    The enum 'QStyle::StyleHint' of Qt, with the 123 names Qt gives in it.
    """

    SH_EtchDisabledText = Kee[int](0)
    SH_DitherDisabledText = Kee[int](1)
    SH_ScrollBar_MiddleClickAbsolutePosition = Kee[int](2)
    SH_ScrollBar_ScrollWhenPointerLeavesControl = Kee[int](3)
    SH_TabBar_SelectMouseType = Kee[int](4)
    SH_TabBar_Alignment = Kee[int](5)
    SH_Header_ArrowAlignment = Kee[int](6)
    SH_Slider_SnapToValue = Kee[int](7)
    SH_Slider_SloppyKeyEvents = Kee[int](8)
    SH_ProgressDialog_CenterCancelButton = Kee[int](9)
    SH_ProgressDialog_TextLabelAlignment = Kee[int](10)
    SH_PrintDialog_RightAlignButtons = Kee[int](11)
    SH_MainWindow_SpaceBelowMenuBar = Kee[int](12)
    SH_FontDialog_SelectAssociatedText = Kee[int](13)
    SH_Menu_AllowActiveAndDisabled = Kee[int](14)
    SH_Menu_SpaceActivatesItem = Kee[int](15)
    SH_Menu_SubMenuPopupDelay = Kee[int](16)
    SH_ScrollView_FrameOnlyAroundContents = Kee[int](17)
    SH_MenuBar_AltKeyNavigation = Kee[int](18)
    SH_ComboBox_ListMouseTracking = Kee[int](19)
    SH_ComboBox_ListMouseTracking_Current = Kee[int](19)
    SH_Menu_MouseTracking = Kee[int](20)
    SH_MenuBar_MouseTracking = Kee[int](21)
    SH_ItemView_ChangeHighlightOnFocus = Kee[int](22)
    SH_Widget_ShareActivation = Kee[int](23)
    SH_Workspace_FillSpaceOnMaximize = Kee[int](24)
    SH_ComboBox_Popup = Kee[int](25)
    SH_TitleBar_NoBorder = Kee[int](26)
    SH_Slider_StopMouseOverSlider = Kee[int](27)
    SH_BlinkCursorWhenTextSelected = Kee[int](28)
    SH_RichText_FullWidthSelection = Kee[int](29)
    SH_Menu_Scrollable = Kee[int](30)
    SH_GroupBox_TextLabelVerticalAlignment = Kee[int](31)
    SH_GroupBox_TextLabelColor = Kee[int](32)
    SH_Menu_SloppySubMenus = Kee[int](33)
    SH_Table_GridLineColor = Kee[int](34)
    SH_LineEdit_PasswordCharacter = Kee[int](35)
    SH_DialogButtons_DefaultButton = Kee[int](36)
    SH_ToolBox_SelectedPageTitleBold = Kee[int](37)
    SH_TabBar_PreferNoArrows = Kee[int](38)
    SH_ScrollBar_LeftClickAbsolutePosition = Kee[int](39)
    SH_ListViewExpand_SelectMouseType = Kee[int](40)
    SH_UnderlineShortcut = Kee[int](41)
    SH_SpinBox_AnimateButton = Kee[int](42)
    SH_SpinBox_KeyPressAutoRepeatRate = Kee[int](43)
    SH_SpinBox_ClickAutoRepeatRate = Kee[int](44)
    SH_Menu_FillScreenWithScroll = Kee[int](45)
    SH_ToolTipLabel_Opacity = Kee[int](46)
    SH_DrawMenuBarSeparator = Kee[int](47)
    SH_TitleBar_ModifyNotification = Kee[int](48)
    SH_Button_FocusPolicy = Kee[int](49)
    SH_MessageBox_UseBorderForButtonSpacing = Kee[int](50)
    SH_TitleBar_AutoRaise = Kee[int](51)
    SH_ToolButton_PopupDelay = Kee[int](52)
    SH_FocusFrame_Mask = Kee[int](53)
    SH_RubberBand_Mask = Kee[int](54)
    SH_WindowFrame_Mask = Kee[int](55)
    SH_SpinControls_DisableOnBounds = Kee[int](56)
    SH_Dial_BackgroundRole = Kee[int](57)
    SH_ComboBox_LayoutDirection = Kee[int](58)
    SH_ItemView_EllipsisLocation = Kee[int](59)
    SH_ItemView_ShowDecorationSelected = Kee[int](60)
    SH_ItemView_ActivateItemOnSingleClick = Kee[int](61)
    SH_ScrollBar_ContextMenu = Kee[int](62)
    SH_ScrollBar_RollBetweenButtons = Kee[int](63)
    SH_Slider_AbsoluteSetButtons = Kee[int](64)
    SH_Slider_PageSetButtons = Kee[int](65)
    SH_Menu_KeyboardSearch = Kee[int](66)
    SH_TabBar_ElideMode = Kee[int](67)
    SH_DialogButtonLayout = Kee[int](68)
    SH_ComboBox_PopupFrameStyle = Kee[int](69)
    SH_MessageBox_TextInteractionFlags = Kee[int](70)
    SH_DialogButtonBox_ButtonsHaveIcons = Kee[int](71)
    SH_MessageBox_CenterButtons = Kee[int](72)
    SH_Menu_SelectionWrap = Kee[int](73)
    SH_ItemView_MovementWithoutUpdatingSelection = Kee[int](74)
    SH_ToolTip_Mask = Kee[int](75)
    SH_FocusFrame_AboveWidget = Kee[int](76)
    SH_TextControl_FocusIndicatorTextCharFormat = Kee[int](77)
    SH_WizardStyle = Kee[int](78)
    SH_ItemView_ArrowKeysNavigateIntoChildren = Kee[int](79)
    SH_Menu_Mask = Kee[int](80)
    SH_Menu_FlashTriggeredItem = Kee[int](81)
    SH_Menu_FadeOutOnHide = Kee[int](82)
    SH_SpinBox_ClickAutoRepeatThreshold = Kee[int](83)
    SH_ItemView_PaintAlternatingRowColorsForEmptyArea = Kee[int](84)
    SH_FormLayoutWrapPolicy = Kee[int](85)
    SH_TabWidget_DefaultTabPosition = Kee[int](86)
    SH_ToolBar_Movable = Kee[int](87)
    SH_FormLayoutFieldGrowthPolicy = Kee[int](88)
    SH_FormLayoutFormAlignment = Kee[int](89)
    SH_FormLayoutLabelAlignment = Kee[int](90)
    SH_ItemView_DrawDelegateFrame = Kee[int](91)
    SH_TabBar_CloseButtonPosition = Kee[int](92)
    SH_DockWidget_ButtonsHaveFrame = Kee[int](93)
    SH_ToolButtonStyle = Kee[int](94)
    SH_RequestSoftwareInputPanel = Kee[int](95)
    SH_ScrollBar_Transient = Kee[int](96)
    SH_Menu_SupportsSections = Kee[int](97)
    SH_ToolTip_WakeUpDelay = Kee[int](98)
    SH_ToolTip_FallAsleepDelay = Kee[int](99)
    SH_Widget_Animate = Kee[int](100)
    SH_Splitter_OpaqueResize = Kee[int](101)
    SH_ComboBox_UseNativePopup = Kee[int](102)
    SH_LineEdit_PasswordMaskDelay = Kee[int](103)
    SH_TabBar_ChangeCurrentDelay = Kee[int](104)
    SH_Menu_SubMenuUniDirection = Kee[int](105)
    SH_Menu_SubMenuUniDirectionFailCount = Kee[int](106)
    SH_Menu_SubMenuSloppySelectOtherActions = Kee[int](107)
    SH_Menu_SubMenuSloppyCloseTimeout = Kee[int](108)
    SH_Menu_SubMenuResetWhenReenteringParent = Kee[int](109)
    SH_Menu_SubMenuDontStartSloppyOnLeave = Kee[int](110)
    SH_ItemView_ScrollMode = Kee[int](111)
    SH_TitleBar_ShowToolTipsOnButtons = Kee[int](112)
    SH_Widget_Animation_Duration = Kee[int](113)
    SH_ComboBox_AllowWheelScrolling = Kee[int](114)
    SH_SpinBox_ButtonsInsideFrame = Kee[int](115)
    SH_SpinBox_StepModifier = Kee[int](116)
    SH_TabBar_AllowWheelScrolling = Kee[int](117)
    SH_Table_AlwaysDrawLeftTopGridLines = Kee[int](118)
    SH_SpinBox_SelectOnStep = Kee[int](119)
    SH_ComboBox_ListMouseTracking_Active = Kee[int](120)
    SH_CustomBase = Kee[int](4026531840)

  class SubControl(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QStyle::SubControl' of Qt, with the 43 names Qt gives in
    it. Qt names the type of its combinations 'QStyle::SubControls'.
    """

    SC_None = 0x0
    SC_ScrollBarAddLine = 0x1
    SC_ScrollBarSubLine = 0x2
    SC_ScrollBarAddPage = 0x4
    SC_ScrollBarSubPage = 0x8
    SC_ScrollBarFirst = 0x10
    SC_ScrollBarLast = 0x20
    SC_ScrollBarSlider = 0x40
    SC_ScrollBarGroove = 0x80
    SC_SpinBoxUp = 0x1
    SC_SpinBoxDown = 0x2
    SC_SpinBoxFrame = 0x4
    SC_SpinBoxEditField = 0x8
    SC_ComboBoxFrame = 0x1
    SC_ComboBoxEditField = 0x2
    SC_ComboBoxArrow = 0x4
    SC_ComboBoxListBoxPopup = 0x8
    SC_SliderGroove = 0x1
    SC_SliderHandle = 0x2
    SC_SliderTickmarks = 0x4
    SC_ToolButton = 0x1
    SC_ToolButtonMenu = 0x2
    SC_TitleBarSysMenu = 0x1
    SC_TitleBarMinButton = 0x2
    SC_TitleBarMaxButton = 0x4
    SC_TitleBarCloseButton = 0x8
    SC_TitleBarNormalButton = 0x10
    SC_TitleBarShadeButton = 0x20
    SC_TitleBarUnshadeButton = 0x40
    SC_TitleBarContextHelpButton = 0x80
    SC_TitleBarLabel = 0x100
    SC_DialGroove = 0x1
    SC_DialHandle = 0x2
    SC_DialTickmarks = 0x4
    SC_GroupBoxCheckBox = 0x1
    SC_GroupBoxLabel = 0x2
    SC_GroupBoxContents = 0x4
    SC_GroupBoxFrame = 0x8
    SC_MdiMinButton = 0x1
    SC_MdiNormalButton = 0x2
    SC_MdiCloseButton = 0x4
    SC_CustomBase = 0xf0000000
    SC_All = 0xffffffff

  SubControls = SubControl

  class SubElement(CuteNum):
    """
    The enum 'QStyle::SubElement' of Qt, with the 59 names Qt gives in it.
    """

    SE_PushButtonContents = Kee[int](0)
    SE_PushButtonFocusRect = Kee[int](1)
    SE_CheckBoxIndicator = Kee[int](2)
    SE_CheckBoxContents = Kee[int](3)
    SE_CheckBoxFocusRect = Kee[int](4)
    SE_CheckBoxClickRect = Kee[int](5)
    SE_RadioButtonIndicator = Kee[int](6)
    SE_RadioButtonContents = Kee[int](7)
    SE_RadioButtonFocusRect = Kee[int](8)
    SE_RadioButtonClickRect = Kee[int](9)
    SE_ComboBoxFocusRect = Kee[int](10)
    SE_SliderFocusRect = Kee[int](11)
    SE_ProgressBarGroove = Kee[int](12)
    SE_ProgressBarContents = Kee[int](13)
    SE_ProgressBarLabel = Kee[int](14)
    SE_ToolBoxTabContents = Kee[int](15)
    SE_HeaderLabel = Kee[int](16)
    SE_HeaderArrow = Kee[int](17)
    SE_TabWidgetTabBar = Kee[int](18)
    SE_TabWidgetTabPane = Kee[int](19)
    SE_TabWidgetTabContents = Kee[int](20)
    SE_TabWidgetLeftCorner = Kee[int](21)
    SE_TabWidgetRightCorner = Kee[int](22)
    SE_ItemViewItemCheckIndicator = Kee[int](23)
    SE_TabBarTearIndicator = Kee[int](24)
    SE_TabBarTearIndicatorLeft = Kee[int](24)
    SE_TreeViewDisclosureItem = Kee[int](25)
    SE_LineEditContents = Kee[int](26)
    SE_FrameContents = Kee[int](27)
    SE_DockWidgetCloseButton = Kee[int](28)
    SE_DockWidgetFloatButton = Kee[int](29)
    SE_DockWidgetTitleBarText = Kee[int](30)
    SE_DockWidgetIcon = Kee[int](31)
    SE_CheckBoxLayoutItem = Kee[int](32)
    SE_ComboBoxLayoutItem = Kee[int](33)
    SE_DateTimeEditLayoutItem = Kee[int](34)
    SE_LabelLayoutItem = Kee[int](35)
    SE_ProgressBarLayoutItem = Kee[int](36)
    SE_PushButtonLayoutItem = Kee[int](37)
    SE_RadioButtonLayoutItem = Kee[int](38)
    SE_SliderLayoutItem = Kee[int](39)
    SE_SpinBoxLayoutItem = Kee[int](40)
    SE_ToolButtonLayoutItem = Kee[int](41)
    SE_FrameLayoutItem = Kee[int](42)
    SE_GroupBoxLayoutItem = Kee[int](43)
    SE_TabWidgetLayoutItem = Kee[int](44)
    SE_ItemViewItemDecoration = Kee[int](45)
    SE_ItemViewItemText = Kee[int](46)
    SE_ItemViewItemFocusRect = Kee[int](47)
    SE_TabBarTabLeftButton = Kee[int](48)
    SE_TabBarTabRightButton = Kee[int](49)
    SE_TabBarTabText = Kee[int](50)
    SE_ShapedFrameContents = Kee[int](51)
    SE_ToolBarHandle = Kee[int](52)
    SE_TabBarScrollLeftButton = Kee[int](53)
    SE_TabBarScrollRightButton = Kee[int](54)
    SE_TabBarTearIndicatorRight = Kee[int](55)
    SE_PushButtonBevel = Kee[int](56)
    SE_CustomBase = Kee[int](4026531840)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QStyle::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(Qt.LayoutDirection, QRect, QRect)
  def visualRect(
      direction: Qt.LayoutDirection,
      boundingRect: QRect,
      logicalRect: QRect,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::visualRect(Qt::LayoutDirection direction, const
    QRect &boundingRect, const QRect &logicalRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#visualRect

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    boundingRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    logicalRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::visualRect(Qt::LayoutDirection direction, const QRect
    #      &boundingRect, const QRect &logicalRect)
    address = Rituals.call(
        'ritual_ZN6QStyle10visualRectEN2Qt15LayoutDirectionERK5QRectS4_',
        direction.value, CuteMixin._valueOf(boundingRect),
        CuteMixin._valueOf(logicalRect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(Qt.LayoutDirection, QRect, QPoint)
  def visualPos(
      direction: Qt.LayoutDirection,
      boundingRect: QRect,
      logicalPos: QPoint,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QStyle::visualPos(Qt::LayoutDirection direction, const
    QRect &boundingRect, const QPoint &logicalPos)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#visualPos

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    boundingRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    logicalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QStyle::visualPos(Qt::LayoutDirection direction, const QRect
    #      &boundingRect, const QPoint &logicalPos)
    address = Rituals.call(
        'ritual_ZN6QStyle9visualPosEN2Qt15LayoutDirectionERK5QRectRK6QPoint',
        direction.value, CuteMixin._valueOf(boundingRect),
        CuteMixin._valueOf(logicalPos),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @staticmethod
  @overload(int, int, int, int)
  @overload(int, int, int, int, bool)
  def sliderPositionFromValue(
      min: int,
      max: int,
      val: int,
      space: int,
      upsideDown: bool = False,
  ) -> int:
    """
    Calls Qt's 'int QStyle::sliderPositionFromValue(int min, int max, int
    val, int space, bool upsideDown)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyle.html#sliderPositionFromValue

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.

    val : int
      Passed on as it is.

    space : int
      Passed on as it is.

    upsideDown : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  int QStyle::sliderPositionFromValue(int min, int max, int val, int
    #      space, bool upsideDown)
    return Rituals.call(
        'ritual_ZN6QStyle23sliderPositionFromValueEiiiib',
        min, max, val, space, upsideDown,
    )

  @staticmethod
  @overload(int, int, int, int)
  @overload(int, int, int, int, bool)
  def sliderValueFromPosition(
      min: int,
      max: int,
      pos: int,
      space: int,
      upsideDown: bool = False,
  ) -> int:
    """
    Calls Qt's 'int QStyle::sliderValueFromPosition(int min, int max, int
    pos, int space, bool upsideDown)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyle.html#sliderValueFromPosition

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.

    pos : int
      Passed on as it is.

    space : int
      Passed on as it is.

    upsideDown : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  int QStyle::sliderValueFromPosition(int min, int max, int pos, int
    #      space, bool upsideDown)
    return Rituals.call(
        'ritual_ZN6QStyle23sliderValueFromPositionEiiiib',
        min, max, pos, space, upsideDown,
    )

  @staticmethod
  @overload(Qt.LayoutDirection, Qt.Alignment)
  def visualAlignment(
      direction: Qt.LayoutDirection,
      alignment: Qt.Alignment,
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QStyle::visualAlignment(Qt::LayoutDirection
    direction, Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#visualAlignment

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    alignment : Qt.Alignment
      Passed on as its number.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QStyle::visualAlignment(Qt::LayoutDirection direction,
    #      Qt::Alignment alignment)
    return Qt.Alignment(Rituals.call(
        'ritual_ZN6QStyle15visualAlignmentEN2Qt15LayoutDirectionE6QFlagsINS'
        '0_13AlignmentFlagEE',
        direction.value, alignment.value,
    ))

  @staticmethod
  @overload(Qt.LayoutDirection, Qt.Alignment, QSize, QRect)
  def alignedRect(
      direction: Qt.LayoutDirection,
      alignment: Qt.Alignment,
      size: QSize,
      rectangle: QRect,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::alignedRect(Qt::LayoutDirection direction,
    Qt::Alignment alignment, const QSize &size, const QRect &rectangle)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#alignedRect

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    alignment : Qt.Alignment
      Passed on as its number.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    rectangle : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::alignedRect(Qt::LayoutDirection direction, Qt::Alignment
    #      alignment, const QSize &size, const QRect &rectangle)
    address = Rituals.call(
        'ritual_ZN6QStyle11alignedRectEN2Qt15LayoutDirectionE6QFlagsINS0_13'
        'AlignmentFlagEERK5QSizeRK5QRect',
        direction.value, alignment.value, CuteMixin._valueOf(size),
        CuteMixin._valueOf(rectangle),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyle'

  #  A C++ QStyle Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStyle'

  #  The functions Qt calls itself that QStyle is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'polish': (
          ('_ZN6QStyle6polishEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZN6QStyle6polishEP12QApplication',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QApplication'),
           )),
      ),
      'unpolish': (
          ('_ZN6QStyle8unpolishEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZN6QStyle8unpolishEP12QApplication',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QApplication'),
           )),
      ),
      'itemTextRect': (
          ('_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'value', 'QtGui:QFontMetrics'),
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'number', ''),
               ('bool', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'itemPixmapRect': (
          ('_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QPixmap'),
           )),
      ),
      'drawItemText': (
          ('_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QSt'
           'ringNS5_9ColorRoleE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QPalette'),
               ('bool', 'number', ''),
               ('address', 'text', ''),
               ('int', 'enum', 'QtGui:QPalette.ColorRole'),
           )),
      ),
      'drawItemPixmap': (
          ('_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QPixmap'),
           )),
      ),
      'standardPalette': (
          ('_ZNK6QStyle15standardPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
      'drawPrimitive': (
          ('_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleOpti'
           'onP8QPainterPK7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PrimitiveElement'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'drawControl': (
          ('_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptionP8'
           'QPainterPK7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ControlElement'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'subElementRect': (
          ('_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7'
           'QWidget',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.SubElement'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'drawComplexControl': (
          ('_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleO'
           'ptionComplexP8QPainterPK7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address', 'QtWidgets:QStyleOptionComplex'),
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'hitTestComplexControl': (
          ('_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QSty'
           'leOptionComplexRK6QPointPK7QWidget',
           ('int', 'enum', 'QtWidgets:QStyle.SubControl'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address', 'QtWidgets:QStyleOptionComplex'),
               ('address', 'value', 'QtCore:QPoint'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'subControlRect': (
          ('_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptio'
           'nComplexNS_10SubControlEPK7QWidget',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address', 'QtWidgets:QStyleOptionComplex'),
               ('int', 'enum', 'QtWidgets:QStyle.SubControl'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'pixelMetric': (
          ('_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QW'
           'idget',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PixelMetric'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'sizeFromContents': (
          ('_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptio'
           'nRK5QSizePK7QWidget',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ContentsType'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'styleHint': (
          ('_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP'
           '16QStyleHintReturn',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StyleHint'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QStyleHintReturn'),
           )),
      ),
      'standardPixmap': (
          ('_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptio'
           'nPK7QWidget',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'standardIcon': (
          ('_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionP'
           'K7QWidget',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'generatedIconPixmap': (
          ('_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QSt'
           'yleOption',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('address', 'value', 'QtGui:QPixmap'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
           )),
      ),
      'layoutSpacing': (
          ('_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt1'
           '1OrientationEPK12QStyleOptionPK7QWidget',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtWidgets:QSizePolicy.ControlType'),
               ('int', 'enum', 'QtWidgets:QSizePolicy.ControlType'),
               ('int', 'enum', 'QtCore:Qt.Orientation'),
               ('address', 'address', 'QtWidgets:QStyleOption'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QStyle::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStyle::name() const
    return self.uglySide.call('ritual_ZNK6QStyle4nameEv')

  @overload(QFontMetrics, QRect, int, bool, str)
  def itemTextRect(
      self,
      fm: QFontMetrics,
      r: QRect,
      flags: int,
      enabled: bool,
      text: str,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::itemTextRect(const QFontMetrics &fm, const
    QRect &r, int flags, bool enabled, const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#itemTextRect

    Parameters
    ----------

    fm : QFontMetrics
      Passed on as a value: Qt reads the C++ QFontMetrics, which stays
      Python's own.

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    enabled : bool
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r, int
    #      flags, bool enabled, const QString &text) const
    ritual = (
        'ritual_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QStri'
        'ng')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK'
          '7QString')
    address = self.uglySide.call(
        ritual, self._valueOf(fm), self._valueOf(r), flags, enabled, text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect, int, QPixmap)
  def itemPixmapRect(self, r: QRect, flags: int, pixmap: QPixmap) -> QRect:
    """
    Calls Qt's 'QRect QStyle::itemPixmapRect(const QRect &r, int flags, const
    QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#itemPixmapRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::itemPixmapRect(const QRect &r, int flags, const QPixmap
    #      &pixmap) const
    ritual = 'ritual_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap'
    address = self.uglySide.call(
        ritual, self._valueOf(r), flags, self._valueOf(pixmap),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QStyle::standardPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QStyle::standardPalette() const
    ritual = 'ritual_ZNK6QStyle15standardPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QStyle15standardPaletteEv'
    address = self.uglySide.call(ritual)
    return QPalette._cuteOwning(address)

  @overload(SubElement, QStyleOption)
  @overload(SubElement, NoneType)
  @overload(SubElement, QStyleOption, QWidget)
  @overload(SubElement, QStyleOption, NoneType)
  @overload(SubElement, NoneType, QWidget)
  @overload(SubElement, NoneType, NoneType)
  def subElementRect(
      self,
      subElement: SubElement,
      option: Optional[QStyleOption],
      widget: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::subElementRect(SubElement subElement, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#subElementRect

    Parameters
    ----------

    subElement : SubElement
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::subElementRect(SubElement subElement, const QStyleOption
    #      *option, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOption'
        'PK7QWidget',
        subElement.value, self._addressOf(option), self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(ComplexControl, QStyleOptionComplex, QPoint)
  @overload(ComplexControl, NoneType, QPoint)
  @overload(ComplexControl, QStyleOptionComplex, QPoint, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, QPoint, NoneType)
  @overload(ComplexControl, NoneType, QPoint, QWidget)
  @overload(ComplexControl, NoneType, QPoint, NoneType)
  def hitTestComplexControl(
      self,
      cc: ComplexControl,
      opt: Optional[QStyleOptionComplex],
      pt: QPoint,
      widget: Optional[QWidget] = None,
  ) -> SubControl:
    """
    Calls Qt's 'SubControl QStyle::hitTestComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, const QPoint &pt, const QWidget *widget)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#hitTestComplexControl

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SubControl(number)'
      gives.
    """
    #  SubControl QStyle::hitTestComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *widget)
    #      const
    return QStyle.SubControl(self.uglySide.call(
        'ritual_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19Q'
        'StyleOptionComplexRK6QPointPK7QWidget',
        cc.value, self._addressOf(opt), self._valueOf(pt),
        self._addressOf(widget),
    ))

  @overload(ComplexControl, QStyleOptionComplex, SubControl)
  @overload(ComplexControl, NoneType, SubControl)
  @overload(ComplexControl, QStyleOptionComplex, SubControl, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, SubControl, NoneType)
  @overload(ComplexControl, NoneType, SubControl, QWidget)
  @overload(ComplexControl, NoneType, SubControl, NoneType)
  def subControlRect(
      self,
      cc: ComplexControl,
      opt: Optional[QStyleOptionComplex],
      sc: SubControl,
      widget: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#subControlRect

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : SubControl
      Passed on as its number.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOp'
        'tionComplexNS_10SubControlEPK7QWidget',
        cc.value, self._addressOf(opt), sc.value, self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(PixelMetric)
  @overload(PixelMetric, QStyleOption)
  @overload(PixelMetric, NoneType)
  @overload(PixelMetric, QStyleOption, QWidget)
  @overload(PixelMetric, QStyleOption, NoneType)
  @overload(PixelMetric, NoneType, QWidget)
  @overload(PixelMetric, NoneType, NoneType)
  def pixelMetric(
      self,
      metric: PixelMetric,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyle::pixelMetric(PixelMetric metric, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#pixelMetric

    Parameters
    ----------

    metric : PixelMetric
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyle::pixelMetric(PixelMetric metric, const QStyleOption
    #      *option, const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK'
        '7QWidget',
        metric.value, self._addressOf(option), self._addressOf(widget),
    )

  @overload(ContentsType, QStyleOption, QSize)
  @overload(ContentsType, NoneType, QSize)
  @overload(ContentsType, QStyleOption, QSize, QWidget)
  @overload(ContentsType, QStyleOption, QSize, NoneType)
  @overload(ContentsType, NoneType, QSize, QWidget)
  @overload(ContentsType, NoneType, QSize, NoneType)
  def sizeFromContents(
      self,
      ct: ContentsType,
      opt: Optional[QStyleOption],
      contentsSize: QSize,
      w: Optional[QWidget] = None,
  ) -> QSize:
    """
    Calls Qt's 'QSize QStyle::sizeFromContents(ContentsType ct, const
    QStyleOption *opt, const QSize &contentsSize, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#sizeFromContents

    Parameters
    ----------

    ct : ContentsType
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QStyle::sizeFromContents(ContentsType ct, const QStyleOption
    #      *opt, const QSize &contentsSize, const QWidget *w) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOp'
        'tionRK5QSizePK7QWidget',
        ct.value, self._addressOf(opt), self._valueOf(contentsSize),
        self._addressOf(w),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(StyleHint)
  @overload(StyleHint, QStyleOption)
  @overload(StyleHint, NoneType)
  @overload(StyleHint, QStyleOption, QWidget)
  @overload(StyleHint, QStyleOption, NoneType)
  @overload(StyleHint, NoneType, QWidget)
  @overload(StyleHint, NoneType, NoneType)
  @overload(StyleHint, QStyleOption, QWidget, QStyleHintReturn)
  @overload(StyleHint, QStyleOption, QWidget, NoneType)
  @overload(StyleHint, QStyleOption, NoneType, QStyleHintReturn)
  @overload(StyleHint, QStyleOption, NoneType, NoneType)
  @overload(StyleHint, NoneType, QWidget, QStyleHintReturn)
  @overload(StyleHint, NoneType, QWidget, NoneType)
  @overload(StyleHint, NoneType, NoneType, QStyleHintReturn)
  @overload(StyleHint, NoneType, NoneType, NoneType)
  def styleHint(
      self,
      stylehint: StyleHint,
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
      returnData: Optional[QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyle::styleHint(StyleHint stylehint, const QStyleOption
    *opt, const QWidget *widget, QStyleHintReturn *returnData) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#styleHint

    Parameters
    ----------

    stylehint : StyleHint
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    returnData : Optional[QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyle::styleHint(StyleHint stylehint, const QStyleOption *opt,
    #      const QWidget *widget, QStyleHintReturn *returnData) const
    return self.uglySide.call(
        'ritual_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidg'
        'etP16QStyleHintReturn',
        stylehint.value, self._addressOf(opt), self._addressOf(widget),
        self._addressOf(returnData),
    )

  @overload(StandardPixmap)
  @overload(StandardPixmap, QStyleOption)
  @overload(StandardPixmap, NoneType)
  @overload(StandardPixmap, QStyleOption, QWidget)
  @overload(StandardPixmap, QStyleOption, NoneType)
  @overload(StandardPixmap, NoneType, QWidget)
  @overload(StandardPixmap, NoneType, NoneType)
  def standardPixmap(
      self,
      standardPixmap: StandardPixmap,
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QStyle::standardPixmap(StandardPixmap standardPixmap,
    const QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#standardPixmap

    Parameters
    ----------

    standardPixmap : StandardPixmap
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QStyle::standardPixmap(StandardPixmap standardPixmap, const
    #      QStyleOption *opt, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOp'
        'tionPK7QWidget',
        standardPixmap.value, self._addressOf(opt), self._addressOf(widget),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(StandardPixmap)
  @overload(StandardPixmap, QStyleOption)
  @overload(StandardPixmap, NoneType)
  @overload(StandardPixmap, QStyleOption, QWidget)
  @overload(StandardPixmap, QStyleOption, NoneType)
  @overload(StandardPixmap, NoneType, QWidget)
  @overload(StandardPixmap, NoneType, NoneType)
  def standardIcon(
      self,
      standardIcon: StandardPixmap,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QStyle::standardIcon(StandardPixmap standardIcon, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#standardIcon

    Parameters
    ----------

    standardIcon : StandardPixmap
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *option, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOpti'
        'onPK7QWidget',
        standardIcon.value, self._addressOf(option), self._addressOf(widget),
    )
    return QIcon._cuteOwning(address)

  @overload(QIcon.Mode, QPixmap, QStyleOption)
  @overload(QIcon.Mode, QPixmap, NoneType)
  def generatedIconPixmap(
      self,
      iconMode: QIcon.Mode,
      pixmap: QPixmap,
      opt: Optional[QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QStyle::generatedIconPixmap(QIcon::Mode iconMode,
    const QPixmap &pixmap, const QStyleOption *opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#generatedIconPixmap

    Parameters
    ----------

    iconMode : QIcon.Mode
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QStyle::generatedIconPixmap(QIcon::Mode iconMode, const
    #      QPixmap &pixmap, const QStyleOption *opt) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12'
        'QStyleOption',
        iconMode.value, self._valueOf(pixmap), self._addressOf(opt),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation)
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      QStyleOption,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      NoneType,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      QStyleOption, QWidget,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      QStyleOption, NoneType,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      NoneType, QWidget,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      NoneType, NoneType,
  )
  def layoutSpacing(
      self,
      control1: QSizePolicy.ControlType,
      control2: QSizePolicy.ControlType,
      orientation: Qt.Orientation,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyle::layoutSpacing(QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2, Qt::Orientation orientation, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#layoutSpacing

    Parameters
    ----------

    control1 : QSizePolicy.ControlType
      Passed on as its number.

    control2 : QSizePolicy.ControlType
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyle::layoutSpacing(QSizePolicy::ControlType control1,
    #      QSizePolicy::ControlType control2, Qt::Orientation orientation,
    #      const QStyleOption *option, const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2'
        'Qt11OrientationEPK12QStyleOptionPK7QWidget',
        control1.value, control2.value, orientation.value,
        self._addressOf(option), self._addressOf(widget),
    )

  @overload(
      QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation,
  )
  @overload(
      QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation,
      QStyleOption,
  )
  @overload(
      QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation,
      NoneType,
  )
  @overload(
      QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation,
      QStyleOption, QWidget,
  )
  @overload(
      QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation,
      QStyleOption, NoneType,
  )
  @overload(
      QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation,
      NoneType, QWidget,
  )
  @overload(
      QSizePolicy.ControlTypes, QSizePolicy.ControlTypes, Qt.Orientation,
      NoneType, NoneType,
  )
  def combinedLayoutSpacing(
      self,
      controls1: QSizePolicy.ControlTypes,
      controls2: QSizePolicy.ControlTypes,
      orientation: Qt.Orientation,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyle::combinedLayoutSpacing(QSizePolicy::ControlTypes
    controls1, QSizePolicy::ControlTypes controls2, Qt::Orientation
    orientation, QStyleOption *option, QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#combinedLayoutSpacing

    Parameters
    ----------

    controls1 : QSizePolicy.ControlTypes
      Passed on as its number.

    controls2 : QSizePolicy.ControlTypes
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyle::combinedLayoutSpacing(QSizePolicy::ControlTypes controls1,
    #      QSizePolicy::ControlTypes controls2, Qt::Orientation orientation,
    #      QStyleOption *option, QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK6QStyle21combinedLayoutSpacingE6QFlagsIN11QSizePolicy11C'
        'ontrolTypeEES3_N2Qt11OrientationEP12QStyleOptionP7QWidget',
        controls1.value, controls2.value, orientation.value,
        self._addressOf(option), self._addressOf(widget),
    )

  def proxy(self) -> Optional[QStyle]:
    """
    Calls Qt's 'const QStyle *QStyle::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#proxy

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStyle *QStyle::proxy() const
    address = self.uglySide.call('ritual_ZNK6QStyle5proxyEv')
    return QStyle._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QStyle::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStyle::setName(const QString &name)
    self.uglySide.call('ritual_ZN6QStyle7setNameERK7QString', name)

  @overload(THIS)
  @overload(NoneType)
  def setProxy(self, style: Optional[QStyle]) -> None:
    """
    Calls Qt's 'void QStyle::setProxy(QStyle *style)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#setProxy

    Parameters
    ----------

    style : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::setProxy(QStyle *style)
    self.uglySide.call(
        'ritual_ZN6QStyle8setProxyEPS_', self._addressOf(style),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::polish(QWidget *widget)
    ritual = 'ritual_ZN6QStyle6polishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QStyle6polishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def polish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyle::polish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#polish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::polish(QApplication *application)
    ritual = 'ritual_ZN6QStyle6polishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QStyle6polishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(application))

  @overload(QWidget)
  @overload(NoneType)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::unpolish(QWidget *widget)
    ritual = 'ritual_ZN6QStyle8unpolishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QStyle8unpolishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def unpolish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyle::unpolish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#unpolish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::unpolish(QApplication *application)
    ritual = 'ritual_ZN6QStyle8unpolishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QStyle8unpolishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(application))

  @overload(QPainter, QRect, int, QPalette, bool, str)
  @overload(NoneType, QRect, int, QPalette, bool, str)
  @overload(QPainter, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  @overload(NoneType, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  def drawItemText(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      flags: int,
      pal: QPalette,
      enabled: bool,
      text: str,
      textRole: QPalette.ColorRole = QPalette.ColorRole.NoRole,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawItemText(QPainter *painter, const QRect
    &rect, int flags, const QPalette &pal, bool enabled, const QString &text,
    QPalette::ColorRole textRole) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawItemText

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    enabled : bool
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    textRole : QPalette.ColorRole
      Passed on as its number. May be left out, as in Qt: it is then
      QPalette.ColorRole.NoRole.
    """
    #  void QStyle::drawItemText(QPainter *painter, const QRect &rect, int
    #      flags, const QPalette &pal, bool enabled, const QString &text,
    #      QPalette::ColorRole textRole) const
    ritual = (
        'ritual_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7'
        'QStringNS5_9ColorRoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalet'
          'tebRK7QStringNS5_9ColorRoleE')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), flags,
        self._valueOf(pal), enabled, text, textRole.value,
    )

  @overload(QPainter, QRect, int, QPixmap)
  @overload(NoneType, QRect, int, QPixmap)
  def drawItemPixmap(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      alignment: int,
      pixmap: QPixmap,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawItemPixmap(QPainter *painter, const QRect
    &rect, int alignment, const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawItemPixmap

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    alignment : int
      Passed on as it is.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QStyle::drawItemPixmap(QPainter *painter, const QRect &rect, int
    #      alignment, const QPixmap &pixmap) const
    ritual = (
        'ritual_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPix'
          'map')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), alignment,
        self._valueOf(pixmap),
    )

  @overload(PrimitiveElement, QStyleOption, QPainter)
  @overload(PrimitiveElement, QStyleOption, NoneType)
  @overload(PrimitiveElement, NoneType, QPainter)
  @overload(PrimitiveElement, NoneType, NoneType)
  @overload(PrimitiveElement, QStyleOption, QPainter, QWidget)
  @overload(PrimitiveElement, QStyleOption, QPainter, NoneType)
  @overload(PrimitiveElement, QStyleOption, NoneType, QWidget)
  @overload(PrimitiveElement, QStyleOption, NoneType, NoneType)
  @overload(PrimitiveElement, NoneType, QPainter, QWidget)
  @overload(PrimitiveElement, NoneType, QPainter, NoneType)
  @overload(PrimitiveElement, NoneType, NoneType, QWidget)
  @overload(PrimitiveElement, NoneType, NoneType, NoneType)
  def drawPrimitive(
      self,
      pe: PrimitiveElement,
      opt: Optional[QStyleOption],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawPrimitive(PrimitiveElement pe, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawPrimitive

    Parameters
    ----------

    pe : PrimitiveElement
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
    #      *opt, QPainter *p, const QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleO'
        'ptionP8QPainterPK7QWidget',
        pe.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(ControlElement, QStyleOption, QPainter)
  @overload(ControlElement, QStyleOption, NoneType)
  @overload(ControlElement, NoneType, QPainter)
  @overload(ControlElement, NoneType, NoneType)
  @overload(ControlElement, QStyleOption, QPainter, QWidget)
  @overload(ControlElement, QStyleOption, QPainter, NoneType)
  @overload(ControlElement, QStyleOption, NoneType, QWidget)
  @overload(ControlElement, QStyleOption, NoneType, NoneType)
  @overload(ControlElement, NoneType, QPainter, QWidget)
  @overload(ControlElement, NoneType, QPainter, NoneType)
  @overload(ControlElement, NoneType, NoneType, QWidget)
  @overload(ControlElement, NoneType, NoneType, NoneType)
  def drawControl(
      self,
      element: ControlElement,
      opt: Optional[QStyleOption],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawControl(ControlElement element, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawControl

    Parameters
    ----------

    element : ControlElement
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QStyle::drawControl(ControlElement element, const QStyleOption
    #      *opt, QPainter *p, const QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptio'
        'nP8QPainterPK7QWidget',
        element.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(ComplexControl, QStyleOptionComplex, QPainter)
  @overload(ComplexControl, QStyleOptionComplex, NoneType)
  @overload(ComplexControl, NoneType, QPainter)
  @overload(ComplexControl, NoneType, NoneType)
  @overload(ComplexControl, QStyleOptionComplex, QPainter, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, QPainter, NoneType)
  @overload(ComplexControl, QStyleOptionComplex, NoneType, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, NoneType, NoneType)
  @overload(ComplexControl, NoneType, QPainter, QWidget)
  @overload(ComplexControl, NoneType, QPainter, NoneType)
  @overload(ComplexControl, NoneType, NoneType, QWidget)
  @overload(ComplexControl, NoneType, NoneType, NoneType)
  def drawComplexControl(
      self,
      cc: ComplexControl,
      opt: Optional[QStyleOptionComplex],
      p: Optional[QPainter],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawComplexControl(ComplexControl cc, const
    QStyleOptionComplex *opt, QPainter *p, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawComplexControl

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p, const QWidget *widget)
    #      const
    self.uglySide.call(
        'ritual_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QSty'
        'leOptionComplexP8QPainterPK7QWidget',
        cc.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(widget),
    )
