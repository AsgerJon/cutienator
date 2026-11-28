"""
QQmlDateExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllocale_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlDateExtension to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlDateExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDateExtension: a plain Python object standing in
  front of one C++ QQmlDateExtension.

  C++ hands a QQmlDateExtension around as a copy, so every C++
  QQmlDateExtension behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlDateExtension yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDateExtension::~QQmlDateExtension()': the destructor: Python
    removes its C++ QQmlDateExtension by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 9 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQmlDateExtension.

  What to expect
  --------------

  - The C++ QQmlDateExtension is created at the first use, not by
    'QQmlDateExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDateExtension back gives a copy the ritual made
    for Python, in a new cute QQmlDateExtension.
  - Each name of Qt's QQmlDateExtension that has no cute function yet,
    'method_fromLocaleDateString', 'method_fromLocaleString',
    'method_fromLocaleTimeString', 'method_timeZoneUpdated',
    'method_toLocaleDateString', 'method_toLocaleString',
    'method_toLocaleTimeString', 'registerExtension', holds a function that
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
  __qt_class__ = 'QQmlDateExtension'

  #  Qt's '~QQmlDateExtension()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlDateExtension behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQmlDateExtensionD1Ev'

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
  def method_fromLocaleDateString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QQmlDateExtension::method_fromLocaleDateString(const QV4::FunctionObject
    *a0, const QV4::Value *thisObject, const QV4::Value *argv, int argc)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'ReturnedValue'.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.method_fromLocaleDateString' has no cute "
        "function yet. Qt's 'QV4::ReturnedValue "
        "QQmlDateExtension::method_fromLocaleDateString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'.")

  @staticmethod
  def method_fromLocaleString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDateExtension::method_fromLocaleString(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'ReturnedValue'; did you mean 'QV4::ReturnedValue'?.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.method_fromLocaleString' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDateExtension::method_fromLocaleString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'; did you mean "
        "'QV4::ReturnedValue'?.")

  @staticmethod
  def method_fromLocaleTimeString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QQmlDateExtension::method_fromLocaleTimeString(const QV4::FunctionObject
    *a0, const QV4::Value *thisObject, const QV4::Value *argv, int argc)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'ReturnedValue'.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.method_fromLocaleTimeString' has no cute "
        "function yet. Qt's 'QV4::ReturnedValue "
        "QQmlDateExtension::method_fromLocaleTimeString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'.")

  @staticmethod
  def method_timeZoneUpdated(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDateExtension::method_timeZoneUpdated(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'ReturnedValue'.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.method_timeZoneUpdated' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDateExtension::method_timeZoneUpdated(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'.")

  @staticmethod
  def method_toLocaleDateString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QQmlDateExtension::method_toLocaleDateString(const QV4::FunctionObject
    *a0, const QV4::Value *thisObject, const QV4::Value *argv, int argc)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'ReturnedValue'; did you
    mean 'QV4::ReturnedValue'?.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.method_toLocaleDateString' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDateExtension::method_toLocaleDateString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'; did you mean "
        "'QV4::ReturnedValue'?.")

  @staticmethod
  def method_toLocaleString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDateExtension::method_toLocaleString(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'ReturnedValue'; did you mean 'QV4::ReturnedValue'?.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.method_toLocaleString' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDateExtension::method_toLocaleString(const QV4::FunctionObject "
        "*a0, const QV4::Value *thisObject, const QV4::Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'ReturnedValue'; did you mean 'QV4::ReturnedValue'?.")

  @staticmethod
  def method_toLocaleTimeString(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QQmlDateExtension::method_toLocaleTimeString(const QV4::FunctionObject
    *a0, const QV4::Value *thisObject, const QV4::Value *argv, int argc)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'ReturnedValue'; did you
    mean 'QV4::ReturnedValue'?.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.method_toLocaleTimeString' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDateExtension::method_toLocaleTimeString(const "
        "QV4::FunctionObject *a0, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ReturnedValue'; did you mean "
        "'QV4::ReturnedValue'?.")

  @staticmethod
  def registerExtension(*__, **_) -> Never:
    """
    Qt's 'void QQmlDateExtension::registerExtension(QV4::ExecutionEngine
    *engine)': leans on
    'QQmlDateExtension::method_toLocaleString(QV4::FunctionObject const*,
    QV4::Value const*, QV4::Value const*, int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDateExtension.registerExtension' has no cute function yet. "
        "Qt's 'void "
        "QQmlDateExtension::registerExtension(QV4::ExecutionEngine "
        "*engine)': leans on "
        "'QQmlDateExtension::method_toLocaleString(QV4::FunctionObject "
        "const*, QV4::Value const*, QV4::Value const*, int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
