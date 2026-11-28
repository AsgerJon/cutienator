"""
QOpcUaDeleteReferenceItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuadeletereferenceitem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QOpcUaExpandedNodeId
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']


class QOpcUaDeleteReferenceItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaDeleteReferenceItem: a plain Python object
  standing in front of one C++ QOpcUaDeleteReferenceItem.

  C++ hands a QOpcUaDeleteReferenceItem around as a copy, so every C++
  QOpcUaDeleteReferenceItem behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaDeleteReferenceItem that has a ritual and that
  Python can call so far, 10 names in all: 'sourceNodeId', 'setSourceNodeId',
  'referenceTypeId', 'setReferenceTypeId', 'isForwardReference',
  'setIsForwardReference', 'targetNodeId', 'setTargetNodeId',
  'deleteBidirectional', 'setDeleteBidirectional'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaDeleteReferenceItem
    &QOpcUaDeleteReferenceItem::operator=(const QOpcUaDeleteReferenceItem
    &rhs)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaDeleteReferenceItem::~QOpcUaDeleteReferenceItem()': the
    destructor: Python removes its C++ QOpcUaDeleteReferenceItem by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaDeleteReferenceItem is created at the first use, not by
    'QOpcUaDeleteReferenceItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaDeleteReferenceItem back gives a copy the
    ritual made for Python, in a new cute QOpcUaDeleteReferenceItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaDeleteReferenceItem'

  #  Qt's '~QOpcUaDeleteReferenceItem()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaDeleteReferenceItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpcUaDeleteReferenceItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sourceNodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaDeleteReferenceItem::sourceNodeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#sourceNodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaDeleteReferenceItem::sourceNodeId() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaDeleteReferenceItem12sourceNodeIdEv',
    )

  def referenceTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaDeleteReferenceItem::referenceTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#referenceTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaDeleteReferenceItem::referenceTypeId() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaDeleteReferenceItem15referenceTypeIdEv',
    )

  def isForwardReference(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDeleteReferenceItem::isForwardReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#isForwardReference
    """
    #  bool QOpcUaDeleteReferenceItem::isForwardReference() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaDeleteReferenceItem18isForwardReferenceEv',
    )

  def targetNodeId(self) -> QOpcUaExpandedNodeId:
    """
    Calls Qt's 'QOpcUaExpandedNodeId
    QOpcUaDeleteReferenceItem::targetNodeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#targetNodeId

    Returns
    -------

    QOpcUaExpandedNodeId
      A new cute QOpcUaExpandedNodeId around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaExpandedNodeId QOpcUaDeleteReferenceItem::targetNodeId() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaDeleteReferenceItem12targetNodeIdEv',
    )
    from . import QOpcUaExpandedNodeId
    return QOpcUaExpandedNodeId._cuteOwning(address)

  def deleteBidirectional(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDeleteReferenceItem::deleteBidirectional() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#deleteBidirectional
    """
    #  bool QOpcUaDeleteReferenceItem::deleteBidirectional() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaDeleteReferenceItem19deleteBidirectionalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSourceNodeId(self, sourceNodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaDeleteReferenceItem::setSourceNodeId(const QString
    &sourceNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#setSourceNodeId

    Parameters
    ----------

    sourceNodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaDeleteReferenceItem::setSourceNodeId(const QString
    #      &sourceNodeId)
    self.uglySide.call(
        'ritual_ZN25QOpcUaDeleteReferenceItem15setSourceNodeIdERK7QString',
        sourceNodeId,
    )

  @overload(str)
  def setReferenceTypeId(self, referenceTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaDeleteReferenceItem::setReferenceTypeId(const
    QString &referenceTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#setReferenceTypeId

    Parameters
    ----------

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaDeleteReferenceItem::setReferenceTypeId(const QString
    #      &referenceTypeId)
    self.uglySide.call(
        'ritual_ZN25QOpcUaDeleteReferenceItem18setReferenceTypeIdERK7QStrin'
        'g',
        referenceTypeId,
    )

  @overload(bool)
  def setIsForwardReference(self, isForwardReference: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDeleteReferenceItem::setIsForwardReference(bool
    isForwardReference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html

    Parameters
    ----------

    isForwardReference : bool
      Passed on as it is.
    """
    #  void QOpcUaDeleteReferenceItem::setIsForwardReference(bool
    #      isForwardReference)
    self.uglySide.call(
        'ritual_ZN25QOpcUaDeleteReferenceItem21setIsForwardReferenceEb',
        isForwardReference,
    )

  @overload(QOpcUaExpandedNodeId)
  def setTargetNodeId(self, targetNodeId: QOpcUaExpandedNodeId) -> None:
    """
    Calls Qt's 'void QOpcUaDeleteReferenceItem::setTargetNodeId(const
    QOpcUaExpandedNodeId &targetNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html#setTargetNodeId

    Parameters
    ----------

    targetNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.
    """
    #  void QOpcUaDeleteReferenceItem::setTargetNodeId(const
    #      QOpcUaExpandedNodeId &targetNodeId)
    self.uglySide.call(
        'ritual_ZN25QOpcUaDeleteReferenceItem15setTargetNodeIdERK20QOpcUaEx'
        'pandedNodeId',
        self._valueOf(targetNodeId),
    )

  @overload(bool)
  def setDeleteBidirectional(self, deleteBidirectional: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDeleteReferenceItem::setDeleteBidirectional(bool
    deleteBidirectional)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html

    Parameters
    ----------

    deleteBidirectional : bool
      Passed on as it is.
    """
    #  void QOpcUaDeleteReferenceItem::setDeleteBidirectional(bool
    #      deleteBidirectional)
    self.uglySide.call(
        'ritual_ZN25QOpcUaDeleteReferenceItem22setDeleteBidirectionalEb',
        deleteBidirectional,
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
    Notes what was given, for Qt's
    'QOpcUaDeleteReferenceItem::QOpcUaDeleteReferenceItem()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html
    """
    #  QOpcUaDeleteReferenceItem::QOpcUaDeleteReferenceItem()
    self._noteCreation(QOpcUaDeleteReferenceItem, lambda: Rituals.call(
        'ritual_ZN25QOpcUaDeleteReferenceItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaDeleteReferenceItem) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaDeleteReferenceItem::QOpcUaDeleteReferenceItem(const
    QOpcUaDeleteReferenceItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadeletereferenceitem.html

    Parameters
    ----------

    other : QOpcUaDeleteReferenceItem
      Passed on as a value: Qt reads the C++ QOpcUaDeleteReferenceItem, which
      stays Python's own.
    """
    #  QOpcUaDeleteReferenceItem::QOpcUaDeleteReferenceItem(const
    #      QOpcUaDeleteReferenceItem &other)
    self._noteCreation(QOpcUaDeleteReferenceItem, lambda: Rituals.call(
        'ritual_ZN25QOpcUaDeleteReferenceItemC1ERKS_', self._valueOf(other),
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
