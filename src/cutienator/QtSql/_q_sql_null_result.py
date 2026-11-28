"""
QSqlNullResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlnulldriver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSqlNullResult to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSql, QSqlResult

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QSqlDriver, QSqlError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlDriver = WAIT['QSqlDriver']
  QSqlError = WAIT['QSqlError']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlNullResult(QSqlResult):
  """
  The cute side of Qt's QSqlNullResult: a plain Python object standing in
  front of one C++ QSqlNullResult.

  It is built on the cute 'QSqlResult', as Qt's QSqlNullResult is built on
  Qt's QSqlResult, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlNullResult that has a ritual and that Python can
  call so far, 18 names in all: 'data', 'reset', 'fetch', 'fetchFirst',
  'fetchLast', 'isNull', 'size', 'numRowsAffected', 'setAt', 'setActive',
  'setLastError', 'setQuery', 'setSelect', 'setForwardOnly', 'exec',
  'prepare', 'savePrepare', 'bindValue'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QSqlNullResult is created at the first use, not by
    'QSqlNullResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlNullResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlNullResult'

  #  A C++ QSqlNullResult Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlNullResult'

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

  @overload(int)
  def setAt(self, a0: int) -> None:
    """
    Calls Qt's 'void QSqlNullResult::setAt(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#setAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSqlNullResult::setAt(int a0)
    ritual = 'ritual_ZN14QSqlNullResult5setAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult5setAtEi'
    self.uglySide.call(ritual, a0)

  @overload(bool)
  def setActive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSqlNullResult::setActive(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#setActive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSqlNullResult::setActive(bool a0)
    ritual = 'ritual_ZN14QSqlNullResult9setActiveEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult9setActiveEb'
    self.uglySide.call(ritual, a0)

  @overload(QSqlError)
  def setLastError(self, a0: QSqlError) -> None:
    """
    Calls Qt's 'void QSqlNullResult::setLastError(const QSqlError &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#setLastError

    Parameters
    ----------

    a0 : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  void QSqlNullResult::setLastError(const QSqlError &a0)
    ritual = 'ritual_ZN14QSqlNullResult12setLastErrorERK9QSqlError'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult12setLastErrorERK9QSqlError'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(str)
  def setQuery(self, a0: str) -> None:
    """
    Calls Qt's 'void QSqlNullResult::setQuery(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#setQuery

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlNullResult::setQuery(const QString &a0)
    ritual = 'ritual_ZN14QSqlNullResult8setQueryERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult8setQueryERK7QString'
    self.uglySide.call(ritual, a0)

  @overload(bool)
  def setSelect(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSqlNullResult::setSelect(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#setSelect

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSqlNullResult::setSelect(bool a0)
    ritual = 'ritual_ZN14QSqlNullResult9setSelectEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult9setSelectEb'
    self.uglySide.call(ritual, a0)

  @overload(bool)
  def setForwardOnly(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSqlNullResult::setForwardOnly(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#setForwardOnly

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSqlNullResult::setForwardOnly(bool a0)
    ritual = 'ritual_ZN14QSqlNullResult14setForwardOnlyEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult14setForwardOnlyEb'
    self.uglySide.call(ritual, a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSqlDriver)
  @overload(NoneType)
  def __init__(self, d: Optional[QSqlDriver]) -> None:
    """
    Notes what was given, for Qt's 'QSqlNullResult::QSqlNullResult(const
    QSqlDriver *d)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#QSqlNullResult

    Parameters
    ----------

    d : Optional[QSqlDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSqlNullResult::QSqlNullResult(const QSqlDriver *d)
    self._noteCreation(QSqlNullResult, lambda: Rituals.call(
        'ritual_ZN14QSqlNullResultC1EPK10QSqlDriver', self._addressOf(d),
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

  @overload(int)
  def data(self, a0: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlNullResult::data(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#data

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlNullResult::data(int a0)
    ritual = 'ritual_ZN14QSqlNullResult4dataEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult4dataEi'
    address = self.uglySide.call(ritual, a0)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def reset(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::reset(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#reset

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlNullResult::reset(const QString &a0)
    ritual = 'ritual_ZN14QSqlNullResult5resetERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult5resetERK7QString'
    return self.uglySide.call(ritual, a0)

  @overload(int)
  def fetch(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::fetch(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#fetch

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QSqlNullResult::fetch(int a0)
    ritual = 'ritual_ZN14QSqlNullResult5fetchEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult5fetchEi'
    return self.uglySide.call(ritual, a0)

  def fetchFirst(self) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::fetchFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#fetchFirst
    """
    #  bool QSqlNullResult::fetchFirst()
    ritual = 'ritual_ZN14QSqlNullResult10fetchFirstEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult10fetchFirstEv'
    return self.uglySide.call(ritual)

  def fetchLast(self) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::fetchLast()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#fetchLast
    """
    #  bool QSqlNullResult::fetchLast()
    ritual = 'ritual_ZN14QSqlNullResult9fetchLastEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult9fetchLastEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def isNull(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::isNull(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#isNull

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QSqlNullResult::isNull(int a0)
    ritual = 'ritual_ZN14QSqlNullResult6isNullEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult6isNullEi'
    return self.uglySide.call(ritual, a0)

  def size(self) -> int:
    """
    Calls Qt's 'int QSqlNullResult::size()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#size
    """
    #  int QSqlNullResult::size()
    ritual = 'ritual_ZN14QSqlNullResult4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult4sizeEv'
    return self.uglySide.call(ritual)

  def numRowsAffected(self) -> int:
    """
    Calls Qt's 'int QSqlNullResult::numRowsAffected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlnullresult.html#numRowsAffected
    """
    #  int QSqlNullResult::numRowsAffected()
    ritual = 'ritual_ZN14QSqlNullResult15numRowsAffectedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult15numRowsAffectedEv'
    return self.uglySide.call(ritual)

  def exec(self) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#exec
    """
    #  bool QSqlNullResult::exec()
    ritual = 'ritual_ZN14QSqlNullResult4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult4execEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def prepare(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::prepare(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#prepare

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlNullResult::prepare(const QString &a0)
    ritual = 'ritual_ZN14QSqlNullResult7prepareERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult7prepareERK7QString'
    return self.uglySide.call(ritual, a0)

  @overload(str)
  def savePrepare(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QSqlNullResult::savePrepare(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#savePrepare

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlNullResult::savePrepare(const QString &a0)
    ritual = 'ritual_ZN14QSqlNullResult11savePrepareERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullResult11savePrepareERK7QString'
    return self.uglySide.call(ritual, a0)

  @overload(int, QVariant, QSql.ParamType)
  def bindValue(self, a0: int, a1: QVariant, a2: QSql.ParamType) -> None:
    """
    Calls Qt's 'void QSqlNullResult::bindValue(int a0, const QVariant &a1,
    QSql::ParamType a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#bindValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a2 : QSql.ParamType
      Passed on as its number.
    """
    #  void QSqlNullResult::bindValue(int a0, const QVariant &a1,
    #      QSql::ParamType a2)
    ritual = (
        'ritual_ZN14QSqlNullResult9bindValueEiRK8QVariant6QFlagsIN4QSql13Pa'
        'ramTypeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlNullResult9bindValueEiRK8QVariant6QFlagsIN4QS'
          'ql13ParamTypeFlagEE')
    self.uglySide.call(ritual, a0, self._valueOf(a1), a2.value)

  @overload(str, QVariant, QSql.ParamType)
  def bindValue(self, a0: str, a1: QVariant, a2: QSql.ParamType) -> None:
    """
    Calls Qt's 'void QSqlNullResult::bindValue(const QString &a0, const
    QVariant &a1, QSql::ParamType a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnullresult.html#bindValue

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a2 : QSql.ParamType
      Passed on as its number.
    """
    #  void QSqlNullResult::bindValue(const QString &a0, const QVariant &a1,
    #      QSql::ParamType a2)
    ritual = (
        'ritual_ZN14QSqlNullResult9bindValueERK7QStringRK8QVariant6QFlagsIN'
        '4QSql13ParamTypeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlNullResult9bindValueERK7QStringRK8QVariant6QF'
          'lagsIN4QSql13ParamTypeFlagEE')
    self.uglySide.call(ritual, a0, self._valueOf(a1), a2.value)
