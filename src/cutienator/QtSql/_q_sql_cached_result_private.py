"""
QSqlCachedResultPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlcachedresult_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSqlCachedResultPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSqlResultPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSqlCachedResult


class QSqlCachedResultPrivate(QSqlResultPrivate):
  """
  The cute side of Qt's QSqlCachedResultPrivate: a plain Python object
  standing in front of one C++ QSqlCachedResultPrivate.

  It is built on the cute 'QSqlResultPrivate', as Qt's
  QSqlCachedResultPrivate is built on Qt's QSqlResultPrivate, and has
  everything that class has.

  C++ hands a QSqlCachedResultPrivate around as a copy, so every C++
  QSqlCachedResultPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlCachedResultPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'q_func', 'canSeek', 'cacheCount',
  'init', 'cleanup', 'nextIndex', 'revertLast'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSqlCachedResult *QSqlCachedResultPrivate::q_func() const':
    takes in Python what 'QSqlCachedResult
    *QSqlCachedResultPrivate::q_func()' takes.
  - Qt's 'QSqlCachedResultPrivate::~QSqlCachedResultPrivate()': the
    destructor: Python removes its C++ QSqlCachedResultPrivate by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QSqlCachedResultPrivate is created at the first use, not by
    'QSqlCachedResultPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlCachedResultPrivate back gives a copy the ritual
    made for Python, in a new cute QSqlCachedResultPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlCachedResultPrivate'

  #  A C++ QSqlCachedResultPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlCachedResultPrivate'

  #  Qt's '~QSqlCachedResultPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QSqlCachedResultPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QSqlCachedResultPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def canSeek(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResultPrivate::canSeek(int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresultprivate.html#canSeek

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlCachedResultPrivate::canSeek(int i) const
    return self.uglySide.call(
        'ritual_ZNK23QSqlCachedResultPrivate7canSeekEi', i,
    )

  def cacheCount(self) -> int:
    """
    Calls Qt's 'int QSqlCachedResultPrivate::cacheCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresultprivate.html#cacheCount
    """
    #  int QSqlCachedResultPrivate::cacheCount() const
    return self.uglySide.call(
        'ritual_ZNK23QSqlCachedResultPrivate10cacheCountEv',
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

  def q_func(self) -> Optional[QSqlCachedResult]:
    """
    Calls Qt's 'QSqlCachedResult *QSqlCachedResultPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresultprivate.html#q_func

    Returns
    -------

    Optional[QSqlCachedResult]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlCachedResult *QSqlCachedResultPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QSqlCachedResultPrivate6q_funcEv',
    )
    from . import QSqlCachedResult
    return QSqlCachedResult._cuteAt(address)

  @overload(int, bool)
  def init(self, count: int, fo: bool) -> None:
    """
    Calls Qt's 'void QSqlCachedResultPrivate::init(int count, bool fo)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresultprivate.html#init

    Parameters
    ----------

    count : int
      Passed on as it is.

    fo : bool
      Passed on as it is.
    """
    #  void QSqlCachedResultPrivate::init(int count, bool fo)
    self.uglySide.call(
        'ritual_ZN23QSqlCachedResultPrivate4initEib', count, fo,
    )

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QSqlCachedResultPrivate::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresultprivate.html#cleanup
    """
    #  void QSqlCachedResultPrivate::cleanup()
    self.uglySide.call('ritual_ZN23QSqlCachedResultPrivate7cleanupEv')

  def nextIndex(self) -> int:
    """
    Calls Qt's 'int QSqlCachedResultPrivate::nextIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresultprivate.html#nextIndex
    """
    #  int QSqlCachedResultPrivate::nextIndex()
    return self.uglySide.call(
        'ritual_ZN23QSqlCachedResultPrivate9nextIndexEv',
    )

  def revertLast(self) -> None:
    """
    Calls Qt's 'void QSqlCachedResultPrivate::revertLast()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresultprivate.html#revertLast
    """
    #  void QSqlCachedResultPrivate::revertLast()
    self.uglySide.call('ritual_ZN23QSqlCachedResultPrivate10revertLastEv')
