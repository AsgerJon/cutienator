"""
QQmlV4Function binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4engine_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlV4Function to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class QQmlV4Function(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlV4Function: a plain Python object standing in
  front of one C++ QQmlV4Function.

  What exists
  -----------

  Every function of Qt's QQmlV4Function that has a ritual and that Python can
  call so far, 4 names in all: 'length', '__getitem__', 'setReturnValue',
  'v4engine'. It can be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlV4Function is created at the first use, not by
    'QQmlV4Function(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlV4Function.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlV4Function'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def length(self) -> int:
    """
    Calls Qt's 'int QQmlV4Function::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlv4function.html#length
    """
    #  int QQmlV4Function::length() const
    return self.uglySide.call('ritual_ZNK14QQmlV4Function6lengthEv')

  def v4engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQmlV4Function::v4engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlv4function.html#v4engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQmlV4Function::v4engine() const
    address = self.uglySide.call('ritual_ZNK14QQmlV4Function8v4engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setReturnValue(self, rv: int) -> None:
    """
    Calls Qt's 'void QQmlV4Function::setReturnValue(QV4::ReturnedValue rv)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlv4function.html#setReturnValue

    Parameters
    ----------

    rv : int
      Passed on as it is.
    """
    #  void QQmlV4Function::setReturnValue(QV4::ReturnedValue rv)
    self.uglySide.call('ritual_ZN14QQmlV4Function14setReturnValueEy', rv)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, idx: int) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlV4Function::operator[](int idx)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlv4function.html#operator[]

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlV4Function::operator[](int idx) const
    return self.uglySide.call('ritual_ZNK14QQmlV4FunctionixEi', idx)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      WAIT['QV4.CallData'], WAIT['QV4.Value'], WAIT['QV4.ExecutionEngine'],
  )
  @overload(WAIT['QV4.CallData'], WAIT['QV4.Value'], NoneType)
  @overload(WAIT['QV4.CallData'], NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(WAIT['QV4.CallData'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, WAIT['QV4.Value'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      callData: Optional[QV4.CallData],
      retVal: Optional[QV4.Value],
      e: Optional[QV4.ExecutionEngine],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlV4Function::QQmlV4Function(QV4::CallData *callData, QV4::Value
    *retVal, QV4::ExecutionEngine *e)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlv4function.html#QQmlV4Function

    Parameters
    ----------

    callData : Optional[QV4.CallData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    retVal : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlV4Function::QQmlV4Function(QV4::CallData *callData, QV4::Value
    #      *retVal, QV4::ExecutionEngine *e)
    self._noteCreation(QQmlV4Function, lambda: Rituals.call(
        'ritual_ZN14QQmlV4FunctionC1EPN3QV48CallDataEPNS0_5ValueEPNS0_15Exe'
        'cutionEngineE',
        self._addressOf(callData), self._addressOf(retVal),
        self._addressOf(e),
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
