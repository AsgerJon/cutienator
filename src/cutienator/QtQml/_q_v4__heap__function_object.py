"""
QV4::Heap::FunctionObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::FunctionObject to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FunctionObject(QV4.Heap.Object, QV4.Heap.FunctionObjectData):
  """
  The cute side of Qt's QV4::Heap::FunctionObject: a plain Python object
  standing in front of one C++ QV4::Heap::FunctionObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::FunctionObject is built on Qt's QV4::Heap::Object, and has
  everything that class has. It is built on the cute
  'QV4::Heap::FunctionObjectData' as well, as Qt's QV4::Heap::FunctionObject
  is built on Qt's QV4::Heap::FunctionObjectData too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::FunctionObject that has a ritual and that
  Python can call so far, 1 name in all: 'init'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::FunctionObject is created at the first use, not by
    'QV4::Heap::FunctionObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::FunctionObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::FunctionObject'

  #  Qt's QV4::Heap::FunctionObject is built on more than one class. The part
  #  of a C++ QV4::Heap::FunctionObject that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::FunctionObjectData':
          'ritual_cast_QV4_Heap_FunctionObject_QV4_Heap_FunctionObjectData',
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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.String'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.String'])
  @overload(NoneType, NoneType)
  def init(
      self,
      engine: Optional[QV4.ExecutionEngine],
      name: Optional[QV4.String] = None,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::FunctionObject::init(QV4::ExecutionEngine
    *engine, QV4::String *name)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-functionobject.html#init

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QV4::Heap::FunctionObject::init(QV4::ExecutionEngine *engine,
    #      QV4::String *name)
    self.uglySide.call(
        'ritual_ZN3QV44Heap14FunctionObject4initEPNS_15ExecutionEngineEPNS_'
        '6StringE',
        self._addressOf(engine), self._addressOf(name),
    )

  @overload(WAIT['QV4.ExecutionEngine'], str)
  @overload(NoneType, str)
  def init(self, engine: Optional[QV4.ExecutionEngine], name: str) -> None:
    """
    Calls Qt's 'void QV4::Heap::FunctionObject::init(QV4::ExecutionEngine
    *engine, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-functionobject.html#init

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QV4::Heap::FunctionObject::init(QV4::ExecutionEngine *engine,
    #      const QString &name)
    self.uglySide.call(
        'ritual_ZN3QV44Heap14FunctionObject4initEPNS_15ExecutionEngineERK7Q'
        'String',
        self._addressOf(engine), name,
    )

  @overload()
  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::FunctionObject::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-functionobject.html#init
    """
    #  void QV4::Heap::FunctionObject::init()
    self.uglySide.call('ritual_ZN3QV44Heap14FunctionObject4initEv')
