"""
QV4::CallData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4calldata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::CallData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class CallData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CallData: a plain Python object standing in
  front of one C++ QV4::CallData.

  C++ hands a QV4::CallData around as a copy, so every C++ QV4::CallData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CallData that has a ritual and that Python can
  call so far, 4 names in all: 'argc', 'setArgc', 'argument', 'HeaderSize'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CallData::~CallData()': the destructor: Python removes its C++
    QV4::CallData by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QV4::CallData is created at the first use, not by
    'QV4::CallData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CallData back gives a copy the ritual made for
    Python, in a new cute QV4::CallData.
  - Each name of Qt's QV4::CallData that has no cute function yet,
    'argValues', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QV4::CallData, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Offsets(CuteNum):
    """
    The enum 'QV4::CallData::Offsets' of Qt, with the 8 names Qt gives in it.
    """

    Function = Kee[int](0)
    Context = Kee[int](1)
    Accumulator = Kee[int](2)
    This = Kee[int](3)
    NewTarget = Kee[int](4)
    Argc = Kee[int](5)
    LastOffset = Kee[int](5)
    OffsetCount = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def HeaderSize() -> int:
    """
    Calls Qt's 'int QV4::CallData::HeaderSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-calldata.html#HeaderSize
    """
    #  int QV4::CallData::HeaderSize()
    return Rituals.call('ritual_ZN3QV48CallData10HeaderSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CallData'

  #  Qt's '~QV4::CallData()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::CallData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV48CallDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def argc(self) -> int:
    """
    Calls Qt's 'int QV4::CallData::argc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-calldata.html#argc
    """
    #  int QV4::CallData::argc() const
    return self.uglySide.call('ritual_ZNK3QV48CallData4argcEv')

  @overload(int)
  def argument(self, i: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::CallData::argument(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-calldata.html#argument

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::CallData::argument(int i) const
    return self.uglySide.call('ritual_ZNK3QV48CallData8argumentEi', i)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setArgc(self, argc: int) -> None:
    """
    Calls Qt's 'void QV4::CallData::setArgc(int argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-calldata.html#setArgc

    Parameters
    ----------

    argc : int
      Passed on as it is.
    """
    #  void QV4::CallData::setArgc(int argc)
    self.uglySide.call('ritual_ZN3QV48CallData7setArgcEi', argc)

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
  def argValues(*__, **_) -> Never:
    """
    Qt's 'QV4::CallData::argValues': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.CallData.argValues' has no cute function yet. Qt's "
        "'QV4::CallData::argValues': a template: a pattern and no single "
        "function.")
