"""
Qt3DInput::Input::AbstractAxisInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/abstractaxisinput_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::Input::AbstractAxisInput to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
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


class AbstractAxisInput(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::AbstractAxisInput: a plain Python
  object standing in front of one C++ Qt3DInput::Input::AbstractAxisInput.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::Input::AbstractAxisInput is built on Qt's
  Qt3DInput::Input::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::AbstractAxisInput that has a
  ritual and that Python can call so far, 4 names in all: 'cleanup',
  'sourceDevice', 'syncFromFrontEnd', 'process'. It can be made from Python,
  in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::AbstractAxisInput is created at the first use,
    not by 'Qt3DInput::Input::AbstractAxisInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::AbstractAxisInput.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::AbstractAxisInput'

  #  A C++ Qt3DInput::Input::AbstractAxisInput Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_Input_AbstractAxisInput'

  #  The functions Qt calls itself that Qt3DInput::Input::AbstractAxisInput
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'cleanup': (
          ('_ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'process': (
          ('_ZN9Qt3DInput5Input17AbstractAxisInput7processEPNS0_12InputHand'
           'lerEx',
           ('float', 'number', ''),
           (
               ('address', 'address',
                'Qt3DInput:Qt3DInput.Input.InputHandler'),
               ('long long', 'number', ''),
           )),
      ),
  }

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
    Qt3DInput::Input::AbstractAxisInput::sourceDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractaxisinput.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DInput::Input::AbstractAxisInput::sourceDevice()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input17AbstractAxisInput12sourceDeviceEv',
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
    'Qt3DInput::Input::AbstractAxisInput::AbstractAxisInput()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractaxisinput.html
    """
    #  Qt3DInput::Input::AbstractAxisInput::AbstractAxisInput()
    self._noteCreation(AbstractAxisInput, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input17AbstractAxisInputC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::AbstractAxisInput::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractaxisinput.html#cleanup
    """
    #  void Qt3DInput::Input::AbstractAxisInput::cleanup()
    ritual = 'ritual_ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv'
    self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::AbstractAxisInput::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractaxisinput.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::AbstractAxisInput::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input17AbstractAxisInput16syncFromFrontEndEPKN'
        '8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input17AbstractAxisInput16syncFromFrontE'
          'ndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DInput.Input.InputHandler'], int)
  @overload(NoneType, int)
  def process(
      self,
      inputHandler: Optional[Qt3DInput.Input.InputHandler],
      currentTime: int,
  ) -> float:
    """
    Calls Qt's 'float
    Qt3DInput::Input::AbstractAxisInput::process(InputHandler *inputHandler,
    qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractaxisinput.html#process

    Parameters
    ----------

    inputHandler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentTime : int
      Passed on as it is.
    """
    #  float Qt3DInput::Input::AbstractAxisInput::process(InputHandler
    #      *inputHandler, qint64 currentTime)
    return self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input17AbstractAxisInput7processEPNS0_12InputH'
        'andlerEx',
        self._addressOf(inputHandler), currentTime,
    )
