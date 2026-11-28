"""
QPlatformTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformtheme.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QKeySequence

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo, QSizeF, QVariant
  from . import QFont, QIcon, QIconEngine, QPalette, QPixmap
  from . import QPlatformDialogHelper, QPlatformMenu, QPlatformMenuBar
  from . import QPlatformMenuItem, QPlatformSystemTrayIcon
  from . import QPlatformThemePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']
  QPlatformThemePrivate = WAIT['QPlatformThemePrivate']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformTheme(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformTheme: a plain Python object standing in
  front of one C++ QPlatformTheme.

  What exists
  -----------

  Every function of Qt's QPlatformTheme that has a ritual and that Python can
  call so far, 25 names in all: 'd_func', 'createPlatformMenuItem',
  'createPlatformMenu', 'createPlatformMenuBar', 'showPlatformMenuBar',
  'usePlatformNativeDialog', 'createPlatformDialogHelper',
  'createPlatformSystemTrayIcon', 'colorScheme', 'palette', 'font',
  'themeHint', 'standardPixmap', 'fileIcon', 'createIconEngine',
  'keyBindings', 'standardButtonText', 'standardButtonShortcut',
  'requestColorScheme', 'contrastPreference', 'motionPreference',
  'defaultThemeHint', 'defaultStandardButtonText', 'removeMnemonics', 'name'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPlatformThemePrivate *QPlatformTheme::d_func() const': takes
    in Python what 'QPlatformThemePrivate *QPlatformTheme::d_func()' takes.
  - Qt's 'QPlatformTheme::~QPlatformTheme()': the destructor: Python never
    removes a C++ QPlatformTheme.

  What has no ritual
  ------------------

  7 of the 36 functions Qt declares: 4 forbidden; 3 not a gap.

  What to expect
  --------------

  - The C++ QPlatformTheme is created at the first use, not by
    'QPlatformTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformTheme.
  """

  #  The enums Qt writes inside QPlatformTheme, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DialogType(CuteNum):
    """
    The enum 'QPlatformTheme::DialogType' of Qt, with the 4 names Qt gives in
    it.
    """

    FileDialog = Kee[int](0)
    ColorDialog = Kee[int](1)
    FontDialog = Kee[int](2)
    MessageDialog = Kee[int](3)

  class Font(CuteNum):
    """
    The enum 'QPlatformTheme::Font' of Qt, with the 28 names Qt gives in it.
    """

    SystemFont = Kee[int](0)
    MenuFont = Kee[int](1)
    MenuBarFont = Kee[int](2)
    MenuItemFont = Kee[int](3)
    MessageBoxFont = Kee[int](4)
    LabelFont = Kee[int](5)
    TipLabelFont = Kee[int](6)
    StatusBarFont = Kee[int](7)
    TitleBarFont = Kee[int](8)
    MdiSubWindowTitleFont = Kee[int](9)
    DockWidgetTitleFont = Kee[int](10)
    PushButtonFont = Kee[int](11)
    CheckBoxFont = Kee[int](12)
    RadioButtonFont = Kee[int](13)
    ToolButtonFont = Kee[int](14)
    ItemViewFont = Kee[int](15)
    ListViewFont = Kee[int](16)
    HeaderViewFont = Kee[int](17)
    ListBoxFont = Kee[int](18)
    ComboMenuItemFont = Kee[int](19)
    ComboLineEditFont = Kee[int](20)
    SmallFont = Kee[int](21)
    MiniFont = Kee[int](22)
    FixedFont = Kee[int](23)
    GroupBoxTitleFont = Kee[int](24)
    TabButtonFont = Kee[int](25)
    EditorFont = Kee[int](26)
    NFonts = Kee[int](27)

  class IconOption(CuteFlags):
    """
    The flags enum 'QPlatformTheme::IconOption' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QPlatformTheme::IconOptions'.
    """

    DontUseCustomDirectoryIcons = 0x1

  IconOptions = IconOption

  class KeyboardSchemes(CuteNum):
    """
    The enum 'QPlatformTheme::KeyboardSchemes' of Qt, with the 6 names Qt
    gives in it.
    """

    WindowsKeyboardScheme = Kee[int](0)
    MacKeyboardScheme = Kee[int](1)
    X11KeyboardScheme = Kee[int](2)
    KdeKeyboardScheme = Kee[int](3)
    GnomeKeyboardScheme = Kee[int](4)
    CdeKeyboardScheme = Kee[int](5)

  class Palette(CuteNum):
    """
    The enum 'QPlatformTheme::Palette' of Qt, with the 19 names Qt gives in
    it.
    """

    SystemPalette = Kee[int](0)
    ToolTipPalette = Kee[int](1)
    ToolButtonPalette = Kee[int](2)
    ButtonPalette = Kee[int](3)
    CheckBoxPalette = Kee[int](4)
    RadioButtonPalette = Kee[int](5)
    HeaderPalette = Kee[int](6)
    ComboBoxPalette = Kee[int](7)
    ItemViewPalette = Kee[int](8)
    MessageBoxLabelPelette = Kee[int](9)
    MessageBoxLabelPalette = Kee[int](9)
    TabBarPalette = Kee[int](10)
    LabelPalette = Kee[int](11)
    GroupBoxPalette = Kee[int](12)
    MenuPalette = Kee[int](13)
    MenuBarPalette = Kee[int](14)
    TextEditPalette = Kee[int](15)
    TextLineEditPalette = Kee[int](16)
    NPalettes = Kee[int](17)

  class StandardPixmap(CuteNum):
    """
    The enum 'QPlatformTheme::StandardPixmap' of Qt, with the 85 names Qt
    gives in it.
    """

    TitleBarMenuButton = Kee[int](0)
    TitleBarMinButton = Kee[int](1)
    TitleBarMaxButton = Kee[int](2)
    TitleBarCloseButton = Kee[int](3)
    TitleBarNormalButton = Kee[int](4)
    TitleBarShadeButton = Kee[int](5)
    TitleBarUnshadeButton = Kee[int](6)
    TitleBarContextHelpButton = Kee[int](7)
    DockWidgetCloseButton = Kee[int](8)
    MessageBoxInformation = Kee[int](9)
    MessageBoxWarning = Kee[int](10)
    MessageBoxCritical = Kee[int](11)
    MessageBoxQuestion = Kee[int](12)
    DesktopIcon = Kee[int](13)
    TrashIcon = Kee[int](14)
    ComputerIcon = Kee[int](15)
    DriveFDIcon = Kee[int](16)
    DriveHDIcon = Kee[int](17)
    DriveCDIcon = Kee[int](18)
    DriveDVDIcon = Kee[int](19)
    DriveNetIcon = Kee[int](20)
    DirOpenIcon = Kee[int](21)
    DirClosedIcon = Kee[int](22)
    DirLinkIcon = Kee[int](23)
    DirLinkOpenIcon = Kee[int](24)
    FileIcon = Kee[int](25)
    FileLinkIcon = Kee[int](26)
    ToolBarHorizontalExtensionButton = Kee[int](27)
    ToolBarVerticalExtensionButton = Kee[int](28)
    FileDialogStart = Kee[int](29)
    FileDialogEnd = Kee[int](30)
    FileDialogToParent = Kee[int](31)
    FileDialogNewFolder = Kee[int](32)
    FileDialogDetailedView = Kee[int](33)
    FileDialogInfoView = Kee[int](34)
    FileDialogContentsView = Kee[int](35)
    FileDialogListView = Kee[int](36)
    FileDialogBack = Kee[int](37)
    DirIcon = Kee[int](38)
    DialogOkButton = Kee[int](39)
    DialogCancelButton = Kee[int](40)
    DialogHelpButton = Kee[int](41)
    DialogOpenButton = Kee[int](42)
    DialogSaveButton = Kee[int](43)
    DialogCloseButton = Kee[int](44)
    DialogApplyButton = Kee[int](45)
    DialogResetButton = Kee[int](46)
    DialogDiscardButton = Kee[int](47)
    DialogYesButton = Kee[int](48)
    DialogNoButton = Kee[int](49)
    ArrowUp = Kee[int](50)
    ArrowDown = Kee[int](51)
    ArrowLeft = Kee[int](52)
    ArrowRight = Kee[int](53)
    ArrowBack = Kee[int](54)
    ArrowForward = Kee[int](55)
    DirHomeIcon = Kee[int](56)
    CommandLink = Kee[int](57)
    VistaShield = Kee[int](58)
    BrowserReload = Kee[int](59)
    BrowserStop = Kee[int](60)
    MediaPlay = Kee[int](61)
    MediaStop = Kee[int](62)
    MediaPause = Kee[int](63)
    MediaSkipForward = Kee[int](64)
    MediaSkipBackward = Kee[int](65)
    MediaSeekForward = Kee[int](66)
    MediaSeekBackward = Kee[int](67)
    MediaVolume = Kee[int](68)
    MediaVolumeMuted = Kee[int](69)
    LineEditClearButton = Kee[int](70)
    DialogYesToAllButton = Kee[int](71)
    DialogNoToAllButton = Kee[int](72)
    DialogSaveAllButton = Kee[int](73)
    DialogAbortButton = Kee[int](74)
    DialogRetryButton = Kee[int](75)
    DialogIgnoreButton = Kee[int](76)
    RestoreDefaultsButton = Kee[int](77)
    TabCloseButton = Kee[int](78)
    TabScrollLeftButton = Kee[int](79)
    TabScrollRightButton = Kee[int](80)
    TabScrollUpButton = Kee[int](81)
    TabScrollDownButton = Kee[int](82)
    NStandardPixmap = Kee[int](83)
    CustomBase = Kee[int](4026531840)

  class ThemeHint(CuteNum):
    """
    The enum 'QPlatformTheme::ThemeHint' of Qt, with the 53 names Qt gives in
    it.
    """

    CursorFlashTime = Kee[int](0)
    KeyboardInputInterval = Kee[int](1)
    MouseDoubleClickInterval = Kee[int](2)
    StartDragDistance = Kee[int](3)
    StartDragTime = Kee[int](4)
    KeyboardAutoRepeatRate = Kee[int](5)
    PasswordMaskDelay = Kee[int](6)
    StartDragVelocity = Kee[int](7)
    TextCursorWidth = Kee[int](8)
    DropShadow = Kee[int](9)
    MaximumScrollBarDragDistance = Kee[int](10)
    ToolButtonStyle = Kee[int](11)
    ToolBarIconSize = Kee[int](12)
    ItemViewActivateItemOnSingleClick = Kee[int](13)
    SystemIconThemeName = Kee[int](14)
    SystemIconFallbackThemeName = Kee[int](15)
    IconThemeSearchPaths = Kee[int](16)
    StyleNames = Kee[int](17)
    WindowAutoPlacement = Kee[int](18)
    DialogButtonBoxLayout = Kee[int](19)
    DialogButtonBoxButtonsHaveIcons = Kee[int](20)
    UseFullScreenForPopupMenu = Kee[int](21)
    KeyboardScheme = Kee[int](22)
    UiEffects = Kee[int](23)
    SpellCheckUnderlineStyle = Kee[int](24)
    TabFocusBehavior = Kee[int](25)
    IconPixmapSizes = Kee[int](26)
    PasswordMaskCharacter = Kee[int](27)
    DialogSnapToDefaultButton = Kee[int](28)
    ContextMenuOnMouseRelease = Kee[int](29)
    MousePressAndHoldInterval = Kee[int](30)
    MouseDoubleClickDistance = Kee[int](31)
    WheelScrollLines = Kee[int](32)
    TouchDoubleTapDistance = Kee[int](33)
    ShowShortcutsInContextMenus = Kee[int](34)
    IconFallbackSearchPaths = Kee[int](35)
    MouseQuickSelectionThreshold = Kee[int](36)
    InteractiveResizeAcrossScreens = Kee[int](37)
    ShowDirectoriesFirst = Kee[int](38)
    PreselectFirstFileInDirectory = Kee[int](39)
    ButtonPressKeys = Kee[int](40)
    SetFocusOnTouchRelease = Kee[int](41)
    FlickStartDistance = Kee[int](42)
    FlickMaximumVelocity = Kee[int](43)
    FlickDeceleration = Kee[int](44)
    MenuBarFocusOnAltPressRelease = Kee[int](45)
    MouseCursorTheme = Kee[int](46)
    MouseCursorSize = Kee[int](47)
    UnderlineShortcut = Kee[int](48)
    ShowIconsInMenus = Kee[int](49)
    PreferFileIconFromTheme = Kee[int](50)
    MenuSelectionWraps = Kee[int](51)
    ScrollSingleStepDistance = Kee[int](52)

  class UiEffect(CuteNum):
    """
    The enum 'QPlatformTheme::UiEffect' of Qt, with the 8 names Qt gives in
    it.
    """

    GeneralUiEffect = Kee[int](1)
    AnimateMenuUiEffect = Kee[int](2)
    FadeMenuUiEffect = Kee[int](4)
    AnimateComboUiEffect = Kee[int](8)
    AnimateTooltipUiEffect = Kee[int](16)
    FadeTooltipUiEffect = Kee[int](32)
    AnimateToolBoxUiEffect = Kee[int](64)
    HoverEffect = Kee[int](128)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(ThemeHint)
  def defaultThemeHint(hint: ThemeHint) -> QVariant:
    """
    Calls Qt's 'QVariant QPlatformTheme::defaultThemeHint(ThemeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#defaultThemeHint

    Parameters
    ----------

    hint : ThemeHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlatformTheme::defaultThemeHint(ThemeHint hint)
    address = Rituals.call(
        'ritual_ZN14QPlatformTheme16defaultThemeHintENS_9ThemeHintE',
        hint.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(int)
  def defaultStandardButtonText(button: int) -> str:
    """
    Calls Qt's 'QString QPlatformTheme::defaultStandardButtonText(int
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#defaultStandardButtonText

    Parameters
    ----------

    button : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformTheme::defaultStandardButtonText(int button)
    return Rituals.call(
        'ritual_ZN14QPlatformTheme25defaultStandardButtonTextEi', button,
    )

  @staticmethod
  @overload(str)
  def removeMnemonics(original: str) -> str:
    """
    Calls Qt's 'QString QPlatformTheme::removeMnemonics(const QString
    &original)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#removeMnemonics

    Parameters
    ----------

    original : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformTheme::removeMnemonics(const QString &original)
    return Rituals.call(
        'ritual_ZN14QPlatformTheme15removeMnemonicsERK7QString', original,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformTheme'

  #  A C++ QPlatformTheme Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformTheme'

  #  The functions Qt calls itself that QPlatformTheme is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'keyBindings': (
          'QList<QKeySequence> '
          'QPlatformTheme::keyBindings(QKeySequence::StandardKey) const',
      ),
  }

  #  The functions Qt calls itself that QPlatformTheme is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createPlatformMenuItem': (
          ('_ZNK14QPlatformTheme22createPlatformMenuItemEv',
           ('address', 'address', 'QtGui:QPlatformMenuItem'),
           ()),
      ),
      'createPlatformMenu': (
          ('_ZNK14QPlatformTheme18createPlatformMenuEv',
           ('address', 'address', 'QtGui:QPlatformMenu'),
           ()),
      ),
      'createPlatformMenuBar': (
          ('_ZNK14QPlatformTheme21createPlatformMenuBarEv',
           ('address', 'address', 'QtGui:QPlatformMenuBar'),
           ()),
      ),
      'showPlatformMenuBar': (
          ('_ZN14QPlatformTheme19showPlatformMenuBarEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'usePlatformNativeDialog': (
          ('_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTypeE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPlatformTheme.DialogType'),
           )),
      ),
      'createPlatformDialogHelper': (
          ('_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10DialogTyp'
           'eE',
           ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           (
               ('int', 'enum', 'QtGui:QPlatformTheme.DialogType'),
           )),
      ),
      'createPlatformSystemTrayIcon': (
          ('_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv',
           ('address', 'address', 'QtGui:QPlatformSystemTrayIcon'),
           ()),
      ),
      'colorScheme': (
          ('_ZNK14QPlatformTheme11colorSchemeEv',
           ('int', 'enum', 'QtCore:Qt.ColorScheme'),
           ()),
      ),
      'palette': (
          ('_ZNK14QPlatformTheme7paletteENS_7PaletteE',
           ('address', 'address', 'QtGui:QPalette'),
           (
               ('int', 'enum', 'QtGui:QPlatformTheme.Palette'),
           )),
      ),
      'font': (
          ('_ZNK14QPlatformTheme4fontENS_4FontE',
           ('address', 'address', 'QtGui:QFont'),
           (
               ('int', 'enum', 'QtGui:QPlatformTheme.Font'),
           )),
      ),
      'themeHint': (
          ('_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtGui:QPlatformTheme.ThemeHint'),
           )),
      ),
      'standardPixmap': (
          ('_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixmapERK6QSi'
           'zeF',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtGui:QPlatformTheme.StandardPixmap'),
               ('address', 'value', 'QtCore:QSizeF'),
           )),
      ),
      'fileIcon': (
          ('_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_10IconOpti'
           'onEE',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('address', 'value', 'QtCore:QFileInfo'),
               ('int', 'flags', 'QtGui:QPlatformTheme.IconOption'),
           )),
      ),
      'createIconEngine': (
          ('_ZNK14QPlatformTheme16createIconEngineERK7QString',
           ('address', 'address', 'QtGui:QIconEngine'),
           (
               ('address', 'text', ''),
           )),
      ),
      'standardButtonText': (
          ('_ZNK14QPlatformTheme18standardButtonTextEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'standardButtonShortcut': (
          ('_ZNK14QPlatformTheme22standardButtonShortcutEi',
           ('address', 'value', 'QtGui:QKeySequence'),
           (
               ('int', 'number', ''),
           )),
      ),
      'requestColorScheme': (
          ('_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSchemeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.ColorScheme'),
           )),
      ),
      'contrastPreference': (
          ('_ZNK14QPlatformTheme18contrastPreferenceEv',
           ('int', 'enum', 'QtCore:Qt.ContrastPreference'),
           ()),
      ),
      'motionPreference': (
          ('_ZNK14QPlatformTheme16motionPreferenceEv',
           ('int', 'enum', 'QtCore:Qt.MotionPreference'),
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

  def createPlatformMenuItem(self) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#createPlatformMenuItem

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QPlatformTheme::createPlatformMenuItem() const
    ritual = 'ritual_ZNK14QPlatformTheme22createPlatformMenuItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme22createPlatformMenuItemEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  def createPlatformMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QPlatformTheme::createPlatformMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#createPlatformMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QPlatformTheme::createPlatformMenu() const
    ritual = 'ritual_ZNK14QPlatformTheme18createPlatformMenuEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme18createPlatformMenuEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def createPlatformMenuBar(self) -> Optional[QPlatformMenuBar]:
    """
    Calls Qt's 'QPlatformMenuBar *QPlatformTheme::createPlatformMenuBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#createPlatformMenuBar

    Returns
    -------

    Optional[QPlatformMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuBar *QPlatformTheme::createPlatformMenuBar() const
    ritual = 'ritual_ZNK14QPlatformTheme21createPlatformMenuBarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme21createPlatformMenuBarEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenuBar
    return QPlatformMenuBar._cuteAt(address)

  @overload(DialogType)
  def usePlatformNativeDialog(self, type: DialogType) -> bool:
    """
    Calls Qt's 'bool QPlatformTheme::usePlatformNativeDialog(DialogType type)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#usePlatformNativeDialog

    Parameters
    ----------

    type : DialogType
      Passed on as its number.
    """
    #  bool QPlatformTheme::usePlatformNativeDialog(DialogType type) const
    ritual = (
        'ritual_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10DialogTyp'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlatformTheme23usePlatformNativeDialogENS_10Dia'
          'logTypeE')
    return self.uglySide.call(ritual, type.value)

  @overload(DialogType)
  def createPlatformDialogHelper(
      self,
      type: DialogType,
  ) -> Optional[QPlatformDialogHelper]:
    """
    Calls Qt's 'QPlatformDialogHelper
    *QPlatformTheme::createPlatformDialogHelper(DialogType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#createPlatformDialogHelper

    Parameters
    ----------

    type : DialogType
      Passed on as its number.

    Returns
    -------

    Optional[QPlatformDialogHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformDialogHelper
    #      *QPlatformTheme::createPlatformDialogHelper(DialogType type) const
    ritual = (
        'ritual_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10Dialog'
        'TypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlatformTheme26createPlatformDialogHelperENS_10'
          'DialogTypeE')
    address = self.uglySide.call(ritual, type.value)
    from . import QPlatformDialogHelper
    return QPlatformDialogHelper._cuteAt(address)

  def createPlatformSystemTrayIcon(
      self,
  ) -> Optional[QPlatformSystemTrayIcon]:
    """
    Calls Qt's 'QPlatformSystemTrayIcon
    *QPlatformTheme::createPlatformSystemTrayIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#createPlatformSystemTrayIcon

    Returns
    -------

    Optional[QPlatformSystemTrayIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSystemTrayIcon
    #      *QPlatformTheme::createPlatformSystemTrayIcon() const
    ritual = 'ritual_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlatformTheme28createPlatformSystemTrayIconEv')
    address = self.uglySide.call(ritual)
    from . import QPlatformSystemTrayIcon
    return QPlatformSystemTrayIcon._cuteAt(address)

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QPlatformTheme::colorScheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QPlatformTheme::colorScheme() const
    ritual = 'ritual_ZNK14QPlatformTheme11colorSchemeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme11colorSchemeEv'
    return Qt.ColorScheme(self.uglySide.call(ritual))

  @overload()
  @overload(Palette)
  def palette(
      self,
      type: Palette = Palette.SystemPalette,
  ) -> Optional[QPalette]:
    """
    Calls Qt's 'const QPalette *QPlatformTheme::palette(Palette type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#palette

    Parameters
    ----------

    type : Palette
      Passed on as its number. May be left out, as in Qt: it is then
      Palette.SystemPalette.

    Returns
    -------

    Optional[QPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPalette *QPlatformTheme::palette(Palette type) const
    ritual = 'ritual_ZNK14QPlatformTheme7paletteENS_7PaletteE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme7paletteENS_7PaletteE'
    address = self.uglySide.call(ritual, type.value)
    from . import QPalette
    return QPalette._cuteAt(address)

  @overload()
  @overload(Font)
  def font(self, type: Font = Font.SystemFont) -> Optional[QFont]:
    """
    Calls Qt's 'const QFont *QPlatformTheme::font(Font type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#font

    Parameters
    ----------

    type : Font
      Passed on as its number. May be left out, as in Qt: it is then
      Font.SystemFont.

    Returns
    -------

    Optional[QFont]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QFont *QPlatformTheme::font(Font type) const
    ritual = 'ritual_ZNK14QPlatformTheme4fontENS_4FontE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme4fontENS_4FontE'
    address = self.uglySide.call(ritual, type.value)
    from . import QFont
    return QFont._cuteAt(address)

  @overload(ThemeHint)
  def themeHint(self, hint: ThemeHint) -> QVariant:
    """
    Calls Qt's 'QVariant QPlatformTheme::themeHint(ThemeHint hint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#themeHint

    Parameters
    ----------

    hint : ThemeHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlatformTheme::themeHint(ThemeHint hint) const
    ritual = 'ritual_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme9themeHintENS_9ThemeHintE'
    address = self.uglySide.call(ritual, hint.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(StandardPixmap, QSizeF)
  def standardPixmap(self, sp: StandardPixmap, size: QSizeF) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPlatformTheme::standardPixmap(StandardPixmap sp,
    const QSizeF &size) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#standardPixmap

    Parameters
    ----------

    sp : StandardPixmap
      Passed on as its number.

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPlatformTheme::standardPixmap(StandardPixmap sp, const QSizeF
    #      &size) const
    ritual = (
        'ritual_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixmapERK6'
        'QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlatformTheme14standardPixmapENS_14StandardPixm'
          'apERK6QSizeF')
    address = self.uglySide.call(ritual, sp.value, self._valueOf(size))
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QFileInfo)
  @overload(QFileInfo, IconOptions)
  def fileIcon(
      self,
      fileInfo: QFileInfo,
      iconOptions: IconOptions = IconOptions(),
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QPlatformTheme::fileIcon(const QFileInfo &fileInfo,
    QPlatformTheme::IconOptions iconOptions) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#fileIcon

    Parameters
    ----------

    fileInfo : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    iconOptions : IconOptions
      Passed on as its number. May be left out, as in Qt: it is then
      IconOptions().

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QPlatformTheme::fileIcon(const QFileInfo &fileInfo,
    #      QPlatformTheme::IconOptions iconOptions) const
    ritual = (
        'ritual_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_10IconO'
        'ptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlatformTheme8fileIconERK9QFileInfo6QFlagsINS_1'
          '0IconOptionEE')
    address = self.uglySide.call(
        ritual, self._valueOf(fileInfo), iconOptions.value,
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(str)
  def createIconEngine(self, iconName: str) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QPlatformTheme::createIconEngine(const QString
    &iconName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#createIconEngine

    Parameters
    ----------

    iconName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QPlatformTheme::createIconEngine(const QString &iconName)
    #      const
    ritual = 'ritual_ZNK14QPlatformTheme16createIconEngineERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme16createIconEngineERK7QString'
    address = self.uglySide.call(ritual, iconName)
    from . import QIconEngine
    return QIconEngine._cuteAt(address)

  @overload(QKeySequence.StandardKey)
  def keyBindings(
      self,
      key: QKeySequence.StandardKey,
  ) -> QList[QKeySequence]:
    """
    Calls Qt's 'QList<QKeySequence>
    QPlatformTheme::keyBindings(QKeySequence::StandardKey key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#keyBindings

    Parameters
    ----------

    key : QKeySequence.StandardKey
      Passed on as its number.

    Returns
    -------

    QList[QKeySequence]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeySequence>
    #      QPlatformTheme::keyBindings(QKeySequence::StandardKey key) const
    address = self.uglySide.call(
        'ritual_ZNK14QPlatformTheme11keyBindingsEN12QKeySequence11StandardK'
        'eyE',
        key.value,
    )
    return QList[QKeySequence]._cuteOwning(address)

  @overload(int)
  def standardButtonText(self, button: int) -> str:
    """
    Calls Qt's 'QString QPlatformTheme::standardButtonText(int button)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#standardButtonText

    Parameters
    ----------

    button : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformTheme::standardButtonText(int button) const
    ritual = 'ritual_ZNK14QPlatformTheme18standardButtonTextEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme18standardButtonTextEi'
    return self.uglySide.call(ritual, button)

  @overload(int)
  def standardButtonShortcut(self, button: int) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QPlatformTheme::standardButtonShortcut(int
    button) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#standardButtonShortcut

    Parameters
    ----------

    button : int
      Passed on as it is.

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QPlatformTheme::standardButtonShortcut(int button) const
    ritual = 'ritual_ZNK14QPlatformTheme22standardButtonShortcutEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme22standardButtonShortcutEi'
    address = self.uglySide.call(ritual, button)
    return QKeySequence._cuteOwning(address)

  def contrastPreference(self) -> Qt.ContrastPreference:
    """
    Calls Qt's 'Qt::ContrastPreference QPlatformTheme::contrastPreference()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#contrastPreference

    Returns
    -------

    Qt.ContrastPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ContrastPreference(number)' gives.
    """
    #  Qt::ContrastPreference QPlatformTheme::contrastPreference() const
    ritual = 'ritual_ZNK14QPlatformTheme18contrastPreferenceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme18contrastPreferenceEv'
    return Qt.ContrastPreference(self.uglySide.call(ritual))

  def motionPreference(self) -> Qt.MotionPreference:
    """
    Calls Qt's 'Qt::MotionPreference QPlatformTheme::motionPreference()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#motionPreference

    Returns
    -------

    Qt.MotionPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MotionPreference(number)' gives.
    """
    #  Qt::MotionPreference QPlatformTheme::motionPreference() const
    ritual = 'ritual_ZNK14QPlatformTheme16motionPreferenceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPlatformTheme16motionPreferenceEv'
    return Qt.MotionPreference(self.uglySide.call(ritual))

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlatformTheme::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformTheme::name() const
    return self.uglySide.call('ritual_ZNK14QPlatformTheme4nameEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPlatformTheme::QPlatformTheme()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#QPlatformTheme
    """
    #  QPlatformTheme::QPlatformTheme()
    self._noteCreation(QPlatformTheme, lambda: Rituals.call(
        'ritual_ZN14QPlatformThemeC1Ev',
    ))

  @overload(QPlatformThemePrivate)
  @overload(NoneType)
  def __init__(self, priv: Optional[QPlatformThemePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformTheme::QPlatformTheme(QPlatformThemePrivate *priv)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#QPlatformTheme

    Parameters
    ----------

    priv : Optional[QPlatformThemePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformTheme::QPlatformTheme(QPlatformThemePrivate *priv)
    self._noteCreation(QPlatformTheme, lambda: Rituals.call(
        'ritual_ZN14QPlatformThemeC1EP21QPlatformThemePrivate',
        self._addressOf(priv),
    ))

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

  def d_func(self) -> Optional[QPlatformThemePrivate]:
    """
    Calls Qt's 'QPlatformThemePrivate *QPlatformTheme::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtheme.html#d_func

    Returns
    -------

    Optional[QPlatformThemePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformThemePrivate *QPlatformTheme::d_func()
    address = self.uglySide.call('ritual_ZN14QPlatformTheme6d_funcEv')
    from . import QPlatformThemePrivate
    return QPlatformThemePrivate._cuteAt(address)

  def showPlatformMenuBar(self) -> None:
    """
    Calls Qt's 'void QPlatformTheme::showPlatformMenuBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#showPlatformMenuBar
    """
    #  void QPlatformTheme::showPlatformMenuBar()
    ritual = 'ritual_ZN14QPlatformTheme19showPlatformMenuBarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlatformTheme19showPlatformMenuBarEv'
    self.uglySide.call(ritual)

  @overload(Qt.ColorScheme)
  def requestColorScheme(self, scheme: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void QPlatformTheme::requestColorScheme(Qt::ColorScheme
    scheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtheme.html#requestColorScheme

    Parameters
    ----------

    scheme : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QPlatformTheme::requestColorScheme(Qt::ColorScheme scheme)
    ritual = (
        'ritual_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSchemeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlatformTheme18requestColorSchemeEN2Qt11ColorSch'
          'emeE')
    self.uglySide.call(ritual, scheme.value)
