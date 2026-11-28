"""
QQuickVelocityCalculator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickvelocitycalculator_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickVelocityCalculator to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QQuickVelocityCalculator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickVelocityCalculator: a plain Python object
  standing in front of one C++ QQuickVelocityCalculator.

  C++ hands a QQuickVelocityCalculator around as a copy, so every C++
  QQuickVelocityCalculator behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickVelocityCalculator that has a ritual and that
  Python can call so far, 4 names in all: 'startMeasuring', 'stopMeasuring',
  'reset', 'velocity'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickVelocityCalculator::~QQuickVelocityCalculator()': the
    destructor: Python removes its C++ QQuickVelocityCalculator by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickVelocityCalculator is created at the first use, not by
    'QQuickVelocityCalculator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickVelocityCalculator back gives a copy the ritual
    made for Python, in a new cute QQuickVelocityCalculator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVelocityCalculator'

  #  Qt's '~QQuickVelocityCalculator()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickVelocityCalculator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQuickVelocityCalculatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def velocity(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickVelocityCalculator::velocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvelocitycalculator.html#velocity

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickVelocityCalculator::velocity() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickVelocityCalculator8velocityEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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

  @overload(QPointF, int)
  def startMeasuring(self, point1: QPointF, timestamp: int) -> None:
    """
    Calls Qt's 'void QQuickVelocityCalculator::startMeasuring(const QPointF
    &point1, qint64 timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvelocitycalculator.html#startMeasuring

    Parameters
    ----------

    point1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  void QQuickVelocityCalculator::startMeasuring(const QPointF &point1,
    #      qint64 timestamp)
    self.uglySide.call(
        'ritual_ZN24QQuickVelocityCalculator14startMeasuringERK7QPointFx',
        self._valueOf(point1, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def stopMeasuring(self, m_point2: QPointF, timestamp: int) -> None:
    """
    Calls Qt's 'void QQuickVelocityCalculator::stopMeasuring(const QPointF
    &m_point2, qint64 timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvelocitycalculator.html#stopMeasuring

    Parameters
    ----------

    m_point2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  void QQuickVelocityCalculator::stopMeasuring(const QPointF &m_point2,
    #      qint64 timestamp)
    self.uglySide.call(
        'ritual_ZN24QQuickVelocityCalculator13stopMeasuringERK7QPointFx',
        self._valueOf(m_point2, 'QPointF'), timestamp,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickVelocityCalculator::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvelocitycalculator.html#reset
    """
    #  void QQuickVelocityCalculator::reset()
    self.uglySide.call('ritual_ZN24QQuickVelocityCalculator5resetEv')
