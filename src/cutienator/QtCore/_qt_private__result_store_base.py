"""
QtPrivate::ResultStoreBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qresultstore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ResultStoreBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::ResultStoreBase: a plain Python object
  standing in front of one C++ QtPrivate::ResultStoreBase.

  C++ hands a QtPrivate::ResultStoreBase around as a copy, so every C++
  QtPrivate::ResultStoreBase behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::ResultStoreBase that has a ritual and
  that Python can call so far, 13 names in all: 'setFilterMode',
  'filterMode', 'begin', 'end', 'hasNextResult', 'resultAt', 'contains',
  'count', 'containsValidResultItem', 'syncPendingResults',
  'syncResultCount', 'updateInsertIndex', 'addCanceledResult'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QtPrivate::ResultStoreBase::addResult(int index, const void
    *result)': names 'void', which has no cute class yet.
  - Qt's 'int QtPrivate::ResultStoreBase::addResults(int index, const void
    *results, int vectorSize, int logicalCount)': names 'void', which has no
    cute class yet.
  - Qt's 'QtPrivate::ResultStoreBase::~ResultStoreBase()': the destructor:
    Python removes its C++ QtPrivate::ResultStoreBase by it, and has no other
    use for it.
  - Qt's 'int QtPrivate::ResultStoreBase::insertResultItem(int index,
    ResultItem &resultItem)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QtPrivate::ResultStoreBase::insertResultItemIfValid(int index,
    ResultItem &resultItem)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  8 of the 27 functions Qt declares: 8 a template.

  What to expect
  --------------

  - The C++ QtPrivate::ResultStoreBase is created at the first use, not by
    'QtPrivate::ResultStoreBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::ResultStoreBase back gives a copy the
    ritual made for Python, in a new cute QtPrivate::ResultStoreBase.
  - Each name of Qt's QtPrivate::ResultStoreBase that has no cute function
    yet, 'addCanceledResults', 'addResult', 'addResults', 'clear',
    'emplaceResult', 'insertResultItem', 'insertResultItemIfValid',
    'moveResult', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::ResultStoreBase'

  #  Qt's '~QtPrivate::ResultStoreBase()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::ResultStoreBase behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate15ResultStoreBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def filterMode(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultStoreBase::filterMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#filterMode
    """
    #  bool QtPrivate::ResultStoreBase::filterMode() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase10filterModeEv',
    )

  def begin(self) -> QtPrivate.ResultIteratorBase:
    """
    Calls Qt's 'ResultIteratorBase QtPrivate::ResultStoreBase::begin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#begin

    Returns
    -------

    QtPrivate.ResultIteratorBase
      A new cute QtPrivate::ResultIteratorBase around the copy Qt gave back.
      Python owns it.
    """
    #  ResultIteratorBase QtPrivate::ResultStoreBase::begin() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase5beginEv',
    )
    return QtPrivate.ResultIteratorBase._cuteOwning(address)

  def end(self) -> QtPrivate.ResultIteratorBase:
    """
    Calls Qt's 'ResultIteratorBase QtPrivate::ResultStoreBase::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#end

    Returns
    -------

    QtPrivate.ResultIteratorBase
      A new cute QtPrivate::ResultIteratorBase around the copy Qt gave back.
      Python owns it.
    """
    #  ResultIteratorBase QtPrivate::ResultStoreBase::end() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase3endEv',
    )
    return QtPrivate.ResultIteratorBase._cuteOwning(address)

  def hasNextResult(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultStoreBase::hasNextResult() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#hasNextResult
    """
    #  bool QtPrivate::ResultStoreBase::hasNextResult() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase13hasNextResultEv',
    )

  @overload(int)
  def resultAt(self, index: int) -> QtPrivate.ResultIteratorBase:
    """
    Calls Qt's 'ResultIteratorBase QtPrivate::ResultStoreBase::resultAt(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#resultAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QtPrivate.ResultIteratorBase
      A new cute QtPrivate::ResultIteratorBase around the copy Qt gave back.
      Python owns it.
    """
    #  ResultIteratorBase QtPrivate::ResultStoreBase::resultAt(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase8resultAtEi', index,
    )
    return QtPrivate.ResultIteratorBase._cuteOwning(address)

  @overload(int)
  def contains(self, index: int) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultStoreBase::contains(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#contains

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QtPrivate::ResultStoreBase::contains(int index) const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase8containsEi', index,
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QtPrivate::ResultStoreBase::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#count
    """
    #  int QtPrivate::ResultStoreBase::count() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase5countEv',
    )

  @overload(int)
  def containsValidResultItem(self, index: int) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultStoreBase::containsValidResultItem(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QtPrivate::ResultStoreBase::containsValidResultItem(int index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate15ResultStoreBase23containsValidResultItemEi',
        index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFilterMode(self, enable: bool) -> None:
    """
    Calls Qt's 'void QtPrivate::ResultStoreBase::setFilterMode(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#setFilterMode

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QtPrivate::ResultStoreBase::setFilterMode(bool enable)
    self.uglySide.call(
        'ritual_ZN9QtPrivate15ResultStoreBase13setFilterModeEb', enable,
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
    'QtPrivate::ResultStoreBase::ResultStoreBase()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#ResultStoreBase
    """
    #  QtPrivate::ResultStoreBase::ResultStoreBase()
    self._noteCreation(ResultStoreBase, lambda: Rituals.call(
        'ritual_ZN9QtPrivate15ResultStoreBaseC1Ev',
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

  def syncPendingResults(self) -> None:
    """
    Calls Qt's 'void QtPrivate::ResultStoreBase::syncPendingResults()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#syncPendingResults
    """
    #  void QtPrivate::ResultStoreBase::syncPendingResults()
    self.uglySide.call(
        'ritual_ZN9QtPrivate15ResultStoreBase18syncPendingResultsEv',
    )

  def syncResultCount(self) -> None:
    """
    Calls Qt's 'void QtPrivate::ResultStoreBase::syncResultCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#syncResultCount
    """
    #  void QtPrivate::ResultStoreBase::syncResultCount()
    self.uglySide.call(
        'ritual_ZN9QtPrivate15ResultStoreBase15syncResultCountEv',
    )

  @overload(int, int)
  def updateInsertIndex(self, index: int, _count: int) -> int:
    """
    Calls Qt's 'int QtPrivate::ResultStoreBase::updateInsertIndex(int index,
    int _count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#updateInsertIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    _count : int
      Passed on as it is.
    """
    #  int QtPrivate::ResultStoreBase::updateInsertIndex(int index, int
    #      _count)
    return self.uglySide.call(
        'ritual_ZN9QtPrivate15ResultStoreBase17updateInsertIndexEii',
        index, _count,
    )

  @overload(int)
  def addCanceledResult(self, index: int) -> int:
    """
    Calls Qt's 'int QtPrivate::ResultStoreBase::addCanceledResult(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultstorebase.html#addCanceledResult

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QtPrivate::ResultStoreBase::addCanceledResult(int index)
    return self.uglySide.call(
        'ritual_ZN9QtPrivate15ResultStoreBase17addCanceledResultEi', index,
    )

  @staticmethod
  def addCanceledResults(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::ResultStoreBase::addCanceledResults': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.addCanceledResults' has no cute "
        "function yet. Qt's "
        "'QtPrivate::ResultStoreBase::addCanceledResults': a template: a "
        "pattern and no single function.")

  @staticmethod
  def addResult(*__, **_) -> Never:
    """
    - Qt's 'int QtPrivate::ResultStoreBase::addResult(int index, const void
      *result)': names 'void', which has no cute class yet.
    - Qt's 'QtPrivate::ResultStoreBase::addResult': a template: a pattern and
      no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.addResult' has no cute function yet. "
        "Qt's 'int QtPrivate::ResultStoreBase::addResult(int index, const "
        "void *result)': names 'void', which has no cute class yet. Qt's "
        "'QtPrivate::ResultStoreBase::addResult': a template: a pattern and "
        "no single function.")

  @staticmethod
  def addResults(*__, **_) -> Never:
    """
    - Qt's 'int QtPrivate::ResultStoreBase::addResults(int index, const void
      *results, int vectorSize, int logicalCount)': names 'void', which has
      no cute class yet.
    - Qt's 'QtPrivate::ResultStoreBase::addResults': a template: a pattern
      and no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.addResults' has no cute function yet. "
        "Qt's 'int QtPrivate::ResultStoreBase::addResults(int index, const "
        "void *results, int vectorSize, int logicalCount)': names 'void', "
        "which has no cute class yet. Qt's "
        "'QtPrivate::ResultStoreBase::addResults': a template: a pattern "
        "and no single function.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::ResultStoreBase::clear': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.clear' has no cute function yet. Qt's "
        "'QtPrivate::ResultStoreBase::clear': a template: a pattern and no "
        "single function.")

  @staticmethod
  def emplaceResult(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::ResultStoreBase::emplaceResult': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.emplaceResult' has no cute function "
        "yet. Qt's 'QtPrivate::ResultStoreBase::emplaceResult': a template: "
        "a pattern and no single function.")

  @staticmethod
  def insertResultItem(*__, **_) -> Never:
    """
    Qt's 'int QtPrivate::ResultStoreBase::insertResultItem(int index,
    ResultItem &resultItem)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.insertResultItem' has no cute function "
        "yet. Qt's 'int QtPrivate::ResultStoreBase::insertResultItem(int "
        "index, ResultItem &resultItem)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def insertResultItemIfValid(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::ResultStoreBase::insertResultItemIfValid(int index,
    ResultItem &resultItem)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.insertResultItemIfValid' has no cute "
        "function yet. Qt's 'void "
        "QtPrivate::ResultStoreBase::insertResultItemIfValid(int index, "
        "ResultItem &resultItem)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def moveResult(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::ResultStoreBase::moveResult': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultStoreBase.moveResult' has no cute function yet. "
        "Qt's 'QtPrivate::ResultStoreBase::moveResult': a template: a "
        "pattern and no single function.")
