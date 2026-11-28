"""
QCanvasBoxGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasboxgradient.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QCanvasGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
  from . import QCanvasBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBrush = WAIT['QCanvasBrush']
  QRectF = WAIT['QRectF']


class QCanvasBoxGradient(QCanvasGradient):
  """
  The cute side of Qt's QCanvasBoxGradient: a plain Python object standing in
  front of one C++ QCanvasBoxGradient.

  It is built on the cute 'QCanvasGradient', as Qt's QCanvasBoxGradient is
  built on Qt's QCanvasGradient, and has everything that class has.

  C++ hands a QCanvasBoxGradient around as a copy, so every C++
  QCanvasBoxGradient behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasBoxGradient that has a ritual and that Python
  can call so far, 6 names in all: 'rect', 'setRect', 'feather',
  'setFeather', 'radius', 'setRadius'. It can be made from Python, in 5 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasBoxGradient &QCanvasBoxGradient::operator=(const
    QCanvasBoxGradient &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanvasBoxGradient::QCanvasBoxGradient(QCanvasBoxGradient &&a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasBoxGradient
    &QCanvasBoxGradient::operator=(QCanvasBoxGradient &&a0)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QCanvasBoxGradient::~QCanvasBoxGradient()': the destructor: Python
    removes its C++ QCanvasBoxGradient by it, and has no other use for it.
  - Qt's 'void QCanvasBoxGradient::swap(QCanvasBoxGradient &other)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCanvasBoxGradient is created at the first use, not by
    'QCanvasBoxGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasBoxGradient back gives a copy the ritual made
    for Python, in a new cute QCanvasBoxGradient.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasBoxGradient'

  #  Qt's '~QCanvasBoxGradient()'. Naming it makes this a value class: Python
  #  owns every C++ QCanvasBoxGradient behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QCanvasBoxGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasBoxGradient::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxgradient.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCanvasBoxGradient::rect() const
    address = self.uglySide.call('ritual_ZNK18QCanvasBoxGradient4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def feather(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxGradient::feather() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxgradient.html#feather
    """
    #  qreal QCanvasBoxGradient::feather() const
    return self.uglySide.call('ritual_ZNK18QCanvasBoxGradient7featherEv')

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxGradient::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxgradient.html#radius
    """
    #  qreal QCanvasBoxGradient::radius() const
    return self.uglySide.call('ritual_ZNK18QCanvasBoxGradient6radiusEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, width: float, height: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxGradient::setRect(qreal x, qreal y, qreal
    width, qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxgradient.html#setRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QCanvasBoxGradient::setRect(qreal x, qreal y, qreal width, qreal
    #      height)
    self.uglySide.call(
        'ritual_ZN18QCanvasBoxGradient7setRectEdddd', x, y, width, height,
    )

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasBoxGradient::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxgradient.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasBoxGradient::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN18QCanvasBoxGradient7setRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float)
  def setFeather(self, feather: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxGradient::setFeather(qreal feather)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxgradient.html#setFeather

    Parameters
    ----------

    feather : float
      Passed on as it is.
    """
    #  void QCanvasBoxGradient::setFeather(qreal feather)
    self.uglySide.call(
        'ritual_ZN18QCanvasBoxGradient10setFeatherEd', feather,
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxGradient::setRadius(qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxgradient.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasBoxGradient::setRadius(qreal radius)
    self.uglySide.call('ritual_ZN18QCanvasBoxGradient9setRadiusEd', radius)

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
    'QCanvasBoxGradient::QCanvasBoxGradient()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxgradient.html#QCanvasBoxGradient
    """
    #  QCanvasBoxGradient::QCanvasBoxGradient()
    self._noteCreation(QCanvasBoxGradient, lambda: Rituals.call(
        'ritual_ZN18QCanvasBoxGradientC1Ev',
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasBoxGradient::QCanvasBoxGradient(qreal x, qreal y, qreal width,
    qreal height)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxgradient.html#QCanvasBoxGradient

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  QCanvasBoxGradient::QCanvasBoxGradient(qreal x, qreal y, qreal width,
    #      qreal height)
    self._noteCreation(QCanvasBoxGradient, lambda: Rituals.call(
        'ritual_ZN18QCanvasBoxGradientC1Edddd', x, y, width, height,
    ))

  @overload(QRectF)
  def __init__(self, rect: QRectF) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasBoxGradient::QCanvasBoxGradient(const QRectF &rect)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxgradient.html#QCanvasBoxGradient

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QCanvasBoxGradient::QCanvasBoxGradient(const QRectF &rect)
    self._noteCreation(QCanvasBoxGradient, lambda: Rituals.call(
        'ritual_ZN18QCanvasBoxGradientC1ERK6QRectF', self._valueOf(rect),
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasBoxGradient) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasBoxGradient::QCanvasBoxGradient(const QCanvasBoxGradient &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxgradient.html#QCanvasBoxGradient

    Parameters
    ----------

    a0 : QCanvasBoxGradient
      Passed on as a value: Qt reads the C++ QCanvasBoxGradient, which stays
      Python's own.
    """
    #  QCanvasBoxGradient::QCanvasBoxGradient(const QCanvasBoxGradient &a0)
    self._noteCreation(QCanvasBoxGradient, lambda: Rituals.call(
        'ritual_ZN18QCanvasBoxGradientC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasBrush)
  def __init__(self, brush: QCanvasBrush) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasBoxGradient::QCanvasBoxGradient(const QCanvasBrush &brush)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxgradient.html#QCanvasBoxGradient

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  QCanvasBoxGradient::QCanvasBoxGradient(const QCanvasBrush &brush)
    self._noteCreation(QCanvasBoxGradient, lambda: Rituals.call(
        'ritual_ZN18QCanvasBoxGradientC1ERK12QCanvasBrush',
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
