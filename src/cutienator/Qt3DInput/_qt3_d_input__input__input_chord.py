"""
Qt3DInput::Input::InputChord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/inputchord_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DInput::Input::InputChord to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InputChord(Qt3DInput.Input.AbstractActionInput):
  """
  The cute side of Qt's Qt3DInput::Input::InputChord: a plain Python object
  standing in front of one C++ Qt3DInput::Input::InputChord.

  It is built on the cute 'Qt3DInput::Input::AbstractActionInput', as Qt's
  Qt3DInput::Input::InputChord is built on Qt's
  Qt3DInput::Input::AbstractActionInput, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::InputChord that has a ritual and
  that Python can call so far, 8 names in all: 'cleanup', 'timeout',
  'startTime', 'setStartTime', 'reset', 'actionTriggered',
  'syncFromFrontEnd', 'process'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Qt3DCore::QNodeId> Qt3DInput::Input::InputChord::chords()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::InputChord is created at the first use, not by
    'Qt3DInput::Input::InputChord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::InputChord.
  - Each name of Qt's Qt3DInput::Input::InputChord that has no cute function
    yet, 'chords', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::InputChord'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def timeout(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DInput::Input::InputChord::timeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#timeout
    """
    #  qint64 Qt3DInput::Input::InputChord::timeout() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input10InputChord7timeoutEv',
    )

  def startTime(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DInput::Input::InputChord::startTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#startTime
    """
    #  qint64 Qt3DInput::Input::InputChord::startTime() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input10InputChord9startTimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStartTime(self, time: int) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::InputChord::setStartTime(qint64
    time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#setStartTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void Qt3DInput::Input::InputChord::setStartTime(qint64 time)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input10InputChord12setStartTimeEx', time,
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
    'Qt3DInput::Input::InputChord::InputChord()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#InputChord
    """
    #  Qt3DInput::Input::InputChord::InputChord()
    self._noteCreation(InputChord, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input10InputChordC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::InputChord::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#cleanup
    """
    #  void Qt3DInput::Input::InputChord::cleanup()
    self.uglySide.call('ritual_ZN9Qt3DInput5Input10InputChord7cleanupEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::InputChord::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#reset
    """
    #  void Qt3DInput::Input::InputChord::reset()
    self.uglySide.call('ritual_ZN9Qt3DInput5Input10InputChord5resetEv')

  @overload(WAIT['Qt3DCore.QNodeId'])
  def actionTriggered(self, input: Qt3DCore.QNodeId) -> bool:
    """
    Calls Qt's 'bool
    Qt3DInput::Input::InputChord::actionTriggered(Qt3DCore::QNodeId input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#actionTriggered

    Parameters
    ----------

    input : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DInput::Input::InputChord::actionTriggered(Qt3DCore::QNodeId
    #      input)
    return self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input10InputChord15actionTriggeredEN8Qt3DCore7'
        'QNodeIdE',
        self._valueOf(input),
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::InputChord::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::InputChord::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input10InputChord16syncFromFrontEndEPKN8Qt3DCo'
        're5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input10InputChord16syncFromFrontEndEPKN8'
          'Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DInput.Input.InputHandler'], int)
  @overload(NoneType, int)
  def process(
      self,
      inputHandler: Optional[Qt3DInput.Input.InputHandler],
      currentTime: int,
  ) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::InputChord::process(InputHandler
    *inputHandler, qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputchord.html#process

    Parameters
    ----------

    inputHandler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentTime : int
      Passed on as it is.
    """
    #  bool Qt3DInput::Input::InputChord::process(InputHandler *inputHandler,
    #      qint64 currentTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input10InputChord7processEPNS0_12InputHandlerE'
        'x')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input10InputChord7processEPNS0_12InputHa'
          'ndlerEx')
    return self.uglySide.call(
        ritual, self._addressOf(inputHandler), currentTime,
    )

  @staticmethod
  def chords(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId> Qt3DInput::Input::InputChord::chords()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputChord.chords' has no cute function yet. Qt's "
        "'QList<Qt3DCore::QNodeId> Qt3DInput::Input::InputChord::chords() "
        "const': gives a type Python has no way to take yet.")
