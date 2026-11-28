"""
QCanvasConicalGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasconicalgradient.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QCanvasGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
  from . import QCanvasBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBrush = WAIT['QCanvasBrush']
  QPointF = WAIT['QPointF']


class QCanvasConicalGradient(QCanvasGradient):
  """
  The cute side of Qt's QCanvasConicalGradient: a plain Python object
  standing in front of one C++ QCanvasConicalGradient.

  It is built on the cute 'QCanvasGradient', as Qt's QCanvasConicalGradient
  is built on Qt's QCanvasGradient, and has everything that class has.

  C++ hands a QCanvasConicalGradient around as a copy, so every C++
  QCanvasConicalGradient behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasConicalGradient that has a ritual and that
  Python can call so far, 4 names in all: 'centerPosition',
  'setCenterPosition', 'startAngle', 'setStartAngle'. It can be made from
  Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasConicalGradient &QCanvasConicalGradient::operator=(const
    QCanvasConicalGradient &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's
    'QCanvasConicalGradient::QCanvasConicalGradient(QCanvasConicalGradient
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasConicalGradient
    &QCanvasConicalGradient::operator=(QCanvasConicalGradient &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasConicalGradient::~QCanvasConicalGradient()': the destructor:
    Python removes its C++ QCanvasConicalGradient by it, and has no other use
    for it.
  - Qt's 'void QCanvasConicalGradient::swap(QCanvasConicalGradient &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCanvasConicalGradient is created at the first use, not by
    'QCanvasConicalGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasConicalGradient back gives a copy the ritual
    made for Python, in a new cute QCanvasConicalGradient.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasConicalGradient'

  #  Qt's '~QCanvasConicalGradient()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasConicalGradient behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QCanvasConicalGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def centerPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasConicalGradient::centerPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#centerPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasConicalGradient::centerPosition() const
    address = self.uglySide.call(
        'ritual_ZNK22QCanvasConicalGradient14centerPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QCanvasConicalGradient::startAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#startAngle
    """
    #  qreal QCanvasConicalGradient::startAngle() const
    return self.uglySide.call(
        'ritual_ZNK22QCanvasConicalGradient10startAngleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setCenterPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasConicalGradient::setCenterPosition(qreal x, qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#setCenterPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasConicalGradient::setCenterPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN22QCanvasConicalGradient17setCenterPositionEdd', x, y,
    )

  @overload(QPointF)
  def setCenterPosition(self, center: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasConicalGradient::setCenterPosition(QPointF
    center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#setCenterPosition

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasConicalGradient::setCenterPosition(QPointF center)
    self.uglySide.call(
        'ritual_ZN22QCanvasConicalGradient17setCenterPositionE7QPointF',
        self._valueOf(center, 'QPointF'),
    )

  @overload(float)
  def setStartAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QCanvasConicalGradient::setStartAngle(qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#setStartAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QCanvasConicalGradient::setStartAngle(qreal angle)
    self.uglySide.call(
        'ritual_ZN22QCanvasConicalGradient13setStartAngleEd', angle,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasConicalGradient::QCanvasConicalGradient()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#QCanvasConicalGradient
    """
    #  QCanvasConicalGradient::QCanvasConicalGradient()
    self._noteCreation(QCanvasConicalGradient, lambda: Rituals.call(
        'ritual_ZN22QCanvasConicalGradientC1Ev',
    ))

  @overload(float, float, float)
  def __init__(
      self,
      centerX: float,
      centerY: float,
      startAngle: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasConicalGradient::QCanvasConicalGradient(qreal centerX, qreal
    centerY, qreal startAngle)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#QCanvasConicalGradient

    Parameters
    ----------

    centerX : float
      Passed on as it is.

    centerY : float
      Passed on as it is.

    startAngle : float
      Passed on as it is.
    """
    #  QCanvasConicalGradient::QCanvasConicalGradient(qreal centerX, qreal
    #      centerY, qreal startAngle)
    self._noteCreation(QCanvasConicalGradient, lambda: Rituals.call(
        'ritual_ZN22QCanvasConicalGradientC1Eddd',
        centerX, centerY, startAngle,
    ))

  @overload(QPointF, float)
  def __init__(self, center: QPointF, startAngle: float) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasConicalGradient::QCanvasConicalGradient(QPointF center, qreal
    startAngle)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#QCanvasConicalGradient

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    startAngle : float
      Passed on as it is.
    """
    #  QCanvasConicalGradient::QCanvasConicalGradient(QPointF center, qreal
    #      startAngle)
    self._noteCreation(QCanvasConicalGradient, lambda: Rituals.call(
        'ritual_ZN22QCanvasConicalGradientC1E7QPointFd',
        self._valueOf(center, 'QPointF'), startAngle,
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasConicalGradient) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasConicalGradient::QCanvasConicalGradient(const
    QCanvasConicalGradient &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#QCanvasConicalGradient

    Parameters
    ----------

    a0 : QCanvasConicalGradient
      Passed on as a value: Qt reads the C++ QCanvasConicalGradient, which
      stays Python's own.
    """
    #  QCanvasConicalGradient::QCanvasConicalGradient(const
    #      QCanvasConicalGradient &a0)
    self._noteCreation(QCanvasConicalGradient, lambda: Rituals.call(
        'ritual_ZN22QCanvasConicalGradientC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasBrush)
  def __init__(self, brush: QCanvasBrush) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasConicalGradient::QCanvasConicalGradient(const QCanvasBrush
    &brush)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasconicalgradient.html#QCanvasConicalGradient

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  QCanvasConicalGradient::QCanvasConicalGradient(const QCanvasBrush
    #      &brush)
    self._noteCreation(QCanvasConicalGradient, lambda: Rituals.call(
        'ritual_ZN22QCanvasConicalGradientC1ERK12QCanvasBrush',
        self._valueOf(brush),
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
