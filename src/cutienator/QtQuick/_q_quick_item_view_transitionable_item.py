"""
QQuickItemViewTransitionableItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickItemViewTransitionableItem to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickItemViewTransitioner

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from . import QQuickItem, QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']
  QQuickTransition = WAIT['QQuickTransition']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemViewTransitionableItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickItemViewTransitionableItem: a plain Python
  object standing in front of one C++ QQuickItemViewTransitionableItem.

  C++ hands a QQuickItemViewTransitionableItem around as a copy, so every C++
  QQuickItemViewTransitionableItem behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickItemViewTransitionableItem that has a ritual
  and that Python can call so far, 15 names in all: 'itemX', 'itemY',
  'moveTo', 'transitionScheduledOrRunning', 'transitionRunning',
  'isPendingRemoval', 'prepareTransition', 'startTransition',
  'completeTransition', 'setNextTransition', 'transitionWillChangePosition',
  'finishedTransition', 'resetNextTransitionPos',
  'clearCurrentScheduledTransition', 'stopTransition'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQuickItemViewTransitionableItem::~QQuickItemViewTransitionableItem()':
    the destructor: Python removes its C++ QQuickItemViewTransitionableItem
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickItemViewTransitionableItem is created at the first use, not
    by 'QQuickItemViewTransitionableItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickItemViewTransitionableItem back gives a copy
    the ritual made for Python, in a new cute
    QQuickItemViewTransitionableItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemViewTransitionableItem'

  #  Qt's '~QQuickItemViewTransitionableItem()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickItemViewTransitionableItem behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QQuickItemViewTransitionableItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def itemX(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewTransitionableItem::itemX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html#itemX
    """
    #  qreal QQuickItemViewTransitionableItem::itemX() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickItemViewTransitionableItem5itemXEv',
    )

  def itemY(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewTransitionableItem::itemY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html#itemY
    """
    #  qreal QQuickItemViewTransitionableItem::itemY() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickItemViewTransitionableItem5itemYEv',
    )

  def transitionScheduledOrRunning(self) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemViewTransitionableItem::transitionScheduledOrRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  bool QQuickItemViewTransitionableItem::transitionScheduledOrRunning()
    #      const
    return self.uglySide.call(
        'ritual_ZNK32QQuickItemViewTransitionableItem28transitionScheduledO'
        'rRunningEv',
    )

  def transitionRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewTransitionableItem::transitionRunning()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  bool QQuickItemViewTransitionableItem::transitionRunning() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickItemViewTransitionableItem17transitionRunningEv',
    )

  def isPendingRemoval(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewTransitionableItem::isPendingRemoval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  bool QQuickItemViewTransitionableItem::isPendingRemoval() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickItemViewTransitionableItem16isPendingRemovalEv',
    )

  def transitionWillChangePosition(self) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemViewTransitionableItem::transitionWillChangePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  bool QQuickItemViewTransitionableItem::transitionWillChangePosition()
    #      const
    return self.uglySide.call(
        'ritual_ZNK32QQuickItemViewTransitionableItem28transitionWillChange'
        'PositionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItemViewTransitioner.TransitionType, bool)
  def setNextTransition(
      self,
      a0: QQuickItemViewTransitioner.TransitionType,
      isTargetItem: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitionableItem::setNextTransition(
    QQuickItemViewTransitioner::TransitionType a0, bool isTargetItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html

    Parameters
    ----------

    a0 : QQuickItemViewTransitioner.TransitionType
      Passed on as its number.

    isTargetItem : bool
      Passed on as it is.
    """
    #  void QQuickItemViewTransitionableItem::setNextTransition(
    #      QQuickItemViewTransitioner::TransitionType a0, bool isTargetItem)
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem17setNextTransitionEN26'
        'QQuickItemViewTransitioner14TransitionTypeEb',
        a0.value, isTargetItem,
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

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, i: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemViewTransitionableItem::QQuickItemViewTransitionableItem(
    QQuickItem *i)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html

    Parameters
    ----------

    i : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickItemViewTransitionableItem::
    #      QQuickItemViewTransitionableItem(QQuickItem *i)
    self._noteCreation(
        QQuickItemViewTransitionableItem, lambda: Rituals.call(
            'ritual_ZN32QQuickItemViewTransitionableItemC1EP10QQuickItem',
            self._addressOf(i),
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

  @overload(QPointF)
  @overload(QPointF, bool)
  def moveTo(self, pos: QPointF, immediate: bool = False) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitionableItem::moveTo(const QPointF
    &pos, bool immediate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html#moveTo

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    immediate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickItemViewTransitionableItem::moveTo(const QPointF &pos, bool
    #      immediate)
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem6moveToERK7QPointFb',
        self._valueOf(pos, 'QPointF'), immediate,
    )

  @overload(QQuickItemViewTransitioner, int, QRectF)
  @overload(NoneType, int, QRectF)
  def prepareTransition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
      index: int,
      viewBounds: QRectF,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewTransitionableItem::prepareTransition(
    QQuickItemViewTransitioner *transitioner, int index, const QRectF
    &viewBounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    viewBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QQuickItemViewTransitionableItem::prepareTransition(
    #      QQuickItemViewTransitioner *transitioner, int index, const QRectF
    #      &viewBounds)
    return self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem17prepareTransitionEP26'
        'QQuickItemViewTransitioneriRK6QRectF',
        self._addressOf(transitioner), index, self._valueOf(viewBounds),
    )

  @overload(QQuickItemViewTransitioner, int)
  @overload(NoneType, int)
  def startTransition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitionableItem::startTransition(
    QQuickItemViewTransitioner *transitioner, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QQuickItemViewTransitionableItem::startTransition(
    #      QQuickItemViewTransitioner *transitioner, int index)
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem15startTransitionEP26QQ'
        'uickItemViewTransitioneri',
        self._addressOf(transitioner), index,
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def completeTransition(
      self,
      quickTransition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewTransitionableItem::completeTransition(QQuickTransition
    *quickTransition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html

    Parameters
    ----------

    quickTransition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewTransitionableItem::completeTransition(
    #      QQuickTransition *quickTransition)
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem18completeTransitionEP1'
        '6QQuickTransition',
        self._addressOf(quickTransition),
    )

  def finishedTransition(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitionableItem::finishedTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  void QQuickItemViewTransitionableItem::finishedTransition()
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem18finishedTransitionEv',
    )

  def resetNextTransitionPos(self) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewTransitionableItem::resetNextTransitionPos()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  void QQuickItemViewTransitionableItem::resetNextTransitionPos()
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem22resetNextTransitionPo'
        'sEv',
    )

  def clearCurrentScheduledTransition(self) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewTransitionableItem::clearCurrentScheduledTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  void
    #      QQuickItemViewTransitionableItem::clearCurrentScheduledTransition(
    #      )
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem31clearCurrentScheduled'
        'TransitionEv',
    )

  def stopTransition(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitionableItem::stopTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionableitem.html
    """
    #  void QQuickItemViewTransitionableItem::stopTransition()
    self.uglySide.call(
        'ritual_ZN32QQuickItemViewTransitionableItem14stopTransitionEv',
    )
