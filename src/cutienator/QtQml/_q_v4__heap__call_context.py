"""
QV4::Heap::CallContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Heap::CallContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CallContext(QV4.Heap.ExecutionContext, QV4.Heap.CallContextData):
  """
  The cute side of Qt's QV4::Heap::CallContext: a plain Python object
  standing in front of one C++ QV4::Heap::CallContext.

  It is built on the cute 'QV4::Heap::ExecutionContext', as Qt's
  QV4::Heap::CallContext is built on Qt's QV4::Heap::ExecutionContext, and
  has everything that class has. It is built on the cute
  'QV4::Heap::CallContextData' as well, as Qt's QV4::Heap::CallContext is
  built on Qt's QV4::Heap::CallContextData too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::CallContext that has a ritual and that
  Python can call so far, 5 names in all: 'markObjects', 'init', 'argc',
  'args', 'setArg'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QV4::Heap::CallContext is created at the first use, not by
    'QV4::Heap::CallContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::CallContext.
  - Each name of Qt's QV4::Heap::CallContext that has no cute function yet,
    'setupLocalTemporalDeadZone', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'void QV4::Heap::CallContext::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-callcontext.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::CallContext::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap11CallContext11markObjectsEPNS0_4BaseEPNS_9MarkS'
        'tackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::CallContext'

  #  Qt's QV4::Heap::CallContext is built on more than one class. The part of
  #  a C++ QV4::Heap::CallContext that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::CallContextData':
          'ritual_cast_QV4_Heap_CallContext_QV4_Heap_CallContextData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def argc(self) -> int:
    """
    Calls Qt's 'int QV4::Heap::CallContext::argc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-callcontext.html#argc
    """
    #  int QV4::Heap::CallContext::argc() const
    return self.uglySide.call('ritual_ZNK3QV44Heap11CallContext4argcEv')

  def args(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::Heap::CallContext::args() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-callcontext.html#args

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::Heap::CallContext::args() const
    address = self.uglySide.call('ritual_ZNK3QV44Heap11CallContext4argsEv')
    return QV4.Value._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, WAIT['QV4.Value'])
  def setArg(self, index: int, v: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::Heap::CallContext::setArg(uint index, Value v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-callcontext.html#setArg

    Parameters
    ----------

    index : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Heap::CallContext::setArg(uint index, Value v)
    self.uglySide.call(
        'ritual_ZN3QV44Heap11CallContext6setArgEjNS_5ValueE',
        index, self._valueOf(v),
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

  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::CallContext::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-callcontext.html#init
    """
    #  void QV4::Heap::CallContext::init()
    self.uglySide.call('ritual_ZN3QV44Heap11CallContext4initEv')

  @staticmethod
  def setupLocalTemporalDeadZone(*__, **_) -> Never:
    """
    Qt's 'QV4::Heap::CallContext::setupLocalTemporalDeadZone': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.Heap.CallContext.setupLocalTemporalDeadZone' has no cute "
        "function yet. Qt's "
        "'QV4::Heap::CallContext::setupLocalTemporalDeadZone': a template: "
        "a pattern and no single function.")
