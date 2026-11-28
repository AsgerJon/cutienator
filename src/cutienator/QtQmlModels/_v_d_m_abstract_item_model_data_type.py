"""
VDMAbstractItemModelDataType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmabstractitemmodeldata_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means VDMAbstractItemModelDataType to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractDynamicMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class VDMAbstractItemModelDataType(QAbstractDynamicMetaObject):
  """
  The cute side of Qt's VDMAbstractItemModelDataType: a plain Python object
  standing in front of one C++ VDMAbstractItemModelDataType.

  What exists
  -----------

  Every function of Qt's VDMAbstractItemModelDataType that has a ritual and
  that Python can call so far, 1 name in all: 'objectDestroyed'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void VDMAbstractItemModelDataType::notifyItems(const
    QVarLengthArray<QQmlGuard<QQmlDMAbstractItemModelData>> &guardedItems,
    int index, QQmlDelegateModel::DelegateModelAccess access) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'void
    VDMAbstractItemModelDataType::replaceWatchedRoles(QQmlAdaptorModel &a0,
    const QList<QByteArray> &oldRoles, const QList<QByteArray> &newRoles)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'int VDMAbstractItemModelDataType::rowCount(const QQmlAdaptorModel
    &model) const': takes a type Python has no way to hand over yet.
  - Qt's 'int VDMAbstractItemModelDataType::columnCount(const
    QQmlAdaptorModel &model) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'void VDMAbstractItemModelDataType::cleanup(QQmlAdaptorModel &a0)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QVariant VDMAbstractItemModelDataType::parentModelIndex(const
    QQmlAdaptorModel &model) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QVariant VDMAbstractItemModelDataType::modelIndex(const
    QQmlAdaptorModel &model, int index) const': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool VDMAbstractItemModelDataType::canFetchMore(const
    QQmlAdaptorModel &model) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'void VDMAbstractItemModelDataType::fetchMore(QQmlAdaptorModel
    &model) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 18 functions Qt declares: 6 leans on 'QQmlDMAbstractItemModelData;
  2 leans on 'QQmlDelegateModelItemObject.

  What to expect
  --------------

  - The C++ VDMAbstractItemModelDataType is created at the first use, not by
    'VDMAbstractItemModelDataType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ VDMAbstractItemModelDataType.
  - Each name of Qt's VDMAbstractItemModelDataType that has no cute function
    yet, '__init__', 'get_hasModelChildren', 'initializeConstructor',
    'initializeMetaObject', 'notifyItems', holds a function that raises
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
  __qt_class__ = 'VDMAbstractItemModelDataType'

  #  Qt's VDMAbstractItemModelDataType is built on more than one class. The
  #  part of a C++ VDMAbstractItemModelDataType that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractDynamicMetaObject':
          'ritual_cast_VDMAbstractItemModelDataType_QAbstractDynamicMetaObject',
  }

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
    Qt's 'VDMAbstractItemModelDataType::VDMAbstractItemModelDataType(
    QQmlAdaptorModel *model)': leans on
    'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'VDMAbstractItemModelDataType.__init__' has no cute function yet. "
        "Qt's "
        "'VDMAbstractItemModelDataType::VDMAbstractItemModelDataType(QQmlAda"
        "ptorModel *model)': leans on "
        "'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void VDMAbstractItemModelDataType::objectDestroyed(QObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/vdmabstractitemmodeldatatype.html#objectDestroyed

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void VDMAbstractItemModelDataType::objectDestroyed(QObject *a0)
    self.uglySide.call(
        'ritual_ZN28VDMAbstractItemModelDataType15objectDestroyedEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @staticmethod
  def get_hasModelChildren(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    VDMAbstractItemModelDataType::get_hasModelChildren(const
    QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value
    *a2, int a3)': leans on 'QQmlDelegateModelItemObject::static_vtbl', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'VDMAbstractItemModelDataType.get_hasModelChildren' has no cute "
        "function yet. Qt's 'QV4::ReturnedValue "
        "VDMAbstractItemModelDataType::get_hasModelChildren(const "
        "QV4::FunctionObject *b, const QV4::Value *thisObject, const "
        "QV4::Value *a2, int a3)': leans on "
        "'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def initializeConstructor(*__, **_) -> Never:
    """
    Qt's 'void VDMAbstractItemModelDataType::initializeConstructor(
    QQmlAdaptorModelEngineData *const data)': leans on
    'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'VDMAbstractItemModelDataType.initializeConstructor' has no cute "
        "function yet. Qt's 'void "
        "VDMAbstractItemModelDataType::initializeConstructor(QQmlAdaptorMode"
        "lEngineData *const data)': leans on "
        "'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def initializeMetaObject(*__, **_) -> Never:
    """
    Qt's 'void VDMAbstractItemModelDataType::initializeMetaObject(const
    QQmlAdaptorModel &model)': leans on
    'QQmlDMAbstractItemModelData::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'VDMAbstractItemModelDataType.initializeMetaObject' has no cute "
        "function yet. Qt's 'void "
        "VDMAbstractItemModelDataType::initializeMetaObject(const "
        "QQmlAdaptorModel &model)': leans on "
        "'QQmlDMAbstractItemModelData::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def notifyItems(*__, **_) -> Never:
    """
    Qt's 'void VDMAbstractItemModelDataType::notifyItems(const
    QVarLengthArray<QQmlGuard<QQmlDMAbstractItemModelData>> &guardedItems,
    int index, QQmlDelegateModel::DelegateModelAccess access) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'VDMAbstractItemModelDataType.notifyItems' has no cute function "
        "yet. Qt's 'void VDMAbstractItemModelDataType::notifyItems(const "
        "QVarLengthArray<QQmlGuard<QQmlDMAbstractItemModelData>> "
        "&guardedItems, int index, QQmlDelegateModel::DelegateModelAccess "
        "access) const': takes a type Python has no way to hand over yet.")
