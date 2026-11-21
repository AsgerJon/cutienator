"""
Qt stands for the namespace 'Qt' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class Qt:
  """
  The namespace 'Qt' of Qt, which holds no objects. It holds the 95 enums Qt
  writes in it, each under its name, and the 24 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AlignmentFlag(CuteFlags):
    """
    The flags enum 'Qt::AlignmentFlag' of Qt, with the 14 names Qt gives in
    it. Qt names the type of its combinations 'Qt::Alignment'.
    """

    AlignLeft = 0x1
    AlignLeading = 0x1
    AlignRight = 0x2
    AlignTrailing = 0x2
    AlignHCenter = 0x4
    AlignJustify = 0x8
    AlignAbsolute = 0x10
    AlignHorizontal_Mask = 0x1f
    AlignTop = 0x20
    AlignBottom = 0x40
    AlignVCenter = 0x80
    AlignBaseline = 0x100
    AlignVertical_Mask = 0x1e0
    AlignCenter = 0x84

  Alignment = AlignmentFlag

  class AnchorPoint(CuteNum):
    """The enum 'Qt::AnchorPoint' of Qt, with the 6 names Qt gives in it."""

    AnchorLeft = Kee[int](0)
    AnchorHorizontalCenter = Kee[int](1)
    AnchorRight = Kee[int](2)
    AnchorTop = Kee[int](3)
    AnchorVerticalCenter = Kee[int](4)
    AnchorBottom = Kee[int](5)

  class ApplicationAttribute(CuteNum):
    """
    The enum 'Qt::ApplicationAttribute' of Qt, with the 31 names Qt gives in
    it.
    """

    AA_QtQuickUseDefaultSizePolicy = Kee[int](1)
    AA_DontShowIconsInMenus = Kee[int](2)
    AA_NativeWindows = Kee[int](3)
    AA_DontCreateNativeWidgetSiblings = Kee[int](4)
    AA_PluginApplication = Kee[int](5)
    AA_DontUseNativeMenuBar = Kee[int](6)
    AA_MacDontSwapCtrlAndMeta = Kee[int](7)
    AA_Use96Dpi = Kee[int](8)
    AA_DisableNativeVirtualKeyboard = Kee[int](9)
    AA_DontUseNativeMenuWindows = Kee[int](10)
    AA_SynthesizeTouchForUnhandledMouseEvents = Kee[int](11)
    AA_SynthesizeMouseForUnhandledTouchEvents = Kee[int](12)
    AA_UseHighDpiPixmaps = Kee[int](13)
    AA_ForceRasterWidgets = Kee[int](14)
    AA_UseDesktopOpenGL = Kee[int](15)
    AA_UseOpenGLES = Kee[int](16)
    AA_UseSoftwareOpenGL = Kee[int](17)
    AA_ShareOpenGLContexts = Kee[int](18)
    AA_SetPalette = Kee[int](19)
    AA_EnableHighDpiScaling = Kee[int](20)
    AA_DisableHighDpiScaling = Kee[int](21)
    AA_UseStyleSheetPropagationInWidgetStyles = Kee[int](22)
    AA_DontUseNativeDialogs = Kee[int](23)
    AA_SynthesizeMouseForUnhandledTabletEvents = Kee[int](24)
    AA_CompressHighFrequencyEvents = Kee[int](25)
    AA_DontCheckOpenGLContextThreadAffinity = Kee[int](26)
    AA_DisableShaderDiskCache = Kee[int](27)
    AA_DontShowShortcutsInContextMenus = Kee[int](28)
    AA_CompressTabletEvents = Kee[int](29)
    AA_DisableSessionManager = Kee[int](31)
    AA_AttributeCount = Kee[int](32)

  class ApplicationState(CuteFlags):
    """
    The flags enum 'Qt::ApplicationState' of Qt, with the 4 names Qt gives in
    it. Qt names the type of its combinations 'Qt::ApplicationStates'.
    """

    ApplicationSuspended = 0x0
    ApplicationHidden = 0x1
    ApplicationInactive = 0x2
    ApplicationActive = 0x4

  ApplicationStates = ApplicationState

  class ArrowType(CuteNum):
    """The enum 'Qt::ArrowType' of Qt, with the 5 names Qt gives in it."""

    NoArrow = Kee[int](0)
    UpArrow = Kee[int](1)
    DownArrow = Kee[int](2)
    LeftArrow = Kee[int](3)
    RightArrow = Kee[int](4)

  class AspectRatioMode(CuteNum):
    """
    The enum 'Qt::AspectRatioMode' of Qt, with the 3 names Qt gives in it.
    """

    IgnoreAspectRatio = Kee[int](0)
    KeepAspectRatio = Kee[int](1)
    KeepAspectRatioByExpanding = Kee[int](2)

  class Axis(CuteNum):
    """The enum 'Qt::Axis' of Qt, with the 3 names Qt gives in it."""

    XAxis = Kee[int](0)
    YAxis = Kee[int](1)
    ZAxis = Kee[int](2)

  class BGMode(CuteNum):
    """The enum 'Qt::BGMode' of Qt, with the 2 names Qt gives in it."""

    TransparentMode = Kee[int](0)
    OpaqueMode = Kee[int](1)

  class BrushStyle(CuteNum):
    """The enum 'Qt::BrushStyle' of Qt, with the 19 names Qt gives in it."""

    NoBrush = Kee[int](0)
    SolidPattern = Kee[int](1)
    Dense1Pattern = Kee[int](2)
    Dense2Pattern = Kee[int](3)
    Dense3Pattern = Kee[int](4)
    Dense4Pattern = Kee[int](5)
    Dense5Pattern = Kee[int](6)
    Dense6Pattern = Kee[int](7)
    Dense7Pattern = Kee[int](8)
    HorPattern = Kee[int](9)
    VerPattern = Kee[int](10)
    CrossPattern = Kee[int](11)
    BDiagPattern = Kee[int](12)
    FDiagPattern = Kee[int](13)
    DiagCrossPattern = Kee[int](14)
    LinearGradientPattern = Kee[int](15)
    RadialGradientPattern = Kee[int](16)
    ConicalGradientPattern = Kee[int](17)
    TexturePattern = Kee[int](24)

  class CaseSensitivity(CuteNum):
    """
    The enum 'Qt::CaseSensitivity' of Qt, with the 2 names Qt gives in it.
    """

    CaseInsensitive = Kee[int](0)
    CaseSensitive = Kee[int](1)

  class CheckState(CuteNum):
    """The enum 'Qt::CheckState' of Qt, with the 3 names Qt gives in it."""

    Unchecked = Kee[int](0)
    PartiallyChecked = Kee[int](1)
    Checked = Kee[int](2)

  class ChecksumType(CuteNum):
    """The enum 'Qt::ChecksumType' of Qt, with the 2 names Qt gives in it."""

    ChecksumIso3309 = Kee[int](0)
    ChecksumItuV41 = Kee[int](1)

  class ClipOperation(CuteNum):
    """
    The enum 'Qt::ClipOperation' of Qt, with the 3 names Qt gives in it.
    """

    NoClip = Kee[int](0)
    ReplaceClip = Kee[int](1)
    IntersectClip = Kee[int](2)

  class ColorScheme(CuteNum, scoped=True):
    """
    The enum 'Qt::ColorScheme' of Qt, with the 3 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Unknown = Kee[int](0)
    Light = Kee[int](1)
    Dark = Kee[int](2)

  class ConnectionType(CuteNum):
    """
    The enum 'Qt::ConnectionType' of Qt, with the 6 names Qt gives in it.
    """

    AutoConnection = Kee[int](0)
    DirectConnection = Kee[int](1)
    QueuedConnection = Kee[int](2)
    BlockingQueuedConnection = Kee[int](3)
    UniqueConnection = Kee[int](128)
    SingleShotConnection = Kee[int](256)

  class ContextMenuPolicy(CuteNum):
    """
    The enum 'Qt::ContextMenuPolicy' of Qt, with the 5 names Qt gives in it.
    """

    NoContextMenu = Kee[int](0)
    DefaultContextMenu = Kee[int](1)
    ActionsContextMenu = Kee[int](2)
    CustomContextMenu = Kee[int](3)
    PreventContextMenu = Kee[int](4)

  class ContextMenuTrigger(CuteNum, scoped=True):
    """
    The enum 'Qt::ContextMenuTrigger' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Press = Kee[int](0)
    Release = Kee[int](1)

  class ContrastPreference(CuteNum, scoped=True):
    """
    The enum 'Qt::ContrastPreference' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoPreference = Kee[int](0)
    HighContrast = Kee[int](1)

  class CoordinateSystem(CuteNum):
    """
    The enum 'Qt::CoordinateSystem' of Qt, with the 2 names Qt gives in it.
    """

    DeviceCoordinates = Kee[int](0)
    LogicalCoordinates = Kee[int](1)

  class Corner(CuteNum):
    """The enum 'Qt::Corner' of Qt, with the 4 names Qt gives in it."""

    TopLeftCorner = Kee[int](0)
    TopRightCorner = Kee[int](1)
    BottomLeftCorner = Kee[int](2)
    BottomRightCorner = Kee[int](3)

  class CursorMoveStyle(CuteNum):
    """
    The enum 'Qt::CursorMoveStyle' of Qt, with the 2 names Qt gives in it.
    """

    LogicalMoveStyle = Kee[int](0)
    VisualMoveStyle = Kee[int](1)

  class CursorShape(CuteNum):
    """The enum 'Qt::CursorShape' of Qt, with the 25 names Qt gives in it."""

    ArrowCursor = Kee[int](0)
    UpArrowCursor = Kee[int](1)
    CrossCursor = Kee[int](2)
    WaitCursor = Kee[int](3)
    IBeamCursor = Kee[int](4)
    SizeVerCursor = Kee[int](5)
    SizeHorCursor = Kee[int](6)
    SizeBDiagCursor = Kee[int](7)
    SizeFDiagCursor = Kee[int](8)
    SizeAllCursor = Kee[int](9)
    BlankCursor = Kee[int](10)
    SplitVCursor = Kee[int](11)
    SplitHCursor = Kee[int](12)
    PointingHandCursor = Kee[int](13)
    ForbiddenCursor = Kee[int](14)
    WhatsThisCursor = Kee[int](15)
    BusyCursor = Kee[int](16)
    OpenHandCursor = Kee[int](17)
    ClosedHandCursor = Kee[int](18)
    DragCopyCursor = Kee[int](19)
    DragMoveCursor = Kee[int](20)
    DragLinkCursor = Kee[int](21)
    LastCursor = Kee[int](21)
    BitmapCursor = Kee[int](24)
    CustomCursor = Kee[int](25)

  class DateFormat(CuteNum):
    """The enum 'Qt::DateFormat' of Qt, with the 4 names Qt gives in it."""

    TextDate = Kee[int](0)
    ISODate = Kee[int](1)
    RFC2822Date = Kee[int](8)
    ISODateWithMs = Kee[int](9)

  class DayOfWeek(CuteNum):
    """The enum 'Qt::DayOfWeek' of Qt, with the 7 names Qt gives in it."""

    Monday = Kee[int](1)
    Tuesday = Kee[int](2)
    Wednesday = Kee[int](3)
    Thursday = Kee[int](4)
    Friday = Kee[int](5)
    Saturday = Kee[int](6)
    Sunday = Kee[int](7)

  class DockWidgetArea(CuteFlags):
    """
    The flags enum 'Qt::DockWidgetArea' of Qt, with the 7 names Qt gives in
    it. Qt names the type of its combinations 'Qt::DockWidgetAreas'.
    """

    LeftDockWidgetArea = 0x1
    RightDockWidgetArea = 0x2
    TopDockWidgetArea = 0x4
    BottomDockWidgetArea = 0x8
    DockWidgetArea_Mask = 0xf
    AllDockWidgetAreas = 0xf
    NoDockWidgetArea = 0x0

  DockWidgetAreas = DockWidgetArea

  class DockWidgetAreaSizes(CuteNum):
    """
    The enum 'Qt::DockWidgetAreaSizes' of Qt, with the 1 names Qt gives in
    it.
    """

    NDockWidgetAreas = Kee[int](4)

  class DropAction(CuteFlags):
    """
    The flags enum 'Qt::DropAction' of Qt, with the 6 names Qt gives in it.
    Qt names the type of its combinations 'Qt::DropActions'.
    """

    CopyAction = 0x1
    MoveAction = 0x2
    LinkAction = 0x4
    ActionMask = 0xff
    TargetMoveAction = 0x8002
    IgnoreAction = 0x0

  DropActions = DropAction

  class Edge(CuteFlags):
    """
    The flags enum 'Qt::Edge' of Qt, with the 4 names Qt gives in it. Qt
    names the type of its combinations 'Qt::Edges'.
    """

    TopEdge = 0x1
    LeftEdge = 0x2
    RightEdge = 0x4
    BottomEdge = 0x8

  Edges = Edge

  class EnterKeyType(CuteNum):
    """The enum 'Qt::EnterKeyType' of Qt, with the 8 names Qt gives in it."""

    EnterKeyDefault = Kee[int](0)
    EnterKeyReturn = Kee[int](1)
    EnterKeyDone = Kee[int](2)
    EnterKeyGo = Kee[int](3)
    EnterKeySend = Kee[int](4)
    EnterKeySearch = Kee[int](5)
    EnterKeyNext = Kee[int](6)
    EnterKeyPrevious = Kee[int](7)

  class EventPriority(CuteNum):
    """
    The enum 'Qt::EventPriority' of Qt, with the 3 names Qt gives in it.
    """

    HighEventPriority = Kee[int](1)
    NormalEventPriority = Kee[int](0)
    LowEventPriority = Kee[int](-1)

  class FillRule(CuteNum):
    """The enum 'Qt::FillRule' of Qt, with the 2 names Qt gives in it."""

    OddEvenFill = Kee[int](0)
    WindingFill = Kee[int](1)

  class FindChildOption(CuteFlags):
    """
    The flags enum 'Qt::FindChildOption' of Qt, with the 2 names Qt gives in
    it. Qt names the type of its combinations 'Qt::FindChildOptions'.
    """

    FindDirectChildrenOnly = 0x0
    FindChildrenRecursively = 0x1

  FindChildOptions = FindChildOption

  class FocusPolicy(CuteNum):
    """The enum 'Qt::FocusPolicy' of Qt, with the 5 names Qt gives in it."""

    NoFocus = Kee[int](0)
    TabFocus = Kee[int](1)
    ClickFocus = Kee[int](2)
    StrongFocus = Kee[int](11)
    WheelFocus = Kee[int](15)

  class FocusReason(CuteNum):
    """The enum 'Qt::FocusReason' of Qt, with the 9 names Qt gives in it."""

    MouseFocusReason = Kee[int](0)
    TabFocusReason = Kee[int](1)
    BacktabFocusReason = Kee[int](2)
    ActiveWindowFocusReason = Kee[int](3)
    PopupFocusReason = Kee[int](4)
    ShortcutFocusReason = Kee[int](5)
    MenuBarFocusReason = Kee[int](6)
    OtherFocusReason = Kee[int](7)
    NoFocusReason = Kee[int](8)

  class GestureFlag(CuteFlags):
    """
    The flags enum 'Qt::GestureFlag' of Qt, with the 3 names Qt gives in it.
    Qt names the type of its combinations 'Qt::GestureFlags'.
    """

    DontStartGestureOnChildren = 0x1
    ReceivePartialGestures = 0x2
    IgnoredGesturesPropagateToParent = 0x4

  GestureFlags = GestureFlag

  class GestureState(CuteNum):
    """The enum 'Qt::GestureState' of Qt, with the 5 names Qt gives in it."""

    NoGesture = Kee[int](0)
    GestureStarted = Kee[int](1)
    GestureUpdated = Kee[int](2)
    GestureFinished = Kee[int](3)
    GestureCanceled = Kee[int](4)

  class GestureType(CuteNum):
    """The enum 'Qt::GestureType' of Qt, with the 7 names Qt gives in it."""

    TapGesture = Kee[int](1)
    TapAndHoldGesture = Kee[int](2)
    PanGesture = Kee[int](3)
    PinchGesture = Kee[int](4)
    SwipeGesture = Kee[int](5)
    CustomGesture = Kee[int](256)
    LastGestureType = Kee[int](4294967295)

  class GlobalColor(CuteNum):
    """The enum 'Qt::GlobalColor' of Qt, with the 20 names Qt gives in it."""

    color0 = Kee[int](0)
    color1 = Kee[int](1)
    black = Kee[int](2)
    white = Kee[int](3)
    darkGray = Kee[int](4)
    gray = Kee[int](5)
    lightGray = Kee[int](6)
    red = Kee[int](7)
    green = Kee[int](8)
    blue = Kee[int](9)
    cyan = Kee[int](10)
    magenta = Kee[int](11)
    yellow = Kee[int](12)
    darkRed = Kee[int](13)
    darkGreen = Kee[int](14)
    darkBlue = Kee[int](15)
    darkCyan = Kee[int](16)
    darkMagenta = Kee[int](17)
    darkYellow = Kee[int](18)
    transparent = Kee[int](19)

  class HighDpiScaleFactorRoundingPolicy(CuteNum, scoped=True):
    """
    The enum 'Qt::HighDpiScaleFactorRoundingPolicy' of Qt, with the 6 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unset = Kee[int](0)
    Round = Kee[int](1)
    Ceil = Kee[int](2)
    Floor = Kee[int](3)
    RoundPreferFloor = Kee[int](4)
    PassThrough = Kee[int](5)

  class HitTestAccuracy(CuteNum):
    """
    The enum 'Qt::HitTestAccuracy' of Qt, with the 2 names Qt gives in it.
    """

    ExactHit = Kee[int](0)
    FuzzyHit = Kee[int](1)

  class ImageConversionFlag(CuteFlags):
    """
    The flags enum 'Qt::ImageConversionFlag' of Qt, with the 19 names Qt
    gives in it. Qt names the type of its combinations
    'Qt::ImageConversionFlags'.
    """

    ColorMode_Mask = 0x3
    AutoColor = 0x0
    ColorOnly = 0x3
    MonoOnly = 0x2
    AlphaDither_Mask = 0xc
    ThresholdAlphaDither = 0x0
    OrderedAlphaDither = 0x4
    DiffuseAlphaDither = 0x8
    NoAlpha = 0xc
    Dither_Mask = 0x30
    DiffuseDither = 0x0
    OrderedDither = 0x10
    ThresholdDither = 0x20
    DitherMode_Mask = 0xc0
    AutoDither = 0x0
    PreferDither = 0x40
    AvoidDither = 0x80
    NoOpaqueDetection = 0x100
    NoFormatConversion = 0x200

  ImageConversionFlags = ImageConversionFlag

  class Initialization(CuteNum, scoped=True):
    """
    The enum 'Qt::Initialization' of Qt, with the 1 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Uninitialized = Kee[int](0)

  class InputMethodHint(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt::InputMethodHint' of Qt, with the 25 names Qt gives in
    it. Qt names the type of its combinations 'Qt::InputMethodHints'.
    """

    ImhNone = 0x0
    ImhHiddenText = 0x1
    ImhSensitiveData = 0x2
    ImhNoAutoUppercase = 0x4
    ImhPreferNumbers = 0x8
    ImhPreferUppercase = 0x10
    ImhPreferLowercase = 0x20
    ImhNoPredictiveText = 0x40
    ImhDate = 0x80
    ImhTime = 0x100
    ImhPreferLatin = 0x200
    ImhMultiLine = 0x400
    ImhNoEditMenu = 0x800
    ImhNoTextHandles = 0x1000
    ImhNoFullscreen = 0x2000
    ImhDigitsOnly = 0x10000
    ImhFormattedNumbersOnly = 0x20000
    ImhUppercaseOnly = 0x40000
    ImhLowercaseOnly = 0x80000
    ImhDialableCharactersOnly = 0x100000
    ImhEmailCharactersOnly = 0x200000
    ImhUrlCharactersOnly = 0x400000
    ImhLatinOnly = 0x800000
    ImhDecimalNumbersOnly = 0x1000000
    ImhExclusiveInputMask = 0xffff0000

  InputMethodHints = InputMethodHint

  class InputMethodQuery(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt::InputMethodQuery' of Qt, with the 20 names Qt gives
    in it. Qt names the type of its combinations 'Qt::InputMethodQueries'.
    """

    ImEnabled = 0x1
    ImCursorRectangle = 0x2
    ImFont = 0x4
    ImCursorPosition = 0x8
    ImSurroundingText = 0x10
    ImCurrentSelection = 0x20
    ImMaximumTextLength = 0x40
    ImAnchorPosition = 0x80
    ImHints = 0x100
    ImPreferredLanguage = 0x200
    ImAbsolutePosition = 0x400
    ImTextBeforeCursor = 0x800
    ImTextAfterCursor = 0x1000
    ImEnterKeyType = 0x2000
    ImAnchorRectangle = 0x4000
    ImInputItemClipRectangle = 0x8000
    ImReadOnly = 0x10000
    ImPlatformData = 0x80000000
    ImQueryInput = 0x40ba
    ImQueryAll = 0xffffffff

  InputMethodQueries = InputMethodQuery

  class ItemDataRole(CuteNum):
    """
    The enum 'Qt::ItemDataRole' of Qt, with the 26 names Qt gives in it.
    """

    DisplayRole = Kee[int](0)
    DecorationRole = Kee[int](1)
    EditRole = Kee[int](2)
    ToolTipRole = Kee[int](3)
    StatusTipRole = Kee[int](4)
    WhatsThisRole = Kee[int](5)
    FontRole = Kee[int](6)
    TextAlignmentRole = Kee[int](7)
    BackgroundRole = Kee[int](8)
    ForegroundRole = Kee[int](9)
    CheckStateRole = Kee[int](10)
    AccessibleTextRole = Kee[int](11)
    AccessibleDescriptionRole = Kee[int](12)
    SizeHintRole = Kee[int](13)
    InitialSortOrderRole = Kee[int](14)
    DisplayPropertyRole = Kee[int](27)
    DecorationPropertyRole = Kee[int](28)
    ToolTipPropertyRole = Kee[int](29)
    StatusTipPropertyRole = Kee[int](30)
    WhatsThisPropertyRole = Kee[int](31)
    RangeModelDataRole = Kee[int](40)
    RangeModelAdapterRole = Kee[int](41)
    UserRole = Kee[int](256)
    StandardItemFlagsRole = Kee[int](255)
    FileInfoRole = Kee[int](252)
    RemoteObjectsCacheRole = Kee[int](255)

  class ItemFlag(CuteFlags):
    """
    The flags enum 'Qt::ItemFlag' of Qt, with the 10 names Qt gives in it. Qt
    names the type of its combinations 'Qt::ItemFlags'.
    """

    NoItemFlags = 0x0
    ItemIsSelectable = 0x1
    ItemIsEditable = 0x2
    ItemIsDragEnabled = 0x4
    ItemIsDropEnabled = 0x8
    ItemIsUserCheckable = 0x10
    ItemIsEnabled = 0x20
    ItemIsAutoTristate = 0x40
    ItemNeverHasChildren = 0x80
    ItemIsUserTristate = 0x100

  ItemFlags = ItemFlag

  class ItemSelectionMode(CuteNum):
    """
    The enum 'Qt::ItemSelectionMode' of Qt, with the 4 names Qt gives in it.
    """

    ContainsItemShape = Kee[int](0)
    IntersectsItemShape = Kee[int](1)
    ContainsItemBoundingRect = Kee[int](2)
    IntersectsItemBoundingRect = Kee[int](3)

  class ItemSelectionOperation(CuteNum):
    """
    The enum 'Qt::ItemSelectionOperation' of Qt, with the 2 names Qt gives in
    it.
    """

    ReplaceSelection = Kee[int](0)
    AddToSelection = Kee[int](1)

  class Key(CuteNum):
    """The enum 'Qt::Key' of Qt, with the 471 names Qt gives in it."""

    Key_Space = Kee[int](32)
    Key_Any = Kee[int](32)
    Key_Exclam = Kee[int](33)
    Key_QuoteDbl = Kee[int](34)
    Key_NumberSign = Kee[int](35)
    Key_Dollar = Kee[int](36)
    Key_Percent = Kee[int](37)
    Key_Ampersand = Kee[int](38)
    Key_Apostrophe = Kee[int](39)
    Key_ParenLeft = Kee[int](40)
    Key_ParenRight = Kee[int](41)
    Key_Asterisk = Kee[int](42)
    Key_Plus = Kee[int](43)
    Key_Comma = Kee[int](44)
    Key_Minus = Kee[int](45)
    Key_Period = Kee[int](46)
    Key_Slash = Kee[int](47)
    Key_0 = Kee[int](48)
    Key_1 = Kee[int](49)
    Key_2 = Kee[int](50)
    Key_3 = Kee[int](51)
    Key_4 = Kee[int](52)
    Key_5 = Kee[int](53)
    Key_6 = Kee[int](54)
    Key_7 = Kee[int](55)
    Key_8 = Kee[int](56)
    Key_9 = Kee[int](57)
    Key_Colon = Kee[int](58)
    Key_Semicolon = Kee[int](59)
    Key_Less = Kee[int](60)
    Key_Equal = Kee[int](61)
    Key_Greater = Kee[int](62)
    Key_Question = Kee[int](63)
    Key_At = Kee[int](64)
    Key_A = Kee[int](65)
    Key_B = Kee[int](66)
    Key_C = Kee[int](67)
    Key_D = Kee[int](68)
    Key_E = Kee[int](69)
    Key_F = Kee[int](70)
    Key_G = Kee[int](71)
    Key_H = Kee[int](72)
    Key_I = Kee[int](73)
    Key_J = Kee[int](74)
    Key_K = Kee[int](75)
    Key_L = Kee[int](76)
    Key_M = Kee[int](77)
    Key_N = Kee[int](78)
    Key_O = Kee[int](79)
    Key_P = Kee[int](80)
    Key_Q = Kee[int](81)
    Key_R = Kee[int](82)
    Key_S = Kee[int](83)
    Key_T = Kee[int](84)
    Key_U = Kee[int](85)
    Key_V = Kee[int](86)
    Key_W = Kee[int](87)
    Key_X = Kee[int](88)
    Key_Y = Kee[int](89)
    Key_Z = Kee[int](90)
    Key_BracketLeft = Kee[int](91)
    Key_Backslash = Kee[int](92)
    Key_BracketRight = Kee[int](93)
    Key_AsciiCircum = Kee[int](94)
    Key_Underscore = Kee[int](95)
    Key_QuoteLeft = Kee[int](96)
    Key_BraceLeft = Kee[int](123)
    Key_Bar = Kee[int](124)
    Key_BraceRight = Kee[int](125)
    Key_AsciiTilde = Kee[int](126)
    Key_nobreakspace = Kee[int](160)
    Key_exclamdown = Kee[int](161)
    Key_cent = Kee[int](162)
    Key_sterling = Kee[int](163)
    Key_currency = Kee[int](164)
    Key_yen = Kee[int](165)
    Key_brokenbar = Kee[int](166)
    Key_section = Kee[int](167)
    Key_diaeresis = Kee[int](168)
    Key_copyright = Kee[int](169)
    Key_ordfeminine = Kee[int](170)
    Key_guillemotleft = Kee[int](171)
    Key_notsign = Kee[int](172)
    Key_hyphen = Kee[int](173)
    Key_registered = Kee[int](174)
    Key_macron = Kee[int](175)
    Key_degree = Kee[int](176)
    Key_plusminus = Kee[int](177)
    Key_twosuperior = Kee[int](178)
    Key_threesuperior = Kee[int](179)
    Key_acute = Kee[int](180)
    Key_micro = Kee[int](181)
    Key_mu = Kee[int](181)
    Key_paragraph = Kee[int](182)
    Key_periodcentered = Kee[int](183)
    Key_cedilla = Kee[int](184)
    Key_onesuperior = Kee[int](185)
    Key_masculine = Kee[int](186)
    Key_guillemotright = Kee[int](187)
    Key_onequarter = Kee[int](188)
    Key_onehalf = Kee[int](189)
    Key_threequarters = Kee[int](190)
    Key_questiondown = Kee[int](191)
    Key_Agrave = Kee[int](192)
    Key_Aacute = Kee[int](193)
    Key_Acircumflex = Kee[int](194)
    Key_Atilde = Kee[int](195)
    Key_Adiaeresis = Kee[int](196)
    Key_Aring = Kee[int](197)
    Key_AE = Kee[int](198)
    Key_Ccedilla = Kee[int](199)
    Key_Egrave = Kee[int](200)
    Key_Eacute = Kee[int](201)
    Key_Ecircumflex = Kee[int](202)
    Key_Ediaeresis = Kee[int](203)
    Key_Igrave = Kee[int](204)
    Key_Iacute = Kee[int](205)
    Key_Icircumflex = Kee[int](206)
    Key_Idiaeresis = Kee[int](207)
    Key_ETH = Kee[int](208)
    Key_Ntilde = Kee[int](209)
    Key_Ograve = Kee[int](210)
    Key_Oacute = Kee[int](211)
    Key_Ocircumflex = Kee[int](212)
    Key_Otilde = Kee[int](213)
    Key_Odiaeresis = Kee[int](214)
    Key_multiply = Kee[int](215)
    Key_Ooblique = Kee[int](216)
    Key_Ugrave = Kee[int](217)
    Key_Uacute = Kee[int](218)
    Key_Ucircumflex = Kee[int](219)
    Key_Udiaeresis = Kee[int](220)
    Key_Yacute = Kee[int](221)
    Key_THORN = Kee[int](222)
    Key_ssharp = Kee[int](223)
    Key_division = Kee[int](247)
    Key_ydiaeresis = Kee[int](255)
    Key_Escape = Kee[int](16777216)
    Key_Tab = Kee[int](16777217)
    Key_Backtab = Kee[int](16777218)
    Key_Backspace = Kee[int](16777219)
    Key_Return = Kee[int](16777220)
    Key_Enter = Kee[int](16777221)
    Key_Insert = Kee[int](16777222)
    Key_Delete = Kee[int](16777223)
    Key_Pause = Kee[int](16777224)
    Key_Print = Kee[int](16777225)
    Key_SysReq = Kee[int](16777226)
    Key_Clear = Kee[int](16777227)
    Key_Home = Kee[int](16777232)
    Key_End = Kee[int](16777233)
    Key_Left = Kee[int](16777234)
    Key_Up = Kee[int](16777235)
    Key_Right = Kee[int](16777236)
    Key_Down = Kee[int](16777237)
    Key_PageUp = Kee[int](16777238)
    Key_PageDown = Kee[int](16777239)
    Key_Shift = Kee[int](16777248)
    Key_Control = Kee[int](16777249)
    Key_Meta = Kee[int](16777250)
    Key_Alt = Kee[int](16777251)
    Key_CapsLock = Kee[int](16777252)
    Key_NumLock = Kee[int](16777253)
    Key_ScrollLock = Kee[int](16777254)
    Key_F1 = Kee[int](16777264)
    Key_F2 = Kee[int](16777265)
    Key_F3 = Kee[int](16777266)
    Key_F4 = Kee[int](16777267)
    Key_F5 = Kee[int](16777268)
    Key_F6 = Kee[int](16777269)
    Key_F7 = Kee[int](16777270)
    Key_F8 = Kee[int](16777271)
    Key_F9 = Kee[int](16777272)
    Key_F10 = Kee[int](16777273)
    Key_F11 = Kee[int](16777274)
    Key_F12 = Kee[int](16777275)
    Key_F13 = Kee[int](16777276)
    Key_F14 = Kee[int](16777277)
    Key_F15 = Kee[int](16777278)
    Key_F16 = Kee[int](16777279)
    Key_F17 = Kee[int](16777280)
    Key_F18 = Kee[int](16777281)
    Key_F19 = Kee[int](16777282)
    Key_F20 = Kee[int](16777283)
    Key_F21 = Kee[int](16777284)
    Key_F22 = Kee[int](16777285)
    Key_F23 = Kee[int](16777286)
    Key_F24 = Kee[int](16777287)
    Key_F25 = Kee[int](16777288)
    Key_F26 = Kee[int](16777289)
    Key_F27 = Kee[int](16777290)
    Key_F28 = Kee[int](16777291)
    Key_F29 = Kee[int](16777292)
    Key_F30 = Kee[int](16777293)
    Key_F31 = Kee[int](16777294)
    Key_F32 = Kee[int](16777295)
    Key_F33 = Kee[int](16777296)
    Key_F34 = Kee[int](16777297)
    Key_F35 = Kee[int](16777298)
    Key_Super_L = Kee[int](16777299)
    Key_Super_R = Kee[int](16777300)
    Key_Menu = Kee[int](16777301)
    Key_Hyper_L = Kee[int](16777302)
    Key_Hyper_R = Kee[int](16777303)
    Key_Help = Kee[int](16777304)
    Key_Direction_L = Kee[int](16777305)
    Key_Direction_R = Kee[int](16777312)
    Key_AltGr = Kee[int](16781571)
    Key_Multi_key = Kee[int](16781600)
    Key_Codeinput = Kee[int](16781623)
    Key_SingleCandidate = Kee[int](16781628)
    Key_MultipleCandidate = Kee[int](16781629)
    Key_PreviousCandidate = Kee[int](16781630)
    Key_Mode_switch = Kee[int](16781694)
    Key_Kanji = Kee[int](16781601)
    Key_Muhenkan = Kee[int](16781602)
    Key_Henkan = Kee[int](16781603)
    Key_Romaji = Kee[int](16781604)
    Key_Hiragana = Kee[int](16781605)
    Key_Katakana = Kee[int](16781606)
    Key_Hiragana_Katakana = Kee[int](16781607)
    Key_Zenkaku = Kee[int](16781608)
    Key_Hankaku = Kee[int](16781609)
    Key_Zenkaku_Hankaku = Kee[int](16781610)
    Key_Touroku = Kee[int](16781611)
    Key_Massyo = Kee[int](16781612)
    Key_Kana_Lock = Kee[int](16781613)
    Key_Kana_Shift = Kee[int](16781614)
    Key_Eisu_Shift = Kee[int](16781615)
    Key_Eisu_toggle = Kee[int](16781616)
    Key_Hangul = Kee[int](16781617)
    Key_Hangul_Start = Kee[int](16781618)
    Key_Hangul_End = Kee[int](16781619)
    Key_Hangul_Hanja = Kee[int](16781620)
    Key_Hangul_Jamo = Kee[int](16781621)
    Key_Hangul_Romaja = Kee[int](16781622)
    Key_Hangul_Jeonja = Kee[int](16781624)
    Key_Hangul_Banja = Kee[int](16781625)
    Key_Hangul_PreHanja = Kee[int](16781626)
    Key_Hangul_PostHanja = Kee[int](16781627)
    Key_Hangul_Special = Kee[int](16781631)
    Key_Dead_Grave = Kee[int](16781904)
    Key_Dead_Acute = Kee[int](16781905)
    Key_Dead_Circumflex = Kee[int](16781906)
    Key_Dead_Tilde = Kee[int](16781907)
    Key_Dead_Macron = Kee[int](16781908)
    Key_Dead_Breve = Kee[int](16781909)
    Key_Dead_Abovedot = Kee[int](16781910)
    Key_Dead_Diaeresis = Kee[int](16781911)
    Key_Dead_Abovering = Kee[int](16781912)
    Key_Dead_Doubleacute = Kee[int](16781913)
    Key_Dead_Caron = Kee[int](16781914)
    Key_Dead_Cedilla = Kee[int](16781915)
    Key_Dead_Ogonek = Kee[int](16781916)
    Key_Dead_Iota = Kee[int](16781917)
    Key_Dead_Voiced_Sound = Kee[int](16781918)
    Key_Dead_Semivoiced_Sound = Kee[int](16781919)
    Key_Dead_Belowdot = Kee[int](16781920)
    Key_Dead_Hook = Kee[int](16781921)
    Key_Dead_Horn = Kee[int](16781922)
    Key_Dead_Stroke = Kee[int](16781923)
    Key_Dead_Abovecomma = Kee[int](16781924)
    Key_Dead_Abovereversedcomma = Kee[int](16781925)
    Key_Dead_Doublegrave = Kee[int](16781926)
    Key_Dead_Belowring = Kee[int](16781927)
    Key_Dead_Belowmacron = Kee[int](16781928)
    Key_Dead_Belowcircumflex = Kee[int](16781929)
    Key_Dead_Belowtilde = Kee[int](16781930)
    Key_Dead_Belowbreve = Kee[int](16781931)
    Key_Dead_Belowdiaeresis = Kee[int](16781932)
    Key_Dead_Invertedbreve = Kee[int](16781933)
    Key_Dead_Belowcomma = Kee[int](16781934)
    Key_Dead_Currency = Kee[int](16781935)
    Key_Dead_a = Kee[int](16781952)
    Key_Dead_A = Kee[int](16781953)
    Key_Dead_e = Kee[int](16781954)
    Key_Dead_E = Kee[int](16781955)
    Key_Dead_i = Kee[int](16781956)
    Key_Dead_I = Kee[int](16781957)
    Key_Dead_o = Kee[int](16781958)
    Key_Dead_O = Kee[int](16781959)
    Key_Dead_u = Kee[int](16781960)
    Key_Dead_U = Kee[int](16781961)
    Key_Dead_Small_Schwa = Kee[int](16781962)
    Key_Dead_Capital_Schwa = Kee[int](16781963)
    Key_Dead_Greek = Kee[int](16781964)
    Key_Dead_Lowline = Kee[int](16781968)
    Key_Dead_Aboveverticalline = Kee[int](16781969)
    Key_Dead_Belowverticalline = Kee[int](16781970)
    Key_Dead_Longsolidusoverlay = Kee[int](16781971)
    Key_Back = Kee[int](16777313)
    Key_Forward = Kee[int](16777314)
    Key_Stop = Kee[int](16777315)
    Key_Refresh = Kee[int](16777316)
    Key_VolumeDown = Kee[int](16777328)
    Key_VolumeMute = Kee[int](16777329)
    Key_VolumeUp = Kee[int](16777330)
    Key_BassBoost = Kee[int](16777331)
    Key_BassUp = Kee[int](16777332)
    Key_BassDown = Kee[int](16777333)
    Key_TrebleUp = Kee[int](16777334)
    Key_TrebleDown = Kee[int](16777335)
    Key_MediaPlay = Kee[int](16777344)
    Key_MediaStop = Kee[int](16777345)
    Key_MediaPrevious = Kee[int](16777346)
    Key_MediaNext = Kee[int](16777347)
    Key_MediaRecord = Kee[int](16777348)
    Key_MediaPause = Kee[int](16777349)
    Key_MediaTogglePlayPause = Kee[int](16777350)
    Key_HomePage = Kee[int](16777360)
    Key_Favorites = Kee[int](16777361)
    Key_Search = Kee[int](16777362)
    Key_Standby = Kee[int](16777363)
    Key_OpenUrl = Kee[int](16777364)
    Key_LaunchMail = Kee[int](16777376)
    Key_LaunchMedia = Kee[int](16777377)
    Key_Launch0 = Kee[int](16777378)
    Key_Launch1 = Kee[int](16777379)
    Key_Launch2 = Kee[int](16777380)
    Key_Launch3 = Kee[int](16777381)
    Key_Launch4 = Kee[int](16777382)
    Key_Launch5 = Kee[int](16777383)
    Key_Launch6 = Kee[int](16777384)
    Key_Launch7 = Kee[int](16777385)
    Key_Launch8 = Kee[int](16777386)
    Key_Launch9 = Kee[int](16777387)
    Key_LaunchA = Kee[int](16777388)
    Key_LaunchB = Kee[int](16777389)
    Key_LaunchC = Kee[int](16777390)
    Key_LaunchD = Kee[int](16777391)
    Key_LaunchE = Kee[int](16777392)
    Key_LaunchF = Kee[int](16777393)
    Key_MonBrightnessUp = Kee[int](16777394)
    Key_MonBrightnessDown = Kee[int](16777395)
    Key_KeyboardLightOnOff = Kee[int](16777396)
    Key_KeyboardBrightnessUp = Kee[int](16777397)
    Key_KeyboardBrightnessDown = Kee[int](16777398)
    Key_PowerOff = Kee[int](16777399)
    Key_WakeUp = Kee[int](16777400)
    Key_Eject = Kee[int](16777401)
    Key_ScreenSaver = Kee[int](16777402)
    Key_WWW = Kee[int](16777403)
    Key_Memo = Kee[int](16777404)
    Key_LightBulb = Kee[int](16777405)
    Key_Shop = Kee[int](16777406)
    Key_History = Kee[int](16777407)
    Key_AddFavorite = Kee[int](16777408)
    Key_HotLinks = Kee[int](16777409)
    Key_BrightnessAdjust = Kee[int](16777410)
    Key_Finance = Kee[int](16777411)
    Key_Community = Kee[int](16777412)
    Key_AudioRewind = Kee[int](16777413)
    Key_BackForward = Kee[int](16777414)
    Key_ApplicationLeft = Kee[int](16777415)
    Key_ApplicationRight = Kee[int](16777416)
    Key_Book = Kee[int](16777417)
    Key_CD = Kee[int](16777418)
    Key_Calculator = Kee[int](16777419)
    Key_ToDoList = Kee[int](16777420)
    Key_ClearGrab = Kee[int](16777421)
    Key_Close = Kee[int](16777422)
    Key_Copy = Kee[int](16777423)
    Key_Cut = Kee[int](16777424)
    Key_Display = Kee[int](16777425)
    Key_DOS = Kee[int](16777426)
    Key_Documents = Kee[int](16777427)
    Key_Excel = Kee[int](16777428)
    Key_Explorer = Kee[int](16777429)
    Key_Game = Kee[int](16777430)
    Key_Go = Kee[int](16777431)
    Key_iTouch = Kee[int](16777432)
    Key_LogOff = Kee[int](16777433)
    Key_Market = Kee[int](16777434)
    Key_Meeting = Kee[int](16777435)
    Key_MenuKB = Kee[int](16777436)
    Key_MenuPB = Kee[int](16777437)
    Key_MySites = Kee[int](16777438)
    Key_News = Kee[int](16777439)
    Key_OfficeHome = Kee[int](16777440)
    Key_Option = Kee[int](16777441)
    Key_Paste = Kee[int](16777442)
    Key_Phone = Kee[int](16777443)
    Key_Calendar = Kee[int](16777444)
    Key_Reply = Kee[int](16777445)
    Key_Reload = Kee[int](16777446)
    Key_RotateWindows = Kee[int](16777447)
    Key_RotationPB = Kee[int](16777448)
    Key_RotationKB = Kee[int](16777449)
    Key_Save = Kee[int](16777450)
    Key_Send = Kee[int](16777451)
    Key_Spell = Kee[int](16777452)
    Key_SplitScreen = Kee[int](16777453)
    Key_Support = Kee[int](16777454)
    Key_TaskPane = Kee[int](16777455)
    Key_Terminal = Kee[int](16777456)
    Key_Tools = Kee[int](16777457)
    Key_Travel = Kee[int](16777458)
    Key_Video = Kee[int](16777459)
    Key_Word = Kee[int](16777460)
    Key_Xfer = Kee[int](16777461)
    Key_ZoomIn = Kee[int](16777462)
    Key_ZoomOut = Kee[int](16777463)
    Key_Away = Kee[int](16777464)
    Key_Messenger = Kee[int](16777465)
    Key_WebCam = Kee[int](16777466)
    Key_MailForward = Kee[int](16777467)
    Key_Pictures = Kee[int](16777468)
    Key_Music = Kee[int](16777469)
    Key_Battery = Kee[int](16777470)
    Key_Bluetooth = Kee[int](16777471)
    Key_WLAN = Kee[int](16777472)
    Key_UWB = Kee[int](16777473)
    Key_AudioForward = Kee[int](16777474)
    Key_AudioRepeat = Kee[int](16777475)
    Key_AudioRandomPlay = Kee[int](16777476)
    Key_Subtitle = Kee[int](16777477)
    Key_AudioCycleTrack = Kee[int](16777478)
    Key_Time = Kee[int](16777479)
    Key_Hibernate = Kee[int](16777480)
    Key_View = Kee[int](16777481)
    Key_TopMenu = Kee[int](16777482)
    Key_PowerDown = Kee[int](16777483)
    Key_Suspend = Kee[int](16777484)
    Key_ContrastAdjust = Kee[int](16777485)
    Key_LaunchG = Kee[int](16777486)
    Key_LaunchH = Kee[int](16777487)
    Key_TouchpadToggle = Kee[int](16777488)
    Key_TouchpadOn = Kee[int](16777489)
    Key_TouchpadOff = Kee[int](16777490)
    Key_MicMute = Kee[int](16777491)
    Key_Red = Kee[int](16777492)
    Key_Green = Kee[int](16777493)
    Key_Yellow = Kee[int](16777494)
    Key_Blue = Kee[int](16777495)
    Key_ChannelUp = Kee[int](16777496)
    Key_ChannelDown = Kee[int](16777497)
    Key_Guide = Kee[int](16777498)
    Key_Info = Kee[int](16777499)
    Key_Settings = Kee[int](16777500)
    Key_MicVolumeUp = Kee[int](16777501)
    Key_MicVolumeDown = Kee[int](16777502)
    Key_Keyboard = Kee[int](16777503)
    Key_New = Kee[int](16777504)
    Key_Open = Kee[int](16777505)
    Key_Find = Kee[int](16777506)
    Key_Undo = Kee[int](16777507)
    Key_Redo = Kee[int](16777508)
    Key_MediaLast = Kee[int](16842751)
    Key_Select = Kee[int](16842752)
    Key_Yes = Kee[int](16842753)
    Key_No = Kee[int](16842754)
    Key_Cancel = Kee[int](16908289)
    Key_Printer = Kee[int](16908290)
    Key_Execute = Kee[int](16908291)
    Key_Sleep = Kee[int](16908292)
    Key_Play = Kee[int](16908293)
    Key_Zoom = Kee[int](16908294)
    Key_Exit = Kee[int](16908298)
    Key_Context1 = Kee[int](17825792)
    Key_Context2 = Kee[int](17825793)
    Key_Context3 = Kee[int](17825794)
    Key_Context4 = Kee[int](17825795)
    Key_Call = Kee[int](17825796)
    Key_Hangup = Kee[int](17825797)
    Key_Flip = Kee[int](17825798)
    Key_ToggleCallHangup = Kee[int](17825799)
    Key_VoiceDial = Kee[int](17825800)
    Key_LastNumberRedial = Kee[int](17825801)
    Key_Camera = Kee[int](17825824)
    Key_CameraFocus = Kee[int](17825825)
    Key_unknown = Kee[int](33554431)

  class KeyboardModifier(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt::KeyboardModifier' of Qt, with the 8 names Qt gives in
    it. Qt names the type of its combinations 'Qt::KeyboardModifiers'.
    """

    NoModifier = 0x0
    ShiftModifier = 0x2000000
    ControlModifier = 0x4000000
    AltModifier = 0x8000000
    MetaModifier = 0x10000000
    KeypadModifier = 0x20000000
    GroupSwitchModifier = 0x40000000
    KeyboardModifierMask = 0xfe000000

  KeyboardModifiers = KeyboardModifier

  class LayoutDirection(CuteNum):
    """
    The enum 'Qt::LayoutDirection' of Qt, with the 3 names Qt gives in it.
    """

    LeftToRight = Kee[int](0)
    RightToLeft = Kee[int](1)
    LayoutDirectionAuto = Kee[int](2)

  class MaskMode(CuteNum):
    """The enum 'Qt::MaskMode' of Qt, with the 2 names Qt gives in it."""

    MaskInColor = Kee[int](0)
    MaskOutColor = Kee[int](1)

  class MatchFlag(CuteFlags):
    """
    The flags enum 'Qt::MatchFlag' of Qt, with the 11 names Qt gives in it.
    Qt names the type of its combinations 'Qt::MatchFlags'.
    """

    MatchExactly = 0x0
    MatchContains = 0x1
    MatchStartsWith = 0x2
    MatchEndsWith = 0x3
    MatchRegularExpression = 0x4
    MatchWildcard = 0x5
    MatchFixedString = 0x8
    MatchTypeMask = 0xf
    MatchCaseSensitive = 0x10
    MatchWrap = 0x20
    MatchRecursive = 0x40

  MatchFlags = MatchFlag

  class Modifier(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt::Modifier' of Qt, with the 5 names Qt gives in it. Qt
    names the type of its combinations 'Qt::Modifiers'.
    """

    META = 0x10000000
    SHIFT = 0x2000000
    CTRL = 0x4000000
    ALT = 0x8000000
    MODIFIER_MASK = 0xfe000000

  Modifiers = Modifier

  class MotionPreference(CuteNum, scoped=True):
    """
    The enum 'Qt::MotionPreference' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoPreference = Kee[int](0)
    ReducedMotion = Kee[int](1)

  class MouseButton(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt::MouseButton' of Qt, with the 36 names Qt gives in it.
    Qt names the type of its combinations 'Qt::MouseButtons'.
    """

    NoButton = 0x0
    LeftButton = 0x1
    RightButton = 0x2
    MiddleButton = 0x4
    BackButton = 0x8
    XButton1 = 0x8
    ExtraButton1 = 0x8
    ForwardButton = 0x10
    XButton2 = 0x10
    ExtraButton2 = 0x10
    TaskButton = 0x20
    ExtraButton3 = 0x20
    ExtraButton4 = 0x40
    ExtraButton5 = 0x80
    ExtraButton6 = 0x100
    ExtraButton7 = 0x200
    ExtraButton8 = 0x400
    ExtraButton9 = 0x800
    ExtraButton10 = 0x1000
    ExtraButton11 = 0x2000
    ExtraButton12 = 0x4000
    ExtraButton13 = 0x8000
    ExtraButton14 = 0x10000
    ExtraButton15 = 0x20000
    ExtraButton16 = 0x40000
    ExtraButton17 = 0x80000
    ExtraButton18 = 0x100000
    ExtraButton19 = 0x200000
    ExtraButton20 = 0x400000
    ExtraButton21 = 0x800000
    ExtraButton22 = 0x1000000
    ExtraButton23 = 0x2000000
    ExtraButton24 = 0x4000000
    AllButtons = 0x7ffffff
    MaxMouseButton = 0x4000000
    MouseButtonMask = 0xffffffff

  MouseButtons = MouseButton

  class MouseEventFlag(CuteFlags):
    """
    The flags enum 'Qt::MouseEventFlag' of Qt, with the 3 names Qt gives in
    it. Qt names the type of its combinations 'Qt::MouseEventFlags'.
    """

    NoMouseEventFlag = 0x0
    MouseEventCreatedDoubleClick = 0x1
    MouseEventFlagMask = 0xff

  MouseEventFlags = MouseEventFlag

  class MouseEventSource(CuteNum):
    """
    The enum 'Qt::MouseEventSource' of Qt, with the 4 names Qt gives in it.
    """

    MouseEventNotSynthesized = Kee[int](0)
    MouseEventSynthesizedBySystem = Kee[int](1)
    MouseEventSynthesizedByQt = Kee[int](2)
    MouseEventSynthesizedByApplication = Kee[int](3)

  class NativeGestureType(CuteNum):
    """
    The enum 'Qt::NativeGestureType' of Qt, with the 7 names Qt gives in it.
    """

    BeginNativeGesture = Kee[int](0)
    EndNativeGesture = Kee[int](1)
    PanNativeGesture = Kee[int](2)
    ZoomNativeGesture = Kee[int](3)
    SmartZoomNativeGesture = Kee[int](4)
    RotateNativeGesture = Kee[int](5)
    SwipeNativeGesture = Kee[int](6)

  class NavigationMode(CuteNum):
    """
    The enum 'Qt::NavigationMode' of Qt, with the 5 names Qt gives in it.
    """

    NavigationModeNone = Kee[int](0)
    NavigationModeKeypadTabOrder = Kee[int](1)
    NavigationModeKeypadDirectional = Kee[int](2)
    NavigationModeCursorAuto = Kee[int](3)
    NavigationModeCursorForceVisible = Kee[int](4)

  class Orientation(CuteFlags):
    """
    The flags enum 'Qt::Orientation' of Qt, with the 2 names Qt gives in it.
    Qt names the type of its combinations 'Qt::Orientations'.
    """

    Horizontal = 0x1
    Vertical = 0x2

  Orientations = Orientation

  class PenCapStyle(CuteNum):
    """The enum 'Qt::PenCapStyle' of Qt, with the 4 names Qt gives in it."""

    FlatCap = Kee[int](0)
    SquareCap = Kee[int](16)
    RoundCap = Kee[int](32)
    MPenCapStyle = Kee[int](48)

  class PenJoinStyle(CuteNum):
    """The enum 'Qt::PenJoinStyle' of Qt, with the 5 names Qt gives in it."""

    MiterJoin = Kee[int](0)
    BevelJoin = Kee[int](64)
    RoundJoin = Kee[int](128)
    SvgMiterJoin = Kee[int](256)
    MPenJoinStyle = Kee[int](448)

  class PenStyle(CuteNum):
    """The enum 'Qt::PenStyle' of Qt, with the 8 names Qt gives in it."""

    NoPen = Kee[int](0)
    SolidLine = Kee[int](1)
    DashLine = Kee[int](2)
    DotLine = Kee[int](3)
    DashDotLine = Kee[int](4)
    DashDotDotLine = Kee[int](5)
    CustomDashLine = Kee[int](6)
    MPenStyle = Kee[int](15)

  class PermissionStatus(CuteNum, scoped=True):
    """
    The enum 'Qt::PermissionStatus' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Undetermined = Kee[int](0)
    Granted = Kee[int](1)
    Denied = Kee[int](2)

  class ReturnByValueConstant(CuteNum):
    """
    The enum 'Qt::ReturnByValueConstant' of Qt, with the 1 names Qt gives in
    it.
    """

    ReturnByValue = Kee[int](0)

  class ScreenOrientation(CuteFlags):
    """
    The flags enum 'Qt::ScreenOrientation' of Qt, with the 5 names Qt gives
    in it. Qt names the type of its combinations 'Qt::ScreenOrientations'.
    """

    PrimaryOrientation = 0x0
    PortraitOrientation = 0x1
    LandscapeOrientation = 0x2
    InvertedPortraitOrientation = 0x4
    InvertedLandscapeOrientation = 0x8

  ScreenOrientations = ScreenOrientation

  class ScrollBarPolicy(CuteNum):
    """
    The enum 'Qt::ScrollBarPolicy' of Qt, with the 3 names Qt gives in it.
    """

    ScrollBarAsNeeded = Kee[int](0)
    ScrollBarAlwaysOff = Kee[int](1)
    ScrollBarAlwaysOn = Kee[int](2)

  class ScrollPhase(CuteNum):
    """The enum 'Qt::ScrollPhase' of Qt, with the 5 names Qt gives in it."""

    NoScrollPhase = Kee[int](0)
    ScrollBegin = Kee[int](1)
    ScrollUpdate = Kee[int](2)
    ScrollEnd = Kee[int](3)
    ScrollMomentum = Kee[int](4)

  class ShortcutContext(CuteNum):
    """
    The enum 'Qt::ShortcutContext' of Qt, with the 4 names Qt gives in it.
    """

    WidgetShortcut = Kee[int](0)
    WindowShortcut = Kee[int](1)
    ApplicationShortcut = Kee[int](2)
    WidgetWithChildrenShortcut = Kee[int](3)

  class SizeHint(CuteNum):
    """The enum 'Qt::SizeHint' of Qt, with the 5 names Qt gives in it."""

    MinimumSize = Kee[int](0)
    PreferredSize = Kee[int](1)
    MaximumSize = Kee[int](2)
    MinimumDescent = Kee[int](3)
    NSizeHints = Kee[int](4)

  class SizeMode(CuteNum):
    """The enum 'Qt::SizeMode' of Qt, with the 2 names Qt gives in it."""

    AbsoluteSize = Kee[int](0)
    RelativeSize = Kee[int](1)

  class SortOrder(CuteNum):
    """The enum 'Qt::SortOrder' of Qt, with the 2 names Qt gives in it."""

    AscendingOrder = Kee[int](0)
    DescendingOrder = Kee[int](1)

  class SplitBehaviorFlags(CuteFlags):
    """
    The flags enum 'Qt::SplitBehaviorFlags' of Qt, with the 2 names Qt gives
    in it. Qt names the type of its combinations 'Qt::SplitBehavior'.
    """

    KeepEmptyParts = 0x0
    SkipEmptyParts = 0x1

  SplitBehavior = SplitBehaviorFlags

  class TabFocusBehavior(CuteNum):
    """
    The enum 'Qt::TabFocusBehavior' of Qt, with the 4 names Qt gives in it.
    """

    NoTabFocus = Kee[int](0)
    TabFocusTextControls = Kee[int](1)
    TabFocusListControls = Kee[int](2)
    TabFocusAllControls = Kee[int](255)

  class TextElideMode(CuteNum):
    """
    The enum 'Qt::TextElideMode' of Qt, with the 4 names Qt gives in it.
    """

    ElideLeft = Kee[int](0)
    ElideRight = Kee[int](1)
    ElideMiddle = Kee[int](2)
    ElideNone = Kee[int](3)

  class TextFlag(CuteNum):
    """The enum 'Qt::TextFlag' of Qt, with the 13 names Qt gives in it."""

    TextSingleLine = Kee[int](256)
    TextDontClip = Kee[int](512)
    TextExpandTabs = Kee[int](1024)
    TextShowMnemonic = Kee[int](2048)
    TextWordWrap = Kee[int](4096)
    TextWrapAnywhere = Kee[int](8192)
    TextDontPrint = Kee[int](16384)
    TextIncludeTrailingSpaces = Kee[int](134217728)
    TextHideMnemonic = Kee[int](32768)
    TextJustificationForced = Kee[int](65536)
    TextForceLeftToRight = Kee[int](131072)
    TextForceRightToLeft = Kee[int](262144)
    TextLongestVariant = Kee[int](524288)

  class TextFormat(CuteNum):
    """The enum 'Qt::TextFormat' of Qt, with the 4 names Qt gives in it."""

    PlainText = Kee[int](0)
    RichText = Kee[int](1)
    AutoText = Kee[int](2)
    MarkdownText = Kee[int](3)

  class TextInteractionFlag(CuteFlags):
    """
    The flags enum 'Qt::TextInteractionFlag' of Qt, with the 8 names Qt gives
    in it. Qt names the type of its combinations 'Qt::TextInteractionFlags'.
    """

    NoTextInteraction = 0x0
    TextSelectableByMouse = 0x1
    TextSelectableByKeyboard = 0x2
    LinksAccessibleByMouse = 0x4
    LinksAccessibleByKeyboard = 0x8
    TextEditable = 0x10
    TextEditorInteraction = 0x13
    TextBrowserInteraction = 0xd

  TextInteractionFlags = TextInteractionFlag

  class TileRule(CuteNum):
    """The enum 'Qt::TileRule' of Qt, with the 3 names Qt gives in it."""

    StretchTile = Kee[int](0)
    RepeatTile = Kee[int](1)
    RoundTile = Kee[int](2)

  class TimeSpec(CuteNum):
    """The enum 'Qt::TimeSpec' of Qt, with the 4 names Qt gives in it."""

    LocalTime = Kee[int](0)
    UTC = Kee[int](1)
    OffsetFromUTC = Kee[int](2)
    TimeZone = Kee[int](3)

  class TimerId(CuteNum, scoped=True):
    """
    The enum 'Qt::TimerId' of Qt, with the 1 names Qt gives in it. C++ keeps
    these names inside the enum, so the class that holds the enum does not
    have them.
    """

    Invalid = Kee[int](0)

  class TimerType(CuteNum):
    """The enum 'Qt::TimerType' of Qt, with the 3 names Qt gives in it."""

    PreciseTimer = Kee[int](0)
    CoarseTimer = Kee[int](1)
    VeryCoarseTimer = Kee[int](2)

  class ToolBarArea(CuteFlags):
    """
    The flags enum 'Qt::ToolBarArea' of Qt, with the 7 names Qt gives in it.
    Qt names the type of its combinations 'Qt::ToolBarAreas'.
    """

    LeftToolBarArea = 0x1
    RightToolBarArea = 0x2
    TopToolBarArea = 0x4
    BottomToolBarArea = 0x8
    ToolBarArea_Mask = 0xf
    AllToolBarAreas = 0xf
    NoToolBarArea = 0x0

  ToolBarAreas = ToolBarArea

  class ToolBarAreaSizes(CuteNum):
    """
    The enum 'Qt::ToolBarAreaSizes' of Qt, with the 1 names Qt gives in it.
    """

    NToolBarAreas = Kee[int](4)

  class ToolButtonStyle(CuteNum):
    """
    The enum 'Qt::ToolButtonStyle' of Qt, with the 5 names Qt gives in it.
    """

    ToolButtonIconOnly = Kee[int](0)
    ToolButtonTextOnly = Kee[int](1)
    ToolButtonTextBesideIcon = Kee[int](2)
    ToolButtonTextUnderIcon = Kee[int](3)
    ToolButtonFollowStyle = Kee[int](4)

  class TouchPointState(CuteFlags):
    """
    The flags enum 'Qt::TouchPointState' of Qt, with the 5 names Qt gives in
    it. Qt names the type of its combinations 'Qt::TouchPointStates'.
    """

    TouchPointUnknownState = 0x0
    TouchPointPressed = 0x1
    TouchPointMoved = 0x2
    TouchPointStationary = 0x4
    TouchPointReleased = 0x8

  TouchPointStates = TouchPointState

  class TransformationMode(CuteNum):
    """
    The enum 'Qt::TransformationMode' of Qt, with the 2 names Qt gives in it.
    """

    FastTransformation = Kee[int](0)
    SmoothTransformation = Kee[int](1)

  class UIEffect(CuteNum):
    """The enum 'Qt::UIEffect' of Qt, with the 7 names Qt gives in it."""

    UI_General = Kee[int](0)
    UI_AnimateMenu = Kee[int](1)
    UI_FadeMenu = Kee[int](2)
    UI_AnimateCombo = Kee[int](3)
    UI_AnimateTooltip = Kee[int](4)
    UI_FadeTooltip = Kee[int](5)
    UI_AnimateToolBox = Kee[int](6)

  class WhiteSpaceMode(CuteNum):
    """
    The enum 'Qt::WhiteSpaceMode' of Qt, with the 4 names Qt gives in it.
    """

    WhiteSpaceNormal = Kee[int](0)
    WhiteSpacePre = Kee[int](1)
    WhiteSpaceNoWrap = Kee[int](2)
    WhiteSpaceModeUndefined = Kee[int](-1)

  class WidgetAttribute(CuteNum):
    """
    The enum 'Qt::WidgetAttribute' of Qt, with the 103 names Qt gives in it.
    """

    WA_Disabled = Kee[int](0)
    WA_UnderMouse = Kee[int](1)
    WA_MouseTracking = Kee[int](2)
    WA_OpaquePaintEvent = Kee[int](4)
    WA_StaticContents = Kee[int](5)
    WA_LaidOut = Kee[int](7)
    WA_PaintOnScreen = Kee[int](8)
    WA_NoSystemBackground = Kee[int](9)
    WA_UpdatesDisabled = Kee[int](10)
    WA_Mapped = Kee[int](11)
    WA_InputMethodEnabled = Kee[int](14)
    WA_WState_Visible = Kee[int](15)
    WA_WState_Hidden = Kee[int](16)
    WA_ForceDisabled = Kee[int](32)
    WA_KeyCompression = Kee[int](33)
    WA_PendingMoveEvent = Kee[int](34)
    WA_PendingResizeEvent = Kee[int](35)
    WA_SetPalette = Kee[int](36)
    WA_SetFont = Kee[int](37)
    WA_SetCursor = Kee[int](38)
    WA_NoChildEventsFromChildren = Kee[int](39)
    WA_WindowModified = Kee[int](41)
    WA_Resized = Kee[int](42)
    WA_Moved = Kee[int](43)
    WA_PendingUpdate = Kee[int](44)
    WA_InvalidSize = Kee[int](45)
    WA_CustomWhatsThis = Kee[int](47)
    WA_LayoutOnEntireRect = Kee[int](48)
    WA_OutsideWSRange = Kee[int](49)
    WA_GrabbedShortcut = Kee[int](50)
    WA_TransparentForMouseEvents = Kee[int](51)
    WA_PaintUnclipped = Kee[int](52)
    WA_SetWindowIcon = Kee[int](53)
    WA_NoMouseReplay = Kee[int](54)
    WA_DeleteOnClose = Kee[int](55)
    WA_RightToLeft = Kee[int](56)
    WA_SetLayoutDirection = Kee[int](57)
    WA_NoChildEventsForParent = Kee[int](58)
    WA_ForceUpdatesDisabled = Kee[int](59)
    WA_WState_Created = Kee[int](60)
    WA_WState_CompressKeys = Kee[int](61)
    WA_WState_InPaintEvent = Kee[int](62)
    WA_WState_Reparented = Kee[int](63)
    WA_WState_ConfigPending = Kee[int](64)
    WA_WState_Polished = Kee[int](66)
    WA_WState_OwnSizePolicy = Kee[int](68)
    WA_WState_ExplicitShowHide = Kee[int](69)
    WA_ShowModal = Kee[int](70)
    WA_MouseNoMask = Kee[int](71)
    WA_NoMousePropagation = Kee[int](73)
    WA_Hover = Kee[int](74)
    WA_InputMethodTransparent = Kee[int](75)
    WA_QuitOnClose = Kee[int](76)
    WA_KeyboardFocusChange = Kee[int](77)
    WA_AcceptDrops = Kee[int](78)
    WA_DropSiteRegistered = Kee[int](79)
    WA_WindowPropagation = Kee[int](80)
    WA_NoX11EventCompression = Kee[int](81)
    WA_TintedBackground = Kee[int](82)
    WA_X11OpenGLOverlay = Kee[int](83)
    WA_AlwaysShowToolTips = Kee[int](84)
    WA_MacOpaqueSizeGrip = Kee[int](85)
    WA_SetStyle = Kee[int](86)
    WA_SetLocale = Kee[int](87)
    WA_MacShowFocusRect = Kee[int](88)
    WA_MacNormalSize = Kee[int](89)
    WA_MacSmallSize = Kee[int](90)
    WA_MacMiniSize = Kee[int](91)
    WA_LayoutUsesWidgetRect = Kee[int](92)
    WA_StyledBackground = Kee[int](93)
    WA_CanHostQMdiSubWindowTitleBar = Kee[int](95)
    WA_MacAlwaysShowToolWindow = Kee[int](96)
    WA_StyleSheet = Kee[int](97)
    WA_ShowWithoutActivating = Kee[int](98)
    WA_X11BypassTransientForHint = Kee[int](99)
    WA_NativeWindow = Kee[int](100)
    WA_DontCreateNativeAncestors = Kee[int](101)
    WA_DontShowOnScreen = Kee[int](103)
    WA_X11NetWmWindowTypeDesktop = Kee[int](104)
    WA_X11NetWmWindowTypeDock = Kee[int](105)
    WA_X11NetWmWindowTypeToolBar = Kee[int](106)
    WA_X11NetWmWindowTypeMenu = Kee[int](107)
    WA_X11NetWmWindowTypeUtility = Kee[int](108)
    WA_X11NetWmWindowTypeSplash = Kee[int](109)
    WA_X11NetWmWindowTypeDialog = Kee[int](110)
    WA_X11NetWmWindowTypeDropDownMenu = Kee[int](111)
    WA_X11NetWmWindowTypePopupMenu = Kee[int](112)
    WA_X11NetWmWindowTypeToolTip = Kee[int](113)
    WA_X11NetWmWindowTypeNotification = Kee[int](114)
    WA_X11NetWmWindowTypeCombo = Kee[int](115)
    WA_X11NetWmWindowTypeDND = Kee[int](116)
    WA_SetWindowModality = Kee[int](118)
    WA_WState_WindowOpacitySet = Kee[int](119)
    WA_TranslucentBackground = Kee[int](120)
    WA_AcceptTouchEvents = Kee[int](121)
    WA_WState_AcceptedTouchBeginEvent = Kee[int](122)
    WA_TouchPadAcceptSingleTouchEvents = Kee[int](123)
    WA_X11DoNotAcceptFocus = Kee[int](126)
    WA_AlwaysStackOnTop = Kee[int](128)
    WA_TabletTracking = Kee[int](129)
    WA_ContentsMarginsRespectsSafeArea = Kee[int](130)
    WA_StyleSheetTarget = Kee[int](131)
    WA_AttributeCount = Kee[int](132)

  class WindowFrameSection(CuteNum):
    """
    The enum 'Qt::WindowFrameSection' of Qt, with the 10 names Qt gives in
    it.
    """

    NoSection = Kee[int](0)
    LeftSection = Kee[int](1)
    TopLeftSection = Kee[int](2)
    TopSection = Kee[int](3)
    TopRightSection = Kee[int](4)
    RightSection = Kee[int](5)
    BottomRightSection = Kee[int](6)
    BottomSection = Kee[int](7)
    BottomLeftSection = Kee[int](8)
    TitleBarArea = Kee[int](9)

  class WindowModality(CuteNum):
    """
    The enum 'Qt::WindowModality' of Qt, with the 3 names Qt gives in it.
    """

    NonModal = Kee[int](0)
    WindowModal = Kee[int](1)
    ApplicationModal = Kee[int](2)

  class WindowState(CuteFlags):
    """
    The flags enum 'Qt::WindowState' of Qt, with the 5 names Qt gives in it.
    Qt names the type of its combinations 'Qt::WindowStates'.
    """

    WindowNoState = 0x0
    WindowMinimized = 0x1
    WindowMaximized = 0x2
    WindowFullScreen = 0x4
    WindowActive = 0x8

  WindowStates = WindowState

  class WindowType(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt::WindowType' of Qt, with the 40 names Qt gives in it.
    Qt names the type of its combinations 'Qt::WindowFlags'.
    """

    Widget = 0x0
    Window = 0x1
    Dialog = 0x3
    Sheet = 0x5
    Drawer = 0x7
    Popup = 0x9
    Tool = 0xb
    ToolTip = 0xd
    SplashScreen = 0xf
    Desktop = 0x11
    SubWindow = 0x12
    ForeignWindow = 0x21
    CoverWindow = 0x41
    WindowType_Mask = 0xff
    MSWindowsFixedSizeDialogHint = 0x100
    MSWindowsOwnDC = 0x200
    BypassWindowManagerHint = 0x400
    X11BypassWindowManagerHint = 0x400
    FramelessWindowHint = 0x800
    WindowTitleHint = 0x1000
    WindowSystemMenuHint = 0x2000
    WindowMinimizeButtonHint = 0x4000
    WindowMaximizeButtonHint = 0x8000
    WindowMinMaxButtonsHint = 0xc000
    WindowContextHelpButtonHint = 0x10000
    WindowShadeButtonHint = 0x20000
    WindowStaysOnTopHint = 0x40000
    WindowTransparentForInput = 0x80000
    WindowOverridesSystemGestures = 0x100000
    WindowDoesNotAcceptFocus = 0x200000
    MaximizeUsingFullscreenGeometryHint = 0x400000
    ExpandedClientAreaHint = 0x400000
    NoTitleBarBackgroundHint = 0x800000
    CustomizeWindowHint = 0x2000000
    WindowStaysOnBottomHint = 0x4000000
    WindowCloseButtonHint = 0x8000000
    MacWindowToolBarButtonHint = 0x10000000
    BypassGraphicsProxyWidget = 0x20000000
    NoDropShadowWindowHint = 0x40000000
    WindowFullscreenButtonHint = 0x80000000

  WindowFlags = WindowType
