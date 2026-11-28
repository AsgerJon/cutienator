"""
Qt3DInput::Input::KeyboardHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/keyboardhandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::KeyboardHandler to be private: it declares the
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


class KeyboardHandler(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::KeyboardHandler: a plain Python
  object standing in front of one C++ Qt3DInput::Input::KeyboardHandler.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::Input::KeyboardHandler is built on Qt's
  Qt3DInput::Input::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::KeyboardHandler that has a ritual
  and that Python can call so far, 7 names in all: 'keyboardDevice',
  'setInputHandler', 'setFocus', 'focus', 'syncFromFrontEnd', 'requestFocus',
  'setSourcerDevice'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::KeyboardHandler is created at the first use,
    not by 'Qt3DInput::Input::KeyboardHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::KeyboardHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::KeyboardHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def keyboardDevice(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DInput::Input::KeyboardHandler::keyboardDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DInput::Input::KeyboardHandler::keyboardDevice()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15KeyboardHandler14keyboardDeviceEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def focus(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::KeyboardHandler::focus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html#focus
    """
    #  bool Qt3DInput::Input::KeyboardHandler::focus() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input15KeyboardHandler5focusEv',
    )

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
    Qt3DInput::Input::KeyboardHandler::setInputHandler(InputHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html

    Parameters
    ----------

    handler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::KeyboardHandler::setInputHandler(InputHandler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15KeyboardHandler15setInputHandlerEPNS0_1'
        '2InputHandlerE',
        self._addressOf(handler),
    )

  @overload(bool)
  def setFocus(self, focus: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::KeyboardHandler::setFocus(bool
    focus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html#setFocus

    Parameters
    ----------

    focus : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::KeyboardHandler::setFocus(bool focus)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15KeyboardHandler8setFocusEb', focus,
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setSourcerDevice(self, device: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::KeyboardHandler::setSourcerDevice(Qt3DCore::QNodeId
    device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html

    Parameters
    ----------

    device : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DInput::Input::KeyboardHandler::setSourcerDevice(Qt3DCore::
    #      QNodeId device)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15KeyboardHandler16setSourcerDeviceEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(device),
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
    'Qt3DInput::Input::KeyboardHandler::KeyboardHandler()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html
    """
    #  Qt3DInput::Input::KeyboardHandler::KeyboardHandler()
    self._noteCreation(KeyboardHandler, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input15KeyboardHandlerC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::KeyboardHandler::syncFromFrontEnd(const Qt3DCore::QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::KeyboardHandler::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input15KeyboardHandler16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input15KeyboardHandler16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def requestFocus(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::KeyboardHandler::requestFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardhandler.html#requestFocus
    """
    #  void Qt3DInput::Input::KeyboardHandler::requestFocus()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input15KeyboardHandler12requestFocusEv',
    )
