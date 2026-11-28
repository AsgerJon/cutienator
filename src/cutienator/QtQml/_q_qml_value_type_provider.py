"""
QQmlValueTypeProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlValueTypeProvider to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlValueTypeProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlValueTypeProvider: a plain Python object standing
  in front of one C++ QQmlValueTypeProvider.

  C++ hands a QQmlValueTypeProvider around as a copy, so every C++
  QQmlValueTypeProvider behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlValueTypeProvider yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlValueTypeProvider::heapCreateValueType(const QQmlType
    &targetType, const QV4::Value &source, QV4::ExecutionEngine *engine)':
    gives 'void', which has no cute class yet.
  - Qt's 'QVariant QQmlValueTypeProvider::constructValueType(QMetaType
    targetMetaType, const QMetaObject *targetMetaObject, int ctorIndex, void
    **args)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlValueTypeProvider::~QQmlValueTypeProvider()': the destructor:
    Python removes its C++ QQmlValueTypeProvider by it, and has no other use
    for it.

  What has no ritual
  ------------------

  6 of the 9 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlValueTypeProvider is created at the first use, not by
    'QQmlValueTypeProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlValueTypeProvider back gives a copy the ritual
    made for Python, in a new cute QQmlValueTypeProvider.
  - Each name of Qt's QQmlValueTypeProvider that has no cute function yet,
    'constructValueType', 'createValueType', 'heapCreateValueType',
    'populateValueType', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlValueTypeProvider'

  #  Qt's '~QQmlValueTypeProvider()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlValueTypeProvider behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQmlValueTypeProviderD1Ev'

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
  def constructValueType(*__, **_) -> Never:
    """
    Qt's 'QVariant QQmlValueTypeProvider::constructValueType(QMetaType
    targetMetaType, const QMetaObject *targetMetaObject, int ctorIndex, void
    **args)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlValueTypeProvider.constructValueType' has no cute function "
        "yet. Qt's 'QVariant "
        "QQmlValueTypeProvider::constructValueType(QMetaType "
        "targetMetaType, const QMetaObject *targetMetaObject, int "
        "ctorIndex, void **args)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def createValueType(*__, **_) -> Never:
    """
    - Qt's 'QVariant QQmlValueTypeProvider::createValueType(const QJSValue
      &a0, QMetaType a1)': Qt's library has no name for it, and its code in
      Qt's source does not compile apart from its file: use of undeclared
      identifier 'isConstructibleMetaType'.
    - Qt's 'QVariant QQmlValueTypeProvider::createValueType(const QString
      &a0, QMetaType a1)': Qt's library has no name for it, and its code in
      Qt's source does not compile apart from its file: use of undeclared
      identifier 'isConstructibleMetaType'.
    - Qt's 'QVariant QQmlValueTypeProvider::createValueType(const QV4::Value
      &a0, QMetaType a1, QV4::ExecutionEngine *a2)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'isConstructibleMetaType'.
    - Qt's 'QVariant QQmlValueTypeProvider::createValueType(const QVariant
      &a0, QMetaType a1, QV4::ExecutionEngine *a2)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'isConstructibleMetaType'.
    """
    raise NotImplementedError(
        "'QQmlValueTypeProvider.createValueType' has no cute function yet. "
        "Qt's 'QVariant QQmlValueTypeProvider::createValueType(const "
        "QJSValue &a0, QMetaType a1)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'isConstructibleMetaType'. Qt's 'QVariant "
        "QQmlValueTypeProvider::createValueType(const QString &a0, "
        "QMetaType a1)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isConstructibleMetaType'. Qt's 'QVariant "
        "QQmlValueTypeProvider::createValueType(const QV4::Value &a0, "
        "QMetaType a1, QV4::ExecutionEngine *a2)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'isConstructibleMetaType'. "
        "Qt's 'QVariant QQmlValueTypeProvider::createValueType(const "
        "QVariant &a0, QMetaType a1, QV4::ExecutionEngine *a2)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'isConstructibleMetaType'.")

  @staticmethod
  def heapCreateValueType(*__, **_) -> Never:
    """
    Qt's 'void *QQmlValueTypeProvider::heapCreateValueType(const QQmlType
    &targetType, const QV4::Value &source, QV4::ExecutionEngine *engine)':
    gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlValueTypeProvider.heapCreateValueType' has no cute function "
        "yet. Qt's 'void *QQmlValueTypeProvider::heapCreateValueType(const "
        "QQmlType &targetType, const QV4::Value &source, "
        "QV4::ExecutionEngine *engine)': gives 'void', which has no cute "
        "class yet.")

  @staticmethod
  def populateValueType(*__, **_) -> Never:
    """
    - Qt's 'bool QQmlValueTypeProvider::populateValueType(QMetaType
      targetMetaType, void *target, QMetaType sourceMetaType, void *source,
      QV4::ExecutionEngine *engine)': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'isConstructibleMetaType'.
    - Qt's 'bool QQmlValueTypeProvider::populateValueType(QMetaType
      targetMetaType, void *target, const QV4::Value &source,
      QV4::ExecutionEngine *engine)': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'createOrConstructValueType'.
    """
    raise NotImplementedError(
        "'QQmlValueTypeProvider.populateValueType' has no cute function "
        "yet. Qt's 'bool QQmlValueTypeProvider::populateValueType(QMetaType "
        "targetMetaType, void *target, QMetaType sourceMetaType, void "
        "*source, QV4::ExecutionEngine *engine)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'isConstructibleMetaType'. "
        "Qt's 'bool QQmlValueTypeProvider::populateValueType(QMetaType "
        "targetMetaType, void *target, const QV4::Value &source, "
        "QV4::ExecutionEngine *engine)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'createOrConstructValueType'.")
