"""
QGraphicsLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicslayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGraphicsLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsLayout(QGraphicsLayoutItem):
  """
  The cute side of Qt's QGraphicsLayout: a plain Python object standing in
  front of one C++ QGraphicsLayout.

  It is built on the cute 'QGraphicsLayoutItem', as Qt's QGraphicsLayout is
  built on Qt's QGraphicsLayoutItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsLayout that has a ritual and that Python
  can call so far, 11 names in all: 'setContentsMargins', 'activate',
  'isActivated', 'invalidate', 'updateGeometry', 'widgetEvent', 'count',
  'itemAt', 'removeAt', 'setInstantInvalidatePropagation',
  'instantInvalidatePropagation'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsLayout::~QGraphicsLayout()': the destructor: Python never
    removes a C++ QGraphicsLayout.
  - Qt's 'void QGraphicsLayout::getContentsMargins(qreal *left, qreal *top,
    qreal *right, qreal *bottom) const': takes a number to change where it
    is.

  What has no ritual
  ------------------

  7 of the 20 functions Qt declares: 2 protected; 2 forbidden; 2 private; 1
  the class is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QGraphicsLayout is created at the first use, not by
    'QGraphicsLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsLayout.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(bool)
  def setInstantInvalidatePropagation(enable: bool) -> None:
    """
    Calls Qt's 'void QGraphicsLayout::setInstantInvalidatePropagation(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayout.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QGraphicsLayout::setInstantInvalidatePropagation(bool enable)
    Rituals.call(
        'ritual_ZN15QGraphicsLayout31setInstantInvalidatePropagationEb',
        enable,
    )

  @staticmethod
  def instantInvalidatePropagation() -> bool:
    """
    Calls Qt's 'bool QGraphicsLayout::instantInvalidatePropagation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayout.html#instantInvalidatePropagation
    """
    #  bool QGraphicsLayout::instantInvalidatePropagation()
    return Rituals.call(
        'ritual_ZN15QGraphicsLayout28instantInvalidatePropagationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isActivated(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsLayout::isActivated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayout.html#isActivated
    """
    #  bool QGraphicsLayout::isActivated() const
    return self.uglySide.call('ritual_ZNK15QGraphicsLayout11isActivatedEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QGraphicsLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayout.html#count
    """
    #  int QGraphicsLayout::count() const
    return self.uglySide.call('ritual_ZNK15QGraphicsLayout5countEv')

  @overload(int)
  def itemAt(self, i: int) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *QGraphicsLayout::itemAt(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayout.html#itemAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *QGraphicsLayout::itemAt(int i) const
    address = self.uglySide.call('ritual_ZNK15QGraphicsLayout6itemAtEi', i)
    return QGraphicsLayoutItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, float, float)
  def setContentsMargins(
      self,
      left: float,
      top: float,
      right: float,
      bottom: float,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsLayout::setContentsMargins(qreal left, qreal
    top, qreal right, qreal bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayout.html#setContentsMargins

    Parameters
    ----------

    left : float
      Passed on as it is.

    top : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.
    """
    #  void QGraphicsLayout::setContentsMargins(qreal left, qreal top, qreal
    #      right, qreal bottom)
    self.uglySide.call(
        'ritual_ZN15QGraphicsLayout18setContentsMarginsEdddd',
        left, top, right, bottom,
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

  def activate(self) -> None:
    """
    Calls Qt's 'void QGraphicsLayout::activate()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayout.html#activate
    """
    #  void QGraphicsLayout::activate()
    self.uglySide.call('ritual_ZN15QGraphicsLayout8activateEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QGraphicsLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayout.html#invalidate
    """
    #  void QGraphicsLayout::invalidate()
    self.uglySide.call('ritual_ZN15QGraphicsLayout10invalidateEv')

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QGraphicsLayout::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayout.html#updateGeometry
    """
    #  void QGraphicsLayout::updateGeometry()
    self.uglySide.call('ritual_ZN15QGraphicsLayout14updateGeometryEv')

  @overload(QEvent)
  @overload(NoneType)
  def widgetEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsLayout::widgetEvent(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayout.html#widgetEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLayout::widgetEvent(QEvent *e)
    self.uglySide.call(
        'ritual_ZN15QGraphicsLayout11widgetEventEP6QEvent',
        self._addressOf(e),
    )

  @overload(int)
  def removeAt(self, index: int) -> None:
    """
    Calls Qt's 'void QGraphicsLayout::removeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayout.html#removeAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGraphicsLayout::removeAt(int index)
    self.uglySide.call('ritual_ZN15QGraphicsLayout8removeAtEi', index)
