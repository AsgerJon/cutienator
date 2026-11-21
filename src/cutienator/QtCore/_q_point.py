"""
QPoint binding of the Qt C++
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

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QPointF


class QPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPoint: a plain Python object standing in front of
  one C++ QPoint.

  C++ hands a QPoint around as a copy, so every C++ QPoint behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPoint that has a ritual and that Python can call so
  far, 9 names in all: 'isNull', 'x', 'y', 'setX', 'setY', 'manhattanLength',
  'transposed', 'dotProduct', 'toPointF'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPoint::~QPoint()': the destructor: Python removes its C++ QPoint
    by it, and has no other use for it.

  What has no ritual
  ------------------

  9 of the 21 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QPoint is created at the first use, not by 'QPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPoint back gives a copy the ritual made for Python,
    in a new cute QPoint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(p1: QPoint, p2: QPoint) -> int:
    """
    Calls Qt's 'int QPoint::dotProduct(const QPoint &p1, const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#dotProduct

    Parameters
    ----------

    p1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QPoint::dotProduct(const QPoint &p1, const QPoint &p2)
    return Rituals.call(
        'ritual_ZN6QPoint10dotProductERKS_S1_',
        CuteMixin._valueOf(p1), CuteMixin._valueOf(p2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPoint'

  #  Qt's '~QPoint()'. Naming it makes this a value class: Python owns every
  #  C++ QPoint behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QPointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPoint::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#isNull
    """
    #  bool QPoint::isNull() const
    return self.uglySide.call('ritual_ZNK6QPoint6isNullEv')

  def x(self) -> int:
    """
    Calls Qt's 'int QPoint::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#x
    """
    #  int QPoint::x() const
    return self.uglySide.call('ritual_ZNK6QPoint1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QPoint::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#y
    """
    #  int QPoint::y() const
    return self.uglySide.call('ritual_ZNK6QPoint1yEv')

  def manhattanLength(self) -> int:
    """
    Calls Qt's 'int QPoint::manhattanLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#manhattanLength
    """
    #  int QPoint::manhattanLength() const
    return self.uglySide.call('ritual_ZNK6QPoint15manhattanLengthEv')

  def transposed(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPoint::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#transposed

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPoint::transposed() const
    address = self.uglySide.call('ritual_ZNK6QPoint10transposedEv')
    return QPoint._cuteOwning(address)

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPoint::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPoint::toPointF() const
    address = self.uglySide.call('ritual_ZNK6QPoint8toPointFEv')
    from . import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setX(self, x: int) -> None:
    """
    Calls Qt's 'void QPoint::setX(int x)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#setX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void QPoint::setX(int x)
    self.uglySide.call('ritual_ZN6QPoint4setXEi', x)

  @overload(int)
  def setY(self, y: int) -> None:
    """
    Calls Qt's 'void QPoint::setY(int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#setY

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  void QPoint::setY(int y)
    self.uglySide.call('ritual_ZN6QPoint4setYEi', y)

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
    Notes what was given, for Qt's 'QPoint::QPoint()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#QPoint
    """
    #  QPoint::QPoint()
    self._noteCreation(QPoint, lambda: Rituals.call('ritual_ZN6QPointC1Ev'))

  @overload(int, int)
  def __init__(self, xpos: int, ypos: int) -> None:
    """
    Notes what was given, for Qt's 'QPoint::QPoint(int xpos, int ypos)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#QPoint

    Parameters
    ----------

    xpos : int
      Passed on as it is.

    ypos : int
      Passed on as it is.
    """
    #  QPoint::QPoint(int xpos, int ypos)
    self._noteCreation(QPoint, lambda: Rituals.call(
        'ritual_ZN6QPointC1Eii', xpos, ypos,
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
