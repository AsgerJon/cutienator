"""
SplineAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/splineanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means SplineAnimation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractAnimation, QList
from . import XYAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPointF, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QVariant = WAIT['QVariant']


class SplineAnimation(XYAnimation):
  """
  The cute side of Qt's SplineAnimation: a plain Python object standing in
  front of one C++ SplineAnimation.

  It is built on the cute 'XYAnimation', as Qt's SplineAnimation is built on
  Qt's XYAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's SplineAnimation that has a ritual and that Python
  can call so far, 4 names in all: 'setup', 'interpolated',
  'updateCurrentValue', 'updateState'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SplineAnimation::SplineAnimation(SplineChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
  - Qt's 'SplineAnimation::~SplineAnimation()': the destructor: Python never
    removes a C++ SplineAnimation.

  What to expect
  --------------

  - The C++ SplineAnimation is created at the first use, not by
    'SplineAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SplineAnimation.
  - Qt tells when it has removed the C++ SplineAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's SplineAnimation that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SplineAnimation'

  #  A C++ SplineAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SplineAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant, float)
  def interpolated(
      self,
      start: QVariant,
      end: QVariant,
      progress: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant SplineAnimation::interpolated(const QVariant &start,
    const QVariant &end, qreal progress) const'.

    Qt's own words: https://doc.qt.io/qt-6/splineanimation.html#interpolated

    Parameters
    ----------

    start : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    end : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    progress : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant SplineAnimation::interpolated(const QVariant &start, const
    #      QVariant &end, qreal progress) const
    ritual = 'ritual_ZNK15SplineAnimation12interpolatedERK8QVariantS2_d'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15SplineAnimation12interpolatedERK8QVariantS2_d')
    address = self.uglySide.call(
        ritual, self._valueOf(start), self._valueOf(end), progress,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'SplineAnimation::SplineAnimation(SplineChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'SplineAnimation.__init__' has no cute function yet. Qt's "
        "'SplineAnimation::SplineAnimation(SplineChartItem *item, int "
        "duration, QEasingCurve &curve)': takes a type Python has no way to "
        "hand over yet.")

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

  @overload(QList[QPointF], QList[QPointF], QList[QPointF], QList[QPointF])
  @overload(
      QList[QPointF], QList[QPointF], QList[QPointF], QList[QPointF], int,
  )
  def setup(
      self,
      oldPoints: QList[QPointF],
      newPoints: QList[QPointF],
      oldContorlPoints: QList[QPointF],
      newControlPoints: QList[QPointF],
      index: int = -1,
  ) -> None:
    """
    Calls Qt's 'void SplineAnimation::setup(const QList<QPointF> &oldPoints,
    const QList<QPointF> &newPoints, const QList<QPointF> &oldContorlPoints,
    const QList<QPointF> &newControlPoints, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/splineanimation.html#setup

    Parameters
    ----------

    oldPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    newPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    oldContorlPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    newControlPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void SplineAnimation::setup(const QList<QPointF> &oldPoints, const
    #      QList<QPointF> &newPoints, const QList<QPointF> &oldContorlPoints,
    #      const QList<QPointF> &newControlPoints, int index)
    self.uglySide.call(
        'ritual_ZN15SplineAnimation5setupERK5QListI7QPointFES4_S4_S4_i',
        self._valueOf(oldPoints), self._valueOf(newPoints),
        self._valueOf(oldContorlPoints), self._valueOf(newControlPoints),
        index,
    )

  @overload(QVariant)
  def updateCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void SplineAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splineanimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void SplineAnimation::updateCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN15SplineAnimation18updateCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineAnimation18updateCurrentValueERK8QVariant')
    self.uglySide.call(ritual, self._valueOf(value))

  @overload(QAbstractAnimation.State, QAbstractAnimation.State)
  def updateState(
      self,
      newState: QAbstractAnimation.State,
      oldState: QAbstractAnimation.State,
  ) -> None:
    """
    Calls Qt's 'void SplineAnimation::updateState(QAbstractAnimation::State
    newState, QAbstractAnimation::State oldState)'.

    Qt's own words: https://doc.qt.io/qt-6/splineanimation.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimation.State
      Passed on as its number.

    oldState : QAbstractAnimation.State
      Passed on as its number.
    """
    #  void SplineAnimation::updateState(QAbstractAnimation::State newState,
    #      QAbstractAnimation::State oldState)
    ritual = (
        'ritual_ZN15SplineAnimation11updateStateEN18QAbstractAnimation5Stat'
        'eES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineAnimation11updateStateEN18QAbstractAnimatio'
          'n5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)
