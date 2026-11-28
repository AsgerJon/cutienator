"""
QV4::Heap::QmlContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Heap::QmlContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QmlContext(QV4.Heap.ExecutionContext, QV4.Heap.QmlContextData):
  """
  The cute side of Qt's QV4::Heap::QmlContext: a plain Python object standing
  in front of one C++ QV4::Heap::QmlContext.

  It is built on the cute 'QV4::Heap::ExecutionContext', as Qt's
  QV4::Heap::QmlContext is built on Qt's QV4::Heap::ExecutionContext, and has
  everything that class has. It is built on the cute
  'QV4::Heap::QmlContextData' as well, as Qt's QV4::Heap::QmlContext is built
  on Qt's QV4::Heap::QmlContextData too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QmlContext that has a ritual and that
  Python can call so far, 3 names in all: 'markObjects', 'qml', 'init'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::QmlContext is created at the first use, not by
    'QV4::Heap::QmlContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QmlContext.
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
    Calls Qt's 'void QV4::Heap::QmlContext::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmlcontext.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QmlContext::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap10QmlContext11markObjectsEPNS0_4BaseEPNS_9MarkSt'
        'ackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::QmlContext'

  #  Qt's QV4::Heap::QmlContext is built on more than one class. The part of
  #  a C++ QV4::Heap::QmlContext that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::QmlContextData':
          'ritual_cast_QV4_Heap_QmlContext_QV4_Heap_QmlContextData',
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

  def qml(self) -> Optional[QV4.Heap.QQmlContextWrapper]:
    """
    Calls Qt's 'QQmlContextWrapper *QV4::Heap::QmlContext::qml()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qmlcontext.html#qml

    Returns
    -------

    Optional[QV4.Heap.QQmlContextWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContextWrapper *QV4::Heap::QmlContext::qml()
    address = self.uglySide.call('ritual_ZN3QV44Heap10QmlContext3qmlEv')
    return QV4.Heap.QQmlContextWrapper._cuteAt(address)

  @overload(WAIT['QV4.ExecutionContext'], WAIT['QV4.QQmlContextWrapper'])
  @overload(WAIT['QV4.ExecutionContext'], NoneType)
  @overload(NoneType, WAIT['QV4.QQmlContextWrapper'])
  @overload(NoneType, NoneType)
  def init(
      self,
      outerContext: Optional[QV4.ExecutionContext],
      qml: Optional[QV4.QQmlContextWrapper],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::QmlContext::init(QV4::ExecutionContext
    *outerContext, QV4::QQmlContextWrapper *qml)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qmlcontext.html#init

    Parameters
    ----------

    outerContext : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qml : Optional[QV4.QQmlContextWrapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QmlContext::init(QV4::ExecutionContext *outerContext,
    #      QV4::QQmlContextWrapper *qml)
    self.uglySide.call(
        'ritual_ZN3QV44Heap10QmlContext4initEPNS_16ExecutionContextEPNS_18Q'
        'QmlContextWrapperE',
        self._addressOf(outerContext), self._addressOf(qml),
    )
