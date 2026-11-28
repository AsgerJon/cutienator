"""
QQC2::QStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyle_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyle to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QIcon, QPalette
from . import QQC2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMargins, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QFont, QFontMetrics, QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFontMetrics = WAIT['QFontMetrics']
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyle(QObject):
  """
  The cute side of Qt's QQC2::QStyle: a plain Python object standing in front
  of one C++ QQC2::QStyle.

  It is built on the cute 'QObject', as Qt's QQC2::QStyle is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQC2::QStyle that has a ritual and that Python can
  call so far, 30 names in all: 'metaObject', 'd_func', 'itemTextRect',
  'itemPixmapRect', 'subElementRect', 'subControlRect', 'sizeFromContents',
  'font', 'ninePatchMargins', 'hitTestComplexControl', 'pixelMetric',
  'styleHint', 'drawItemText', 'drawItemPixmap', 'drawPrimitive',
  'drawControl', 'drawComplexControl', 'standardPalette', 'standardPixmap',
  'standardIcon', 'generatedIconPixmap', 'polish', 'visualRect', 'visualPos',
  'sliderPositionFromValue', 'sliderValueFromPosition', 'visualAlignment',
  'alignedRect', 'proxy', 'handleThemeChange'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQC2::QStyle::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQC2::QStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QStylePrivate *QQC2::QStyle::d_func() const': takes in Python
    what 'QStylePrivate *QQC2::QStyle::d_func()' takes.
  - Qt's 'QQC2::QStyle::~QStyle()': the destructor: Python never removes a
    C++ QQC2::QStyle.

  What has no ritual
  ------------------

  7 of the 42 functions Qt declares: 3 leans on 'QQC2; 2 not a gap; 2
  forbidden.

  What to expect
  --------------

  - The C++ QQC2::QStyle is created at the first use, not by
    'QQC2::QStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQC2::QStyle.
  - Qt tells when it has removed the C++ QQC2::QStyle. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQC2::QStyle that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQC2::QStyle, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ComplexControl(CuteNum):
    """
    The enum 'QQC2::QStyle::ComplexControl' of Qt, with the 11 names Qt gives
    in it.
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
    CC_SearchField = Kee[int](9)
    CC_CustomBase = Kee[int](4026531840)

  class ContentsType(CuteNum):
    """
    The enum 'QQC2::QStyle::ContentsType' of Qt, with the 27 names Qt gives
    in it.
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
    CT_Dial = Kee[int](13)
    CT_ScrollBar = Kee[int](14)
    CT_LineEdit = Kee[int](15)
    CT_SpinBox = Kee[int](16)
    CT_SizeGrip = Kee[int](17)
    CT_SearchField = Kee[int](18)
    CT_TabWidget = Kee[int](19)
    CT_DialogButtons = Kee[int](20)
    CT_HeaderSection = Kee[int](21)
    CT_GroupBox = Kee[int](22)
    CT_MdiControls = Kee[int](23)
    CT_ItemViewItem = Kee[int](24)
    CT_Frame = Kee[int](25)
    CT_CustomBase = Kee[int](4026531840)

  class ControlElement(CuteNum):
    """
    The enum 'QQC2::QStyle::ControlElement' of Qt, with the 48 names Qt gives
    in it.
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
    The enum 'QQC2::QStyle::PixelMetric' of Qt, with the 108 names Qt gives
    in it.
    """

    PM_ButtonMargin = Kee[int](0)
    PM_ButtonDefaultIndicator = Kee[int](1)
    PM_MenuButtonIndicator = Kee[int](2)
    PM_ButtonShiftHorizontal = Kee[int](3)
    PM_ButtonShiftVertical = Kee[int](4)
    PM_DefaultFrameWidth = Kee[int](5)
    PM_SpinBoxFrameWidth = Kee[int](6)
    PM_ComboBoxFrameWidth = Kee[int](7)
    PM_SearchFieldFrameWidth = Kee[int](8)
    PM_MaximumDragDistance = Kee[int](9)
    PM_ScrollBarExtent = Kee[int](10)
    PM_ScrollBarSliderMin = Kee[int](11)
    PM_SliderThickness = Kee[int](12)
    PM_SliderControlThickness = Kee[int](13)
    PM_SliderLength = Kee[int](14)
    PM_SliderTickmarkOffset = Kee[int](15)
    PM_SliderSpaceAvailable = Kee[int](16)
    PM_DockWidgetSeparatorExtent = Kee[int](17)
    PM_DockWidgetHandleExtent = Kee[int](18)
    PM_DockWidgetFrameWidth = Kee[int](19)
    PM_TabBarTabOverlap = Kee[int](20)
    PM_TabBarTabHSpace = Kee[int](21)
    PM_TabBarTabVSpace = Kee[int](22)
    PM_TabBarBaseHeight = Kee[int](23)
    PM_TabBarBaseOverlap = Kee[int](24)
    PM_ProgressBarChunkWidth = Kee[int](25)
    PM_SplitterWidth = Kee[int](26)
    PM_TitleBarHeight = Kee[int](27)
    PM_MenuScrollerHeight = Kee[int](28)
    PM_MenuHMargin = Kee[int](29)
    PM_MenuVMargin = Kee[int](30)
    PM_MenuPanelWidth = Kee[int](31)
    PM_MenuTearoffHeight = Kee[int](32)
    PM_MenuDesktopFrameWidth = Kee[int](33)
    PM_MenuBarPanelWidth = Kee[int](34)
    PM_MenuBarItemSpacing = Kee[int](35)
    PM_MenuBarVMargin = Kee[int](36)
    PM_MenuBarHMargin = Kee[int](37)
    PM_IndicatorWidth = Kee[int](38)
    PM_IndicatorHeight = Kee[int](39)
    PM_ExclusiveIndicatorWidth = Kee[int](40)
    PM_ExclusiveIndicatorHeight = Kee[int](41)
    PM_DialogButtonsSeparator = Kee[int](42)
    PM_DialogButtonsButtonWidth = Kee[int](43)
    PM_DialogButtonsButtonHeight = Kee[int](44)
    PM_MdiSubWindowFrameWidth = Kee[int](45)
    PM_MdiSubWindowMinimizedWidth = Kee[int](46)
    PM_HeaderMargin = Kee[int](47)
    PM_HeaderMarkSize = Kee[int](48)
    PM_HeaderGripMargin = Kee[int](49)
    PM_TabBarTabShiftHorizontal = Kee[int](50)
    PM_TabBarTabShiftVertical = Kee[int](51)
    PM_TabBarScrollButtonWidth = Kee[int](52)
    PM_ToolBarFrameWidth = Kee[int](53)
    PM_ToolBarHandleExtent = Kee[int](54)
    PM_ToolBarItemSpacing = Kee[int](55)
    PM_ToolBarItemMargin = Kee[int](56)
    PM_ToolBarSeparatorExtent = Kee[int](57)
    PM_ToolBarExtensionExtent = Kee[int](58)
    PM_SpinBoxSliderHeight = Kee[int](59)
    PM_DefaultTopLevelMargin = Kee[int](60)
    PM_DefaultChildMargin = Kee[int](61)
    PM_DefaultLayoutSpacing = Kee[int](62)
    PM_ToolBarIconSize = Kee[int](63)
    PM_ListViewIconSize = Kee[int](64)
    PM_IconViewIconSize = Kee[int](65)
    PM_SmallIconSize = Kee[int](66)
    PM_LargeIconSize = Kee[int](67)
    PM_FocusFrameVMargin = Kee[int](68)
    PM_FocusFrameHMargin = Kee[int](69)
    PM_ToolTipLabelFrameWidth = Kee[int](70)
    PM_CheckBoxLabelSpacing = Kee[int](71)
    PM_TabBarIconSize = Kee[int](72)
    PM_SizeGripSize = Kee[int](73)
    PM_DockWidgetTitleMargin = Kee[int](74)
    PM_MessageBoxIconSize = Kee[int](75)
    PM_ButtonIconSize = Kee[int](76)
    PM_DockWidgetTitleBarButtonMargin = Kee[int](77)
    PM_RadioButtonLabelSpacing = Kee[int](78)
    PM_LayoutLeftMargin = Kee[int](79)
    PM_LayoutTopMargin = Kee[int](80)
    PM_LayoutRightMargin = Kee[int](81)
    PM_LayoutBottomMargin = Kee[int](82)
    PM_LayoutHorizontalSpacing = Kee[int](83)
    PM_LayoutVerticalSpacing = Kee[int](84)
    PM_TabBar_ScrollButtonOverlap = Kee[int](85)
    PM_TextCursorWidth = Kee[int](86)
    PM_TabCloseIndicatorWidth = Kee[int](87)
    PM_TabCloseIndicatorHeight = Kee[int](88)
    PM_ScrollView_ScrollBarSpacing = Kee[int](89)
    PM_ScrollView_ScrollBarOverlap = Kee[int](90)
    PM_SubMenuOverlap = Kee[int](91)
    PM_TreeViewIndentation = Kee[int](92)
    PM_HeaderDefaultSectionSizeHorizontal = Kee[int](93)
    PM_HeaderDefaultSectionSizeVertical = Kee[int](94)
    PM_TitleBarButtonIconSize = Kee[int](95)
    PM_TitleBarButtonSize = Kee[int](96)
    PM_PushButtonFocusFrameRadius = Kee[int](97)
    PM_CheckBoxFocusFrameRadius = Kee[int](98)
    PM_ComboBoxFocusFrameRadius = Kee[int](99)
    PM_DialFocusFrameRadius = Kee[int](100)
    PM_RadioButtonFocusFrameRadius = Kee[int](101)
    PM_SearchFieldFocusFrameRadius = Kee[int](102)
    PM_SliderFocusFrameRadius = Kee[int](103)
    PM_SpinBoxFocusFrameRadius = Kee[int](104)
    PM_TextAreaFocusFrameRadius = Kee[int](105)
    PM_TextFieldFocusFrameRadius = Kee[int](106)
    PM_CustomBase = Kee[int](4026531840)

  class PrimitiveElement(CuteNum):
    """
    The enum 'QQC2::QStyle::PrimitiveElement' of Qt, with the 52 names Qt
    gives in it.
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
    The enum 'QQC2::QStyle::RequestSoftwareInputPanel' of Qt, with the 2
    names Qt gives in it.
    """

    RSIP_OnMouseClickAndAlreadyFocused = Kee[int](0)
    RSIP_OnMouseClick = Kee[int](1)

  class StandardPixmap(CuteNum):
    """
    The enum 'QQC2::QStyle::StandardPixmap' of Qt, with the 79 names Qt gives
    in it.
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
    SP_CustomBase = Kee[int](4026531840)

  class StateFlag(CuteFlags):
    """
    The flags enum 'QQC2::QStyle::StateFlag' of Qt, with the 28 names Qt
    gives in it. Qt names the type of its combinations 'QQC2::QStyle::State'.
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
    The enum 'QQC2::QStyle::StyleHint' of Qt, with the 119 names Qt gives in
    it.
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
    SH_SpellCheckUnderlineStyle = Kee[int](72)
    SH_MessageBox_CenterButtons = Kee[int](73)
    SH_Menu_SelectionWrap = Kee[int](74)
    SH_ItemView_MovementWithoutUpdatingSelection = Kee[int](75)
    SH_ToolTip_Mask = Kee[int](76)
    SH_FocusFrame_AboveWidget = Kee[int](77)
    SH_TextControl_FocusIndicatorTextCharFormat = Kee[int](78)
    SH_WizardStyle = Kee[int](79)
    SH_ItemView_ArrowKeysNavigateIntoChildren = Kee[int](80)
    SH_Menu_Mask = Kee[int](81)
    SH_Menu_FlashTriggeredItem = Kee[int](82)
    SH_Menu_FadeOutOnHide = Kee[int](83)
    SH_SpinBox_ClickAutoRepeatThreshold = Kee[int](84)
    SH_ItemView_PaintAlternatingRowColorsForEmptyArea = Kee[int](85)
    SH_FormLayoutWrapPolicy = Kee[int](86)
    SH_TabWidget_DefaultTabPosition = Kee[int](87)
    SH_ToolBar_Movable = Kee[int](88)
    SH_FormLayoutFieldGrowthPolicy = Kee[int](89)
    SH_FormLayoutFormAlignment = Kee[int](90)
    SH_FormLayoutLabelAlignment = Kee[int](91)
    SH_ItemView_DrawDelegateFrame = Kee[int](92)
    SH_TabBar_CloseButtonPosition = Kee[int](93)
    SH_DockWidget_ButtonsHaveFrame = Kee[int](94)
    SH_ToolButtonStyle = Kee[int](95)
    SH_RequestSoftwareInputPanel = Kee[int](96)
    SH_ScrollBar_Transient = Kee[int](97)
    SH_Menu_SupportsSections = Kee[int](98)
    SH_ToolTip_WakeUpDelay = Kee[int](99)
    SH_ToolTip_FallAsleepDelay = Kee[int](100)
    SH_Widget_Animate = Kee[int](101)
    SH_Splitter_OpaqueResize = Kee[int](102)
    SH_ComboBox_UseNativePopup = Kee[int](103)
    SH_LineEdit_PasswordMaskDelay = Kee[int](104)
    SH_TabBar_ChangeCurrentDelay = Kee[int](105)
    SH_Menu_SubMenuUniDirection = Kee[int](106)
    SH_Menu_SubMenuUniDirectionFailCount = Kee[int](107)
    SH_Menu_SubMenuSloppySelectOtherActions = Kee[int](108)
    SH_Menu_SubMenuSloppyCloseTimeout = Kee[int](109)
    SH_Menu_SubMenuResetWhenReenteringParent = Kee[int](110)
    SH_Menu_SubMenuDontStartSloppyOnLeave = Kee[int](111)
    SH_ItemView_ScrollMode = Kee[int](112)
    SH_TitleBar_ShowToolTipsOnButtons = Kee[int](113)
    SH_Widget_Animation_Duration = Kee[int](114)
    SH_ComboBox_AllowWheelScrolling = Kee[int](115)
    SH_SpinBox_ButtonsInsideFrame = Kee[int](116)
    SH_SpinBox_StepModifier = Kee[int](117)
    SH_CustomBase = Kee[int](4026531840)

  class SubControl(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QQC2::QStyle::SubControl' of Qt, with the 48 names Qt
    gives in it. Qt names the type of its combinations
    'QQC2::QStyle::SubControls'.
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
    SC_SearchFieldSearch = 0x1
    SC_SearchFieldClear = 0x2
    SC_SearchFieldFrame = 0x4
    SC_SearchFieldEditField = 0x8
    SC_SearchFieldPopup = 0x10
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
    The enum 'QQC2::QStyle::SubElement' of Qt, with the 60 names Qt gives in
    it.
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
    SE_ScrollBarLayoutItem = Kee[int](40)
    SE_SpinBoxLayoutItem = Kee[int](41)
    SE_ToolButtonLayoutItem = Kee[int](42)
    SE_SearchFieldLayoutItem = Kee[int](43)
    SE_FrameLayoutItem = Kee[int](44)
    SE_GroupBoxLayoutItem = Kee[int](45)
    SE_TabWidgetLayoutItem = Kee[int](46)
    SE_ItemViewItemDecoration = Kee[int](47)
    SE_ItemViewItemText = Kee[int](48)
    SE_ItemViewItemFocusRect = Kee[int](49)
    SE_TabBarTabLeftButton = Kee[int](50)
    SE_TabBarTabRightButton = Kee[int](51)
    SE_TabBarTabText = Kee[int](52)
    SE_ShapedFrameContents = Kee[int](53)
    SE_ToolBarHandle = Kee[int](54)
    SE_TabBarScrollLeftButton = Kee[int](55)
    SE_TabBarScrollRightButton = Kee[int](56)
    SE_TabBarTearIndicatorRight = Kee[int](57)
    SE_CustomBase = Kee[int](4026531840)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Qt.LayoutDirection, QRect, QRect)
  def visualRect(
      direction: Qt.LayoutDirection,
      boundingRect: QRect,
      logicalRect: QRect,
  ) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QStyle::visualRect(Qt::LayoutDirection direction,
    const QRect &boundingRect, const QRect &logicalRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#visualRect

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
    #  QRect QQC2::QStyle::visualRect(Qt::LayoutDirection direction, const
    #      QRect &boundingRect, const QRect &logicalRect)
    address = Rituals.call(
        'ritual_ZN4QQC26QStyle10visualRectEN2Qt15LayoutDirectionERK5QRectS5'
        '_',
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
    Calls Qt's 'QPoint QQC2::QStyle::visualPos(Qt::LayoutDirection direction,
    const QRect &boundingRect, const QPoint &logicalPos)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#visualPos

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
    #  QPoint QQC2::QStyle::visualPos(Qt::LayoutDirection direction, const
    #      QRect &boundingRect, const QPoint &logicalPos)
    address = Rituals.call(
        'ritual_ZN4QQC26QStyle9visualPosEN2Qt15LayoutDirectionERK5QRectRK6Q'
        'Point',
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
    Calls Qt's 'int QQC2::QStyle::sliderPositionFromValue(int min, int max,
    int val, int space, bool upsideDown)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyle.html#sliderPositionFromValue

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
    #  int QQC2::QStyle::sliderPositionFromValue(int min, int max, int val,
    #      int space, bool upsideDown)
    return Rituals.call(
        'ritual_ZN4QQC26QStyle23sliderPositionFromValueEiiiib',
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
    Calls Qt's 'int QQC2::QStyle::sliderValueFromPosition(int min, int max,
    int pos, int space, bool upsideDown)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyle.html#sliderValueFromPosition

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
    #  int QQC2::QStyle::sliderValueFromPosition(int min, int max, int pos,
    #      int space, bool upsideDown)
    return Rituals.call(
        'ritual_ZN4QQC26QStyle23sliderValueFromPositionEiiiib',
        min, max, pos, space, upsideDown,
    )

  @staticmethod
  @overload(Qt.LayoutDirection, Qt.Alignment)
  def visualAlignment(
      direction: Qt.LayoutDirection,
      alignment: Qt.Alignment,
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment
    QQC2::QStyle::visualAlignment(Qt::LayoutDirection direction,
    Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#visualAlignment

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
    #  Qt::Alignment QQC2::QStyle::visualAlignment(Qt::LayoutDirection
    #      direction, Qt::Alignment alignment)
    return Qt.Alignment(Rituals.call(
        'ritual_ZN4QQC26QStyle15visualAlignmentEN2Qt15LayoutDirectionE6QFla'
        'gsINS1_13AlignmentFlagEE',
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
    Calls Qt's 'QRect QQC2::QStyle::alignedRect(Qt::LayoutDirection
    direction, Qt::Alignment alignment, const QSize &size, const QRect
    &rectangle)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#alignedRect

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
    #  QRect QQC2::QStyle::alignedRect(Qt::LayoutDirection direction,
    #      Qt::Alignment alignment, const QSize &size, const QRect
    #      &rectangle)
    address = Rituals.call(
        'ritual_ZN4QQC26QStyle11alignedRectEN2Qt15LayoutDirectionE6QFlagsIN'
        'S1_13AlignmentFlagEERK5QSizeRK5QRect',
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
  __qt_class__ = 'QQC2::QStyle'

  #  A C++ QQC2::QStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQC2_QStyle'

  #  The functions Qt calls itself that QQC2::QStyle is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'itemTextRect': (
          ('_ZNK4QQC26QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QSt'
           'ring',
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
          ('_ZNK4QQC26QStyle14itemPixmapRectERK5QRectiRK7QPixmap',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QPixmap'),
           )),
      ),
      'subElementRect': (
          ('_ZNK4QQC26QStyle14subElementRectENS0_10SubElementEPKNS_12QStyle'
           'OptionE',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtQuickNativeStyle:QQC2.QStyle.SubElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'subControlRect': (
          ('_ZNK4QQC26QStyle14subControlRectENS0_14ComplexControlEPKNS_19QS'
           'tyleOptionComplexENS0_10SubControlE',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('int', 'enum', 'QtQuickNativeStyle:QQC2.QStyle.SubControl'),
           )),
      ),
      'sizeFromContents': (
          ('_ZNK4QQC26QStyle16sizeFromContentsENS0_12ContentsTypeEPKNS_12QS'
           'tyleOptionERK5QSize',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ContentsType'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'font': (
          ('_ZNK4QQC26QStyle4fontENS0_14ControlElementE6QFlagsINS0_9StateFl'
           'agEE',
           ('address', 'value', 'QtGui:QFont'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ControlElement'),
               ('int', 'flags', 'QtQuickNativeStyle:QQC2.QStyle.StateFlag'),
           )),
      ),
      'ninePatchMargins': (
          ('_ZNK4QQC26QStyle16ninePatchMarginsENS0_14ControlElementEPKNS_12'
           'QStyleOptionERK5QSize',
           ('address', 'value', 'QtCore:QMargins'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ControlElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'value', 'QtCore:QSize'),
           )),
          ('_ZNK4QQC26QStyle16ninePatchMarginsENS0_14ComplexControlEPKNS_19'
           'QStyleOptionComplexERK5QSize',
           ('address', 'value', 'QtCore:QMargins'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'hitTestComplexControl': (
          ('_ZNK4QQC26QStyle21hitTestComplexControlENS0_14ComplexControlEPK'
           'NS_19QStyleOptionComplexERK6QPoint',
           ('int', 'enum', 'QtQuickNativeStyle:QQC2.QStyle.SubControl'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'pixelMetric': (
          ('_ZNK4QQC26QStyle11pixelMetricENS0_11PixelMetricEPKNS_12QStyleOp'
           'tionE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtQuickNativeStyle:QQC2.QStyle.PixelMetric'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'styleHint': (
          ('_ZNK4QQC26QStyle9styleHintENS0_9StyleHintEPKNS_12QStyleOptionEP'
           'NS_16QStyleHintReturnE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtQuickNativeStyle:QQC2.QStyle.StyleHint'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleHintReturn'),
           )),
      ),
      'drawItemText': (
          ('_ZNK4QQC26QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebR'
           'K7QStringNS6_9ColorRoleE',
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
          ('_ZNK4QQC26QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QPixmap'),
           )),
      ),
      'drawPrimitive': (
          ('_ZNK4QQC26QStyle13drawPrimitiveENS0_16PrimitiveElementEPKNS_12Q'
           'StyleOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.PrimitiveElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'drawControl': (
          ('_ZNK4QQC26QStyle11drawControlENS0_14ControlElementEPKNS_12QStyl'
           'eOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ControlElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'drawComplexControl': (
          ('_ZNK4QQC26QStyle18drawComplexControlENS0_14ComplexControlEPKNS_'
           '19QStyleOptionComplexEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'standardPalette': (
          ('_ZNK4QQC26QStyle15standardPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
      'standardPixmap': (
          ('_ZNK4QQC26QStyle14standardPixmapENS0_14StandardPixmapEPKNS_12QS'
           'tyleOptionE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'standardIcon': (
          ('_ZNK4QQC26QStyle12standardIconENS0_14StandardPixmapEPKNS_12QSty'
           'leOptionE',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'generatedIconPixmap': (
          ('_ZNK4QQC26QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK'
           'NS_12QStyleOptionE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('address', 'value', 'QtGui:QPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'polish': (
          ('_ZN4QQC26QStyle6polishEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleThemeChange': (
          ('_ZN4QQC26QStyle17handleThemeChangeEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QQC2::QStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQC2::QStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK4QQC26QStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Calls Qt's 'QRect QQC2::QStyle::itemTextRect(const QFontMetrics &fm,
    const QRect &r, int flags, bool enabled, const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#itemTextRect

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
    #  QRect QQC2::QStyle::itemTextRect(const QFontMetrics &fm, const QRect
    #      &r, int flags, bool enabled, const QString &text) const
    ritual = (
        'ritual_ZNK4QQC26QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7'
        'QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC26QStyle12itemTextRectERK12QFontMetricsRK5QRec'
          'tibRK7QString')
    address = self.uglySide.call(
        ritual, self._valueOf(fm), self._valueOf(r), flags, enabled, text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect, int, QPixmap)
  def itemPixmapRect(self, r: QRect, flags: int, pixmap: QPixmap) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QStyle::itemPixmapRect(const QRect &r, int flags,
    const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#itemPixmapRect

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
    #  QRect QQC2::QStyle::itemPixmapRect(const QRect &r, int flags, const
    #      QPixmap &pixmap) const
    ritual = 'ritual_ZNK4QQC26QStyle14itemPixmapRectERK5QRectiRK7QPixmap'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC26QStyle14itemPixmapRectERK5QRectiRK7QPixmap')
    address = self.uglySide.call(
        ritual, self._valueOf(r), flags, self._valueOf(pixmap),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(SubElement, WAIT['QQC2.QStyleOption'])
  @overload(SubElement, NoneType)
  def subElementRect(
      self,
      subElement: SubElement,
      option: Optional[QQC2.QStyleOption],
  ) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QStyle::subElementRect(SubElement subElement,
    const QStyleOption *option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#subElementRect

    Parameters
    ----------

    subElement : SubElement
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQC2::QStyle::subElementRect(SubElement subElement, const
    #      QStyleOption *option) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle14subElementRectENS0_10SubElementEPKNS_12QSt'
        'yleOptionE',
        subElement.value, self._addressOf(option),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(ComplexControl, WAIT['QQC2.QStyleOptionComplex'], SubControl)
  @overload(ComplexControl, NoneType, SubControl)
  def subControlRect(
      self,
      cc: ComplexControl,
      opt: Optional[QQC2.QStyleOptionComplex],
      sc: SubControl,
  ) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *opt, SubControl sc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#subControlRect

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : SubControl
      Passed on as its number.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQC2::QStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle14subControlRectENS0_14ComplexControlEPKNS_1'
        '9QStyleOptionComplexENS0_10SubControlE',
        cc.value, self._addressOf(opt), sc.value,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(ContentsType, WAIT['QQC2.QStyleOption'], QSize)
  @overload(ContentsType, NoneType, QSize)
  def sizeFromContents(
      self,
      ct: ContentsType,
      opt: Optional[QQC2.QStyleOption],
      contentsSize: QSize,
  ) -> QSize:
    """
    Calls Qt's 'QSize QQC2::QStyle::sizeFromContents(ContentsType ct, const
    QStyleOption *opt, const QSize &contentsSize) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#sizeFromContents

    Parameters
    ----------

    ct : ContentsType
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQC2::QStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *opt, const QSize &contentsSize) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle16sizeFromContentsENS0_12ContentsTypeEPKNS_1'
        '2QStyleOptionERK5QSize',
        ct.value, self._addressOf(opt), self._valueOf(contentsSize),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(ControlElement, State)
  def font(self, element: ControlElement, state: State) -> QFont:
    """
    Calls Qt's 'QFont QQC2::QStyle::font(ControlElement element, const
    QStyle::State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#font

    Parameters
    ----------

    element : ControlElement
      Passed on as its number.

    state : State
      Passed on as its number.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQC2::QStyle::font(ControlElement element, const QStyle::State
    #      state) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle4fontENS0_14ControlElementE6QFlagsINS0_9Stat'
        'eFlagEE',
        element.value, state.value,
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @overload(ControlElement, WAIT['QQC2.QStyleOption'], QSize)
  @overload(ControlElement, NoneType, QSize)
  def ninePatchMargins(
      self,
      ce: ControlElement,
      opt: Optional[QQC2.QStyleOption],
      imageSize: QSize,
  ) -> QMargins:
    """
    Calls Qt's 'QMargins QQC2::QStyle::ninePatchMargins(ControlElement ce,
    const QStyleOption *opt, const QSize &imageSize) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#ninePatchMargins

    Parameters
    ----------

    ce : ControlElement
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QQC2::QStyle::ninePatchMargins(ControlElement ce, const
    #      QStyleOption *opt, const QSize &imageSize) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle16ninePatchMarginsENS0_14ControlElementEPKNS'
        '_12QStyleOptionERK5QSize',
        ce.value, self._addressOf(opt), self._valueOf(imageSize),
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  @overload(ComplexControl, WAIT['QQC2.QStyleOptionComplex'], QSize)
  @overload(ComplexControl, NoneType, QSize)
  def ninePatchMargins(
      self,
      cc: ComplexControl,
      opt: Optional[QQC2.QStyleOptionComplex],
      imageSize: QSize,
  ) -> QMargins:
    """
    Calls Qt's 'QMargins QQC2::QStyle::ninePatchMargins(ComplexControl cc,
    const QStyleOptionComplex *opt, const QSize &imageSize) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#ninePatchMargins

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QQC2::QStyle::ninePatchMargins(ComplexControl cc, const
    #      QStyleOptionComplex *opt, const QSize &imageSize) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle16ninePatchMarginsENS0_14ComplexControlEPKNS'
        '_19QStyleOptionComplexERK5QSize',
        cc.value, self._addressOf(opt), self._valueOf(imageSize),
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  @overload(ComplexControl, WAIT['QQC2.QStyleOptionComplex'], QPoint)
  @overload(ComplexControl, NoneType, QPoint)
  def hitTestComplexControl(
      self,
      cc: ComplexControl,
      opt: Optional[QQC2.QStyleOptionComplex],
      pt: QPoint,
  ) -> SubControl:
    """
    Calls Qt's 'SubControl QQC2::QStyle::hitTestComplexControl(ComplexControl
    cc, const QStyleOptionComplex *opt, const QPoint &pt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyle.html#hitTestComplexControl

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SubControl(number)'
      gives.
    """
    #  SubControl QQC2::QStyle::hitTestComplexControl(ComplexControl cc,
    #      const QStyleOptionComplex *opt, const QPoint &pt) const
    return QStyle.SubControl(self.uglySide.call(
        'ritual_ZNK4QQC26QStyle21hitTestComplexControlENS0_14ComplexControl'
        'EPKNS_19QStyleOptionComplexERK6QPoint',
        cc.value, self._addressOf(opt), self._valueOf(pt),
    ))

  @overload(PixelMetric)
  @overload(PixelMetric, WAIT['QQC2.QStyleOption'])
  @overload(PixelMetric, NoneType)
  def pixelMetric(
      self,
      metric: PixelMetric,
      option: Optional[QQC2.QStyleOption] = None,
  ) -> int:
    """
    Calls Qt's 'int QQC2::QStyle::pixelMetric(PixelMetric metric, const
    QStyleOption *option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#pixelMetric

    Parameters
    ----------

    metric : PixelMetric
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QStyle::pixelMetric(PixelMetric metric, const QStyleOption
    #      *option) const
    return self.uglySide.call(
        'ritual_ZNK4QQC26QStyle11pixelMetricENS0_11PixelMetricEPKNS_12QStyl'
        'eOptionE',
        metric.value, self._addressOf(option),
    )

  @overload(StyleHint)
  @overload(StyleHint, WAIT['QQC2.QStyleOption'])
  @overload(StyleHint, NoneType)
  @overload(
      StyleHint, WAIT['QQC2.QStyleOption'], WAIT['QQC2.QStyleHintReturn'],
  )
  @overload(StyleHint, WAIT['QQC2.QStyleOption'], NoneType)
  @overload(StyleHint, NoneType, WAIT['QQC2.QStyleHintReturn'])
  @overload(StyleHint, NoneType, NoneType)
  def styleHint(
      self,
      stylehint: StyleHint,
      opt: Optional[QQC2.QStyleOption] = None,
      returnData: Optional[QQC2.QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QQC2::QStyle::styleHint(StyleHint stylehint, const
    QStyleOption *opt, QStyleHintReturn *returnData) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#styleHint

    Parameters
    ----------

    stylehint : StyleHint
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    returnData : Optional[QQC2.QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QStyle::styleHint(StyleHint stylehint, const QStyleOption
    #      *opt, QStyleHintReturn *returnData) const
    return self.uglySide.call(
        'ritual_ZNK4QQC26QStyle9styleHintENS0_9StyleHintEPKNS_12QStyleOptio'
        'nEPNS_16QStyleHintReturnE',
        stylehint.value, self._addressOf(opt), self._addressOf(returnData),
    )

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQC2::QStyle::standardPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQC2::QStyle::standardPalette() const
    ritual = 'ritual_ZNK4QQC26QStyle15standardPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK4QQC26QStyle15standardPaletteEv'
    address = self.uglySide.call(ritual)
    return QPalette._cuteOwning(address)

  @overload(StandardPixmap)
  @overload(StandardPixmap, WAIT['QQC2.QStyleOption'])
  @overload(StandardPixmap, NoneType)
  def standardPixmap(
      self,
      standardPixmap: StandardPixmap,
      opt: Optional[QQC2.QStyleOption] = None,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQC2::QStyle::standardPixmap(StandardPixmap
    standardPixmap, const QStyleOption *opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#standardPixmap

    Parameters
    ----------

    standardPixmap : StandardPixmap
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQC2::QStyle::standardPixmap(StandardPixmap standardPixmap,
    #      const QStyleOption *opt) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle14standardPixmapENS0_14StandardPixmapEPKNS_1'
        '2QStyleOptionE',
        standardPixmap.value, self._addressOf(opt),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(StandardPixmap)
  @overload(StandardPixmap, WAIT['QQC2.QStyleOption'])
  @overload(StandardPixmap, NoneType)
  def standardIcon(
      self,
      standardIcon: StandardPixmap,
      option: Optional[QQC2.QStyleOption] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QQC2::QStyle::standardIcon(StandardPixmap standardIcon,
    const QStyleOption *option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#standardIcon

    Parameters
    ----------

    standardIcon : StandardPixmap
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QQC2::QStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *option) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle12standardIconENS0_14StandardPixmapEPKNS_12Q'
        'StyleOptionE',
        standardIcon.value, self._addressOf(option),
    )
    return QIcon._cuteOwning(address)

  @overload(QIcon.Mode, QPixmap, WAIT['QQC2.QStyleOption'])
  @overload(QIcon.Mode, QPixmap, NoneType)
  def generatedIconPixmap(
      self,
      iconMode: QIcon.Mode,
      pixmap: QPixmap,
      opt: Optional[QQC2.QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQC2::QStyle::generatedIconPixmap(QIcon::Mode
    iconMode, const QPixmap &pixmap, const QStyleOption *opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyle.html#generatedIconPixmap

    Parameters
    ----------

    iconMode : QIcon.Mode
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQC2::QStyle::generatedIconPixmap(QIcon::Mode iconMode, const
    #      QPixmap &pixmap, const QStyleOption *opt) const
    address = self.uglySide.call(
        'ritual_ZNK4QQC26QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixma'
        'pPKNS_12QStyleOptionE',
        iconMode.value, self._valueOf(pixmap), self._addressOf(opt),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def proxy(self) -> Optional[QStyle]:
    """
    Calls Qt's 'const QStyle *QQC2::QStyle::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#proxy

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStyle *QQC2::QStyle::proxy() const
    address = self.uglySide.call('ritual_ZNK4QQC26QStyle5proxyEv')
    return QStyle._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQC2::QStyle::QStyle(QStylePrivate &dd)': leans on
      'QQC2::QStyle::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'QQC2::QStyle::QStyle()': leans on
      'QQC2::QStyle::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QQC2.QStyle.__init__' has no cute function yet. Qt's "
        "'QQC2::QStyle::QStyle(QStylePrivate &dd)': leans on "
        "'QQC2::QStyle::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'QQC2::QStyle::QStyle()': leans on "
        "'QQC2::QStyle::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def d_func(self) -> Optional[QQC2.QStylePrivate]:
    """
    Calls Qt's 'QStylePrivate *QQC2::QStyle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#d_func

    Returns
    -------

    Optional[QQC2.QStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStylePrivate *QQC2::QStyle::d_func()
    address = self.uglySide.call('ritual_ZN4QQC26QStyle6d_funcEv')
    return QQC2.QStylePrivate._cuteAt(address)

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
    Calls Qt's 'void QQC2::QStyle::drawItemText(QPainter *painter, const
    QRect &rect, int flags, const QPalette &pal, bool enabled, const QString
    &text, QPalette::ColorRole textRole) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#drawItemText

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
    #  void QQC2::QStyle::drawItemText(QPainter *painter, const QRect &rect,
    #      int flags, const QPalette &pal, bool enabled, const QString &text,
    #      QPalette::ColorRole textRole) const
    ritual = (
        'ritual_ZNK4QQC26QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalett'
        'ebRK7QStringNS6_9ColorRoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC26QStyle12drawItemTextEP8QPainterRK5QRectiRK8Q'
          'PalettebRK7QStringNS6_9ColorRoleE')
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
    Calls Qt's 'void QQC2::QStyle::drawItemPixmap(QPainter *painter, const
    QRect &rect, int alignment, const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#drawItemPixmap

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
    #  void QQC2::QStyle::drawItemPixmap(QPainter *painter, const QRect
    #      &rect, int alignment, const QPixmap &pixmap) const
    ritual = (
        'ritual_ZNK4QQC26QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixm'
        'ap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC26QStyle14drawItemPixmapEP8QPainterRK5QRectiRK'
          '7QPixmap')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), alignment,
        self._valueOf(pixmap),
    )

  @overload(PrimitiveElement, WAIT['QQC2.QStyleOption'], QPainter)
  @overload(PrimitiveElement, WAIT['QQC2.QStyleOption'], NoneType)
  @overload(PrimitiveElement, NoneType, QPainter)
  @overload(PrimitiveElement, NoneType, NoneType)
  def drawPrimitive(
      self,
      pe: PrimitiveElement,
      opt: Optional[QQC2.QStyleOption],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QStyle::drawPrimitive(PrimitiveElement pe, const
    QStyleOption *opt, QPainter *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#drawPrimitive

    Parameters
    ----------

    pe : PrimitiveElement
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *opt, QPainter *p) const
    self.uglySide.call(
        'ritual_ZNK4QQC26QStyle13drawPrimitiveENS0_16PrimitiveElementEPKNS_'
        '12QStyleOptionEP8QPainter',
        pe.value, self._addressOf(opt), self._addressOf(p),
    )

  @overload(ControlElement, WAIT['QQC2.QStyleOption'], QPainter)
  @overload(ControlElement, WAIT['QQC2.QStyleOption'], NoneType)
  @overload(ControlElement, NoneType, QPainter)
  @overload(ControlElement, NoneType, NoneType)
  def drawControl(
      self,
      element: ControlElement,
      opt: Optional[QQC2.QStyleOption],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QStyle::drawControl(ControlElement element, const
    QStyleOption *opt, QPainter *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#drawControl

    Parameters
    ----------

    element : ControlElement
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QStyle::drawControl(ControlElement element, const
    #      QStyleOption *opt, QPainter *p) const
    self.uglySide.call(
        'ritual_ZNK4QQC26QStyle11drawControlENS0_14ControlElementEPKNS_12QS'
        'tyleOptionEP8QPainter',
        element.value, self._addressOf(opt), self._addressOf(p),
    )

  @overload(ComplexControl, WAIT['QQC2.QStyleOptionComplex'], QPainter)
  @overload(ComplexControl, WAIT['QQC2.QStyleOptionComplex'], NoneType)
  @overload(ComplexControl, NoneType, QPainter)
  @overload(ComplexControl, NoneType, NoneType)
  def drawComplexControl(
      self,
      cc: ComplexControl,
      opt: Optional[QQC2.QStyleOptionComplex],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QStyle::drawComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyle.html#drawComplexControl

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p) const
    self.uglySide.call(
        'ritual_ZNK4QQC26QStyle18drawComplexControlENS0_14ComplexControlEPK'
        'NS_19QStyleOptionComplexEP8QPainter',
        cc.value, self._addressOf(opt), self._addressOf(p),
    )

  def polish(self) -> None:
    """
    Calls Qt's 'void QQC2::QStyle::polish()'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#polish
    """
    #  void QQC2::QStyle::polish()
    ritual = 'ritual_ZN4QQC26QStyle6polishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN4QQC26QStyle6polishEv'
    self.uglySide.call(ritual)

  def handleThemeChange(self) -> None:
    """
    Calls Qt's 'void QQC2::QStyle::handleThemeChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qstyle.html#handleThemeChange
    """
    #  void QQC2::QStyle::handleThemeChange()
    ritual = 'ritual_ZN4QQC26QStyle17handleThemeChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN4QQC26QStyle17handleThemeChangeEv'
    self.uglySide.call(ritual)
