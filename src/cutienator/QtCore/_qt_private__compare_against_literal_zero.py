"""
QtPrivate::CompareAgainstLiteralZero binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcompare_impl.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class CompareAgainstLiteralZero(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::CompareAgainstLiteralZero: a plain Python
  object standing in front of one C++ QtPrivate::CompareAgainstLiteralZero.

  C++ hands a QtPrivate::CompareAgainstLiteralZero around as a copy, so every
  C++ QtPrivate::CompareAgainstLiteralZero behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QtPrivate::CompareAgainstLiteralZero yet. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QtPrivate::CompareAgainstLiteralZero::~CompareAgainstLiteralZero()': the
    destructor: Python removes its C++ QtPrivate::CompareAgainstLiteralZero
    by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QtPrivate::CompareAgainstLiteralZero is created at the first use,
    not by 'QtPrivate::CompareAgainstLiteralZero(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::CompareAgainstLiteralZero back gives a
    copy the ritual made for Python, in a new cute
    QtPrivate::CompareAgainstLiteralZero.
  - Each name of Qt's QtPrivate::CompareAgainstLiteralZero that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QtPrivate::CompareAgainstLiteralZero'

  #  Qt's '~QtPrivate::CompareAgainstLiteralZero()'. Naming it makes this a
  #  value class: Python owns every C++ QtPrivate::CompareAgainstLiteralZero
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate25CompareAgainstLiteralZeroD1Ev'

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
    - Qt's 'QtPrivate::CompareAgainstLiteralZero::CompareAgainstLiteralZero(
      SafeZero a0)': takes or gives a type that cannot be passed yet: void
      (QtPrivate::CompareAgainstLiteralZero::*)().
    - Qt's 'QtPrivate::CompareAgainstLiteralZero::CompareAgainstLiteralZero':
      a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.CompareAgainstLiteralZero.__init__' has no cute "
        "function yet. Qt's "
        "'QtPrivate::CompareAgainstLiteralZero::CompareAgainstLiteralZero(Sa"
        "feZero a0)': takes or gives a type that cannot be passed yet: void "
        "(QtPrivate::CompareAgainstLiteralZero::*)(). Qt's "
        "'QtPrivate::CompareAgainstLiteralZero::CompareAgainstLiteralZero': "
        "a template: a pattern and no single function.")

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
