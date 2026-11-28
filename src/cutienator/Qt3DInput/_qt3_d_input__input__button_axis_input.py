"""
Qt3DInput::Input::ButtonAxisInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/buttonaxisinput_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::ButtonAxisInput to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ButtonAxisInput(Qt3DInput.Input.AbstractAxisInput):
  """
  The cute side of Qt's Qt3DInput::Input::ButtonAxisInput: a plain Python
  object standing in front of one C++ Qt3DInput::Input::ButtonAxisInput.

  It is built on the cute 'Qt3DInput::Input::AbstractAxisInput', as Qt's
  Qt3DInput::Input::ButtonAxisInput is built on Qt's
  Qt3DInput::Input::AbstractAxisInput, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::ButtonAxisInput that has a ritual
  and that Python can call so far, 9 names in all: 'cleanup', 'scale',
  'acceleration', 'deceleration', 'speedRatio', 'lastUpdateTime',
  'syncFromFrontEnd', 'process', 'updateSpeedRatio'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> Qt3DInput::Input::ButtonAxisInput::buttons() const':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::ButtonAxisInput is created at the first use,
    not by 'Qt3DInput::Input::ButtonAxisInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::ButtonAxisInput.
  - Each name of Qt's Qt3DInput::Input::ButtonAxisInput that has no cute
    function yet, 'buttons', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DInput::Input::ButtonAxisInput, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class UpdateType(CuteNum):
    """
    The enum 'Qt3DInput::Input::ButtonAxisInput::UpdateType' of Qt, with the
    2 names Qt gives in it.
    """

    Accelerate = Kee[int](0)
    Decelerate = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::ButtonAxisInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scale(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::ButtonAxisInput::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html#scale
    """
    #  float Qt3DInput::Input::ButtonAxisInput::scale() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15ButtonAxisInput5scaleEv',
    )

  def acceleration(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::ButtonAxisInput::acceleration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html#acceleration
    """
    #  float Qt3DInput::Input::ButtonAxisInput::acceleration() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15ButtonAxisInput12accelerationEv',
    )

  def deceleration(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::ButtonAxisInput::deceleration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html#deceleration
    """
    #  float Qt3DInput::Input::ButtonAxisInput::deceleration() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15ButtonAxisInput12decelerationEv',
    )

  def speedRatio(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::ButtonAxisInput::speedRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html#speedRatio
    """
    #  float Qt3DInput::Input::ButtonAxisInput::speedRatio() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15ButtonAxisInput10speedRatioEv',
    )

  def lastUpdateTime(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DInput::Input::ButtonAxisInput::lastUpdateTime()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html
    """
    #  qint64 Qt3DInput::Input::ButtonAxisInput::lastUpdateTime() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15ButtonAxisInput14lastUpdateTimeEv',
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
    'Qt3DInput::Input::ButtonAxisInput::ButtonAxisInput()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html
    """
    #  Qt3DInput::Input::ButtonAxisInput::ButtonAxisInput()
    self._noteCreation(ButtonAxisInput, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input15ButtonAxisInputC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::ButtonAxisInput::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html#cleanup
    """
    #  void Qt3DInput::Input::ButtonAxisInput::cleanup()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15ButtonAxisInput7cleanupEv',
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
    Qt3DInput::Input::ButtonAxisInput::syncFromFrontEnd(const Qt3DCore::QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::ButtonAxisInput::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15ButtonAxisInput16syncFromFrontEndEPKN8Q'
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
    Calls Qt's 'float Qt3DInput::Input::ButtonAxisInput::process(InputHandler
    *inputHandler, qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html#process

    Parameters
    ----------

    inputHandler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentTime : int
      Passed on as it is.
    """
    #  float Qt3DInput::Input::ButtonAxisInput::process(InputHandler
    #      *inputHandler, qint64 currentTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input15ButtonAxisInput7processEPNS0_12InputHan'
        'dlerEx')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input15ButtonAxisInput7processEPNS0_12In'
          'putHandlerEx')
    return self.uglySide.call(
        ritual, self._addressOf(inputHandler), currentTime,
    )

  @overload(int, UpdateType)
  def updateSpeedRatio(self, currentTime: int, type: UpdateType) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::ButtonAxisInput::updateSpeedRatio(qint64 currentTime,
    UpdateType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-buttonaxisinput.html

    Parameters
    ----------

    currentTime : int
      Passed on as it is.

    type : UpdateType
      Passed on as its number.
    """
    #  void Qt3DInput::Input::ButtonAxisInput::updateSpeedRatio(qint64
    #      currentTime, UpdateType type)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15ButtonAxisInput16updateSpeedRatioExNS1_'
        '10UpdateTypeE',
        currentTime, type.value,
    )

  @staticmethod
  def buttons(*__, **_) -> Never:
    """
    Qt's 'QList<int> Qt3DInput::Input::ButtonAxisInput::buttons() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.ButtonAxisInput.buttons' has no cute function "
        "yet. Qt's 'QList<int> Qt3DInput::Input::ButtonAxisInput::buttons() "
        "const': gives a type Python has no way to take yet.")
