"""
QJSValueIteratorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qjsvalueiterator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QJSValueIteratorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QJSValueIteratorPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSValueIteratorPrivate: a plain Python object
  standing in front of one C++ QJSValueIteratorPrivate.

  What exists
  -----------

  Every function of Qt's QJSValueIteratorPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'init', 'isValid', 'next'. It can
  be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QJSValueIteratorPrivate is created at the first use, not by
    'QJSValueIteratorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QJSValueIteratorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSValueIteratorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QJSValueIteratorPrivate::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueiteratorprivate.html#isValid
    """
    #  bool QJSValueIteratorPrivate::isValid() const
    return self.uglySide.call(
        'ritual_ZNK23QJSValueIteratorPrivate7isValidEv',
    )

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

  @overload(QJSValue)
  def __init__(self, v: QJSValue) -> None:
    """
    Notes what was given, for Qt's
    'QJSValueIteratorPrivate::QJSValueIteratorPrivate(const QJSValue &v)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueiteratorprivate.html

    Parameters
    ----------

    v : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  QJSValueIteratorPrivate::QJSValueIteratorPrivate(const QJSValue &v)
    self._noteCreation(QJSValueIteratorPrivate, lambda: Rituals.call(
        'ritual_ZN23QJSValueIteratorPrivateC1ERK8QJSValue', self._valueOf(v),
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

  @overload(QJSValue)
  def init(self, v: QJSValue) -> None:
    """
    Calls Qt's 'void QJSValueIteratorPrivate::init(const QJSValue &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueiteratorprivate.html#init

    Parameters
    ----------

    v : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSValueIteratorPrivate::init(const QJSValue &v)
    self.uglySide.call(
        'ritual_ZN23QJSValueIteratorPrivate4initERK8QJSValue',
        self._valueOf(v),
    )

  def next(self) -> None:
    """
    Calls Qt's 'void QJSValueIteratorPrivate::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueiteratorprivate.html#next
    """
    #  void QJSValueIteratorPrivate::next()
    self.uglySide.call('ritual_ZN23QJSValueIteratorPrivate4nextEv')
