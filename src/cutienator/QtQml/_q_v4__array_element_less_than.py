"""
QV4::ArrayElementLessThan binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::ArrayElementLessThan to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class ArrayElementLessThan(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::ArrayElementLessThan: a plain Python object
  standing in front of one C++ QV4::ArrayElementLessThan.

  C++ hands a QV4::ArrayElementLessThan around as a copy, so every C++
  QV4::ArrayElementLessThan behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::ArrayElementLessThan that has a ritual and that
  Python can call so far, 1 name in all: '__call__'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::ArrayElementLessThan::~ArrayElementLessThan()': the
    destructor: Python removes its C++ QV4::ArrayElementLessThan by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QV4::ArrayElementLessThan is created at the first use, not by
    'QV4::ArrayElementLessThan(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::ArrayElementLessThan back gives a copy the
    ritual made for Python, in a new cute QV4::ArrayElementLessThan.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ArrayElementLessThan'

  #  Qt's '~QV4::ArrayElementLessThan()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::ArrayElementLessThan behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV420ArrayElementLessThanD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
  def __call__(self, v1: QV4.Value, v2: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QV4::ArrayElementLessThan::operator()(Value v1, Value
    v2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arrayelementlessthan.html#operator()

    Parameters
    ----------

    v1 : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    v2 : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::ArrayElementLessThan::operator()(Value v1, Value v2) const
    return self.uglySide.call(
        'ritual_ZNK3QV420ArrayElementLessThanclENS_5ValueES1_',
        self._valueOf(v1), self._valueOf(v2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      comparefn: QV4.Value,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::ArrayElementLessThan::ArrayElementLessThan(ExecutionEngine *engine,
    const Value &comparefn)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arrayelementlessthan.html#ArrayElementLessThan

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    comparefn : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  QV4::ArrayElementLessThan::ArrayElementLessThan(ExecutionEngine
    #      *engine, const Value &comparefn)
    self._noteCreation(ArrayElementLessThan, lambda: Rituals.call(
        'ritual_ZN3QV420ArrayElementLessThanC1EPNS_15ExecutionEngineERKNS_5'
        'ValueE',
        self._addressOf(engine), self._valueOf(comparefn),
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
