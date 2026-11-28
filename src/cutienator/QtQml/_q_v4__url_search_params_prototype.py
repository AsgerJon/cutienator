"""
QV4::UrlSearchParamsPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::UrlSearchParamsPrototype to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class UrlSearchParamsPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::UrlSearchParamsPrototype: a plain Python object
  standing in front of one C++ QV4::UrlSearchParamsPrototype.

  It is built on the cute 'QV4::Object', as Qt's
  QV4::UrlSearchParamsPrototype is built on Qt's QV4::Object, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::UrlSearchParamsPrototype that has a ritual and
  that Python can call so far, 1 name in all: 'defaultPrototype'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  13 of the 14 functions Qt declares: 12 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::UrlSearchParamsPrototype is created at the first use, not by
    'QV4::UrlSearchParamsPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::UrlSearchParamsPrototype.
  - Each name of Qt's QV4::UrlSearchParamsPrototype that has no cute function
    yet, 'init', 'method_append', 'method_delete', 'method_entries',
    'method_forEach', 'method_get', 'method_getAll', 'method_has',
    'method_keys', 'method_set', 'method_sort', 'method_toString',
    'method_values', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    *QV4::UrlSearchParamsPrototype::defaultPrototype(QV4::ExecutionEngine
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsprototype.html#defaultPrototype

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
    #  QV4::Object *QV4::UrlSearchParamsPrototype::defaultPrototype(QV4::
    #      ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV424UrlSearchParamsPrototype16defaultPrototypeEPNS_15Ex'
        'ecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::UrlSearchParamsPrototype'

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
    Qt's 'void QV4::UrlSearchParamsPrototype::init(ExecutionEngine *engine,
    Object *ctor)': leans on
    'QV4::UrlSearchParamsPrototype::method_get(QV4::FunctionObject const*,
    QV4::Value const*, QV4::Value const*, int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.init' has no cute function yet. Qt's "
        "'void QV4::UrlSearchParamsPrototype::init(ExecutionEngine *engine, "
        "Object *ctor)': leans on "
        "'QV4::UrlSearchParamsPrototype::method_get(QV4::FunctionObject "
        "const*, QV4::Value const*, QV4::Value const*, int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_append(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_append(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_append' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_append(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_delete(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_delete(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_delete' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_delete(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_entries(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_entries(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_entries' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_entries(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_forEach(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_forEach(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_forEach' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_forEach(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_get(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_get(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_get' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_get(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_getAll(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_getAll(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_getAll' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_getAll(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_has(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_has(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_has' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_has(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_keys(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_keys(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_keys' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_keys(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_set(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_set(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_set' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_set(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_sort(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_sort(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_sort' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_sort(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")

  @staticmethod
  def method_toString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_toString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_toString' has no cute "
        "function yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_toString(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkSearchParamsType'.")

  @staticmethod
  def method_values(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlSearchParamsPrototype::method_values(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkSearchParamsType'.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsPrototype.method_values' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlSearchParamsPrototype::method_values(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkSearchParamsType'.")
