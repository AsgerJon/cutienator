"""
QWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qwindow_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QWindowPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate
from . import QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QPoint, QRect, QRectF
  from . import QCursor, QMouseEvent, QPalette, QScreen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCursor = WAIT['QCursor']
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWindowPrivate: a plain Python object standing in
  front of one C++ QWindowPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QWindowPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowPrivate that has a ritual and that Python can
  call so far, 33 names in all: 'q_func', 'init', 'setCursor', 'applyCursor',
  'globalPosition', 'topLevelWindow', 'eventReceiver', 'windowPalette',
  'setVisible', 'updateVisibility', '_q_clearAlert', 'updateSiblingPosition',
  'windowRecreationRequired', 'create', 'destroy', 'setTopLevelScreen',
  'connectToScreen', 'disconnectFromScreen', 'emitScreenChangedRecursion',
  'screenForGeometry', 'setTransientParent', 'clearFocusObject',
  'setFocusToTarget', 'closestAcceptableGeometry',
  'participatesInLastWindowClosed', 'treatAsVisible',
  'maybeSynthesizeContextMenuEvent', 'forwardToPopup', 'isPopup',
  'setAutomaticPositionAndResizeEnabled', 'updateDevicePixelRatio', 'get',
  'effectiveState'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWindow *QWindowPrivate::q_func() const': takes in Python
    what 'QWindow *QWindowPrivate::q_func()' takes.
  - Qt's 'QWindowPrivate::QWindowPrivate(decltype(QObjectPrivateVersion)
    version)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
  - Qt's 'QWindowPrivate::~QWindowPrivate()': the destructor: Python never
    removes a C++ QWindowPrivate.
  - Qt's 'void QWindowPrivate::setMinOrMaxSize(QSize *oldSizeMember, const
    QSize &size, qxp::function_ref<void ()> funcWidthChanged,
    qxp::function_ref<void ()> funcHeightChanged)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 40 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWindowPrivate is created at the first use, not by
    'QWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowPrivate.
  - Each name of Qt's QWindowPrivate that has no cute function yet,
    '__init__', 'setMinOrMaxSize', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWindowPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FocusTarget(CuteNum, scoped=True):
    """
    The enum 'QWindowPrivate::FocusTarget' of Qt, with the 5 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    First = Kee[int](0)
    Last = Kee[int](1)
    Current = Kee[int](2)
    Next = Kee[int](3)
    Prev = Kee[int](4)

  class PositionPolicy(CuteNum):
    """
    The enum 'QWindowPrivate::PositionPolicy' of Qt, with the 2 names Qt
    gives in it.
    """

    WindowFrameInclusive = Kee[int](0)
    WindowFrameExclusive = Kee[int](1)

  class SiblingPosition(CuteNum):
    """
    The enum 'QWindowPrivate::SiblingPosition' of Qt, with the 2 names Qt
    gives in it.
    """

    PositionTop = Kee[int](0)
    PositionBottom = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def get(window: Optional[QWindow]) -> Optional[QWindowPrivate]:
    """
    Calls Qt's 'QWindowPrivate *QWindowPrivate::get(QWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#get

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowPrivate *QWindowPrivate::get(QWindow *window)
    address = Rituals.call(
        'ritual_ZN14QWindowPrivate3getEP7QWindow',
        CuteMixin._addressOf(window),
    )
    return QWindowPrivate._cuteAt(address)

  @staticmethod
  @overload(Qt.WindowStates)
  def effectiveState(a0: Qt.WindowStates) -> Qt.WindowState:
    """
    Calls Qt's 'Qt::WindowState
    QWindowPrivate::effectiveState(Qt::WindowStates a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#effectiveState

    Parameters
    ----------

    a0 : Qt.WindowStates
      Passed on as its number.

    Returns
    -------

    Qt.WindowState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowState(number)'
      gives.
    """
    #  Qt::WindowState QWindowPrivate::effectiveState(Qt::WindowStates a0)
    return Qt.WindowState(Rituals.call(
        'ritual_ZN14QWindowPrivate14effectiveStateE6QFlagsIN2Qt11WindowStat'
        'eEE',
        a0.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowPrivate'

  #  A C++ QWindowPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowPrivate'

  #  The functions Qt calls itself that QWindowPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'eventReceiver': (
          ('_ZN14QWindowPrivate13eventReceiverEv',
           ('address', 'address', 'QtGui:QWindow'),
           ()),
      ),
      'windowPalette': (
          ('_ZNK14QWindowPrivate13windowPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
      'setVisible': (
          ('_ZN14QWindowPrivate10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'clearFocusObject': (
          ('_ZN14QWindowPrivate16clearFocusObjectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setFocusToTarget': (
          ('_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11Fo'
           'cusReasonE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QWindowPrivate.FocusTarget'),
               ('int', 'enum', 'QtCore:Qt.FocusReason'),
           )),
      ),
      'closestAcceptableGeometry': (
          ('_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'participatesInLastWindowClosed': (
          ('_ZNK14QWindowPrivate30participatesInLastWindowClosedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'treatAsVisible': (
          ('_ZNK14QWindowPrivate14treatAsVisibleEv',
           ('bool', 'number', ''),
           ()),
      ),
      'maybeSynthesizeContextMenuEvent': (
          ('_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseE'
           'vent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
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

  def globalPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWindowPrivate::globalPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#globalPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWindowPrivate::globalPosition() const
    address = self.uglySide.call(
        'ritual_ZNK14QWindowPrivate14globalPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload()
  @overload(QWindow.AncestorMode)
  def topLevelWindow(
      self,
      mode: QWindow.AncestorMode = QWindow.AncestorMode.IncludeTransients,
  ) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWindowPrivate::topLevelWindow(QWindow::AncestorMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#topLevelWindow

    Parameters
    ----------

    mode : QWindow.AncestorMode
      Passed on as its number. May be left out, as in Qt: it is then
      QWindow.AncestorMode.IncludeTransients.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWindowPrivate::topLevelWindow(QWindow::AncestorMode mode)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QWindowPrivate14topLevelWindowEN7QWindow12AncestorMode'
        'E',
        mode.value,
    )
    return QWindow._cuteAt(address)

  def windowPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QWindowPrivate::windowPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#windowPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QWindowPrivate::windowPalette() const
    ritual = 'ritual_ZNK14QWindowPrivate13windowPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QWindowPrivate13windowPaletteEv'
    address = self.uglySide.call(ritual)
    from . import QPalette
    return QPalette._cuteOwning(address)

  @overload(QScreen)
  @overload(NoneType)
  def windowRecreationRequired(self, newScreen: Optional[QScreen]) -> bool:
    """
    Calls Qt's 'bool QWindowPrivate::windowRecreationRequired(QScreen
    *newScreen) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#windowRecreationRequired

    Parameters
    ----------

    newScreen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWindowPrivate::windowRecreationRequired(QScreen *newScreen)
    #      const
    return self.uglySide.call(
        'ritual_ZNK14QWindowPrivate24windowRecreationRequiredEP7QScreen',
        self._addressOf(newScreen),
    )

  @overload(QRect)
  def screenForGeometry(self, rect: QRect) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QWindowPrivate::screenForGeometry(const QRect &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#screenForGeometry

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QWindowPrivate::screenForGeometry(const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK14QWindowPrivate17screenForGeometryERK5QRect',
        self._valueOf(rect),
    )
    from . import QScreen
    return QScreen._cuteAt(address)

  @overload(QRectF)
  def closestAcceptableGeometry(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#closestAcceptableGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
    #      const
    ritual = (
        'ritual_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRe'
          'ctF')
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def participatesInLastWindowClosed(self) -> bool:
    """
    Calls Qt's 'bool QWindowPrivate::participatesInLastWindowClosed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#participatesInLastWindowClosed
    """
    #  bool QWindowPrivate::participatesInLastWindowClosed() const
    ritual = 'ritual_ZNK14QWindowPrivate30participatesInLastWindowClosedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QWindowPrivate30participatesInLastWindowClosedEv')
    return self.uglySide.call(ritual)

  def treatAsVisible(self) -> bool:
    """
    Calls Qt's 'bool QWindowPrivate::treatAsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#treatAsVisible
    """
    #  bool QWindowPrivate::treatAsVisible() const
    ritual = 'ritual_ZNK14QWindowPrivate14treatAsVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QWindowPrivate14treatAsVisibleEv'
    return self.uglySide.call(ritual)

  def isPopup(self) -> bool:
    """
    Calls Qt's 'bool QWindowPrivate::isPopup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#isPopup
    """
    #  bool QWindowPrivate::isPopup() const
    return self.uglySide.call('ritual_ZNK14QWindowPrivate7isPopupEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QCursor)
  @overload(NoneType)
  def setCursor(self, c: Optional[QCursor] = None) -> None:
    """
    Calls Qt's 'void QWindowPrivate::setCursor(const QCursor *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#setCursor

    Parameters
    ----------

    c : Optional[QCursor]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWindowPrivate::setCursor(const QCursor *c)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate9setCursorEPK7QCursor', self._addressOf(c),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QWindowPrivate::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QWindowPrivate::setVisible(bool visible)
    ritual = 'ritual_ZN14QWindowPrivate10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWindowPrivate10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(QScreen, bool)
  @overload(NoneType, bool)
  def setTopLevelScreen(
      self,
      newScreen: Optional[QScreen],
      recreate: bool,
  ) -> None:
    """
    Calls Qt's 'void QWindowPrivate::setTopLevelScreen(QScreen *newScreen,
    bool recreate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#setTopLevelScreen

    Parameters
    ----------

    newScreen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    recreate : bool
      Passed on as it is.
    """
    #  void QWindowPrivate::setTopLevelScreen(QScreen *newScreen, bool
    #      recreate)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate17setTopLevelScreenEP7QScreenb',
        self._addressOf(newScreen), recreate,
    )

  @overload(QWindow)
  @overload(NoneType)
  def setTransientParent(self, parent: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QWindowPrivate::setTransientParent(QWindow *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#setTransientParent

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowPrivate::setTransientParent(QWindow *parent)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate18setTransientParentEP7QWindow',
        self._addressOf(parent),
    )

  @overload(FocusTarget, Qt.FocusReason)
  def setFocusToTarget(self, a0: FocusTarget, a1: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QWindowPrivate::setFocusToTarget(FocusTarget a0,
    Qt::FocusReason a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#setFocusToTarget

    Parameters
    ----------

    a0 : FocusTarget
      Passed on as its number.

    a1 : Qt.FocusReason
      Passed on as its number.
    """
    #  void QWindowPrivate::setFocusToTarget(FocusTarget a0, Qt::FocusReason
    #      a1)
    ritual = (
        'ritual_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt1'
        '1FocusReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTarget'
          'EN2Qt11FocusReasonE')
    self.uglySide.call(ritual, a0.value, a1.value)

  @overload(bool)
  def setAutomaticPositionAndResizeEnabled(self, a: bool) -> None:
    """
    Calls Qt's 'void
    QWindowPrivate::setAutomaticPositionAndResizeEnabled(bool a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QWindowPrivate::setAutomaticPositionAndResizeEnabled(bool a)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate36setAutomaticPositionAndResizeEnabledEb',
        a,
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
    Qt's 'QWindowPrivate::QWindowPrivate(decltype(QObjectPrivateVersion)
    version)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QWindowPrivate.__init__' has no cute function yet. Qt's "
        "'QWindowPrivate::QWindowPrivate(decltype(QObjectPrivateVersion) "
        "version)': names the enum 'QtPrivate_6_12_0', whose class cannot "
        "be named here.")

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

  def q_func(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWindowPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#q_func

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWindowPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QWindowPrivate6q_funcEv')
    return QWindow._cuteAt(address)

  @overload(QWindow)
  @overload(NoneType)
  @overload(QWindow, QScreen)
  @overload(QWindow, NoneType)
  @overload(NoneType, QScreen)
  @overload(NoneType, NoneType)
  def init(
      self,
      parent: Optional[QWindow],
      targetScreen: Optional[QScreen] = None,
  ) -> None:
    """
    Calls Qt's 'void QWindowPrivate::init(QWindow *parent, QScreen
    *targetScreen)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#init

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetScreen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWindowPrivate::init(QWindow *parent, QScreen *targetScreen)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate4initEP7QWindowP7QScreen',
        self._addressOf(parent), self._addressOf(targetScreen),
    )

  def applyCursor(self) -> bool:
    """
    Calls Qt's 'bool QWindowPrivate::applyCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#applyCursor
    """
    #  bool QWindowPrivate::applyCursor()
    return self.uglySide.call('ritual_ZN14QWindowPrivate11applyCursorEv')

  def eventReceiver(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWindowPrivate::eventReceiver()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#eventReceiver

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWindowPrivate::eventReceiver()
    ritual = 'ritual_ZN14QWindowPrivate13eventReceiverEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWindowPrivate13eventReceiverEv'
    address = self.uglySide.call(ritual)
    return QWindow._cuteAt(address)

  def updateVisibility(self) -> None:
    """
    Calls Qt's 'void QWindowPrivate::updateVisibility()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#updateVisibility
    """
    #  void QWindowPrivate::updateVisibility()
    self.uglySide.call('ritual_ZN14QWindowPrivate16updateVisibilityEv')

  def _q_clearAlert(self) -> None:
    """
    Calls Qt's 'void QWindowPrivate::_q_clearAlert()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#_q_clearAlert
    """
    #  void QWindowPrivate::_q_clearAlert()
    self.uglySide.call('ritual_ZN14QWindowPrivate13_q_clearAlertEv')

  @overload(SiblingPosition)
  def updateSiblingPosition(self, a0: SiblingPosition) -> None:
    """
    Calls Qt's 'void QWindowPrivate::updateSiblingPosition(SiblingPosition
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#updateSiblingPosition

    Parameters
    ----------

    a0 : SiblingPosition
      Passed on as its number.
    """
    #  void QWindowPrivate::updateSiblingPosition(SiblingPosition a0)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate21updateSiblingPositionENS_15SiblingPosit'
        'ionE',
        a0.value,
    )

  @overload(bool)
  def create(self, recursive: bool) -> None:
    """
    Calls Qt's 'void QWindowPrivate::create(bool recursive)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#create

    Parameters
    ----------

    recursive : bool
      Passed on as it is.
    """
    #  void QWindowPrivate::create(bool recursive)
    self.uglySide.call('ritual_ZN14QWindowPrivate6createEb', recursive)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QWindowPrivate::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#destroy
    """
    #  void QWindowPrivate::destroy()
    self.uglySide.call('ritual_ZN14QWindowPrivate7destroyEv')

  @overload(QScreen)
  @overload(NoneType)
  def connectToScreen(self, topLevelScreen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QWindowPrivate::connectToScreen(QScreen
    *topLevelScreen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#connectToScreen

    Parameters
    ----------

    topLevelScreen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowPrivate::connectToScreen(QScreen *topLevelScreen)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate15connectToScreenEP7QScreen',
        self._addressOf(topLevelScreen),
    )

  def disconnectFromScreen(self) -> None:
    """
    Calls Qt's 'void QWindowPrivate::disconnectFromScreen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#disconnectFromScreen
    """
    #  void QWindowPrivate::disconnectFromScreen()
    self.uglySide.call('ritual_ZN14QWindowPrivate20disconnectFromScreenEv')

  @overload(QScreen)
  @overload(NoneType)
  def emitScreenChangedRecursion(self, newScreen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QWindowPrivate::emitScreenChangedRecursion(QScreen
    *newScreen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#emitScreenChangedRecursion

    Parameters
    ----------

    newScreen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowPrivate::emitScreenChangedRecursion(QScreen *newScreen)
    self.uglySide.call(
        'ritual_ZN14QWindowPrivate26emitScreenChangedRecursionEP7QScreen',
        self._addressOf(newScreen),
    )

  def clearFocusObject(self) -> None:
    """
    Calls Qt's 'void QWindowPrivate::clearFocusObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#clearFocusObject
    """
    #  void QWindowPrivate::clearFocusObject()
    ritual = 'ritual_ZN14QWindowPrivate16clearFocusObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWindowPrivate16clearFocusObjectEv'
    self.uglySide.call(ritual)

  @overload(QMouseEvent)
  @overload(NoneType)
  def maybeSynthesizeContextMenuEvent(
      self,
      event: Optional[QMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMou'
        'seEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP'
          '11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent, QWindow)
  @overload(QEvent, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def forwardToPopup(
      self,
      event: Optional[QEvent],
      activePopupOnPress: Optional[QWindow],
  ) -> Optional[QWindow]:
    """
    Calls Qt's 'const QWindow *QWindowPrivate::forwardToPopup(QEvent *event,
    const QWindow *activePopupOnPress)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowprivate.html#forwardToPopup

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    activePopupOnPress : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QWindow *QWindowPrivate::forwardToPopup(QEvent *event, const
    #      QWindow *activePopupOnPress)
    address = self.uglySide.call(
        'ritual_ZN14QWindowPrivate14forwardToPopupEP6QEventPK7QWindow',
        self._addressOf(event), self._addressOf(activePopupOnPress),
    )
    return QWindow._cuteAt(address)

  def updateDevicePixelRatio(self) -> bool:
    """
    Calls Qt's 'bool QWindowPrivate::updateDevicePixelRatio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowprivate.html#updateDevicePixelRatio
    """
    #  bool QWindowPrivate::updateDevicePixelRatio()
    return self.uglySide.call(
        'ritual_ZN14QWindowPrivate22updateDevicePixelRatioEv',
    )

  @staticmethod
  def setMinOrMaxSize(*__, **_) -> Never:
    """
    Qt's 'void QWindowPrivate::setMinOrMaxSize(QSize *oldSizeMember, const
    QSize &size, qxp::function_ref<void ()> funcWidthChanged,
    qxp::function_ref<void ()> funcHeightChanged)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWindowPrivate.setMinOrMaxSize' has no cute function yet. Qt's "
        "'void QWindowPrivate::setMinOrMaxSize(QSize *oldSizeMember, const "
        "QSize &size, qxp::function_ref<void ()> funcWidthChanged, "
        "qxp::function_ref<void ()> funcHeightChanged)': takes a type "
        "Python has no way to hand over yet.")
