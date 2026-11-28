"""
QV4::JSCallData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4jscall_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::JSCallData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JSCallData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::JSCallData: a plain Python object standing in
  front of one C++ QV4::JSCallData.

  C++ hands a QV4::JSCallData around as a copy, so every C++ QV4::JSCallData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::JSCallData yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'CallData *QV4::JSCallData::callData(const Scope &scope, const
    FunctionObject *f) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QV4::JSCallData::~JSCallData()': the destructor: Python removes its
    C++ QV4::JSCallData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::JSCallData is created at the first use, not by
    'QV4::JSCallData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::JSCallData back gives a copy the ritual made for
    Python, in a new cute QV4::JSCallData.
  - Each name of Qt's QV4::JSCallData that has no cute function yet,
    'callData', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QV4::JSCallData'

  #  Qt's '~QV4::JSCallData()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::JSCallData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV410JSCallDataD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, int)
  def __init__(
      self,
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QV4::JSCallData::JSCallData(const Value
    *thisObject, const Value *argv, int argc)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jscalldata.html#JSCallData

    Parameters
    ----------

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  QV4::JSCallData::JSCallData(const Value *thisObject, const Value
    #      *argv, int argc)
    self._noteCreation(JSCallData, lambda: Rituals.call(
        'ritual_ZN3QV410JSCallDataC1EPKNS_5ValueES3_i',
        self._addressOf(thisObject), self._addressOf(argv), argc,
    ))

  @overload(WAIT['QV4.JSCallArguments'])
  def __init__(self, args: QV4.JSCallArguments) -> None:
    """
    Notes what was given, for Qt's 'QV4::JSCallData::JSCallData(const
    JSCallArguments &args)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jscalldata.html#JSCallData

    Parameters
    ----------

    args : QV4.JSCallArguments
      Passed on as a value: Qt reads the C++ QV4::JSCallArguments, which
      stays Python's own.
    """
    #  QV4::JSCallData::JSCallData(const JSCallArguments &args)
    self._noteCreation(JSCallData, lambda: Rituals.call(
        'ritual_ZN3QV410JSCallDataC1ERKNS_15JSCallArgumentsE',
        self._valueOf(args),
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
  def callData(*__, **_) -> Never:
    """
    Qt's 'CallData *QV4::JSCallData::callData(const Scope &scope, const
    FunctionObject *f) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QV4.JSCallData.callData' has no cute function yet. Qt's 'CallData "
        "*QV4::JSCallData::callData(const Scope &scope, const "
        "FunctionObject *f) const': takes a type Python has no way to hand "
        "over yet.")
