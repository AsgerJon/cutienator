"""
QV4::Scope binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Scope to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scope(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Scope: a plain Python object standing in front
  of one C++ QV4::Scope.

  What exists
  -----------

  Every function of Qt's QV4::Scope that has a ritual and that Python can
  call so far, 4 names in all: 'construct', 'constructUndefined',
  'hasException', 'alloc'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Scope::~Scope()': the destructor: Python never removes a C++
    QV4::Scope.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QV4::Scope is created at the first use, not by 'QV4::Scope(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Scope.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Scope'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def construct(
      self,
      nValues: int,
      initialValue: int,
  ) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::Scope::construct(int nValues, const ReturnedValue
    &initialValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#construct

    Parameters
    ----------

    nValues : int
      Passed on as it is.

    initialValue : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::Scope::construct(int nValues, const ReturnedValue
    #      &initialValue) const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Scope9constructEiRKy', nValues, initialValue,
    )
    return QV4.Value._cuteAt(address)

  @overload(int, WAIT['QV4.Value'])
  def construct(
      self,
      nValues: int,
      initialValue: QV4.Value,
  ) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::Scope::construct(int nValues, const Value
    &initialValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#construct

    Parameters
    ----------

    nValues : int
      Passed on as it is.

    initialValue : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::Scope::construct(int nValues, const Value &initialValue)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Scope9constructEiRKNS_5ValueE',
        nValues, self._valueOf(initialValue),
    )
    return QV4.Value._cuteAt(address)

  @overload(int, WAIT['QV4.Heap.Base'])
  @overload(int, NoneType)
  def construct(
      self,
      nValues: int,
      initialValue: Optional[QV4.Heap.Base],
  ) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::Scope::construct(int nValues, Heap::Base
    *initialValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#construct

    Parameters
    ----------

    nValues : int
      Passed on as it is.

    initialValue : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::Scope::construct(int nValues, Heap::Base *initialValue)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Scope9constructEiPNS_4Heap4BaseE',
        nValues, self._addressOf(initialValue),
    )
    return QV4.Value._cuteAt(address)

  @overload(int, WAIT['QV4.PropertyKey'])
  def construct(
      self,
      nValues: int,
      initialValue: QV4.PropertyKey,
  ) -> Optional[QV4.PropertyKey]:
    """
    Calls Qt's 'PropertyKey *QV4::Scope::construct(int nValues, const
    PropertyKey &initialValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#construct

    Parameters
    ----------

    nValues : int
      Passed on as it is.

    initialValue : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    Optional[QV4.PropertyKey]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PropertyKey *QV4::Scope::construct(int nValues, const PropertyKey
    #      &initialValue) const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Scope9constructEiRKNS_11PropertyKeyE',
        nValues, self._valueOf(initialValue),
    )
    return QV4.PropertyKey._cuteAt(address)

  @overload(int)
  def constructUndefined(self, nValues: int) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::Scope::constructUndefined(int nValues) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#constructUndefined

    Parameters
    ----------

    nValues : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::Scope::constructUndefined(int nValues) const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Scope18constructUndefinedEi', nValues,
    )
    return QV4.Value._cuteAt(address)

  def hasException(self) -> bool:
    """
    Calls Qt's 'bool QV4::Scope::hasException() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#hasException
    """
    #  bool QV4::Scope::hasException() const
    return self.uglySide.call('ritual_ZNK3QV45Scope12hasExceptionEv')

  @overload(int)
  def alloc(self, nValues: int) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::Scope::alloc(int nValues) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#alloc

    Parameters
    ----------

    nValues : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::Scope::alloc(int nValues) const
    address = self.uglySide.call('ritual_ZNK3QV45Scope5allocEi', nValues)
    return QV4.Value._cuteAt(address)

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

  @overload(WAIT['QV4.ExecutionContext'])
  @overload(NoneType)
  def __init__(self, ctx: Optional[QV4.ExecutionContext]) -> None:
    """
    Notes what was given, for Qt's 'QV4::Scope::Scope(ExecutionContext
    *ctx)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#Scope

    Parameters
    ----------

    ctx : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Scope::Scope(ExecutionContext *ctx)
    self._noteCreation(Scope, lambda: Rituals.call(
        'ritual_ZN3QV45ScopeC1EPNS_16ExecutionContextE',
        self._addressOf(ctx),
    ))

  @overload(WAIT['QV4.ExecutionEngine'])
  def __init__(self, e: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's 'QV4::Scope::Scope(ExecutionEngine *e)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#Scope

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Scope::Scope(ExecutionEngine *e)
    self._noteCreation(Scope, lambda: Rituals.call(
        'ritual_ZN3QV45ScopeC1EPNS_15ExecutionEngineE', self._addressOf(e),
    ))

  @overload(WAIT['QV4.Managed'])
  def __init__(self, m: Optional[QV4.Managed]) -> None:
    """
    Notes what was given, for Qt's 'QV4::Scope::Scope(const Managed *m)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scope.html#Scope

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Scope::Scope(const Managed *m)
    self._noteCreation(Scope, lambda: Rituals.call(
        'ritual_ZN3QV45ScopeC1EPKNS_7ManagedE', self._addressOf(m),
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
