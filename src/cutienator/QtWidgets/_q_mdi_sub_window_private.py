"""
QMdiSubWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMdiSubWindowPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QStyle, QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect, QSize
  from ..QtGui import QPalette
  from . import QMdiSubWindow, QStyleOptionTitleBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QStyleOptionTitleBar = WAIT['QStyleOptionTitleBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMdiSubWindowPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QMdiSubWindowPrivate: a plain Python object standing
  in front of one C++ QMdiSubWindowPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QMdiSubWindowPrivate is
  built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMdiSubWindowPrivate that has a ritual and that
  Python can call so far, 36 names in all: 'q_func',
  '_q_updateStaysOnTopHint', '_q_enterInteractiveMode',
  'leaveInteractiveMode', 'removeBaseWidget', 'initOperationMap',
  'updateCursor', 'updateDirtyRegions', 'updateGeometryConstraints',
  'updateMask', 'getOperation', 'titleBarOptions', 'ensureWindowState',
  'titleBarHeight', 'drawTitleBarWhenMaximized', 'updateWindowTitle',
  'enterRubberBandMode', 'leaveRubberBandMode', 'desktopPalette',
  'setFocusWidget', 'restoreFocus', 'storeFocusWidget', 'setWindowFlags',
  'setEnabled', 'addToSystemMenu', 'iconSize', 'setSizeGripVisible',
  'originalWindowTitle', 'originalWindowTitleHelper', 'setNewWindowTitle',
  'getSubControl', 'setNewGeometry', 'hasBorder', 'autoRaise',
  'isResizeOperation', 'isMoveOperation'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMdiSubWindow *QMdiSubWindowPrivate::q_func() const': takes
    in Python what 'QMdiSubWindow *QMdiSubWindowPrivate::q_func()' takes.

  What has no ritual
  ------------------

  18 of the 56 functions Qt declares: 11 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 7 leans on
  'QMdiSubWindowPrivate.

  What to expect
  --------------

  - The C++ QMdiSubWindowPrivate is created at the first use, not by
    'QMdiSubWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMdiSubWindowPrivate.
  - Each name of Qt's QMdiSubWindowPrivate that has no cute function yet,
    '__init__', '_q_processFocusChanged', 'createSystemMenu', 'getRegion',
    'menuBar', 'processClickedSubControl', 'removeButtonsFromMenuBar',
    'setActive', 'setMaximizeMode', 'setMinimizeMode', 'setNormalMode',
    'setSizeGrip', 'showButtonsInMenuBar', 'sizeParameters', 'updateActions',
    'updateInternalWindowTitle', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMdiSubWindowPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ChangeFlag(CuteNum):
    """
    The enum 'QMdiSubWindowPrivate::ChangeFlag' of Qt, with the 6 names Qt
    gives in it.
    """

    HMove = Kee[int](1)
    VMove = Kee[int](2)
    HResize = Kee[int](4)
    VResize = Kee[int](8)
    HResizeReverse = Kee[int](16)
    VResizeReverse = Kee[int](32)

  class Operation(CuteNum):
    """
    The enum 'QMdiSubWindowPrivate::Operation' of Qt, with the 10 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Move = Kee[int](1)
    TopResize = Kee[int](2)
    BottomResize = Kee[int](3)
    LeftResize = Kee[int](4)
    RightResize = Kee[int](5)
    TopLeftResize = Kee[int](6)
    TopRightResize = Kee[int](7)
    BottomLeftResize = Kee[int](8)
    BottomRightResize = Kee[int](9)

  class WindowStateAction(CuteNum):
    """
    The enum 'QMdiSubWindowPrivate::WindowStateAction' of Qt, with the 8
    names Qt gives in it.
    """

    RestoreAction = Kee[int](0)
    MoveAction = Kee[int](1)
    ResizeAction = Kee[int](2)
    MinimizeAction = Kee[int](3)
    MaximizeAction = Kee[int](4)
    StayOnTopAction = Kee[int](5)
    CloseAction = Kee[int](6)
    NumWindowStateActions = Kee[int](7)

  #  The classes Qt writes inside QMdiSubWindowPrivate, each a class in here
  #  as in C++.

  class OperationInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QMdiSubWindowPrivate::OperationInfo: a plain Python
    object standing in front of one C++ QMdiSubWindowPrivate::OperationInfo.

    C++ hands a QMdiSubWindowPrivate::OperationInfo around as a copy, so
    every C++ QMdiSubWindowPrivate::OperationInfo behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QMdiSubWindowPrivate::OperationInfo yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QMdiSubWindowPrivate::OperationInfo::~OperationInfo()': the
      destructor: Python removes its C++ QMdiSubWindowPrivate::OperationInfo
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QMdiSubWindowPrivate::OperationInfo is created at the first
      use, not by 'QMdiSubWindowPrivate::OperationInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QMdiSubWindowPrivate::OperationInfo back gives a
      copy the ritual made for Python, in a new cute
      QMdiSubWindowPrivate::OperationInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QMdiSubWindowPrivate::OperationInfo'

    #  Qt's '~QMdiSubWindowPrivate::OperationInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QMdiSubWindowPrivate::OperationInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN20QMdiSubWindowPrivate13OperationInfoD1Ev'

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

    @overload(int, Qt.CursorShape)
    @overload(int, Qt.CursorShape, bool)
    def __init__(
        self,
        changeFlags: int,
        cursorShape: Qt.CursorShape,
        hover: bool = True,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QMdiSubWindowPrivate::OperationInfo::OperationInfo(uint changeFlags,
      Qt::CursorShape cursorShape, bool hover)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmdisubwindowprivate-operationinfo.html

      Parameters
      ----------

      changeFlags : int
        Passed on as it is.

      cursorShape : Qt.CursorShape
        Passed on as its number.

      hover : bool
        Passed on as it is. May be left out, as in Qt: it is then True.
      """
      #  QMdiSubWindowPrivate::OperationInfo::OperationInfo(uint changeFlags,
      #      Qt::CursorShape cursorShape, bool hover)
      self._noteCreation(
          QMdiSubWindowPrivate.OperationInfo, lambda: Rituals.call(
              'ritual_ZN20QMdiSubWindowPrivate13OperationInfoC1EjN2Qt11Curs'
              'orShapeEb',
              changeFlags, cursorShape.value, hover,
          ))

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdiSubWindowPrivate'

  #  A C++ QMdiSubWindowPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMdiSubWindowPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def getOperation(self, pos: QPoint) -> Operation:
    """
    Calls Qt's 'Operation QMdiSubWindowPrivate::getOperation(const QPoint
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#getOperation

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operation(number)' gives.
    """
    #  Operation QMdiSubWindowPrivate::getOperation(const QPoint &pos) const
    return QMdiSubWindowPrivate.Operation(self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate12getOperationERK6QPoint',
        self._valueOf(pos),
    ))

  def titleBarOptions(self) -> QStyleOptionTitleBar:
    """
    Calls Qt's 'QStyleOptionTitleBar QMdiSubWindowPrivate::titleBarOptions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#titleBarOptions

    Returns
    -------

    QStyleOptionTitleBar
      A new cute QStyleOptionTitleBar around the copy Qt gave back. Python
      owns it.
    """
    #  QStyleOptionTitleBar QMdiSubWindowPrivate::titleBarOptions() const
    address = self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate15titleBarOptionsEv',
    )
    from . import QStyleOptionTitleBar
    return QStyleOptionTitleBar._cuteOwning(address)

  @overload(QStyleOptionTitleBar)
  def titleBarHeight(self, options: QStyleOptionTitleBar) -> int:
    """
    Calls Qt's 'int QMdiSubWindowPrivate::titleBarHeight(const
    QStyleOptionTitleBar &options) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#titleBarHeight

    Parameters
    ----------

    options : QStyleOptionTitleBar
      Passed on as a value: Qt reads the C++ QStyleOptionTitleBar, which
      stays Python's own.
    """
    #  int QMdiSubWindowPrivate::titleBarHeight(const QStyleOptionTitleBar
    #      &options) const
    return self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate14titleBarHeightERK20QStyleOptionT'
        'itleBar',
        self._valueOf(options),
    )

  @overload()
  def titleBarHeight(self) -> int:
    """
    Calls Qt's 'int QMdiSubWindowPrivate::titleBarHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#titleBarHeight
    """
    #  int QMdiSubWindowPrivate::titleBarHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate14titleBarHeightEv',
    )

  def drawTitleBarWhenMaximized(self) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindowPrivate::drawTitleBarWhenMaximized()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html
    """
    #  bool QMdiSubWindowPrivate::drawTitleBarWhenMaximized() const
    return self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate25drawTitleBarWhenMaximizedEv',
    )

  def desktopPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QMdiSubWindowPrivate::desktopPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#desktopPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QMdiSubWindowPrivate::desktopPalette() const
    address = self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate14desktopPaletteEv',
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QMdiSubWindowPrivate::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindowprivate.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMdiSubWindowPrivate::iconSize() const
    address = self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate8iconSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def originalWindowTitleHelper(self) -> str:
    """
    Calls Qt's 'QString QMdiSubWindowPrivate::originalWindowTitleHelper()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMdiSubWindowPrivate::originalWindowTitleHelper() const
    return self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate25originalWindowTitleHelperEv',
    )

  @overload(QPoint)
  def getSubControl(self, pos: QPoint) -> QStyle.SubControl:
    """
    Calls Qt's 'QStyle::SubControl QMdiSubWindowPrivate::getSubControl(const
    QPoint &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#getSubControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  QStyle::SubControl QMdiSubWindowPrivate::getSubControl(const QPoint
    #      &pos) const
    return QStyle.SubControl(self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate13getSubControlERK6QPoint',
        self._valueOf(pos),
    ))

  @overload(QStyleOptionTitleBar)
  def hasBorder(self, options: QStyleOptionTitleBar) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindowPrivate::hasBorder(const
    QStyleOptionTitleBar &options) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#hasBorder

    Parameters
    ----------

    options : QStyleOptionTitleBar
      Passed on as a value: Qt reads the C++ QStyleOptionTitleBar, which
      stays Python's own.
    """
    #  bool QMdiSubWindowPrivate::hasBorder(const QStyleOptionTitleBar
    #      &options) const
    return self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate9hasBorderERK20QStyleOptionTitleBa'
        'r',
        self._valueOf(options),
    )

  def autoRaise(self) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindowPrivate::autoRaise() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#autoRaise
    """
    #  bool QMdiSubWindowPrivate::autoRaise() const
    return self.uglySide.call('ritual_ZNK20QMdiSubWindowPrivate9autoRaiseEv')

  def isResizeOperation(self) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindowPrivate::isResizeOperation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#isResizeOperation
    """
    #  bool QMdiSubWindowPrivate::isResizeOperation() const
    return self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate17isResizeOperationEv',
    )

  def isMoveOperation(self) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindowPrivate::isMoveOperation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#isMoveOperation
    """
    #  bool QMdiSubWindowPrivate::isMoveOperation() const
    return self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate15isMoveOperationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setFocusWidget(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::setFocusWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#setFocusWidget
    """
    #  void QMdiSubWindowPrivate::setFocusWidget()
    self.uglySide.call('ritual_ZN20QMdiSubWindowPrivate14setFocusWidgetEv')

  @overload(Qt.WindowFlags)
  def setWindowFlags(self, windowFlags: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::setWindowFlags(Qt::WindowFlags
    windowFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#setWindowFlags

    Parameters
    ----------

    windowFlags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QMdiSubWindowPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate14setWindowFlagsE6QFlagsIN2Qt10Wind'
        'owTypeEE',
        windowFlags.value,
    )

  @overload(WindowStateAction)
  @overload(WindowStateAction, bool)
  def setEnabled(self, a0: WindowStateAction, enable: bool = True) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::setEnabled(WindowStateAction a0,
    bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#setEnabled

    Parameters
    ----------

    a0 : WindowStateAction
      Passed on as its number.

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMdiSubWindowPrivate::setEnabled(WindowStateAction a0, bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate10setEnabledENS_17WindowStateAction'
        'Eb',
        a0.value, enable,
    )

  @overload()
  @overload(bool)
  def setSizeGripVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::setSizeGripVisible(bool visible)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#setSizeGripVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMdiSubWindowPrivate::setSizeGripVisible(bool visible) const
    self.uglySide.call(
        'ritual_ZNK20QMdiSubWindowPrivate18setSizeGripVisibleEb', visible,
    )

  def setNewWindowTitle(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::setNewWindowTitle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#setNewWindowTitle
    """
    #  void QMdiSubWindowPrivate::setNewWindowTitle()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate17setNewWindowTitleEv',
    )

  @overload(QRect)
  @overload(NoneType)
  def setNewGeometry(self, geometry: Optional[QRect]) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::setNewGeometry(QRect *geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#setNewGeometry

    Parameters
    ----------

    geometry : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindowPrivate::setNewGeometry(QRect *geometry)
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate14setNewGeometryEP5QRect',
        self._addressOf(geometry),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QMdiSubWindowPrivate::QMdiSubWindowPrivate()': leans on
    'QMdiSubWindowPrivate::setVisible(QMdiSubWindowPrivate::
    WindowStateAction, bool)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.__init__' has no cute function yet. Qt's "
        "'QMdiSubWindowPrivate::QMdiSubWindowPrivate()': leans on "
        "'QMdiSubWindowPrivate::setVisible(QMdiSubWindowPrivate::WindowState"
        "Action, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QMdiSubWindow]:
    """
    Calls Qt's 'QMdiSubWindow *QMdiSubWindowPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindowprivate.html#q_func

    Returns
    -------

    Optional[QMdiSubWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiSubWindow *QMdiSubWindowPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QMdiSubWindowPrivate6q_funcEv')
    from . import QMdiSubWindow
    return QMdiSubWindow._cuteAt(address)

  def _q_updateStaysOnTopHint(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::_q_updateStaysOnTopHint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#_q_updateStaysOnTopHint
    """
    #  void QMdiSubWindowPrivate::_q_updateStaysOnTopHint()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate23_q_updateStaysOnTopHintEv',
    )

  def _q_enterInteractiveMode(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::_q_enterInteractiveMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#_q_enterInteractiveMode
    """
    #  void QMdiSubWindowPrivate::_q_enterInteractiveMode()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate23_q_enterInteractiveModeEv',
    )

  def leaveInteractiveMode(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::leaveInteractiveMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#leaveInteractiveMode
    """
    #  void QMdiSubWindowPrivate::leaveInteractiveMode()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate20leaveInteractiveModeEv',
    )

  def removeBaseWidget(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::removeBaseWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#removeBaseWidget
    """
    #  void QMdiSubWindowPrivate::removeBaseWidget()
    self.uglySide.call('ritual_ZN20QMdiSubWindowPrivate16removeBaseWidgetEv')

  def initOperationMap(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::initOperationMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#initOperationMap
    """
    #  void QMdiSubWindowPrivate::initOperationMap()
    self.uglySide.call('ritual_ZN20QMdiSubWindowPrivate16initOperationMapEv')

  def updateCursor(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::updateCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#updateCursor
    """
    #  void QMdiSubWindowPrivate::updateCursor()
    self.uglySide.call('ritual_ZN20QMdiSubWindowPrivate12updateCursorEv')

  def updateDirtyRegions(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::updateDirtyRegions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#updateDirtyRegions
    """
    #  void QMdiSubWindowPrivate::updateDirtyRegions()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate18updateDirtyRegionsEv',
    )

  def updateGeometryConstraints(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::updateGeometryConstraints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html
    """
    #  void QMdiSubWindowPrivate::updateGeometryConstraints()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate25updateGeometryConstraintsEv',
    )

  def updateMask(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::updateMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#updateMask
    """
    #  void QMdiSubWindowPrivate::updateMask()
    self.uglySide.call('ritual_ZN20QMdiSubWindowPrivate10updateMaskEv')

  @overload(Qt.WindowState)
  def ensureWindowState(self, state: Qt.WindowState) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::ensureWindowState(Qt::WindowState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#ensureWindowState

    Parameters
    ----------

    state : Qt.WindowState
      Passed on as its number.
    """
    #  void QMdiSubWindowPrivate::ensureWindowState(Qt::WindowState state)
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate17ensureWindowStateEN2Qt11WindowSta'
        'teE',
        state.value,
    )

  @overload(bool)
  def updateWindowTitle(self, requestFromChild: bool) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::updateWindowTitle(bool
    requestFromChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#updateWindowTitle

    Parameters
    ----------

    requestFromChild : bool
      Passed on as it is.
    """
    #  void QMdiSubWindowPrivate::updateWindowTitle(bool requestFromChild)
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate17updateWindowTitleEb',
        requestFromChild,
    )

  def enterRubberBandMode(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::enterRubberBandMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#enterRubberBandMode
    """
    #  void QMdiSubWindowPrivate::enterRubberBandMode()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate19enterRubberBandModeEv',
    )

  def leaveRubberBandMode(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::leaveRubberBandMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#leaveRubberBandMode
    """
    #  void QMdiSubWindowPrivate::leaveRubberBandMode()
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate19leaveRubberBandModeEv',
    )

  def restoreFocus(self) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindowPrivate::restoreFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#restoreFocus
    """
    #  bool QMdiSubWindowPrivate::restoreFocus()
    return self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate12restoreFocusEv',
    )

  def storeFocusWidget(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::storeFocusWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#storeFocusWidget
    """
    #  void QMdiSubWindowPrivate::storeFocusWidget()
    self.uglySide.call('ritual_ZN20QMdiSubWindowPrivate16storeFocusWidgetEv')

  @overload(WindowStateAction, str, str)
  @overload(WindowStateAction, str, NoneType)
  def addToSystemMenu(
      self,
      a0: WindowStateAction,
      text: str,
      slot: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QMdiSubWindowPrivate::addToSystemMenu(WindowStateAction
    a0, const QString &text, const char *slot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#addToSystemMenu

    Parameters
    ----------

    a0 : WindowStateAction
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QMdiSubWindowPrivate::addToSystemMenu(WindowStateAction a0, const
    #      QString &text, const char *slot)
    self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate15addToSystemMenuENS_17WindowStateA'
        'ctionERK7QStringPKc',
        a0.value, text, self._bytesOf(slot),
    )

  def originalWindowTitle(self) -> str:
    """
    Calls Qt's 'QString QMdiSubWindowPrivate::originalWindowTitle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindowprivate.html#originalWindowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMdiSubWindowPrivate::originalWindowTitle()
    return self.uglySide.call(
        'ritual_ZN20QMdiSubWindowPrivate19originalWindowTitleEv',
    )

  @staticmethod
  def _q_processFocusChanged(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::_q_processFocusChanged(QWidget *old,
    QWidget *now)': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate._q_processFocusChanged' has no cute function "
        "yet. Qt's 'void "
        "QMdiSubWindowPrivate::_q_processFocusChanged(QWidget *old, QWidget "
        "*now)': leans on "
        "'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def createSystemMenu(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::createSystemMenu()': leans on
    'QMdiSubWindowPrivate::setVisible(QMdiSubWindowPrivate::
    WindowStateAction, bool)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.createSystemMenu' has no cute function yet. "
        "Qt's 'void QMdiSubWindowPrivate::createSystemMenu()': leans on "
        "'QMdiSubWindowPrivate::setVisible(QMdiSubWindowPrivate::WindowState"
        "Action, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def getRegion(*__, **_) -> Never:
    """
    Qt's 'QRegion QMdiSubWindowPrivate::getRegion(Operation operation)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'SubControls'; did you mean 'QStyleOptionTitleBar::subControls'?.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.getRegion' has no cute function yet. Qt's "
        "'QRegion QMdiSubWindowPrivate::getRegion(Operation operation) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'SubControls'; did you mean "
        "'QStyleOptionTitleBar::subControls'?.")

  @staticmethod
  def menuBar(*__, **_) -> Never:
    """
    Qt's 'QMenuBar *QMdiSubWindowPrivate::menuBar() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'isChildOfTabbedQMdiArea'.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.menuBar' has no cute function yet. Qt's "
        "'QMenuBar *QMdiSubWindowPrivate::menuBar() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'isChildOfTabbedQMdiArea'.")

  @staticmethod
  def processClickedSubControl(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::processClickedSubControl()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'isMacStyle'.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.processClickedSubControl' has no cute "
        "function yet. Qt's 'void "
        "QMdiSubWindowPrivate::processClickedSubControl()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isMacStyle'.")

  @staticmethod
  def removeButtonsFromMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::removeButtonsFromMenuBar()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'isChildOfTabbedQMdiArea'.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.removeButtonsFromMenuBar' has no cute "
        "function yet. Qt's 'void "
        "QMdiSubWindowPrivate::removeButtonsFromMenuBar()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'isChildOfTabbedQMdiArea'.")

  @staticmethod
  def setActive(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::setActive(bool activate, bool
    changeFocus)': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.setActive' has no cute function yet. Qt's "
        "'void QMdiSubWindowPrivate::setActive(bool activate, bool "
        "changeFocus)': leans on "
        "'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setMaximizeMode(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::setMaximizeMode()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'ControlContainer'; did you mean
    'QMdi::ControlContainer'?.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.setMaximizeMode' has no cute function yet. "
        "Qt's 'void QMdiSubWindowPrivate::setMaximizeMode()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'ControlContainer'; did you "
        "mean 'QMdi::ControlContainer'?.")

  @staticmethod
  def setMinimizeMode(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::setMinimizeMode()': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.setMinimizeMode' has no cute function yet. "
        "Qt's 'void QMdiSubWindowPrivate::setMinimizeMode()': leans on "
        "'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setNormalMode(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::setNormalMode()': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.setNormalMode' has no cute function yet. "
        "Qt's 'void QMdiSubWindowPrivate::setNormalMode()': leans on "
        "'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setSizeGrip(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::setSizeGrip(QSizeGrip *sizeGrip)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'isMacStyle'.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.setSizeGrip' has no cute function yet. Qt's "
        "'void QMdiSubWindowPrivate::setSizeGrip(QSizeGrip *sizeGrip)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'isMacStyle'.")

  @staticmethod
  def showButtonsInMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar
    *menuBar)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isChildOfTabbedQMdiArea'.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.showButtonsInMenuBar' has no cute function "
        "yet. Qt's 'void "
        "QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar *menuBar)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'isChildOfTabbedQMdiArea'.")

  @staticmethod
  def sizeParameters(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::sizeParameters(int *margin, int
    *minWidth) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'NumSubControls'.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.sizeParameters' has no cute function yet. "
        "Qt's 'void QMdiSubWindowPrivate::sizeParameters(int *margin, int "
        "*minWidth) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'NumSubControls'.")

  @staticmethod
  def updateActions(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::updateActions()': leans on
    'QMdiSubWindowPrivate::setVisible(QMdiSubWindowPrivate::
    WindowStateAction, bool)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.updateActions' has no cute function yet. "
        "Qt's 'void QMdiSubWindowPrivate::updateActions()': leans on "
        "'QMdiSubWindowPrivate::setVisible(QMdiSubWindowPrivate::WindowState"
        "Action, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateInternalWindowTitle(*__, **_) -> Never:
    """
    Qt's 'void QMdiSubWindowPrivate::updateInternalWindowTitle()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'qt_setWindowTitle_helperHelper'.
    """
    raise NotImplementedError(
        "'QMdiSubWindowPrivate.updateInternalWindowTitle' has no cute "
        "function yet. Qt's 'void "
        "QMdiSubWindowPrivate::updateInternalWindowTitle()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qt_setWindowTitle_helperHelper'.")
