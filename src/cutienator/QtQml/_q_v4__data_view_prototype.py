"""
QV4::DataViewPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4dataview_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::DataViewPrototype to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DataViewPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::DataViewPrototype: a plain Python object
  standing in front of one C++ QV4::DataViewPrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::DataViewPrototype is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  No function of Qt's QV4::DataViewPrototype yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  10 of the 10 functions Qt declares: 6 a template; 3 leans on 'QV4; 1 leans
  on 'unsigned long long QV4.

  What to expect
  --------------

  - The C++ QV4::DataViewPrototype is created at the first use, not by
    'QV4::DataViewPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::DataViewPrototype.
  - Each name of Qt's QV4::DataViewPrototype that has no cute function yet,
    'init', 'method_get', 'method_getChar', 'method_getFloat',
    'method_get_buffer', 'method_get_byteLength', 'method_get_byteOffset',
    'method_set', 'method_setChar', 'method_setFloat', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::DataViewPrototype'

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
    Qt's 'void QV4::DataViewPrototype::init(ExecutionEngine *engine, Object
    *ctor)': leans on 'unsigned long long
    QV4::DataViewPrototype::method_get<int>(QV4::FunctionObject const*,
    QV4::Value const*, QV4::Value const*, int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.init' has no cute function yet. Qt's 'void "
        "QV4::DataViewPrototype::init(ExecutionEngine *engine, Object "
        "*ctor)': leans on 'unsigned long long "
        "QV4::DataViewPrototype::method_get<int>(QV4::FunctionObject "
        "const*, QV4::Value const*, QV4::Value const*, int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_get(*__, **_) -> Never:
    """
    Qt's 'QV4::DataViewPrototype::method_get': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_get' has no cute function yet. Qt's "
        "'QV4::DataViewPrototype::method_get': a template: a pattern and no "
        "single function.")

  @staticmethod
  def method_getChar(*__, **_) -> Never:
    """
    Qt's 'QV4::DataViewPrototype::method_getChar': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_getChar' has no cute function yet. "
        "Qt's 'QV4::DataViewPrototype::method_getChar': a template: a "
        "pattern and no single function.")

  @staticmethod
  def method_getFloat(*__, **_) -> Never:
    """
    Qt's 'QV4::DataViewPrototype::method_getFloat': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_getFloat' has no cute function yet. "
        "Qt's 'QV4::DataViewPrototype::method_getFloat': a template: a "
        "pattern and no single function.")

  @staticmethod
  def method_get_buffer(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DataViewPrototype::method_get_buffer(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::DataView::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_get_buffer' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DataViewPrototype::method_get_buffer(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': leans "
        "on 'QV4::DataView::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def method_get_byteLength(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DataViewPrototype::method_get_byteLength(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::DataView::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_get_byteLength' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DataViewPrototype::method_get_byteLength(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': leans "
        "on 'QV4::DataView::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def method_get_byteOffset(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::DataViewPrototype::method_get_byteOffset(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::DataView::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_get_byteOffset' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::DataViewPrototype::method_get_byteOffset(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': leans "
        "on 'QV4::DataView::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def method_set(*__, **_) -> Never:
    """
    Qt's 'QV4::DataViewPrototype::method_set': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_set' has no cute function yet. Qt's "
        "'QV4::DataViewPrototype::method_set': a template: a pattern and no "
        "single function.")

  @staticmethod
  def method_setChar(*__, **_) -> Never:
    """
    Qt's 'QV4::DataViewPrototype::method_setChar': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_setChar' has no cute function yet. "
        "Qt's 'QV4::DataViewPrototype::method_setChar': a template: a "
        "pattern and no single function.")

  @staticmethod
  def method_setFloat(*__, **_) -> Never:
    """
    Qt's 'QV4::DataViewPrototype::method_setFloat': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.DataViewPrototype.method_setFloat' has no cute function yet. "
        "Qt's 'QV4::DataViewPrototype::method_setFloat': a template: a "
        "pattern and no single function.")
