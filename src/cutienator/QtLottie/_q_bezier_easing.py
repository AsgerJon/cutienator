"""
QBezierEasing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qbeziereasing_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBezierEasing to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
  from ..QtGui import QBezier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QBezierEasing(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBezierEasing: a plain Python object standing in
  front of one C++ QBezierEasing.

  C++ hands a QBezierEasing around as a copy, so every C++ QBezierEasing
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBezierEasing that has a ritual and that Python can
  call so far, 4 names in all: 'addCubicBezierSegment', 'valueForProgress',
  'bezier', 'tForX'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBezierEasing::~QBezierEasing()': the destructor: Python removes
    its C++ QBezierEasing by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QBezierEasing is created at the first use, not by
    'QBezierEasing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBezierEasing back gives a copy the ritual made for
    Python, in a new cute QBezierEasing.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBezierEasing'

  #  Qt's '~QBezierEasing()'. Naming it makes this a value class: Python owns
  #  every C++ QBezierEasing behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QBezierEasingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def valueForProgress(self, progress: float) -> float:
    """
    Calls Qt's 'qreal QBezierEasing::valueForProgress(qreal progress) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbeziereasing.html#valueForProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  qreal QBezierEasing::valueForProgress(qreal progress) const
    return self.uglySide.call(
        'ritual_ZNK13QBezierEasing16valueForProgressEd', progress,
    )

  def bezier(self) -> QBezier:
    """
    Calls Qt's 'QBezier QBezierEasing::bezier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbeziereasing.html#bezier

    Returns
    -------

    QBezier
      A new cute QBezier around the copy Qt gave back. Python owns it.
    """
    #  QBezier QBezierEasing::bezier() const
    address = self.uglySide.call('ritual_ZNK13QBezierEasing6bezierEv')
    from ..QtGui import QBezier
    return QBezier._cuteOwning(address)

  @overload(float)
  def tForX(self, x: float) -> float:
    """
    Calls Qt's 'qreal QBezierEasing::tForX(qreal x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbeziereasing.html#tForX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  qreal QBezierEasing::tForX(qreal x) const
    return self.uglySide.call('ritual_ZNK13QBezierEasing5tForXEd', x)

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

  @overload(QPointF, QPointF, QPointF)
  def addCubicBezierSegment(
      self,
      c1: QPointF,
      c2: QPointF,
      endPoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QBezierEasing::addCubicBezierSegment(const QPointF &c1,
    const QPointF &c2, const QPointF &endPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbeziereasing.html#addCubicBezierSegment

    Parameters
    ----------

    c1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    c2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QBezierEasing::addCubicBezierSegment(const QPointF &c1, const
    #      QPointF &c2, const QPointF &endPoint)
    self.uglySide.call(
        'ritual_ZN13QBezierEasing21addCubicBezierSegmentERK7QPointFS2_S2_',
        self._valueOf(c1, 'QPointF'), self._valueOf(c2, 'QPointF'),
        self._valueOf(endPoint, 'QPointF'),
    )
