"""
QTextStreamManipulator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QTextStreamManipulator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextStreamManipulator: a plain Python object
  standing in front of one C++ QTextStreamManipulator.

  C++ hands a QTextStreamManipulator around as a copy, so every C++
  QTextStreamManipulator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QTextStreamManipulator yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QTextStreamManipulator::exec(QTextStream &s)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QTextStreamManipulator::~QTextStreamManipulator()': the destructor:
    Python removes its C++ QTextStreamManipulator by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QTextStreamManipulator is created at the first use, not by
    'QTextStreamManipulator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextStreamManipulator back gives a copy the ritual
    made for Python, in a new cute QTextStreamManipulator.
  - Each name of Qt's QTextStreamManipulator that has no cute function yet,
    '__init__', 'exec', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextStreamManipulator'

  #  Qt's '~QTextStreamManipulator()'. Naming it makes this a value class:
  #  Python owns every C++ QTextStreamManipulator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QTextStreamManipulatorD1Ev'

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
    - Qt's 'QTextStreamManipulator::QTextStreamManipulator(QTSMFI m, int a)':
      takes or gives a type that cannot be passed yet: void
      (QTextStream::*)(int).
    - Qt's 'QTextStreamManipulator::QTextStreamManipulator(QTSMFC m, QChar
      c)': takes or gives a type that cannot be passed yet: void
      (QTextStream::*)(QChar).
    """
    raise NotImplementedError(
        "'QTextStreamManipulator.__init__' has no cute function yet. Qt's "
        "'QTextStreamManipulator::QTextStreamManipulator(QTSMFI m, int a)': "
        "takes or gives a type that cannot be passed yet: void "
        "(QTextStream::*)(int). Qt's "
        "'QTextStreamManipulator::QTextStreamManipulator(QTSMFC m, QChar "
        "c)': takes or gives a type that cannot be passed yet: void "
        "(QTextStream::*)(QChar).")

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
  def exec(*__, **_) -> Never:
    """
    Qt's 'void QTextStreamManipulator::exec(QTextStream &s)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextStreamManipulator.exec' has no cute function yet. Qt's 'void "
        "QTextStreamManipulator::exec(QTextStream &s)': takes a type Python "
        "has no way to hand over yet.")
