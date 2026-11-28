"""
Qt3DInput::QKeyboardHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qkeyboardhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::QKeyboardHandlerPrivate to be private: it declares the
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


class QKeyboardHandlerPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DInput::QKeyboardHandlerPrivate: a plain Python
  object standing in front of one C++ Qt3DInput::QKeyboardHandlerPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DInput::QKeyboardHandlerPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QKeyboardHandlerPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::QKeyboardHandlerPrivate::~QKeyboardHandlerPrivate()':
    the destructor: Python never removes a C++
    Qt3DInput::QKeyboardHandlerPrivate.
  - Qt's 'const QKeyboardHandler
    *Qt3DInput::QKeyboardHandlerPrivate::q_func() const': takes in Python
    what 'QKeyboardHandler *Qt3DInput::QKeyboardHandlerPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DInput::QKeyboardHandlerPrivate is created at the first use,
    not by 'Qt3DInput::QKeyboardHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QKeyboardHandlerPrivate.
  - Each name of Qt's Qt3DInput::QKeyboardHandlerPrivate that has no cute
    function yet, 'keyEvent', holds a function that raises
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
  __qt_class__ = 'Qt3DInput::QKeyboardHandlerPrivate'

  #  A C++ Qt3DInput::QKeyboardHandlerPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QKeyboardHandlerPrivate'

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
    'Qt3DInput::QKeyboardHandlerPrivate::QKeyboardHandlerPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandlerprivate.html
    """
    #  Qt3DInput::QKeyboardHandlerPrivate::QKeyboardHandlerPrivate()
    self._noteCreation(QKeyboardHandlerPrivate, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput23QKeyboardHandlerPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DInput.QKeyboardHandler]:
    """
    Calls Qt's 'QKeyboardHandler
    *Qt3DInput::QKeyboardHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandlerprivate.html#q_func

    Returns
    -------

    Optional[Qt3DInput.QKeyboardHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyboardHandler *Qt3DInput::QKeyboardHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput23QKeyboardHandlerPrivate6q_funcEv',
    )
    return Qt3DInput.QKeyboardHandler._cuteAt(address)

  @staticmethod
  def keyEvent(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::QKeyboardHandlerPrivate::keyEvent(QKeyEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'keyToSignal'.
    """
    raise NotImplementedError(
        "'Qt3DInput.QKeyboardHandlerPrivate.keyEvent' has no cute function "
        "yet. Qt's 'void "
        "Qt3DInput::QKeyboardHandlerPrivate::keyEvent(QKeyEvent *event)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'keyToSignal'.")
