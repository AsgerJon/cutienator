"""
QtPrivate::ResultIteratorBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qresultstore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ResultIteratorBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::ResultIteratorBase: a plain Python object
  standing in front of one C++ QtPrivate::ResultIteratorBase.

  C++ hands a QtPrivate::ResultIteratorBase around as a copy, so every C++
  QtPrivate::ResultIteratorBase behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::ResultIteratorBase that has a ritual and
  that Python can call so far, 9 names in all: 'vectorIndex', 'resultIndex',
  'batchSize', 'batchedAdvance', 'isVector', 'canIncrementVectorIndex',
  'isValid', '__eq__', '__ne__'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::ResultIteratorBase::ResultIteratorBase(QMap<int,
    ResultItem>::const_iterator _mapIterator, int _vectorIndex)': takes a
    type Python has no way to hand over yet.
  - Qt's 'ResultIteratorBase QtPrivate::ResultIteratorBase::operator++()': an
    operator Python has no name for.
  - Qt's 'QtPrivate::ResultIteratorBase::~ResultIteratorBase()': the
    destructor: Python removes its C++ QtPrivate::ResultIteratorBase by it,
    and has no other use for it.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 4 a template.

  What to expect
  --------------

  - The C++ QtPrivate::ResultIteratorBase is created at the first use, not by
    'QtPrivate::ResultIteratorBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::ResultIteratorBase back gives a copy the
    ritual made for Python, in a new cute QtPrivate::ResultIteratorBase.
  - Each name of Qt's QtPrivate::ResultIteratorBase that has no cute function
    yet, 'pointer', 'value', holds a function that raises
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
  __qt_class__ = 'QtPrivate::ResultIteratorBase'

  #  Qt's '~QtPrivate::ResultIteratorBase()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::ResultIteratorBase behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate18ResultIteratorBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def vectorIndex(self) -> int:
    """
    Calls Qt's 'int QtPrivate::ResultIteratorBase::vectorIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#vectorIndex
    """
    #  int QtPrivate::ResultIteratorBase::vectorIndex() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate18ResultIteratorBase11vectorIndexEv',
    )

  def resultIndex(self) -> int:
    """
    Calls Qt's 'int QtPrivate::ResultIteratorBase::resultIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#resultIndex
    """
    #  int QtPrivate::ResultIteratorBase::resultIndex() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate18ResultIteratorBase11resultIndexEv',
    )

  def batchSize(self) -> int:
    """
    Calls Qt's 'int QtPrivate::ResultIteratorBase::batchSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#batchSize
    """
    #  int QtPrivate::ResultIteratorBase::batchSize() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate18ResultIteratorBase9batchSizeEv',
    )

  def isVector(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultIteratorBase::isVector() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#isVector
    """
    #  bool QtPrivate::ResultIteratorBase::isVector() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate18ResultIteratorBase8isVectorEv',
    )

  def canIncrementVectorIndex(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultIteratorBase::canIncrementVectorIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html
    """
    #  bool QtPrivate::ResultIteratorBase::canIncrementVectorIndex() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate18ResultIteratorBase23canIncrementVectorIndexE'
        'v',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultIteratorBase::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#isValid
    """
    #  bool QtPrivate::ResultIteratorBase::isValid() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate18ResultIteratorBase7isValidEv',
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

  @overload(THIS)
  def __eq__(self, rhs: ResultIteratorBase) -> bool:
    """
    Calls Qt's 'bool operator==(const ResultIteratorBase &lhs, const
    ResultIteratorBase &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#operator==

    Parameters
    ----------

    rhs : ResultIteratorBase
      Passed on as a value: Qt reads the C++ QtPrivate::ResultIteratorBase,
      which stays Python's own.
    """
    #  bool operator==(const ResultIteratorBase &lhs, const
    #      ResultIteratorBase &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_18ResultIteratorBaseES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: ResultIteratorBase) -> bool:
    """
    Calls Qt's 'bool operator!=(const ResultIteratorBase &lhs, const
    ResultIteratorBase &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#operator!=

    Parameters
    ----------

    rhs : ResultIteratorBase
      Passed on as a value: Qt reads the C++ QtPrivate::ResultIteratorBase,
      which stays Python's own.
    """
    #  bool operator!=(const ResultIteratorBase &lhs, const
    #      ResultIteratorBase &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_18ResultIteratorBaseES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::ResultIteratorBase::ResultIteratorBase()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html
    """
    #  QtPrivate::ResultIteratorBase::ResultIteratorBase()
    self._noteCreation(ResultIteratorBase, lambda: Rituals.call(
        'ritual_ZN9QtPrivate18ResultIteratorBaseC1Ev',
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

  def batchedAdvance(self) -> None:
    """
    Calls Qt's 'void QtPrivate::ResultIteratorBase::batchedAdvance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultiteratorbase.html#batchedAdvance
    """
    #  void QtPrivate::ResultIteratorBase::batchedAdvance()
    self.uglySide.call(
        'ritual_ZN9QtPrivate18ResultIteratorBase14batchedAdvanceEv',
    )

  @staticmethod
  def pointer(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::ResultIteratorBase::pointer': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultIteratorBase.pointer' has no cute function yet. "
        "Qt's 'QtPrivate::ResultIteratorBase::pointer': a template: a "
        "pattern and no single function.")

  @staticmethod
  def value(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::ResultIteratorBase::value': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtPrivate.ResultIteratorBase.value' has no cute function yet. "
        "Qt's 'QtPrivate::ResultIteratorBase::value': a template: a pattern "
        "and no single function.")
