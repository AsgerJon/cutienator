"""
QSqlRelation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlrelationaltablemodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSqlRelation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlRelation: a plain Python object standing in front
  of one C++ QSqlRelation.

  C++ hands a QSqlRelation around as a copy, so every C++ QSqlRelation behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlRelation that has a ritual and that Python can
  call so far, 4 names in all: 'tableName', 'indexColumn', 'displayColumn',
  'isValid'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSqlRelation::swap(QSqlRelation &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QSqlRelation::~QSqlRelation()': the destructor: Python removes its
    C++ QSqlRelation by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSqlRelation is created at the first use, not by
    'QSqlRelation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlRelation back gives a copy the ritual made for
    Python, in a new cute QSqlRelation.
  - Each name of Qt's QSqlRelation that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlRelation'

  #  Qt's '~QSqlRelation()'. Naming it makes this a value class: Python owns
  #  every C++ QSqlRelation behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QSqlRelationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def tableName(self) -> str:
    """
    Calls Qt's 'QString QSqlRelation::tableName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelation.html#tableName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlRelation::tableName() const
    return self.uglySide.call('ritual_ZNK12QSqlRelation9tableNameEv')

  def indexColumn(self) -> str:
    """
    Calls Qt's 'QString QSqlRelation::indexColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelation.html#indexColumn

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlRelation::indexColumn() const
    return self.uglySide.call('ritual_ZNK12QSqlRelation11indexColumnEv')

  def displayColumn(self) -> str:
    """
    Calls Qt's 'QString QSqlRelation::displayColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelation.html#displayColumn

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlRelation::displayColumn() const
    return self.uglySide.call('ritual_ZNK12QSqlRelation13displayColumnEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSqlRelation::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelation.html#isValid
    """
    #  bool QSqlRelation::isValid() const
    return self.uglySide.call('ritual_ZNK12QSqlRelation7isValidEv')

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
    Notes what was given, for Qt's 'QSqlRelation::QSqlRelation()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelation.html#QSqlRelation
    """
    #  QSqlRelation::QSqlRelation()
    self._noteCreation(QSqlRelation, lambda: Rituals.call(
        'ritual_ZN12QSqlRelationC1Ev',
    ))

  @overload(str, str, str)
  def __init__(
      self,
      aTableName: str,
      indexCol: str,
      displayCol: str,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSqlRelation::QSqlRelation(const QString
    &aTableName, const QString &indexCol, const QString &displayCol)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelation.html#QSqlRelation

    Parameters
    ----------

    aTableName : str
      Passed on as it is: a QString is made of it for the call.

    indexCol : str
      Passed on as it is: a QString is made of it for the call.

    displayCol : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSqlRelation::QSqlRelation(const QString &aTableName, const QString
    #      &indexCol, const QString &displayCol)
    self._noteCreation(QSqlRelation, lambda: Rituals.call(
        'ritual_ZN12QSqlRelationC1ERK7QStringS2_S2_',
        aTableName, indexCol, displayCol,
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSqlRelation::swap(QSqlRelation &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlRelation.swap' has no cute function yet. Qt's 'void "
        "QSqlRelation::swap(QSqlRelation &other)': takes a type Python has "
        "no way to hand over yet.")
