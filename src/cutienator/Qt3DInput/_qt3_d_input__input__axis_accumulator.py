"""
Qt3DInput::Input::AxisAccumulator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/axisaccumulator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::AxisAccumulator to be private: it declares the
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AxisAccumulator(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::AxisAccumulator: a plain Python
  object standing in front of one C++ Qt3DInput::Input::AxisAccumulator.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::Input::AxisAccumulator is built on Qt's
  Qt3DInput::Input::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::AxisAccumulator that has a ritual
  and that Python can call so far, 10 names in all: 'cleanup',
  'sourceAxisId', 'sourceAxisType', 'scale', 'value', 'setValue', 'velocity',
  'setVelocity', 'syncFromFrontEnd', 'stepIntegration'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::AxisAccumulator is created at the first use,
    not by 'Qt3DInput::Input::AxisAccumulator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::AxisAccumulator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::AxisAccumulator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sourceAxisId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DInput::Input::AxisAccumulator::sourceAxisId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html#sourceAxisId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DInput::Input::AxisAccumulator::sourceAxisId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15AxisAccumulator12sourceAxisIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def sourceAxisType(self) -> Qt3DInput.QAxisAccumulator.SourceAxisType:
    """
    Calls Qt's 'QAxisAccumulator::SourceAxisType
    Qt3DInput::Input::AxisAccumulator::sourceAxisType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html

    Returns
    -------

    Qt3DInput.QAxisAccumulator.SourceAxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DInput.QAxisAccumulator.SourceAxisType(number)' gives.
    """
    #  QAxisAccumulator::SourceAxisType
    #      Qt3DInput::Input::AxisAccumulator::sourceAxisType() const
    return Qt3DInput.QAxisAccumulator.SourceAxisType(self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15AxisAccumulator14sourceAxisTypeEv',
    ))

  def scale(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::AxisAccumulator::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html#scale
    """
    #  float Qt3DInput::Input::AxisAccumulator::scale() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15AxisAccumulator5scaleEv',
    )

  def value(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::AxisAccumulator::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html#value
    """
    #  float Qt3DInput::Input::AxisAccumulator::value() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15AxisAccumulator5valueEv',
    )

  def velocity(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::AxisAccumulator::velocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html#velocity
    """
    #  float Qt3DInput::Input::AxisAccumulator::velocity() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15AxisAccumulator8velocityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::AxisAccumulator::setValue(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::Input::AxisAccumulator::setValue(float value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15AxisAccumulator8setValueEf', value,
    )

  @overload(float)
  def setVelocity(self, velocity: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::AxisAccumulator::setVelocity(float
    velocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html#setVelocity

    Parameters
    ----------

    velocity : float
      Passed on as it is.
    """
    #  void Qt3DInput::Input::AxisAccumulator::setVelocity(float velocity)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15AxisAccumulator11setVelocityEf',
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
    'Qt3DInput::Input::AxisAccumulator::AxisAccumulator()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html
    """
    #  Qt3DInput::Input::AxisAccumulator::AxisAccumulator()
    self._noteCreation(AxisAccumulator, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input15AxisAccumulatorC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::AxisAccumulator::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html#cleanup
    """
    #  void Qt3DInput::Input::AxisAccumulator::cleanup()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15AxisAccumulator7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::AxisAccumulator::syncFromFrontEnd(const Qt3DCore::QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::AxisAccumulator::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input15AxisAccumulator16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input15AxisAccumulator16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DInput.Input.AxisManager'], float)
  @overload(NoneType, float)
  def stepIntegration(
      self,
      axisManager: Optional[Qt3DInput.Input.AxisManager],
      dt: float,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::AxisAccumulator::stepIntegration(AxisManager
    *axisManager, float dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axisaccumulator.html

    Parameters
    ----------

    axisManager : Optional[Qt3DInput.Input.AxisManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  void Qt3DInput::Input::AxisAccumulator::stepIntegration(AxisManager
    #      *axisManager, float dt)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15AxisAccumulator15stepIntegrationEPNS0_1'
        '1AxisManagerEf',
        self._addressOf(axisManager), dt,
    )
