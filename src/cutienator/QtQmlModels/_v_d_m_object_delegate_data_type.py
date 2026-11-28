"""
VDMObjectDelegateDataType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means VDMObjectDelegateDataType to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class VDMObjectDelegateDataType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's VDMObjectDelegateDataType: a plain Python object
  standing in front of one C++ VDMObjectDelegateDataType.

  C++ hands a VDMObjectDelegateDataType around as a copy, so every C++
  VDMObjectDelegateDataType behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's VDMObjectDelegateDataType yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int VDMObjectDelegateDataType::rowCount(const QQmlAdaptorModel
    &model) const': takes a type Python has no way to hand over yet.
  - Qt's 'int VDMObjectDelegateDataType::columnCount(const QQmlAdaptorModel
    &a0) const': takes a type Python has no way to hand over yet.
  - Qt's 'QVariant VDMObjectDelegateDataType::value(const QQmlAdaptorModel
    &model, int index, const QString &role) const': takes a type Python has
    no way to hand over yet.
  - Qt's 'void VDMObjectDelegateDataType::cleanup(QQmlAdaptorModel &a0)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'VDMObjectDelegateDataType::~VDMObjectDelegateDataType()': the
    destructor: Python removes its C++ VDMObjectDelegateDataType by it, and
    has no other use for it.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 5 leans on 'QQmlDMObjectData.

  What to expect
  --------------

  - The C++ VDMObjectDelegateDataType is created at the first use, not by
    'VDMObjectDelegateDataType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a VDMObjectDelegateDataType back gives a copy the
    ritual made for Python, in a new cute VDMObjectDelegateDataType.
  - Each name of Qt's VDMObjectDelegateDataType that has no cute function
    yet, '__init__', 'initializeMetaObject', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'VDMObjectDelegateDataType'

  #  Qt's '~VDMObjectDelegateDataType()'. Naming it makes this a value class:
  #  Python owns every C++ VDMObjectDelegateDataType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25VDMObjectDelegateDataTypeD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's
      'VDMObjectDelegateDataType::VDMObjectDelegateDataType(QQmlAdaptorModel
      *model)': leans on 'QQmlDMObjectData::modelDataChanged()', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'VDMObjectDelegateDataType::VDMObjectDelegateDataType(const
      VDMObjectDelegateDataType &type)': leans on
      'QQmlDMObjectData::modelDataChanged()', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'VDMObjectDelegateDataType.__init__' has no cute function yet. "
        "Qt's "
        "'VDMObjectDelegateDataType::VDMObjectDelegateDataType(QQmlAdaptorMo"
        "del *model)': leans on 'QQmlDMObjectData::modelDataChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's "
        "'VDMObjectDelegateDataType::VDMObjectDelegateDataType(const "
        "VDMObjectDelegateDataType &type)': leans on "
        "'QQmlDMObjectData::modelDataChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def initializeMetaObject(*__, **_) -> Never:
    """
    Qt's 'void VDMObjectDelegateDataType::initializeMetaObject()': leans on
    'QQmlDMObjectData::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'VDMObjectDelegateDataType.initializeMetaObject' has no cute "
        "function yet. Qt's 'void "
        "VDMObjectDelegateDataType::initializeMetaObject()': leans on "
        "'QQmlDMObjectData::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
