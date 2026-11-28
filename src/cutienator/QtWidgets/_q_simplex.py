"""
QSimplex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsimplex_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSimplex to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSimplexConstraint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSimplexConstraint = WAIT['QSimplexConstraint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSimplex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSimplex: a plain Python object standing in front of
  one C++ QSimplex.

  What exists
  -----------

  Every function of Qt's QSimplex that has a ritual and that Python can call
  so far, 17 names in all: 'solveMin', 'solveMax', 'setConstraints',
  'setObjective', 'dumpMatrix', 'valueAt', 'setValueAt', 'clearRow',
  'clearColumns', 'combineRows', 'findPivotColumn', 'pivotRowForColumn',
  'reducedRowEchelon', 'iterate', 'clearDataStructures', 'solveMaxHelper',
  'collectResults'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSimplex::~QSimplex()': the destructor: Python never removes a C++
    QSimplex.
  - Qt's 'bool QSimplex::simplifyConstraints(QList<QSimplexConstraint *>
    *constraints)': names 'QList<QSimplexConstraint *>', which has no cute
    class yet.
  - Qt's 'qreal QSimplex::solver(SolverFactor factor)': names the enum
    'QSimplex::SolverFactor', whose class cannot be named here.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSimplex is created at the first use, not by 'QSimplex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSimplex.
  - Each name of Qt's QSimplex that has no cute function yet,
    'simplifyConstraints', 'solver', holds a function that raises
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
  __qt_class__ = 'QSimplex'

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

  @overload(QList[QSimplexConstraint])
  def setConstraints(self, constraints: QList[QSimplexConstraint]) -> bool:
    """
    Calls Qt's 'bool QSimplex::setConstraints(const QList<QSimplexConstraint
    *> &constraints)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#setConstraints

    Parameters
    ----------

    constraints : QList[QSimplexConstraint]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QSimplex::setConstraints(const QList<QSimplexConstraint *>
    #      &constraints)
    return self.uglySide.call(
        'ritual_ZN8QSimplex14setConstraintsERK5QListIP18QSimplexConstraintE',
        self._valueOf(constraints),
    )

  @overload(QSimplexConstraint)
  @overload(NoneType)
  def setObjective(self, objective: Optional[QSimplexConstraint]) -> None:
    """
    Calls Qt's 'void QSimplex::setObjective(QSimplexConstraint *objective)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#setObjective

    Parameters
    ----------

    objective : Optional[QSimplexConstraint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSimplex::setObjective(QSimplexConstraint *objective)
    self.uglySide.call(
        'ritual_ZN8QSimplex12setObjectiveEP18QSimplexConstraint',
        self._addressOf(objective),
    )

  @overload(int, int, float)
  def setValueAt(self, row: int, column: int, value: float) -> None:
    """
    Calls Qt's 'void QSimplex::setValueAt(int row, int column, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#setValueAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QSimplex::setValueAt(int row, int column, qreal value)
    self.uglySide.call(
        'ritual_ZN8QSimplex10setValueAtEiid', row, column, value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSimplex::QSimplex()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#QSimplex
    """
    #  QSimplex::QSimplex()
    self._noteCreation(QSimplex, lambda: Rituals.call(
        'ritual_ZN8QSimplexC1Ev',
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

  def solveMin(self) -> float:
    """
    Calls Qt's 'qreal QSimplex::solveMin()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#solveMin
    """
    #  qreal QSimplex::solveMin()
    return self.uglySide.call('ritual_ZN8QSimplex8solveMinEv')

  def solveMax(self) -> float:
    """
    Calls Qt's 'qreal QSimplex::solveMax()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#solveMax
    """
    #  qreal QSimplex::solveMax()
    return self.uglySide.call('ritual_ZN8QSimplex8solveMaxEv')

  def dumpMatrix(self) -> None:
    """
    Calls Qt's 'void QSimplex::dumpMatrix()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#dumpMatrix
    """
    #  void QSimplex::dumpMatrix()
    self.uglySide.call('ritual_ZN8QSimplex10dumpMatrixEv')

  @overload(int, int)
  def valueAt(self, row: int, column: int) -> float:
    """
    Calls Qt's 'qreal QSimplex::valueAt(int row, int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#valueAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  qreal QSimplex::valueAt(int row, int column)
    return self.uglySide.call('ritual_ZN8QSimplex7valueAtEii', row, column)

  @overload(int)
  def clearRow(self, rowIndex: int) -> None:
    """
    Calls Qt's 'void QSimplex::clearRow(int rowIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#clearRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.
    """
    #  void QSimplex::clearRow(int rowIndex)
    self.uglySide.call('ritual_ZN8QSimplex8clearRowEi', rowIndex)

  @overload(int, int)
  def clearColumns(self, first: int, last: int) -> None:
    """
    Calls Qt's 'void QSimplex::clearColumns(int first, int last)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#clearColumns

    Parameters
    ----------

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QSimplex::clearColumns(int first, int last)
    self.uglySide.call('ritual_ZN8QSimplex12clearColumnsEii', first, last)

  @overload(int, int, float)
  def combineRows(self, toIndex: int, fromIndex: int, factor: float) -> None:
    """
    Calls Qt's 'void QSimplex::combineRows(int toIndex, int fromIndex, qreal
    factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#combineRows

    Parameters
    ----------

    toIndex : int
      Passed on as it is.

    fromIndex : int
      Passed on as it is.

    factor : float
      Passed on as it is.
    """
    #  void QSimplex::combineRows(int toIndex, int fromIndex, qreal factor)
    self.uglySide.call(
        'ritual_ZN8QSimplex11combineRowsEiid', toIndex, fromIndex, factor,
    )

  def findPivotColumn(self) -> int:
    """
    Calls Qt's 'int QSimplex::findPivotColumn()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#findPivotColumn
    """
    #  int QSimplex::findPivotColumn()
    return self.uglySide.call('ritual_ZN8QSimplex15findPivotColumnEv')

  @overload(int)
  def pivotRowForColumn(self, column: int) -> int:
    """
    Calls Qt's 'int QSimplex::pivotRowForColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#pivotRowForColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QSimplex::pivotRowForColumn(int column)
    return self.uglySide.call(
        'ritual_ZN8QSimplex17pivotRowForColumnEi', column,
    )

  def reducedRowEchelon(self) -> None:
    """
    Calls Qt's 'void QSimplex::reducedRowEchelon()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#reducedRowEchelon
    """
    #  void QSimplex::reducedRowEchelon()
    self.uglySide.call('ritual_ZN8QSimplex17reducedRowEchelonEv')

  def iterate(self) -> bool:
    """
    Calls Qt's 'bool QSimplex::iterate()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#iterate
    """
    #  bool QSimplex::iterate()
    return self.uglySide.call('ritual_ZN8QSimplex7iterateEv')

  def clearDataStructures(self) -> None:
    """
    Calls Qt's 'void QSimplex::clearDataStructures()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#clearDataStructures
    """
    #  void QSimplex::clearDataStructures()
    self.uglySide.call('ritual_ZN8QSimplex19clearDataStructuresEv')

  def solveMaxHelper(self) -> None:
    """
    Calls Qt's 'void QSimplex::solveMaxHelper()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#solveMaxHelper
    """
    #  void QSimplex::solveMaxHelper()
    self.uglySide.call('ritual_ZN8QSimplex14solveMaxHelperEv')

  def collectResults(self) -> None:
    """
    Calls Qt's 'void QSimplex::collectResults()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplex.html#collectResults
    """
    #  void QSimplex::collectResults()
    self.uglySide.call('ritual_ZN8QSimplex14collectResultsEv')

  @staticmethod
  def simplifyConstraints(*__, **_) -> Never:
    """
    Qt's 'bool QSimplex::simplifyConstraints(QList<QSimplexConstraint *>
    *constraints)': names 'QList<QSimplexConstraint *>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSimplex.simplifyConstraints' has no cute function yet. Qt's "
        "'bool QSimplex::simplifyConstraints(QList<QSimplexConstraint *> "
        "*constraints)': names 'QList<QSimplexConstraint *>', which has no "
        "cute class yet.")

  @staticmethod
  def solver(*__, **_) -> Never:
    """
    Qt's 'qreal QSimplex::solver(SolverFactor factor)': names the enum
    'QSimplex::SolverFactor', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSimplex.solver' has no cute function yet. Qt's 'qreal "
        "QSimplex::solver(SolverFactor factor)': names the enum "
        "'QSimplex::SolverFactor', whose class cannot be named here.")
