"""
QV4::PropertyListPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::PropertyListPrototype to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class PropertyListPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::PropertyListPrototype: a plain Python object
  standing in front of one C++ QV4::PropertyListPrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::PropertyListPrototype
  is built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::PropertyListPrototype that has a ritual and
  that Python can call so far, 1 name in all: 'defaultPrototype'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  11 of the 12 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::PropertyListPrototype is created at the first use, not by
    'QV4::PropertyListPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::PropertyListPrototype.
  - Each name of Qt's QV4::PropertyListPrototype that has no cute function
    yet, 'init', 'method_get_length', 'method_indexOf', 'method_lastIndexOf',
    'method_pop', 'method_push', 'method_set_length', 'method_shift',
    'method_sort', 'method_splice', 'method_unshift', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::PropertyListPrototype::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertylistprototype.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object
    #      *QV4::PropertyListPrototype::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV421PropertyListPrototype16defaultPrototypeEPNS_15Execu'
        'tionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::PropertyListPrototype'

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
  def init(*__, **_) -> Never:
    """
    Qt's 'void QV4::PropertyListPrototype::init()': leans on
    'QV4::ArrayElementLessThan::operator()(QV4::Value, QV4::Value) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.init' has no cute function yet. Qt's "
        "'void QV4::PropertyListPrototype::init()': leans on "
        "'QV4::ArrayElementLessThan::operator()(QV4::Value, QV4::Value) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def method_get_length(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_get_length(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching constructor for
    initialization of 'Scope'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_get_length' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::PropertyListPrototype::method_get_length(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching constructor for "
        "initialization of 'Scope'.")

  @staticmethod
  def method_indexOf(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_indexOf(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching function for call to
    'firstOrLastIndexOf'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_indexOf' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::PropertyListPrototype::method_indexOf(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching function for call to "
        "'firstOrLastIndexOf'.")

  @staticmethod
  def method_lastIndexOf(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_lastIndexOf(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'firstOrLastIndexOf'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_lastIndexOf' has no cute "
        "function yet. Qt's 'ReturnedValue "
        "QV4::PropertyListPrototype::method_lastIndexOf(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'firstOrLastIndexOf'.")

  @staticmethod
  def method_pop(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_pop(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching constructor for
    initialization of 'Scope'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_pop' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::PropertyListPrototype::method_pop(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching "
        "constructor for initialization of 'Scope'.")

  @staticmethod
  def method_push(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_push(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching constructor for
    initialization of 'Scope'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_push' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::PropertyListPrototype::method_push(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching "
        "constructor for initialization of 'Scope'.")

  @staticmethod
  def method_set_length(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_set_length(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching constructor for
    initialization of 'QV4::Scope'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_set_length' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::PropertyListPrototype::method_set_length(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching constructor for "
        "initialization of 'QV4::Scope'.")

  @staticmethod
  def method_shift(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_shift(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching constructor for
    initialization of 'Scope'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_shift' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::PropertyListPrototype::method_shift(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching "
        "constructor for initialization of 'Scope'.")

  @staticmethod
  def method_sort(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_sort(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::ArrayElementLessThan::operator()(QV4::Value,
    QV4::Value) const', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_sort' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::PropertyListPrototype::method_sort(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on "
        "'QV4::ArrayElementLessThan::operator()(QV4::Value, QV4::Value) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def method_splice(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_splice(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching constructor for
    initialization of 'Scope'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_splice' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::PropertyListPrototype::method_splice(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching constructor for "
        "initialization of 'Scope'.")

  @staticmethod
  def method_unshift(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::PropertyListPrototype::method_unshift(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching constructor for
    initialization of 'Scope'.
    """
    raise NotImplementedError(
        "'QV4.PropertyListPrototype.method_unshift' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::PropertyListPrototype::method_unshift(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching constructor for "
        "initialization of 'Scope'.")
