"""
QQmlDMListAccessorData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlDMListAccessorData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQmlDelegateModelItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QQmlDMListAccessorData(QQmlDelegateModelItem):
  """
  The cute side of Qt's QQmlDMListAccessorData: a plain Python object
  standing in front of one C++ QQmlDMListAccessorData.

  It is built on the cute 'QQmlDelegateModelItem', as Qt's
  QQmlDMListAccessorData is built on Qt's QQmlDelegateModelItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDMListAccessorData that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'modelData', 'get',
  'setValue', 'modelDataChanged'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDMListAccessorData::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlDMListAccessorData::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlDMListAccessorData::~QQmlDMListAccessorData()': the destructor:
    Python never removes a C++ QQmlDMListAccessorData.
  - Qt's 'bool QQmlDMListAccessorData::resolveIndex(const QQmlAdaptorModel
    &model, int idx)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 16 functions Qt declares: 3 leans on 'QQmlDMListAccessorData; 2
  not a gap; 2 leans on 'QQmlDelegateModelItemObject.

  What to expect
  --------------

  - The C++ QQmlDMListAccessorData is created at the first use, not by
    'QQmlDMListAccessorData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDMListAccessorData.
  - Qt tells when it has removed the C++ QQmlDMListAccessorData. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDMListAccessorData that has no cute function yet,
    '__init__', 'get_modelData', 'setModelData', 'set_modelData', holds a
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
  __qt_class__ = 'QQmlDMListAccessorData'

  #  A C++ QQmlDMListAccessorData Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDMListAccessorData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDMListAccessorData::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmlistaccessordata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDMListAccessorData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlDMListAccessorData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def modelData(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDMListAccessorData::modelData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmlistaccessordata.html#modelData

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDMListAccessorData::modelData() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlDMListAccessorData9modelDataEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QVariant)
  def setValue(self, role: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlDMListAccessorData::setValue(const QString &role,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmlistaccessordata.html#setValue

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlDMListAccessorData::setValue(const QString &role, const
    #      QVariant &value)
    ritual = (
        'ritual_ZN22QQmlDMListAccessorData8setValueERK7QStringRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQmlDMListAccessorData8setValueERK7QStringRK8QVar'
          'iant')
    self.uglySide.call(ritual, role, self._valueOf(value))

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
    Qt's 'QQmlDMListAccessorData::QQmlDMListAccessorData(const
    QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
    VDMListDelegateDataType *dataType, int index, int row, int column, const
    QVariant &value)': leans on
    'QQmlDMListAccessorData::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMListAccessorData.__init__' has no cute function yet. Qt's "
        "'QQmlDMListAccessorData::QQmlDMListAccessorData(const "
        "QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, "
        "VDMListDelegateDataType *dataType, int index, int row, int column, "
        "const QVariant &value)': leans on "
        "'QQmlDMListAccessorData::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'QV4::ReturnedValue QQmlDMListAccessorData::get()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldmlistaccessordata.html#get
    """
    #  QV4::ReturnedValue QQmlDMListAccessorData::get()
    return self.uglySide.call('ritual_ZN22QQmlDMListAccessorData3getEv')

  def modelDataChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDMListAccessorData::modelDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmlistaccessordata.html#modelDataChanged
    """
    #  void QQmlDMListAccessorData::modelDataChanged()
    self.uglySide.call(
        'ritual_ZN22QQmlDMListAccessorData16modelDataChangedEv',
    )

  @staticmethod
  def get_modelData(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDMListAccessorData::get_modelData(const
    QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value
    *a2, int a3)': leans on 'QQmlDelegateModelItemObject::static_vtbl', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMListAccessorData.get_modelData' has no cute function yet. "
        "Qt's 'QV4::ReturnedValue "
        "QQmlDMListAccessorData::get_modelData(const QV4::FunctionObject "
        "*b, const QV4::Value *thisObject, const QV4::Value *a2, int a3)': "
        "leans on 'QQmlDelegateModelItemObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setModelData(*__, **_) -> Never:
    """
    Qt's 'void QQmlDMListAccessorData::setModelData(const QVariant &data)':
    leans on 'QQmlDMListAccessorData::modelDataChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlDMListAccessorData.setModelData' has no cute function yet. "
        "Qt's 'void QQmlDMListAccessorData::setModelData(const QVariant "
        "&data)': leans on 'QQmlDMListAccessorData::modelDataChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def set_modelData(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlDMListAccessorData::set_modelData(const
    QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)': leans on 'QQmlDelegateModelItemObject::static_vtbl',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMListAccessorData.set_modelData' has no cute function yet. "
        "Qt's 'QV4::ReturnedValue "
        "QQmlDMListAccessorData::set_modelData(const QV4::FunctionObject "
        "*b, const QV4::Value *thisObject, const QV4::Value *argv, int "
        "argc)': leans on 'QQmlDelegateModelItemObject::static_vtbl', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
