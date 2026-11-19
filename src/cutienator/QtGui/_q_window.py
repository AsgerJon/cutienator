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

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ._q_cursor import QCursor
from ._q_icon import QIcon
from ..QtCore import QMargins
from ..QtCore import QMetaObject
from ..QtCore import QObject
from ..QtCore import QPoint
from ..QtCore import QPointF
from ..QtCore import QRect
from ._q_region import QRegion
from ._q_screen import QScreen
from ..QtCore import QSize
from ._q_surface import QSurface
from ._q_window_ancestor_mode import AncestorMode
from ._q_window_visibility import Visibility

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindow(QObject):
  """
  The cute side of Qt's QWindow: a plain Python object standing in front of
  one C++ QWindow.

  It is built on the cute 'QObject', as Qt's QWindow is built on Qt's
  QObject, and has everything that class has. Qt's QWindow is built on Qt's
  QSurface as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QWindow that has a ritual and that Python can call
  so far, 103 names in all: 'metaObject', 'tr', 'setSurfaceType',
  'surfaceType', 'isVisible', 'visibility', 'setVisibility', 'create',
  'winId', 'parent', 'setParent', 'isTopLevel', 'isModal', 'modality',
  'setModality', 'setFlags', 'flags', 'setFlag', 'type', 'title',
  'setOpacity', 'opacity', 'setMask', 'mask', 'isActive',
  'reportContentOrientationChange', 'contentOrientation', 'devicePixelRatio',
  'windowState', 'windowStates', 'setWindowState', 'setWindowStates',
  'setTransientParent', 'transientParent', 'isAncestorOf', 'isExposed',
  'minimumWidth', 'minimumHeight', 'maximumWidth', 'maximumHeight',
  'minimumSize', 'maximumSize', 'baseSize', 'sizeIncrement',
  'setMinimumSize', 'setMaximumSize', 'setBaseSize', 'setSizeIncrement',
  'geometry', 'frameMargins', 'frameGeometry', 'framePosition',
  'setFramePosition', 'safeAreaMargins', 'width', 'height', 'x', 'y', 'size',
  'position', 'setPosition', 'resize', 'setFilePath', 'filePath', 'setIcon',
  'icon', 'destroy', 'setKeyboardGrabEnabled', 'setMouseGrabEnabled',
  'screen', 'setScreen', 'focusObject', 'mapToGlobal', 'mapFromGlobal',
  'cursor', 'setCursor', 'unsetCursor', 'fromWinId', 'requestActivate',
  'setVisible', 'show', 'hide', 'showMinimized', 'showMaximized',
  'showFullScreen', 'showNormal', 'close', 'raise_', 'lower',
  'startSystemResize', 'startSystemMove', 'setTitle', 'setX', 'setY',
  'setWidth', 'setHeight', 'setGeometry', 'setMinimumWidth',
  'setMinimumHeight', 'setMaximumWidth', 'setMaximumHeight', 'alert',
  'requestUpdate'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWindow::~QWindow()': the destructor: Python never removes a C++
    QWindow.
  - Qt's 'void QWindow::setFormat(const QSurfaceFormat &format)': names
    'QSurfaceFormat', which has no cute class yet.
  - Qt's 'QSurfaceFormat QWindow::format() const': gives 'QSurfaceFormat',
    which has no cute class yet.
  - Qt's 'QSurfaceFormat QWindow::requestedFormat() const': gives
    'QSurfaceFormat', which has no cute class yet.
  - Qt's 'QAccessibleInterface *QWindow::accessibleRoot() const': gives
    'QAccessibleInterface', which has no cute class yet.

  What has no ritual
  ------------------

  56 of the 172 functions Qt declares: 22 protected; 21 a signal; 5 takes or
  gives a type that cannot be passed yet; 4 private; 2 a template; 2
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

  #  The enums Qt writes inside QWindow, and the names Qt has for the
  #  combinations of its flags enums.
  AncestorMode = AncestorMode
  Visibility = Visibility

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
    return QSurface.SurfaceType(self.uglySide.call(
        'ritual_ZNK7QWindow11surfaceTypeEv',
    ))

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
    return Visibility(self.uglySide.call('ritual_ZNK7QWindow10visibilityEv'))

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
    address = self.uglySide.call('ritual_ZNK7QWindow4sizeEv')
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
    return QScreen._cuteAt(address)

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
    address = self.uglySide.call('ritual_ZNK7QWindow11focusObjectEv')
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
