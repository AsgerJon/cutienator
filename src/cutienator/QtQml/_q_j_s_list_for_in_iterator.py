"""
QJSListForInIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtQml/qjslist.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QJSListForInIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSListForInIterator: a plain Python object standing
  in front of one C++ QJSListForInIterator.

  C++ hands a QJSListForInIterator around as a copy, so every C++
  QJSListForInIterator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJSListForInIterator that has a ritual and that
  Python can call so far, 2 names in all: 'hasNext', 'next'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJSListForInIterator::~QJSListForInIterator()': the destructor:
    Python removes its C++ QJSListForInIterator by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QJSListForInIterator is created at the first use, not by
    'QJSListForInIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJSListForInIterator back gives a copy the ritual
    made for Python, in a new cute QJSListForInIterator.
  - Each name of Qt's QJSListForInIterator that has no cute function yet,
    'init', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSListForInIterator'

  #  Qt's '~QJSListForInIterator()'. Naming it makes this a value class:
  #  Python owns every C++ QJSListForInIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QJSListForInIteratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QJSListForInIterator::hasNext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjslistforiniterator.html#hasNext
    """
    #  bool QJSListForInIterator::hasNext() const
    return self.uglySide.call('ritual_ZNK20QJSListForInIterator7hasNextEv')

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

  def next(self) -> int:
    """
    Calls Qt's 'qsizetype QJSListForInIterator::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qjslistforiniterator.html#next
    """
    #  qsizetype QJSListForInIterator::next()
    return self.uglySide.call('ritual_ZN20QJSListForInIterator4nextEv')

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'QJSListForInIterator::init': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSListForInIterator.init' has no cute function yet. Qt's "
        "'QJSListForInIterator::init': a template: a pattern and no single "
        "function.")
