"""
Qt3DInput::Input::InputSequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/inputsequence_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::InputSequence to be private: it declares the
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
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InputSequence(Qt3DInput.Input.AbstractActionInput):
  """
  The cute side of Qt's Qt3DInput::Input::InputSequence: a plain Python
  object standing in front of one C++ Qt3DInput::Input::InputSequence.

  It is built on the cute 'Qt3DInput::Input::AbstractActionInput', as Qt's
  Qt3DInput::Input::InputSequence is built on Qt's
  Qt3DInput::Input::AbstractActionInput, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::InputSequence that has a ritual
  and that Python can call so far, 9 names in all: 'cleanup', 'timeout',
  'buttonInterval', 'startTime', 'setStartTime', 'reset', 'actionTriggered',
  'syncFromFrontEnd', 'process'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::Input::InputSequence::sequences() const': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::InputSequence is created at the first use, not
    by 'Qt3DInput::Input::InputSequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::InputSequence.
  - Each name of Qt's Qt3DInput::Input::InputSequence that has no cute
    function yet, 'sequenceTriggered', 'sequences', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::InputSequence'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def timeout(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DInput::Input::InputSequence::timeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#timeout
    """
    #  qint64 Qt3DInput::Input::InputSequence::timeout() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input13InputSequence7timeoutEv',
    )

  def buttonInterval(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DInput::Input::InputSequence::buttonInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#buttonInterval
    """
    #  qint64 Qt3DInput::Input::InputSequence::buttonInterval() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input13InputSequence14buttonIntervalEv',
    )

  def startTime(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DInput::Input::InputSequence::startTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#startTime
    """
    #  qint64 Qt3DInput::Input::InputSequence::startTime() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input13InputSequence9startTimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStartTime(self, time: int) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::InputSequence::setStartTime(qint64
    time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#setStartTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void Qt3DInput::Input::InputSequence::setStartTime(qint64 time)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input13InputSequence12setStartTimeEx', time,
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
    'Qt3DInput::Input::InputSequence::InputSequence()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#InputSequence
    """
    #  Qt3DInput::Input::InputSequence::InputSequence()
    self._noteCreation(InputSequence, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input13InputSequenceC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::InputSequence::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#cleanup
    """
    #  void Qt3DInput::Input::InputSequence::cleanup()
    self.uglySide.call('ritual_ZN9Qt3DInput5Input13InputSequence7cleanupEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::InputSequence::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#reset
    """
    #  void Qt3DInput::Input::InputSequence::reset()
    self.uglySide.call('ritual_ZN9Qt3DInput5Input13InputSequence5resetEv')

  @overload(WAIT['Qt3DCore.QNodeId'], int)
  def actionTriggered(
      self,
      input: Qt3DCore.QNodeId,
      currentTime: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DInput::Input::InputSequence::actionTriggered(Qt3DCore::QNodeId input,
    const qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#actionTriggered

    Parameters
    ----------

    input : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    currentTime : int
      Passed on as it is.
    """
    #  bool
    #      Qt3DInput::Input::InputSequence::actionTriggered(Qt3DCore::QNodeId
    #      input, const qint64 currentTime)
    return self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input13InputSequence15actionTriggeredEN8Qt3DCo'
        're7QNodeIdEx',
        self._valueOf(input), currentTime,
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::InputSequence::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::InputSequence::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input13InputSequence16syncFromFrontEndEPKN8Qt3'
        'DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input13InputSequence16syncFromFrontEndEP'
          'KN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DInput.Input.InputHandler'], int)
  @overload(NoneType, int)
  def process(
      self,
      inputHandler: Optional[Qt3DInput.Input.InputHandler],
      currentTime: int,
  ) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::InputSequence::process(InputHandler
    *inputHandler, qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputsequence.html#process

    Parameters
    ----------

    inputHandler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentTime : int
      Passed on as it is.
    """
    #  bool Qt3DInput::Input::InputSequence::process(InputHandler
    #      *inputHandler, qint64 currentTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input13InputSequence7processEPNS0_12InputHandl'
        'erEx')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input13InputSequence7processEPNS0_12Inpu'
          'tHandlerEx')
    return self.uglySide.call(
        ritual, self._addressOf(inputHandler), currentTime,
    )

  @staticmethod
  def sequenceTriggered(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DInput::Input::InputSequence::sequenceTriggered() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputSequence.sequenceTriggered' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DInput::Input::InputSequence::sequenceTriggered() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def sequences(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::Input::InputSequence::sequences() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputSequence.sequences' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DInput::Input::InputSequence::sequences() const': gives a type "
        "Python has no way to take yet.")
