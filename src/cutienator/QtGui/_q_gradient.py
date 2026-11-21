"""
QGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QGradientCoordinateMode, QGradientInterpolationMode
from . import QGradientPreset, QGradientSpread, QGradientType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QGradient(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGradient: a plain Python object standing in front of
  one C++ QGradient.

  C++ hands a QGradient around as a copy, so every C++ QGradient behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGradient that has a ritual and that Python can call
  so far, 8 names in all: 'type', 'setSpread', 'spread', 'setColorAt',
  'coordinateMode', 'setCoordinateMode', 'interpolationMode',
  'setInterpolationMode'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGradient::~QGradient()': the destructor: Python removes its C++
    QGradient by it, and has no other use for it.
  - Qt's 'bool QGradient::operator==(const QGradient &gradient) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QGradient::operator!=(const QGradient &other) const': an
    operator, which is not reflected yet.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QGradient is created at the first use, not by 'QGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGradient back gives a copy the ritual made for
    Python, in a new cute QGradient.
  """

  #  The enums Qt writes inside QGradient, and the names Qt has for the
  #  combinations of its flags enums.
  CoordinateMode = QGradientCoordinateMode
  InterpolationMode = QGradientInterpolationMode
  Preset = QGradientPreset
  Spread = QGradientSpread
  Type = QGradientType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGradient'

  #  Qt's '~QGradient()'. Naming it makes this a value class: Python owns
  #  every C++ QGradient behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QGradient::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QGradient::type() const
    return QGradient.Type(self.uglySide.call('ritual_ZNK9QGradient4typeEv'))

  def spread(self) -> Spread:
    """
    Calls Qt's 'Spread QGradient::spread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#spread

    Returns
    -------

    Spread
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Spread(number)' gives.
    """
    #  Spread QGradient::spread() const
    return QGradient.Spread(self.uglySide.call(
        'ritual_ZNK9QGradient6spreadEv',
    ))

  def coordinateMode(self) -> CoordinateMode:
    """
    Calls Qt's 'CoordinateMode QGradient::coordinateMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#coordinateMode

    Returns
    -------

    CoordinateMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CoordinateMode(number)'
      gives.
    """
    #  CoordinateMode QGradient::coordinateMode() const
    return QGradient.CoordinateMode(self.uglySide.call(
        'ritual_ZNK9QGradient14coordinateModeEv',
    ))

  def interpolationMode(self) -> InterpolationMode:
    """
    Calls Qt's 'InterpolationMode QGradient::interpolationMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#interpolationMode

    Returns
    -------

    InterpolationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'InterpolationMode(number)' gives.
    """
    #  InterpolationMode QGradient::interpolationMode() const
    return QGradient.InterpolationMode(self.uglySide.call(
        'ritual_ZNK9QGradient17interpolationModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Spread)
  def setSpread(self, spread: Spread) -> None:
    """
    Calls Qt's 'void QGradient::setSpread(Spread spread)'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#setSpread

    Parameters
    ----------

    spread : Spread
      Passed on as its number.
    """
    #  void QGradient::setSpread(Spread spread)
    self.uglySide.call(
        'ritual_ZN9QGradient9setSpreadENS_6SpreadE', spread.value,
    )

  @overload(float, QColor)
  def setColorAt(self, pos: float, color: QColor) -> None:
    """
    Calls Qt's 'void QGradient::setColorAt(qreal pos, const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#setColorAt

    Parameters
    ----------

    pos : float
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGradient::setColorAt(qreal pos, const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QGradient10setColorAtEdRK6QColor',
        pos, self._valueOf(color),
    )

  @overload(CoordinateMode)
  def setCoordinateMode(self, mode: CoordinateMode) -> None:
    """
    Calls Qt's 'void QGradient::setCoordinateMode(CoordinateMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#setCoordinateMode

    Parameters
    ----------

    mode : CoordinateMode
      Passed on as its number.
    """
    #  void QGradient::setCoordinateMode(CoordinateMode mode)
    self.uglySide.call(
        'ritual_ZN9QGradient17setCoordinateModeENS_14CoordinateModeE',
        mode.value,
    )

  @overload(InterpolationMode)
  def setInterpolationMode(self, mode: InterpolationMode) -> None:
    """
    Calls Qt's 'void QGradient::setInterpolationMode(InterpolationMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgradient.html#setInterpolationMode

    Parameters
    ----------

    mode : InterpolationMode
      Passed on as its number.
    """
    #  void QGradient::setInterpolationMode(InterpolationMode mode)
    self.uglySide.call(
        'ritual_ZN9QGradient20setInterpolationModeENS_17InterpolationModeE',
        mode.value,
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
    Notes what was given, for Qt's 'QGradient::QGradient()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#QGradient
    """
    #  QGradient::QGradient()
    self._noteCreation(QGradient, lambda: Rituals.call(
        'ritual_ZN9QGradientC1Ev',
    ))

  @overload(Preset)
  def __init__(self, a0: Preset) -> None:
    """
    Notes what was given, for Qt's 'QGradient::QGradient(Preset a0)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#QGradient

    Parameters
    ----------

    a0 : Preset
      Passed on as its number.
    """
    #  QGradient::QGradient(Preset a0)
    self._noteCreation(QGradient, lambda: Rituals.call(
        'ritual_ZN9QGradientC1ENS_6PresetE', a0.value,
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
