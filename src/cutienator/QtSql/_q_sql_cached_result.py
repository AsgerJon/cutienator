"""
QSqlCachedResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlcachedresult_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSqlCachedResult to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSql, QSqlResult

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QSqlCachedResultPrivate


class QSqlCachedResult(QSqlResult):
  """
  The cute side of Qt's QSqlCachedResult: a plain Python object standing in
  front of one C++ QSqlCachedResult.

  It is built on the cute 'QSqlResult', as Qt's QSqlCachedResult is built on
  Qt's QSqlResult, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlCachedResult that has a ritual and that Python
  can call so far, 15 names in all: 'd_func', 'init', 'cleanup',
  'clearValues', 'data', 'isNull', 'fetch', 'fetchNext', 'fetchPrevious',
  'fetchFirst', 'fetchLast', 'colCount', 'detachFromResultSet',
  'setNumericalPrecisionPolicy', 'cacheNext'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSqlCachedResultPrivate *QSqlCachedResult::d_func() const':
    takes in Python what 'QSqlCachedResultPrivate
    *QSqlCachedResult::d_func()' takes.
  - Qt's 'bool QSqlCachedResult::gotoNext(ValueCache &values, int index)':
    takes a type Python has no way to hand over yet.
  - Qt's 'ValueCache &QSqlCachedResult::cache()': gives a type Python has no
    way to take yet.
  - Qt's 'void QSqlCachedResult::virtual_hook(int id, void *data)': names
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QSqlCachedResult is created at the first use, not by
    'QSqlCachedResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlCachedResult.
  - Each name of Qt's QSqlCachedResult that has no cute function yet,
    '__init__', 'cache', 'gotoNext', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlCachedResult'

  #  The functions Qt calls itself that QSqlCachedResult is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'gotoNext': (
          'bool QSqlCachedResult::gotoNext(ValueCache &, int)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def colCount(self) -> int:
    """
    Calls Qt's 'int QSqlCachedResult::colCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#colCount
    """
    #  int QSqlCachedResult::colCount() const
    return self.uglySide.call('ritual_ZNK16QSqlCachedResult8colCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSql.NumericalPrecisionPolicy)
  def setNumericalPrecisionPolicy(
      self,
      policy: QSql.NumericalPrecisionPolicy,
  ) -> None:
    """
    Calls Qt's 'void QSqlCachedResult::setNumericalPrecisionPolicy(QSql::
    NumericalPrecisionPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresult.html#setNumericalPrecisionPolicy

    Parameters
    ----------

    policy : QSql.NumericalPrecisionPolicy
      Passed on as its number.
    """
    #  void QSqlCachedResult::setNumericalPrecisionPolicy(QSql::
    #      NumericalPrecisionPolicy policy)
    ritual = (
        'ritual_ZN16QSqlCachedResult27setNumericalPrecisionPolicyEN4QSql24N'
        'umericalPrecisionPolicyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSqlCachedResult27setNumericalPrecisionPolicyEN4Q'
          'Sql24NumericalPrecisionPolicyE')
    self.uglySide.call(ritual, policy.value)

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
    Qt's 'QSqlCachedResult::QSqlCachedResult(QSqlCachedResultPrivate &d)':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QSqlCachedResult.__init__' has no cute function yet. Qt's "
        "'QSqlCachedResult::QSqlCachedResult(QSqlCachedResultPrivate &d)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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

  def d_func(self) -> Optional[QSqlCachedResultPrivate]:
    """
    Calls Qt's 'QSqlCachedResultPrivate *QSqlCachedResult::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#d_func

    Returns
    -------

    Optional[QSqlCachedResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlCachedResultPrivate *QSqlCachedResult::d_func()
    address = self.uglySide.call('ritual_ZN16QSqlCachedResult6d_funcEv')
    from . import QSqlCachedResultPrivate
    return QSqlCachedResultPrivate._cuteAt(address)

  @overload(int)
  def init(self, colCount: int) -> None:
    """
    Calls Qt's 'void QSqlCachedResult::init(int colCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#init

    Parameters
    ----------

    colCount : int
      Passed on as it is.
    """
    #  void QSqlCachedResult::init(int colCount)
    self.uglySide.call('ritual_ZN16QSqlCachedResult4initEi', colCount)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QSqlCachedResult::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#cleanup
    """
    #  void QSqlCachedResult::cleanup()
    self.uglySide.call('ritual_ZN16QSqlCachedResult7cleanupEv')

  def clearValues(self) -> None:
    """
    Calls Qt's 'void QSqlCachedResult::clearValues()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#clearValues
    """
    #  void QSqlCachedResult::clearValues()
    self.uglySide.call('ritual_ZN16QSqlCachedResult11clearValuesEv')

  @overload(int)
  def data(self, i: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlCachedResult::data(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#data

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlCachedResult::data(int i)
    ritual = 'ritual_ZN16QSqlCachedResult4dataEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult4dataEi'
    address = self.uglySide.call(ritual, i)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isNull(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResult::isNull(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#isNull

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlCachedResult::isNull(int i)
    ritual = 'ritual_ZN16QSqlCachedResult6isNullEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult6isNullEi'
    return self.uglySide.call(ritual, i)

  @overload(int)
  def fetch(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResult::fetch(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#fetch

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlCachedResult::fetch(int i)
    ritual = 'ritual_ZN16QSqlCachedResult5fetchEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult5fetchEi'
    return self.uglySide.call(ritual, i)

  def fetchNext(self) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResult::fetchNext()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#fetchNext
    """
    #  bool QSqlCachedResult::fetchNext()
    ritual = 'ritual_ZN16QSqlCachedResult9fetchNextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult9fetchNextEv'
    return self.uglySide.call(ritual)

  def fetchPrevious(self) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResult::fetchPrevious()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresult.html#fetchPrevious
    """
    #  bool QSqlCachedResult::fetchPrevious()
    ritual = 'ritual_ZN16QSqlCachedResult13fetchPreviousEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult13fetchPreviousEv'
    return self.uglySide.call(ritual)

  def fetchFirst(self) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResult::fetchFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#fetchFirst
    """
    #  bool QSqlCachedResult::fetchFirst()
    ritual = 'ritual_ZN16QSqlCachedResult10fetchFirstEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult10fetchFirstEv'
    return self.uglySide.call(ritual)

  def fetchLast(self) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResult::fetchLast()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#fetchLast
    """
    #  bool QSqlCachedResult::fetchLast()
    ritual = 'ritual_ZN16QSqlCachedResult9fetchLastEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult9fetchLastEv'
    return self.uglySide.call(ritual)

  def detachFromResultSet(self) -> None:
    """
    Calls Qt's 'void QSqlCachedResult::detachFromResultSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlcachedresult.html#detachFromResultSet
    """
    #  void QSqlCachedResult::detachFromResultSet()
    ritual = 'ritual_ZN16QSqlCachedResult19detachFromResultSetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSqlCachedResult19detachFromResultSetEv'
    self.uglySide.call(ritual)

  def cacheNext(self) -> bool:
    """
    Calls Qt's 'bool QSqlCachedResult::cacheNext()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlcachedresult.html#cacheNext
    """
    #  bool QSqlCachedResult::cacheNext()
    return self.uglySide.call('ritual_ZN16QSqlCachedResult9cacheNextEv')

  @staticmethod
  def cache(*__, **_) -> Never:
    """
    Qt's 'ValueCache &QSqlCachedResult::cache()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSqlCachedResult.cache' has no cute function yet. Qt's "
        "'ValueCache &QSqlCachedResult::cache()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def gotoNext(*__, **_) -> Never:
    """
    Qt's 'bool QSqlCachedResult::gotoNext(ValueCache &values, int index)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlCachedResult.gotoNext' has no cute function yet. Qt's 'bool "
        "QSqlCachedResult::gotoNext(ValueCache &values, int index)': takes "
        "a type Python has no way to hand over yet.")
