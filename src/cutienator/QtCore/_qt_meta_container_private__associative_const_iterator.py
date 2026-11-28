"""
QtMetaContainerPrivate::AssociativeConstIterator binding of the Qt C++
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


class AssociativeConstIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaContainerPrivate::AssociativeConstIterator: a
  plain Python object standing in front of one C++
  QtMetaContainerPrivate::AssociativeConstIterator.

  C++ hands a QtMetaContainerPrivate::AssociativeConstIterator around as a
  copy, so every C++ QtMetaContainerPrivate::AssociativeConstIterator behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtMetaContainerPrivate::AssociativeConstIterator
  that has a ritual and that Python can call so far, 2 names in all: 'key',
  'value'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::AssociativeConstIterator::
    AssociativeConstIterator(QConstIterator<QMetaAssociation> &&it)': takes a
    type Python has no way to hand over yet.
  - Qt's 'mapped_type
    QtMetaContainerPrivate::AssociativeConstIterator::operator*() const': an
    operator Python has no name for.
  - Qt's 'pointer
    QtMetaContainerPrivate::AssociativeConstIterator::operator->() const': an
    operator Python has no name for.
  - Qt's 'QtMetaContainerPrivate::AssociativeConstIterator::
    ~AssociativeConstIterator()': the destructor: Python removes its C++
    QtMetaContainerPrivate::AssociativeConstIterator by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::AssociativeConstIterator is created at
    the first use, not by
    'QtMetaContainerPrivate::AssociativeConstIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::AssociativeConstIterator back
    gives a copy the ritual made for Python, in a new cute
    QtMetaContainerPrivate::AssociativeConstIterator.
  - Each name of Qt's QtMetaContainerPrivate::AssociativeConstIterator that
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
  __qt_class__ = 'QtMetaContainerPrivate::AssociativeConstIterator'

  #  Qt's '~QtMetaContainerPrivate::AssociativeConstIterator()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtMetaContainerPrivate::AssociativeConstIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtMetaContainerPrivate24AssociativeConstIteratorD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> QVariant:
    """
    Calls Qt's 'key_type
    QtMetaContainerPrivate::AssociativeConstIterator::key() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-associativeconstiterator.html

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  key_type QtMetaContainerPrivate::AssociativeConstIterator::key() const
    address = self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate24AssociativeConstIterator3keyEv',
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def value(self) -> QVariant:
    """
    Calls Qt's 'mapped_type
    QtMetaContainerPrivate::AssociativeConstIterator::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-associativeconstiterator.html

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  mapped_type QtMetaContainerPrivate::AssociativeConstIterator::value()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate24AssociativeConstIterator5value'
        'Ev',
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
    Qt's 'QtMetaContainerPrivate::AssociativeConstIterator::
    AssociativeConstIterator(QConstIterator<QMetaAssociation> &&it)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.AssociativeConstIterator.__init__' has no "
        "cute function yet. Qt's "
        "'QtMetaContainerPrivate::AssociativeConstIterator::AssociativeConst"
        "Iterator(QConstIterator<QMetaAssociation> &&it)': takes a type "
        "Python has no way to hand over yet.")

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
