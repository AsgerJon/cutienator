"""
QQmlNumberExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllocale_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlNumberExtension to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlNumberExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlNumberExtension: a plain Python object standing
  in front of one C++ QQmlNumberExtension.

  C++ hands a QQmlNumberExtension around as a copy, so every C++
  QQmlNumberExtension behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlNumberExtension yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlNumberExtension::~QQmlNumberExtension()': the destructor:
    Python removes its C++ QQmlNumberExtension by it, and has no other use
    for it.

  What has no ritual
  ------------------

  4 of the 5 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQmlNumberExtension.

  What to expect
  --------------

  - The C++ QQmlNumberExtension is created at the first use, not by
    'QQmlNumberExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlNumberExtension back gives a copy the ritual made
    for Python, in a new cute QQmlNumberExtension.
  - Each name of Qt's QQmlNumberExtension that has no cute function yet,
    'method_fromLocaleString', 'method_toLocaleCurrencyString',
    'method_toLocaleString', 'registerExtension', holds a function that
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
  __qt_class__ = 'QQmlNumberExtension'

  #  Qt's '~QQmlNumberExtension()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlNumberExtension behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlNumberExtensionD1Ev'

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
  def method_fromLocaleString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QQmlNumberExtension::method_fromLocaleString(const QV4::FunctionObject
    *a0, const QV4::Value *thisObject, const QV4::Value *argv, int argc)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'ReturnedValue'; did you
    mean 'QV4::ReturnedValue'?.
    """
    raise NotImplementedError(
        "'QQmlNumberExtension.method_fromLocaleString' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlNumberExtension::method_fromLocaleString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'; did you mean "
        "'QV4::ReturnedValue'?.")

  @staticmethod
  def method_toLocaleCurrencyString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QQmlNumberExtension::method_toLocaleCurrencyString(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'ReturnedValue'; did you mean 'QV4::ReturnedValue'?.
    """
    raise NotImplementedError(
        "'QQmlNumberExtension.method_toLocaleCurrencyString' has no cute "
        "function yet. Qt's 'QV4::ReturnedValue "
        "QQmlNumberExtension::method_toLocaleCurrencyString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'; did you mean "
        "'QV4::ReturnedValue'?.")

  @staticmethod
  def method_toLocaleString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlNumberExtension::method_toLocaleString(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'THROW_ERROR'.
    """
    raise NotImplementedError(
        "'QQmlNumberExtension.method_toLocaleString' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlNumberExtension::method_toLocaleString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'THROW_ERROR'.")

  @staticmethod
  def registerExtension(*__, **_) -> Never:
    """
    Qt's 'void QQmlNumberExtension::registerExtension(QV4::ExecutionEngine
    *engine)': leans on
    'QQmlNumberExtension::method_toLocaleString(QV4::FunctionObject const*,
    QV4::Value const*, QV4::Value const*, int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlNumberExtension.registerExtension' has no cute function yet. "
        "Qt's 'void "
        "QQmlNumberExtension::registerExtension(QV4::ExecutionEngine "
        "*engine)': leans on "
        "'QQmlNumberExtension::method_toLocaleString(QV4::FunctionObject "
        "const*, QV4::Value const*, QV4::Value const*, int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
