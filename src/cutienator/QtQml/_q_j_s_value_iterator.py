"""
QJSValueIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qjsvalueiterator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QJSValue, QJSValueIteratorPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QJSValueIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSValueIterator: a plain Python object standing in
  front of one C++ QJSValueIterator.

  What exists
  -----------

  Every function of Qt's QJSValueIterator that has a ritual and that Python
  can call so far, 5 names in all: 'hasNext', 'next', 'name', 'value',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJSValueIterator::~QJSValueIterator()': the destructor: Python
    never removes a C++ QJSValueIterator.
  - Qt's 'QJSValueIterator &QJSValueIterator::operator=(QJSValue &value)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const QJSValueIteratorPrivate *QJSValueIterator::d_func() const':
    takes in Python what 'QJSValueIteratorPrivate
    *QJSValueIterator::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QJSValueIterator is created at the first use, not by
    'QJSValueIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QJSValueIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSValueIterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QJSValueIterator::hasNext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueiterator.html#hasNext
    """
    #  bool QJSValueIterator::hasNext() const
    return self.uglySide.call('ritual_ZNK16QJSValueIterator7hasNextEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QJSValueIterator::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueiterator.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSValueIterator::name() const
    return self.uglySide.call('ritual_ZNK16QJSValueIterator4nameEv')

  def value(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSValueIterator::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueiterator.html#value

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValueIterator::value() const
    address = self.uglySide.call('ritual_ZNK16QJSValueIterator5valueEv')
    from . import QJSValue
    return QJSValue._cuteOwning(address)

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
  def __init__(self, value: QJSValue) -> None:
    """
    Notes what was given, for Qt's 'QJSValueIterator::QJSValueIterator(const
    QJSValue &value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsvalueiterator.html#QJSValueIterator

    Parameters
    ----------

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  QJSValueIterator::QJSValueIterator(const QJSValue &value)
    self._noteCreation(QJSValueIterator, lambda: Rituals.call(
        'ritual_ZN16QJSValueIteratorC1ERK8QJSValue', self._valueOf(value),
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

  def next(self) -> bool:
    """
    Calls Qt's 'bool QJSValueIterator::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueiterator.html#next
    """
    #  bool QJSValueIterator::next()
    return self.uglySide.call('ritual_ZN16QJSValueIterator4nextEv')

  def d_func(self) -> Optional[QJSValueIteratorPrivate]:
    """
    Calls Qt's 'QJSValueIteratorPrivate *QJSValueIterator::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalueiterator.html#d_func

    Returns
    -------

    Optional[QJSValueIteratorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSValueIteratorPrivate *QJSValueIterator::d_func()
    address = self.uglySide.call('ritual_ZN16QJSValueIterator6d_funcEv')
    from . import QJSValueIteratorPrivate
    return QJSValueIteratorPrivate._cuteAt(address)
