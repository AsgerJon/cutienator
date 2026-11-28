"""
QV4::FunctionCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::FunctionCtor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class FunctionCtor(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::FunctionCtor: a plain Python object standing in
  front of one C++ QV4::FunctionCtor.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::FunctionCtor is
  built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::FunctionCtor that has a ritual and that Python
  can call so far, 3 names in all: '__dataTest', 'd_unchecked', 'd'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  8 of the 11 functions Qt declares: 3 forbidden; 3 leans on 'QV4; 1 not a
  gap; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::FunctionCtor is created at the first use, not by
    'QV4::FunctionCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::FunctionCtor.
  - Each name of Qt's QV4::FunctionCtor that has no cute function yet,
    'parse', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QV4::FunctionCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.FunctionCtor]:
    """
    Calls Qt's 'QV4::Heap::FunctionCtor *QV4::FunctionCtor::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.FunctionCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::FunctionCtor *QV4::FunctionCtor::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412FunctionCtor11d_uncheckedEv',
    )
    return QV4.Heap.FunctionCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.FunctionCtor]:
    """
    Calls Qt's 'QV4::Heap::FunctionCtor *QV4::FunctionCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionctor.html#d

    Returns
    -------

    Optional[QV4.Heap.FunctionCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::FunctionCtor *QV4::FunctionCtor::d() const
    address = self.uglySide.call('ritual_ZNK3QV412FunctionCtor1dEv')
    return QV4.Heap.FunctionCtor._cuteAt(address)

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
    Calls Qt's 'void QV4::FunctionCtor::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-functionctor.html#__dataTest
    """
    #  void QV4::FunctionCtor::__dataTest()
    self.uglySide.call('ritual_ZN3QV412FunctionCtor10__dataTestEv')

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::FunctionCtor::parse(ExecutionEngine *engine, const Value *argv, int
    argc, Type t)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: variable has incomplete type
    'QQmlJS::Lexer'.
    """
    raise NotImplementedError(
        "'QV4.FunctionCtor.parse' has no cute function yet. Qt's "
        "'QQmlRefPointer<ExecutableCompilationUnit> "
        "QV4::FunctionCtor::parse(ExecutionEngine *engine, const Value "
        "*argv, int argc, Type t)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "variable has incomplete type 'QQmlJS::Lexer'.")
