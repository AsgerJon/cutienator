"""
QRangeModelImplBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QHash, QList, QRangeModelDetails

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QCollator, QMetaObject, QMetaProperty, QMimeData
  from . import QModelIndex, QObject, QRangeModel, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCollator = WAIT['QCollator']
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QObject = WAIT['QObject']
  QRangeModel = WAIT['QRangeModel']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRangeModelImplBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRangeModelImplBase: a plain Python object standing
  in front of one C++ QRangeModelImplBase.

  What exists
  -----------

  Every function of Qt's QRangeModelImplBase that has a ritual and that
  Python can call so far, 33 names in all: 'roleNames', 'getImplementation',
  'persistentIndexList', 'changePersistentIndex', 'beginResetModel',
  'endResetModel', 'beginInsertColumns', 'endInsertColumns',
  'beginRemoveColumns', 'endRemoveColumns', 'beginMoveColumns',
  'endMoveColumns', 'beginInsertRows', 'endInsertRows', 'beginRemoveRows',
  'endRemoveRows', 'beginMoveRows', 'endMoveRows', 'beginLayoutChange',
  'endLayoutChange', 'autoConnectPolicy', 'compareData',
  'roleNamesForSimpleType', 'columnProperties', 'connectProperty',
  'connectPropertyConst', 'connectProperties', 'connectPropertiesConst',
  'sortRole', 'sortCollator', 'convertMatchValue', 'matchValue',
  'dropDataOnItem'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRangeModelImplBase
    *QRangeModelImplBase::getImplementation(const QRangeModel *model)': takes
    in Python what 'QRangeModelImplBase
    *QRangeModelImplBase::getImplementation(QRangeModel *model)' takes.
  - Qt's 'QModelIndex QRangeModelImplBase::createIndex(int row, int column,
    const void *ptr) const': names 'void', which has no cute class yet.
  - Qt's 'void QRangeModelImplBase::dataChanged(const QModelIndex &from,
    const QModelIndex &to, const QList<int> &roles)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QAbstractItemModel &QRangeModelImplBase::itemModel()': gives a type
    Python has no way to take yet.
  - Qt's 'const QAbstractItemModel &QRangeModelImplBase::itemModel() const':
    gives a type Python has no way to take yet.
  - Qt's 'QHash<int, QByteArray>
    QRangeModelImplBase::roleNamesForMetaObject(const QAbstractItemModel
    &model, const QMetaObject &metaObject)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QScopedValueRollback<bool>
    QRangeModelImplBase::blockDataChangedDispatch()': gives a type Python has
    no way to take yet.
  - Qt's 'QHash<int, QMetaProperty> QRangeModelImplBase::roleProperties(const
    QAbstractItemModel &model, const QMetaObject &metaObject)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  31 of the 74 functions Qt declares: 31 cannot be called and cannot be
  called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QRangeModelImplBase is created at the first use, not by
    'QRangeModelImplBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRangeModelImplBase.
  - Each name of Qt's QRangeModelImplBase that has no cute function yet,
    'adjustSupportedDragActions', 'adjustSupportedDropActions',
    'blockDataChangedDispatch', 'canDropMimeData', 'clearItemData',
    'columnCount', 'createIndex', 'data', 'dataChanged', 'dropMimeData',
    'flags', 'headerData', 'index', 'insertColumns', 'insertRows',
    'interfaceVersion', 'invalidateCaches', 'itemData', 'itemModel', 'match',
    'mimeData', 'mimeTypes', 'moveColumns', 'moveRows', 'multiData',
    'parent', 'removeColumns', 'removeRows', 'roleNamesForMetaObject',
    'roleProperties', 'rowCount', 'setAutoConnectPolicy', 'setData',
    'setHeaderData', 'setItemData', 'sibling', 'sort', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRangeModelImplBase, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AutoConnectPolicy(CuteNum, scoped=True):
    """
    The enum 'QRangeModelImplBase::AutoConnectPolicy' of Qt, with the 3 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Full = Kee[int](1)
    OnRead = Kee[int](2)

  class DropOperation(CuteNum, scoped=True):
    """
    The enum 'QRangeModelImplBase::DropOperation' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    DontDrop = Kee[int](0)
    Automatic = Kee[int](1)
    OverwriteAndIgnore = Kee[int](2)
    OverwriteAndExtend = Kee[int](3)
    InsertAsSiblings = Kee[int](4)
    InsertAsChildren = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRangeModel)
  @overload(NoneType)
  def getImplementation(
      model: Optional[QRangeModel],
  ) -> Optional[QRangeModelImplBase]:
    """
    Calls Qt's 'QRangeModelImplBase
    *QRangeModelImplBase::getImplementation(QRangeModel *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#getImplementation

    Parameters
    ----------

    model : Optional[QRangeModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRangeModelImplBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRangeModelImplBase
    #      *QRangeModelImplBase::getImplementation(QRangeModel *model)
    address = Rituals.call(
        'ritual_ZN19QRangeModelImplBase17getImplementationEP11QRangeModel',
        CuteMixin._addressOf(model),
    )
    return QRangeModelImplBase._cuteAt(address)

  @staticmethod
  @overload(QVariant, QVariant, QCollator)
  @overload(QVariant, QVariant, NoneType)
  def compareData(
      lhs: QVariant,
      rhs: QVariant,
      collator: Optional[QCollator],
  ) -> Qt.weak_ordering:
    """
    Calls Qt's 'Qt::weak_ordering QRangeModelImplBase::compareData(const
    QVariant &lhs, const QVariant &rhs, const QCollator *collator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#compareData

    Parameters
    ----------

    lhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    rhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    collator : Optional[QCollator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.weak_ordering
      A new cute Qt::weak_ordering around the copy Qt gave back. Python owns
      it.
    """
    #  Qt::weak_ordering QRangeModelImplBase::compareData(const QVariant
    #      &lhs, const QVariant &rhs, const QCollator *collator)
    address = Rituals.call(
        'ritual_ZN19QRangeModelImplBase11compareDataERK8QVariantS2_PK9QColl'
        'ator',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
        CuteMixin._addressOf(collator),
    )
    return Qt.weak_ordering._cuteOwning(address)

  @staticmethod
  def roleNamesForSimpleType() -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QRangeModelImplBase::roleNamesForSimpleType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#roleNamesForSimpleType

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QRangeModelImplBase::roleNamesForSimpleType()
    address = Rituals.call(
        'ritual_ZN19QRangeModelImplBase22roleNamesForSimpleTypeEv',
    )
    from . import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject)
  def columnProperties(metaObject: QMetaObject) -> QHash[int, QMetaProperty]:
    """
    Calls Qt's 'QHash<int, QMetaProperty>
    QRangeModelImplBase::columnProperties(const QMetaObject &metaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#columnProperties

    Parameters
    ----------

    metaObject : QMetaObject
      Passed on as a value: Qt reads the C++ QMetaObject, which stays
      Python's own.

    Returns
    -------

    QHash[int, QMetaProperty]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QMetaProperty> QRangeModelImplBase::columnProperties(const
    #      QMetaObject &metaObject)
    address = Rituals.call(
        'ritual_ZN19QRangeModelImplBase16columnPropertiesERK11QMetaObject',
        CuteMixin._valueOf(metaObject, 'QMetaObject'),
    )
    from . import QMetaProperty
    return QHash[int, QMetaProperty]._cuteOwning(address)

  @staticmethod
  @overload(
      QModelIndex, QObject, WAIT['QRangeModelDetails.AutoConnectContext'],
      int, QMetaProperty,
  )
  @overload(QModelIndex, QObject, NoneType, int, QMetaProperty)
  @overload(
      QModelIndex, NoneType, WAIT['QRangeModelDetails.AutoConnectContext'],
      int, QMetaProperty,
  )
  @overload(QModelIndex, NoneType, NoneType, int, QMetaProperty)
  def connectProperty(
      index: QModelIndex,
      item: Optional[QObject],
      context: Optional[QRangeModelDetails.AutoConnectContext],
      role: int,
      property: QMetaProperty,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::connectProperty(const QModelIndex
    &index, const QObject *item, QRangeModelDetails::AutoConnectContext
    *context, int role, const QMetaProperty &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#connectProperty

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QRangeModelDetails.AutoConnectContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : int
      Passed on as it is.

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  bool QRangeModelImplBase::connectProperty(const QModelIndex &index,
    #      const QObject *item, QRangeModelDetails::AutoConnectContext
    #      *context, int role, const QMetaProperty &property)
    return Rituals.call(
        'ritual_ZN19QRangeModelImplBase15connectPropertyERK11QModelIndexPK7'
        'QObjectPN18QRangeModelDetails18AutoConnectContextEiRK13QMetaProper'
        'ty',
        CuteMixin._valueOf(index), CuteMixin._addressOf(item, 'QObject'),
        CuteMixin._addressOf(context), role, CuteMixin._valueOf(property),
    )

  @staticmethod
  @overload(
      QModelIndex, QObject, WAIT['QRangeModelDetails.AutoConnectContext'],
      int, QMetaProperty,
  )
  @overload(QModelIndex, QObject, NoneType, int, QMetaProperty)
  @overload(
      QModelIndex, NoneType, WAIT['QRangeModelDetails.AutoConnectContext'],
      int, QMetaProperty,
  )
  @overload(QModelIndex, NoneType, NoneType, int, QMetaProperty)
  def connectPropertyConst(
      index: QModelIndex,
      item: Optional[QObject],
      context: Optional[QRangeModelDetails.AutoConnectContext],
      role: int,
      property: QMetaProperty,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::connectPropertyConst(const
    QModelIndex &index, const QObject *item,
    QRangeModelDetails::AutoConnectContext *context, int role, const
    QMetaProperty &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#connectPropertyConst

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QRangeModelDetails.AutoConnectContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : int
      Passed on as it is.

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  bool QRangeModelImplBase::connectPropertyConst(const QModelIndex
    #      &index, const QObject *item,
    #      QRangeModelDetails::AutoConnectContext *context, int role, const
    #      QMetaProperty &property)
    return Rituals.call(
        'ritual_ZN19QRangeModelImplBase20connectPropertyConstERK11QModelInd'
        'exPK7QObjectPN18QRangeModelDetails18AutoConnectContextEiRK13QMetaP'
        'roperty',
        CuteMixin._valueOf(index), CuteMixin._addressOf(item, 'QObject'),
        CuteMixin._addressOf(context), role, CuteMixin._valueOf(property),
    )

  @staticmethod
  @overload(
      QModelIndex, QObject, WAIT['QRangeModelDetails.AutoConnectContext'],
      QHash[int, QMetaProperty],
  )
  @overload(QModelIndex, QObject, NoneType, QHash[int, QMetaProperty])
  @overload(
      QModelIndex, NoneType, WAIT['QRangeModelDetails.AutoConnectContext'],
      QHash[int, QMetaProperty],
  )
  @overload(QModelIndex, NoneType, NoneType, QHash[int, QMetaProperty])
  def connectProperties(
      index: QModelIndex,
      item: Optional[QObject],
      context: Optional[QRangeModelDetails.AutoConnectContext],
      properties: QHash[int, QMetaProperty],
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::connectProperties(const QModelIndex
    &index, const QObject *item, QRangeModelDetails::AutoConnectContext
    *context, const QHash<int, QMetaProperty> &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#connectProperties

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QRangeModelDetails.AutoConnectContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QHash[int, QMetaProperty]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QRangeModelImplBase::connectProperties(const QModelIndex &index,
    #      const QObject *item, QRangeModelDetails::AutoConnectContext
    #      *context, const QHash<int, QMetaProperty> &properties)
    return Rituals.call(
        'ritual_ZN19QRangeModelImplBase17connectPropertiesERK11QModelIndexP'
        'K7QObjectPN18QRangeModelDetails18AutoConnectContextERK5QHashIi13QM'
        'etaPropertyE',
        CuteMixin._valueOf(index), CuteMixin._addressOf(item, 'QObject'),
        CuteMixin._addressOf(context), CuteMixin._valueOf(properties),
    )

  @staticmethod
  @overload(
      QModelIndex, QObject, WAIT['QRangeModelDetails.AutoConnectContext'],
      QHash[int, QMetaProperty],
  )
  @overload(QModelIndex, QObject, NoneType, QHash[int, QMetaProperty])
  @overload(
      QModelIndex, NoneType, WAIT['QRangeModelDetails.AutoConnectContext'],
      QHash[int, QMetaProperty],
  )
  @overload(QModelIndex, NoneType, NoneType, QHash[int, QMetaProperty])
  def connectPropertiesConst(
      index: QModelIndex,
      item: Optional[QObject],
      context: Optional[QRangeModelDetails.AutoConnectContext],
      properties: QHash[int, QMetaProperty],
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::connectPropertiesConst(const
    QModelIndex &index, const QObject *item,
    QRangeModelDetails::AutoConnectContext *context, const QHash<int,
    QMetaProperty> &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#connectPropertiesConst

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QRangeModelDetails.AutoConnectContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QHash[int, QMetaProperty]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QRangeModelImplBase::connectPropertiesConst(const QModelIndex
    #      &index, const QObject *item,
    #      QRangeModelDetails::AutoConnectContext *context, const QHash<int,
    #      QMetaProperty> &properties)
    return Rituals.call(
        'ritual_ZN19QRangeModelImplBase22connectPropertiesConstERK11QModelI'
        'ndexPK7QObjectPN18QRangeModelDetails18AutoConnectContextERK5QHashI'
        'i13QMetaPropertyE',
        CuteMixin._valueOf(index), CuteMixin._addressOf(item, 'QObject'),
        CuteMixin._addressOf(context), CuteMixin._valueOf(properties),
    )

  @staticmethod
  @overload(QVariant, Qt.MatchFlags)
  def convertMatchValue(value: QVariant, flags: Qt.MatchFlags) -> QVariant:
    """
    Calls Qt's 'QVariant QRangeModelImplBase::convertMatchValue(const
    QVariant &value, Qt::MatchFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#convertMatchValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    flags : Qt.MatchFlags
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QRangeModelImplBase::convertMatchValue(const QVariant &value,
    #      Qt::MatchFlags flags)
    address = Rituals.call(
        'ritual_ZN19QRangeModelImplBase17convertMatchValueERK8QVariant6QFla'
        'gsIN2Qt9MatchFlagEE',
        CuteMixin._valueOf(value), flags.value,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(str, QVariant, Qt.MatchFlags)
  def matchValue(
      itemData: str,
      value: QVariant,
      flags: Qt.MatchFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::matchValue(const QString &itemData,
    const QVariant &value, Qt::MatchFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#matchValue

    Parameters
    ----------

    itemData : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    flags : Qt.MatchFlags
      Passed on as its number.
    """
    #  bool QRangeModelImplBase::matchValue(const QString &itemData, const
    #      QVariant &value, Qt::MatchFlags flags)
    return Rituals.call(
        'ritual_ZN19QRangeModelImplBase10matchValueERK7QStringRK8QVariant6Q'
        'FlagsIN2Qt9MatchFlagEE',
        itemData, CuteMixin._valueOf(value), flags.value,
    )

  @staticmethod
  @overload(QVariant, QVariant, Qt.MatchFlags)
  def matchValue(
      itemData: QVariant,
      value: QVariant,
      flags: Qt.MatchFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::matchValue(const QVariant
    &itemData, const QVariant &value, Qt::MatchFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#matchValue

    Parameters
    ----------

    itemData : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    flags : Qt.MatchFlags
      Passed on as its number.
    """
    #  bool QRangeModelImplBase::matchValue(const QVariant &itemData, const
    #      QVariant &value, Qt::MatchFlags flags)
    return Rituals.call(
        'ritual_ZN19QRangeModelImplBase10matchValueERK8QVariantS2_6QFlagsIN'
        '2Qt9MatchFlagEE',
        CuteMixin._valueOf(itemData), CuteMixin._valueOf(value), flags.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRangeModelImplBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QRangeModelImplBase::roleNames()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodelimplbase.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QRangeModelImplBase::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK19QRangeModelImplBase9roleNamesEv',
    )
    from . import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def persistentIndexList(self) -> QList[QModelIndex]:
    """
    Calls Qt's 'QModelIndexList QRangeModelImplBase::persistentIndexList()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#persistentIndexList

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QModelIndexList QRangeModelImplBase::persistentIndexList() const
    address = self.uglySide.call(
        'ritual_ZNK19QRangeModelImplBase19persistentIndexListEv',
    )
    from . import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  def autoConnectPolicy(self) -> AutoConnectPolicy:
    """
    Calls Qt's 'AutoConnectPolicy QRangeModelImplBase::autoConnectPolicy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#autoConnectPolicy

    Returns
    -------

    AutoConnectPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AutoConnectPolicy(number)' gives.
    """
    #  AutoConnectPolicy QRangeModelImplBase::autoConnectPolicy() const
    return QRangeModelImplBase.AutoConnectPolicy(self.uglySide.call(
        'ritual_ZNK19QRangeModelImplBase17autoConnectPolicyEv',
    ))

  def sortRole(self) -> int:
    """
    Calls Qt's 'int QRangeModelImplBase::sortRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodelimplbase.html#sortRole
    """
    #  int QRangeModelImplBase::sortRole() const
    return self.uglySide.call('ritual_ZNK19QRangeModelImplBase8sortRoleEv')

  def sortCollator(self) -> Optional[QCollator]:
    """
    Calls Qt's 'const QCollator *QRangeModelImplBase::sortCollator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#sortCollator

    Returns
    -------

    Optional[QCollator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCollator *QRangeModelImplBase::sortCollator() const
    address = self.uglySide.call(
        'ritual_ZNK19QRangeModelImplBase12sortCollatorEv',
    )
    from . import QCollator
    return QCollator._cuteAt(address)

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

  @overload(QRangeModel)
  @overload(NoneType)
  def __init__(self, itemModel: Optional[QRangeModel]) -> None:
    """
    Notes what was given, for Qt's
    'QRangeModelImplBase::QRangeModelImplBase(QRangeModel *itemModel)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#QRangeModelImplBase

    Parameters
    ----------

    itemModel : Optional[QRangeModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRangeModelImplBase::QRangeModelImplBase(QRangeModel *itemModel)
    self._noteCreation(QRangeModelImplBase, lambda: Rituals.call(
        'ritual_ZN19QRangeModelImplBaseC1EP11QRangeModel',
        self._addressOf(itemModel),
    ))

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

  @overload(QModelIndex, QModelIndex)
  def changePersistentIndex(
      self,
      from_: QModelIndex,
      to: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::changePersistentIndex(const
    QModelIndex &from, const QModelIndex &to)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#changePersistentIndex

    Parameters
    ----------

    from_ : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    to : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QRangeModelImplBase::changePersistentIndex(const QModelIndex
    #      &from, const QModelIndex &to)
    self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase21changePersistentIndexERK11QModelIn'
        'dexS2_',
        self._valueOf(from_), self._valueOf(to),
    )

  def beginResetModel(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::beginResetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginResetModel
    """
    #  void QRangeModelImplBase::beginResetModel()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase15beginResetModelEv')

  def endResetModel(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endResetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endResetModel
    """
    #  void QRangeModelImplBase::endResetModel()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase13endResetModelEv')

  @overload(QModelIndex, int, int)
  def beginInsertColumns(
      self,
      parent: QModelIndex,
      start: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::beginInsertColumns(const
    QModelIndex &parent, int start, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginInsertColumns

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QRangeModelImplBase::beginInsertColumns(const QModelIndex
    #      &parent, int start, int count)
    self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase18beginInsertColumnsERK11QModelIndex'
        'ii',
        self._valueOf(parent), start, count,
    )

  def endInsertColumns(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endInsertColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endInsertColumns
    """
    #  void QRangeModelImplBase::endInsertColumns()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase16endInsertColumnsEv')

  @overload(QModelIndex, int, int)
  def beginRemoveColumns(
      self,
      parent: QModelIndex,
      start: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::beginRemoveColumns(const
    QModelIndex &parent, int start, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginRemoveColumns

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QRangeModelImplBase::beginRemoveColumns(const QModelIndex
    #      &parent, int start, int count)
    self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase18beginRemoveColumnsERK11QModelIndex'
        'ii',
        self._valueOf(parent), start, count,
    )

  def endRemoveColumns(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endRemoveColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endRemoveColumns
    """
    #  void QRangeModelImplBase::endRemoveColumns()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase16endRemoveColumnsEv')

  @overload(QModelIndex, int, int, QModelIndex, int)
  def beginMoveColumns(
      self,
      sourceParent: QModelIndex,
      sourceFirst: int,
      sourceLast: int,
      destParent: QModelIndex,
      destRow: int,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::beginMoveColumns(const QModelIndex
    &sourceParent, int sourceFirst, int sourceLast, const QModelIndex
    &destParent, int destRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginMoveColumns

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceFirst : int
      Passed on as it is.

    sourceLast : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destRow : int
      Passed on as it is.
    """
    #  bool QRangeModelImplBase::beginMoveColumns(const QModelIndex
    #      &sourceParent, int sourceFirst, int sourceLast, const QModelIndex
    #      &destParent, int destRow)
    return self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase16beginMoveColumnsERK11QModelIndexii'
        'S2_i',
        self._valueOf(sourceParent), sourceFirst, sourceLast,
        self._valueOf(destParent), destRow,
    )

  def endMoveColumns(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endMoveColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endMoveColumns
    """
    #  void QRangeModelImplBase::endMoveColumns()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase14endMoveColumnsEv')

  @overload(QModelIndex, int, int)
  def beginInsertRows(
      self,
      parent: QModelIndex,
      start: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::beginInsertRows(const QModelIndex
    &parent, int start, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginInsertRows

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QRangeModelImplBase::beginInsertRows(const QModelIndex &parent,
    #      int start, int count)
    self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase15beginInsertRowsERK11QModelIndexii',
        self._valueOf(parent), start, count,
    )

  def endInsertRows(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endInsertRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endInsertRows
    """
    #  void QRangeModelImplBase::endInsertRows()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase13endInsertRowsEv')

  @overload(QModelIndex, int, int)
  def beginRemoveRows(
      self,
      parent: QModelIndex,
      start: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::beginRemoveRows(const QModelIndex
    &parent, int start, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginRemoveRows

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QRangeModelImplBase::beginRemoveRows(const QModelIndex &parent,
    #      int start, int count)
    self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase15beginRemoveRowsERK11QModelIndexii',
        self._valueOf(parent), start, count,
    )

  def endRemoveRows(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endRemoveRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endRemoveRows
    """
    #  void QRangeModelImplBase::endRemoveRows()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase13endRemoveRowsEv')

  @overload(QModelIndex, int, int, QModelIndex, int)
  def beginMoveRows(
      self,
      sourceParent: QModelIndex,
      sourceFirst: int,
      sourceLast: int,
      destParent: QModelIndex,
      destRow: int,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::beginMoveRows(const QModelIndex
    &sourceParent, int sourceFirst, int sourceLast, const QModelIndex
    &destParent, int destRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginMoveRows

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceFirst : int
      Passed on as it is.

    sourceLast : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destRow : int
      Passed on as it is.
    """
    #  bool QRangeModelImplBase::beginMoveRows(const QModelIndex
    #      &sourceParent, int sourceFirst, int sourceLast, const QModelIndex
    #      &destParent, int destRow)
    return self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase13beginMoveRowsERK11QModelIndexiiS2_'
        'i',
        self._valueOf(sourceParent), sourceFirst, sourceLast,
        self._valueOf(destParent), destRow,
    )

  def endMoveRows(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endMoveRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endMoveRows
    """
    #  void QRangeModelImplBase::endMoveRows()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase11endMoveRowsEv')

  def beginLayoutChange(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::beginLayoutChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#beginLayoutChange
    """
    #  void QRangeModelImplBase::beginLayoutChange()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase17beginLayoutChangeEv')

  def endLayoutChange(self) -> None:
    """
    Calls Qt's 'void QRangeModelImplBase::endLayoutChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#endLayoutChange
    """
    #  void QRangeModelImplBase::endLayoutChange()
    self.uglySide.call('ritual_ZN19QRangeModelImplBase15endLayoutChangeEv')

  @overload(QMimeData, QModelIndex)
  @overload(NoneType, QModelIndex)
  def dropDataOnItem(
      self,
      data: Optional[QMimeData],
      index: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModelImplBase::dropDataOnItem(const QMimeData
    *data, const QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#dropDataOnItem

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QRangeModelImplBase::dropDataOnItem(const QMimeData *data, const
    #      QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN19QRangeModelImplBase14dropDataOnItemEPK9QMimeDataRK11QMo'
        'delIndex',
        self._addressOf(data), self._valueOf(index),
    )

  @staticmethod
  def adjustSupportedDragActions(*__, **_) -> Never:
    """
    Qt's 'Qt::DropActions
    QRangeModelImplBase::adjustSupportedDragActions(Qt::DropActions
    dragActions)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.adjustSupportedDragActions' has no cute "
        "function yet. Qt's 'Qt::DropActions "
        "QRangeModelImplBase::adjustSupportedDragActions(Qt::DropActions "
        "dragActions)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def adjustSupportedDropActions(*__, **_) -> Never:
    """
    Qt's 'Qt::DropActions
    QRangeModelImplBase::adjustSupportedDropActions(Qt::DropActions
    dropActions)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.adjustSupportedDropActions' has no cute "
        "function yet. Qt's 'Qt::DropActions "
        "QRangeModelImplBase::adjustSupportedDropActions(Qt::DropActions "
        "dropActions)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def blockDataChangedDispatch(*__, **_) -> Never:
    """
    Qt's 'QScopedValueRollback<bool>
    QRangeModelImplBase::blockDataChangedDispatch()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.blockDataChangedDispatch' has no cute "
        "function yet. Qt's 'QScopedValueRollback<bool> "
        "QRangeModelImplBase::blockDataChangedDispatch()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def canDropMimeData(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::canDropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.canDropMimeData' has no cute function yet. "
        "Qt's 'bool QRangeModelImplBase::canDropMimeData(const QMimeData "
        "*data, Qt::DropAction action, int row, int column, const "
        "QModelIndex &parent) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def clearItemData(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::clearItemData(const QModelIndex &index)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.clearItemData' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::clearItemData(const QModelIndex "
        "&index)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def columnCount(*__, **_) -> Never:
    """
    Qt's 'int QRangeModelImplBase::columnCount(const QModelIndex &parent)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.columnCount' has no cute function yet. Qt's "
        "'int QRangeModelImplBase::columnCount(const QModelIndex &parent) "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def createIndex(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QRangeModelImplBase::createIndex(int row, int column,
    const void *ptr) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.createIndex' has no cute function yet. Qt's "
        "'QModelIndex QRangeModelImplBase::createIndex(int row, int column, "
        "const void *ptr) const': names 'void', which has no cute class yet."
    )

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QVariant QRangeModelImplBase::data(const QModelIndex &index, int
    role) const': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.data' has no cute function yet. Qt's "
        "'QVariant QRangeModelImplBase::data(const QModelIndex &index, int "
        "role) const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void QRangeModelImplBase::dataChanged(const QModelIndex &from,
    const QModelIndex &to, const QList<int> &roles)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.dataChanged' has no cute function yet. Qt's "
        "'void QRangeModelImplBase::dataChanged(const QModelIndex &from, "
        "const QModelIndex &to, const QList<int> &roles)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def dropMimeData(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.dropMimeData' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::dropMimeData(const QMimeData *data, "
        "Qt::DropAction action, int row, int column, const QModelIndex "
        "&parent)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def flags(*__, **_) -> Never:
    """
    Qt's 'Qt::ItemFlags QRangeModelImplBase::flags(const QModelIndex &index)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.flags' has no cute function yet. Qt's "
        "'Qt::ItemFlags QRangeModelImplBase::flags(const QModelIndex "
        "&index) const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def headerData(*__, **_) -> Never:
    """
    Qt's 'QVariant QRangeModelImplBase::headerData(int section,
    Qt::Orientation orientation, int role) const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.headerData' has no cute function yet. Qt's "
        "'QVariant QRangeModelImplBase::headerData(int section, "
        "Qt::Orientation orientation, int role) const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def index(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QRangeModelImplBase::index(int row, int column, const
    QModelIndex &parent) const': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.index' has no cute function yet. Qt's "
        "'QModelIndex QRangeModelImplBase::index(int row, int column, const "
        "QModelIndex &parent) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def insertColumns(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::insertColumns(int column, int count,
    const QModelIndex &parent)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.insertColumns' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::insertColumns(int column, int count, "
        "const QModelIndex &parent)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::insertRows(int row, int count, const
    QModelIndex &parent)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.insertRows' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::insertRows(int row, int count, const "
        "QModelIndex &parent)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def interfaceVersion(*__, **_) -> Never:
    """
    Qt's 'void QRangeModelImplBase::interfaceVersion(int &version) const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.interfaceVersion' has no cute function yet. "
        "Qt's 'void QRangeModelImplBase::interfaceVersion(int &version) "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def invalidateCaches(*__, **_) -> Never:
    """
    Qt's 'void QRangeModelImplBase::invalidateCaches()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.invalidateCaches' has no cute function yet. "
        "Qt's 'void QRangeModelImplBase::invalidateCaches()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def itemData(*__, **_) -> Never:
    """
    Qt's 'QMap<int, QVariant> QRangeModelImplBase::itemData(const QModelIndex
    &index) const': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.itemData' has no cute function yet. Qt's "
        "'QMap<int, QVariant> QRangeModelImplBase::itemData(const "
        "QModelIndex &index) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def itemModel(*__, **_) -> Never:
    """
    - Qt's 'QAbstractItemModel &QRangeModelImplBase::itemModel()': gives a
      type Python has no way to take yet.
    - Qt's 'const QAbstractItemModel &QRangeModelImplBase::itemModel()
      const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.itemModel' has no cute function yet. Qt's "
        "'QAbstractItemModel &QRangeModelImplBase::itemModel()': gives a "
        "type Python has no way to take yet. Qt's 'const QAbstractItemModel "
        "&QRangeModelImplBase::itemModel() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def match(*__, **_) -> Never:
    """
    Qt's 'QModelIndexList QRangeModelImplBase::match(const QModelIndex
    &start, int role, const QVariant &value, int hits, Qt::MatchFlags flags)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.match' has no cute function yet. Qt's "
        "'QModelIndexList QRangeModelImplBase::match(const QModelIndex "
        "&start, int role, const QVariant &value, int hits, Qt::MatchFlags "
        "flags) const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def mimeData(*__, **_) -> Never:
    """
    Qt's 'QMimeData *QRangeModelImplBase::mimeData(const QModelIndexList
    &indexes) const': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.mimeData' has no cute function yet. Qt's "
        "'QMimeData *QRangeModelImplBase::mimeData(const QModelIndexList "
        "&indexes) const': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def mimeTypes(*__, **_) -> Never:
    """
    Qt's 'QStringList QRangeModelImplBase::mimeTypes() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.mimeTypes' has no cute function yet. Qt's "
        "'QStringList QRangeModelImplBase::mimeTypes() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def moveColumns(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::moveColumns(const QModelIndex
    &sourceParent, int sourceColumn, int count, const QModelIndex
    &destParent, int destColumn)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.moveColumns' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::moveColumns(const QModelIndex "
        "&sourceParent, int sourceColumn, int count, const QModelIndex "
        "&destParent, int destColumn)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def moveRows(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::moveRows(const QModelIndex &sourceParent,
    int sourceRow, int count, const QModelIndex &destParent, int destRow)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.moveRows' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::moveRows(const QModelIndex "
        "&sourceParent, int sourceRow, int count, const QModelIndex "
        "&destParent, int destRow)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def multiData(*__, **_) -> Never:
    """
    Qt's 'void QRangeModelImplBase::multiData(const QModelIndex &index,
    QModelRoleDataSpan roleDataSpan) const': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.multiData' has no cute function yet. Qt's "
        "'void QRangeModelImplBase::multiData(const QModelIndex &index, "
        "QModelRoleDataSpan roleDataSpan) const': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def parent(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QRangeModelImplBase::parent(const QModelIndex &child)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.parent' has no cute function yet. Qt's "
        "'QModelIndex QRangeModelImplBase::parent(const QModelIndex &child) "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def removeColumns(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::removeColumns(int column, int count,
    const QModelIndex &parent)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.removeColumns' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::removeColumns(int column, int count, "
        "const QModelIndex &parent)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def removeRows(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::removeRows(int row, int count, const
    QModelIndex &parent)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.removeRows' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::removeRows(int row, int count, const "
        "QModelIndex &parent)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def roleNamesForMetaObject(*__, **_) -> Never:
    """
    Qt's 'QHash<int, QByteArray>
    QRangeModelImplBase::roleNamesForMetaObject(const QAbstractItemModel
    &model, const QMetaObject &metaObject)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.roleNamesForMetaObject' has no cute function "
        "yet. Qt's 'QHash<int, QByteArray> "
        "QRangeModelImplBase::roleNamesForMetaObject(const "
        "QAbstractItemModel &model, const QMetaObject &metaObject)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def roleProperties(*__, **_) -> Never:
    """
    Qt's 'QHash<int, QMetaProperty> QRangeModelImplBase::roleProperties(const
    QAbstractItemModel &model, const QMetaObject &metaObject)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.roleProperties' has no cute function yet. "
        "Qt's 'QHash<int, QMetaProperty> "
        "QRangeModelImplBase::roleProperties(const QAbstractItemModel "
        "&model, const QMetaObject &metaObject)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def rowCount(*__, **_) -> Never:
    """
    Qt's 'int QRangeModelImplBase::rowCount(const QModelIndex &parent)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.rowCount' has no cute function yet. Qt's 'int "
        "QRangeModelImplBase::rowCount(const QModelIndex &parent) const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setAutoConnectPolicy(*__, **_) -> Never:
    """
    Qt's 'void QRangeModelImplBase::setAutoConnectPolicy()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.setAutoConnectPolicy' has no cute function "
        "yet. Qt's 'void QRangeModelImplBase::setAutoConnectPolicy()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setData(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::setData(const QModelIndex &index, const
    QVariant &data, int role)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.setData' has no cute function yet. Qt's 'bool "
        "QRangeModelImplBase::setData(const QModelIndex &index, const "
        "QVariant &data, int role)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setHeaderData(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &data, int role)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.setHeaderData' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::setHeaderData(int section, "
        "Qt::Orientation orientation, const QVariant &data, int role)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setItemData(*__, **_) -> Never:
    """
    Qt's 'bool QRangeModelImplBase::setItemData(const QModelIndex &index,
    const QMap<int, QVariant> &data)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.setItemData' has no cute function yet. Qt's "
        "'bool QRangeModelImplBase::setItemData(const QModelIndex &index, "
        "const QMap<int, QVariant> &data)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def sibling(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QRangeModelImplBase::sibling(int row, int column, const
    QModelIndex &index) const': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.sibling' has no cute function yet. Qt's "
        "'QModelIndex QRangeModelImplBase::sibling(int row, int column, "
        "const QModelIndex &index) const': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def sort(*__, **_) -> Never:
    """
    Qt's 'void QRangeModelImplBase::sort(int column, Qt::SortOrder order)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QRangeModelImplBase.sort' has no cute function yet. Qt's 'void "
        "QRangeModelImplBase::sort(int column, Qt::SortOrder order)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
