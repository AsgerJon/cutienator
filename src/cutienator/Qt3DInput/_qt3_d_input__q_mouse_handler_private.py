"""
Qt3DInput::QMouseHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qmousehandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::QMouseHandlerPrivate to be private: it declares the
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


class QMouseHandlerPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DInput::QMouseHandlerPrivate: a plain Python
  object standing in front of one C++ Qt3DInput::QMouseHandlerPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DInput::QMouseHandlerPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QMouseHandlerPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'init', 'q_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::QMouseHandlerPrivate::~QMouseHandlerPrivate()': the
    destructor: Python never removes a C++ Qt3DInput::QMouseHandlerPrivate.
  - Qt's 'void Qt3DInput::QMouseHandlerPrivate::mouseEvent(const
    QMouseEventPtr &event)': takes a type Python has no way to hand over yet.
  - Qt's 'const QMouseHandler *Qt3DInput::QMouseHandlerPrivate::q_func()
    const': takes in Python what 'QMouseHandler
    *Qt3DInput::QMouseHandlerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DInput::QMouseHandlerPrivate is created at the first use, not
    by 'Qt3DInput::QMouseHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QMouseHandlerPrivate.
  - Each name of Qt's Qt3DInput::QMouseHandlerPrivate that has no cute
    function yet, 'mouseEvent', holds a function that raises
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
  __qt_class__ = 'Qt3DInput::QMouseHandlerPrivate'

  #  A C++ Qt3DInput::QMouseHandlerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QMouseHandlerPrivate'

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
    'Qt3DInput::QMouseHandlerPrivate::QMouseHandlerPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandlerprivate.html
    """
    #  Qt3DInput::QMouseHandlerPrivate::QMouseHandlerPrivate()
    self._noteCreation(QMouseHandlerPrivate, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput20QMouseHandlerPrivateC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandlerPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandlerprivate.html#init
    """
    #  void Qt3DInput::QMouseHandlerPrivate::init()
    self.uglySide.call('ritual_ZN9Qt3DInput20QMouseHandlerPrivate4initEv')

  def q_func(self) -> Optional[Qt3DInput.QMouseHandler]:
    """
    Calls Qt's 'QMouseHandler *Qt3DInput::QMouseHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandlerprivate.html#q_func

    Returns
    -------

    Optional[Qt3DInput.QMouseHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMouseHandler *Qt3DInput::QMouseHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput20QMouseHandlerPrivate6q_funcEv',
    )
    return Qt3DInput.QMouseHandler._cuteAt(address)

  @staticmethod
  def mouseEvent(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::QMouseHandlerPrivate::mouseEvent(const
    QMouseEventPtr &event)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QMouseHandlerPrivate.mouseEvent' has no cute function "
        "yet. Qt's 'void Qt3DInput::QMouseHandlerPrivate::mouseEvent(const "
        "QMouseEventPtr &event)': takes a type Python has no way to hand "
        "over yet.")
