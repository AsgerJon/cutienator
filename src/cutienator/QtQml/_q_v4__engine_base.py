"""
QV4::EngineBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4enginebase_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::EngineBase to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class EngineBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::EngineBase: a plain Python object standing in
  front of one C++ QV4::EngineBase.

  C++ hands a QV4::EngineBase around as a copy, so every C++ QV4::EngineBase
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::EngineBase that has a ritual and that Python
  can call so far, 1 name in all: 'internalClasses'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::EngineBase::~EngineBase()': the destructor: Python removes its
    C++ QV4::EngineBase by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::EngineBase is created at the first use, not by
    'QV4::EngineBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::EngineBase back gives a copy the ritual made for
    Python, in a new cute QV4::EngineBase.
  """

  #  The enums Qt writes inside QV4::EngineBase, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class InternalClassType(CuteNum):
    """
    The enum 'QV4::EngineBase::InternalClassType' of Qt, with the 34 names Qt
    gives in it.
    """

    Class_Empty = Kee[int](0)
    Class_String = Kee[int](1)
    Class_MemberData = Kee[int](2)
    Class_SimpleArrayData = Kee[int](3)
    Class_SparseArrayData = Kee[int](4)
    Class_ExecutionContext = Kee[int](5)
    Class_CallContext = Kee[int](6)
    Class_QmlContext = Kee[int](7)
    Class_Object = Kee[int](8)
    Class_ArrayObject = Kee[int](9)
    Class_FunctionObject = Kee[int](10)
    Class_ArrowFunction = Kee[int](11)
    Class_GeneratorFunction = Kee[int](12)
    Class_GeneratorObject = Kee[int](13)
    Class_StringObject = Kee[int](14)
    Class_SymbolObject = Kee[int](15)
    Class_ScriptFunction = Kee[int](16)
    Class_ConstructorFunction = Kee[int](17)
    Class_MemberFunction = Kee[int](18)
    Class_MemberGeneratorFunction = Kee[int](19)
    Class_ObjectProto = Kee[int](20)
    Class_RegExp = Kee[int](21)
    Class_RegExpObject = Kee[int](22)
    Class_RegExpExecArray = Kee[int](23)
    Class_ArgumentsObject = Kee[int](24)
    Class_StrictArgumentsObject = Kee[int](25)
    Class_ErrorObject = Kee[int](26)
    Class_ErrorObjectWithMessage = Kee[int](27)
    Class_ErrorProto = Kee[int](28)
    Class_QmlContextWrapper = Kee[int](29)
    Class_ProxyObject = Kee[int](30)
    Class_ProxyFunctionObject = Kee[int](31)
    Class_Symbol = Kee[int](32)
    NClasses = Kee[int](33)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::EngineBase'

  #  Qt's '~QV4::EngineBase()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::EngineBase behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV410EngineBaseD1Ev'

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

  @overload(InternalClassType)
  def internalClasses(
      self,
      icType: InternalClassType,
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::EngineBase::internalClasses(InternalClassType icType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-enginebase.html#internalClasses

    Parameters
    ----------

    icType : InternalClassType
      Passed on as its number.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::EngineBase::internalClasses(InternalClassType icType)
    address = self.uglySide.call(
        'ritual_ZN3QV410EngineBase15internalClassesENS0_17InternalClassType'
        'E',
        icType.value,
    )
    return QV4.Heap.InternalClass._cuteAt(address)
