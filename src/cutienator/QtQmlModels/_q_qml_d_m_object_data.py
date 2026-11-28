"""
QQmlDMObjectData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDMObjectData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject
from . import QQmlDelegateModelItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQmlDMObjectData(QQmlDelegateModelItem):
  """
  The cute side of Qt's QQmlDMObjectData: a plain Python object standing in
  front of one C++ QQmlDMObjectData.

  It is built on the cute 'QQmlDelegateModelItem', as Qt's QQmlDMObjectData
  is built on Qt's QQmlDelegateModelItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDMObjectData that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'modelData',
  'modelDataChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDMObjectData::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlDMObjectData::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlDMObjectData::initProxy()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 3 leans on 'QQmlDMObjectData; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QQmlDMObjectData is created at the first use, not by
    'QQmlDMObjectData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDMObjectData.
  - Qt tells when it has removed the C++ QQmlDMObjectData. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDMObjectData that has no cute function yet,
    '__init__', 'setModelData', holds a function that raises
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
  __qt_class__ = 'QQmlDMObjectData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDMObjectData::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldmobjectdata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDMObjectData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlDMObjectData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def modelData(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDMObjectData::modelData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldmobjectdata.html#modelData

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDMObjectData::modelData() const
    address = self.uglySide.call('ritual_ZNK16QQmlDMObjectData9modelDataEv')
    return QObject._cuteAt(address)

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
    Qt's 'QQmlDMObjectData::QQmlDMObjectData(const
    QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
    VDMObjectDelegateDataType *dataType, int index, int row, int column,
    QObject *object)': leans on 'QQmlDMObjectData::modelDataChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMObjectData.__init__' has no cute function yet. Qt's "
        "'QQmlDMObjectData::QQmlDMObjectData(const "
        "QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, "
        "VDMObjectDelegateDataType *dataType, int index, int row, int "
        "column, QObject *object)': leans on "
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

  def modelDataChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDMObjectData::modelDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmobjectdata.html#modelDataChanged
    """
    #  void QQmlDMObjectData::modelDataChanged()
    self.uglySide.call('ritual_ZN16QQmlDMObjectData16modelDataChangedEv')

  @staticmethod
  def setModelData(*__, **_) -> Never:
    """
    Qt's 'void QQmlDMObjectData::setModelData(QObject *modelData)': leans on
    'QQmlDMObjectData::modelDataChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMObjectData.setModelData' has no cute function yet. Qt's "
        "'void QQmlDMObjectData::setModelData(QObject *modelData)': leans "
        "on 'QQmlDMObjectData::modelDataChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
