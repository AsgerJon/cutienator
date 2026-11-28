"""
QConicalGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QConicalGradient(QGradient):
  """
  The cute side of Qt's QConicalGradient: a plain Python object standing in
  front of one C++ QConicalGradient.

  It is built on the cute 'QGradient', as Qt's QConicalGradient is built on
  Qt's QGradient, and has everything that class has.

  C++ hands a QConicalGradient around as a copy, so every C++
  QConicalGradient behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QConicalGradient that has a ritual and that Python
  can call so far, 4 names in all: 'center', 'setCenter', 'angle',
  'setAngle'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QConicalGradient::~QConicalGradient()': the destructor: Python
    removes its C++ QConicalGradient by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QConicalGradient is created at the first use, not by
    'QConicalGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QConicalGradient back gives a copy the ritual made
    for Python, in a new cute QConicalGradient.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QConicalGradient'

  #  Qt's '~QConicalGradient()'. Naming it makes this a value class: Python
  #  owns every C++ QConicalGradient behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QConicalGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def center(self) -> QPointF:
    """
    Calls Qt's 'QPointF QConicalGradient::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qconicalgradient.html#center

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QConicalGradient::center() const
    address = self.uglySide.call('ritual_ZNK16QConicalGradient6centerEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QConicalGradient::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qconicalgradient.html#angle
    """
    #  qreal QConicalGradient::angle() const
    return self.uglySide.call('ritual_ZNK16QConicalGradient5angleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setCenter(self, center: QPointF) -> None:
    """
    Calls Qt's 'void QConicalGradient::setCenter(const QPointF &center)'.

    Qt's own words: https://doc.qt.io/qt-6/qconicalgradient.html#setCenter

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QConicalGradient::setCenter(const QPointF &center)
    self.uglySide.call(
        'ritual_ZN16QConicalGradient9setCenterERK7QPointF',
        self._valueOf(center, 'QPointF'),
    )

  @overload(float, float)
  def setCenter(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QConicalGradient::setCenter(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qconicalgradient.html#setCenter

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QConicalGradient::setCenter(qreal x, qreal y)
    self.uglySide.call('ritual_ZN16QConicalGradient9setCenterEdd', x, y)

  @overload(float)
  def setAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QConicalGradient::setAngle(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qconicalgradient.html#setAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QConicalGradient::setAngle(qreal angle)
    self.uglySide.call('ritual_ZN16QConicalGradient8setAngleEd', angle)

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
    Notes what was given, for Qt's 'QConicalGradient::QConicalGradient()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qconicalgradient.html#QConicalGradient
    """
    #  QConicalGradient::QConicalGradient()
    self._noteCreation(QConicalGradient, lambda: Rituals.call(
        'ritual_ZN16QConicalGradientC1Ev',
    ))

  @overload(QPointF, float)
  def __init__(self, center: QPointF, startAngle: float) -> None:
    """
    Notes what was given, for Qt's 'QConicalGradient::QConicalGradient(const
    QPointF &center, qreal startAngle)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qconicalgradient.html#QConicalGradient

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    startAngle : float
      Passed on as it is.
    """
    #  QConicalGradient::QConicalGradient(const QPointF &center, qreal
    #      startAngle)
    self._noteCreation(QConicalGradient, lambda: Rituals.call(
        'ritual_ZN16QConicalGradientC1ERK7QPointFd',
        self._valueOf(center, 'QPointF'), startAngle,
    ))

  @overload(float, float, float)
  def __init__(self, cx: float, cy: float, startAngle: float) -> None:
    """
    Notes what was given, for Qt's 'QConicalGradient::QConicalGradient(qreal
    cx, qreal cy, qreal startAngle)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qconicalgradient.html#QConicalGradient

    Parameters
    ----------

    cx : float
      Passed on as it is.

    cy : float
      Passed on as it is.

    startAngle : float
      Passed on as it is.
    """
    #  QConicalGradient::QConicalGradient(qreal cx, qreal cy, qreal
    #      startAngle)
    self._noteCreation(QConicalGradient, lambda: Rituals.call(
        'ritual_ZN16QConicalGradientC1Eddd', cx, cy, startAngle,
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
