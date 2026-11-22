"""
QCborError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcborcommon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute


class QCborError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCborError: a plain Python object standing in front
  of one C++ QCborError.

  C++ hands a QCborError around as a copy, so every C++ QCborError behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCborError that has a ritual and that Python can
  call so far, 1 name in all: 'toString'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Code QCborError::operator QCborError::Code() const': an operator
    Python has no name for.
  - Qt's 'QCborError::~QCborError()': the destructor: Python removes its C++
    QCborError by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 6 functions Qt declares: 1 declared and nowhere to be found; 1 a
  template; 1 private.

  What to expect
  --------------

  - The C++ QCborError is created at the first use, not by 'QCborError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCborError back gives a copy the ritual made for
    Python, in a new cute QCborError.
  """

  #  The enums Qt writes inside QCborError, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Code(CuteNum):
    """
    The enum 'QCborError::Code' of Qt, with the 15 names Qt gives in it.
    """

    UnknownError = Kee[int](1)
    AdvancePastEnd = Kee[int](3)
    InputOutputError = Kee[int](4)
    GarbageAtEnd = Kee[int](256)
    EndOfFile = Kee[int](257)
    UnexpectedBreak = Kee[int](258)
    UnknownType = Kee[int](259)
    IllegalType = Kee[int](260)
    IllegalNumber = Kee[int](261)
    IllegalSimpleType = Kee[int](262)
    InvalidUtf8String = Kee[int](516)
    DataTooLarge = Kee[int](1024)
    NestingTooDeep = Kee[int](1025)
    UnsupportedType = Kee[int](1026)
    NoError = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborError'

  #  Qt's '~QCborError()'. Naming it makes this a value class: Python owns
  #  every C++ QCborError behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QCborErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QCborError::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborerror.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCborError::toString() const
    return self.uglySide.call('ritual_ZNK10QCborError8toStringEv')

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
