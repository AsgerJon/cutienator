"""
QV4::Heap::GeneratorFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4generatorobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::GeneratorFunction to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class GeneratorFunction(QV4.Heap.ArrowFunction):
  """
  The cute side of Qt's QV4::Heap::GeneratorFunction: a plain Python object
  standing in front of one C++ QV4::Heap::GeneratorFunction.

  It is built on the cute 'QV4::Heap::ArrowFunction', as Qt's
  QV4::Heap::GeneratorFunction is built on Qt's QV4::Heap::ArrowFunction, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::GeneratorFunction that has a ritual and
  that Python can call so far, 1 name in all: 'init'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::GeneratorFunction is created at the first use, not by
    'QV4::Heap::GeneratorFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::GeneratorFunction.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::GeneratorFunction'

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
      name: Optional[QV4.String] = None,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::GeneratorFunction::init(QV4::ExecutionContext
    *scope, Function *function, QV4::String *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-generatorfunction.html#init

    Parameters
    ----------

    scope : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QV4::Heap::GeneratorFunction::init(QV4::ExecutionContext *scope,
    #      Function *function, QV4::String *name)
    self.uglySide.call(
        'ritual_ZN3QV44Heap17GeneratorFunction4initEPNS_16ExecutionContextE'
        'PNS_8FunctionEPNS_6StringE',
        self._addressOf(scope), self._addressOf(function),
        self._addressOf(name),
    )
