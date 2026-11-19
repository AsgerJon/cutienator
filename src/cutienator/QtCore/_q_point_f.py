"""
QPointF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qpoint.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_point import QPoint


class QPointF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPointF: a plain Python object standing in front of
  one C++ QPointF.

  C++ hands a QPointF around as a copy, so every C++ QPointF behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPointF that has a ritual and that Python can call
  so far, 9 names in all: 'manhattanLength', 'isNull', 'x', 'y', 'setX',
  'setY', 'transposed', 'dotProduct', 'toPoint'. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPointF::~QPointF()': the destructor: Python removes its C++
    QPointF by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 19 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPointF is created at the first use, not by 'QPointF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPointF back gives a copy the ritual made for Python,
    in a new cute QPointF.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(p1: QPointF, p2: QPointF) -> float:
    """
    Calls Qt's 'qreal QPointF::dotProduct(const QPointF &p1, const QPointF
    &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#dotProduct

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QPointF::dotProduct(const QPointF &p1, const QPointF &p2)
    return Rituals.call(
        'ritual_ZN7QPointF10dotProductERKS_S1_',
        CuteMixin._valueOf(p1), CuteMixin._valueOf(p2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPointF'

  #  Qt's '~QPointF()'. Naming it makes this a value class: Python owns every
  #  C++ QPointF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QPointFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def manhattanLength(self) -> float:
    """
    Calls Qt's 'qreal QPointF::manhattanLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#manhattanLength
    """
    #  qreal QPointF::manhattanLength() const
    return self.uglySide.call('ritual_ZNK7QPointF15manhattanLengthEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPointF::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#isNull
    """
    #  bool QPointF::isNull() const
    return self.uglySide.call('ritual_ZNK7QPointF6isNullEv')

  def x(self) -> float:
    """
    Calls Qt's 'qreal QPointF::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#x
    """
    #  qreal QPointF::x() const
    return self.uglySide.call('ritual_ZNK7QPointF1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QPointF::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#y
    """
    #  qreal QPointF::y() const
    return self.uglySide.call('ritual_ZNK7QPointF1yEv')

  def transposed(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPointF::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#transposed

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPointF::transposed() const
    address = self.uglySide.call('ritual_ZNK7QPointF10transposedEv')
    return QPointF._cuteOwning(address)

  def toPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPointF::toPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#toPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPointF::toPoint() const
    address = self.uglySide.call('ritual_ZNK7QPointF7toPointEv')
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QPointF::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QPointF::setX(qreal x)
    self.uglySide.call('ritual_ZN7QPointF4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QPointF::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QPointF::setY(qreal y)
    self.uglySide.call('ritual_ZN7QPointF4setYEd', y)

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
    Notes what was given, for Qt's 'QPointF::QPointF()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#QPointF
    """
    #  QPointF::QPointF()
    self._noteCreation(QPointF, lambda: Rituals.call(
        'ritual_ZN7QPointFC1Ev',
    ))

  @overload(QPoint)
  def __init__(self, p: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QPointF::QPointF(const QPoint &p)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#QPointF

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QPointF::QPointF(const QPoint &p)
    self._noteCreation(QPointF, lambda: Rituals.call(
        'ritual_ZN7QPointFC1ERK6QPoint', self._valueOf(p),
    ))

  @overload(float, float)
  def __init__(self, xpos: float, ypos: float) -> None:
    """
    Notes what was given, for Qt's 'QPointF::QPointF(qreal xpos, qreal
    ypos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#QPointF

    Parameters
    ----------

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.
    """
    #  QPointF::QPointF(qreal xpos, qreal ypos)
    self._noteCreation(QPointF, lambda: Rituals.call(
        'ritual_ZN7QPointFC1Edd', xpos, ypos,
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
