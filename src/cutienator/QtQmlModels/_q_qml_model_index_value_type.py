"""
QQmlModelIndexValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlmodelindexvaluetype_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlModelIndexValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QModelIndex, QPersistentModelIndex
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QQmlModelIndexValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlModelIndexValueType: a plain Python object
  standing in front of one C++ QQmlModelIndexValueType.

  C++ hands a QQmlModelIndexValueType around as a copy, so every C++
  QQmlModelIndexValueType behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlModelIndexValueType that has a ritual and that
  Python can call so far, 10 names in all: 'toString', 'data', 'row',
  'column', 'parent', 'isValid', 'model', 'internalId', 'propertiesString',
  'toPersistentModelIndex'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlModelIndexValueType::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.
  - Qt's 'void QQmlModelIndexValueType::qt_qmlMarker_extended()': one of Qt's
    own inner workings.
  - Qt's 'void QQmlModelIndexValueType::qt_qmlMarker_foreign()': one of Qt's
    own inner workings.
  - Qt's 'QModelIndex QQmlModelIndexValueType::operator QModelIndex() const':
    an operator Python has no name for.
  - Qt's 'QQmlModelIndexValueType::~QQmlModelIndexValueType()': the
    destructor: Python removes its C++ QQmlModelIndexValueType by it, and has
    no other use for it.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlModelIndexValueType is created at the first use, not by
    'QQmlModelIndexValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlModelIndexValueType back gives a copy the ritual
    made for Python, in a new cute QQmlModelIndexValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QModelIndex)
  def propertiesString(idx: QModelIndex) -> str:
    """
    Calls Qt's 'QString QQmlModelIndexValueType::propertiesString(const
    QModelIndex &idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#propertiesString

    Parameters
    ----------

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlModelIndexValueType::propertiesString(const QModelIndex
    #      &idx)
    return Rituals.call(
        'ritual_ZN23QQmlModelIndexValueType16propertiesStringERK11QModelInd'
        'ex',
        CuteMixin._valueOf(idx),
    )

  @staticmethod
  @overload(QModelIndex)
  def toPersistentModelIndex(index: QModelIndex) -> QPersistentModelIndex:
    """
    Calls Qt's 'QPersistentModelIndex
    QQmlModelIndexValueType::toPersistentModelIndex(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QPersistentModelIndex
      A new cute QPersistentModelIndex around the copy Qt gave back. Python
      owns it.
    """
    #  QPersistentModelIndex
    #      QQmlModelIndexValueType::toPersistentModelIndex(const QModelIndex
    #      &index)
    address = Rituals.call(
        'ritual_ZN23QQmlModelIndexValueType22toPersistentModelIndexERK11QMo'
        'delIndex',
        CuteMixin._valueOf(index),
    )
    from ..QtCore import QPersistentModelIndex
    return QPersistentModelIndex._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlModelIndexValueType'

  #  Qt's '~QQmlModelIndexValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlModelIndexValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQmlModelIndexValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlModelIndexValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlModelIndexValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK23QQmlModelIndexValueType8toStringEv',
    )

  @overload()
  @overload(int)
  def data(self, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlModelIndexValueType::data(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#data

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlModelIndexValueType::data(int role) const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlModelIndexValueType4dataEi', role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def row(self) -> int:
    """
    Calls Qt's 'int QQmlModelIndexValueType::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#row
    """
    #  int QQmlModelIndexValueType::row() const
    return self.uglySide.call('ritual_ZNK23QQmlModelIndexValueType3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QQmlModelIndexValueType::column() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#column
    """
    #  int QQmlModelIndexValueType::column() const
    return self.uglySide.call('ritual_ZNK23QQmlModelIndexValueType6columnEv')

  def parent(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlModelIndexValueType::parent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#parent

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlModelIndexValueType::parent() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlModelIndexValueType6parentEv',
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlModelIndexValueType::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#isValid
    """
    #  bool QQmlModelIndexValueType::isValid() const
    return self.uglySide.call(
        'ritual_ZNK23QQmlModelIndexValueType7isValidEv',
    )

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QQmlModelIndexValueType::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQmlModelIndexValueType::model() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlModelIndexValueType5modelEv',
    )
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def internalId(self) -> int:
    """
    Calls Qt's 'quint64 QQmlModelIndexValueType::internalId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmodelindexvaluetype.html#internalId
    """
    #  quint64 QQmlModelIndexValueType::internalId() const
    return self.uglySide.call(
        'ritual_ZNK23QQmlModelIndexValueType10internalIdEv',
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
