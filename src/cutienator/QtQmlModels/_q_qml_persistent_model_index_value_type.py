"""
QQmlPersistentModelIndexValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlmodelindexvaluetype_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlPersistentModelIndexValueType to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QModelIndex, QVariant


class QQmlPersistentModelIndexValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPersistentModelIndexValueType: a plain Python
  object standing in front of one C++ QQmlPersistentModelIndexValueType.

  C++ hands a QQmlPersistentModelIndexValueType around as a copy, so every
  C++ QQmlPersistentModelIndexValueType behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QQmlPersistentModelIndexValueType that has a ritual
  and that Python can call so far, 8 names in all: 'toString', 'data', 'row',
  'column', 'parent', 'isValid', 'model', 'internalId'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlPersistentModelIndexValueType::qt_qmlMarker_anonymous()':
    one of Qt's own inner workings.
  - Qt's 'void QQmlPersistentModelIndexValueType::qt_qmlMarker_extended()':
    one of Qt's own inner workings.
  - Qt's 'void QQmlPersistentModelIndexValueType::qt_qmlMarker_foreign()':
    one of Qt's own inner workings.
  - Qt's 'QPersistentModelIndex QQmlPersistentModelIndexValueType::operator
    QPersistentModelIndex() const': an operator Python has no name for.
  - Qt's
    'QQmlPersistentModelIndexValueType::~QQmlPersistentModelIndexValueType(
    )': the destructor: Python removes its C++
    QQmlPersistentModelIndexValueType by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlPersistentModelIndexValueType is created at the first use,
    not by 'QQmlPersistentModelIndexValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPersistentModelIndexValueType back gives a copy
    the ritual made for Python, in a new cute
    QQmlPersistentModelIndexValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPersistentModelIndexValueType'

  #  Qt's '~QQmlPersistentModelIndexValueType()'. Naming it makes this a
  #  value class: Python owns every C++ QQmlPersistentModelIndexValueType
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QQmlPersistentModelIndexValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlPersistentModelIndexValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPersistentModelIndexValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType8toStringEv',
    )

  @overload()
  @overload(int)
  def data(self, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlPersistentModelIndexValueType::data(int role)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#data

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlPersistentModelIndexValueType::data(int role) const
    address = self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType4dataEi', role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def row(self) -> int:
    """
    Calls Qt's 'int QQmlPersistentModelIndexValueType::row() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#row
    """
    #  int QQmlPersistentModelIndexValueType::row() const
    return self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType3rowEv',
    )

  def column(self) -> int:
    """
    Calls Qt's 'int QQmlPersistentModelIndexValueType::column() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#column
    """
    #  int QQmlPersistentModelIndexValueType::column() const
    return self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType6columnEv',
    )

  def parent(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlPersistentModelIndexValueType::parent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#parent

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlPersistentModelIndexValueType::parent() const
    address = self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType6parentEv',
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlPersistentModelIndexValueType::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#isValid
    """
    #  bool QQmlPersistentModelIndexValueType::isValid() const
    return self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType7isValidEv',
    )

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel
    *QQmlPersistentModelIndexValueType::model() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQmlPersistentModelIndexValueType::model() const
    address = self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType5modelEv',
    )
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def internalId(self) -> int:
    """
    Calls Qt's 'quint64 QQmlPersistentModelIndexValueType::internalId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpersistentmodelindexvaluetype.html#internalId
    """
    #  quint64 QQmlPersistentModelIndexValueType::internalId() const
    return self.uglySide.call(
        'ritual_ZNK33QQmlPersistentModelIndexValueType10internalIdEv',
    )

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
