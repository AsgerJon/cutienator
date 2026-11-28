"""
QAssociativeIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qassociativeiterable.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QVariant


class QAssociativeIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAssociativeIterator: a plain Python object standing
  in front of one C++ QAssociativeIterator.

  What exists
  -----------

  Every function of Qt's QAssociativeIterator that has a ritual and that
  Python can call so far, 1 name in all: 'key'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QAssociativeIterator::QAssociativeIterator(QIterator<QMetaAssociation>
    &&it)': takes a type Python has no way to hand over yet.
  - Qt's 'QVariantRef<QAssociativeIterator> QAssociativeIterator::value()
    const': gives a type Python has no way to take yet.
  - Qt's 'QVariantRef<QAssociativeIterator> QAssociativeIterator::operator*()
    const': an operator Python has no name for.
  - Qt's 'QVariantPointer<QAssociativeIterator>
    QAssociativeIterator::operator->() const': an operator Python has no name
    for.

  What to expect
  --------------

  - The C++ QAssociativeIterator is created at the first use, not by
    'QAssociativeIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAssociativeIterator.
  - Each name of Qt's QAssociativeIterator that has no cute function yet,
    '__init__', 'value', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QAssociativeIterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAssociativeIterator::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qassociativeiterator.html#key

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAssociativeIterator::key() const
    address = self.uglySide.call('ritual_ZNK20QAssociativeIterator3keyEv')
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
    Qt's
    'QAssociativeIterator::QAssociativeIterator(QIterator<QMetaAssociation>
    &&it)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterator.__init__' has no cute function yet. Qt's "
        "'QAssociativeIterator::QAssociativeIterator(QIterator<QMetaAssociat"
        "ion> &&it)': takes a type Python has no way to hand over yet.")

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
    Qt's 'QVariantRef<QAssociativeIterator> QAssociativeIterator::value()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterator.value' has no cute function yet. Qt's "
        "'QVariantRef<QAssociativeIterator> QAssociativeIterator::value() "
        "const': gives a type Python has no way to take yet.")
