"""
QPlatformIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformintegration.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QStringList
from . import QOpenGLContext, QPlatformPixmap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractEventDispatcher, QVariant
  from . import QIcon, QOffscreenSurface, QPaintDevice, QPaintEngine
  from . import QPlatformAccessibility, QPlatformBackingStore
  from . import QPlatformClipboard, QPlatformDrag, QPlatformFontDatabase
  from . import QPlatformInputContext, QPlatformKeyMapper
  from . import QPlatformNativeInterface, QPlatformOffscreenSurface
  from . import QPlatformOpenGLContext, QPlatformServices
  from . import QPlatformSessionManager, QPlatformSharedGraphicsCache
  from . import QPlatformTheme, QPlatformVulkanInstance, QPlatformWindow
  from . import QVulkanInstance, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QOffscreenSurface = WAIT['QOffscreenSurface']
  QPaintDevice = WAIT['QPaintDevice']
  QVulkanInstance = WAIT['QVulkanInstance']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformIntegration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformIntegration: a plain Python object standing
  in front of one C++ QPlatformIntegration.

  What exists
  -----------

  Every function of Qt's QPlatformIntegration that has a ritual and that
  Python can call so far, 33 names in all: 'hasCapability',
  'createPlatformPixmap', 'createPlatformWindow', 'createForeignWindow',
  'createPlatformBackingStore', 'createPlatformOpenGLContext',
  'createPlatformSharedGraphicsCache', 'createImagePaintEngine',
  'createEventDispatcher', 'initialize', 'destroy', 'fontDatabase',
  'clipboard', 'drag', 'inputContext', 'accessibility', 'nativeInterface',
  'services', 'styleHint', 'defaultWindowState', 'queryKeyboardModifiers',
  'keyMapper', 'themeNames', 'createPlatformTheme',
  'createPlatformOffscreenSurface', 'createPlatformSessionManager', 'sync',
  'openGLModuleType', 'setApplicationIcon', 'setApplicationBadge', 'beep',
  'quit', 'createPlatformVulkanInstance'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformIntegration::~QPlatformIntegration()': the destructor:
    Python never removes a C++ QPlatformIntegration.
  - Qt's 'QList<int> QPlatformIntegration::possibleKeys(const QKeyEvent *a0)
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 41 functions Qt declares: 4 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QPlatformIntegration is created at the first use, not by
    'QPlatformIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformIntegration.
  - Each name of Qt's QPlatformIntegration that has no cute function yet,
    'call', 'possibleKeys', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformIntegration, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Capability(CuteNum):
    """
    The enum 'QPlatformIntegration::Capability' of Qt, with the 27 names Qt
    gives in it.
    """

    ThreadedPixmaps = Kee[int](1)
    OpenGL = Kee[int](2)
    ThreadedOpenGL = Kee[int](3)
    SharedGraphicsCache = Kee[int](4)
    BufferQueueingOpenGL = Kee[int](5)
    WindowMasks = Kee[int](6)
    MultipleWindows = Kee[int](7)
    ApplicationState = Kee[int](8)
    ForeignWindows = Kee[int](9)
    NonFullScreenWindows = Kee[int](10)
    NativeWidgets = Kee[int](11)
    WindowManagement = Kee[int](12)
    WindowActivation = Kee[int](13)
    SyncState = Kee[int](14)
    RasterGLSurface = Kee[int](15)
    AllGLFunctionsQueryable = Kee[int](16)
    ApplicationIcon = Kee[int](17)
    SwitchableWidgetComposition = Kee[int](18)
    TopStackedNativeChildWindows = Kee[int](19)
    OpenGLOnRasterSurface = Kee[int](20)
    MaximizeUsingFullscreenGeometry = Kee[int](21)
    PaintEvents = Kee[int](22)
    RhiBasedRendering = Kee[int](23)
    ScreenWindowGrabbing = Kee[int](24)
    BackingStoreStaticContents = Kee[int](25)
    OffscreenSurface = Kee[int](26)
    MouseCursorPositioning = Kee[int](27)

  class StyleHint(CuteNum):
    """
    The enum 'QPlatformIntegration::StyleHint' of Qt, with the 27 names Qt
    gives in it.
    """

    CursorFlashTime = Kee[int](0)
    KeyboardInputInterval = Kee[int](1)
    MouseDoubleClickInterval = Kee[int](2)
    StartDragDistance = Kee[int](3)
    StartDragTime = Kee[int](4)
    KeyboardAutoRepeatRate = Kee[int](5)
    ShowIsFullScreen = Kee[int](6)
    PasswordMaskDelay = Kee[int](7)
    FontSmoothingGamma = Kee[int](8)
    StartDragVelocity = Kee[int](9)
    UseRtlExtensions = Kee[int](10)
    PasswordMaskCharacter = Kee[int](11)
    SetFocusOnTouchRelease = Kee[int](12)
    ShowIsMaximized = Kee[int](13)
    MousePressAndHoldInterval = Kee[int](14)
    TabFocusBehavior = Kee[int](15)
    ReplayMousePressOutsidePopup = Kee[int](16)
    ItemViewActivateItemOnSingleClick = Kee[int](17)
    UiEffects = Kee[int](18)
    WheelScrollLines = Kee[int](19)
    ShowShortcutsInContextMenus = Kee[int](20)
    MouseQuickSelectionThreshold = Kee[int](21)
    MouseDoubleClickDistance = Kee[int](22)
    FlickStartDistance = Kee[int](23)
    FlickMaximumVelocity = Kee[int](24)
    FlickDeceleration = Kee[int](25)
    UnderlineShortcut = Kee[int](26)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformIntegration'

  #  A C++ QPlatformIntegration Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformIntegration'

  #  The functions Qt calls itself that QPlatformIntegration is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createPlatformSharedGraphicsCache': (
          'QPlatformSharedGraphicsCache '
          '*QPlatformIntegration::createPlatformSharedGraphicsCache(const '
          'char *) const',
      ),
      'possibleKeys': (
          'QList<int> QPlatformIntegration::possibleKeys(const QKeyEvent '
          '*) const',
      ),
      'themeNames': (
          'QStringList QPlatformIntegration::themeNames() const',
      ),
  }

  #  The functions Qt calls itself that QPlatformIntegration is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'hasCapability': (
          ('_ZNK20QPlatformIntegration13hasCapabilityENS_10CapabilityE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPlatformIntegration.Capability'),
           )),
      ),
      'createPlatformPixmap': (
          ('_ZNK20QPlatformIntegration20createPlatformPixmapEN15QPlatformPi'
           'xmap9PixelTypeE',
           ('address', 'address', 'QtGui:QPlatformPixmap'),
           (
               ('int', 'enum', 'QtGui:QPlatformPixmap.PixelType'),
           )),
      ),
      'createPlatformWindow': (
          ('_ZNK20QPlatformIntegration20createPlatformWindowEP7QWindow',
           ('address', 'address', 'QtGui:QPlatformWindow'),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'createForeignWindow': (
          ('_ZNK20QPlatformIntegration19createForeignWindowEP7QWindowy',
           ('address', 'address', 'QtGui:QPlatformWindow'),
           (
               ('address', 'address', 'QtGui:QWindow'),
               ('unsigned long long', 'number', ''),
           )),
      ),
      'createPlatformBackingStore': (
          ('_ZNK20QPlatformIntegration26createPlatformBackingStoreEP7QWindo'
           'w',
           ('address', 'address', 'QtGui:QPlatformBackingStore'),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'createPlatformOpenGLContext': (
          ('_ZNK20QPlatformIntegration27createPlatformOpenGLContextEP14QOpe'
           'nGLContext',
           ('address', 'address', 'QtGui:QPlatformOpenGLContext'),
           (
               ('address', 'address', 'QtGui:QOpenGLContext'),
           )),
      ),
      'createImagePaintEngine': (
          ('_ZNK20QPlatformIntegration22createImagePaintEngineEP12QPaintDev'
           'ice',
           ('address', 'address', 'QtGui:QPaintEngine'),
           (
               ('address', 'address', 'QtGui:QPaintDevice'),
           )),
      ),
      'createEventDispatcher': (
          ('_ZNK20QPlatformIntegration21createEventDispatcherEv',
           ('address', 'address', 'QtCore:QAbstractEventDispatcher'),
           ()),
      ),
      'initialize': (
          ('_ZN20QPlatformIntegration10initializeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'destroy': (
          ('_ZN20QPlatformIntegration7destroyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'fontDatabase': (
          ('_ZNK20QPlatformIntegration12fontDatabaseEv',
           ('address', 'address', 'QtGui:QPlatformFontDatabase'),
           ()),
      ),
      'clipboard': (
          ('_ZNK20QPlatformIntegration9clipboardEv',
           ('address', 'address', 'QtGui:QPlatformClipboard'),
           ()),
      ),
      'drag': (
          ('_ZNK20QPlatformIntegration4dragEv',
           ('address', 'address', 'QtGui:QPlatformDrag'),
           ()),
      ),
      'inputContext': (
          ('_ZNK20QPlatformIntegration12inputContextEv',
           ('address', 'address', 'QtGui:QPlatformInputContext'),
           ()),
      ),
      'accessibility': (
          ('_ZNK20QPlatformIntegration13accessibilityEv',
           ('address', 'address', 'QtGui:QPlatformAccessibility'),
           ()),
      ),
      'nativeInterface': (
          ('_ZNK20QPlatformIntegration15nativeInterfaceEv',
           ('address', 'address', 'QtGui:QPlatformNativeInterface'),
           ()),
      ),
      'services': (
          ('_ZNK20QPlatformIntegration8servicesEv',
           ('address', 'address', 'QtGui:QPlatformServices'),
           ()),
      ),
      'styleHint': (
          ('_ZNK20QPlatformIntegration9styleHintENS_9StyleHintE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtGui:QPlatformIntegration.StyleHint'),
           )),
      ),
      'defaultWindowState': (
          ('_ZNK20QPlatformIntegration18defaultWindowStateE6QFlagsIN2Qt10Wi'
           'ndowTypeEE',
           ('int', 'enum', 'QtCore:Qt.WindowState'),
           (
               ('int', 'flags', 'QtCore:Qt.WindowType'),
           )),
      ),
      'queryKeyboardModifiers': (
          ('_ZNK20QPlatformIntegration22queryKeyboardModifiersEv',
           ('int', 'flags', 'QtCore:Qt.KeyboardModifier'),
           ()),
      ),
      'keyMapper': (
          ('_ZNK20QPlatformIntegration9keyMapperEv',
           ('address', 'address', 'QtGui:QPlatformKeyMapper'),
           ()),
      ),
      'createPlatformTheme': (
          ('_ZNK20QPlatformIntegration19createPlatformThemeERK7QString',
           ('address', 'address', 'QtGui:QPlatformTheme'),
           (
               ('address', 'text', ''),
           )),
      ),
      'createPlatformOffscreenSurface': (
          ('_ZNK20QPlatformIntegration30createPlatformOffscreenSurfaceEP17Q'
           'OffscreenSurface',
           ('address', 'address', 'QtGui:QPlatformOffscreenSurface'),
           (
               ('address', 'address', 'QtGui:QOffscreenSurface'),
           )),
      ),
      'createPlatformSessionManager': (
          ('_ZNK20QPlatformIntegration28createPlatformSessionManagerERK7QSt'
           'ringS2_',
           ('address', 'address', 'QtGui:QPlatformSessionManager'),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'sync': (
          ('_ZN20QPlatformIntegration4syncEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'openGLModuleType': (
          ('_ZN20QPlatformIntegration16openGLModuleTypeEv',
           ('int', 'enum', 'QtGui:QOpenGLContext.OpenGLModuleType'),
           ()),
      ),
      'setApplicationIcon': (
          ('_ZNK20QPlatformIntegration18setApplicationIconERK5QIcon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QIcon'),
           )),
      ),
      'setApplicationBadge': (
          ('_ZN20QPlatformIntegration19setApplicationBadgeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'beep': (
          ('_ZNK20QPlatformIntegration4beepEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'quit': (
          ('_ZNK20QPlatformIntegration4quitEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createPlatformVulkanInstance': (
          ('_ZNK20QPlatformIntegration28createPlatformVulkanInstanceEP15QVu'
           'lkanInstance',
           ('address', 'address', 'QtGui:QPlatformVulkanInstance'),
           (
               ('address', 'address', 'QtGui:QVulkanInstance'),
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

  @overload(Capability)
  def hasCapability(self, cap: Capability) -> bool:
    """
    Calls Qt's 'bool QPlatformIntegration::hasCapability(Capability cap)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#hasCapability

    Parameters
    ----------

    cap : Capability
      Passed on as its number.
    """
    #  bool QPlatformIntegration::hasCapability(Capability cap) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration13hasCapabilityENS_10CapabilityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration13hasCapabilityENS_10Capabil'
          'ityE')
    return self.uglySide.call(ritual, cap.value)

  @overload(QPlatformPixmap.PixelType)
  def createPlatformPixmap(
      self,
      type: QPlatformPixmap.PixelType,
  ) -> Optional[QPlatformPixmap]:
    """
    Calls Qt's 'QPlatformPixmap
    *QPlatformIntegration::createPlatformPixmap(QPlatformPixmap::PixelType
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#createPlatformPixmap

    Parameters
    ----------

    type : QPlatformPixmap.PixelType
      Passed on as its number.

    Returns
    -------

    Optional[QPlatformPixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformPixmap
    #      *QPlatformIntegration::createPlatformPixmap(QPlatformPixmap::
    #      PixelType type) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration20createPlatformPixmapEN15QPlatfor'
        'mPixmap9PixelTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration20createPlatformPixmapEN15QP'
          'latformPixmap9PixelTypeE')
    address = self.uglySide.call(ritual, type.value)
    return QPlatformPixmap._cuteAt(address)

  @overload(QWindow)
  @overload(NoneType)
  def createPlatformWindow(
      self,
      window: Optional[QWindow],
  ) -> Optional[QPlatformWindow]:
    """
    Calls Qt's 'QPlatformWindow
    *QPlatformIntegration::createPlatformWindow(QWindow *window) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#createPlatformWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformWindow *QPlatformIntegration::createPlatformWindow(QWindow
    #      *window) const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformIntegration20createPlatformWindowEP7QWindow',
        self._addressOf(window),
    )
    from . import QPlatformWindow
    return QPlatformWindow._cuteAt(address)

  @overload(QWindow, int)
  @overload(NoneType, int)
  def createForeignWindow(
      self,
      a0: Optional[QWindow],
      a1: int,
  ) -> Optional[QPlatformWindow]:
    """
    Calls Qt's 'QPlatformWindow
    *QPlatformIntegration::createForeignWindow(QWindow *a0, WId a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#createForeignWindow

    Parameters
    ----------

    a0 : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.

    Returns
    -------

    Optional[QPlatformWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformWindow *QPlatformIntegration::createForeignWindow(QWindow
    #      *a0, WId a1) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration19createForeignWindowEP7QWindowy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration19createForeignWindowEP7QWin'
          'dowy')
    address = self.uglySide.call(ritual, self._addressOf(a0), a1)
    from . import QPlatformWindow
    return QPlatformWindow._cuteAt(address)

  @overload(QWindow)
  @overload(NoneType)
  def createPlatformBackingStore(
      self,
      window: Optional[QWindow],
  ) -> Optional[QPlatformBackingStore]:
    """
    Calls Qt's 'QPlatformBackingStore
    *QPlatformIntegration::createPlatformBackingStore(QWindow *window)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformBackingStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformBackingStore
    #      *QPlatformIntegration::createPlatformBackingStore(QWindow *window)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformIntegration26createPlatformBackingStoreEP7QWi'
        'ndow',
        self._addressOf(window),
    )
    from . import QPlatformBackingStore
    return QPlatformBackingStore._cuteAt(address)

  @overload(QOpenGLContext)
  @overload(NoneType)
  def createPlatformOpenGLContext(
      self,
      context: Optional[QOpenGLContext],
  ) -> Optional[QPlatformOpenGLContext]:
    """
    Calls Qt's 'QPlatformOpenGLContext
    *QPlatformIntegration::createPlatformOpenGLContext(QOpenGLContext
    *context) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformOpenGLContext
    #      *QPlatformIntegration::createPlatformOpenGLContext(QOpenGLContext
    #      *context) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration27createPlatformOpenGLContextEP14Q'
        'OpenGLContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration27createPlatformOpenGLContex'
          'tEP14QOpenGLContext')
    address = self.uglySide.call(ritual, self._addressOf(context))
    from . import QPlatformOpenGLContext
    return QPlatformOpenGLContext._cuteAt(address)

  @overload(str)
  @overload(NoneType)
  def createPlatformSharedGraphicsCache(
      self,
      cacheId: Optional[str],
  ) -> Optional[QPlatformSharedGraphicsCache]:
    """
    Calls Qt's 'QPlatformSharedGraphicsCache
    *QPlatformIntegration::createPlatformSharedGraphicsCache(const char
    *cacheId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html

    Parameters
    ----------

    cacheId : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    Optional[QPlatformSharedGraphicsCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSharedGraphicsCache
    #      *QPlatformIntegration::createPlatformSharedGraphicsCache(const
    #      char *cacheId) const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformIntegration33createPlatformSharedGraphicsCach'
        'eEPKc',
        self._bytesOf(cacheId),
    )
    from . import QPlatformSharedGraphicsCache
    return QPlatformSharedGraphicsCache._cuteAt(address)

  @overload(QPaintDevice)
  @overload(NoneType)
  def createImagePaintEngine(
      self,
      paintDevice: Optional[QPaintDevice],
  ) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine
    *QPlatformIntegration::createImagePaintEngine(QPaintDevice *paintDevice)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#createImagePaintEngine

    Parameters
    ----------

    paintDevice : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine
    #      *QPlatformIntegration::createImagePaintEngine(QPaintDevice
    #      *paintDevice) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration22createImagePaintEngineEP12QPaint'
        'Device')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration22createImagePaintEngineEP12'
          'QPaintDevice')
    address = self.uglySide.call(
        ritual, self._addressOf(paintDevice, 'QPaintDevice'),
    )
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  def createEventDispatcher(self) -> Optional[QAbstractEventDispatcher]:
    """
    Calls Qt's 'QAbstractEventDispatcher
    *QPlatformIntegration::createEventDispatcher() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#createEventDispatcher

    Returns
    -------

    Optional[QAbstractEventDispatcher]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractEventDispatcher
    #      *QPlatformIntegration::createEventDispatcher() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformIntegration21createEventDispatcherEv',
    )
    from ..QtCore import QAbstractEventDispatcher
    return QAbstractEventDispatcher._cuteAt(address)

  def fontDatabase(self) -> Optional[QPlatformFontDatabase]:
    """
    Calls Qt's 'QPlatformFontDatabase *QPlatformIntegration::fontDatabase()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#fontDatabase

    Returns
    -------

    Optional[QPlatformFontDatabase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformFontDatabase *QPlatformIntegration::fontDatabase() const
    ritual = 'ritual_ZNK20QPlatformIntegration12fontDatabaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration12fontDatabaseEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformFontDatabase
    return QPlatformFontDatabase._cuteAt(address)

  def clipboard(self) -> Optional[QPlatformClipboard]:
    """
    Calls Qt's 'QPlatformClipboard *QPlatformIntegration::clipboard() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#clipboard

    Returns
    -------

    Optional[QPlatformClipboard]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformClipboard *QPlatformIntegration::clipboard() const
    ritual = 'ritual_ZNK20QPlatformIntegration9clipboardEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration9clipboardEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformClipboard
    return QPlatformClipboard._cuteAt(address)

  def drag(self) -> Optional[QPlatformDrag]:
    """
    Calls Qt's 'QPlatformDrag *QPlatformIntegration::drag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformintegration.html#drag

    Returns
    -------

    Optional[QPlatformDrag]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformDrag *QPlatformIntegration::drag() const
    ritual = 'ritual_ZNK20QPlatformIntegration4dragEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration4dragEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformDrag
    return QPlatformDrag._cuteAt(address)

  def inputContext(self) -> Optional[QPlatformInputContext]:
    """
    Calls Qt's 'QPlatformInputContext *QPlatformIntegration::inputContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#inputContext

    Returns
    -------

    Optional[QPlatformInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformInputContext *QPlatformIntegration::inputContext() const
    ritual = 'ritual_ZNK20QPlatformIntegration12inputContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration12inputContextEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformInputContext
    return QPlatformInputContext._cuteAt(address)

  def accessibility(self) -> Optional[QPlatformAccessibility]:
    """
    Calls Qt's 'QPlatformAccessibility *QPlatformIntegration::accessibility()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#accessibility

    Returns
    -------

    Optional[QPlatformAccessibility]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAccessibility *QPlatformIntegration::accessibility() const
    ritual = 'ritual_ZNK20QPlatformIntegration13accessibilityEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration13accessibilityEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformAccessibility
    return QPlatformAccessibility._cuteAt(address)

  def nativeInterface(self) -> Optional[QPlatformNativeInterface]:
    """
    Calls Qt's 'QPlatformNativeInterface
    *QPlatformIntegration::nativeInterface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#nativeInterface

    Returns
    -------

    Optional[QPlatformNativeInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformNativeInterface *QPlatformIntegration::nativeInterface()
    #      const
    ritual = 'ritual_ZNK20QPlatformIntegration15nativeInterfaceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration15nativeInterfaceEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformNativeInterface
    return QPlatformNativeInterface._cuteAt(address)

  def services(self) -> Optional[QPlatformServices]:
    """
    Calls Qt's 'QPlatformServices *QPlatformIntegration::services() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformintegration.html#services

    Returns
    -------

    Optional[QPlatformServices]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformServices *QPlatformIntegration::services() const
    ritual = 'ritual_ZNK20QPlatformIntegration8servicesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration8servicesEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformServices
    return QPlatformServices._cuteAt(address)

  @overload(StyleHint)
  def styleHint(self, hint: StyleHint) -> QVariant:
    """
    Calls Qt's 'QVariant QPlatformIntegration::styleHint(StyleHint hint)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#styleHint

    Parameters
    ----------

    hint : StyleHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlatformIntegration::styleHint(StyleHint hint) const
    ritual = 'ritual_ZNK20QPlatformIntegration9styleHintENS_9StyleHintE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration9styleHintENS_9StyleHintE')
    address = self.uglySide.call(ritual, hint.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Qt.WindowFlags)
  def defaultWindowState(self, a0: Qt.WindowFlags) -> Qt.WindowState:
    """
    Calls Qt's 'Qt::WindowState
    QPlatformIntegration::defaultWindowState(Qt::WindowFlags a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#defaultWindowState

    Parameters
    ----------

    a0 : Qt.WindowFlags
      Passed on as its number.

    Returns
    -------

    Qt.WindowState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowState(number)'
      gives.
    """
    #  Qt::WindowState
    #      QPlatformIntegration::defaultWindowState(Qt::WindowFlags a0) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration18defaultWindowStateE6QFlagsIN2Qt1'
        '0WindowTypeEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration18defaultWindowStateE6QFlags'
          'IN2Qt10WindowTypeEE')
    return Qt.WindowState(self.uglySide.call(ritual, a0.value))

  def queryKeyboardModifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers
    QPlatformIntegration::queryKeyboardModifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#queryKeyboardModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QPlatformIntegration::queryKeyboardModifiers()
    #      const
    ritual = 'ritual_ZNK20QPlatformIntegration22queryKeyboardModifiersEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration22queryKeyboardModifiersEv')
    return Qt.KeyboardModifiers(self.uglySide.call(ritual))

  def keyMapper(self) -> Optional[QPlatformKeyMapper]:
    """
    Calls Qt's 'QPlatformKeyMapper *QPlatformIntegration::keyMapper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#keyMapper

    Returns
    -------

    Optional[QPlatformKeyMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformKeyMapper *QPlatformIntegration::keyMapper() const
    ritual = 'ritual_ZNK20QPlatformIntegration9keyMapperEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration9keyMapperEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformKeyMapper
    return QPlatformKeyMapper._cuteAt(address)

  def themeNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformIntegration::themeNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#themeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformIntegration::themeNames() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformIntegration10themeNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def createPlatformTheme(self, name: str) -> Optional[QPlatformTheme]:
    """
    Calls Qt's 'QPlatformTheme
    *QPlatformIntegration::createPlatformTheme(const QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#createPlatformTheme

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlatformTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformTheme *QPlatformIntegration::createPlatformTheme(const
    #      QString &name) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration19createPlatformThemeERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration19createPlatformThemeERK7QSt'
          'ring')
    address = self.uglySide.call(ritual, name)
    from . import QPlatformTheme
    return QPlatformTheme._cuteAt(address)

  @overload(QOffscreenSurface)
  @overload(NoneType)
  def createPlatformOffscreenSurface(
      self,
      surface: Optional[QOffscreenSurface],
  ) -> Optional[QPlatformOffscreenSurface]:
    """
    Calls Qt's 'QPlatformOffscreenSurface
    *QPlatformIntegration::createPlatformOffscreenSurface(QOffscreenSurface
    *surface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html

    Parameters
    ----------

    surface : Optional[QOffscreenSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformOffscreenSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformOffscreenSurface
    #      *QPlatformIntegration::createPlatformOffscreenSurface(
    #      QOffscreenSurface *surface) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration30createPlatformOffscreenSurfaceEP'
        '17QOffscreenSurface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration30createPlatformOffscreenSur'
          'faceEP17QOffscreenSurface')
    address = self.uglySide.call(ritual, self._addressOf(surface))
    from . import QPlatformOffscreenSurface
    return QPlatformOffscreenSurface._cuteAt(address)

  @overload(str, str)
  def createPlatformSessionManager(
      self,
      id: str,
      key: str,
  ) -> Optional[QPlatformSessionManager]:
    """
    Calls Qt's 'QPlatformSessionManager
    *QPlatformIntegration::createPlatformSessionManager(const QString &id,
    const QString &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlatformSessionManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSessionManager
    #      *QPlatformIntegration::createPlatformSessionManager(const QString
    #      &id, const QString &key) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration28createPlatformSessionManagerERK7'
        'QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration28createPlatformSessionManag'
          'erERK7QStringS2_')
    address = self.uglySide.call(ritual, id, key)
    from . import QPlatformSessionManager
    return QPlatformSessionManager._cuteAt(address)

  @overload(QVulkanInstance)
  @overload(NoneType)
  def createPlatformVulkanInstance(
      self,
      instance: Optional[QVulkanInstance],
  ) -> Optional[QPlatformVulkanInstance]:
    """
    Calls Qt's 'QPlatformVulkanInstance
    *QPlatformIntegration::createPlatformVulkanInstance(QVulkanInstance
    *instance) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html

    Parameters
    ----------

    instance : Optional[QVulkanInstance]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformVulkanInstance]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformVulkanInstance
    #      *QPlatformIntegration::createPlatformVulkanInstance(
    #      QVulkanInstance *instance) const
    ritual = (
        'ritual_ZNK20QPlatformIntegration28createPlatformVulkanInstanceEP15'
        'QVulkanInstance')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration28createPlatformVulkanInstan'
          'ceEP15QVulkanInstance')
    address = self.uglySide.call(ritual, self._addressOf(instance))
    from . import QPlatformVulkanInstance
    return QPlatformVulkanInstance._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIcon)
  def setApplicationIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QPlatformIntegration::setApplicationIcon(const QIcon
    &icon) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#setApplicationIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QPlatformIntegration::setApplicationIcon(const QIcon &icon) const
    ritual = 'ritual_ZNK20QPlatformIntegration18setApplicationIconERK5QIcon'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformIntegration18setApplicationIconERK5QIco'
          'n')
    self.uglySide.call(ritual, self._valueOf(icon))

  @overload(int)
  def setApplicationBadge(self, number: int) -> None:
    """
    Calls Qt's 'void QPlatformIntegration::setApplicationBadge(qint64
    number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#setApplicationBadge

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void QPlatformIntegration::setApplicationBadge(qint64 number)
    ritual = 'ritual_ZN20QPlatformIntegration19setApplicationBadgeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformIntegration19setApplicationBadgeEx'
    self.uglySide.call(ritual, number)

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
    Notes what was given, for Qt's
    'QPlatformIntegration::QPlatformIntegration()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#QPlatformIntegration
    """
    #  QPlatformIntegration::QPlatformIntegration()
    self._noteCreation(QPlatformIntegration, lambda: Rituals.call(
        'ritual_ZN20QPlatformIntegrationC1Ev',
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QPlatformIntegration::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#initialize
    """
    #  void QPlatformIntegration::initialize()
    ritual = 'ritual_ZN20QPlatformIntegration10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformIntegration10initializeEv'
    self.uglySide.call(ritual)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QPlatformIntegration::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformintegration.html#destroy
    """
    #  void QPlatformIntegration::destroy()
    ritual = 'ritual_ZN20QPlatformIntegration7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformIntegration7destroyEv'
    self.uglySide.call(ritual)

  def sync(self) -> None:
    """
    Calls Qt's 'void QPlatformIntegration::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformintegration.html#sync
    """
    #  void QPlatformIntegration::sync()
    ritual = 'ritual_ZN20QPlatformIntegration4syncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformIntegration4syncEv'
    self.uglySide.call(ritual)

  def openGLModuleType(self) -> QOpenGLContext.OpenGLModuleType:
    """
    Calls Qt's 'QOpenGLContext::OpenGLModuleType
    QPlatformIntegration::openGLModuleType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegration.html#openGLModuleType

    Returns
    -------

    QOpenGLContext.OpenGLModuleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLContext.OpenGLModuleType(number)' gives.
    """
    #  QOpenGLContext::OpenGLModuleType
    #      QPlatformIntegration::openGLModuleType()
    ritual = 'ritual_ZN20QPlatformIntegration16openGLModuleTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformIntegration16openGLModuleTypeEv'
    return QOpenGLContext.OpenGLModuleType(self.uglySide.call(ritual))

  def beep(self) -> None:
    """
    Calls Qt's 'void QPlatformIntegration::beep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformintegration.html#beep
    """
    #  void QPlatformIntegration::beep() const
    ritual = 'ritual_ZNK20QPlatformIntegration4beepEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration4beepEv'
    self.uglySide.call(ritual)

  def quit(self) -> None:
    """
    Calls Qt's 'void QPlatformIntegration::quit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformintegration.html#quit
    """
    #  void QPlatformIntegration::quit() const
    ritual = 'ritual_ZNK20QPlatformIntegration4quitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformIntegration4quitEv'
    self.uglySide.call(ritual)

  @staticmethod
  def call(*__, **_) -> Never:
    """
    Qt's 'QPlatformIntegration::call': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QPlatformIntegration.call' has no cute function yet. Qt's "
        "'QPlatformIntegration::call': a template: a pattern and no single "
        "function.")

  @staticmethod
  def possibleKeys(*__, **_) -> Never:
    """
    Qt's 'QList<int> QPlatformIntegration::possibleKeys(const QKeyEvent *a0)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformIntegration.possibleKeys' has no cute function yet. Qt's "
        "'QList<int> QPlatformIntegration::possibleKeys(const QKeyEvent "
        "*a0) const': gives a type Python has no way to take yet.")
