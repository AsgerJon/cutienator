"""
Qt3DInput::Input::AbstractActionInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/abstractactioninput_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::Input::AbstractActionInput to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractActionInput(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::AbstractActionInput: a plain Python
  object standing in front of one C++ Qt3DInput::Input::AbstractActionInput.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::Input::AbstractActionInput is built on Qt's
  Qt3DInput::Input::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::AbstractActionInput that has a
  ritual and that Python can call so far, 2 names in all: 'milliToNano',
  'process'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::AbstractActionInput is created at the first
    use, not by 'Qt3DInput::Input::AbstractActionInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::AbstractActionInput.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def milliToNano(milli: int) -> int:
    """
    Calls Qt's 'qint64
    Qt3DInput::Input::AbstractActionInput::milliToNano(qint64 milli)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractactioninput.html

    Parameters
    ----------

    milli : int
      Passed on as it is.
    """
    #  qint64 Qt3DInput::Input::AbstractActionInput::milliToNano(qint64
    #      milli)
    return Rituals.call(
        'ritual_ZN9Qt3DInput5Input19AbstractActionInput11milliToNanoEx',
        milli,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::AbstractActionInput'

  #  A C++ Qt3DInput::Input::AbstractActionInput Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_Input_AbstractActionInput'

  #  The functions Qt calls itself that Qt3DInput::Input::AbstractActionInput
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'process': (
          ('_ZN9Qt3DInput5Input19AbstractActionInput7processEPNS0_12InputHa'
           'ndlerEx',
           ('bool', 'number', ''),
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
    'Qt3DInput::Input::AbstractActionInput::AbstractActionInput()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractactioninput.html
    """
    #  Qt3DInput::Input::AbstractActionInput::AbstractActionInput()
    self._noteCreation(AbstractActionInput, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input19AbstractActionInputC1Ev',
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

  @overload(WAIT['Qt3DInput.Input.InputHandler'], int)
  @overload(NoneType, int)
  def process(
      self,
      inputHandler: Optional[Qt3DInput.Input.InputHandler],
      currentTime: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DInput::Input::AbstractActionInput::process(InputHandler
    *inputHandler, qint64 currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-abstractactioninput.html#process

    Parameters
    ----------

    inputHandler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentTime : int
      Passed on as it is.
    """
    #  bool Qt3DInput::Input::AbstractActionInput::process(InputHandler
    #      *inputHandler, qint64 currentTime)
    return self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input19AbstractActionInput7processEPNS0_12Inpu'
        'tHandlerEx',
        self._addressOf(inputHandler), currentTime,
    )
