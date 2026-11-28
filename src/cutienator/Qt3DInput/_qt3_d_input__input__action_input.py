"""
Qt3DInput::Input::ActionInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/actioninput_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::ActionInput to be private: it declares the
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


class ActionInput(Qt3DInput.Input.AbstractActionInput):
  """
  The cute side of Qt's Qt3DInput::Input::ActionInput: a plain Python object
  standing in front of one C++ Qt3DInput::Input::ActionInput.

  It is built on the cute 'Qt3DInput::Input::AbstractActionInput', as Qt's
  Qt3DInput::Input::ActionInput is built on Qt's
  Qt3DInput::Input::AbstractActionInput, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::ActionInput that has a ritual and
  that Python can call so far, 4 names in all: 'cleanup', 'sourceDevice',
  'syncFromFrontEnd', 'process'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> Qt3DInput::Input::ActionInput::buttons() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::ActionInput is created at the first use, not by
    'Qt3DInput::Input::ActionInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::ActionInput.
  - Each name of Qt's Qt3DInput::Input::ActionInput that has no cute function
    yet, 'buttons', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'Qt3DInput::Input::ActionInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sourceDevice(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DInput::Input::ActionInput::sourceDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-actioninput.html#sourceDevice

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DInput::Input::ActionInput::sourceDevice() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11ActionInput12sourceDeviceEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

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
    'Qt3DInput::Input::ActionInput::ActionInput()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-actioninput.html#ActionInput
    """
    #  Qt3DInput::Input::ActionInput::ActionInput()
    self._noteCreation(ActionInput, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input11ActionInputC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::ActionInput::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-actioninput.html#cleanup
    """
    #  void Qt3DInput::Input::ActionInput::cleanup()
    self.uglySide.call('ritual_ZN9Qt3DInput5Input11ActionInput7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::ActionInput::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-actioninput.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::ActionInput::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input11ActionInput16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input11ActionInput16syncFromFrontEndEPKN'
          '8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DInput.Input.InputHandler'], int)
  @overload(NoneType, int)
  def process(
      self,
      inputHandler: Optional[Qt3DInput.Input.InputHandler],
      currentTime: int,
  ) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::ActionInput::process(InputHandler
    *inputHandler, qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-actioninput.html#process

    Parameters
    ----------

    inputHandler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentTime : int
      Passed on as it is.
    """
    #  bool Qt3DInput::Input::ActionInput::process(InputHandler
    #      *inputHandler, qint64 currentTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input11ActionInput7processEPNS0_12InputHandler'
        'Ex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input11ActionInput7processEPNS0_12InputH'
          'andlerEx')
    return self.uglySide.call(
        ritual, self._addressOf(inputHandler), currentTime,
    )

  @staticmethod
  def buttons(*__, **_) -> Never:
    """
    Qt's 'QList<int> Qt3DInput::Input::ActionInput::buttons() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.ActionInput.buttons' has no cute function yet. "
        "Qt's 'QList<int> Qt3DInput::Input::ActionInput::buttons() const': "
        "gives a type Python has no way to take yet.")
