"""
QV4::WriteBarrier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4writebarrier_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::WriteBarrier to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class WriteBarrier(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::WriteBarrier: a plain Python object standing in
  front of one C++ QV4::WriteBarrier.

  C++ hands a QV4::WriteBarrier around as a copy, so every C++
  QV4::WriteBarrier behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::WriteBarrier yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::WriteBarrier::write(EngineBase *engine, Heap::Base *base,
    ReturnedValue *slot, ReturnedValue value)': takes a number to change
    where it is.
  - Qt's 'void QV4::WriteBarrier::write_slowpath(EngineBase *engine,
    Heap::Base *base, ReturnedValue *slot, ReturnedValue value)': takes a
    number to change where it is.
  - Qt's 'void QV4::WriteBarrier::write(EngineBase *engine, Heap::Base *base,
    Heap::Base **slot, Heap::Base *value)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QV4::WriteBarrier::write_slowpath(EngineBase *engine,
    Heap::Base *base, Heap::Base **slot, Heap::Base *value)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QV4::WriteBarrier::~WriteBarrier()': the destructor: Python removes
    its C++ QV4::WriteBarrier by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QV4::WriteBarrier is created at the first use, not by
    'QV4::WriteBarrier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::WriteBarrier back gives a copy the ritual made
    for Python, in a new cute QV4::WriteBarrier.
  - Each name of Qt's QV4::WriteBarrier that has no cute function yet,
    'markCustom', 'write', 'write_slowpath', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QV4::WriteBarrier, each a class in here as
  #  in C++.

  class HeapObjectWrapperBase(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::WriteBarrier::HeapObjectWrapperBase: a plain
    Python object standing in front of one C++
    QV4::WriteBarrier::HeapObjectWrapperBase.

    C++ hands a QV4::WriteBarrier::HeapObjectWrapperBase around as a copy, so
    every C++ QV4::WriteBarrier::HeapObjectWrapperBase behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::WriteBarrier::HeapObjectWrapperBase that has
    a ritual and that Python can call so far, 1 name in all: 'clear'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QV4::WriteBarrier::HeapObjectWrapperBase::~HeapObjectWrapperBase()':
      the destructor: Python removes its C++
      QV4::WriteBarrier::HeapObjectWrapperBase by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::WriteBarrier::HeapObjectWrapperBase is created at the
      first use, not by 'QV4::WriteBarrier::HeapObjectWrapperBase(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::WriteBarrier::HeapObjectWrapperBase back gives
      a copy the ritual made for Python, in a new cute
      QV4::WriteBarrier::HeapObjectWrapperBase.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::WriteBarrier::HeapObjectWrapperBase'

    #  Qt's '~QV4::WriteBarrier::HeapObjectWrapperBase()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::WriteBarrier::HeapObjectWrapperBase behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV412WriteBarrier21HeapObjectWrapperBaseD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def clear(self) -> None:
      """
      Calls Qt's 'void QV4::WriteBarrier::HeapObjectWrapperBase::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-writebarrier-heapobjectwrapperbase.html
      """
      #  void QV4::WriteBarrier::HeapObjectWrapperBase::clear()
      self.uglySide.call(
          'ritual_ZN3QV412WriteBarrier21HeapObjectWrapperBase5clearEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::WriteBarrier'

  #  Qt's '~QV4::WriteBarrier()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::WriteBarrier behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412WriteBarrierD1Ev'

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

  @staticmethod
  def markCustom(*__, **_) -> Never:
    """
    Qt's 'QV4::WriteBarrier::markCustom': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.WriteBarrier.markCustom' has no cute function yet. Qt's "
        "'QV4::WriteBarrier::markCustom': a template: a pattern and no "
        "single function.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    - Qt's 'void QV4::WriteBarrier::write(EngineBase *engine, Heap::Base
      *base, ReturnedValue *slot, ReturnedValue value)': takes a number to
      change where it is.
    - Qt's 'void QV4::WriteBarrier::write(EngineBase *engine, Heap::Base
      *base, Heap::Base **slot, Heap::Base *value)': takes a type Python has
      no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.WriteBarrier.write' has no cute function yet. Qt's 'void "
        "QV4::WriteBarrier::write(EngineBase *engine, Heap::Base *base, "
        "ReturnedValue *slot, ReturnedValue value)': takes a number to "
        "change where it is. Qt's 'void QV4::WriteBarrier::write(EngineBase "
        "*engine, Heap::Base *base, Heap::Base **slot, Heap::Base *value)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def write_slowpath(*__, **_) -> Never:
    """
    - Qt's 'void QV4::WriteBarrier::write_slowpath(EngineBase *engine,
      Heap::Base *base, ReturnedValue *slot, ReturnedValue value)': takes a
      number to change where it is.
    - Qt's 'void QV4::WriteBarrier::write_slowpath(EngineBase *engine,
      Heap::Base *base, Heap::Base **slot, Heap::Base *value)': takes a type
      Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.WriteBarrier.write_slowpath' has no cute function yet. Qt's "
        "'void QV4::WriteBarrier::write_slowpath(EngineBase *engine, "
        "Heap::Base *base, ReturnedValue *slot, ReturnedValue value)': "
        "takes a number to change where it is. Qt's 'void "
        "QV4::WriteBarrier::write_slowpath(EngineBase *engine, Heap::Base "
        "*base, Heap::Base **slot, Heap::Base *value)': takes a type Python "
        "has no way to hand over yet.")
