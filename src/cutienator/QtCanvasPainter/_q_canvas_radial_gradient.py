"""
QCanvasRadialGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasradialgradient.h, Qt 6.12.0. Changes made here are
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


class QCanvasRadialGradient(QCanvasGradient):
  """
  The cute side of Qt's QCanvasRadialGradient: a plain Python object standing
  in front of one C++ QCanvasRadialGradient.

  It is built on the cute 'QCanvasGradient', as Qt's QCanvasRadialGradient is
  built on Qt's QCanvasGradient, and has everything that class has.

  C++ hands a QCanvasRadialGradient around as a copy, so every C++
  QCanvasRadialGradient behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasRadialGradient that has a ritual and that
  Python can call so far, 10 names in all: 'centerPosition',
  'setCenterPosition', 'innerCenterPosition', 'setInnerCenterPosition',
  'outerCenterPosition', 'setOuterCenterPosition', 'outerRadius',
  'setOuterRadius', 'innerRadius', 'setInnerRadius'. It can be made from
  Python, in 7 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasRadialGradient &QCanvasRadialGradient::operator=(const
    QCanvasRadialGradient &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanvasRadialGradient::QCanvasRadialGradient(QCanvasRadialGradient
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasRadialGradient
    &QCanvasRadialGradient::operator=(QCanvasRadialGradient &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasRadialGradient::~QCanvasRadialGradient()': the destructor:
    Python removes its C++ QCanvasRadialGradient by it, and has no other use
    for it.
  - Qt's 'void QCanvasRadialGradient::swap(QCanvasRadialGradient &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCanvasRadialGradient is created at the first use, not by
    'QCanvasRadialGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasRadialGradient back gives a copy the ritual
    made for Python, in a new cute QCanvasRadialGradient.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasRadialGradient'

  #  Qt's '~QCanvasRadialGradient()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasRadialGradient behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QCanvasRadialGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def centerPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasRadialGradient::centerPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#centerPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasRadialGradient::centerPosition() const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasRadialGradient14centerPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def innerCenterPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasRadialGradient::innerCenterPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#innerCenterPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasRadialGradient::innerCenterPosition() const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasRadialGradient19innerCenterPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def outerCenterPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasRadialGradient::outerCenterPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#outerCenterPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasRadialGradient::outerCenterPosition() const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasRadialGradient19outerCenterPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def outerRadius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasRadialGradient::outerRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#outerRadius
    """
    #  qreal QCanvasRadialGradient::outerRadius() const
    return self.uglySide.call(
        'ritual_ZNK21QCanvasRadialGradient11outerRadiusEv',
    )

  def innerRadius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasRadialGradient::innerRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#innerRadius
    """
    #  qreal QCanvasRadialGradient::innerRadius() const
    return self.uglySide.call(
        'ritual_ZNK21QCanvasRadialGradient11innerRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setCenterPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setCenterPosition(qreal x, qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setCenterPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasRadialGradient::setCenterPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient17setCenterPositionEdd', x, y,
    )

  @overload(QPointF)
  def setCenterPosition(self, center: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setCenterPosition(QPointF
    center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setCenterPosition

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasRadialGradient::setCenterPosition(QPointF center)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient17setCenterPositionE7QPointF',
        self._valueOf(center, 'QPointF'),
    )

  @overload(float, float)
  def setInnerCenterPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setInnerCenterPosition(qreal x,
    qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setInnerCenterPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasRadialGradient::setInnerCenterPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient22setInnerCenterPositionEdd', x, y,
    )

  @overload(QPointF)
  def setInnerCenterPosition(self, center: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setInnerCenterPosition(QPointF
    center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setInnerCenterPosition

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasRadialGradient::setInnerCenterPosition(QPointF center)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient22setInnerCenterPositionE7QPointF',
        self._valueOf(center, 'QPointF'),
    )

  @overload(float, float)
  def setOuterCenterPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setOuterCenterPosition(qreal x,
    qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setOuterCenterPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasRadialGradient::setOuterCenterPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient22setOuterCenterPositionEdd', x, y,
    )

  @overload(QPointF)
  def setOuterCenterPosition(self, center: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setOuterCenterPosition(QPointF
    center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setOuterCenterPosition

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasRadialGradient::setOuterCenterPosition(QPointF center)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient22setOuterCenterPositionE7QPointF',
        self._valueOf(center, 'QPointF'),
    )

  @overload(float)
  def setOuterRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setOuterRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setOuterRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasRadialGradient::setOuterRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient14setOuterRadiusEd', radius,
    )

  @overload(float)
  def setInnerRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasRadialGradient::setInnerRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#setInnerRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasRadialGradient::setInnerRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN21QCanvasRadialGradient14setInnerRadiusEd', radius,
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
    'QCanvasRadialGradient::QCanvasRadialGradient()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#QCanvasRadialGradient
    """
    #  QCanvasRadialGradient::QCanvasRadialGradient()
    self._noteCreation(QCanvasRadialGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasRadialGradientC1Ev',
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      centerX: float,
      centerY: float,
      innerRadius: float,
      outerRadius: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasRadialGradient::QCanvasRadialGradient(qreal centerX, qreal
    centerY, qreal innerRadius, qreal outerRadius)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#QCanvasRadialGradient

    Parameters
    ----------

    centerX : float
      Passed on as it is.

    centerY : float
      Passed on as it is.

    innerRadius : float
      Passed on as it is.

    outerRadius : float
      Passed on as it is.
    """
    #  QCanvasRadialGradient::QCanvasRadialGradient(qreal centerX, qreal
    #      centerY, qreal innerRadius, qreal outerRadius)
    self._noteCreation(QCanvasRadialGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasRadialGradientC1Edddd',
        centerX, centerY, innerRadius, outerRadius,
    ))

  @overload(QPointF, float, float)
  def __init__(
      self,
      centerPosition: QPointF,
      innerRadius: float,
      outerRadius: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasRadialGradient::QCanvasRadialGradient(QPointF centerPosition,
    qreal innerRadius, qreal outerRadius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#QCanvasRadialGradient

    Parameters
    ----------

    centerPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    innerRadius : float
      Passed on as it is.

    outerRadius : float
      Passed on as it is.
    """
    #  QCanvasRadialGradient::QCanvasRadialGradient(QPointF centerPosition,
    #      qreal innerRadius, qreal outerRadius)
    self._noteCreation(QCanvasRadialGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasRadialGradientC1E7QPointFdd',
        self._valueOf(centerPosition, 'QPointF'), innerRadius, outerRadius,
    ))

  @overload(float, float, float, float, float, float)
  def __init__(
      self,
      innerCenterX: float,
      innerCenterY: float,
      innerRadius: float,
      outerCenterX: float,
      outerCenterY: float,
      outerRadius: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasRadialGradient::QCanvasRadialGradient(qreal innerCenterX, qreal
    innerCenterY, qreal innerRadius, qreal outerCenterX, qreal outerCenterY,
    qreal outerRadius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#QCanvasRadialGradient

    Parameters
    ----------

    innerCenterX : float
      Passed on as it is.

    innerCenterY : float
      Passed on as it is.

    innerRadius : float
      Passed on as it is.

    outerCenterX : float
      Passed on as it is.

    outerCenterY : float
      Passed on as it is.

    outerRadius : float
      Passed on as it is.
    """
    #  QCanvasRadialGradient::QCanvasRadialGradient(qreal innerCenterX, qreal
    #      innerCenterY, qreal innerRadius, qreal outerCenterX, qreal
    #      outerCenterY, qreal outerRadius)
    self._noteCreation(QCanvasRadialGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasRadialGradientC1Edddddd',
        innerCenterX, innerCenterY, innerRadius, outerCenterX, outerCenterY,
        outerRadius,
    ))

  @overload(QPointF, float, QPointF, float)
  def __init__(
      self,
      innerCenterPosition: QPointF,
      innerRadius: float,
      outerCenterPosition: QPointF,
      outerRadius: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasRadialGradient::QCanvasRadialGradient(QPointF
    innerCenterPosition, qreal innerRadius, QPointF outerCenterPosition,
    qreal outerRadius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#QCanvasRadialGradient

    Parameters
    ----------

    innerCenterPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    innerRadius : float
      Passed on as it is.

    outerCenterPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    outerRadius : float
      Passed on as it is.
    """
    #  QCanvasRadialGradient::QCanvasRadialGradient(QPointF
    #      innerCenterPosition, qreal innerRadius, QPointF
    #      outerCenterPosition, qreal outerRadius)
    self._noteCreation(QCanvasRadialGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasRadialGradientC1E7QPointFdS0_d',
        self._valueOf(innerCenterPosition, 'QPointF'), innerRadius,
        self._valueOf(outerCenterPosition, 'QPointF'), outerRadius,
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasRadialGradient) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasRadialGradient::QCanvasRadialGradient(const QCanvasRadialGradient
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#QCanvasRadialGradient

    Parameters
    ----------

    a0 : QCanvasRadialGradient
      Passed on as a value: Qt reads the C++ QCanvasRadialGradient, which
      stays Python's own.
    """
    #  QCanvasRadialGradient::QCanvasRadialGradient(const
    #      QCanvasRadialGradient &a0)
    self._noteCreation(QCanvasRadialGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasRadialGradientC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasBrush)
  def __init__(self, brush: QCanvasBrush) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasRadialGradient::QCanvasRadialGradient(const QCanvasBrush
    &brush)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradient.html#QCanvasRadialGradient

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  QCanvasRadialGradient::QCanvasRadialGradient(const QCanvasBrush
    #      &brush)
    self._noteCreation(QCanvasRadialGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasRadialGradientC1ERK12QCanvasBrush',
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
