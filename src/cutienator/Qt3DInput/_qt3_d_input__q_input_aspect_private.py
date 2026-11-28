"""
Qt3DInput::QInputAspectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qinputaspect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::QInputAspectPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QInputAspectPrivate(Qt3DCore.QAbstractAspectPrivate):
  """
  The cute side of Qt's Qt3DInput::QInputAspectPrivate: a plain Python object
  standing in front of one C++ Qt3DInput::QInputAspectPrivate.

  It is built on the cute 'Qt3DCore::QAbstractAspectPrivate', as Qt's
  Qt3DInput::QInputAspectPrivate is built on Qt's
  Qt3DCore::QAbstractAspectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QInputAspectPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QInputAspect *Qt3DInput::QInputAspectPrivate::q_func()
    const': takes in Python what 'QInputAspect
    *Qt3DInput::QInputAspectPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 leans on 'Qt3DInput.

  What to expect
  --------------

  - The C++ Qt3DInput::QInputAspectPrivate is created at the first use, not
    by 'Qt3DInput::QInputAspectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QInputAspectPrivate.
  - Each name of Qt's Qt3DInput::QInputAspectPrivate that has no cute
    function yet, '__init__', 'loadInputDevicePlugins', holds a function that
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
  __qt_class__ = 'Qt3DInput::QInputAspectPrivate'

  #  A C++ Qt3DInput::QInputAspectPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QInputAspectPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DInput::QInputAspectPrivate::QInputAspectPrivate()': leans on
    'Qt3DInput::Input::InputHandler::InputHandler()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DInput.QInputAspectPrivate.__init__' has no cute function yet. "
        "Qt's 'Qt3DInput::QInputAspectPrivate::QInputAspectPrivate()': "
        "leans on 'Qt3DInput::Input::InputHandler::InputHandler()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def q_func(self) -> Optional[Qt3DInput.QInputAspect]:
    """
    Calls Qt's 'QInputAspect *Qt3DInput::QInputAspectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspectprivate.html#q_func

    Returns
    -------

    Optional[Qt3DInput.QInputAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputAspect *Qt3DInput::QInputAspectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput19QInputAspectPrivate6q_funcEv',
    )
    return Qt3DInput.QInputAspect._cuteAt(address)

  @staticmethod
  def loadInputDevicePlugins(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::QInputAspectPrivate::loadInputDevicePlugins()':
    leans on 'Qt3DInput::QInputDeviceIntegrationFactory::keys()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Qt3DInput.QInputAspectPrivate.loadInputDevicePlugins' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::QInputAspectPrivate::loadInputDevicePlugins()': leans "
        "on 'Qt3DInput::QInputDeviceIntegrationFactory::keys()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
