"""
QPlatformScreen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformscreen.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect, QSizeF
  from . import QColorSpace, QPixmap, QPlatformCursor, QPlatformScreenPrivate
  from . import QScreen, QTransform, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformScreen(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformScreen: a plain Python object standing in
  front of one C++ QPlatformScreen.

  What exists
  -----------

  Every function of Qt's QPlatformScreen that has a ritual and that Python
  can call so far, 33 names in all: 'd_func', 'isPlaceholder', 'grabWindow',
  'geometry', 'availableGeometry', 'depth', 'format', 'colorSpace',
  'physicalSize', 'devicePixelRatio', 'refreshRate', 'nativeOrientation',
  'orientation', 'topLevelAt', 'windows', 'virtualSiblings',
  'screenForPosition', 'screen', 'platformScreenForWindow', 'name',
  'manufacturer', 'model', 'serialNumber', 'cursor',
  'subpixelAntialiasingTypeHint', 'powerState', 'setPowerState',
  'currentMode', 'preferredMode', 'angleBetween', 'transformBetween',
  'mapBetween', 'resizeMaximizedWindows'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPlatformScreenPrivate *QPlatformScreen::d_func() const':
    takes in Python what 'QPlatformScreenPrivate *QPlatformScreen::d_func()'
    takes.
  - Qt's 'QPlatformScreen::~QPlatformScreen()': the destructor: Python never
    removes a C++ QPlatformScreen.
  - Qt's 'QDpi QPlatformScreen::logicalDpi() const': gives a type Python has
    no way to take yet.
  - Qt's 'QDpi QPlatformScreen::logicalBaseDpi() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<Mode> QPlatformScreen::modes() const': gives a type Python
    has no way to take yet.
  - Qt's 'QDpi QPlatformScreen::overrideDpi(const QDpi &in)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 47 functions Qt declares: 4 forbidden; 3 not a gap.

  What to expect
  --------------

  - The C++ QPlatformScreen is created at the first use, not by
    'QPlatformScreen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformScreen.
  - Each name of Qt's QPlatformScreen that has no cute function yet,
    'logicalBaseDpi', 'logicalDpi', 'modes', 'overrideDpi', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformScreen, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PowerState(CuteNum):
    """
    The enum 'QPlatformScreen::PowerState' of Qt, with the 4 names Qt gives
    in it.
    """

    PowerStateOn = Kee[int](0)
    PowerStateStandby = Kee[int](1)
    PowerStateSuspend = Kee[int](2)
    PowerStateOff = Kee[int](3)

  class SubpixelAntialiasingType(CuteNum):
    """
    The enum 'QPlatformScreen::SubpixelAntialiasingType' of Qt, with the 5
    names Qt gives in it.
    """

    Subpixel_None = Kee[int](0)
    Subpixel_RGB = Kee[int](1)
    Subpixel_BGR = Kee[int](2)
    Subpixel_VRGB = Kee[int](3)
    Subpixel_VBGR = Kee[int](4)

  #  The classes Qt writes inside QPlatformScreen, each a class in here as in
  #  C++.

  class Mode(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPlatformScreen::Mode: a plain Python object
    standing in front of one C++ QPlatformScreen::Mode.

    C++ hands a QPlatformScreen::Mode around as a copy, so every C++
    QPlatformScreen::Mode behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QPlatformScreen::Mode yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPlatformScreen::Mode::~Mode()': the destructor: Python removes
      its C++ QPlatformScreen::Mode by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QPlatformScreen::Mode is created at the first use, not by
      'QPlatformScreen::Mode(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPlatformScreen::Mode back gives a copy the ritual
      made for Python, in a new cute QPlatformScreen::Mode.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPlatformScreen::Mode'

    #  Qt's '~QPlatformScreen::Mode()'. Naming it makes this a value class:
    #  Python owns every C++ QPlatformScreen::Mode behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QPlatformScreen4ModeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def platformScreenForWindow(
      window: Optional[QWindow],
  ) -> Optional[QPlatformScreen]:
    """
    Calls Qt's 'QPlatformScreen
    *QPlatformScreen::platformScreenForWindow(const QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#platformScreenForWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformScreen *QPlatformScreen::platformScreenForWindow(const
    #      QWindow *window)
    address = Rituals.call(
        'ritual_ZN15QPlatformScreen23platformScreenForWindowEPK7QWindow',
        CuteMixin._addressOf(window),
    )
    return QPlatformScreen._cuteAt(address)

  @staticmethod
  @overload(Qt.ScreenOrientation, Qt.ScreenOrientation)
  def angleBetween(a: Qt.ScreenOrientation, b: Qt.ScreenOrientation) -> int:
    """
    Calls Qt's 'int QPlatformScreen::angleBetween(Qt::ScreenOrientation a,
    Qt::ScreenOrientation b)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#angleBetween

    Parameters
    ----------

    a : Qt.ScreenOrientation
      Passed on as its number.

    b : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  int QPlatformScreen::angleBetween(Qt::ScreenOrientation a,
    #      Qt::ScreenOrientation b)
    return Rituals.call(
        'ritual_ZN15QPlatformScreen12angleBetweenEN2Qt17ScreenOrientationES'
        '1_',
        a.value, b.value,
    )

  @staticmethod
  @overload(Qt.ScreenOrientation, Qt.ScreenOrientation, QRect)
  def transformBetween(
      a: Qt.ScreenOrientation,
      b: Qt.ScreenOrientation,
      target: QRect,
  ) -> QTransform:
    """
    Calls Qt's 'QTransform
    QPlatformScreen::transformBetween(Qt::ScreenOrientation a,
    Qt::ScreenOrientation b, const QRect &target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#transformBetween

    Parameters
    ----------

    a : Qt.ScreenOrientation
      Passed on as its number.

    b : Qt.ScreenOrientation
      Passed on as its number.

    target : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QPlatformScreen::transformBetween(Qt::ScreenOrientation a,
    #      Qt::ScreenOrientation b, const QRect &target)
    address = Rituals.call(
        'ritual_ZN15QPlatformScreen16transformBetweenEN2Qt17ScreenOrientati'
        'onES1_RK5QRect',
        a.value, b.value, CuteMixin._valueOf(target),
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  @staticmethod
  @overload(Qt.ScreenOrientation, Qt.ScreenOrientation, QRect)
  def mapBetween(
      a: Qt.ScreenOrientation,
      b: Qt.ScreenOrientation,
      rect: QRect,
  ) -> QRect:
    """
    Calls Qt's 'QRect QPlatformScreen::mapBetween(Qt::ScreenOrientation a,
    Qt::ScreenOrientation b, const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#mapBetween

    Parameters
    ----------

    a : Qt.ScreenOrientation
      Passed on as its number.

    b : Qt.ScreenOrientation
      Passed on as its number.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformScreen::mapBetween(Qt::ScreenOrientation a,
    #      Qt::ScreenOrientation b, const QRect &rect)
    address = Rituals.call(
        'ritual_ZN15QPlatformScreen10mapBetweenEN2Qt17ScreenOrientationES1_'
        'RK5QRect',
        a.value, b.value, CuteMixin._valueOf(rect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformScreen'

  #  A C++ QPlatformScreen Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformScreen'

  #  The functions Qt calls itself that QPlatformScreen is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'logicalDpi': (
          'QDpi QPlatformScreen::logicalDpi() const',
      ),
      'logicalBaseDpi': (
          'QDpi QPlatformScreen::logicalBaseDpi() const',
      ),
      'virtualSiblings': (
          'QList<QPlatformScreen *> QPlatformScreen::virtualSiblings() '
          'const',
      ),
      'modes': (
          'QList<Mode> QPlatformScreen::modes() const',
      ),
  }

  #  The functions Qt calls itself that QPlatformScreen is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isPlaceholder': (
          ('_ZNK15QPlatformScreen13isPlaceholderEv',
           ('bool', 'number', ''),
           ()),
      ),
      'grabWindow': (
          ('_ZNK15QPlatformScreen10grabWindowEyiiii',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('unsigned long long', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'geometry': (
          ('_ZNK15QPlatformScreen8geometryEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
      'availableGeometry': (
          ('_ZNK15QPlatformScreen17availableGeometryEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
      'depth': (
          ('_ZNK15QPlatformScreen5depthEv',
           ('int', 'number', ''),
           ()),
      ),
      'format': (
          ('_ZNK15QPlatformScreen6formatEv',
           ('int', 'enum', 'QtGui:QImage.Format'),
           ()),
      ),
      'colorSpace': (
          ('_ZNK15QPlatformScreen10colorSpaceEv',
           ('address', 'value', 'QtGui:QColorSpace'),
           ()),
      ),
      'physicalSize': (
          ('_ZNK15QPlatformScreen12physicalSizeEv',
           ('address', 'value', 'QtCore:QSizeF'),
           ()),
      ),
      'devicePixelRatio': (
          ('_ZNK15QPlatformScreen16devicePixelRatioEv',
           ('double', 'number', ''),
           ()),
      ),
      'refreshRate': (
          ('_ZNK15QPlatformScreen11refreshRateEv',
           ('double', 'number', ''),
           ()),
      ),
      'nativeOrientation': (
          ('_ZNK15QPlatformScreen17nativeOrientationEv',
           ('int', 'enum', 'QtCore:Qt.ScreenOrientation'),
           ()),
      ),
      'orientation': (
          ('_ZNK15QPlatformScreen11orientationEv',
           ('int', 'enum', 'QtCore:Qt.ScreenOrientation'),
           ()),
      ),
      'topLevelAt': (
          ('_ZNK15QPlatformScreen10topLevelAtERK6QPoint',
           ('address', 'address', 'QtGui:QWindow'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'name': (
          ('_ZNK15QPlatformScreen4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'manufacturer': (
          ('_ZNK15QPlatformScreen12manufacturerEv',
           ('address', 'text', ''),
           ()),
      ),
      'model': (
          ('_ZNK15QPlatformScreen5modelEv',
           ('address', 'text', ''),
           ()),
      ),
      'serialNumber': (
          ('_ZNK15QPlatformScreen12serialNumberEv',
           ('address', 'text', ''),
           ()),
      ),
      'cursor': (
          ('_ZNK15QPlatformScreen6cursorEv',
           ('address', 'address', 'QtGui:QPlatformCursor'),
           ()),
      ),
      'subpixelAntialiasingTypeHint': (
          ('_ZNK15QPlatformScreen28subpixelAntialiasingTypeHintEv',
           ('int', 'enum', 'QtGui:QPlatformScreen.SubpixelAntialiasingType'),
           ()),
      ),
      'powerState': (
          ('_ZNK15QPlatformScreen10powerStateEv',
           ('int', 'enum', 'QtGui:QPlatformScreen.PowerState'),
           ()),
      ),
      'setPowerState': (
          ('_ZN15QPlatformScreen13setPowerStateENS_10PowerStateE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QPlatformScreen.PowerState'),
           )),
      ),
      'currentMode': (
          ('_ZNK15QPlatformScreen11currentModeEv',
           ('int', 'number', ''),
           ()),
      ),
      'preferredMode': (
          ('_ZNK15QPlatformScreen13preferredModeEv',
           ('int', 'number', ''),
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

  def isPlaceholder(self) -> bool:
    """
    Calls Qt's 'bool QPlatformScreen::isPlaceholder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#isPlaceholder
    """
    #  bool QPlatformScreen::isPlaceholder() const
    ritual = 'ritual_ZNK15QPlatformScreen13isPlaceholderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen13isPlaceholderEv'
    return self.uglySide.call(ritual)

  @overload(int, int, int, int, int)
  def grabWindow(
      self,
      window: int,
      x: int,
      y: int,
      width: int,
      height: int,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPlatformScreen::grabWindow(WId window, int x, int y,
    int width, int height) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#grabWindow

    Parameters
    ----------

    window : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPlatformScreen::grabWindow(WId window, int x, int y, int
    #      width, int height) const
    ritual = 'ritual_ZNK15QPlatformScreen10grabWindowEyiiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen10grabWindowEyiiii'
    address = self.uglySide.call(ritual, window, x, y, width, height)
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformScreen::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformScreen::geometry() const
    address = self.uglySide.call('ritual_ZNK15QPlatformScreen8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def availableGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformScreen::availableGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#availableGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformScreen::availableGeometry() const
    ritual = 'ritual_ZNK15QPlatformScreen17availableGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen17availableGeometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def depth(self) -> int:
    """
    Calls Qt's 'int QPlatformScreen::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#depth
    """
    #  int QPlatformScreen::depth() const
    return self.uglySide.call('ritual_ZNK15QPlatformScreen5depthEv')

  def format(self) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QPlatformScreen::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#format

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QPlatformScreen::format() const
    return QImage.Format(self.uglySide.call(
        'ritual_ZNK15QPlatformScreen6formatEv',
    ))

  def colorSpace(self) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QPlatformScreen::colorSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#colorSpace

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QPlatformScreen::colorSpace() const
    ritual = 'ritual_ZNK15QPlatformScreen10colorSpaceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen10colorSpaceEv'
    address = self.uglySide.call(ritual)
    from . import QColorSpace
    return QColorSpace._cuteOwning(address)

  def physicalSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPlatformScreen::physicalSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#physicalSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPlatformScreen::physicalSize() const
    ritual = 'ritual_ZNK15QPlatformScreen12physicalSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen12physicalSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QPlatformScreen::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#devicePixelRatio
    """
    #  qreal QPlatformScreen::devicePixelRatio() const
    ritual = 'ritual_ZNK15QPlatformScreen16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen16devicePixelRatioEv'
    return self.uglySide.call(ritual)

  def refreshRate(self) -> float:
    """
    Calls Qt's 'qreal QPlatformScreen::refreshRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#refreshRate
    """
    #  qreal QPlatformScreen::refreshRate() const
    ritual = 'ritual_ZNK15QPlatformScreen11refreshRateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen11refreshRateEv'
    return self.uglySide.call(ritual)

  def nativeOrientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QPlatformScreen::nativeOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#nativeOrientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QPlatformScreen::nativeOrientation() const
    ritual = 'ritual_ZNK15QPlatformScreen17nativeOrientationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen17nativeOrientationEv'
    return Qt.ScreenOrientation(self.uglySide.call(ritual))

  def orientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QPlatformScreen::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#orientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QPlatformScreen::orientation() const
    ritual = 'ritual_ZNK15QPlatformScreen11orientationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen11orientationEv'
    return Qt.ScreenOrientation(self.uglySide.call(ritual))

  @overload(QPoint)
  def topLevelAt(self, point: QPoint) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QPlatformScreen::topLevelAt(const QPoint &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#topLevelAt

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QPlatformScreen::topLevelAt(const QPoint &point) const
    ritual = 'ritual_ZNK15QPlatformScreen10topLevelAtERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen10topLevelAtERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(point))
    from . import QWindow
    return QWindow._cuteAt(address)

  def windows(self) -> QList[QWindow]:
    """
    Calls Qt's 'QWindowList QPlatformScreen::windows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#windows

    Returns
    -------

    QList[QWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWindowList QPlatformScreen::windows() const
    address = self.uglySide.call('ritual_ZNK15QPlatformScreen7windowsEv')
    from . import QWindow
    return QList[QWindow]._cuteOwning(address)

  def virtualSiblings(self) -> QList[QPlatformScreen]:
    """
    Calls Qt's 'QList<QPlatformScreen *> QPlatformScreen::virtualSiblings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#virtualSiblings

    Returns
    -------

    QList[QPlatformScreen]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlatformScreen *> QPlatformScreen::virtualSiblings() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformScreen15virtualSiblingsEv',
    )
    return QList[QPlatformScreen]._cuteOwning(address)

  @overload(QPoint)
  def screenForPosition(self, point: QPoint) -> Optional[QPlatformScreen]:
    """
    Calls Qt's 'const QPlatformScreen
    *QPlatformScreen::screenForPosition(const QPoint &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#screenForPosition

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QPlatformScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlatformScreen *QPlatformScreen::screenForPosition(const QPoint
    #      &point) const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformScreen17screenForPositionERK6QPoint',
        self._valueOf(point),
    )
    return QPlatformScreen._cuteAt(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QPlatformScreen::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QPlatformScreen::screen() const
    address = self.uglySide.call('ritual_ZNK15QPlatformScreen6screenEv')
    from . import QScreen
    return QScreen._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlatformScreen::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformScreen::name() const
    ritual = 'ritual_ZNK15QPlatformScreen4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen4nameEv'
    return self.uglySide.call(ritual)

  def manufacturer(self) -> str:
    """
    Calls Qt's 'QString QPlatformScreen::manufacturer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#manufacturer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformScreen::manufacturer() const
    ritual = 'ritual_ZNK15QPlatformScreen12manufacturerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen12manufacturerEv'
    return self.uglySide.call(ritual)

  def model(self) -> str:
    """
    Calls Qt's 'QString QPlatformScreen::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#model

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformScreen::model() const
    ritual = 'ritual_ZNK15QPlatformScreen5modelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen5modelEv'
    return self.uglySide.call(ritual)

  def serialNumber(self) -> str:
    """
    Calls Qt's 'QString QPlatformScreen::serialNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#serialNumber

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformScreen::serialNumber() const
    ritual = 'ritual_ZNK15QPlatformScreen12serialNumberEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen12serialNumberEv'
    return self.uglySide.call(ritual)

  def cursor(self) -> Optional[QPlatformCursor]:
    """
    Calls Qt's 'QPlatformCursor *QPlatformScreen::cursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#cursor

    Returns
    -------

    Optional[QPlatformCursor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformCursor *QPlatformScreen::cursor() const
    ritual = 'ritual_ZNK15QPlatformScreen6cursorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen6cursorEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformCursor
    return QPlatformCursor._cuteAt(address)

  def subpixelAntialiasingTypeHint(self) -> SubpixelAntialiasingType:
    """
    Calls Qt's 'SubpixelAntialiasingType
    QPlatformScreen::subpixelAntialiasingTypeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#subpixelAntialiasingTypeHint

    Returns
    -------

    SubpixelAntialiasingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SubpixelAntialiasingType(number)' gives.
    """
    #  SubpixelAntialiasingType
    #      QPlatformScreen::subpixelAntialiasingTypeHint() const
    ritual = 'ritual_ZNK15QPlatformScreen28subpixelAntialiasingTypeHintEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QPlatformScreen28subpixelAntialiasingTypeHintEv')
    return QPlatformScreen.SubpixelAntialiasingType(self.uglySide.call(
        ritual,
    ))

  def powerState(self) -> PowerState:
    """
    Calls Qt's 'PowerState QPlatformScreen::powerState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#powerState

    Returns
    -------

    PowerState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PowerState(number)'
      gives.
    """
    #  PowerState QPlatformScreen::powerState() const
    ritual = 'ritual_ZNK15QPlatformScreen10powerStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen10powerStateEv'
    return QPlatformScreen.PowerState(self.uglySide.call(ritual))

  def currentMode(self) -> int:
    """
    Calls Qt's 'int QPlatformScreen::currentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#currentMode
    """
    #  int QPlatformScreen::currentMode() const
    ritual = 'ritual_ZNK15QPlatformScreen11currentModeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen11currentModeEv'
    return self.uglySide.call(ritual)

  def preferredMode(self) -> int:
    """
    Calls Qt's 'int QPlatformScreen::preferredMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#preferredMode
    """
    #  int QPlatformScreen::preferredMode() const
    ritual = 'ritual_ZNK15QPlatformScreen13preferredModeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformScreen13preferredModeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PowerState)
  def setPowerState(self, state: PowerState) -> None:
    """
    Calls Qt's 'void QPlatformScreen::setPowerState(PowerState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#setPowerState

    Parameters
    ----------

    state : PowerState
      Passed on as its number.
    """
    #  void QPlatformScreen::setPowerState(PowerState state)
    ritual = 'ritual_ZN15QPlatformScreen13setPowerStateENS_10PowerStateE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QPlatformScreen13setPowerStateENS_10PowerStateE')
    self.uglySide.call(ritual, state.value)

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
    Notes what was given, for Qt's 'QPlatformScreen::QPlatformScreen()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#QPlatformScreen
    """
    #  QPlatformScreen::QPlatformScreen()
    self._noteCreation(QPlatformScreen, lambda: Rituals.call(
        'ritual_ZN15QPlatformScreenC1Ev',
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

  def d_func(self) -> Optional[QPlatformScreenPrivate]:
    """
    Calls Qt's 'QPlatformScreenPrivate *QPlatformScreen::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformscreen.html#d_func

    Returns
    -------

    Optional[QPlatformScreenPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformScreenPrivate *QPlatformScreen::d_func()
    address = self.uglySide.call('ritual_ZN15QPlatformScreen6d_funcEv')
    from . import QPlatformScreenPrivate
    return QPlatformScreenPrivate._cuteAt(address)

  def resizeMaximizedWindows(self) -> None:
    """
    Calls Qt's 'void QPlatformScreen::resizeMaximizedWindows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformscreen.html#resizeMaximizedWindows
    """
    #  void QPlatformScreen::resizeMaximizedWindows()
    self.uglySide.call(
        'ritual_ZN15QPlatformScreen22resizeMaximizedWindowsEv',
    )

  @staticmethod
  def logicalBaseDpi(*__, **_) -> Never:
    """
    Qt's 'QDpi QPlatformScreen::logicalBaseDpi() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformScreen.logicalBaseDpi' has no cute function yet. Qt's "
        "'QDpi QPlatformScreen::logicalBaseDpi() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def logicalDpi(*__, **_) -> Never:
    """
    Qt's 'QDpi QPlatformScreen::logicalDpi() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformScreen.logicalDpi' has no cute function yet. Qt's 'QDpi "
        "QPlatformScreen::logicalDpi() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def modes(*__, **_) -> Never:
    """
    Qt's 'QList<Mode> QPlatformScreen::modes() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformScreen.modes' has no cute function yet. Qt's "
        "'QList<Mode> QPlatformScreen::modes() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def overrideDpi(*__, **_) -> Never:
    """
    Qt's 'QDpi QPlatformScreen::overrideDpi(const QDpi &in)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformScreen.overrideDpi' has no cute function yet. Qt's 'QDpi "
        "QPlatformScreen::overrideDpi(const QDpi &in)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QPlatformScreen *>': the list of QPlatformScreen, which
#  'QList[QPlatformScreen]' gives. It is made here, so that there is one as
#  soon as there can be a QPlatformScreen.
QList.createKind(
    QPlatformScreen, 'address',
    make='ritual_list_make_QPlatformScreen_ptr',
    add='ritual_list_add_QPlatformScreen_ptr',
    size='ritual_list_size_QPlatformScreen_ptr',
    at='ritual_list_at_QPlatformScreen_ptr',
    drop='ritual_list_drop_QPlatformScreen_ptr',
)
