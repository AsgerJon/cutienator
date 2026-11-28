"""
QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QRegularExpressionMatchIterator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRegularExpressionMatchIterator = WAIT['QRegularExpressionMatchIterator']


class QRegularExpressionMatchIteratorRangeBasedForIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator: a plain
  Python object standing in front of one C++
  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator.

  C++ hands a QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator
  around as a copy, so every C++
  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's
  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator that has a
  ritual and that Python can call so far, 2 names in all: '__eq__', '__ne__'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRegularExpressionMatch
    &QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    operator*() const': an operator Python has no name for.
  - Qt's 'QRegularExpressionMatchIteratorRangeBasedForIterator
    &QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    operator++()': an operator Python has no name for.
  - Qt's 'QRegularExpressionMatchIteratorRangeBasedForIterator
    QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    operator++(int a0)': an operator Python has no name for.
  - Qt's 'bool operator==(const
    QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)': takes in
    Python what 'bool operator==(const
    QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)'
    takes.
  - Qt's 'bool operator!=(const
    QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)': takes in
    Python what 'bool operator!=(const
    QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)'
    takes.
  - Qt's 'QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    ~QRegularExpressionMatchIteratorRangeBasedForIterator()': the destructor:
    Python removes its C++
    QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator
    is created at the first use, not by
    'QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a
    QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator back
    gives a copy the ritual made for Python, in a new cute
    QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator'

  #  Qt's
  #  '~QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator()'.
  #  Naming it makes this a value class: Python owns every C++
  #  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN9QtPrivate52QRegularExpressionMatchIteratorRangeBasedForIteratorD1Ev')

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

  @overload(THIS)
  def __eq__(
      self,
      rhs: QRegularExpressionMatchIteratorRangeBasedForIterator,
  ) -> bool:
    """
    Calls Qt's 'bool operator==(const
    QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qregularexpressionmatchiteratorrangebasedforiterator.html

    Parameters
    ----------

    rhs : QRegularExpressionMatchIteratorRangeBasedForIterator
      Passed on as a value: Qt reads the C++
      QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator, which
      stays Python's own.
    """
    #  bool operator==(const
    #      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    #      QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_52QRegularExpressionMatchIteratorRangeB'
        'asedForIteratorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(
      WAIT['QtPrivate.QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel'],
  )
  def __eq__(
      self,
      rhs: QtPrivate.QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel,
  ) -> bool:
    """
    Calls Qt's 'bool operator==(const
    QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qregularexpressionmatchiteratorrangebasedforiterator.html

    Parameters
    ----------

    rhs : QtPrivate.QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel
      Passed on as a value: Qt reads the C++
      QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel,
      which stays Python's own.
    """
    #  bool operator==(const
    #      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    #      QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_52QRegularExpressionMatchIteratorRangeB'
        'asedForIteratorERKNS_60QRegularExpressionMatchIteratorRangeBasedFo'
        'rIteratorSentinelE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(
      self,
      rhs: QRegularExpressionMatchIteratorRangeBasedForIterator,
  ) -> bool:
    """
    Calls Qt's 'bool operator!=(const
    QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qregularexpressionmatchiteratorrangebasedforiterator.html

    Parameters
    ----------

    rhs : QRegularExpressionMatchIteratorRangeBasedForIterator
      Passed on as a value: Qt reads the C++
      QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator, which
      stays Python's own.
    """
    #  bool operator!=(const
    #      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    #      QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_52QRegularExpressionMatchIteratorRangeB'
        'asedForIteratorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(
      WAIT['QtPrivate.QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel'],
  )
  def __ne__(
      self,
      rhs: QtPrivate.QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel,
  ) -> bool:
    """
    Calls Qt's 'bool operator!=(const
    QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qregularexpressionmatchiteratorrangebasedforiterator.html

    Parameters
    ----------

    rhs : QtPrivate.QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel
      Passed on as a value: Qt reads the C++
      QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel,
      which stays Python's own.
    """
    #  bool operator!=(const
    #      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
    #      QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_52QRegularExpressionMatchIteratorRangeB'
        'asedForIteratorERKNS_60QRegularExpressionMatchIteratorRangeBasedFo'
        'rIteratorSentinelE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    QRegularExpressionMatchIteratorRangeBasedForIterator()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qregularexpressionmatchiteratorrangebasedforiterator.html
    """
    #  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    #      QRegularExpressionMatchIteratorRangeBasedForIterator()
    self._noteCreation(
        QRegularExpressionMatchIteratorRangeBasedForIterator, lambda: Rituals.call(
            'ritual_ZN9QtPrivate52QRegularExpressionMatchIteratorRangeBased'
            'ForIteratorC1Ev',
        ))

  @overload(QRegularExpressionMatchIterator)
  def __init__(self, iterator: QRegularExpressionMatchIterator) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    QRegularExpressionMatchIteratorRangeBasedForIterator(const
    QRegularExpressionMatchIterator &iterator)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qregularexpressionmatchiteratorrangebasedforiterator.html

    Parameters
    ----------

    iterator : QRegularExpressionMatchIterator
      Passed on as a value: Qt reads the C++ QRegularExpressionMatchIterator,
      which stays Python's own.
    """
    #  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::
    #      QRegularExpressionMatchIteratorRangeBasedForIterator(const
    #      QRegularExpressionMatchIterator &iterator)
    self._noteCreation(
        QRegularExpressionMatchIteratorRangeBasedForIterator, lambda: Rituals.call(
            'ritual_ZN9QtPrivate52QRegularExpressionMatchIteratorRangeBased'
            'ForIteratorC1ERK31QRegularExpressionMatchIterator',
            self._valueOf(iterator),
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
