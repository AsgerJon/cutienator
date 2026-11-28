"""
QtMetaContainerPrivate::SequentialConstIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetasequence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QVariant


class SequentialConstIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaContainerPrivate::SequentialConstIterator: a
  plain Python object standing in front of one C++
  QtMetaContainerPrivate::SequentialConstIterator.

  C++ hands a QtMetaContainerPrivate::SequentialConstIterator around as a
  copy, so every C++ QtMetaContainerPrivate::SequentialConstIterator behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtMetaContainerPrivate::SequentialConstIterator that
  has a ritual and that Python can call so far, 1 name in all: '__getitem__'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::SequentialConstIterator::
    SequentialConstIterator(QConstIterator<QMetaSequence> &&it)': takes a
    type Python has no way to hand over yet.
  - Qt's 'value_type
    QtMetaContainerPrivate::SequentialConstIterator::operator*() const': an
    operator Python has no name for.
  - Qt's 'pointer
    QtMetaContainerPrivate::SequentialConstIterator::operator->() const': an
    operator Python has no name for.
  - Qt's 'QtMetaContainerPrivate::SequentialConstIterator::
    ~SequentialConstIterator()': the destructor: Python removes its C++
    QtMetaContainerPrivate::SequentialConstIterator by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::SequentialConstIterator is created at the
    first use, not by 'QtMetaContainerPrivate::SequentialConstIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::SequentialConstIterator back
    gives a copy the ritual made for Python, in a new cute
    QtMetaContainerPrivate::SequentialConstIterator.
  - Each name of Qt's QtMetaContainerPrivate::SequentialConstIterator that
    has no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QtMetaContainerPrivate::SequentialConstIterator'

  #  Qt's '~QtMetaContainerPrivate::SequentialConstIterator()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtMetaContainerPrivate::SequentialConstIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtMetaContainerPrivate23SequentialConstIteratorD1Ev')

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

  @overload(int)
  def __getitem__(self, n: int) -> QVariant:
    """
    Calls Qt's 'value_type
    QtMetaContainerPrivate::SequentialConstIterator::operator[](qsizetype n)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequentialconstiterator.html

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  value_type
    #      QtMetaContainerPrivate::SequentialConstIterator::operator[](
    #      qsizetype n) const
    address = self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate23SequentialConstIteratorixEx', n,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtMetaContainerPrivate::SequentialConstIterator::
    SequentialConstIterator(QConstIterator<QMetaSequence> &&it)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.SequentialConstIterator.__init__' has no "
        "cute function yet. Qt's "
        "'QtMetaContainerPrivate::SequentialConstIterator::SequentialConstIt"
        "erator(QConstIterator<QMetaSequence> &&it)': takes a type Python "
        "has no way to hand over yet.")

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
