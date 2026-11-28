"""
Qt3DInput::QAxisAccumulatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qaxisaccumulator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::QAxisAccumulatorPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QAxisAccumulatorPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DInput::QAxisAccumulatorPrivate: a plain Python
  object standing in front of one C++ Qt3DInput::QAxisAccumulatorPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DInput::QAxisAccumulatorPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAxisAccumulatorPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'q_func', 'setValue',
  'setVelocity'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAxisAccumulator
    *Qt3DInput::QAxisAccumulatorPrivate::q_func() const': takes in Python
    what 'QAxisAccumulator *Qt3DInput::QAxisAccumulatorPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DInput::QAxisAccumulatorPrivate is created at the first use,
    not by 'Qt3DInput::QAxisAccumulatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAxisAccumulatorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAxisAccumulatorPrivate'

  #  A C++ Qt3DInput::QAxisAccumulatorPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAxisAccumulatorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisAccumulatorPrivate::setValue(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulatorprivate.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisAccumulatorPrivate::setValue(float value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput23QAxisAccumulatorPrivate8setValueEf', value,
    )

  @overload(float)
  def setVelocity(self, velocity: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisAccumulatorPrivate::setVelocity(float
    velocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulatorprivate.html#setVelocity

    Parameters
    ----------

    velocity : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisAccumulatorPrivate::setVelocity(float velocity)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput23QAxisAccumulatorPrivate11setVelocityEf',
        velocity,
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
    'Qt3DInput::QAxisAccumulatorPrivate::QAxisAccumulatorPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulatorprivate.html
    """
    #  Qt3DInput::QAxisAccumulatorPrivate::QAxisAccumulatorPrivate()
    self._noteCreation(QAxisAccumulatorPrivate, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput23QAxisAccumulatorPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DInput.QAxisAccumulator]:
    """
    Calls Qt's 'QAxisAccumulator
    *Qt3DInput::QAxisAccumulatorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxisaccumulatorprivate.html#q_func

    Returns
    -------

    Optional[Qt3DInput.QAxisAccumulator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAxisAccumulator *Qt3DInput::QAxisAccumulatorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput23QAxisAccumulatorPrivate6q_funcEv',
    )
    return Qt3DInput.QAxisAccumulator._cuteAt(address)
