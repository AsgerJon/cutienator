"""
QAbstract3DInputHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3dinputhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstract3DInputHandlerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstract3DInputHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DInputHandler = WAIT['QAbstract3DInputHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DInputHandlerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstract3DInputHandlerPrivate: a plain Python object
  standing in front of one C++ QAbstract3DInputHandlerPrivate.

  C++ hands a QAbstract3DInputHandlerPrivate around as a copy, so every C++
  QAbstract3DInputHandlerPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QAbstract3DInputHandlerPrivate yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstract3DInputHandlerPrivate::~QAbstract3DInputHandlerPrivate()':
    the destructor: Python removes its C++ QAbstract3DInputHandlerPrivate by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QAbstract3DInputHandlerPrivate is created at the first use, not
    by 'QAbstract3DInputHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAbstract3DInputHandlerPrivate back gives a copy the
    ritual made for Python, in a new cute QAbstract3DInputHandlerPrivate.
  """

  #  The enums Qt writes inside QAbstract3DInputHandlerPrivate, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class InputState(CuteNum):
    """
    The enum 'QAbstract3DInputHandlerPrivate::InputState' of Qt, with the 4
    names Qt gives in it.
    """

    InputStateNone = Kee[int](0)
    InputStateSelecting = Kee[int](1)
    InputStateRotating = Kee[int](2)
    InputStatePinching = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstract3DInputHandlerPrivate'

  #  Qt's '~QAbstract3DInputHandlerPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QAbstract3DInputHandlerPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QAbstract3DInputHandlerPrivateD1Ev'

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

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def __init__(self, q: Optional[QAbstract3DInputHandler]) -> None:
    """
    Notes what was given, for Qt's
    'QAbstract3DInputHandlerPrivate::QAbstract3DInputHandlerPrivate(
    QAbstract3DInputHandler *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandlerprivate.html

    Parameters
    ----------

    q : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstract3DInputHandlerPrivate::QAbstract3DInputHandlerPrivate(
    #      QAbstract3DInputHandler *q)
    self._noteCreation(QAbstract3DInputHandlerPrivate, lambda: Rituals.call(
        'ritual_ZN30QAbstract3DInputHandlerPrivateC1EP23QAbstract3DInputHan'
        'dler',
        self._addressOf(q),
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
