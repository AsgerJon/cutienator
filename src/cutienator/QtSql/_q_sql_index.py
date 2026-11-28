"""
QSqlIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlindex.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSqlRecord

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QSqlField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlField = WAIT['QSqlField']


class QSqlIndex(QSqlRecord):
  """
  The cute side of Qt's QSqlIndex: a plain Python object standing in front of
  one C++ QSqlIndex.

  It is built on the cute 'QSqlRecord', as Qt's QSqlIndex is built on Qt's
  QSqlRecord, and has everything that class has.

  C++ hands a QSqlIndex around as a copy, so every C++ QSqlIndex behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlIndex that has a ritual and that Python can call
  so far, 7 names in all: 'setCursorName', 'cursorName', 'setName', 'name',
  'append', 'isDescending', 'setDescending'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSqlIndex::QSqlIndex(QSqlIndex &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QSqlIndex::~QSqlIndex()': the destructor: Python removes its C++
    QSqlIndex by it, and has no other use for it.
  - Qt's 'QSqlIndex &QSqlIndex::operator=(const QSqlIndex &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QSqlIndex &QSqlIndex::operator=(QSqlIndex &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QSqlIndex::swap(QSqlIndex &other)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QSqlIndex is created at the first use, not by 'QSqlIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlIndex back gives a copy the ritual made for
    Python, in a new cute QSqlIndex.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlIndex'

  #  Qt's '~QSqlIndex()'. Naming it makes this a value class: Python owns
  #  every C++ QSqlIndex behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSqlIndexD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cursorName(self) -> str:
    """
    Calls Qt's 'QString QSqlIndex::cursorName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#cursorName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlIndex::cursorName() const
    return self.uglySide.call('ritual_ZNK9QSqlIndex10cursorNameEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QSqlIndex::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlIndex::name() const
    return self.uglySide.call('ritual_ZNK9QSqlIndex4nameEv')

  @overload(int)
  def isDescending(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlIndex::isDescending(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#isDescending

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlIndex::isDescending(int i) const
    return self.uglySide.call('ritual_ZNK9QSqlIndex12isDescendingEi', i)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCursorName(self, cursorName: str) -> None:
    """
    Calls Qt's 'void QSqlIndex::setCursorName(const QString &cursorName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#setCursorName

    Parameters
    ----------

    cursorName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlIndex::setCursorName(const QString &cursorName)
    self.uglySide.call(
        'ritual_ZN9QSqlIndex13setCursorNameERK7QString', cursorName,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QSqlIndex::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlIndex::setName(const QString &name)
    self.uglySide.call('ritual_ZN9QSqlIndex7setNameERK7QString', name)

  @overload(int, bool)
  def setDescending(self, i: int, desc: bool) -> None:
    """
    Calls Qt's 'void QSqlIndex::setDescending(int i, bool desc)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#setDescending

    Parameters
    ----------

    i : int
      Passed on as it is.

    desc : bool
      Passed on as it is.
    """
    #  void QSqlIndex::setDescending(int i, bool desc)
    self.uglySide.call('ritual_ZN9QSqlIndex13setDescendingEib', i, desc)

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
  @overload(str)
  @overload(str, str)
  def __init__(self, cursorName: str = '', name: str = '') -> None:
    """
    Notes what was given, for Qt's 'QSqlIndex::QSqlIndex(const QString
    &cursorName, const QString &name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#QSqlIndex

    Parameters
    ----------

    cursorName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QSqlIndex::QSqlIndex(const QString &cursorName, const QString &name)
    self._noteCreation(QSqlIndex, lambda: Rituals.call(
        'ritual_ZN9QSqlIndexC1ERK7QStringS2_', cursorName, name,
    ))

  @overload(THIS)
  def __init__(self, other: QSqlIndex) -> None:
    """
    Notes what was given, for Qt's 'QSqlIndex::QSqlIndex(const QSqlIndex
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#QSqlIndex

    Parameters
    ----------

    other : QSqlIndex
      Passed on as a value: Qt reads the C++ QSqlIndex, which stays Python's
      own.
    """
    #  QSqlIndex::QSqlIndex(const QSqlIndex &other)
    self._noteCreation(QSqlIndex, lambda: Rituals.call(
        'ritual_ZN9QSqlIndexC1ERKS_', self._valueOf(other),
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

  @overload(QSqlField)
  def append(self, field: QSqlField) -> None:
    """
    Calls Qt's 'void QSqlIndex::append(const QSqlField &field)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#append

    Parameters
    ----------

    field : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.
    """
    #  void QSqlIndex::append(const QSqlField &field)
    self.uglySide.call(
        'ritual_ZN9QSqlIndex6appendERK9QSqlField', self._valueOf(field),
    )

  @overload(QSqlField, bool)
  def append(self, field: QSqlField, desc: bool) -> None:
    """
    Calls Qt's 'void QSqlIndex::append(const QSqlField &field, bool desc)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlindex.html#append

    Parameters
    ----------

    field : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.

    desc : bool
      Passed on as it is.
    """
    #  void QSqlIndex::append(const QSqlField &field, bool desc)
    self.uglySide.call(
        'ritual_ZN9QSqlIndex6appendERK9QSqlFieldb',
        self._valueOf(field), desc,
    )
