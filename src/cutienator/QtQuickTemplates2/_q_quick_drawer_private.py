"""
QQuickDrawerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdrawer_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDrawerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickPopup, QQuickPopupPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QPointF
  from ..QtGui import QMouseEvent, QTouchEvent
  from ..QtQuick import QQuickItem
  from . import QQuickDrawer, QQuickPopupPositioner
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QQuickDrawer = WAIT['QQuickDrawer']
  QQuickItem = WAIT['QQuickItem']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDrawerPrivate(QQuickPopupPrivate):
  """
  The cute side of Qt's QQuickDrawerPrivate: a plain Python object standing
  in front of one C++ QQuickDrawerPrivate.

  It is built on the cute 'QQuickPopupPrivate', as Qt's QQuickDrawerPrivate
  is built on Qt's QQuickPopupPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDrawerPrivate that has a ritual and that
  Python can call so far, 22 names in all: 'q_func', 'get', 'offsetAt',
  'positionAt', 'getPositioner', 'showDimmer', 'hideDimmer', 'resizeDimmer',
  'startDrag', 'grabMouse', 'grabTouch', 'blockInput', 'handlePress',
  'handleMove', 'handleRelease', 'handleUngrab', 'prepareEnterTransition',
  'prepareExitTransition', 'resolvedPopupType', 'setEdge', 'effectiveEdge',
  'isWithinDragMargin'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickDrawer *QQuickDrawerPrivate::q_func() const': takes in
    Python what 'QQuickDrawer *QQuickDrawerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickDrawerPrivate is created at the first use, not by
    'QQuickDrawerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDrawerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickDrawer)
  @overload(NoneType)
  def get(drawer: Optional[QQuickDrawer]) -> Optional[QQuickDrawerPrivate]:
    """
    Calls Qt's 'QQuickDrawerPrivate *QQuickDrawerPrivate::get(QQuickDrawer
    *drawer)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawerprivate.html#get

    Parameters
    ----------

    drawer : Optional[QQuickDrawer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDrawerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDrawerPrivate *QQuickDrawerPrivate::get(QQuickDrawer *drawer)
    address = Rituals.call(
        'ritual_ZN19QQuickDrawerPrivate3getEP12QQuickDrawer',
        CuteMixin._addressOf(drawer),
    )
    return QQuickDrawerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDrawerPrivate'

  #  A C++ QQuickDrawerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDrawerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def offsetAt(self, point: QPointF) -> float:
    """
    Calls Qt's 'qreal QQuickDrawerPrivate::offsetAt(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawerprivate.html#offsetAt

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QQuickDrawerPrivate::offsetAt(const QPointF &point) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickDrawerPrivate8offsetAtERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def positionAt(self, point: QPointF) -> float:
    """
    Calls Qt's 'qreal QQuickDrawerPrivate::positionAt(const QPointF &point)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#positionAt

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QQuickDrawerPrivate::positionAt(const QPointF &point) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickDrawerPrivate10positionAtERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QQuickItem, QPointF)
  @overload(NoneType, QPointF)
  def blockInput(self, item: Optional[QQuickItem], point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::blockInput(QQuickItem *item, const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#blockInput

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickDrawerPrivate::blockInput(QQuickItem *item, const QPointF
    #      &point) const
    ritual = (
        'ritual_ZNK19QQuickDrawerPrivate10blockInputEP10QQuickItemRK7QPoint'
        'F')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QQuickDrawerPrivate10blockInputEP10QQuickItemRK7'
          'QPointF')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._valueOf(point, 'QPointF'),
    )

  def resolvedPopupType(self) -> QQuickPopup.PopupType:
    """
    Calls Qt's 'QQuickPopup::PopupType
    QQuickDrawerPrivate::resolvedPopupType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#resolvedPopupType

    Returns
    -------

    QQuickPopup.PopupType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickPopup.PopupType(number)' gives.
    """
    #  QQuickPopup::PopupType QQuickDrawerPrivate::resolvedPopupType() const
    ritual = 'ritual_ZNK19QQuickDrawerPrivate17resolvedPopupTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickDrawerPrivate17resolvedPopupTypeEv'
    return QQuickPopup.PopupType(self.uglySide.call(ritual))

  def effectiveEdge(self) -> Qt.Edge:
    """
    Calls Qt's 'Qt::Edge QQuickDrawerPrivate::effectiveEdge() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#effectiveEdge

    Returns
    -------

    Qt.Edge
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Edge(number)' gives.
    """
    #  Qt::Edge QQuickDrawerPrivate::effectiveEdge() const
    return Qt.Edge(self.uglySide.call(
        'ritual_ZNK19QQuickDrawerPrivate13effectiveEdgeEv',
    ))

  @overload(QPointF)
  def isWithinDragMargin(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::isWithinDragMargin(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#isWithinDragMargin

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickDrawerPrivate::isWithinDragMargin(const QPointF &point)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QQuickDrawerPrivate18isWithinDragMarginERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Edge)
  def setEdge(self, edge: Qt.Edge) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::setEdge(Qt::Edge edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawerprivate.html#setEdge

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.
    """
    #  bool QQuickDrawerPrivate::setEdge(Qt::Edge edge)
    return self.uglySide.call(
        'ritual_ZN19QQuickDrawerPrivate7setEdgeEN2Qt4EdgeE', edge.value,
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

  def q_func(self) -> Optional[QQuickDrawer]:
    """
    Calls Qt's 'QQuickDrawer *QQuickDrawerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawerprivate.html#q_func

    Returns
    -------

    Optional[QQuickDrawer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDrawer *QQuickDrawerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QQuickDrawerPrivate6q_funcEv')
    from . import QQuickDrawer
    return QQuickDrawer._cuteAt(address)

  def getPositioner(self) -> Optional[QQuickPopupPositioner]:
    """
    Calls Qt's 'QQuickPopupPositioner *QQuickDrawerPrivate::getPositioner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#getPositioner

    Returns
    -------

    Optional[QQuickPopupPositioner]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupPositioner *QQuickDrawerPrivate::getPositioner()
    ritual = 'ritual_ZN19QQuickDrawerPrivate13getPositionerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDrawerPrivate13getPositionerEv'
    address = self.uglySide.call(ritual)
    from . import QQuickPopupPositioner
    return QQuickPopupPositioner._cuteAt(address)

  def showDimmer(self) -> None:
    """
    Calls Qt's 'void QQuickDrawerPrivate::showDimmer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#showDimmer
    """
    #  void QQuickDrawerPrivate::showDimmer()
    ritual = 'ritual_ZN19QQuickDrawerPrivate10showDimmerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDrawerPrivate10showDimmerEv'
    self.uglySide.call(ritual)

  def hideDimmer(self) -> None:
    """
    Calls Qt's 'void QQuickDrawerPrivate::hideDimmer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#hideDimmer
    """
    #  void QQuickDrawerPrivate::hideDimmer()
    ritual = 'ritual_ZN19QQuickDrawerPrivate10hideDimmerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDrawerPrivate10hideDimmerEv'
    self.uglySide.call(ritual)

  def resizeDimmer(self) -> None:
    """
    Calls Qt's 'void QQuickDrawerPrivate::resizeDimmer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#resizeDimmer
    """
    #  void QQuickDrawerPrivate::resizeDimmer()
    ritual = 'ritual_ZN19QQuickDrawerPrivate12resizeDimmerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDrawerPrivate12resizeDimmerEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def startDrag(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::startDrag(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawerprivate.html#startDrag

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDrawerPrivate::startDrag(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN19QQuickDrawerPrivate9startDragEP6QEvent',
        self._addressOf(event),
    )

  @overload(QQuickItem, QMouseEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QMouseEvent)
  @overload(NoneType, NoneType)
  def grabMouse(
      self,
      item: Optional[QQuickItem],
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::grabMouse(QQuickItem *item,
    QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawerprivate.html#grabMouse

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDrawerPrivate::grabMouse(QQuickItem *item, QMouseEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN19QQuickDrawerPrivate9grabMouseEP10QQuickItemP11QMouseEve'
        'nt',
        self._addressOf(item), self._addressOf(event),
    )

  @overload(QQuickItem, QTouchEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def grabTouch(
      self,
      item: Optional[QQuickItem],
      event: Optional[QTouchEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::grabTouch(QQuickItem *item,
    QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrawerprivate.html#grabTouch

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDrawerPrivate::grabTouch(QQuickItem *item, QTouchEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN19QQuickDrawerPrivate9grabTouchEP10QQuickItemP11QTouchEve'
        'nt',
        self._addressOf(item), self._addressOf(event),
    )

  @overload(QQuickItem, QPointF, int)
  @overload(NoneType, QPointF, int)
  def handlePress(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::handlePress(QQuickItem *item, const
    QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#handlePress

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickDrawerPrivate::handlePress(QQuickItem *item, const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN19QQuickDrawerPrivate11handlePressEP10QQuickItemRK7QPoint'
        'Fm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDrawerPrivate11handlePressEP10QQuickItemRK7'
          'QPointFm')
    return self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QQuickItem, QPointF, int)
  @overload(NoneType, QPointF, int)
  def handleMove(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::handleMove(QQuickItem *item, const
    QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#handleMove

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickDrawerPrivate::handleMove(QQuickItem *item, const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN19QQuickDrawerPrivate10handleMoveEP10QQuickItemRK7QPointF'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDrawerPrivate10handleMoveEP10QQuickItemRK7Q'
          'PointFm')
    return self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QQuickItem, QPointF, int)
  @overload(NoneType, QPointF, int)
  def handleRelease(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::handleRelease(QQuickItem *item,
    const QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#handleRelease

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickDrawerPrivate::handleRelease(QQuickItem *item, const
    #      QPointF &point, ulong timestamp)
    ritual = (
        'ritual_ZN19QQuickDrawerPrivate13handleReleaseEP10QQuickItemRK7QPoi'
        'ntFm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDrawerPrivate13handleReleaseEP10QQuickItemR'
          'K7QPointFm')
    return self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(point, 'QPointF'), timestamp,
    )

  def handleUngrab(self) -> None:
    """
    Calls Qt's 'void QQuickDrawerPrivate::handleUngrab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#handleUngrab
    """
    #  void QQuickDrawerPrivate::handleUngrab()
    ritual = 'ritual_ZN19QQuickDrawerPrivate12handleUngrabEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDrawerPrivate12handleUngrabEv'
    self.uglySide.call(ritual)

  def prepareEnterTransition(self) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::prepareEnterTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#prepareEnterTransition
    """
    #  bool QQuickDrawerPrivate::prepareEnterTransition()
    ritual = 'ritual_ZN19QQuickDrawerPrivate22prepareEnterTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDrawerPrivate22prepareEnterTransitionEv'
    return self.uglySide.call(ritual)

  def prepareExitTransition(self) -> bool:
    """
    Calls Qt's 'bool QQuickDrawerPrivate::prepareExitTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrawerprivate.html#prepareExitTransition
    """
    #  bool QQuickDrawerPrivate::prepareExitTransition()
    ritual = 'ritual_ZN19QQuickDrawerPrivate21prepareExitTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDrawerPrivate21prepareExitTransitionEv'
    return self.uglySide.call(ritual)
