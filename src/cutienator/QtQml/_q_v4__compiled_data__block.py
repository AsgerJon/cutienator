"""
QV4::CompiledData::Block binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Block to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Block(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Block: a plain Python object
  standing in front of one C++ QV4::CompiledData::Block.

  C++ hands a QV4::CompiledData::Block around as a copy, so every C++
  QV4::CompiledData::Block behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Block that has a ritual and that
  Python can call so far, 2 names in all: 'calculateSize', 'align'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const quint32_le *QV4::CompiledData::Block::localsTable() const':
    gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which
    has no cute class yet.
  - Qt's 'QV4::CompiledData::Block::~Block()': the destructor: Python removes
    its C++ QV4::CompiledData::Block by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Block is created at the first use, not by
    'QV4::CompiledData::Block(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Block back gives a copy the ritual
    made for Python, in a new cute QV4::CompiledData::Block.
  - Each name of Qt's QV4::CompiledData::Block that has no cute function yet,
    'localsTable', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def calculateSize(nLocals: int) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Block::calculateSize(int nLocals)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-block.html#calculateSize

    Parameters
    ----------

    nLocals : int
      Passed on as it is.
    """
    #  int QV4::CompiledData::Block::calculateSize(int nLocals)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData5Block13calculateSizeEi', nLocals,
    )

  @staticmethod
  @overload(int)
  def align(a: int) -> int:
    """
    Calls Qt's 'size_t QV4::CompiledData::Block::align(size_t a)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-block.html#align

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  size_t QV4::CompiledData::Block::align(size_t a)
    return Rituals.call('ritual_ZN3QV412CompiledData5Block5alignEm', a)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Block'

  #  Qt's '~QV4::CompiledData::Block()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::CompiledData::Block behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData5BlockD1Ev'

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
  def localsTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Block::localsTable() const':
    gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Block.localsTable' has no cute function yet. "
        "Qt's 'const quint32_le *QV4::CompiledData::Block::localsTable() "
        "const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned "
        "int>>', which has no cute class yet.")
