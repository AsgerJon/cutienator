"""
QQmlDMAbstractItemModelData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmabstractitemmodeldata_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlDMAbstractItemModelData to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQmlDelegateModelItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import VDMAbstractItemModelDataType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QQmlDMAbstractItemModelData(QQmlDelegateModelItem):
  """
  The cute side of Qt's QQmlDMAbstractItemModelData: a plain Python object
  standing in front of one C++ QQmlDMAbstractItemModelData.

  It is built on the cute 'QQmlDelegateModelItem', as Qt's
  QQmlDMAbstractItemModelData is built on Qt's QQmlDelegateModelItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDMAbstractItemModelData that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject',
  'hasModelChildren', 'get', 'setValue', 'type', 'modelDataChanged', 'value'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDMAbstractItemModelData::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQmlDMAbstractItemModelData::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'bool QQmlDMAbstractItemModelData::resolveIndex(const
    QQmlAdaptorModel &model, int idx)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  11 of the 22 functions Qt declares: 7 leans on
  'QQmlDMAbstractItemModelData; 2 not a gap; 1 leans on 'vtable for
  QQmlDMAbstractItemModelData', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'QQmlDelegateModelItemObject.

  What to expect
  --------------

  - The C++ QQmlDMAbstractItemModelData is created at the first use, not by
    'QQmlDMAbstractItemModelData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDMAbstractItemModelData.
  - Qt tells when it has removed the C++ QQmlDMAbstractItemModelData. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDMAbstractItemModelData that has no cute function
    yet, '__init__', 'get_modelData', 'get_property', 'metaCall',
    'modelData', 'setModelData', 'set_modelData', 'set_property', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDMAbstractItemModelData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDMAbstractItemModelData::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDMAbstractItemModelData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQmlDMAbstractItemModelData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasModelChildren(self) -> bool:
    """
    Calls Qt's 'bool QQmlDMAbstractItemModelData::hasModelChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#hasModelChildren
    """
    #  bool QQmlDMAbstractItemModelData::hasModelChildren() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlDMAbstractItemModelData16hasModelChildrenEv',
    )

  def type(self) -> Optional[VDMAbstractItemModelDataType]:
    """
    Calls Qt's 'const VDMAbstractItemModelDataType
    *QQmlDMAbstractItemModelData::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#type

    Returns
    -------

    Optional[VDMAbstractItemModelDataType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const VDMAbstractItemModelDataType
    #      *QQmlDMAbstractItemModelData::type() const
    address = self.uglySide.call(
        'ritual_ZNK27QQmlDMAbstractItemModelData4typeEv',
    )
    from . import VDMAbstractItemModelDataType
    return VDMAbstractItemModelDataType._cuteAt(address)

  @overload(int)
  def value(self, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDMAbstractItemModelData::value(int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#value

    Parameters
    ----------

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDMAbstractItemModelData::value(int role) const
    address = self.uglySide.call(
        'ritual_ZNK27QQmlDMAbstractItemModelData5valueEi', role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QVariant)
  def setValue(self, role: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlDMAbstractItemModelData::setValue(const QString
    &role, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#setValue

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlDMAbstractItemModelData::setValue(const QString &role, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN27QQmlDMAbstractItemModelData8setValueERK7QStringRK8QVari'
        'ant',
        role, self._valueOf(value),
    )

  @overload(int, QVariant)
  def setValue(self, role: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlDMAbstractItemModelData::setValue(int role, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#setValue

    Parameters
    ----------

    role : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlDMAbstractItemModelData::setValue(int role, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN27QQmlDMAbstractItemModelData8setValueEiRK8QVariant',
        role, self._valueOf(value),
    )

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
    Qt's 'QQmlDMAbstractItemModelData::QQmlDMAbstractItemModelData(const
    QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
    VDMAbstractItemModelDataType *dataType, int index, int row, int column)':
    leans on 'vtable for QQmlDMAbstractItemModelData', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.__init__' has no cute function yet. "
        "Qt's "
        "'QQmlDMAbstractItemModelData::QQmlDMAbstractItemModelData(const "
        "QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, "
        "VDMAbstractItemModelDataType *dataType, int index, int row, int "
        "column)': leans on 'vtable for QQmlDMAbstractItemModelData', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def get(self) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlDMAbstractItemModelData::get()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#get
    """
    #  QV4::ReturnedValue QQmlDMAbstractItemModelData::get()
    return self.uglySide.call('ritual_ZN27QQmlDMAbstractItemModelData3getEv')

  def modelDataChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDMAbstractItemModelData::modelDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmabstractitemmodeldata.html#modelDataChanged
    """
    #  void QQmlDMAbstractItemModelData::modelDataChanged()
    self.uglySide.call(
        'ritual_ZN27QQmlDMAbstractItemModelData16modelDataChangedEv',
    )

  @staticmethod
  def get_modelData(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDMAbstractItemModelData::get_modelData(const
    QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': leans on
    'QQmlDMAbstractItemModelData::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.get_modelData' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDMAbstractItemModelData::get_modelData(const "
        "QV4::FunctionObject *b, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': leans on "
        "'QQmlDMAbstractItemModelData::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def get_property(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDMAbstractItemModelData::get_property(const
    QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': leans on 'QQmlDelegateModelItemObject::static_vtbl',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.get_property' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDMAbstractItemModelData::get_property(const "
        "QV4::FunctionObject *b, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': leans on "
        "'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def metaCall(*__, **_) -> Never:
    """
    Qt's 'int QQmlDMAbstractItemModelData::metaCall(QMetaObject::Call call,
    int id, void **arguments)': leans on
    'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.metaCall' has no cute function yet. "
        "Qt's 'int QQmlDMAbstractItemModelData::metaCall(QMetaObject::Call "
        "call, int id, void **arguments)': leans on "
        "'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def modelData(*__, **_) -> Never:
    """
    Qt's 'QVariant QQmlDMAbstractItemModelData::modelData() const': leans on
    'QQmlDMAbstractItemModelData::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.modelData' has no cute function yet. "
        "Qt's 'QVariant QQmlDMAbstractItemModelData::modelData() const': "
        "leans on 'QQmlDMAbstractItemModelData::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setModelData(*__, **_) -> Never:
    """
    Qt's 'void QQmlDMAbstractItemModelData::setModelData(const QVariant
    &modelData)': leans on 'QQmlDMAbstractItemModelData::modelDataChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.setModelData' has no cute function "
        "yet. Qt's 'void QQmlDMAbstractItemModelData::setModelData(const "
        "QVariant &modelData)': leans on "
        "'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def set_modelData(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDMAbstractItemModelData::set_modelData(const
    QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': leans on
    'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.set_modelData' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDMAbstractItemModelData::set_modelData(const "
        "QV4::FunctionObject *b, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': leans on "
        "'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def set_property(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDMAbstractItemModelData::set_property(const
    QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': leans on
    'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMAbstractItemModelData.set_property' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQmlDMAbstractItemModelData::set_property(const "
        "QV4::FunctionObject *b, const QV4::Value *thisObject, const "
        "QV4::Value *argv, int argc)': leans on "
        "'QQmlDMAbstractItemModelData::modelDataChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
