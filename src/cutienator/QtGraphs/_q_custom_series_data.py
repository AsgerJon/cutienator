"""
QCustomSeriesData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qcustomseriesdata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCustomSeriesData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QCustomSeriesData(QObject):
  """
  The cute side of Qt's QCustomSeriesData: a plain Python object standing in
  front of one C++ QCustomSeriesData.

  It is built on the cute 'QObject', as Qt's QCustomSeriesData is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCustomSeriesData that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'data', 'setData'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustomSeriesData::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCustomSeriesData::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 not a gap; 1 leans on
  'QCustomSeriesData; 1 leans on 'vtable for QCustomSeriesData', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QCustomSeriesData is created at the first use, not by
    'QCustomSeriesData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustomSeriesData.
  - Qt tells when it has removed the C++ QCustomSeriesData. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCustomSeriesData that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustomSeriesData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCustomSeriesData::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseriesdata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustomSeriesData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QCustomSeriesData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def data(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QCustomSeriesData::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseriesdata.html#data

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QCustomSeriesData::data() const
    address = self.uglySide.call('ritual_ZNK17QCustomSeriesData4dataEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant])
  def setData(self, newData: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QCustomSeriesData::setData(const QVariantMap &newData)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustomseriesdata.html#setData

    Parameters
    ----------

    newData : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QCustomSeriesData::setData(const QVariantMap &newData)
    self.uglySide.call(
        'ritual_ZN17QCustomSeriesData7setDataERK4QMapI7QString8QVariantE',
        self._valueOf(newData),
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
    Qt's 'QCustomSeriesData::QCustomSeriesData(QObject *parent)': leans on
    'vtable for QCustomSeriesData', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCustomSeriesData.__init__' has no cute function yet. Qt's "
        "'QCustomSeriesData::QCustomSeriesData(QObject *parent)': leans on "
        "'vtable for QCustomSeriesData', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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


#  Qt's 'QList<QCustomSeriesData *>': the list of QCustomSeriesData, which
#  'QList[QCustomSeriesData]' gives. It is made here, so that there is one as
#  soon as there can be a QCustomSeriesData.
QList.createKind(
    QCustomSeriesData, 'address',
    make='ritual_list_make_QCustomSeriesData_ptr',
    add='ritual_list_add_QCustomSeriesData_ptr',
    size='ritual_list_size_QCustomSeriesData_ptr',
    at='ritual_list_at_QCustomSeriesData_ptr',
    drop='ritual_list_drop_QCustomSeriesData_ptr',
)
