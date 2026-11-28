"""
QAssociativeConstIterator binding of the Qt C++
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


class QAssociativeConstIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAssociativeConstIterator: a plain Python object
  standing in front of one C++ QAssociativeConstIterator.

  What exists
  -----------

  Every function of Qt's QAssociativeConstIterator that has a ritual and that
  Python can call so far, 2 names in all: 'key', 'value'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAssociativeConstIterator::QAssociativeConstIterator(
    QConstIterator<QMetaAssociation> &&it)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QVariant QAssociativeConstIterator::operator*() const': an operator
    Python has no name for.
  - Qt's 'QVariantConstPointer QAssociativeConstIterator::operator->()
    const': an operator Python has no name for.

  What to expect
  --------------

  - The C++ QAssociativeConstIterator is created at the first use, not by
    'QAssociativeConstIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAssociativeConstIterator.
  - Each name of Qt's QAssociativeConstIterator that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAssociativeConstIterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAssociativeConstIterator::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qassociativeconstiterator.html#key

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAssociativeConstIterator::key() const
    address = self.uglySide.call(
        'ritual_ZNK25QAssociativeConstIterator3keyEv',
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAssociativeConstIterator::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeconstiterator.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAssociativeConstIterator::value() const
    address = self.uglySide.call(
        'ritual_ZNK25QAssociativeConstIterator5valueEv',
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
    Qt's 'QAssociativeConstIterator::QAssociativeConstIterator(
    QConstIterator<QMetaAssociation> &&it)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QAssociativeConstIterator.__init__' has no cute function yet. "
        "Qt's "
        "'QAssociativeConstIterator::QAssociativeConstIterator(QConstIterato"
        "r<QMetaAssociation> &&it)': takes a type Python has no way to hand "
        "over yet.")

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
