"""
QFixedPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfixed_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QFixedPoint to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
  from . import QFixed
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFixed = WAIT['QFixed']
  QPointF = WAIT['QPointF']


class QFixedPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFixedPoint: a plain Python object standing in front
  of one C++ QFixedPoint.

  C++ hands a QFixedPoint around as a copy, so every C++ QFixedPoint behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFixedPoint that has a ritual and that Python can
  call so far, 3 names in all: 'toPointF', 'fromPointF', '__eq__'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFixedPoint::~QFixedPoint()': the destructor: Python removes its
    C++ QFixedPoint by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QFixedPoint is created at the first use, not by
    'QFixedPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFixedPoint back gives a copy the ritual made for
    Python, in a new cute QFixedPoint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPointF)
  def fromPointF(p: QPointF) -> QFixedPoint:
    """
    Calls Qt's 'QFixedPoint QFixedPoint::fromPointF(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixedpoint.html#fromPointF

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QFixedPoint
      A new cute QFixedPoint around the copy Qt gave back. Python owns it.
    """
    #  QFixedPoint QFixedPoint::fromPointF(const QPointF &p)
    address = Rituals.call(
        'ritual_ZN11QFixedPoint10fromPointFERK7QPointF',
        CuteMixin._valueOf(p, 'QPointF'),
    )
    return QFixedPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFixedPoint'

  #  Qt's '~QFixedPoint()'. Naming it makes this a value class: Python owns
  #  every C++ QFixedPoint behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QFixedPointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QFixedPoint::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixedpoint.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QFixedPoint::toPointF() const
    address = self.uglySide.call('ritual_ZNK11QFixedPoint8toPointFEv')
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

  @overload(THIS)
  def __eq__(self, other: QFixedPoint) -> bool:
    """
    Calls Qt's 'bool QFixedPoint::operator==(const QFixedPoint &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixedpoint.html#operator==

    Parameters
    ----------

    other : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.
    """
    #  bool QFixedPoint::operator==(const QFixedPoint &other) const
    return self.uglySide.call(
        'ritual_ZNK11QFixedPointeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFixedPoint::QFixedPoint()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixedpoint.html#QFixedPoint
    """
    #  QFixedPoint::QFixedPoint()
    self._noteCreation(QFixedPoint, lambda: Rituals.call(
        'ritual_ZN11QFixedPointC1Ev',
    ))

  @overload(QFixed, QFixed)
  def __init__(self, _x: QFixed, _y: QFixed) -> None:
    """
    Notes what was given, for Qt's 'QFixedPoint::QFixedPoint(QFixed _x,
    QFixed _y)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixedpoint.html#QFixedPoint

    Parameters
    ----------

    _x : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    _y : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  QFixedPoint::QFixedPoint(QFixed _x, QFixed _y)
    self._noteCreation(QFixedPoint, lambda: Rituals.call(
        'ritual_ZN11QFixedPointC1E6QFixedS0_',
        self._valueOf(_x), self._valueOf(_y),
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
