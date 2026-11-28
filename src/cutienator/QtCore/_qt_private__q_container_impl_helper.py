"""
QtPrivate::QContainerImplHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qarraydata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QContainerImplHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QContainerImplHelper: a plain Python
  object standing in front of one C++ QtPrivate::QContainerImplHelper.

  C++ hands a QtPrivate::QContainerImplHelper around as a copy, so every C++
  QtPrivate::QContainerImplHelper behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QtPrivate::QContainerImplHelper yet. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'CutResult QtPrivate::QContainerImplHelper::mid(qsizetype
    originalLength, qsizetype *_position, qsizetype *_length)': takes a
    number to change where it is.
  - Qt's 'QtPrivate::QContainerImplHelper::~QContainerImplHelper()': the
    destructor: Python removes its C++ QtPrivate::QContainerImplHelper by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QContainerImplHelper is created at the first use, not
    by 'QtPrivate::QContainerImplHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QContainerImplHelper back gives a copy the
    ritual made for Python, in a new cute QtPrivate::QContainerImplHelper.
  - Each name of Qt's QtPrivate::QContainerImplHelper that has no cute
    function yet, 'mid', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QtPrivate::QContainerImplHelper, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class CutResult(CuteNum):
    """
    The enum 'QtPrivate::QContainerImplHelper::CutResult' of Qt, with the 4
    names Qt gives in it.
    """

    Null = Kee[int](0)
    Empty = Kee[int](1)
    Full = Kee[int](2)
    Subset = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QContainerImplHelper'

  #  Qt's '~QtPrivate::QContainerImplHelper()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::QContainerImplHelper behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate20QContainerImplHelperD1Ev'

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
  def mid(*__, **_) -> Never:
    """
    Qt's 'CutResult QtPrivate::QContainerImplHelper::mid(qsizetype
    originalLength, qsizetype *_position, qsizetype *_length)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QtPrivate.QContainerImplHelper.mid' has no cute function yet. "
        "Qt's 'CutResult QtPrivate::QContainerImplHelper::mid(qsizetype "
        "originalLength, qsizetype *_position, qsizetype *_length)': takes "
        "a number to change where it is.")
