"""
QV4::Heap::ExecutionContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Heap::ExecutionContext to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExecutionContext(QV4.Heap.Base, QV4.Heap.ExecutionContextData):
  """
  The cute side of Qt's QV4::Heap::ExecutionContext: a plain Python object
  standing in front of one C++ QV4::Heap::ExecutionContext.

  It is built on the cute 'QV4::Heap::Base', as Qt's
  QV4::Heap::ExecutionContext is built on Qt's QV4::Heap::Base, and has
  everything that class has. It is built on the cute
  'QV4::Heap::ExecutionContextData' as well, as Qt's
  QV4::Heap::ExecutionContext is built on Qt's
  QV4::Heap::ExecutionContextData too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::ExecutionContext that has a ritual and
  that Python can call so far, 2 names in all: 'markObjects', 'init'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const VTable *QV4::Heap::ExecutionContext::vtable() const': gives
    'QV4::VTable', which has no cute class yet.

  What to expect
  --------------

  - The C++ QV4::Heap::ExecutionContext is created at the first use, not by
    'QV4::Heap::ExecutionContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::ExecutionContext.
  - Each name of Qt's QV4::Heap::ExecutionContext that has no cute function
    yet, 'vtable', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QV4::Heap::ExecutionContext, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ContextType(CuteNum):
    """
    The enum 'QV4::Heap::ExecutionContext::ContextType' of Qt, with the 5
    names Qt gives in it.
    """

    Type_GlobalContext = Kee[int](1)
    Type_WithContext = Kee[int](2)
    Type_QmlContext = Kee[int](3)
    Type_BlockContext = Kee[int](4)
    Type_CallContext = Kee[int](5)

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
    Calls Qt's 'void QV4::Heap::ExecutionContext::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-executioncontext.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ExecutionContext::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap16ExecutionContext11markObjectsEPNS0_4BaseEPNS_9'
        'MarkStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ExecutionContext'

  #  Qt's QV4::Heap::ExecutionContext is built on more than one class. The
  #  part of a C++ QV4::Heap::ExecutionContext that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::ExecutionContextData':
          'ritual_cast_QV4_Heap_ExecutionContext_QV4_Heap_ExecutionContextData',
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

  @overload(ContextType)
  def init(self, t: ContextType) -> None:
    """
    Calls Qt's 'void QV4::Heap::ExecutionContext::init(ContextType t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-executioncontext.html#init

    Parameters
    ----------

    t : ContextType
      Passed on as its number.
    """
    #  void QV4::Heap::ExecutionContext::init(ContextType t)
    self.uglySide.call(
        'ritual_ZN3QV44Heap16ExecutionContext4initENS1_11ContextTypeE',
        t.value,
    )

  @staticmethod
  def vtable(*__, **_) -> Never:
    """
    Qt's 'const VTable *QV4::Heap::ExecutionContext::vtable() const': gives
    'QV4::VTable', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.ExecutionContext.vtable' has no cute function yet. Qt's "
        "'const VTable *QV4::Heap::ExecutionContext::vtable() const': gives "
        "'QV4::VTable', which has no cute class yet.")
