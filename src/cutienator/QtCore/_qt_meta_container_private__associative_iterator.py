"""
QtMetaContainerPrivate::AssociativeIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetaassociation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QVariant


class AssociativeIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaContainerPrivate::AssociativeIterator: a plain
  Python object standing in front of one C++
  QtMetaContainerPrivate::AssociativeIterator.

  C++ hands a QtMetaContainerPrivate::AssociativeIterator around as a copy,
  so every C++ QtMetaContainerPrivate::AssociativeIterator behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtMetaContainerPrivate::AssociativeIterator that has
  a ritual and that Python can call so far, 1 name in all: 'key'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::AssociativeIterator::AssociativeIterator(
    QIterator<QMetaAssociation> &&it)': takes a type Python has no way to
    hand over yet.
  - Qt's 'reference QtMetaContainerPrivate::AssociativeIterator::value()
    const': gives a type Python has no way to take yet.
  - Qt's 'reference QtMetaContainerPrivate::AssociativeIterator::operator*()
    const': an operator Python has no name for.
  - Qt's 'pointer QtMetaContainerPrivate::AssociativeIterator::operator->()
    const': an operator Python has no name for.
  - Qt's
    'QtMetaContainerPrivate::AssociativeIterator::~AssociativeIterator()':
    the destructor: Python removes its C++
    QtMetaContainerPrivate::AssociativeIterator by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::AssociativeIterator is created at the
    first use, not by 'QtMetaContainerPrivate::AssociativeIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::AssociativeIterator back
    gives a copy the ritual made for Python, in a new cute
    QtMetaContainerPrivate::AssociativeIterator.
  - Each name of Qt's QtMetaContainerPrivate::AssociativeIterator that has no
    cute function yet, '__init__', 'value', holds a function that raises
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
  __qt_class__ = 'QtMetaContainerPrivate::AssociativeIterator'

  #  Qt's '~QtMetaContainerPrivate::AssociativeIterator()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtMetaContainerPrivate::AssociativeIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtMetaContainerPrivate19AssociativeIteratorD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> QVariant:
    """
    Calls Qt's 'key_type QtMetaContainerPrivate::AssociativeIterator::key()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-associativeiterator.html

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  key_type QtMetaContainerPrivate::AssociativeIterator::key() const
    address = self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate19AssociativeIterator3keyEv',
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

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
    Qt's 'QtMetaContainerPrivate::AssociativeIterator::AssociativeIterator(
    QIterator<QMetaAssociation> &&it)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.AssociativeIterator.__init__' has no cute "
        "function yet. Qt's "
        "'QtMetaContainerPrivate::AssociativeIterator::AssociativeIterator(Q"
        "Iterator<QMetaAssociation> &&it)': takes a type Python has no way "
        "to hand over yet.")

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
  def value(*__, **_) -> Never:
    """
    Qt's 'reference QtMetaContainerPrivate::AssociativeIterator::value()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.AssociativeIterator.value' has no cute "
        "function yet. Qt's 'reference "
        "QtMetaContainerPrivate::AssociativeIterator::value() const': gives "
        "a type Python has no way to take yet.")
