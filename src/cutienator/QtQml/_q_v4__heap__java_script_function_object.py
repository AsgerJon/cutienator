"""
QV4::Heap::JavaScriptFunctionObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::JavaScriptFunctionObject to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JavaScriptFunctionObject(QV4.Heap.FunctionObject, QV4.Heap.JavaScriptFunctionObjectData):
  """
  The cute side of Qt's QV4::Heap::JavaScriptFunctionObject: a plain Python
  object standing in front of one C++ QV4::Heap::JavaScriptFunctionObject.

  It is built on the cute 'QV4::Heap::FunctionObject', as Qt's
  QV4::Heap::JavaScriptFunctionObject is built on Qt's
  QV4::Heap::FunctionObject, and has everything that class has. It is built
  on the cute 'QV4::Heap::JavaScriptFunctionObjectData' as well, as Qt's
  QV4::Heap::JavaScriptFunctionObject is built on Qt's
  QV4::Heap::JavaScriptFunctionObjectData too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::JavaScriptFunctionObject that has a
  ritual and that Python can call so far, 6 names in all: 'markObjects',
  'init', 'destroy', 'setFunction', 'formalParameterCount', 'varCount'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::JavaScriptFunctionObject is created at the first use,
    not by 'QV4::Heap::JavaScriptFunctionObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::JavaScriptFunctionObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::JavaScriptFunctionObject::markObjects(Heap::Base *b, MarkStack
    *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-javascriptfunctionobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::JavaScriptFunctionObject::markObjects(Heap::Base *b,
    #      MarkStack *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap24JavaScriptFunctionObject11markObjectsEPNS0_4Ba'
        'seEPNS_9MarkStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::JavaScriptFunctionObject'

  #  Qt's QV4::Heap::JavaScriptFunctionObject is built on more than one
  #  class. The part of a C++ QV4::Heap::JavaScriptFunctionObject that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::JavaScriptFunctionObjectData':
          'ritual_cast_QV4_Heap_JavaScriptFunctionObject_QV4_Heap_JavaScriptFunctionObjectData',
  }

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

  @overload(WAIT['QV4.Function'])
  @overload(NoneType)
  def setFunction(self, f: Optional[QV4.Function]) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::JavaScriptFunctionObject::setFunction(Function *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-javascriptfunctionobject.html#setFunction

    Parameters
    ----------

    f : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::JavaScriptFunctionObject::setFunction(Function *f)
    self.uglySide.call(
        'ritual_ZN3QV44Heap24JavaScriptFunctionObject11setFunctionEPNS_8Fun'
        'ctionE',
        self._addressOf(f),
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

  @overload(WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'])
  @overload(WAIT['QV4.ExecutionContext'], NoneType)
  @overload(NoneType, WAIT['QV4.Function'])
  @overload(NoneType, NoneType)
  @overload(
      WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], WAIT['QV4.String'],
  )
  @overload(WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'], NoneType)
  @overload(WAIT['QV4.ExecutionContext'], NoneType, WAIT['QV4.String'])
  @overload(WAIT['QV4.ExecutionContext'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.Function'], WAIT['QV4.String'])
  @overload(NoneType, WAIT['QV4.Function'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.String'])
  @overload(NoneType, NoneType, NoneType)
  def init(
      self,
      scope: Optional[QV4.ExecutionContext],
      function: Optional[QV4.Function],
      n: Optional[QV4.String] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::JavaScriptFunctionObject::init(QV4::ExecutionContext *scope,
    QV4::Function *function, QV4::String *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-javascriptfunctionobject.html#init

    Parameters
    ----------

    scope : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QV4::Heap::JavaScriptFunctionObject::init(QV4::ExecutionContext
    #      *scope, QV4::Function *function, QV4::String *n)
    self.uglySide.call(
        'ritual_ZN3QV44Heap24JavaScriptFunctionObject4initEPNS_16ExecutionC'
        'ontextEPNS_8FunctionEPNS_6StringE',
        self._addressOf(scope), self._addressOf(function),
        self._addressOf(n),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::JavaScriptFunctionObject::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-javascriptfunctionobject.html#destroy
    """
    #  void QV4::Heap::JavaScriptFunctionObject::destroy()
    self.uglySide.call(
        'ritual_ZN3QV44Heap24JavaScriptFunctionObject7destroyEv',
    )

  def formalParameterCount(self) -> int:
    """
    Calls Qt's 'unsigned int
    QV4::Heap::JavaScriptFunctionObject::formalParameterCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-javascriptfunctionobject.html
    """
    #  unsigned int
    #      QV4::Heap::JavaScriptFunctionObject::formalParameterCount()
    return self.uglySide.call(
        'ritual_ZN3QV44Heap24JavaScriptFunctionObject20formalParameterCount'
        'Ev',
    )

  def varCount(self) -> int:
    """
    Calls Qt's 'unsigned int
    QV4::Heap::JavaScriptFunctionObject::varCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-javascriptfunctionobject.html#varCount
    """
    #  unsigned int QV4::Heap::JavaScriptFunctionObject::varCount()
    return self.uglySide.call(
        'ritual_ZN3QV44Heap24JavaScriptFunctionObject8varCountEv',
    )
