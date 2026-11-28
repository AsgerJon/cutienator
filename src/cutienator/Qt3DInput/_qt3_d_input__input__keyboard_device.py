"""
Qt3DInput::Input::KeyboardDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/keyboarddevice_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::KeyboardDevice to be private: it declares the
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


class KeyboardDevice(Qt3DInput.QAbstractPhysicalDeviceBackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::KeyboardDevice: a plain Python
  object standing in front of one C++ Qt3DInput::Input::KeyboardDevice.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDeviceBackendNode', as
  Qt's Qt3DInput::Input::KeyboardDevice is built on Qt's
  Qt3DInput::QAbstractPhysicalDeviceBackendNode, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::KeyboardDevice that has a ritual
  and that Python can call so far, 9 names in all: 'cleanup',
  'requestFocusForInput', 'setInputHandler', 'setCurrentFocusItem',
  'axisValue', 'isButtonPressed', 'currentFocusItem',
  'lastKeyboardInputRequester', 'setButtonValue'. It can be made from Python,
  in 1 way; see '__init__'.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::KeyboardDevice is created at the first use, not
    by 'Qt3DInput::Input::KeyboardDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::KeyboardDevice.
  - Each name of Qt's Qt3DInput::Input::KeyboardDevice that has no cute
    function yet, 'updateKeyEvent', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::KeyboardDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def axisValue(self, axisIdentifier: int) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::KeyboardDevice::axisValue(int
    axisIdentifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html#axisValue

    Parameters
    ----------

    axisIdentifier : int
      Passed on as it is.
    """
    #  float Qt3DInput::Input::KeyboardDevice::axisValue(int axisIdentifier)
    #      const
    ritual = 'ritual_ZNK9Qt3DInput5Input14KeyboardDevice9axisValueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9Qt3DInput5Input14KeyboardDevice9axisValueEi'
    return self.uglySide.call(ritual, axisIdentifier)

  @overload(int)
  def isButtonPressed(self, buttonIdentifier: int) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::KeyboardDevice::isButtonPressed(int
    buttonIdentifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html

    Parameters
    ----------

    buttonIdentifier : int
      Passed on as it is.
    """
    #  bool Qt3DInput::Input::KeyboardDevice::isButtonPressed(int
    #      buttonIdentifier) const
    ritual = 'ritual_ZNK9Qt3DInput5Input14KeyboardDevice15isButtonPressedEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput5Input14KeyboardDevice15isButtonPressedE'
          'i')
    return self.uglySide.call(ritual, buttonIdentifier)

  def currentFocusItem(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DInput::Input::KeyboardDevice::currentFocusItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DInput::Input::KeyboardDevice::currentFocusItem()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input14KeyboardDevice16currentFocusItemEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def lastKeyboardInputRequester(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DInput::Input::KeyboardDevice::lastKeyboardInputRequester() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DInput::Input::KeyboardDevice::lastKeyboardInputRequester()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input14KeyboardDevice26lastKeyboardInputReque'
        'sterEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.Input.InputHandler'])
  @overload(NoneType)
  def setInputHandler(
      self,
      handler: Optional[Qt3DInput.Input.InputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::KeyboardDevice::setInputHandler(InputHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html

    Parameters
    ----------

    handler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::KeyboardDevice::setInputHandler(InputHandler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input14KeyboardDevice15setInputHandlerEPNS0_12'
        'InputHandlerE',
        self._addressOf(handler),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setCurrentFocusItem(self, input: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::KeyboardDevice::setCurrentFocusItem(Qt3DCore::QNodeId
    input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html

    Parameters
    ----------

    input : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DInput::Input::KeyboardDevice::setCurrentFocusItem(Qt3DCore::
    #      QNodeId input)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input14KeyboardDevice19setCurrentFocusItemEN8Q'
        't3DCore7QNodeIdE',
        self._valueOf(input),
    )

  @overload(int, bool)
  def setButtonValue(self, key: int, value: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::KeyboardDevice::setButtonValue(int
    key, bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html#setButtonValue

    Parameters
    ----------

    key : int
      Passed on as it is.

    value : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::KeyboardDevice::setButtonValue(int key, bool
    #      value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input14KeyboardDevice14setButtonValueEib',
        key, value,
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
    'Qt3DInput::Input::KeyboardDevice::KeyboardDevice()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html#KeyboardDevice
    """
    #  Qt3DInput::Input::KeyboardDevice::KeyboardDevice()
    self._noteCreation(KeyboardDevice, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input14KeyboardDeviceC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::KeyboardDevice::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html#cleanup
    """
    #  void Qt3DInput::Input::KeyboardDevice::cleanup()
    ritual = 'ritual_ZN9Qt3DInput5Input14KeyboardDevice7cleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DInput5Input14KeyboardDevice7cleanupEv'
    self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def requestFocusForInput(self, inputId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::KeyboardDevice::requestFocusForInput(Qt3DCore::QNodeId
    inputId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboarddevice.html

    Parameters
    ----------

    inputId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DInput::Input::KeyboardDevice::requestFocusForInput(Qt3DCore::
    #      QNodeId inputId)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input14KeyboardDevice20requestFocusForInputEN8'
        'Qt3DCore7QNodeIdE',
        self._valueOf(inputId),
    )

  @staticmethod
  def updateKeyEvent(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::KeyboardDevice::updateKeyEvent(::QKeyEvent
    *event)': the compiler refuses its ritual as it would be written here:
    cannot initialize a parameter of type '::QKeyEvent *' with an lvalue of
    type '::Qt3DInput::QKeyEvent *'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.KeyboardDevice.updateKeyEvent' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::KeyboardDevice::updateKeyEvent(::QKeyEvent "
        "*event)': the compiler refuses its ritual as it would be written "
        "here: cannot initialize a parameter of type '::QKeyEvent *' with "
        "an lvalue of type '::Qt3DInput::QKeyEvent *'.")
