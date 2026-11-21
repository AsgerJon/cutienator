"""
QRegularExpressionMatchIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QRegularExpression

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QRegularExpressionMatch


class QRegularExpressionMatchIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRegularExpressionMatchIterator: a plain Python
  object standing in front of one C++ QRegularExpressionMatchIterator.

  C++ hands a QRegularExpressionMatchIterator around as a copy, so every C++
  QRegularExpressionMatchIterator behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QRegularExpressionMatchIterator that has a ritual
  and that Python can call so far, 7 names in all: 'isValid', 'hasNext',
  'next', 'peekNext', 'regularExpression', 'matchType', 'matchOptions'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QRegularExpressionMatchIterator::~QRegularExpressionMatchIterator()':
    the destructor: Python removes its C++ QRegularExpressionMatchIterator by
    it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 15 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QRegularExpressionMatchIterator is created at the first use, not
    by 'QRegularExpressionMatchIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRegularExpressionMatchIterator back gives a copy the
    ritual made for Python, in a new cute QRegularExpressionMatchIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRegularExpressionMatchIterator'

  #  Qt's '~QRegularExpressionMatchIterator()'. Naming it makes this a value
  #  class: Python owns every C++ QRegularExpressionMatchIterator behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QRegularExpressionMatchIteratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRegularExpressionMatchIterator::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html#isValid
    """
    #  bool QRegularExpressionMatchIterator::isValid() const
    return self.uglySide.call(
        'ritual_ZNK31QRegularExpressionMatchIterator7isValidEv',
    )

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QRegularExpressionMatchIterator::hasNext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html#hasNext
    """
    #  bool QRegularExpressionMatchIterator::hasNext() const
    return self.uglySide.call(
        'ritual_ZNK31QRegularExpressionMatchIterator7hasNextEv',
    )

  def peekNext(self) -> QRegularExpressionMatch:
    """
    Calls Qt's 'QRegularExpressionMatch
    QRegularExpressionMatchIterator::peekNext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html#peekNext

    Returns
    -------

    QRegularExpressionMatch
      A new cute QRegularExpressionMatch around the copy Qt gave back. Python
      owns it.
    """
    #  QRegularExpressionMatch QRegularExpressionMatchIterator::peekNext()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QRegularExpressionMatchIterator8peekNextEv',
    )
    from . import QRegularExpressionMatch
    return QRegularExpressionMatch._cuteOwning(address)

  def regularExpression(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QRegularExpressionMatchIterator::regularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression
    #      QRegularExpressionMatchIterator::regularExpression() const
    address = self.uglySide.call(
        'ritual_ZNK31QRegularExpressionMatchIterator17regularExpressionEv',
    )
    return QRegularExpression._cuteOwning(address)

  def matchType(self) -> QRegularExpression.MatchType:
    """
    Calls Qt's 'QRegularExpression::MatchType
    QRegularExpressionMatchIterator::matchType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html#matchType

    Returns
    -------

    QRegularExpression.MatchType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRegularExpression.MatchType(number)' gives.
    """
    #  QRegularExpression::MatchType
    #      QRegularExpressionMatchIterator::matchType() const
    return QRegularExpression.MatchType(self.uglySide.call(
        'ritual_ZNK31QRegularExpressionMatchIterator9matchTypeEv',
    ))

  def matchOptions(self) -> QRegularExpression.MatchOptions:
    """
    Calls Qt's 'QRegularExpression::MatchOptions
    QRegularExpressionMatchIterator::matchOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html#matchOptions

    Returns
    -------

    QRegularExpression.MatchOptions
      The value standing for the combination Qt gave back.
    """
    #  QRegularExpression::MatchOptions
    #      QRegularExpressionMatchIterator::matchOptions() const
    return QRegularExpression.MatchOptions(self.uglySide.call(
        'ritual_ZNK31QRegularExpressionMatchIterator12matchOptionsEv',
    ))

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpressionMatchIterator::QRegularExpressionMatchIterator()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html
    """
    #  QRegularExpressionMatchIterator::QRegularExpressionMatchIterator()
    self._noteCreation(QRegularExpressionMatchIterator, lambda: Rituals.call(
        'ritual_ZN31QRegularExpressionMatchIteratorC1Ev',
    ))

  @overload(THIS)
  def __init__(self, iterator: QRegularExpressionMatchIterator) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpressionMatchIterator::QRegularExpressionMatchIterator(const
    QRegularExpressionMatchIterator &iterator)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html

    Parameters
    ----------

    iterator : QRegularExpressionMatchIterator
      Passed on as a value: Qt reads the C++ QRegularExpressionMatchIterator,
      which stays Python's own.
    """
    #  QRegularExpressionMatchIterator::QRegularExpressionMatchIterator(const
    #      QRegularExpressionMatchIterator &iterator)
    self._noteCreation(QRegularExpressionMatchIterator, lambda: Rituals.call(
        'ritual_ZN31QRegularExpressionMatchIteratorC1ERKS_',
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

  def next(self) -> QRegularExpressionMatch:
    """
    Calls Qt's 'QRegularExpressionMatch
    QRegularExpressionMatchIterator::next()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionmatchiterator.html#next

    Returns
    -------

    QRegularExpressionMatch
      A new cute QRegularExpressionMatch around the copy Qt gave back. Python
      owns it.
    """
    #  QRegularExpressionMatch QRegularExpressionMatchIterator::next()
    address = self.uglySide.call(
        'ritual_ZN31QRegularExpressionMatchIterator4nextEv',
    )
    from . import QRegularExpressionMatch
    return QRegularExpressionMatch._cuteOwning(address)
