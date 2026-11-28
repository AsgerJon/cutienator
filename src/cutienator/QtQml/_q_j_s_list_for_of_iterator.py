"""
QJSListForOfIterator binding of the Qt C++
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


class QJSListForOfIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSListForOfIterator: a plain Python object standing
  in front of one C++ QJSListForOfIterator.

  C++ hands a QJSListForOfIterator around as a copy, so every C++
  QJSListForOfIterator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJSListForOfIterator that has a ritual and that
  Python can call so far, 1 name in all: 'init'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJSListForOfIterator::~QJSListForOfIterator()': the destructor:
    Python removes its C++ QJSListForOfIterator by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QJSListForOfIterator is created at the first use, not by
    'QJSListForOfIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJSListForOfIterator back gives a copy the ritual
    made for Python, in a new cute QJSListForOfIterator.
  - Each name of Qt's QJSListForOfIterator that has no cute function yet,
    'hasNext', 'next', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QJSListForOfIterator'

  #  Qt's '~QJSListForOfIterator()'. Naming it makes this a value class:
  #  Python owns every C++ QJSListForOfIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QJSListForOfIteratorD1Ev'

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

  def init(self) -> None:
    """
    Calls Qt's 'void QJSListForOfIterator::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qjslistforofiterator.html#init
    """
    #  void QJSListForOfIterator::init()
    self.uglySide.call('ritual_ZN20QJSListForOfIterator4initEv')

  @staticmethod
  def hasNext(*__, **_) -> Never:
    """
    Qt's 'QJSListForOfIterator::hasNext': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSListForOfIterator.hasNext' has no cute function yet. Qt's "
        "'QJSListForOfIterator::hasNext': a template: a pattern and no "
        "single function.")

  @staticmethod
  def next(*__, **_) -> Never:
    """
    Qt's 'QJSListForOfIterator::next': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSListForOfIterator.next' has no cute function yet. Qt's "
        "'QJSListForOfIterator::next': a template: a pattern and no single "
        "function.")
