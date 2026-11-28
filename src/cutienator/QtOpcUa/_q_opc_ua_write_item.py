"""
QOpcUaWriteItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuawriteitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDateTime, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QVariant = WAIT['QVariant']


class QOpcUaWriteItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaWriteItem: a plain Python object standing in
  front of one C++ QOpcUaWriteItem.

  C++ hands a QOpcUaWriteItem around as a copy, so every C++ QOpcUaWriteItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaWriteItem that has a ritual and that Python
  can call so far, 17 names in all: 'nodeId', 'setNodeId', 'attribute',
  'setAttribute', 'indexRange', 'setIndexRange', 'value', 'setValue', 'type',
  'setType', 'sourceTimestamp', 'setSourceTimestamp', 'serverTimestamp',
  'setServerTimestamp', 'statusCode', 'hasStatusCode', 'setStatusCode'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaWriteItem &QOpcUaWriteItem::operator=(const QOpcUaWriteItem
    &rhs)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaWriteItem::~QOpcUaWriteItem()': the destructor: Python
    removes its C++ QOpcUaWriteItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaWriteItem is created at the first use, not by
    'QOpcUaWriteItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaWriteItem back gives a copy the ritual made for
    Python, in a new cute QOpcUaWriteItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaWriteItem'

  #  Qt's '~QOpcUaWriteItem()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaWriteItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QOpcUaWriteItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaWriteItem::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaWriteItem::nodeId() const
    return self.uglySide.call('ritual_ZNK15QOpcUaWriteItem6nodeIdEv')

  def attribute(self) -> QOpcUa.NodeAttribute:
    """
    Calls Qt's 'QOpcUa::NodeAttribute QOpcUaWriteItem::attribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#attribute

    Returns
    -------

    QOpcUa.NodeAttribute
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.NodeAttribute(number)' gives.
    """
    #  QOpcUa::NodeAttribute QOpcUaWriteItem::attribute() const
    return QOpcUa.NodeAttribute(self.uglySide.call(
        'ritual_ZNK15QOpcUaWriteItem9attributeEv',
    ))

  def indexRange(self) -> str:
    """
    Calls Qt's 'QString QOpcUaWriteItem::indexRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#indexRange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaWriteItem::indexRange() const
    return self.uglySide.call('ritual_ZNK15QOpcUaWriteItem10indexRangeEv')

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaWriteItem::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaWriteItem::value() const
    address = self.uglySide.call('ritual_ZNK15QOpcUaWriteItem5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> QOpcUa.Types:
    """
    Calls Qt's 'QOpcUa::Types QOpcUaWriteItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#type

    Returns
    -------

    QOpcUa.Types
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.Types(number)'
      gives.
    """
    #  QOpcUa::Types QOpcUaWriteItem::type() const
    return QOpcUa.Types(self.uglySide.call(
        'ritual_ZNK15QOpcUaWriteItem4typeEv',
    ))

  def sourceTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaWriteItem::sourceTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteitem.html#sourceTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaWriteItem::sourceTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaWriteItem15sourceTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def serverTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaWriteItem::serverTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteitem.html#serverTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaWriteItem::serverTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaWriteItem15serverTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaWriteItem::statusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaWriteItem::statusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK15QOpcUaWriteItem10statusCodeEv',
    ))

  def hasStatusCode(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaWriteItem::hasStatusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#hasStatusCode
    """
    #  bool QOpcUaWriteItem::hasStatusCode() const
    return self.uglySide.call('ritual_ZNK15QOpcUaWriteItem13hasStatusCodeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setNodeId(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaWriteItem::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem9setNodeIdERK7QString', nodeId,
    )

  @overload(QOpcUa.NodeAttribute)
  def setAttribute(self, attribute: QOpcUa.NodeAttribute) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setAttribute(QOpcUa::NodeAttribute
    attribute)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#setAttribute

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.
    """
    #  void QOpcUaWriteItem::setAttribute(QOpcUa::NodeAttribute attribute)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem12setAttributeEN6QOpcUa13NodeAttributeE',
        attribute.value,
    )

  @overload(str)
  def setIndexRange(self, indexRange: str) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setIndexRange(const QString
    &indexRange)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#setIndexRange

    Parameters
    ----------

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaWriteItem::setIndexRange(const QString &indexRange)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem13setIndexRangeERK7QString', indexRange,
    )

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaWriteItem::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem8setValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(QVariant, QOpcUa.Types)
  def setValue(self, value: QVariant, type: QOpcUa.Types) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setValue(const QVariant &value,
    QOpcUa::Types type)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QOpcUa.Types
      Passed on as its number.
    """
    #  void QOpcUaWriteItem::setValue(const QVariant &value, QOpcUa::Types
    #      type)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem8setValueERK8QVariantN6QOpcUa5TypesE',
        self._valueOf(value), type.value,
    )

  @overload(QOpcUa.Types)
  def setType(self, type: QOpcUa.Types) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setType(QOpcUa::Types type)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#setType

    Parameters
    ----------

    type : QOpcUa.Types
      Passed on as its number.
    """
    #  void QOpcUaWriteItem::setType(QOpcUa::Types type)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem7setTypeEN6QOpcUa5TypesE', type.value,
    )

  @overload(QDateTime)
  def setSourceTimestamp(self, sourceTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setSourceTimestamp(const QDateTime
    &sourceTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteitem.html#setSourceTimestamp

    Parameters
    ----------

    sourceTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaWriteItem::setSourceTimestamp(const QDateTime
    #      &sourceTimestamp)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem18setSourceTimestampERK9QDateTime',
        self._valueOf(sourceTimestamp),
    )

  @overload(QDateTime)
  def setServerTimestamp(self, serverTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setServerTimestamp(const QDateTime
    &serverTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteitem.html#setServerTimestamp

    Parameters
    ----------

    serverTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaWriteItem::setServerTimestamp(const QDateTime
    #      &serverTimestamp)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem18setServerTimestampERK9QDateTime',
        self._valueOf(serverTimestamp),
    )

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void QOpcUaWriteItem::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuawriteitem.html#setStatusCode

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaWriteItem::setStatusCode(QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN15QOpcUaWriteItem13setStatusCodeEN6QOpcUa12UaStatusCodeE',
        statusCode.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaWriteItem::QOpcUaWriteItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteitem.html#QOpcUaWriteItem
    """
    #  QOpcUaWriteItem::QOpcUaWriteItem()
    self._noteCreation(QOpcUaWriteItem, lambda: Rituals.call(
        'ritual_ZN15QOpcUaWriteItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaWriteItem) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaWriteItem::QOpcUaWriteItem(const
    QOpcUaWriteItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteitem.html#QOpcUaWriteItem

    Parameters
    ----------

    other : QOpcUaWriteItem
      Passed on as a value: Qt reads the C++ QOpcUaWriteItem, which stays
      Python's own.
    """
    #  QOpcUaWriteItem::QOpcUaWriteItem(const QOpcUaWriteItem &other)
    self._noteCreation(QOpcUaWriteItem, lambda: Rituals.call(
        'ritual_ZN15QOpcUaWriteItemC1ERKS_', self._valueOf(other),
    ))

  @overload(str, QOpcUa.NodeAttribute, QVariant)
  @overload(str, QOpcUa.NodeAttribute, QVariant, QOpcUa.Types)
  @overload(str, QOpcUa.NodeAttribute, QVariant, QOpcUa.Types, str)
  def __init__(
      self,
      nodeId: str,
      attribute: QOpcUa.NodeAttribute,
      value: QVariant,
      type: QOpcUa.Types = QOpcUa.Types.Undefined,
      indexRange: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaWriteItem::QOpcUaWriteItem(const
    QString &nodeId, QOpcUa::NodeAttribute attribute, const QVariant &value,
    QOpcUa::Types type, const QString &indexRange)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuawriteitem.html#QOpcUaWriteItem

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QOpcUa.Types
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.Types.Undefined.

    indexRange : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QOpcUaWriteItem::QOpcUaWriteItem(const QString &nodeId,
    #      QOpcUa::NodeAttribute attribute, const QVariant &value,
    #      QOpcUa::Types type, const QString &indexRange)
    self._noteCreation(QOpcUaWriteItem, lambda: Rituals.call(
        'ritual_ZN15QOpcUaWriteItemC1ERK7QStringN6QOpcUa13NodeAttributeERK8'
        'QVariantNS3_5TypesES2_',
        nodeId, attribute.value, self._valueOf(value), type.value,
        indexRange,
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


#  Qt's 'QList<QOpcUaWriteItem>': the list of QOpcUaWriteItem, which
#  'QList[QOpcUaWriteItem]' gives. It is made here, so that there is one as
#  soon as there can be a QOpcUaWriteItem.
QList.createKind(
    QOpcUaWriteItem, 'value',
    make='ritual_list_make_QOpcUaWriteItem',
    add='ritual_list_add_QOpcUaWriteItem',
    size='ritual_list_size_QOpcUaWriteItem',
    at='ritual_list_at_QOpcUaWriteItem',
    drop='ritual_list_drop_QOpcUaWriteItem',
)
