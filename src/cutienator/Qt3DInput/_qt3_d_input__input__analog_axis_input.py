"""
Qt3DInput::Input::AnalogAxisInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/analogaxisinput_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::AnalogAxisInput to be private: it declares the
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


class AnalogAxisInput(Qt3DInput.Input.AbstractAxisInput):
  """
  The cute side of Qt's Qt3DInput::Input::AnalogAxisInput: a plain Python
  object standing in front of one C++ Qt3DInput::Input::AnalogAxisInput.

  It is built on the cute 'Qt3DInput::Input::AbstractAxisInput', as Qt's
  Qt3DInput::Input::AnalogAxisInput is built on Qt's
  Qt3DInput::Input::AbstractAxisInput, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::AnalogAxisInput that has a ritual
  and that Python can call so far, 4 names in all: 'cleanup', 'axis',
  'syncFromFrontEnd', 'process'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::AnalogAxisInput is created at the first use,
    not by 'Qt3DInput::Input::AnalogAxisInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::AnalogAxisInput.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::AnalogAxisInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def axis(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::Input::AnalogAxisInput::axis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-analogaxisinput.html#axis
    """
    #  int Qt3DInput::Input::AnalogAxisInput::axis() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15AnalogAxisInput4axisEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'Qt3DInput::Input::AnalogAxisInput::AnalogAxisInput()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-analogaxisinput.html
    """
    #  Qt3DInput::Input::AnalogAxisInput::AnalogAxisInput()
    self._noteCreation(AnalogAxisInput, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input15AnalogAxisInputC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::AnalogAxisInput::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-analogaxisinput.html#cleanup
    """
    #  void Qt3DInput::Input::AnalogAxisInput::cleanup()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15AnalogAxisInput7cleanupEv',
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
    Qt3DInput::Input::AnalogAxisInput::syncFromFrontEnd(const Qt3DCore::QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-analogaxisinput.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::AnalogAxisInput::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15AnalogAxisInput16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb',
        self._addressOf(frontEnd), firstTime,
    )

  @overload(WAIT['Qt3DInput.Input.InputHandler'], int)
  @overload(NoneType, int)
  def process(
      self,
      inputHandler: Optional[Qt3DInput.Input.InputHandler],
      currentTime: int,
  ) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::AnalogAxisInput::process(InputHandler
    *inputHandler, qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-analogaxisinput.html#process

    Parameters
    ----------

    inputHandler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentTime : int
      Passed on as it is.
    """
    #  float Qt3DInput::Input::AnalogAxisInput::process(InputHandler
    #      *inputHandler, qint64 currentTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input15AnalogAxisInput7processEPNS0_12InputHan'
        'dlerEx')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input15AnalogAxisInput7processEPNS0_12In'
          'putHandlerEx')
    return self.uglySide.call(
        ritual, self._addressOf(inputHandler), currentTime,
    )
