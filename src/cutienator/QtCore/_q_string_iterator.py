"""
QStringIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qstringiterator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QStringIterator to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStringIterator: a plain Python object standing in
  front of one C++ QStringIterator.

  C++ hands a QStringIterator around as a copy, so every C++ QStringIterator
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStringIterator that has a ritual and that Python
  can call so far, 20 names in all: 'less', 'position', 'index',
  'setPosition', 'hasNext', 'advance', 'advanceUnchecked',
  'peekNextUnchecked', 'peekNext', 'nextUnchecked', 'next',
  'nextOrRawCodeUnit', 'hasPrevious', 'recede', 'recedeUnchecked',
  'peekPreviousUnchecked', 'peekPrevious', 'previousUnchecked', 'previous',
  'previousOrRawCodeUnit'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStringIterator::~QStringIterator()': the destructor: Python
    removes its C++ QStringIterator by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QStringIterator is created at the first use, not by
    'QStringIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStringIterator back gives a copy the ritual made for
    Python, in a new cute QStringIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QChar, QChar)
  @overload(QChar, NoneType)
  @overload(NoneType, QChar)
  @overload(NoneType, NoneType)
  def less(lhs: Optional[QChar], rhs: Optional[QChar]) -> bool:
    """
    Calls Qt's 'bool QStringIterator::less(const QChar *lhs, const QChar
    *rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#less

    Parameters
    ----------

    lhs : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rhs : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStringIterator::less(const QChar *lhs, const QChar *rhs)
    return Rituals.call(
        'ritual_ZN15QStringIterator4lessEPK5QCharS2_',
        CuteMixin._addressOf(lhs), CuteMixin._addressOf(rhs),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringIterator'

  #  Qt's '~QStringIterator()'. Naming it makes this a value class: Python
  #  owns every C++ QStringIterator behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QStringIteratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> Optional[QChar]:
    """
    Calls Qt's 'QString::const_iterator QStringIterator::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#position

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QString::const_iterator QStringIterator::position() const
    address = self.uglySide.call('ritual_ZNK15QStringIterator8positionEv')
    from . import QChar
    return QChar._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'qsizetype QStringIterator::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#index
    """
    #  qsizetype QStringIterator::index() const
    return self.uglySide.call('ritual_ZNK15QStringIterator5indexEv')

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QStringIterator::hasNext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#hasNext
    """
    #  bool QStringIterator::hasNext() const
    return self.uglySide.call('ritual_ZNK15QStringIterator7hasNextEv')

  def peekNextUnchecked(self) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::peekNextUnchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#peekNextUnchecked
    """
    #  char32_t QStringIterator::peekNextUnchecked() const
    return self.uglySide.call(
        'ritual_ZNK15QStringIterator17peekNextUncheckedEv',
    )

  @overload()
  @overload(int)
  def peekNext(self, invalidAs: int = 65533) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::peekNext(char32_t invalidAs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#peekNext

    Parameters
    ----------

    invalidAs : int
      Passed on as it is. May be left out, as in Qt: it is then 65533.
    """
    #  char32_t QStringIterator::peekNext(char32_t invalidAs) const
    return self.uglySide.call(
        'ritual_ZNK15QStringIterator8peekNextEDi', invalidAs,
    )

  def hasPrevious(self) -> bool:
    """
    Calls Qt's 'bool QStringIterator::hasPrevious() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#hasPrevious
    """
    #  bool QStringIterator::hasPrevious() const
    return self.uglySide.call('ritual_ZNK15QStringIterator11hasPreviousEv')

  def peekPreviousUnchecked(self) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::peekPreviousUnchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#peekPreviousUnchecked
    """
    #  char32_t QStringIterator::peekPreviousUnchecked() const
    return self.uglySide.call(
        'ritual_ZNK15QStringIterator21peekPreviousUncheckedEv',
    )

  @overload()
  @overload(int)
  def peekPrevious(self, invalidAs: int = 65533) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::peekPrevious(char32_t invalidAs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#peekPrevious

    Parameters
    ----------

    invalidAs : int
      Passed on as it is. May be left out, as in Qt: it is then 65533.
    """
    #  char32_t QStringIterator::peekPrevious(char32_t invalidAs) const
    return self.uglySide.call(
        'ritual_ZNK15QStringIterator12peekPreviousEDi', invalidAs,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QChar)
  @overload(NoneType)
  def setPosition(self, position: Optional[QChar]) -> None:
    """
    Calls Qt's 'void QStringIterator::setPosition(QString::const_iterator
    position)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#setPosition

    Parameters
    ----------

    position : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStringIterator::setPosition(QString::const_iterator position)
    self.uglySide.call(
        'ritual_ZN15QStringIterator11setPositionEPK5QChar',
        self._addressOf(position),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, int)
  def __init__(self, string: str, idx: int = 0) -> None:
    """
    Notes what was given, for Qt's
    'QStringIterator::QStringIterator(QStringView string, qsizetype idx)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#QStringIterator

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    idx : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QStringIterator::QStringIterator(QStringView string, qsizetype idx)
    self._noteCreation(QStringIterator, lambda: Rituals.call(
        'ritual_ZN15QStringIteratorC1E11QStringViewx', string, idx,
    ))

  @overload(QChar, QChar)
  @overload(QChar, NoneType)
  @overload(NoneType, QChar)
  @overload(NoneType, NoneType)
  def __init__(self, begin: Optional[QChar], end: Optional[QChar]) -> None:
    """
    Notes what was given, for Qt's 'QStringIterator::QStringIterator(const
    QChar *begin, const QChar *end)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#QStringIterator

    Parameters
    ----------

    begin : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    end : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStringIterator::QStringIterator(const QChar *begin, const QChar *end)
    self._noteCreation(QStringIterator, lambda: Rituals.call(
        'ritual_ZN15QStringIteratorC1EPK5QCharS2_',
        self._addressOf(begin), self._addressOf(end),
    ))

  @overload(QChar, int, QChar)
  @overload(QChar, int, NoneType)
  @overload(NoneType, int, QChar)
  @overload(NoneType, int, NoneType)
  def __init__(
      self,
      begin: Optional[QChar],
      idx: int,
      end: Optional[QChar],
  ) -> None:
    """
    Notes what was given, for Qt's 'QStringIterator::QStringIterator(const
    QChar *begin, qsizetype idx, const QChar *end)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#QStringIterator

    Parameters
    ----------

    begin : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.

    end : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStringIterator::QStringIterator(const QChar *begin, qsizetype idx,
    #      const QChar *end)
    self._noteCreation(QStringIterator, lambda: Rituals.call(
        'ritual_ZN15QStringIteratorC1EPK5QCharxS2_',
        self._addressOf(begin), idx, self._addressOf(end),
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

  def advance(self) -> None:
    """
    Calls Qt's 'void QStringIterator::advance()'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#advance
    """
    #  void QStringIterator::advance()
    self.uglySide.call('ritual_ZN15QStringIterator7advanceEv')

  def advanceUnchecked(self) -> None:
    """
    Calls Qt's 'void QStringIterator::advanceUnchecked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#advanceUnchecked
    """
    #  void QStringIterator::advanceUnchecked()
    self.uglySide.call('ritual_ZN15QStringIterator16advanceUncheckedEv')

  def nextUnchecked(self) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::nextUnchecked()'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#nextUnchecked
    """
    #  char32_t QStringIterator::nextUnchecked()
    return self.uglySide.call('ritual_ZN15QStringIterator13nextUncheckedEv')

  @overload()
  @overload(int)
  def next(self, invalidAs: int = 65533) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::next(char32_t invalidAs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#next

    Parameters
    ----------

    invalidAs : int
      Passed on as it is. May be left out, as in Qt: it is then 65533.
    """
    #  char32_t QStringIterator::next(char32_t invalidAs)
    return self.uglySide.call(
        'ritual_ZN15QStringIterator4nextEDi', invalidAs,
    )

  def nextOrRawCodeUnit(self) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::nextOrRawCodeUnit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#nextOrRawCodeUnit
    """
    #  char32_t QStringIterator::nextOrRawCodeUnit()
    return self.uglySide.call(
        'ritual_ZN15QStringIterator17nextOrRawCodeUnitEv',
    )

  def recede(self) -> None:
    """
    Calls Qt's 'void QStringIterator::recede()'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#recede
    """
    #  void QStringIterator::recede()
    self.uglySide.call('ritual_ZN15QStringIterator6recedeEv')

  def recedeUnchecked(self) -> None:
    """
    Calls Qt's 'void QStringIterator::recedeUnchecked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#recedeUnchecked
    """
    #  void QStringIterator::recedeUnchecked()
    self.uglySide.call('ritual_ZN15QStringIterator15recedeUncheckedEv')

  def previousUnchecked(self) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::previousUnchecked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#previousUnchecked
    """
    #  char32_t QStringIterator::previousUnchecked()
    return self.uglySide.call(
        'ritual_ZN15QStringIterator17previousUncheckedEv',
    )

  @overload()
  @overload(int)
  def previous(self, invalidAs: int = 65533) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::previous(char32_t invalidAs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringiterator.html#previous

    Parameters
    ----------

    invalidAs : int
      Passed on as it is. May be left out, as in Qt: it is then 65533.
    """
    #  char32_t QStringIterator::previous(char32_t invalidAs)
    return self.uglySide.call(
        'ritual_ZN15QStringIterator8previousEDi', invalidAs,
    )

  def previousOrRawCodeUnit(self) -> int:
    """
    Calls Qt's 'char32_t QStringIterator::previousOrRawCodeUnit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringiterator.html#previousOrRawCodeUnit
    """
    #  char32_t QStringIterator::previousOrRawCodeUnit()
    return self.uglySide.call(
        'ritual_ZN15QStringIterator21previousOrRawCodeUnitEv',
    )
