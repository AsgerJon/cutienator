"""
QOpcUaEventFilterResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaeventfilterresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaContentFilterElementResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaContentFilterElementResult = WAIT['QOpcUaContentFilterElementResult']


class QOpcUaEventFilterResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaEventFilterResult: a plain Python object
  standing in front of one C++ QOpcUaEventFilterResult.

  C++ hands a QOpcUaEventFilterResult around as a copy, so every C++
  QOpcUaEventFilterResult behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaEventFilterResult that has a ritual and that
  Python can call so far, 3 names in all: 'isGood', 'whereClauseResults',
  'setWhereClauseResults'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaEventFilterResult &QOpcUaEventFilterResult::operator=(const
    QOpcUaEventFilterResult &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaEventFilterResult::~QOpcUaEventFilterResult()': the
    destructor: Python removes its C++ QOpcUaEventFilterResult by it, and has
    no other use for it.
  - Qt's 'QList<QOpcUa::UaStatusCode>
    QOpcUaEventFilterResult::selectClauseResults() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<QOpcUa::UaStatusCode>
    &QOpcUaEventFilterResult::selectClauseResultsRef()': gives a type Python
    has no way to take yet.
  - Qt's 'void QOpcUaEventFilterResult::setSelectClauseResults(const
    QList<QOpcUa::UaStatusCode> &selectClausesResult)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QList<QOpcUaContentFilterElementResult>
    &QOpcUaEventFilterResult::whereClauseResultsRef()': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaEventFilterResult is created at the first use, not by
    'QOpcUaEventFilterResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaEventFilterResult back gives a copy the ritual
    made for Python, in a new cute QOpcUaEventFilterResult.
  - Each name of Qt's QOpcUaEventFilterResult that has no cute function yet,
    'selectClauseResults', 'selectClauseResultsRef',
    'setSelectClauseResults', 'whereClauseResultsRef', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaEventFilterResult'

  #  Qt's '~QOpcUaEventFilterResult()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaEventFilterResult behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QOpcUaEventFilterResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isGood(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaEventFilterResult::isGood() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeventfilterresult.html#isGood
    """
    #  bool QOpcUaEventFilterResult::isGood() const
    return self.uglySide.call('ritual_ZNK23QOpcUaEventFilterResult6isGoodEv')

  def whereClauseResults(self) -> QList[QOpcUaContentFilterElementResult]:
    """
    Calls Qt's 'QList<QOpcUaContentFilterElementResult>
    QOpcUaEventFilterResult::whereClauseResults() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeventfilterresult.html#whereClauseResults

    Returns
    -------

    QList[QOpcUaContentFilterElementResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaContentFilterElementResult>
    #      QOpcUaEventFilterResult::whereClauseResults() const
    address = self.uglySide.call(
        'ritual_ZNK23QOpcUaEventFilterResult18whereClauseResultsEv',
    )
    from . import QOpcUaContentFilterElementResult
    return QList[QOpcUaContentFilterElementResult]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QOpcUaContentFilterElementResult])
  def setWhereClauseResults(
      self,
      whereClauseResult: QList[QOpcUaContentFilterElementResult],
  ) -> None:
    """
    Calls Qt's 'void QOpcUaEventFilterResult::setWhereClauseResults(const
    QList<QOpcUaContentFilterElementResult> &whereClauseResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeventfilterresult.html#setWhereClauseResults

    Parameters
    ----------

    whereClauseResult : QList[QOpcUaContentFilterElementResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaEventFilterResult::setWhereClauseResults(const
    #      QList<QOpcUaContentFilterElementResult> &whereClauseResult)
    self.uglySide.call(
        'ritual_ZN23QOpcUaEventFilterResult21setWhereClauseResultsERK5QList'
        'I32QOpcUaContentFilterElementResultE',
        self._valueOf(whereClauseResult),
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
    Notes what was given, for Qt's
    'QOpcUaEventFilterResult::QOpcUaEventFilterResult()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeventfilterresult.html
    """
    #  QOpcUaEventFilterResult::QOpcUaEventFilterResult()
    self._noteCreation(QOpcUaEventFilterResult, lambda: Rituals.call(
        'ritual_ZN23QOpcUaEventFilterResultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaEventFilterResult) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaEventFilterResult::QOpcUaEventFilterResult(const
    QOpcUaEventFilterResult &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeventfilterresult.html

    Parameters
    ----------

    a0 : QOpcUaEventFilterResult
      Passed on as a value: Qt reads the C++ QOpcUaEventFilterResult, which
      stays Python's own.
    """
    #  QOpcUaEventFilterResult::QOpcUaEventFilterResult(const
    #      QOpcUaEventFilterResult &a0)
    self._noteCreation(QOpcUaEventFilterResult, lambda: Rituals.call(
        'ritual_ZN23QOpcUaEventFilterResultC1ERKS_', self._valueOf(a0),
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
  def selectClauseResults(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUa::UaStatusCode>
    QOpcUaEventFilterResult::selectClauseResults() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaEventFilterResult.selectClauseResults' has no cute function "
        "yet. Qt's 'QList<QOpcUa::UaStatusCode> "
        "QOpcUaEventFilterResult::selectClauseResults() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def selectClauseResultsRef(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUa::UaStatusCode>
    &QOpcUaEventFilterResult::selectClauseResultsRef()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaEventFilterResult.selectClauseResultsRef' has no cute "
        "function yet. Qt's 'QList<QOpcUa::UaStatusCode> "
        "&QOpcUaEventFilterResult::selectClauseResultsRef()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setSelectClauseResults(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaEventFilterResult::setSelectClauseResults(const
    QList<QOpcUa::UaStatusCode> &selectClausesResult)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaEventFilterResult.setSelectClauseResults' has no cute "
        "function yet. Qt's 'void "
        "QOpcUaEventFilterResult::setSelectClauseResults(const "
        "QList<QOpcUa::UaStatusCode> &selectClausesResult)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def whereClauseResultsRef(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUaContentFilterElementResult>
    &QOpcUaEventFilterResult::whereClauseResultsRef()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaEventFilterResult.whereClauseResultsRef' has no cute "
        "function yet. Qt's 'QList<QOpcUaContentFilterElementResult> "
        "&QOpcUaEventFilterResult::whereClauseResultsRef()': gives a type "
        "Python has no way to take yet.")
