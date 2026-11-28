"""
QtMetaContainerPrivate::SequentialIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetasequence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class SequentialIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaContainerPrivate::SequentialIterator: a plain
  Python object standing in front of one C++
  QtMetaContainerPrivate::SequentialIterator.

  C++ hands a QtMetaContainerPrivate::SequentialIterator around as a copy, so
  every C++ QtMetaContainerPrivate::SequentialIterator behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QtMetaContainerPrivate::SequentialIterator yet. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::SequentialIterator::SequentialIterator(
    QIterator<QMetaSequence> &&it)': takes a type Python has no way to hand
    over yet.
  - Qt's 'reference QtMetaContainerPrivate::SequentialIterator::operator*()
    const': an operator Python has no name for.
  - Qt's 'pointer QtMetaContainerPrivate::SequentialIterator::operator->()
    const': an operator Python has no name for.
  - Qt's 'reference
    QtMetaContainerPrivate::SequentialIterator::operator[](qsizetype n)
    const': gives a type Python has no way to take yet.
  - Qt's 'QtMetaContainerPrivate::SequentialIterator::~SequentialIterator()':
    the destructor: Python removes its C++
    QtMetaContainerPrivate::SequentialIterator by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::SequentialIterator is created at the
    first use, not by 'QtMetaContainerPrivate::SequentialIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::SequentialIterator back gives
    a copy the ritual made for Python, in a new cute
    QtMetaContainerPrivate::SequentialIterator.
  - Each name of Qt's QtMetaContainerPrivate::SequentialIterator that has no
    cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QtMetaContainerPrivate::SequentialIterator'

  #  Qt's '~QtMetaContainerPrivate::SequentialIterator()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtMetaContainerPrivate::SequentialIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtMetaContainerPrivate18SequentialIteratorD1Ev')

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
    Qt's 'QtMetaContainerPrivate::SequentialIterator::SequentialIterator(
    QIterator<QMetaSequence> &&it)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.SequentialIterator.__init__' has no cute "
        "function yet. Qt's "
        "'QtMetaContainerPrivate::SequentialIterator::SequentialIterator(QIt"
        "erator<QMetaSequence> &&it)': takes a type Python has no way to "
        "hand over yet.")

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
