"""
QMdiAreaPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMdiAreaPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QAbstractScrollAreaPrivate, QMdiArea

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRect, QSize
  from . import QMdiSubWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMdiSubWindow = WAIT['QMdiSubWindow']
  QObject = WAIT['QObject']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMdiAreaPrivate(QAbstractScrollAreaPrivate):
  """
  The cute side of Qt's QMdiAreaPrivate: a plain Python object standing in
  front of one C++ QMdiAreaPrivate.

  It is built on the cute 'QAbstractScrollAreaPrivate', as Qt's
  QMdiAreaPrivate is built on Qt's QAbstractScrollAreaPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QMdiAreaPrivate that has a ritual and that Python
  can call so far, 17 names in all: 'q_func', '_q_closeTab', '_q_moveTab',
  'resetActiveWindow', 'scrollBarsEnabled', 'lastWindowAboutToBeDestroyed',
  'setChildActivationEnabled', 'resizeToMinimumTileSize',
  'scrollBarPolicyChanged', 'highlightNextSubWindow', 'subWindowList',
  'disconnectSubWindow', 'startResizeTimer', 'startTabToPreviousTimer',
  'windowStaysOnTop', 'isExplicitlyDeactivated', 'hideRubberBand'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMdiArea *QMdiAreaPrivate::q_func() const': takes in Python
    what 'QMdiArea *QMdiAreaPrivate::q_func()' takes.

  What has no ritual
  ------------------

  20 of the 39 functions Qt declares: 14 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 5 leans on
  'QMdiSubWindowPrivate; 1 leans on 'QMdiAreaPrivate.

  What to expect
  --------------

  - The C++ QMdiAreaPrivate is created at the first use, not by
    'QMdiAreaPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMdiAreaPrivate.
  - Each name of Qt's QMdiAreaPrivate that has no cute function yet,
    '_q_currentTabChanged', '_q_deactivateAllWindows',
    '_q_processWindowStateChanged', 'activateCurrentWindow',
    'activateHighlightedWindow', 'activateWindow', 'appendChild',
    'arrangeMinimizedSubWindows', 'emitWindowActivated', 'internalRaise',
    'nextVisibleSubWindow', 'place', 'rearrange', 'refreshTabBar',
    'setActive', 'setViewMode', 'showRubberBandFor', 'updateActiveWindow',
    'updateScrollBars', 'updateTabBarGeometry', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdiAreaPrivate'

  #  A C++ QMdiAreaPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMdiAreaPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scrollBarsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QMdiAreaPrivate::scrollBarsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#scrollBarsEnabled
    """
    #  bool QMdiAreaPrivate::scrollBarsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QMdiAreaPrivate17scrollBarsEnabledEv',
    )

  def lastWindowAboutToBeDestroyed(self) -> bool:
    """
    Calls Qt's 'bool QMdiAreaPrivate::lastWindowAboutToBeDestroyed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#lastWindowAboutToBeDestroyed
    """
    #  bool QMdiAreaPrivate::lastWindowAboutToBeDestroyed() const
    return self.uglySide.call(
        'ritual_ZNK15QMdiAreaPrivate28lastWindowAboutToBeDestroyedEv',
    )

  @overload(QMdiArea.WindowOrder)
  @overload(QMdiArea.WindowOrder, bool)
  def subWindowList(
      self,
      a0: QMdiArea.WindowOrder,
      reversed: bool = False,
  ) -> QList[QMdiSubWindow]:
    """
    Calls Qt's 'QList<QMdiSubWindow *>
    QMdiAreaPrivate::subWindowList(QMdiArea::WindowOrder a0, bool reversed)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiareaprivate.html#subWindowList

    Parameters
    ----------

    a0 : QMdiArea.WindowOrder
      Passed on as its number.

    reversed : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QList[QMdiSubWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMdiSubWindow *>
    #      QMdiAreaPrivate::subWindowList(QMdiArea::WindowOrder a0, bool
    #      reversed) const
    address = self.uglySide.call(
        'ritual_ZNK15QMdiAreaPrivate13subWindowListEN8QMdiArea11WindowOrder'
        'Eb',
        a0.value, reversed,
    )
    from . import QMdiSubWindow
    return QList[QMdiSubWindow]._cuteOwning(address)

  @overload(QMdiSubWindow)
  @overload(NoneType)
  def windowStaysOnTop(self, subWindow: Optional[QMdiSubWindow]) -> bool:
    """
    Calls Qt's 'bool QMdiAreaPrivate::windowStaysOnTop(QMdiSubWindow
    *subWindow) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#windowStaysOnTop

    Parameters
    ----------

    subWindow : Optional[QMdiSubWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMdiAreaPrivate::windowStaysOnTop(QMdiSubWindow *subWindow) const
    return self.uglySide.call(
        'ritual_ZNK15QMdiAreaPrivate16windowStaysOnTopEP13QMdiSubWindow',
        self._addressOf(subWindow),
    )

  @overload(QMdiSubWindow)
  @overload(NoneType)
  def isExplicitlyDeactivated(
      self,
      subWindow: Optional[QMdiSubWindow],
  ) -> bool:
    """
    Calls Qt's 'bool QMdiAreaPrivate::isExplicitlyDeactivated(QMdiSubWindow
    *subWindow) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#isExplicitlyDeactivated

    Parameters
    ----------

    subWindow : Optional[QMdiSubWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMdiAreaPrivate::isExplicitlyDeactivated(QMdiSubWindow
    #      *subWindow) const
    return self.uglySide.call(
        'ritual_ZNK15QMdiAreaPrivate23isExplicitlyDeactivatedEP13QMdiSubWin'
        'dow',
        self._addressOf(subWindow),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  @overload(bool, bool)
  def setChildActivationEnabled(
      self,
      enable: bool = True,
      onlyNextActivationEvent: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::setChildActivationEnabled(bool enable,
    bool onlyNextActivationEvent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#setChildActivationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    onlyNextActivationEvent : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QMdiAreaPrivate::setChildActivationEnabled(bool enable, bool
    #      onlyNextActivationEvent) const
    self.uglySide.call(
        'ritual_ZNK15QMdiAreaPrivate25setChildActivationEnabledEbb',
        enable, onlyNextActivationEvent,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMdiAreaPrivate::QMdiAreaPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#QMdiAreaPrivate
    """
    #  QMdiAreaPrivate::QMdiAreaPrivate()
    self._noteCreation(QMdiAreaPrivate, lambda: Rituals.call(
        'ritual_ZN15QMdiAreaPrivateC1Ev',
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

  def q_func(self) -> Optional[QMdiArea]:
    """
    Calls Qt's 'QMdiArea *QMdiAreaPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiareaprivate.html#q_func

    Returns
    -------

    Optional[QMdiArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiArea *QMdiAreaPrivate::q_func()
    address = self.uglySide.call('ritual_ZN15QMdiAreaPrivate6q_funcEv')
    return QMdiArea._cuteAt(address)

  @overload(int)
  def _q_closeTab(self, index: int) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::_q_closeTab(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiareaprivate.html#_q_closeTab

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMdiAreaPrivate::_q_closeTab(int index)
    self.uglySide.call('ritual_ZN15QMdiAreaPrivate11_q_closeTabEi', index)

  @overload(int, int)
  def _q_moveTab(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::_q_moveTab(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiareaprivate.html#_q_moveTab

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QMdiAreaPrivate::_q_moveTab(int from, int to)
    self.uglySide.call(
        'ritual_ZN15QMdiAreaPrivate10_q_moveTabEii', from_, to,
    )

  @overload()
  @overload(QMdiSubWindow)
  @overload(NoneType)
  def resetActiveWindow(self, child: Optional[QMdiSubWindow] = None) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::resetActiveWindow(QMdiSubWindow
    *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#resetActiveWindow

    Parameters
    ----------

    child : Optional[QMdiSubWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QMdiAreaPrivate::resetActiveWindow(QMdiSubWindow *child)
    self.uglySide.call(
        'ritual_ZN15QMdiAreaPrivate17resetActiveWindowEP13QMdiSubWindow',
        self._addressOf(child),
    )

  @overload(QSize, int)
  def resizeToMinimumTileSize(
      self,
      minSubWindowSize: QSize,
      subWindowCount: int,
  ) -> QRect:
    """
    Calls Qt's 'QRect QMdiAreaPrivate::resizeToMinimumTileSize(const QSize
    &minSubWindowSize, int subWindowCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#resizeToMinimumTileSize

    Parameters
    ----------

    minSubWindowSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    subWindowCount : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMdiAreaPrivate::resizeToMinimumTileSize(const QSize
    #      &minSubWindowSize, int subWindowCount)
    address = self.uglySide.call(
        'ritual_ZN15QMdiAreaPrivate23resizeToMinimumTileSizeERK5QSizei',
        self._valueOf(minSubWindowSize), subWindowCount,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(Qt.Orientation, Qt.ScrollBarPolicy)
  def scrollBarPolicyChanged(
      self,
      a0: Qt.Orientation,
      a1: Qt.ScrollBarPolicy,
  ) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::scrollBarPolicyChanged(Qt::Orientation
    a0, Qt::ScrollBarPolicy a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#scrollBarPolicyChanged

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    a1 : Qt.ScrollBarPolicy
      Passed on as its number.
    """
    #  void QMdiAreaPrivate::scrollBarPolicyChanged(Qt::Orientation a0,
    #      Qt::ScrollBarPolicy a1)
    ritual = (
        'ritual_ZN15QMdiAreaPrivate22scrollBarPolicyChangedEN2Qt11Orientati'
        'onENS0_15ScrollBarPolicyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QMdiAreaPrivate22scrollBarPolicyChangedEN2Qt11Ori'
          'entationENS0_15ScrollBarPolicyE')
    self.uglySide.call(ritual, a0.value, a1.value)

  @overload(int)
  def highlightNextSubWindow(self, increaseFactor: int) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::highlightNextSubWindow(int
    increaseFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#highlightNextSubWindow

    Parameters
    ----------

    increaseFactor : int
      Passed on as it is.
    """
    #  void QMdiAreaPrivate::highlightNextSubWindow(int increaseFactor)
    self.uglySide.call(
        'ritual_ZN15QMdiAreaPrivate22highlightNextSubWindowEi',
        increaseFactor,
    )

  @overload(QObject)
  @overload(NoneType)
  def disconnectSubWindow(self, subWindow: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::disconnectSubWindow(QObject
    *subWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#disconnectSubWindow

    Parameters
    ----------

    subWindow : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiAreaPrivate::disconnectSubWindow(QObject *subWindow)
    self.uglySide.call(
        'ritual_ZN15QMdiAreaPrivate19disconnectSubWindowEP7QObject',
        self._addressOf(subWindow, 'QObject'),
    )

  def startResizeTimer(self) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::startResizeTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#startResizeTimer
    """
    #  void QMdiAreaPrivate::startResizeTimer()
    self.uglySide.call('ritual_ZN15QMdiAreaPrivate16startResizeTimerEv')

  def startTabToPreviousTimer(self) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::startTabToPreviousTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#startTabToPreviousTimer
    """
    #  void QMdiAreaPrivate::startTabToPreviousTimer()
    self.uglySide.call(
        'ritual_ZN15QMdiAreaPrivate23startTabToPreviousTimerEv',
    )

  def hideRubberBand(self) -> None:
    """
    Calls Qt's 'void QMdiAreaPrivate::hideRubberBand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiareaprivate.html#hideRubberBand
    """
    #  void QMdiAreaPrivate::hideRubberBand()
    self.uglySide.call('ritual_ZN15QMdiAreaPrivate14hideRubberBandEv')

  @staticmethod
  def _q_currentTabChanged(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::_q_currentTabChanged(int index)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QMdiAreaTabBar'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate._q_currentTabChanged' has no cute function yet. "
        "Qt's 'void QMdiAreaPrivate::_q_currentTabChanged(int index)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QMdiAreaTabBar'.")

  @staticmethod
  def _q_deactivateAllWindows(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::_q_deactivateAllWindows(QMdiSubWindow
    *aboutToActivate)': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate._q_deactivateAllWindows' has no cute function "
        "yet. Qt's 'void "
        "QMdiAreaPrivate::_q_deactivateAllWindows(QMdiSubWindow "
        "*aboutToActivate)': leans on "
        "'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def _q_processWindowStateChanged(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::_q_processWindowStateChanged(Qt::WindowStates
    oldState, Qt::WindowStates newState)': leans on
    'QMdiAreaPrivate::arrangeMinimizedSubWindows()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate._q_processWindowStateChanged' has no cute "
        "function yet. Qt's 'void "
        "QMdiAreaPrivate::_q_processWindowStateChanged(Qt::WindowStates "
        "oldState, Qt::WindowStates newState)': leans on "
        "'QMdiAreaPrivate::arrangeMinimizedSubWindows()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def activateCurrentWindow(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::activateCurrentWindow()': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.activateCurrentWindow' has no cute function yet. "
        "Qt's 'void QMdiAreaPrivate::activateCurrentWindow()': leans on "
        "'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def activateHighlightedWindow(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::activateHighlightedWindow()': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.activateHighlightedWindow' has no cute function "
        "yet. Qt's 'void QMdiAreaPrivate::activateHighlightedWindow()': "
        "leans on 'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def activateWindow(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::activateWindow(QMdiSubWindow *child)': leans
    on 'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.activateWindow' has no cute function yet. Qt's "
        "'void QMdiAreaPrivate::activateWindow(QMdiSubWindow *child)': "
        "leans on 'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def appendChild(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::appendChild(QMdiSubWindow *child)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'MinOverlapPlacer'; did you mean
    'QMdi::MinOverlapPlacer'?.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.appendChild' has no cute function yet. Qt's 'void "
        "QMdiAreaPrivate::appendChild(QMdiSubWindow *child)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'MinOverlapPlacer'; did you "
        "mean 'QMdi::MinOverlapPlacer'?.")

  @staticmethod
  def arrangeMinimizedSubWindows(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::arrangeMinimizedSubWindows()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'IconTiler'; did you mean
    'QMdi::IconTiler'?.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.arrangeMinimizedSubWindows' has no cute function "
        "yet. Qt's 'void QMdiAreaPrivate::arrangeMinimizedSubWindows()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name 'IconTiler'; "
        "did you mean 'QMdi::IconTiler'?.")

  @staticmethod
  def emitWindowActivated(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::emitWindowActivated(QMdiSubWindow *child)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QMdiAreaTabBar'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.emitWindowActivated' has no cute function yet. "
        "Qt's 'void QMdiAreaPrivate::emitWindowActivated(QMdiSubWindow "
        "*child)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QMdiAreaTabBar'.")

  @staticmethod
  def internalRaise(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::internalRaise(QMdiSubWindow *child) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'sanityCheck'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.internalRaise' has no cute function yet. Qt's "
        "'void QMdiAreaPrivate::internalRaise(QMdiSubWindow *child) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'sanityCheck'.")

  @staticmethod
  def nextVisibleSubWindow(*__, **_) -> Never:
    """
    Qt's 'QMdiSubWindow *QMdiAreaPrivate::nextVisibleSubWindow(int
    increaseFactor, QMdiArea::WindowOrder a1, int removed, int fromIndex)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'setIndex'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.nextVisibleSubWindow' has no cute function yet. "
        "Qt's 'QMdiSubWindow *QMdiAreaPrivate::nextVisibleSubWindow(int "
        "increaseFactor, QMdiArea::WindowOrder a1, int removed, int "
        "fromIndex) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'setIndex'.")

  @staticmethod
  def place(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::place(QMdi::Placer *placer, QMdiSubWindow
    *child)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'Placer'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.place' has no cute function yet. Qt's 'void "
        "QMdiAreaPrivate::place(QMdi::Placer *placer, QMdiSubWindow "
        "*child)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'Placer'.")

  @staticmethod
  def rearrange(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::rearrange(QMdi::Rearranger *rearranger)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'Rearranger'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.rearrange' has no cute function yet. Qt's 'void "
        "QMdiAreaPrivate::rearrange(QMdi::Rearranger *rearranger)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'Rearranger'.")

  @staticmethod
  def refreshTabBar(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::refreshTabBar()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QMdiAreaTabBar'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.refreshTabBar' has no cute function yet. Qt's "
        "'void QMdiAreaPrivate::refreshTabBar()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type 'QMdiAreaTabBar'.")

  @staticmethod
  def setActive(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::setActive(QMdiSubWindow *subWindow, bool
    active, bool changeFocus) const': leans on
    'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.setActive' has no cute function yet. Qt's 'void "
        "QMdiAreaPrivate::setActive(QMdiSubWindow *subWindow, bool active, "
        "bool changeFocus) const': leans on "
        "'QMdiSubWindowPrivate::showButtonsInMenuBar(QMenuBar*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setViewMode(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::setViewMode(QMdiArea::ViewMode mode)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: allocation of incomplete type 'QMdiAreaTabBar'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.setViewMode' has no cute function yet. Qt's 'void "
        "QMdiAreaPrivate::setViewMode(QMdiArea::ViewMode mode)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: allocation of incomplete type "
        "'QMdiAreaTabBar'.")

  @staticmethod
  def showRubberBandFor(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::showRubberBandFor(QMdiSubWindow *subWindow)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QMdiAreaTabBar'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.showRubberBandFor' has no cute function yet. Qt's "
        "'void QMdiAreaPrivate::showRubberBandFor(QMdiSubWindow "
        "*subWindow)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QMdiAreaTabBar'.")

  @staticmethod
  def updateActiveWindow(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::updateActiveWindow(int removedIndex, bool
    activeRemoved)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: no matching constructor for
    initialization of 'const QSignalBlocker'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.updateActiveWindow' has no cute function yet. "
        "Qt's 'void QMdiAreaPrivate::updateActiveWindow(int removedIndex, "
        "bool activeRemoved)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: no "
        "matching constructor for initialization of 'const QSignalBlocker'.")

  @staticmethod
  def updateScrollBars(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::updateScrollBars()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'useScrollBar'; did you mean 'QScrollBar'?.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.updateScrollBars' has no cute function yet. Qt's "
        "'void QMdiAreaPrivate::updateScrollBars()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'useScrollBar'; did "
        "you mean 'QScrollBar'?.")

  @staticmethod
  def updateTabBarGeometry(*__, **_) -> Never:
    """
    Qt's 'void QMdiAreaPrivate::updateTabBarGeometry()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier '_q_tb_tabBarShapeFrom'.
    """
    raise NotImplementedError(
        "'QMdiAreaPrivate.updateTabBarGeometry' has no cute function yet. "
        "Qt's 'void QMdiAreaPrivate::updateTabBarGeometry()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'_q_tb_tabBarShapeFrom'.")
