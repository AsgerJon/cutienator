"""
QMetaTypeModuleHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetatype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QMetaTypeModuleHelper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMetaTypeModuleHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaTypeModuleHelper: a plain Python object standing
  in front of one C++ QMetaTypeModuleHelper.

  What exists
  -----------

  No function of Qt's QMetaTypeModuleHelper yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  4 of the 4 functions Qt declares: 4 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QMetaTypeModuleHelper is created at the first use, not by
    'QMetaTypeModuleHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetaTypeModuleHelper.
  - Each name of Qt's QMetaTypeModuleHelper that has no cute function yet,
    'convert_dummy', 'interfaceForType_dummy', 'makePair', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaTypeModuleHelper'

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
  def convert_dummy(*__, **_) -> Never:
    """
    Qt's 'bool QMetaTypeModuleHelper::convert_dummy(const void *a0, int a1,
    void *a2, int a3)': the compiler refuses its ritual as it would be
    written here: templates must have C++ linkage.
    """
    raise NotImplementedError(
        "'QMetaTypeModuleHelper.convert_dummy' has no cute function yet. "
        "Qt's 'bool QMetaTypeModuleHelper::convert_dummy(const void *a0, "
        "int a1, void *a2, int a3)': the compiler refuses its ritual as it "
        "would be written here: templates must have C++ linkage.")

  @staticmethod
  def interfaceForType_dummy(*__, **_) -> Never:
    """
    Qt's 'const QtPrivate::QMetaTypeInterface
    *QMetaTypeModuleHelper::interfaceForType_dummy(int a0)': the compiler
    refuses its ritual as it would be written here: templates must have C++
    linkage.
    """
    raise NotImplementedError(
        "'QMetaTypeModuleHelper.interfaceForType_dummy' has no cute "
        "function yet. Qt's 'const QtPrivate::QMetaTypeInterface "
        "*QMetaTypeModuleHelper::interfaceForType_dummy(int a0)': the "
        "compiler refuses its ritual as it would be written here: templates "
        "must have C++ linkage.")

  @staticmethod
  def makePair(*__, **_) -> Never:
    """
    Qt's 'auto QMetaTypeModuleHelper::makePair(int from, int to)': the
    compiler refuses its ritual as it would be written here: templates must
    have C++ linkage.
    """
    raise NotImplementedError(
        "'QMetaTypeModuleHelper.makePair' has no cute function yet. Qt's "
        "'auto QMetaTypeModuleHelper::makePair(int from, int to)': the "
        "compiler refuses its ritual as it would be written here: templates "
        "must have C++ linkage.")
