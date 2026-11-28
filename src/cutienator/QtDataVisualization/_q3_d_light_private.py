"""
Q3DLightPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dlight_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Q3DLightPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import Q3DLight
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DLight = WAIT['Q3DLight']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DLightPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Q3DLightPrivate: a plain Python object standing in
  front of one C++ Q3DLightPrivate.

  C++ hands a Q3DLightPrivate around as a copy, so every C++ Q3DLightPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's Q3DLightPrivate yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Q3DLightPrivate::~Q3DLightPrivate()': the destructor: Python
    removes its C++ Q3DLightPrivate by it, and has no other use for it.
  - Qt's 'void Q3DLightPrivate::sync(Q3DLight &other)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ Q3DLightPrivate is created at the first use, not by
    'Q3DLightPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Q3DLightPrivate back gives a copy the ritual made for
    Python, in a new cute Q3DLightPrivate.
  - Each name of Qt's Q3DLightPrivate that has no cute function yet, 'sync',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DLightPrivate'

  #  Qt's '~Q3DLightPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ Q3DLightPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15Q3DLightPrivateD1Ev'

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

  @overload(Q3DLight)
  @overload(NoneType)
  def __init__(self, q: Optional[Q3DLight]) -> None:
    """
    Notes what was given, for Qt's 'Q3DLightPrivate::Q3DLightPrivate(Q3DLight
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dlightprivate.html#Q3DLightPrivate

    Parameters
    ----------

    q : Optional[Q3DLight]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Q3DLightPrivate::Q3DLightPrivate(Q3DLight *q)
    self._noteCreation(Q3DLightPrivate, lambda: Rituals.call(
        'ritual_ZN15Q3DLightPrivateC1EP8Q3DLight', self._addressOf(q),
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

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'void Q3DLightPrivate::sync(Q3DLight &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DLightPrivate.sync' has no cute function yet. Qt's 'void "
        "Q3DLightPrivate::sync(Q3DLight &other)': takes a type Python has "
        "no way to hand over yet.")
