"""
QV4::WeakMapPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4mapobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::WeakMapPrototype to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class WeakMapPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::WeakMapPrototype: a plain Python object standing
  in front of one C++ QV4::WeakMapPrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::WeakMapPrototype is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  No function of Qt's QV4::WeakMapPrototype yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 5 functions Qt declares: 5 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::WeakMapPrototype is created at the first use, not by
    'QV4::WeakMapPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::WeakMapPrototype.
  - Each name of Qt's QV4::WeakMapPrototype that has no cute function yet,
    'init', 'method_delete', 'method_get', 'method_has', 'method_set', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::WeakMapPrototype'

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
    Qt's 'void QV4::WeakMapPrototype::init(ExecutionEngine *engine, Object
    *ctor)': leans on 'QV4::MapObject::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.WeakMapPrototype.init' has no cute function yet. Qt's 'void "
        "QV4::WeakMapPrototype::init(ExecutionEngine *engine, Object "
        "*ctor)': leans on 'QV4::MapObject::static_vtbl', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def method_delete(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::WeakMapPrototype::method_delete(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.WeakMapPrototype.method_delete' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::WeakMapPrototype::method_delete(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_get(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::WeakMapPrototype::method_get(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.WeakMapPrototype.method_get' has no cute function yet. Qt's "
        "'ReturnedValue QV4::WeakMapPrototype::method_get(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_has(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::WeakMapPrototype::method_has(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.WeakMapPrototype.method_has' has no cute function yet. Qt's "
        "'ReturnedValue QV4::WeakMapPrototype::method_has(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_set(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::WeakMapPrototype::method_set(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.WeakMapPrototype.method_set' has no cute function yet. Qt's "
        "'ReturnedValue QV4::WeakMapPrototype::method_set(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::MapObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
