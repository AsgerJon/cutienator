"""
QWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qwindow.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMargins, QMetaObject, QPoint, QPointF, QRect
  from ..QtCore import QSize
  from . import QAccessibleInterface, QCloseEvent, QCursor, QExposeEvent
  from . import QFocusEvent, QHideEvent, QIcon, QKeyEvent, QMouseEvent
  from . import QMoveEvent, QPaintEvent, QRegion, QResizeEvent, QScreen
  from . import QShowEvent, QSurfaceFormat, QTabletEvent, QTouchEvent
  from . import QWheelEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCloseEvent = WAIT['QCloseEvent']
  QCursor = WAIT['QCursor']
  QEvent = WAIT['QEvent']
  QExposeEvent = WAIT['QExposeEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHideEvent = WAIT['QHideEvent']
  QIcon = WAIT['QIcon']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QMoveEvent = WAIT['QMoveEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']
  QResizeEvent = WAIT['QResizeEvent']
  QScreen = WAIT['QScreen']
  QShowEvent = WAIT['QShowEvent']
  QSize = WAIT['QSize']
  QSurfaceFormat = WAIT['QSurfaceFormat']
  QTabletEvent = WAIT['QTabletEvent']
  QTouchEvent = WAIT['QTouchEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindow(QObject, QSurface):
  """
  The cute side of Qt's QWindow: a plain Python object standing in front of
  one C++ QWindow.

  It is built on the cute 'QObject', as Qt's QWindow is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QSurface' as well, as Qt's QWindow is built on Qt's QSurface too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWindow that has a ritual and that Python can call
  so far, 126 names in all: 'metaObject', 'tr', 'setSurfaceType',
  'surfaceType', 'isVisible', 'visibility', 'setVisibility', 'create',
  'winId', 'parent', 'setParent', 'isTopLevel', 'isModal', 'modality',
  'setModality', 'setFormat', 'format', 'requestedFormat', 'setFlags',
  'flags', 'setFlag', 'type', 'title', 'setOpacity', 'opacity', 'setMask',
  'mask', 'isActive', 'reportContentOrientationChange', 'contentOrientation',
  'devicePixelRatio', 'windowState', 'windowStates', 'setWindowState',
  'setWindowStates', 'setTransientParent', 'transientParent', 'isAncestorOf',
  'isExposed', 'minimumWidth', 'minimumHeight', 'maximumWidth',
  'maximumHeight', 'minimumSize', 'maximumSize', 'baseSize', 'sizeIncrement',
  'setMinimumSize', 'setMaximumSize', 'setBaseSize', 'setSizeIncrement',
  'geometry', 'frameMargins', 'frameGeometry', 'framePosition',
  'setFramePosition', 'safeAreaMargins', 'width', 'height', 'x', 'y', 'size',
  'position', 'setPosition', 'resize', 'setFilePath', 'filePath', 'setIcon',
  'icon', 'destroy', 'setKeyboardGrabEnabled', 'setMouseGrabEnabled',
  'screen', 'setScreen', 'accessibleRoot', 'focusObject', 'mapToGlobal',
  'mapFromGlobal', 'cursor', 'setCursor', 'unsetCursor', 'fromWinId',
  'requestActivate', 'setVisible', 'show', 'hide', 'showMinimized',
  'showMaximized', 'showFullScreen', 'showNormal', 'close', 'raise_',
  'lower', 'startSystemResize', 'startSystemMove', 'setTitle', 'setX',
  'setY', 'setWidth', 'setHeight', 'setGeometry', 'setMinimumWidth',
  'setMinimumHeight', 'setMaximumWidth', 'setMaximumHeight', 'alert',
  'requestUpdate', 'exposeEvent', 'resizeEvent', 'paintEvent', 'moveEvent',
  'focusInEvent', 'focusOutEvent', 'showEvent', 'hideEvent', 'closeEvent',
  'event', 'keyPressEvent', 'keyReleaseEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'mouseMoveEvent',
  'wheelEvent', 'touchEvent', 'tabletEvent'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWindow::~QWindow()': the destructor: Python never removes a C++
    QWindow.

  What has no ritual
  ------------------

  37 of the 172 functions Qt declares: 21 a signal; 5 takes or gives a type
  that cannot be passed yet; 4 private; 3 protected; 2 a template; 2
  forbidden.

  What to expect
  --------------

  - The C++ QWindow is created at the first use, not by 'QWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindow.
  - Qt tells when it has removed the C++ QWindow. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QWindow, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class AncestorMode(CuteNum):
    """
    The enum 'QWindow::AncestorMode' of Qt, with the 2 names Qt gives in it.
    """

    ExcludeTransients = Kee[int](0)
    IncludeTransients = Kee[int](1)

  class Visibility(CuteNum):
    """
    The enum 'QWindow::Visibility' of Qt, with the 6 names Qt gives in it.
    """

    Hidden = Kee[int](0)
    AutomaticVisibility = Kee[int](1)
    Windowed = Kee[int](2)
    Minimized = Kee[int](3)
    Maximized = Kee[int](4)
    FullScreen = Kee[int](5)

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
    Calls Qt's 'QString QWindow::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#tr

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
    #  QString QWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int)
  def fromWinId(id: int) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWindow::fromWinId(WId id)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#fromWinId

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWindow::fromWinId(WId id)
    address = Rituals.call('ritual_ZN7QWindow9fromWinIdEy', id)
    return QWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindow'

  #  Qt's QWindow is built on more than one class. The part of a C++ QWindow
  #  that belongs to a class after the first begins somewhere inside the
  #  object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSurface': 'ritual_cast_QWindow_QSurface',
  }

  #  A C++ QWindow Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindow'

  #  The functions Qt calls itself that QWindow is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nativeEvent': (
          'bool QWindow::nativeEvent(const QByteArray &, void *, qintptr *)',
      ),
  }

  #  The functions Qt calls itself that QWindow is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'accessibleRoot': (
          ('_ZNK7QWindow14accessibleRootEv',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           ()),
      ),
      'focusObject': (
          ('_ZNK7QWindow11focusObjectEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'exposeEvent': (
          ('_ZN7QWindow11exposeEventEP12QExposeEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QExposeEvent'),
           )),
      ),
      'resizeEvent': (
          ('_ZN7QWindow11resizeEventEP12QResizeEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QResizeEvent'),
           )),
      ),
      'paintEvent': (
          ('_ZN7QWindow10paintEventEP11QPaintEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPaintEvent'),
           )),
      ),
      'moveEvent': (
          ('_ZN7QWindow9moveEventEP10QMoveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMoveEvent'),
           )),
      ),
      'focusInEvent': (
          ('_ZN7QWindow12focusInEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'focusOutEvent': (
          ('_ZN7QWindow13focusOutEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'showEvent': (
          ('_ZN7QWindow9showEventEP10QShowEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QShowEvent'),
           )),
      ),
      'hideEvent': (
          ('_ZN7QWindow9hideEventEP10QHideEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QHideEvent'),
           )),
      ),
      'closeEvent': (
          ('_ZN7QWindow10closeEventEP11QCloseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QCloseEvent'),
           )),
      ),
      'keyPressEvent': (
          ('_ZN7QWindow13keyPressEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'keyReleaseEvent': (
          ('_ZN7QWindow15keyReleaseEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'mousePressEvent': (
          ('_ZN7QWindow15mousePressEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseReleaseEvent': (
          ('_ZN7QWindow17mouseReleaseEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseDoubleClickEvent': (
          ('_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseMoveEvent': (
          ('_ZN7QWindow14mouseMoveEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'wheelEvent': (
          ('_ZN7QWindow10wheelEventEP11QWheelEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWheelEvent'),
           )),
      ),
      'touchEvent': (
          ('_ZN7QWindow10touchEventEP11QTouchEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QTouchEvent'),
           )),
      ),
      'tabletEvent': (
          ('_ZN7QWindow11tabletEventEP12QTabletEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QTabletEvent'),
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
    Calls Qt's 'const QMetaObject *QWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def surfaceType(self) -> QSurface.SurfaceType:
    """
    Calls Qt's 'SurfaceType QWindow::surfaceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#surfaceType

    Returns
    -------

    QSurface.SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurface.SurfaceType(number)' gives.
    """
    #  SurfaceType QWindow::surfaceType() const
    ritual = 'ritual_ZNK7QWindow11surfaceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWindow11surfaceTypeEv'
    return QSurface.SurfaceType(self.uglySide.call(ritual))

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QWindow::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#isVisible
    """
    #  bool QWindow::isVisible() const
    return self.uglySide.call('ritual_ZNK7QWindow9isVisibleEv')

  def visibility(self) -> Visibility:
    """
    Calls Qt's 'Visibility QWindow::visibility() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#visibility

    Returns
    -------

    Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Visibility(number)'
      gives.
    """
    #  Visibility QWindow::visibility() const
    return QWindow.Visibility(self.uglySide.call(
        'ritual_ZNK7QWindow10visibilityEv',
    ))

  def winId(self) -> int:
    """
    Calls Qt's 'WId QWindow::winId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#winId
    """
    #  WId QWindow::winId() const
    return self.uglySide.call('ritual_ZNK7QWindow5winIdEv')

  @overload()
  @overload(AncestorMode)
  def parent(
      self,
      mode: AncestorMode = AncestorMode.ExcludeTransients,
  ) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWindow::parent(AncestorMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#parent

    Parameters
    ----------

    mode : AncestorMode
      Passed on as its number. May be left out, as in Qt: it is then
      AncestorMode.ExcludeTransients.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWindow::parent(AncestorMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK7QWindow6parentENS_12AncestorModeE', mode.value,
    )
    return QWindow._cuteAt(address)

  def isTopLevel(self) -> bool:
    """
    Calls Qt's 'bool QWindow::isTopLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#isTopLevel
    """
    #  bool QWindow::isTopLevel() const
    return self.uglySide.call('ritual_ZNK7QWindow10isTopLevelEv')

  def isModal(self) -> bool:
    """
    Calls Qt's 'bool QWindow::isModal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#isModal
    """
    #  bool QWindow::isModal() const
    return self.uglySide.call('ritual_ZNK7QWindow7isModalEv')

  def modality(self) -> Qt.WindowModality:
    """
    Calls Qt's 'Qt::WindowModality QWindow::modality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#modality

    Returns
    -------

    Qt.WindowModality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.WindowModality(number)' gives.
    """
    #  Qt::WindowModality QWindow::modality() const
    return Qt.WindowModality(self.uglySide.call(
        'ritual_ZNK7QWindow8modalityEv',
    ))

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QWindow::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QWindow::format() const
    ritual = 'ritual_ZNK7QWindow6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWindow6formatEv'
    address = self.uglySide.call(ritual)
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def requestedFormat(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QWindow::requestedFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#requestedFormat

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QWindow::requestedFormat() const
    address = self.uglySide.call('ritual_ZNK7QWindow15requestedFormatEv')
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def flags(self) -> Qt.WindowFlags:
    """
    Calls Qt's 'Qt::WindowFlags QWindow::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#flags

    Returns
    -------

    Qt.WindowFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowFlags QWindow::flags() const
    return Qt.WindowFlags(self.uglySide.call('ritual_ZNK7QWindow5flagsEv'))

  def type(self) -> Qt.WindowType:
    """
    Calls Qt's 'Qt::WindowType QWindow::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#type

    Returns
    -------

    Qt.WindowType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowType(number)'
      gives.
    """
    #  Qt::WindowType QWindow::type() const
    return Qt.WindowType(self.uglySide.call('ritual_ZNK7QWindow4typeEv'))

  def title(self) -> str:
    """
    Calls Qt's 'QString QWindow::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWindow::title() const
    return self.uglySide.call('ritual_ZNK7QWindow5titleEv')

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QWindow::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#opacity
    """
    #  qreal QWindow::opacity() const
    return self.uglySide.call('ritual_ZNK7QWindow7opacityEv')

  def mask(self) -> QRegion:
    """
    Calls Qt's 'QRegion QWindow::mask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mask

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWindow::mask() const
    address = self.uglySide.call('ritual_ZNK7QWindow4maskEv')
    from . import QRegion
    return QRegion._cuteOwning(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QWindow::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#isActive
    """
    #  bool QWindow::isActive() const
    return self.uglySide.call('ritual_ZNK7QWindow8isActiveEv')

  def contentOrientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QWindow::contentOrientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#contentOrientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QWindow::contentOrientation() const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK7QWindow18contentOrientationEv',
    ))

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QWindow::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#devicePixelRatio
    """
    #  qreal QWindow::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK7QWindow16devicePixelRatioEv')

  def windowState(self) -> Qt.WindowState:
    """
    Calls Qt's 'Qt::WindowState QWindow::windowState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#windowState

    Returns
    -------

    Qt.WindowState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowState(number)'
      gives.
    """
    #  Qt::WindowState QWindow::windowState() const
    return Qt.WindowState(self.uglySide.call(
        'ritual_ZNK7QWindow11windowStateEv',
    ))

  def windowStates(self) -> Qt.WindowStates:
    """
    Calls Qt's 'Qt::WindowStates QWindow::windowStates() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#windowStates

    Returns
    -------

    Qt.WindowStates
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowStates QWindow::windowStates() const
    return Qt.WindowStates(self.uglySide.call(
        'ritual_ZNK7QWindow12windowStatesEv',
    ))

  def transientParent(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWindow::transientParent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#transientParent

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWindow::transientParent() const
    address = self.uglySide.call('ritual_ZNK7QWindow15transientParentEv')
    return QWindow._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  @overload(THIS, AncestorMode)
  @overload(NoneType, AncestorMode)
  def isAncestorOf(
      self,
      child: Optional[QWindow],
      mode: AncestorMode = AncestorMode.IncludeTransients,
  ) -> bool:
    """
    Calls Qt's 'bool QWindow::isAncestorOf(const QWindow *child, AncestorMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#isAncestorOf

    Parameters
    ----------

    child : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : AncestorMode
      Passed on as its number. May be left out, as in Qt: it is then
      AncestorMode.IncludeTransients.
    """
    #  bool QWindow::isAncestorOf(const QWindow *child, AncestorMode mode)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QWindow12isAncestorOfEPKS_NS_12AncestorModeE',
        self._addressOf(child), mode.value,
    )

  def isExposed(self) -> bool:
    """
    Calls Qt's 'bool QWindow::isExposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#isExposed
    """
    #  bool QWindow::isExposed() const
    return self.uglySide.call('ritual_ZNK7QWindow9isExposedEv')

  def minimumWidth(self) -> int:
    """
    Calls Qt's 'int QWindow::minimumWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#minimumWidth
    """
    #  int QWindow::minimumWidth() const
    return self.uglySide.call('ritual_ZNK7QWindow12minimumWidthEv')

  def minimumHeight(self) -> int:
    """
    Calls Qt's 'int QWindow::minimumHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#minimumHeight
    """
    #  int QWindow::minimumHeight() const
    return self.uglySide.call('ritual_ZNK7QWindow13minimumHeightEv')

  def maximumWidth(self) -> int:
    """
    Calls Qt's 'int QWindow::maximumWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#maximumWidth
    """
    #  int QWindow::maximumWidth() const
    return self.uglySide.call('ritual_ZNK7QWindow12maximumWidthEv')

  def maximumHeight(self) -> int:
    """
    Calls Qt's 'int QWindow::maximumHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#maximumHeight
    """
    #  int QWindow::maximumHeight() const
    return self.uglySide.call('ritual_ZNK7QWindow13maximumHeightEv')

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWindow::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWindow::minimumSize() const
    address = self.uglySide.call('ritual_ZNK7QWindow11minimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWindow::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWindow::maximumSize() const
    address = self.uglySide.call('ritual_ZNK7QWindow11maximumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def baseSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWindow::baseSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#baseSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWindow::baseSize() const
    address = self.uglySide.call('ritual_ZNK7QWindow8baseSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeIncrement(self) -> QSize:
    """
    Calls Qt's 'QSize QWindow::sizeIncrement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#sizeIncrement

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWindow::sizeIncrement() const
    address = self.uglySide.call('ritual_ZNK7QWindow13sizeIncrementEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWindow::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWindow::geometry() const
    address = self.uglySide.call('ritual_ZNK7QWindow8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def frameMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QWindow::frameMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#frameMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QWindow::frameMargins() const
    address = self.uglySide.call('ritual_ZNK7QWindow12frameMarginsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def frameGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWindow::frameGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#frameGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWindow::frameGeometry() const
    address = self.uglySide.call('ritual_ZNK7QWindow13frameGeometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def framePosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWindow::framePosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#framePosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWindow::framePosition() const
    address = self.uglySide.call('ritual_ZNK7QWindow13framePositionEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def safeAreaMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QWindow::safeAreaMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#safeAreaMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QWindow::safeAreaMargins() const
    address = self.uglySide.call('ritual_ZNK7QWindow15safeAreaMarginsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QWindow::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#width
    """
    #  int QWindow::width() const
    return self.uglySide.call('ritual_ZNK7QWindow5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QWindow::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#height
    """
    #  int QWindow::height() const
    return self.uglySide.call('ritual_ZNK7QWindow6heightEv')

  def x(self) -> int:
    """
    Calls Qt's 'int QWindow::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#x
    """
    #  int QWindow::x() const
    return self.uglySide.call('ritual_ZNK7QWindow1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QWindow::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#y
    """
    #  int QWindow::y() const
    return self.uglySide.call('ritual_ZNK7QWindow1yEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QWindow::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWindow::size() const
    ritual = 'ritual_ZNK7QWindow4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWindow4sizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def position(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWindow::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#position

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWindow::position() const
    address = self.uglySide.call('ritual_ZNK7QWindow8positionEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QWindow::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWindow::filePath() const
    return self.uglySide.call('ritual_ZNK7QWindow8filePathEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QWindow::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QWindow::icon() const
    address = self.uglySide.call('ritual_ZNK7QWindow4iconEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QWindow::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QWindow::screen() const
    address = self.uglySide.call('ritual_ZNK7QWindow6screenEv')
    from . import QScreen
    return QScreen._cuteAt(address)

  def accessibleRoot(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QWindow::accessibleRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#accessibleRoot

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QWindow::accessibleRoot() const
    ritual = 'ritual_ZNK7QWindow14accessibleRootEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWindow14accessibleRootEv'
    address = self.uglySide.call(ritual)
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  def focusObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QWindow::focusObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#focusObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QWindow::focusObject() const
    ritual = 'ritual_ZNK7QWindow11focusObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWindow11focusObjectEv'
    address = self.uglySide.call(ritual)
    return QObject._cuteAt(address)

  @overload(QPointF)
  def mapToGlobal(self, pos: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWindow::mapToGlobal(const QPointF &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mapToGlobal

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
    #  QPointF QWindow::mapToGlobal(const QPointF &pos) const
    address = self.uglySide.call(
        'ritual_ZNK7QWindow11mapToGlobalERK7QPointF', self._valueOf(pos),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint)
  def mapToGlobal(self, pos: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWindow::mapToGlobal(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mapToGlobal

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
    #  QPoint QWindow::mapToGlobal(const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK7QWindow11mapToGlobalERK6QPoint', self._valueOf(pos),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def mapFromGlobal(self, pos: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWindow::mapFromGlobal(const QPointF &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mapFromGlobal

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
    #  QPointF QWindow::mapFromGlobal(const QPointF &pos) const
    address = self.uglySide.call(
        'ritual_ZNK7QWindow13mapFromGlobalERK7QPointF', self._valueOf(pos),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint)
  def mapFromGlobal(self, pos: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWindow::mapFromGlobal(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mapFromGlobal

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
    #  QPoint QWindow::mapFromGlobal(const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK7QWindow13mapFromGlobalERK6QPoint', self._valueOf(pos),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def cursor(self) -> QCursor:
    """
    Calls Qt's 'QCursor QWindow::cursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#cursor

    Returns
    -------

    QCursor
      A new cute QCursor around the copy Qt gave back. Python owns it.
    """
    #  QCursor QWindow::cursor() const
    address = self.uglySide.call('ritual_ZNK7QWindow6cursorEv')
    from . import QCursor
    return QCursor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSurface.SurfaceType)
  def setSurfaceType(self, surfaceType: QSurface.SurfaceType) -> None:
    """
    Calls Qt's 'void QWindow::setSurfaceType(SurfaceType surfaceType)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setSurfaceType

    Parameters
    ----------

    surfaceType : QSurface.SurfaceType
      Passed on as its number.
    """
    #  void QWindow::setSurfaceType(SurfaceType surfaceType)
    self.uglySide.call(
        'ritual_ZN7QWindow14setSurfaceTypeEN8QSurface11SurfaceTypeE',
        surfaceType.value,
    )

  @overload(Visibility)
  def setVisibility(self, v: Visibility) -> None:
    """
    Calls Qt's 'void QWindow::setVisibility(Visibility v)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setVisibility

    Parameters
    ----------

    v : Visibility
      Passed on as its number.
    """
    #  void QWindow::setVisibility(Visibility v)
    self.uglySide.call(
        'ritual_ZN7QWindow13setVisibilityENS_10VisibilityE', v.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, parent: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QWindow::setParent(QWindow *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setParent

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::setParent(QWindow *parent)
    self.uglySide.call(
        'ritual_ZN7QWindow9setParentEPS_', self._addressOf(parent),
    )

  @overload(Qt.WindowModality)
  def setModality(self, modality: Qt.WindowModality) -> None:
    """
    Calls Qt's 'void QWindow::setModality(Qt::WindowModality modality)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setModality

    Parameters
    ----------

    modality : Qt.WindowModality
      Passed on as its number.
    """
    #  void QWindow::setModality(Qt::WindowModality modality)
    self.uglySide.call(
        'ritual_ZN7QWindow11setModalityEN2Qt14WindowModalityE',
        modality.value,
    )

  @overload(QSurfaceFormat)
  def setFormat(self, format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QWindow::setFormat(const QSurfaceFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setFormat

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QWindow::setFormat(const QSurfaceFormat &format)
    self.uglySide.call(
        'ritual_ZN7QWindow9setFormatERK14QSurfaceFormat',
        self._valueOf(format),
    )

  @overload(Qt.WindowFlags)
  def setFlags(self, flags: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QWindow::setFlags(Qt::WindowFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setFlags

    Parameters
    ----------

    flags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QWindow::setFlags(Qt::WindowFlags flags)
    self.uglySide.call(
        'ritual_ZN7QWindow8setFlagsE6QFlagsIN2Qt10WindowTypeEE', flags.value,
    )

  @overload(Qt.WindowType)
  @overload(Qt.WindowType, bool)
  def setFlag(self, a0: Qt.WindowType, on: bool = True) -> None:
    """
    Calls Qt's 'void QWindow::setFlag(Qt::WindowType a0, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setFlag

    Parameters
    ----------

    a0 : Qt.WindowType
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWindow::setFlag(Qt::WindowType a0, bool on)
    self.uglySide.call(
        'ritual_ZN7QWindow7setFlagEN2Qt10WindowTypeEb', a0.value, on,
    )

  @overload(float)
  def setOpacity(self, level: float) -> None:
    """
    Calls Qt's 'void QWindow::setOpacity(qreal level)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setOpacity

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QWindow::setOpacity(qreal level)
    self.uglySide.call('ritual_ZN7QWindow10setOpacityEd', level)

  @overload(QRegion)
  def setMask(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QWindow::setMask(const QRegion &region)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMask

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWindow::setMask(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN7QWindow7setMaskERK7QRegion', self._valueOf(region),
    )

  @overload(Qt.WindowState)
  def setWindowState(self, state: Qt.WindowState) -> None:
    """
    Calls Qt's 'void QWindow::setWindowState(Qt::WindowState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setWindowState

    Parameters
    ----------

    state : Qt.WindowState
      Passed on as its number.
    """
    #  void QWindow::setWindowState(Qt::WindowState state)
    self.uglySide.call(
        'ritual_ZN7QWindow14setWindowStateEN2Qt11WindowStateE', state.value,
    )

  @overload(Qt.WindowStates)
  def setWindowStates(self, states: Qt.WindowStates) -> None:
    """
    Calls Qt's 'void QWindow::setWindowStates(Qt::WindowStates states)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setWindowStates

    Parameters
    ----------

    states : Qt.WindowStates
      Passed on as its number.
    """
    #  void QWindow::setWindowStates(Qt::WindowStates states)
    self.uglySide.call(
        'ritual_ZN7QWindow15setWindowStatesE6QFlagsIN2Qt11WindowStateEE',
        states.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setTransientParent(self, parent: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QWindow::setTransientParent(QWindow *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setTransientParent

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::setTransientParent(QWindow *parent)
    self.uglySide.call(
        'ritual_ZN7QWindow18setTransientParentEPS_', self._addressOf(parent),
    )

  @overload(QSize)
  def setMinimumSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWindow::setMinimumSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMinimumSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWindow::setMinimumSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN7QWindow14setMinimumSizeERK5QSize', self._valueOf(size),
    )

  @overload(QSize)
  def setMaximumSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWindow::setMaximumSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMaximumSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWindow::setMaximumSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN7QWindow14setMaximumSizeERK5QSize', self._valueOf(size),
    )

  @overload(QSize)
  def setBaseSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWindow::setBaseSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setBaseSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWindow::setBaseSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN7QWindow11setBaseSizeERK5QSize', self._valueOf(size),
    )

  @overload(QSize)
  def setSizeIncrement(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWindow::setSizeIncrement(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setSizeIncrement

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWindow::setSizeIncrement(const QSize &size)
    self.uglySide.call(
        'ritual_ZN7QWindow16setSizeIncrementERK5QSize', self._valueOf(size),
    )

  @overload(QPoint)
  def setFramePosition(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QWindow::setFramePosition(const QPoint &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setFramePosition

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWindow::setFramePosition(const QPoint &point)
    self.uglySide.call(
        'ritual_ZN7QWindow16setFramePositionERK6QPoint',
        self._valueOf(point),
    )

  @overload(int, int)
  def setFramePosition(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QWindow::setFramePosition(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setFramePosition

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QWindow::setFramePosition(int x, int y)
    self.uglySide.call('ritual_ZN7QWindow16setFramePositionEii', x, y)

  @overload(QPoint)
  def setPosition(self, pt: QPoint) -> None:
    """
    Calls Qt's 'void QWindow::setPosition(const QPoint &pt)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setPosition

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWindow::setPosition(const QPoint &pt)
    self.uglySide.call(
        'ritual_ZN7QWindow11setPositionERK6QPoint', self._valueOf(pt),
    )

  @overload(int, int)
  def setPosition(self, posx: int, posy: int) -> None:
    """
    Calls Qt's 'void QWindow::setPosition(int posx, int posy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setPosition

    Parameters
    ----------

    posx : int
      Passed on as it is.

    posy : int
      Passed on as it is.
    """
    #  void QWindow::setPosition(int posx, int posy)
    self.uglySide.call('ritual_ZN7QWindow11setPositionEii', posx, posy)

  @overload(str)
  def setFilePath(self, filePath: str) -> None:
    """
    Calls Qt's 'void QWindow::setFilePath(const QString &filePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setFilePath

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWindow::setFilePath(const QString &filePath)
    self.uglySide.call('ritual_ZN7QWindow11setFilePathERK7QString', filePath)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QWindow::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QWindow::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN7QWindow7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(bool)
  def setKeyboardGrabEnabled(self, grab: bool) -> bool:
    """
    Calls Qt's 'bool QWindow::setKeyboardGrabEnabled(bool grab)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindow.html#setKeyboardGrabEnabled

    Parameters
    ----------

    grab : bool
      Passed on as it is.
    """
    #  bool QWindow::setKeyboardGrabEnabled(bool grab)
    return self.uglySide.call(
        'ritual_ZN7QWindow22setKeyboardGrabEnabledEb', grab,
    )

  @overload(bool)
  def setMouseGrabEnabled(self, grab: bool) -> bool:
    """
    Calls Qt's 'bool QWindow::setMouseGrabEnabled(bool grab)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMouseGrabEnabled

    Parameters
    ----------

    grab : bool
      Passed on as it is.
    """
    #  bool QWindow::setMouseGrabEnabled(bool grab)
    return self.uglySide.call(
        'ritual_ZN7QWindow19setMouseGrabEnabledEb', grab,
    )

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QWindow::setScreen(QScreen *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::setScreen(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN7QWindow9setScreenEP7QScreen', self._addressOf(screen),
    )

  @overload(QCursor)
  def setCursor(self, a0: QCursor) -> None:
    """
    Calls Qt's 'void QWindow::setCursor(const QCursor &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setCursor

    Parameters
    ----------

    a0 : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QWindow::setCursor(const QCursor &a0)
    self.uglySide.call(
        'ritual_ZN7QWindow9setCursorERK7QCursor', self._valueOf(a0),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QWindow::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QWindow::setVisible(bool visible)
    self.uglySide.call('ritual_ZN7QWindow10setVisibleEb', visible)

  @overload(str)
  def setTitle(self, a0: str) -> None:
    """
    Calls Qt's 'void QWindow::setTitle(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setTitle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWindow::setTitle(const QString &a0)
    self.uglySide.call('ritual_ZN7QWindow8setTitleERK7QString', a0)

  @overload(int)
  def setX(self, arg: int) -> None:
    """
    Calls Qt's 'void QWindow::setX(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setX

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QWindow::setX(int arg)
    self.uglySide.call('ritual_ZN7QWindow4setXEi', arg)

  @overload(int)
  def setY(self, arg: int) -> None:
    """
    Calls Qt's 'void QWindow::setY(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setY

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QWindow::setY(int arg)
    self.uglySide.call('ritual_ZN7QWindow4setYEi', arg)

  @overload(int)
  def setWidth(self, arg: int) -> None:
    """
    Calls Qt's 'void QWindow::setWidth(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setWidth

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QWindow::setWidth(int arg)
    self.uglySide.call('ritual_ZN7QWindow8setWidthEi', arg)

  @overload(int)
  def setHeight(self, arg: int) -> None:
    """
    Calls Qt's 'void QWindow::setHeight(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setHeight

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QWindow::setHeight(int arg)
    self.uglySide.call('ritual_ZN7QWindow9setHeightEi', arg)

  @overload(int, int, int, int)
  def setGeometry(self, posx: int, posy: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWindow::setGeometry(int posx, int posy, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setGeometry

    Parameters
    ----------

    posx : int
      Passed on as it is.

    posy : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWindow::setGeometry(int posx, int posy, int w, int h)
    self.uglySide.call(
        'ritual_ZN7QWindow11setGeometryEiiii', posx, posy, w, h,
    )

  @overload(QRect)
  def setGeometry(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QWindow::setGeometry(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setGeometry

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWindow::setGeometry(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN7QWindow11setGeometryERK5QRect', self._valueOf(rect),
    )

  @overload(int)
  def setMinimumWidth(self, w: int) -> None:
    """
    Calls Qt's 'void QWindow::setMinimumWidth(int w)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMinimumWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QWindow::setMinimumWidth(int w)
    self.uglySide.call('ritual_ZN7QWindow15setMinimumWidthEi', w)

  @overload(int)
  def setMinimumHeight(self, h: int) -> None:
    """
    Calls Qt's 'void QWindow::setMinimumHeight(int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMinimumHeight

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void QWindow::setMinimumHeight(int h)
    self.uglySide.call('ritual_ZN7QWindow16setMinimumHeightEi', h)

  @overload(int)
  def setMaximumWidth(self, w: int) -> None:
    """
    Calls Qt's 'void QWindow::setMaximumWidth(int w)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMaximumWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QWindow::setMaximumWidth(int w)
    self.uglySide.call('ritual_ZN7QWindow15setMaximumWidthEi', w)

  @overload(int)
  def setMaximumHeight(self, h: int) -> None:
    """
    Calls Qt's 'void QWindow::setMaximumHeight(int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#setMaximumHeight

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void QWindow::setMaximumHeight(int h)
    self.uglySide.call('ritual_ZN7QWindow16setMaximumHeightEi', h)

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
  @overload(QScreen)
  @overload(NoneType)
  def __init__(self, screen: Optional[QScreen] = None) -> None:
    """
    Notes what was given, for Qt's 'QWindow::QWindow(QScreen *screen)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#QWindow

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWindow::QWindow(QScreen *screen)
    self._noteCreation(QWindow, lambda: Rituals.call(
        'ritual_ZN7QWindowC1EP7QScreen', self._addressOf(screen),
    ))

  @overload(THIS)
  def __init__(self, parent: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's 'QWindow::QWindow(QWindow *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#QWindow

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWindow::QWindow(QWindow *parent)
    self._noteCreation(QWindow, lambda: Rituals.call(
        'ritual_ZN7QWindowC1EPS_', self._addressOf(parent),
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

  def create(self) -> None:
    """
    Calls Qt's 'void QWindow::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#create
    """
    #  void QWindow::create()
    self.uglySide.call('ritual_ZN7QWindow6createEv')

  @overload(Qt.ScreenOrientation)
  def reportContentOrientationChange(
      self,
      orientation: Qt.ScreenOrientation,
  ) -> None:
    """
    Calls Qt's 'void
    QWindow::reportContentOrientationChange(Qt::ScreenOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindow.html#reportContentOrientationChange

    Parameters
    ----------

    orientation : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  void QWindow::reportContentOrientationChange(Qt::ScreenOrientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN7QWindow30reportContentOrientationChangeEN2Qt17ScreenOrie'
        'ntationE',
        orientation.value,
    )

  @overload(QSize)
  def resize(self, newSize: QSize) -> None:
    """
    Calls Qt's 'void QWindow::resize(const QSize &newSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#resize

    Parameters
    ----------

    newSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWindow::resize(const QSize &newSize)
    self.uglySide.call(
        'ritual_ZN7QWindow6resizeERK5QSize', self._valueOf(newSize),
    )

  @overload(int, int)
  def resize(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWindow::resize(int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#resize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWindow::resize(int w, int h)
    self.uglySide.call('ritual_ZN7QWindow6resizeEii', w, h)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QWindow::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#destroy
    """
    #  void QWindow::destroy()
    self.uglySide.call('ritual_ZN7QWindow7destroyEv')

  def unsetCursor(self) -> None:
    """
    Calls Qt's 'void QWindow::unsetCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#unsetCursor
    """
    #  void QWindow::unsetCursor()
    self.uglySide.call('ritual_ZN7QWindow11unsetCursorEv')

  def requestActivate(self) -> None:
    """
    Calls Qt's 'void QWindow::requestActivate()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#requestActivate
    """
    #  void QWindow::requestActivate()
    self.uglySide.call('ritual_ZN7QWindow15requestActivateEv')

  def show(self) -> None:
    """
    Calls Qt's 'void QWindow::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#show
    """
    #  void QWindow::show()
    self.uglySide.call('ritual_ZN7QWindow4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QWindow::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#hide
    """
    #  void QWindow::hide()
    self.uglySide.call('ritual_ZN7QWindow4hideEv')

  def showMinimized(self) -> None:
    """
    Calls Qt's 'void QWindow::showMinimized()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#showMinimized
    """
    #  void QWindow::showMinimized()
    self.uglySide.call('ritual_ZN7QWindow13showMinimizedEv')

  def showMaximized(self) -> None:
    """
    Calls Qt's 'void QWindow::showMaximized()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#showMaximized
    """
    #  void QWindow::showMaximized()
    self.uglySide.call('ritual_ZN7QWindow13showMaximizedEv')

  def showFullScreen(self) -> None:
    """
    Calls Qt's 'void QWindow::showFullScreen()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#showFullScreen
    """
    #  void QWindow::showFullScreen()
    self.uglySide.call('ritual_ZN7QWindow14showFullScreenEv')

  def showNormal(self) -> None:
    """
    Calls Qt's 'void QWindow::showNormal()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#showNormal
    """
    #  void QWindow::showNormal()
    self.uglySide.call('ritual_ZN7QWindow10showNormalEv')

  def close(self) -> bool:
    """
    Calls Qt's 'bool QWindow::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#close
    """
    #  bool QWindow::close()
    return self.uglySide.call('ritual_ZN7QWindow5closeEv')

  def raise_(self) -> None:
    """
    Calls Qt's 'void QWindow::raise()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#raise
    """
    #  void QWindow::raise()
    self.uglySide.call('ritual_ZN7QWindow5raiseEv')

  def lower(self) -> None:
    """
    Calls Qt's 'void QWindow::lower()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#lower
    """
    #  void QWindow::lower()
    self.uglySide.call('ritual_ZN7QWindow5lowerEv')

  @overload(Qt.Edges)
  def startSystemResize(self, edges: Qt.Edges) -> bool:
    """
    Calls Qt's 'bool QWindow::startSystemResize(Qt::Edges edges)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#startSystemResize

    Parameters
    ----------

    edges : Qt.Edges
      Passed on as its number.
    """
    #  bool QWindow::startSystemResize(Qt::Edges edges)
    return self.uglySide.call(
        'ritual_ZN7QWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE',
        edges.value,
    )

  def startSystemMove(self) -> bool:
    """
    Calls Qt's 'bool QWindow::startSystemMove()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#startSystemMove
    """
    #  bool QWindow::startSystemMove()
    return self.uglySide.call('ritual_ZN7QWindow15startSystemMoveEv')

  @overload(int)
  def alert(self, msec: int) -> None:
    """
    Calls Qt's 'void QWindow::alert(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#alert

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QWindow::alert(int msec)
    self.uglySide.call('ritual_ZN7QWindow5alertEi', msec)

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void QWindow::requestUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#requestUpdate
    """
    #  void QWindow::requestUpdate()
    self.uglySide.call('ritual_ZN7QWindow13requestUpdateEv')

  @overload(QExposeEvent)
  @overload(NoneType)
  def exposeEvent(self, a0: Optional[QExposeEvent]) -> None:
    """
    Calls Qt's 'void QWindow::exposeEvent(QExposeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#exposeEvent

    Parameters
    ----------

    a0 : Optional[QExposeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::exposeEvent(QExposeEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow11exposeEventEP12QExposeEvent',
        self._addressOf(a0),
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QWindow::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::resizeEvent(QResizeEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow11resizeEventEP12QResizeEvent',
        self._addressOf(a0),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QWindow::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::paintEvent(QPaintEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow10paintEventEP11QPaintEvent',
        self._addressOf(a0),
    )

  @overload(QMoveEvent)
  @overload(NoneType)
  def moveEvent(self, a0: Optional[QMoveEvent]) -> None:
    """
    Calls Qt's 'void QWindow::moveEvent(QMoveEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#moveEvent

    Parameters
    ----------

    a0 : Optional[QMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::moveEvent(QMoveEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow9moveEventEP10QMoveEvent', self._addressOf(a0),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QWindow::focusInEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#focusInEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::focusInEvent(QFocusEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow12focusInEventEP11QFocusEvent',
        self._addressOf(a0),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QWindow::focusOutEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#focusOutEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::focusOutEvent(QFocusEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow13focusOutEventEP11QFocusEvent',
        self._addressOf(a0),
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, a0: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QWindow::showEvent(QShowEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#showEvent

    Parameters
    ----------

    a0 : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::showEvent(QShowEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow9showEventEP10QShowEvent', self._addressOf(a0),
    )

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QWindow::hideEvent(QHideEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::hideEvent(QHideEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow9hideEventEP10QHideEvent', self._addressOf(a0),
    )

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, a0: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QWindow::closeEvent(QCloseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#closeEvent

    Parameters
    ----------

    a0 : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::closeEvent(QCloseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow10closeEventEP11QCloseEvent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWindow::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWindow::event(QEvent *a0)
    return self.uglySide.call(
        'ritual_own_ZN7QWindow5eventEP6QEvent', self._addressOf(a0),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWindow::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::keyPressEvent(QKeyEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow13keyPressEventEP9QKeyEvent',
        self._addressOf(a0),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWindow::keyReleaseEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#keyReleaseEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::keyReleaseEvent(QKeyEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow15keyReleaseEventEP9QKeyEvent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWindow::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::mousePressEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow15mousePressEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWindow::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mouseDoubleClickEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWindow::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::mouseMoveEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow14mouseMoveEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, a0: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QWindow::wheelEvent(QWheelEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#wheelEvent

    Parameters
    ----------

    a0 : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::wheelEvent(QWheelEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow10wheelEventEP11QWheelEvent',
        self._addressOf(a0),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, a0: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QWindow::touchEvent(QTouchEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#touchEvent

    Parameters
    ----------

    a0 : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::touchEvent(QTouchEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow10touchEventEP11QTouchEvent',
        self._addressOf(a0),
    )

  @overload(QTabletEvent)
  @overload(NoneType)
  def tabletEvent(self, a0: Optional[QTabletEvent]) -> None:
    """
    Calls Qt's 'void QWindow::tabletEvent(QTabletEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindow.html#tabletEvent

    Parameters
    ----------

    a0 : Optional[QTabletEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindow::tabletEvent(QTabletEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN7QWindow11tabletEventEP12QTabletEvent',
        self._addressOf(a0),
    )


#  Qt's 'QList<QWindow *>': the list of QWindow, which 'QList[QWindow]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QWindow. Qt has a name of its own for it.
QWindowList = QList.createKind(
    QWindow, 'address',
    name='QWindowList',
    make='ritual_list_make_QWindow_ptr',
    add='ritual_list_add_QWindow_ptr',
    size='ritual_list_size_QWindow_ptr',
    at='ritual_list_at_QWindow_ptr',
    drop='ritual_list_drop_QWindow_ptr',
)
