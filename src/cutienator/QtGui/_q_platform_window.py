"""
QPlatformWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformwindow.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPlatformSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMargins, QPoint, QPointF, QRect, QRectF
  from ..QtCore import QSize
  from . import QIcon, QPlatformScreen, QPlatformWindowPrivate, QRegion
  from . import QSurfaceFormat, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QIcon = WAIT['QIcon']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']
  QSize = WAIT['QSize']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformWindow(QPlatformSurface):
  """
  The cute side of Qt's QPlatformWindow: a plain Python object standing in
  front of one C++ QPlatformWindow.

  It is built on the cute 'QPlatformSurface', as Qt's QPlatformWindow is
  built on Qt's QPlatformSurface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformWindow that has a ritual and that Python
  can call so far, 65 names in all: 'd_func', 'initialize', 'window',
  'parent', 'screen', 'format', 'setGeometry', 'geometry', 'normalGeometry',
  'frameMargins', 'safeAreaMargins', 'setVisible', 'setWindowFlags',
  'setWindowState', 'winId', 'setParent', 'setWindowTitle', 'windowTitle',
  'setWindowFilePath', 'setWindowIcon', 'close', 'raise_', 'lower',
  'isExposed', 'isActive', 'isAncestorOf', 'isEmbedded', 'isForeignWindow',
  'mapToGlobal', 'mapToGlobalF', 'mapFromGlobal', 'mapFromGlobalF',
  'propagateSizeHints', 'setOpacity', 'setMask', 'requestActivateWindow',
  'handleContentOrientationChange', 'devicePixelRatio',
  'setKeyboardGrabEnabled', 'setMouseGrabEnabled', 'setWindowModified',
  'windowEvent', 'startSystemResize', 'startSystemMove',
  'setFrameStrutEventsEnabled', 'frameStrutEventsEnabled', 'setAlertState',
  'isAlertState', 'invalidateSurface', 'requestUpdate',
  'hasPendingUpdateRequest', 'deliverUpdateRequest',
  'allowsIndependentThreadedRendering', 'windowMinimumSize',
  'windowMaximumSize', 'windowBaseSize', 'windowSizeIncrement',
  'windowGeometry', 'windowFrameGeometry', 'windowClosestAcceptableGeometry',
  'closestAcceptableGeometry', 'formatWindowTitle', 'screenForGeometry',
  'constrainWindowSize', 'isSubWindow'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPlatformWindowPrivate *QPlatformWindow::d_func() const':
    takes in Python what 'QPlatformWindowPrivate *QPlatformWindow::d_func()'
    takes.
  - Qt's 'QPlatformWindow::~QPlatformWindow()': the destructor: Python never
    removes a C++ QPlatformWindow.
  - Qt's 'QRect QPlatformWindow::initialGeometry(const QWindow *w, const
    QRect &initialGeometry, int defaultWidth, int defaultHeight, const
    QScreen **resultingScreenReturn)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 73 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPlatformWindow is created at the first use, not by
    'QPlatformWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformWindow.
  - Each name of Qt's QPlatformWindow that has no cute function yet,
    'initialGeometry', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWindow, QRectF)
  @overload(NoneType, QRectF)
  def closestAcceptableGeometry(
      w: Optional[QWindow],
      nativeRect: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformWindow::closestAcceptableGeometry(const
    QWindow *w, const QRectF &nativeRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#closestAcceptableGeometry

    Parameters
    ----------

    w : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    nativeRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformWindow::closestAcceptableGeometry(const QWindow *w,
    #      const QRectF &nativeRect)
    address = Rituals.call(
        'ritual_ZN15QPlatformWindow25closestAcceptableGeometryEPK7QWindowRK'
        '6QRectF',
        CuteMixin._addressOf(w), CuteMixin._valueOf(nativeRect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def formatWindowTitle(title: str, separator: str) -> str:
    """
    Calls Qt's 'QString QPlatformWindow::formatWindowTitle(const QString
    &title, const QString &separator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#formatWindowTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    separator : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformWindow::formatWindowTitle(const QString &title, const
    #      QString &separator)
    return Rituals.call(
        'ritual_ZN15QPlatformWindow17formatWindowTitleERK7QStringS2_',
        title, separator,
    )

  @staticmethod
  @overload(QSize)
  def constrainWindowSize(size: QSize) -> QSize:
    """
    Calls Qt's 'QSize QPlatformWindow::constrainWindowSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#constrainWindowSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformWindow::constrainWindowSize(const QSize &size)
    address = Rituals.call(
        'ritual_ZN15QPlatformWindow19constrainWindowSizeERK5QSize',
        CuteMixin._valueOf(size),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def isSubWindow(window: Optional[QWindow]) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::isSubWindow(const QWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#isSubWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlatformWindow::isSubWindow(const QWindow *window)
    return Rituals.call(
        'ritual_ZN15QPlatformWindow11isSubWindowEPK7QWindow',
        CuteMixin._addressOf(window),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformWindow'

  #  A C++ QPlatformWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformWindow'

  #  The functions Qt calls itself that QPlatformWindow is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN15QPlatformWindow10initializeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setGeometry': (
          ('_ZN15QPlatformWindow11setGeometryERK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'geometry': (
          ('_ZNK15QPlatformWindow8geometryEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
      'normalGeometry': (
          ('_ZNK15QPlatformWindow14normalGeometryEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
      'frameMargins': (
          ('_ZNK15QPlatformWindow12frameMarginsEv',
           ('address', 'value', 'QtCore:QMargins'),
           ()),
      ),
      'safeAreaMargins': (
          ('_ZNK15QPlatformWindow15safeAreaMarginsEv',
           ('address', 'value', 'QtCore:QMargins'),
           ()),
      ),
      'setVisible': (
          ('_ZN15QPlatformWindow10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setWindowFlags': (
          ('_ZN15QPlatformWindow14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtCore:Qt.WindowType'),
           )),
      ),
      'setWindowState': (
          ('_ZN15QPlatformWindow14setWindowStateE6QFlagsIN2Qt11WindowStateE'
           'E',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtCore:Qt.WindowState'),
           )),
      ),
      'winId': (
          ('_ZNK15QPlatformWindow5winIdEv',
           ('unsigned long long', 'number', ''),
           ()),
      ),
      'setParent': (
          ('_ZN15QPlatformWindow9setParentEPKS_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformWindow'),
           )),
      ),
      'setWindowTitle': (
          ('_ZN15QPlatformWindow14setWindowTitleERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'windowTitle': (
          ('_ZNK15QPlatformWindow11windowTitleEv',
           ('address', 'text', ''),
           ()),
      ),
      'setWindowFilePath': (
          ('_ZN15QPlatformWindow17setWindowFilePathERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setWindowIcon': (
          ('_ZN15QPlatformWindow13setWindowIconERK5QIcon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QIcon'),
           )),
      ),
      'close': (
          ('_ZN15QPlatformWindow5closeEv',
           ('bool', 'number', ''),
           ()),
      ),
      'raise': (
          ('_ZN15QPlatformWindow5raiseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'lower': (
          ('_ZN15QPlatformWindow5lowerEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isExposed': (
          ('_ZNK15QPlatformWindow9isExposedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isActive': (
          ('_ZNK15QPlatformWindow8isActiveEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isAncestorOf': (
          ('_ZNK15QPlatformWindow12isAncestorOfEPKS_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPlatformWindow'),
           )),
      ),
      'isEmbedded': (
          ('_ZNK15QPlatformWindow10isEmbeddedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isForeignWindow': (
          ('_ZNK15QPlatformWindow15isForeignWindowEv',
           ('bool', 'number', ''),
           ()),
      ),
      'mapToGlobal': (
          ('_ZNK15QPlatformWindow11mapToGlobalERK6QPoint',
           ('address', 'value', 'QtCore:QPoint'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'mapFromGlobal': (
          ('_ZNK15QPlatformWindow13mapFromGlobalERK6QPoint',
           ('address', 'value', 'QtCore:QPoint'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'propagateSizeHints': (
          ('_ZN15QPlatformWindow18propagateSizeHintsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setOpacity': (
          ('_ZN15QPlatformWindow10setOpacityEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setMask': (
          ('_ZN15QPlatformWindow7setMaskERK7QRegion',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QRegion'),
           )),
      ),
      'requestActivateWindow': (
          ('_ZN15QPlatformWindow21requestActivateWindowEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleContentOrientationChange': (
          ('_ZN15QPlatformWindow30handleContentOrientationChangeEN2Qt17Scre'
           'enOrientationE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.ScreenOrientation'),
           )),
      ),
      'devicePixelRatio': (
          ('_ZNK15QPlatformWindow16devicePixelRatioEv',
           ('double', 'number', ''),
           ()),
      ),
      'setKeyboardGrabEnabled': (
          ('_ZN15QPlatformWindow22setKeyboardGrabEnabledEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setMouseGrabEnabled': (
          ('_ZN15QPlatformWindow19setMouseGrabEnabledEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setWindowModified': (
          ('_ZN15QPlatformWindow17setWindowModifiedEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'windowEvent': (
          ('_ZN15QPlatformWindow11windowEventEP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'startSystemResize': (
          ('_ZN15QPlatformWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtCore:Qt.Edge'),
           )),
      ),
      'startSystemMove': (
          ('_ZN15QPlatformWindow15startSystemMoveEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setFrameStrutEventsEnabled': (
          ('_ZN15QPlatformWindow26setFrameStrutEventsEnabledEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'frameStrutEventsEnabled': (
          ('_ZNK15QPlatformWindow23frameStrutEventsEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setAlertState': (
          ('_ZN15QPlatformWindow13setAlertStateEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isAlertState': (
          ('_ZNK15QPlatformWindow12isAlertStateEv',
           ('bool', 'number', ''),
           ()),
      ),
      'invalidateSurface': (
          ('_ZN15QPlatformWindow17invalidateSurfaceEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'requestUpdate': (
          ('_ZN15QPlatformWindow13requestUpdateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'deliverUpdateRequest': (
          ('_ZN15QPlatformWindow20deliverUpdateRequestEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'allowsIndependentThreadedRendering': (
          ('_ZNK15QPlatformWindow34allowsIndependentThreadedRenderingEv',
           ('bool', 'number', ''),
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

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QPlatformWindow::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QPlatformWindow::window() const
    address = self.uglySide.call('ritual_ZNK15QPlatformWindow6windowEv')
    from . import QWindow
    return QWindow._cuteAt(address)

  def parent(self) -> Optional[QPlatformWindow]:
    """
    Calls Qt's 'QPlatformWindow *QPlatformWindow::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#parent

    Returns
    -------

    Optional[QPlatformWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformWindow *QPlatformWindow::parent() const
    address = self.uglySide.call('ritual_ZNK15QPlatformWindow6parentEv')
    return QPlatformWindow._cuteAt(address)

  def screen(self) -> Optional[QPlatformScreen]:
    """
    Calls Qt's 'QPlatformScreen *QPlatformWindow::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#screen

    Returns
    -------

    Optional[QPlatformScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformScreen *QPlatformWindow::screen() const
    ritual = 'ritual_ZNK15QPlatformWindow6screenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow6screenEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformScreen
    return QPlatformScreen._cuteAt(address)

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QPlatformWindow::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QPlatformWindow::format() const
    ritual = 'ritual_ZNK15QPlatformWindow6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow6formatEv'
    address = self.uglySide.call(ritual)
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformWindow::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformWindow::geometry() const
    ritual = 'ritual_ZNK15QPlatformWindow8geometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow8geometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def normalGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformWindow::normalGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#normalGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformWindow::normalGeometry() const
    ritual = 'ritual_ZNK15QPlatformWindow14normalGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow14normalGeometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def frameMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QPlatformWindow::frameMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#frameMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QPlatformWindow::frameMargins() const
    ritual = 'ritual_ZNK15QPlatformWindow12frameMarginsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow12frameMarginsEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def safeAreaMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QPlatformWindow::safeAreaMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#safeAreaMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QPlatformWindow::safeAreaMargins() const
    ritual = 'ritual_ZNK15QPlatformWindow15safeAreaMarginsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow15safeAreaMarginsEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def winId(self) -> int:
    """
    Calls Qt's 'WId QPlatformWindow::winId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#winId
    """
    #  WId QPlatformWindow::winId() const
    ritual = 'ritual_ZNK15QPlatformWindow5winIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow5winIdEv'
    return self.uglySide.call(ritual)

  def windowTitle(self) -> str:
    """
    Calls Qt's 'QString QPlatformWindow::windowTitle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#windowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformWindow::windowTitle() const
    ritual = 'ritual_ZNK15QPlatformWindow11windowTitleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow11windowTitleEv'
    return self.uglySide.call(ritual)

  def isExposed(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::isExposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#isExposed
    """
    #  bool QPlatformWindow::isExposed() const
    ritual = 'ritual_ZNK15QPlatformWindow9isExposedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow9isExposedEv'
    return self.uglySide.call(ritual)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#isActive
    """
    #  bool QPlatformWindow::isActive() const
    ritual = 'ritual_ZNK15QPlatformWindow8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow8isActiveEv'
    return self.uglySide.call(ritual)

  @overload(THIS)
  @overload(NoneType)
  def isAncestorOf(self, child: Optional[QPlatformWindow]) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::isAncestorOf(const QPlatformWindow
    *child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#isAncestorOf

    Parameters
    ----------

    child : Optional[QPlatformWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlatformWindow::isAncestorOf(const QPlatformWindow *child) const
    ritual = 'ritual_ZNK15QPlatformWindow12isAncestorOfEPKS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow12isAncestorOfEPKS_'
    return self.uglySide.call(ritual, self._addressOf(child))

  def isEmbedded(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::isEmbedded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#isEmbedded
    """
    #  bool QPlatformWindow::isEmbedded() const
    ritual = 'ritual_ZNK15QPlatformWindow10isEmbeddedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow10isEmbeddedEv'
    return self.uglySide.call(ritual)

  def isForeignWindow(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::isForeignWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#isForeignWindow
    """
    #  bool QPlatformWindow::isForeignWindow() const
    ritual = 'ritual_ZNK15QPlatformWindow15isForeignWindowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow15isForeignWindowEv'
    return self.uglySide.call(ritual)

  @overload(QPoint)
  def mapToGlobal(self, pos: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QPlatformWindow::mapToGlobal(const QPoint &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#mapToGlobal

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPlatformWindow::mapToGlobal(const QPoint &pos) const
    ritual = 'ritual_ZNK15QPlatformWindow11mapToGlobalERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow11mapToGlobalERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(pos))
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def mapToGlobalF(self, pos: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QPlatformWindow::mapToGlobalF(const QPointF &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#mapToGlobalF

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPlatformWindow::mapToGlobalF(const QPointF &pos) const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow12mapToGlobalFERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint)
  def mapFromGlobal(self, pos: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QPlatformWindow::mapFromGlobal(const QPoint &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#mapFromGlobal

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPlatformWindow::mapFromGlobal(const QPoint &pos) const
    ritual = 'ritual_ZNK15QPlatformWindow13mapFromGlobalERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow13mapFromGlobalERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(pos))
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def mapFromGlobalF(self, pos: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QPlatformWindow::mapFromGlobalF(const QPointF &pos)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#mapFromGlobalF

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPlatformWindow::mapFromGlobalF(const QPointF &pos) const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow14mapFromGlobalFERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QPlatformWindow::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#devicePixelRatio
    """
    #  qreal QPlatformWindow::devicePixelRatio() const
    ritual = 'ritual_ZNK15QPlatformWindow16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow16devicePixelRatioEv'
    return self.uglySide.call(ritual)

  def frameStrutEventsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::frameStrutEventsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#frameStrutEventsEnabled
    """
    #  bool QPlatformWindow::frameStrutEventsEnabled() const
    ritual = 'ritual_ZNK15QPlatformWindow23frameStrutEventsEnabledEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow23frameStrutEventsEnabledEv'
    return self.uglySide.call(ritual)

  def isAlertState(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::isAlertState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#isAlertState
    """
    #  bool QPlatformWindow::isAlertState() const
    ritual = 'ritual_ZNK15QPlatformWindow12isAlertStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformWindow12isAlertStateEv'
    return self.uglySide.call(ritual)

  def hasPendingUpdateRequest(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::hasPendingUpdateRequest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#hasPendingUpdateRequest
    """
    #  bool QPlatformWindow::hasPendingUpdateRequest() const
    return self.uglySide.call(
        'ritual_ZNK15QPlatformWindow23hasPendingUpdateRequestEv',
    )

  def allowsIndependentThreadedRendering(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::allowsIndependentThreadedRendering()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html
    """
    #  bool QPlatformWindow::allowsIndependentThreadedRendering() const
    ritual = (
        'ritual_ZNK15QPlatformWindow34allowsIndependentThreadedRenderingEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QPlatformWindow34allowsIndependentThreadedRender'
          'ingEv')
    return self.uglySide.call(ritual)

  def windowMinimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QPlatformWindow::windowMinimumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#windowMinimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformWindow::windowMinimumSize() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow17windowMinimumSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def windowMaximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QPlatformWindow::windowMaximumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#windowMaximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformWindow::windowMaximumSize() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow17windowMaximumSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def windowBaseSize(self) -> QSize:
    """
    Calls Qt's 'QSize QPlatformWindow::windowBaseSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#windowBaseSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformWindow::windowBaseSize() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow14windowBaseSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def windowSizeIncrement(self) -> QSize:
    """
    Calls Qt's 'QSize QPlatformWindow::windowSizeIncrement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#windowSizeIncrement

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformWindow::windowSizeIncrement() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow19windowSizeIncrementEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def windowGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformWindow::windowGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#windowGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformWindow::windowGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow14windowGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def windowFrameGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformWindow::windowFrameGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#windowFrameGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformWindow::windowFrameGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow19windowFrameGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRectF)
  def windowClosestAcceptableGeometry(self, nativeRect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformWindow::windowClosestAcceptableGeometry(const
    QRectF &nativeRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html

    Parameters
    ----------

    nativeRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformWindow::windowClosestAcceptableGeometry(const QRectF
    #      &nativeRect) const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow31windowClosestAcceptableGeometryERK6QR'
        'ectF',
        self._valueOf(nativeRect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRect)
  def screenForGeometry(
      self,
      newGeometry: QRect,
  ) -> Optional[QPlatformScreen]:
    """
    Calls Qt's 'QPlatformScreen *QPlatformWindow::screenForGeometry(const
    QRect &newGeometry) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#screenForGeometry

    Parameters
    ----------

    newGeometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    Optional[QPlatformScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformScreen *QPlatformWindow::screenForGeometry(const QRect
    #      &newGeometry) const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformWindow17screenForGeometryERK5QRect',
        self._valueOf(newGeometry),
    )
    from . import QPlatformScreen
    return QPlatformScreen._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setGeometry(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setGeometry(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#setGeometry

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPlatformWindow::setGeometry(const QRect &rect)
    ritual = 'ritual_ZN15QPlatformWindow11setGeometryERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow11setGeometryERK5QRect'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QPlatformWindow::setVisible(bool visible)
    ritual = 'ritual_ZN15QPlatformWindow10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(Qt.WindowFlags)
  def setWindowFlags(self, flags: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setWindowFlags(Qt::WindowFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setWindowFlags

    Parameters
    ----------

    flags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QPlatformWindow::setWindowFlags(Qt::WindowFlags flags)
    ritual = (
        'ritual_ZN15QPlatformWindow14setWindowFlagsE6QFlagsIN2Qt10WindowTyp'
        'eEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QPlatformWindow14setWindowFlagsE6QFlagsIN2Qt10Win'
          'dowTypeEE')
    self.uglySide.call(ritual, flags.value)

  @overload(Qt.WindowStates)
  def setWindowState(self, state: Qt.WindowStates) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setWindowState(Qt::WindowStates
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setWindowState

    Parameters
    ----------

    state : Qt.WindowStates
      Passed on as its number.
    """
    #  void QPlatformWindow::setWindowState(Qt::WindowStates state)
    ritual = (
        'ritual_ZN15QPlatformWindow14setWindowStateE6QFlagsIN2Qt11WindowSta'
        'teEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QPlatformWindow14setWindowStateE6QFlagsIN2Qt11Win'
          'dowStateEE')
    self.uglySide.call(ritual, state.value)

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, window: Optional[QPlatformWindow]) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setParent(const QPlatformWindow
    *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#setParent

    Parameters
    ----------

    window : Optional[QPlatformWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformWindow::setParent(const QPlatformWindow *window)
    ritual = 'ritual_ZN15QPlatformWindow9setParentEPKS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow9setParentEPKS_'
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(str)
  def setWindowTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setWindowTitle(const QString &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setWindowTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformWindow::setWindowTitle(const QString &title)
    ritual = 'ritual_ZN15QPlatformWindow14setWindowTitleERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow14setWindowTitleERK7QString'
    self.uglySide.call(ritual, title)

  @overload(str)
  def setWindowFilePath(self, title: str) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setWindowFilePath(const QString
    &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setWindowFilePath

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformWindow::setWindowFilePath(const QString &title)
    ritual = 'ritual_ZN15QPlatformWindow17setWindowFilePathERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow17setWindowFilePathERK7QString'
    self.uglySide.call(ritual, title)

  @overload(QIcon)
  def setWindowIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setWindowIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#setWindowIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QPlatformWindow::setWindowIcon(const QIcon &icon)
    ritual = 'ritual_ZN15QPlatformWindow13setWindowIconERK5QIcon'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow13setWindowIconERK5QIcon'
    self.uglySide.call(ritual, self._valueOf(icon))

  @overload(float)
  def setOpacity(self, level: float) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setOpacity(qreal level)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#setOpacity

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QPlatformWindow::setOpacity(qreal level)
    ritual = 'ritual_ZN15QPlatformWindow10setOpacityEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow10setOpacityEd'
    self.uglySide.call(ritual, level)

  @overload(QRegion)
  def setMask(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setMask(const QRegion &region)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#setMask

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPlatformWindow::setMask(const QRegion &region)
    ritual = 'ritual_ZN15QPlatformWindow7setMaskERK7QRegion'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow7setMaskERK7QRegion'
    self.uglySide.call(ritual, self._valueOf(region))

  @overload(bool)
  def setKeyboardGrabEnabled(self, grab: bool) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::setKeyboardGrabEnabled(bool grab)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setKeyboardGrabEnabled

    Parameters
    ----------

    grab : bool
      Passed on as it is.
    """
    #  bool QPlatformWindow::setKeyboardGrabEnabled(bool grab)
    ritual = 'ritual_ZN15QPlatformWindow22setKeyboardGrabEnabledEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow22setKeyboardGrabEnabledEb'
    return self.uglySide.call(ritual, grab)

  @overload(bool)
  def setMouseGrabEnabled(self, grab: bool) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::setMouseGrabEnabled(bool grab)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setMouseGrabEnabled

    Parameters
    ----------

    grab : bool
      Passed on as it is.
    """
    #  bool QPlatformWindow::setMouseGrabEnabled(bool grab)
    ritual = 'ritual_ZN15QPlatformWindow19setMouseGrabEnabledEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow19setMouseGrabEnabledEb'
    return self.uglySide.call(ritual, grab)

  @overload(bool)
  def setWindowModified(self, modified: bool) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::setWindowModified(bool modified)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setWindowModified

    Parameters
    ----------

    modified : bool
      Passed on as it is.
    """
    #  bool QPlatformWindow::setWindowModified(bool modified)
    ritual = 'ritual_ZN15QPlatformWindow17setWindowModifiedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow17setWindowModifiedEb'
    return self.uglySide.call(ritual, modified)

  @overload(bool)
  def setFrameStrutEventsEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setFrameStrutEventsEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#setFrameStrutEventsEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPlatformWindow::setFrameStrutEventsEnabled(bool enabled)
    ritual = 'ritual_ZN15QPlatformWindow26setFrameStrutEventsEnabledEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow26setFrameStrutEventsEnabledEb'
    self.uglySide.call(ritual, enabled)

  @overload(bool)
  def setAlertState(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPlatformWindow::setAlertState(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#setAlertState

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPlatformWindow::setAlertState(bool enabled)
    ritual = 'ritual_ZN15QPlatformWindow13setAlertStateEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow13setAlertStateEb'
    self.uglySide.call(ritual, enabled)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's 'QPlatformWindow::QPlatformWindow(QWindow
    *window)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#QPlatformWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformWindow::QPlatformWindow(QWindow *window)
    self._noteCreation(QPlatformWindow, lambda: Rituals.call(
        'ritual_ZN15QPlatformWindowC1EP7QWindow', self._addressOf(window),
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

  def d_func(self) -> Optional[QPlatformWindowPrivate]:
    """
    Calls Qt's 'QPlatformWindowPrivate *QPlatformWindow::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#d_func

    Returns
    -------

    Optional[QPlatformWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformWindowPrivate *QPlatformWindow::d_func()
    address = self.uglySide.call('ritual_ZN15QPlatformWindow6d_funcEv')
    from . import QPlatformWindowPrivate
    return QPlatformWindowPrivate._cuteAt(address)

  def initialize(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#initialize
    """
    #  void QPlatformWindow::initialize()
    ritual = 'ritual_ZN15QPlatformWindow10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow10initializeEv'
    self.uglySide.call(ritual)

  def close(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#close
    """
    #  bool QPlatformWindow::close()
    ritual = 'ritual_ZN15QPlatformWindow5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow5closeEv'
    return self.uglySide.call(ritual)

  def raise_(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::raise()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#raise
    """
    #  void QPlatformWindow::raise()
    ritual = 'ritual_ZN15QPlatformWindow5raiseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow5raiseEv'
    self.uglySide.call(ritual)

  def lower(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::lower()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#lower
    """
    #  void QPlatformWindow::lower()
    ritual = 'ritual_ZN15QPlatformWindow5lowerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow5lowerEv'
    self.uglySide.call(ritual)

  def propagateSizeHints(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::propagateSizeHints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#propagateSizeHints
    """
    #  void QPlatformWindow::propagateSizeHints()
    ritual = 'ritual_ZN15QPlatformWindow18propagateSizeHintsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow18propagateSizeHintsEv'
    self.uglySide.call(ritual)

  def requestActivateWindow(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::requestActivateWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#requestActivateWindow
    """
    #  void QPlatformWindow::requestActivateWindow()
    ritual = 'ritual_ZN15QPlatformWindow21requestActivateWindowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow21requestActivateWindowEv'
    self.uglySide.call(ritual)

  @overload(Qt.ScreenOrientation)
  def handleContentOrientationChange(
      self,
      orientation: Qt.ScreenOrientation,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformWindow::handleContentOrientationChange(Qt::ScreenOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html

    Parameters
    ----------

    orientation : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  void QPlatformWindow::handleContentOrientationChange(Qt::
    #      ScreenOrientation orientation)
    ritual = (
        'ritual_ZN15QPlatformWindow30handleContentOrientationChangeEN2Qt17S'
        'creenOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QPlatformWindow30handleContentOrientationChangeEN'
          '2Qt17ScreenOrientationE')
    self.uglySide.call(ritual, orientation.value)

  @overload(QEvent)
  @overload(NoneType)
  def windowEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::windowEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#windowEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlatformWindow::windowEvent(QEvent *event)
    ritual = 'ritual_ZN15QPlatformWindow11windowEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow11windowEventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(Qt.Edges)
  def startSystemResize(self, edges: Qt.Edges) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::startSystemResize(Qt::Edges edges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#startSystemResize

    Parameters
    ----------

    edges : Qt.Edges
      Passed on as its number.
    """
    #  bool QPlatformWindow::startSystemResize(Qt::Edges edges)
    ritual = (
        'ritual_ZN15QPlatformWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QPlatformWindow17startSystemResizeE6QFlagsIN2Qt4E'
          'dgeEE')
    return self.uglySide.call(ritual, edges.value)

  def startSystemMove(self) -> bool:
    """
    Calls Qt's 'bool QPlatformWindow::startSystemMove()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#startSystemMove
    """
    #  bool QPlatformWindow::startSystemMove()
    ritual = 'ritual_ZN15QPlatformWindow15startSystemMoveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow15startSystemMoveEv'
    return self.uglySide.call(ritual)

  def invalidateSurface(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::invalidateSurface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#invalidateSurface
    """
    #  void QPlatformWindow::invalidateSurface()
    ritual = 'ritual_ZN15QPlatformWindow17invalidateSurfaceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow17invalidateSurfaceEv'
    self.uglySide.call(ritual)

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::requestUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformwindow.html#requestUpdate
    """
    #  void QPlatformWindow::requestUpdate()
    ritual = 'ritual_ZN15QPlatformWindow13requestUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow13requestUpdateEv'
    self.uglySide.call(ritual)

  def deliverUpdateRequest(self) -> None:
    """
    Calls Qt's 'void QPlatformWindow::deliverUpdateRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformwindow.html#deliverUpdateRequest
    """
    #  void QPlatformWindow::deliverUpdateRequest()
    ritual = 'ritual_ZN15QPlatformWindow20deliverUpdateRequestEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformWindow20deliverUpdateRequestEv'
    self.uglySide.call(ritual)

  @staticmethod
  def initialGeometry(*__, **_) -> Never:
    """
    Qt's 'QRect QPlatformWindow::initialGeometry(const QWindow *w, const
    QRect &initialGeometry, int defaultWidth, int defaultHeight, const
    QScreen **resultingScreenReturn)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QPlatformWindow.initialGeometry' has no cute function yet. Qt's "
        "'QRect QPlatformWindow::initialGeometry(const QWindow *w, const "
        "QRect &initialGeometry, int defaultWidth, int defaultHeight, const "
        "QScreen **resultingScreenReturn)': takes a type Python has no way "
        "to hand over yet.")
