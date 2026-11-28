"""
HPack::PrefixTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/huffman_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means HPack::PrefixTable to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class PrefixTable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HPack::PrefixTable: a plain Python object standing in
  front of one C++ HPack::PrefixTable.

  C++ hands a HPack::PrefixTable around as a copy, so every C++
  HPack::PrefixTable behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's HPack::PrefixTable that has a ritual and that Python
  can call so far, 1 name in all: 'size'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'HPack::PrefixTable::~PrefixTable()': the destructor: Python removes
    its C++ HPack::PrefixTable by it, and has no other use for it.

  What to expect
  --------------

  - The C++ HPack::PrefixTable is created at the first use, not by
    'HPack::PrefixTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a HPack::PrefixTable back gives a copy the ritual made
    for Python, in a new cute HPack::PrefixTable.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'HPack::PrefixTable'

  #  Qt's '~HPack::PrefixTable()'. Naming it makes this a value class: Python
  #  owns every C++ HPack::PrefixTable behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN5HPack11PrefixTableD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'quint32 HPack::PrefixTable::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-prefixtable.html#size
    """
    #  quint32 HPack::PrefixTable::size() const
    return self.uglySide.call('ritual_ZNK5HPack11PrefixTable4sizeEv')

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
    Notes what was given, for Qt's 'HPack::PrefixTable::PrefixTable()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/hpack-prefixtable.html#PrefixTable
    """
    #  HPack::PrefixTable::PrefixTable()
    self._noteCreation(PrefixTable, lambda: Rituals.call(
        'ritual_ZN5HPack11PrefixTableC1Ev',
    ))

  @overload(int, int)
  def __init__(self, prefix: int, index: int) -> None:
    """
    Notes what was given, for Qt's 'HPack::PrefixTable::PrefixTable(quint32
    prefix, quint32 index)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/hpack-prefixtable.html#PrefixTable

    Parameters
    ----------

    prefix : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  HPack::PrefixTable::PrefixTable(quint32 prefix, quint32 index)
    self._noteCreation(PrefixTable, lambda: Rituals.call(
        'ritual_ZN5HPack11PrefixTableC1Ejj', prefix, index,
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
