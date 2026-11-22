"""
QIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qicon.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QIconEngine, QPainter, QPixmap, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIconEngine = WAIT['QIconEngine']
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIcon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIcon: a plain Python object standing in front of one
  C++ QIcon.

  C++ hands a QIcon around as a copy, so every C++ QIcon behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QIcon that has a ritual and that Python can call so
  far, 23 names in all: 'pixmap', 'actualSize', 'name', 'paint', 'isNull',
  'isDetached', 'detach', 'cacheKey', 'addPixmap', 'addFile',
  'availableSizes', 'setIsMask', 'isMask', 'fromTheme', 'hasThemeIcon',
  'themeSearchPaths', 'setThemeSearchPaths', 'fallbackSearchPaths',
  'setFallbackSearchPaths', 'themeName', 'setThemeName', 'fallbackThemeName',
  'setFallbackThemeName'. It can be made from Python, in 5 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIcon::~QIcon()': the destructor: Python removes its C++ QIcon by
    it, and has no other use for it.
  - Qt's 'QVariant QIcon::operator QVariant() const': an operator Python has
    no name for.

  What has no ritual
  ------------------

  12 of the 52 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 declared and nowhere to be found; 1 a template;
  1 private.

  What to expect
  --------------

  - The C++ QIcon is created at the first use, not by 'QIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QIcon back gives a copy the ritual made for Python,
    in a new cute QIcon.
  """

  #  The enums Qt writes inside QIcon, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """The enum 'QIcon::Mode' of Qt, with the 4 names Qt gives in it."""

    Normal = Kee[int](0)
    Disabled = Kee[int](1)
    Active = Kee[int](2)
    Selected = Kee[int](3)

  class State(CuteNum):
    """The enum 'QIcon::State' of Qt, with the 2 names Qt gives in it."""

    On = Kee[int](0)
    Off = Kee[int](1)

  class ThemeIcon(CuteNum, scoped=True):
    """
    The enum 'QIcon::ThemeIcon' of Qt, with the 151 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    AddressBookNew = Kee[int](0)
    ApplicationExit = Kee[int](1)
    AppointmentNew = Kee[int](2)
    CallStart = Kee[int](3)
    CallStop = Kee[int](4)
    ContactNew = Kee[int](5)
    DocumentNew = Kee[int](6)
    DocumentOpen = Kee[int](7)
    DocumentOpenRecent = Kee[int](8)
    DocumentPageSetup = Kee[int](9)
    DocumentPrint = Kee[int](10)
    DocumentPrintPreview = Kee[int](11)
    DocumentProperties = Kee[int](12)
    DocumentRevert = Kee[int](13)
    DocumentSave = Kee[int](14)
    DocumentSaveAs = Kee[int](15)
    DocumentSend = Kee[int](16)
    EditClear = Kee[int](17)
    EditCopy = Kee[int](18)
    EditCut = Kee[int](19)
    EditDelete = Kee[int](20)
    EditFind = Kee[int](21)
    EditPaste = Kee[int](22)
    EditRedo = Kee[int](23)
    EditSelectAll = Kee[int](24)
    EditUndo = Kee[int](25)
    FolderNew = Kee[int](26)
    FormatIndentLess = Kee[int](27)
    FormatIndentMore = Kee[int](28)
    FormatJustifyCenter = Kee[int](29)
    FormatJustifyFill = Kee[int](30)
    FormatJustifyLeft = Kee[int](31)
    FormatJustifyRight = Kee[int](32)
    FormatTextDirectionLtr = Kee[int](33)
    FormatTextDirectionRtl = Kee[int](34)
    FormatTextBold = Kee[int](35)
    FormatTextItalic = Kee[int](36)
    FormatTextUnderline = Kee[int](37)
    FormatTextStrikethrough = Kee[int](38)
    GoDown = Kee[int](39)
    GoHome = Kee[int](40)
    GoNext = Kee[int](41)
    GoPrevious = Kee[int](42)
    GoUp = Kee[int](43)
    HelpAbout = Kee[int](44)
    HelpFaq = Kee[int](45)
    InsertImage = Kee[int](46)
    InsertLink = Kee[int](47)
    InsertText = Kee[int](48)
    ListAdd = Kee[int](49)
    ListRemove = Kee[int](50)
    MailForward = Kee[int](51)
    MailMarkImportant = Kee[int](52)
    MailMarkRead = Kee[int](53)
    MailMarkUnread = Kee[int](54)
    MailMessageNew = Kee[int](55)
    MailReplyAll = Kee[int](56)
    MailReplySender = Kee[int](57)
    MailSend = Kee[int](58)
    MediaEject = Kee[int](59)
    MediaPlaybackPause = Kee[int](60)
    MediaPlaybackStart = Kee[int](61)
    MediaPlaybackStop = Kee[int](62)
    MediaRecord = Kee[int](63)
    MediaSeekBackward = Kee[int](64)
    MediaSeekForward = Kee[int](65)
    MediaSkipBackward = Kee[int](66)
    MediaSkipForward = Kee[int](67)
    ObjectRotateLeft = Kee[int](68)
    ObjectRotateRight = Kee[int](69)
    ProcessStop = Kee[int](70)
    SystemLockScreen = Kee[int](71)
    SystemLogOut = Kee[int](72)
    SystemSearch = Kee[int](73)
    SystemReboot = Kee[int](74)
    SystemShutdown = Kee[int](75)
    ToolsCheckSpelling = Kee[int](76)
    ViewFullscreen = Kee[int](77)
    ViewRefresh = Kee[int](78)
    ViewRestore = Kee[int](79)
    WindowClose = Kee[int](80)
    WindowNew = Kee[int](81)
    ZoomFitBest = Kee[int](82)
    ZoomIn = Kee[int](83)
    ZoomOut = Kee[int](84)
    AudioCard = Kee[int](85)
    AudioInputMicrophone = Kee[int](86)
    Battery = Kee[int](87)
    CameraPhoto = Kee[int](88)
    CameraVideo = Kee[int](89)
    CameraWeb = Kee[int](90)
    Computer = Kee[int](91)
    DriveHarddisk = Kee[int](92)
    DriveOptical = Kee[int](93)
    InputGaming = Kee[int](94)
    InputKeyboard = Kee[int](95)
    InputMouse = Kee[int](96)
    InputTablet = Kee[int](97)
    MediaFlash = Kee[int](98)
    MediaOptical = Kee[int](99)
    MediaTape = Kee[int](100)
    MultimediaPlayer = Kee[int](101)
    NetworkWired = Kee[int](102)
    NetworkWireless = Kee[int](103)
    Phone = Kee[int](104)
    Printer = Kee[int](105)
    Scanner = Kee[int](106)
    VideoDisplay = Kee[int](107)
    AppointmentMissed = Kee[int](108)
    AppointmentSoon = Kee[int](109)
    AudioVolumeHigh = Kee[int](110)
    AudioVolumeLow = Kee[int](111)
    AudioVolumeMedium = Kee[int](112)
    AudioVolumeMuted = Kee[int](113)
    BatteryCaution = Kee[int](114)
    BatteryLow = Kee[int](115)
    DialogError = Kee[int](116)
    DialogInformation = Kee[int](117)
    DialogPassword = Kee[int](118)
    DialogQuestion = Kee[int](119)
    DialogWarning = Kee[int](120)
    FolderDragAccept = Kee[int](121)
    FolderOpen = Kee[int](122)
    FolderVisiting = Kee[int](123)
    ImageLoading = Kee[int](124)
    ImageMissing = Kee[int](125)
    MailAttachment = Kee[int](126)
    MailUnread = Kee[int](127)
    MailRead = Kee[int](128)
    MailReplied = Kee[int](129)
    MediaPlaylistRepeat = Kee[int](130)
    MediaPlaylistShuffle = Kee[int](131)
    NetworkOffline = Kee[int](132)
    PrinterPrinting = Kee[int](133)
    SecurityHigh = Kee[int](134)
    SecurityLow = Kee[int](135)
    SoftwareUpdateAvailable = Kee[int](136)
    SoftwareUpdateUrgent = Kee[int](137)
    SyncError = Kee[int](138)
    SyncSynchronizing = Kee[int](139)
    UserAvailable = Kee[int](140)
    UserOffline = Kee[int](141)
    WeatherClear = Kee[int](142)
    WeatherClearNight = Kee[int](143)
    WeatherFewClouds = Kee[int](144)
    WeatherFewCloudsNight = Kee[int](145)
    WeatherFog = Kee[int](146)
    WeatherShowers = Kee[int](147)
    WeatherSnow = Kee[int](148)
    WeatherStorm = Kee[int](149)
    NThemeIcons = Kee[int](150)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromTheme(name: str) -> QIcon:
    """
    Calls Qt's 'QIcon QIcon::fromTheme(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#fromTheme

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QIcon::fromTheme(const QString &name)
    address = Rituals.call('ritual_ZN5QIcon9fromThemeERK7QString', name)
    return QIcon._cuteOwning(address)

  @staticmethod
  @overload(str, THIS)
  def fromTheme(name: str, fallback: QIcon) -> QIcon:
    """
    Calls Qt's 'QIcon QIcon::fromTheme(const QString &name, const QIcon
    &fallback)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#fromTheme

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    fallback : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QIcon::fromTheme(const QString &name, const QIcon &fallback)
    address = Rituals.call(
        'ritual_ZN5QIcon9fromThemeERK7QStringRKS_',
        name, CuteMixin._valueOf(fallback),
    )
    return QIcon._cuteOwning(address)

  @staticmethod
  @overload(ThemeIcon)
  def fromTheme(icon: ThemeIcon) -> QIcon:
    """
    Calls Qt's 'QIcon QIcon::fromTheme(ThemeIcon icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#fromTheme

    Parameters
    ----------

    icon : ThemeIcon
      Passed on as its number.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QIcon::fromTheme(ThemeIcon icon)
    address = Rituals.call(
        'ritual_ZN5QIcon9fromThemeENS_9ThemeIconE', icon.value,
    )
    return QIcon._cuteOwning(address)

  @staticmethod
  @overload(ThemeIcon, THIS)
  def fromTheme(icon: ThemeIcon, fallback: QIcon) -> QIcon:
    """
    Calls Qt's 'QIcon QIcon::fromTheme(ThemeIcon icon, const QIcon
    &fallback)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#fromTheme

    Parameters
    ----------

    icon : ThemeIcon
      Passed on as its number.

    fallback : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QIcon::fromTheme(ThemeIcon icon, const QIcon &fallback)
    address = Rituals.call(
        'ritual_ZN5QIcon9fromThemeENS_9ThemeIconERKS_',
        icon.value, CuteMixin._valueOf(fallback),
    )
    return QIcon._cuteOwning(address)

  @staticmethod
  @overload(str)
  def hasThemeIcon(name: str) -> bool:
    """
    Calls Qt's 'bool QIcon::hasThemeIcon(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#hasThemeIcon

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QIcon::hasThemeIcon(const QString &name)
    return Rituals.call('ritual_ZN5QIcon12hasThemeIconERK7QString', name)

  @staticmethod
  @overload(ThemeIcon)
  def hasThemeIcon(icon: ThemeIcon) -> bool:
    """
    Calls Qt's 'bool QIcon::hasThemeIcon(ThemeIcon icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#hasThemeIcon

    Parameters
    ----------

    icon : ThemeIcon
      Passed on as its number.
    """
    #  bool QIcon::hasThemeIcon(ThemeIcon icon)
    return Rituals.call(
        'ritual_ZN5QIcon12hasThemeIconENS_9ThemeIconE', icon.value,
    )

  @staticmethod
  def themeSearchPaths() -> QStringList:
    """
    Calls Qt's 'QStringList QIcon::themeSearchPaths()'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#themeSearchPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QIcon::themeSearchPaths()
    address = Rituals.call('ritual_ZN5QIcon16themeSearchPathsEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QStringList)
  def setThemeSearchPaths(searchpath: QStringList) -> None:
    """
    Calls Qt's 'void QIcon::setThemeSearchPaths(const QStringList
    &searchpath)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#setThemeSearchPaths

    Parameters
    ----------

    searchpath : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QIcon::setThemeSearchPaths(const QStringList &searchpath)
    Rituals.call(
        'ritual_ZN5QIcon19setThemeSearchPathsERK5QListI7QStringE',
        CuteMixin._valueOf(searchpath),
    )

  @staticmethod
  def fallbackSearchPaths() -> QStringList:
    """
    Calls Qt's 'QStringList QIcon::fallbackSearchPaths()'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#fallbackSearchPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QIcon::fallbackSearchPaths()
    address = Rituals.call('ritual_ZN5QIcon19fallbackSearchPathsEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QStringList)
  def setFallbackSearchPaths(paths: QStringList) -> None:
    """
    Calls Qt's 'void QIcon::setFallbackSearchPaths(const QStringList
    &paths)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#setFallbackSearchPaths

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QIcon::setFallbackSearchPaths(const QStringList &paths)
    Rituals.call(
        'ritual_ZN5QIcon22setFallbackSearchPathsERK5QListI7QStringE',
        CuteMixin._valueOf(paths),
    )

  @staticmethod
  def themeName() -> str:
    """
    Calls Qt's 'QString QIcon::themeName()'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#themeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIcon::themeName()
    return Rituals.call('ritual_ZN5QIcon9themeNameEv')

  @staticmethod
  @overload(str)
  def setThemeName(path: str) -> None:
    """
    Calls Qt's 'void QIcon::setThemeName(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#setThemeName

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QIcon::setThemeName(const QString &path)
    Rituals.call('ritual_ZN5QIcon12setThemeNameERK7QString', path)

  @staticmethod
  def fallbackThemeName() -> str:
    """
    Calls Qt's 'QString QIcon::fallbackThemeName()'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#fallbackThemeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIcon::fallbackThemeName()
    return Rituals.call('ritual_ZN5QIcon17fallbackThemeNameEv')

  @staticmethod
  @overload(str)
  def setFallbackThemeName(name: str) -> None:
    """
    Calls Qt's 'void QIcon::setFallbackThemeName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#setFallbackThemeName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QIcon::setFallbackThemeName(const QString &name)
    Rituals.call('ritual_ZN5QIcon20setFallbackThemeNameERK7QString', name)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIcon'

  #  Qt's '~QIcon()'. Naming it makes this a value class: Python owns every
  #  C++ QIcon behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QIconD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  @overload(QSize, Mode)
  @overload(QSize, Mode, State)
  def pixmap(
      self,
      size: QSize,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIcon::pixmap(const QSize &size, Mode mode, State
    state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#pixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QIcon::pixmap(const QSize &size, Mode mode, State state) const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon6pixmapERK5QSizeNS_4ModeENS_5StateE',
        self._valueOf(size), mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, Mode)
  @overload(int, int, Mode, State)
  def pixmap(
      self,
      w: int,
      h: int,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIcon::pixmap(int w, int h, Mode mode, State state)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#pixmap

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QIcon::pixmap(int w, int h, Mode mode, State state) const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon6pixmapEiiNS_4ModeENS_5StateE',
        w, h, mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(int)
  @overload(int, Mode)
  @overload(int, Mode, State)
  def pixmap(
      self,
      extent: int,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIcon::pixmap(int extent, Mode mode, State state)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#pixmap

    Parameters
    ----------

    extent : int
      Passed on as it is.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QIcon::pixmap(int extent, Mode mode, State state) const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon6pixmapEiNS_4ModeENS_5StateE',
        extent, mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSize, float)
  @overload(QSize, float, Mode)
  @overload(QSize, float, Mode, State)
  def pixmap(
      self,
      size: QSize,
      devicePixelRatio: float,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIcon::pixmap(const QSize &size, qreal
    devicePixelRatio, Mode mode, State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#pixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    devicePixelRatio : float
      Passed on as it is.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QIcon::pixmap(const QSize &size, qreal devicePixelRatio, Mode
    #      mode, State state) const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon6pixmapERK5QSizedNS_4ModeENS_5StateE',
        self._valueOf(size), devicePixelRatio, mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QWindow, QSize)
  @overload(NoneType, QSize)
  @overload(QWindow, QSize, Mode)
  @overload(NoneType, QSize, Mode)
  @overload(QWindow, QSize, Mode, State)
  @overload(NoneType, QSize, Mode, State)
  def pixmap(
      self,
      window: Optional[QWindow],
      size: QSize,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIcon::pixmap(QWindow *window, const QSize &size,
    Mode mode, State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#pixmap

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QIcon::pixmap(QWindow *window, const QSize &size, Mode mode,
    #      State state) const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon6pixmapEP7QWindowRK5QSizeNS_4ModeENS_5StateE',
        self._addressOf(window), self._valueOf(size), mode.value,
        state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSize)
  @overload(QSize, Mode)
  @overload(QSize, Mode, State)
  def actualSize(
      self,
      size: QSize,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QSize:
    """
    Calls Qt's 'QSize QIcon::actualSize(const QSize &size, Mode mode, State
    state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#actualSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QIcon::actualSize(const QSize &size, Mode mode, State state)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon10actualSizeERK5QSizeNS_4ModeENS_5StateE',
        self._valueOf(size), mode.value, state.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QWindow, QSize)
  @overload(NoneType, QSize)
  @overload(QWindow, QSize, Mode)
  @overload(NoneType, QSize, Mode)
  @overload(QWindow, QSize, Mode, State)
  @overload(NoneType, QSize, Mode, State)
  def actualSize(
      self,
      window: Optional[QWindow],
      size: QSize,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QSize:
    """
    Calls Qt's 'QSize QIcon::actualSize(QWindow *window, const QSize &size,
    Mode mode, State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#actualSize

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QIcon::actualSize(QWindow *window, const QSize &size, Mode mode,
    #      State state) const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon10actualSizeEP7QWindowRK5QSizeNS_4ModeENS_5StateE',
        self._addressOf(window), self._valueOf(size), mode.value,
        state.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QIcon::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIcon::name() const
    return self.uglySide.call('ritual_ZNK5QIcon4nameEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QIcon::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#isNull
    """
    #  bool QIcon::isNull() const
    return self.uglySide.call('ritual_ZNK5QIcon6isNullEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QIcon::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#isDetached
    """
    #  bool QIcon::isDetached() const
    return self.uglySide.call('ritual_ZNK5QIcon10isDetachedEv')

  def cacheKey(self) -> int:
    """
    Calls Qt's 'qint64 QIcon::cacheKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#cacheKey
    """
    #  qint64 QIcon::cacheKey() const
    return self.uglySide.call('ritual_ZNK5QIcon8cacheKeyEv')

  @overload()
  @overload(Mode)
  @overload(Mode, State)
  def availableSizes(
      self,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QIcon::availableSizes(Mode mode, State state)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#availableSizes

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QIcon::availableSizes(Mode mode, State state) const
    address = self.uglySide.call(
        'ritual_ZNK5QIcon14availableSizesENS_4ModeENS_5StateE',
        mode.value, state.value,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def isMask(self) -> bool:
    """
    Calls Qt's 'bool QIcon::isMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#isMask
    """
    #  bool QIcon::isMask() const
    return self.uglySide.call('ritual_ZNK5QIcon6isMaskEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsMask(self, isMask: bool) -> None:
    """
    Calls Qt's 'void QIcon::setIsMask(bool isMask)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#setIsMask

    Parameters
    ----------

    isMask : bool
      Passed on as it is.
    """
    #  void QIcon::setIsMask(bool isMask)
    self.uglySide.call('ritual_ZN5QIcon9setIsMaskEb', isMask)

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
    Notes what was given, for Qt's 'QIcon::QIcon()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#QIcon
    """
    #  QIcon::QIcon()
    self._noteCreation(QIcon, lambda: Rituals.call('ritual_ZN5QIconC1Ev'))

  @overload(QPixmap)
  def __init__(self, pixmap: QPixmap) -> None:
    """
    Notes what was given, for Qt's 'QIcon::QIcon(const QPixmap &pixmap)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#QIcon

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  QIcon::QIcon(const QPixmap &pixmap)
    self._noteCreation(QIcon, lambda: Rituals.call(
        'ritual_ZN5QIconC1ERK7QPixmap', self._valueOf(pixmap),
    ))

  @overload(THIS)
  def __init__(self, other: QIcon) -> None:
    """
    Notes what was given, for Qt's 'QIcon::QIcon(const QIcon &other)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#QIcon

    Parameters
    ----------

    other : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  QIcon::QIcon(const QIcon &other)
    self._noteCreation(QIcon, lambda: Rituals.call(
        'ritual_ZN5QIconC1ERKS_', self._valueOf(other),
    ))

  @overload(str)
  def __init__(self, fileName: str) -> None:
    """
    Notes what was given, for Qt's 'QIcon::QIcon(const QString &fileName)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#QIcon

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QIcon::QIcon(const QString &fileName)
    self._noteCreation(QIcon, lambda: Rituals.call(
        'ritual_ZN5QIconC1ERK7QString', fileName,
    ))

  @overload(QIconEngine)
  @overload(NoneType)
  def __init__(self, engine: Optional[QIconEngine]) -> None:
    """
    Notes what was given, for Qt's 'QIcon::QIcon(QIconEngine *engine)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#QIcon

    Parameters
    ----------

    engine : Optional[QIconEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QIcon::QIcon(QIconEngine *engine)
    self._noteCreation(QIcon, lambda: Rituals.call(
        'ritual_ZN5QIconC1EP11QIconEngine', self._addressOf(engine),
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

  @overload(QPainter, QRect)
  @overload(NoneType, QRect)
  @overload(QPainter, QRect, Qt.Alignment)
  @overload(NoneType, QRect, Qt.Alignment)
  @overload(QPainter, QRect, Qt.Alignment, Mode)
  @overload(NoneType, QRect, Qt.Alignment, Mode)
  @overload(QPainter, QRect, Qt.Alignment, Mode, State)
  @overload(NoneType, QRect, Qt.Alignment, Mode, State)
  def paint(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      alignment: Qt.Alignment = Qt.Alignment.AlignCenter,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> None:
    """
    Calls Qt's 'void QIcon::paint(QPainter *painter, const QRect &rect,
    Qt::Alignment alignment, Mode mode, State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment.AlignCenter.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.
    """
    #  void QIcon::paint(QPainter *painter, const QRect &rect, Qt::Alignment
    #      alignment, Mode mode, State state) const
    self.uglySide.call(
        'ritual_ZNK5QIcon5paintEP8QPainterRK5QRect6QFlagsIN2Qt13AlignmentFl'
        'agEENS_4ModeENS_5StateE',
        self._addressOf(painter), self._valueOf(rect), alignment.value,
        mode.value, state.value,
    )

  @overload(QPainter, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  @overload(QPainter, int, int, int, int, Qt.Alignment)
  @overload(NoneType, int, int, int, int, Qt.Alignment)
  @overload(QPainter, int, int, int, int, Qt.Alignment, Mode)
  @overload(NoneType, int, int, int, int, Qt.Alignment, Mode)
  @overload(QPainter, int, int, int, int, Qt.Alignment, Mode, State)
  @overload(NoneType, int, int, int, int, Qt.Alignment, Mode, State)
  def paint(
      self,
      painter: Optional[QPainter],
      x: int,
      y: int,
      w: int,
      h: int,
      alignment: Qt.Alignment = Qt.Alignment.AlignCenter,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> None:
    """
    Calls Qt's 'void QIcon::paint(QPainter *painter, int x, int y, int w, int
    h, Qt::Alignment alignment, Mode mode, State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment.AlignCenter.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.
    """
    #  void QIcon::paint(QPainter *painter, int x, int y, int w, int h,
    #      Qt::Alignment alignment, Mode mode, State state) const
    self.uglySide.call(
        'ritual_ZNK5QIcon5paintEP8QPainteriiii6QFlagsIN2Qt13AlignmentFlagEE'
        'NS_4ModeENS_5StateE',
        self._addressOf(painter), x, y, w, h, alignment.value, mode.value,
        state.value,
    )

  def detach(self) -> None:
    """
    Calls Qt's 'void QIcon::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#detach
    """
    #  void QIcon::detach()
    self.uglySide.call('ritual_ZN5QIcon6detachEv')

  @overload(QPixmap)
  @overload(QPixmap, Mode)
  @overload(QPixmap, Mode, State)
  def addPixmap(
      self,
      pixmap: QPixmap,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> None:
    """
    Calls Qt's 'void QIcon::addPixmap(const QPixmap &pixmap, Mode mode, State
    state)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#addPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.
    """
    #  void QIcon::addPixmap(const QPixmap &pixmap, Mode mode, State state)
    self.uglySide.call(
        'ritual_ZN5QIcon9addPixmapERK7QPixmapNS_4ModeENS_5StateE',
        self._valueOf(pixmap), mode.value, state.value,
    )

  @overload(str)
  @overload(str, QSize)
  @overload(str, QSize, Mode)
  @overload(str, QSize, Mode, State)
  def addFile(
      self,
      fileName: str,
      size: Optional[QSize] = None,
      mode: Mode = Mode.Normal,
      state: State = State.Off,
  ) -> None:
    """
    Calls Qt's 'void QIcon::addFile(const QString &fileName, const QSize
    &size, Mode mode, State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qicon.html#addFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.Normal.

    state : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.Off.
    """
    #  void QIcon::addFile(const QString &fileName, const QSize &size, Mode
    #      mode, State state)
    if size is None:
      from ..QtCore import QSize
      size = QSize()
    self.uglySide.call(
        'ritual_ZN5QIcon7addFileERK7QStringRK5QSizeNS_4ModeENS_5StateE',
        fileName, self._valueOf(size), mode.value, state.value,
    )
