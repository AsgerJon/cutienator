"""
QV4::GeneratorFunctionCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4generatorobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::GeneratorFunctionCtor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class GeneratorFunctionCtor(QV4.FunctionCtor):
  """
  The cute side of Qt's QV4::GeneratorFunctionCtor: a plain Python object
  standing in front of one C++ QV4::GeneratorFunctionCtor.

  It is built on the cute 'QV4::FunctionCtor', as Qt's
  QV4::GeneratorFunctionCtor is built on Qt's QV4::FunctionCtor, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::GeneratorFunctionCtor that has a ritual and
  that Python can call so far, 3 names in all: '__dataTest', 'd_unchecked',
  'd'. None can be made from Python: one comes out of a function of another
  class that gives one back.

  What has no ritual
  ------------------

  7 of the 10 functions Qt declares: 3 forbidden; 3 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::GeneratorFunctionCtor is created at the first use, not by
    'QV4::GeneratorFunctionCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::GeneratorFunctionCtor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::GeneratorFunctionCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.GeneratorFunctionCtor]:
    """
    Calls Qt's 'QV4::Heap::GeneratorFunctionCtor
    *QV4::GeneratorFunctionCtor::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-generatorfunctionctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.GeneratorFunctionCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::GeneratorFunctionCtor
    #      *QV4::GeneratorFunctionCtor::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV421GeneratorFunctionCtor11d_uncheckedEv',
    )
    return QV4.Heap.GeneratorFunctionCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.GeneratorFunctionCtor]:
    """
    Calls Qt's 'QV4::Heap::GeneratorFunctionCtor
    *QV4::GeneratorFunctionCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-generatorfunctionctor.html#d

    Returns
    -------

    Optional[QV4.Heap.GeneratorFunctionCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::GeneratorFunctionCtor *QV4::GeneratorFunctionCtor::d()
    #      const
    address = self.uglySide.call('ritual_ZNK3QV421GeneratorFunctionCtor1dEv')
    return QV4.Heap.GeneratorFunctionCtor._cuteAt(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::GeneratorFunctionCtor::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-generatorfunctionctor.html#__dataTest
    """
    #  void QV4::GeneratorFunctionCtor::__dataTest()
    self.uglySide.call('ritual_ZN3QV421GeneratorFunctionCtor10__dataTestEv')
