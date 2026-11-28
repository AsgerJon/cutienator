"""
QOpcUaReadItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuareaditem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa


class QOpcUaReadItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaReadItem: a plain Python object standing in
  front of one C++ QOpcUaReadItem.

  C++ hands a QOpcUaReadItem around as a copy, so every C++ QOpcUaReadItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaReadItem that has a ritual and that Python can
  call so far, 8 names in all: 'nodeId', 'setNodeId', 'attribute',
  'setAttribute', 'indexRange', 'setIndexRange', '__eq__', '__ne__'. It can
  be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaReadItem &QOpcUaReadItem::operator=(const QOpcUaReadItem
    &rhs)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaReadItem::~QOpcUaReadItem()': the destructor: Python removes
    its C++ QOpcUaReadItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaReadItem is created at the first use, not by
    'QOpcUaReadItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaReadItem back gives a copy the ritual made for
    Python, in a new cute QOpcUaReadItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaReadItem'

  #  Qt's '~QOpcUaReadItem()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaReadItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QOpcUaReadItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaReadItem::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaReadItem::nodeId() const
    return self.uglySide.call('ritual_ZNK14QOpcUaReadItem6nodeIdEv')

  def attribute(self) -> QOpcUa.NodeAttribute:
    """
    Calls Qt's 'QOpcUa::NodeAttribute QOpcUaReadItem::attribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#attribute

    Returns
    -------

    QOpcUa.NodeAttribute
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.NodeAttribute(number)' gives.
    """
    #  QOpcUa::NodeAttribute QOpcUaReadItem::attribute() const
    return QOpcUa.NodeAttribute(self.uglySide.call(
        'ritual_ZNK14QOpcUaReadItem9attributeEv',
    ))

  def indexRange(self) -> str:
    """
    Calls Qt's 'QString QOpcUaReadItem::indexRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#indexRange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaReadItem::indexRange() const
    return self.uglySide.call('ritual_ZNK14QOpcUaReadItem10indexRangeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaReadItem::setNodeId(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaReadItem::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN14QOpcUaReadItem9setNodeIdERK7QString', nodeId,
    )

  @overload(QOpcUa.NodeAttribute)
  def setAttribute(self, attribute: QOpcUa.NodeAttribute) -> None:
    """
    Calls Qt's 'void QOpcUaReadItem::setAttribute(QOpcUa::NodeAttribute
    attribute)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#setAttribute

    Parameters
    ----------

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.
    """
    #  void QOpcUaReadItem::setAttribute(QOpcUa::NodeAttribute attribute)
    self.uglySide.call(
        'ritual_ZN14QOpcUaReadItem12setAttributeEN6QOpcUa13NodeAttributeE',
        attribute.value,
    )

  @overload(str)
  def setIndexRange(self, indexRange: str) -> None:
    """
    Calls Qt's 'void QOpcUaReadItem::setIndexRange(const QString
    &indexRange)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#setIndexRange

    Parameters
    ----------

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaReadItem::setIndexRange(const QString &indexRange)
    self.uglySide.call(
        'ritual_ZN14QOpcUaReadItem13setIndexRangeERK7QString', indexRange,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaReadItem) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaReadItem &lhs, const
    QOpcUaReadItem &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#operator==

    Parameters
    ----------

    rhs : QOpcUaReadItem
      Passed on as a value: Qt reads the C++ QOpcUaReadItem, which stays
      Python's own.
    """
    #  bool operator==(const QOpcUaReadItem &lhs, const QOpcUaReadItem &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QOpcUaReadItemS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QOpcUaReadItem) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaReadItem &lhs, const
    QOpcUaReadItem &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaReadItem
      Passed on as a value: Qt reads the C++ QOpcUaReadItem, which stays
      Python's own.
    """
    #  bool operator!=(const QOpcUaReadItem &lhs, const QOpcUaReadItem &rhs)
    return Rituals.call(
        'ritual_ZneRK14QOpcUaReadItemS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaReadItem::QOpcUaReadItem()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#QOpcUaReadItem
    """
    #  QOpcUaReadItem::QOpcUaReadItem()
    self._noteCreation(QOpcUaReadItem, lambda: Rituals.call(
        'ritual_ZN14QOpcUaReadItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaReadItem) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaReadItem::QOpcUaReadItem(const
    QOpcUaReadItem &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#QOpcUaReadItem

    Parameters
    ----------

    other : QOpcUaReadItem
      Passed on as a value: Qt reads the C++ QOpcUaReadItem, which stays
      Python's own.
    """
    #  QOpcUaReadItem::QOpcUaReadItem(const QOpcUaReadItem &other)
    self._noteCreation(QOpcUaReadItem, lambda: Rituals.call(
        'ritual_ZN14QOpcUaReadItemC1ERKS_', self._valueOf(other),
    ))

  @overload(str)
  @overload(str, QOpcUa.NodeAttribute)
  @overload(str, QOpcUa.NodeAttribute, str)
  def __init__(
      self,
      nodeId: str,
      attr: QOpcUa.NodeAttribute = QOpcUa.NodeAttribute.Value,
      indexRange: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaReadItem::QOpcUaReadItem(const
    QString &nodeId, QOpcUa::NodeAttribute attr, const QString &indexRange)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuareaditem.html#QOpcUaReadItem

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    attr : QOpcUa.NodeAttribute
      Passed on as its number. May be left out, as in Qt: it is then
      QOpcUa.NodeAttribute.Value.

    indexRange : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QOpcUaReadItem::QOpcUaReadItem(const QString &nodeId,
    #      QOpcUa::NodeAttribute attr, const QString &indexRange)
    self._noteCreation(QOpcUaReadItem, lambda: Rituals.call(
        'ritual_ZN14QOpcUaReadItemC1ERK7QStringN6QOpcUa13NodeAttributeES2_',
        nodeId, attr.value, indexRange,
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


#  Qt's 'QList<QOpcUaReadItem>': the list of QOpcUaReadItem, which
#  'QList[QOpcUaReadItem]' gives. It is made here, so that there is one as
#  soon as there can be a QOpcUaReadItem.
QList.createKind(
    QOpcUaReadItem, 'value',
    make='ritual_list_make_QOpcUaReadItem',
    add='ritual_list_add_QOpcUaReadItem',
    size='ritual_list_size_QOpcUaReadItem',
    at='ritual_list_at_QOpcUaReadItem',
    drop='ritual_list_drop_QOpcUaReadItem',
)
