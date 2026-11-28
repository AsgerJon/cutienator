"""
qdesigner_internal::ItemData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ItemData to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QListWidgetItem, QTableWidgetItem, QTreeWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QListWidgetItem = WAIT['QListWidgetItem']
  QTableWidgetItem = WAIT['QTableWidgetItem']
  QTreeWidgetItem = WAIT['QTreeWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ItemData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::ItemData: a plain Python object
  standing in front of one C++ qdesigner_internal::ItemData.

  C++ hands a qdesigner_internal::ItemData around as a copy, so every C++
  qdesigner_internal::ItemData behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ItemData that has a ritual and
  that Python can call so far, 6 names in all: 'createListItem',
  'createTableItem', 'fillTreeItemColumn', 'isValid', '__eq__', '__ne__'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::ItemData::~ItemData()': the destructor: Python
    removes its C++ qdesigner_internal::ItemData by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::ItemData is created at the first use, not by
    'qdesigner_internal::ItemData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::ItemData back gives a copy the
    ritual made for Python, in a new cute qdesigner_internal::ItemData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ItemData'

  #  Qt's '~qdesigner_internal::ItemData()'. Naming it makes this a value
  #  class: Python owns every C++ qdesigner_internal::ItemData behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal8ItemDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(NoneType, bool)
  def createListItem(
      self,
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
      editor: bool,
  ) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem
    *qdesigner_internal::ItemData::createListItem(DesignerIconCache
    *iconCache, bool editor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#createListItem

    Parameters
    ----------

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem
    #      *qdesigner_internal::ItemData::createListItem(DesignerIconCache
    #      *iconCache, bool editor) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ItemData14createListItemEPNS_17Desi'
        'gnerIconCacheEb',
        self._addressOf(iconCache), editor,
    )
    from ..QtWidgets import QListWidgetItem
    return QListWidgetItem._cuteAt(address)

  @overload(WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(NoneType, bool)
  def createTableItem(
      self,
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
      editor: bool,
  ) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem
    *qdesigner_internal::ItemData::createTableItem(DesignerIconCache
    *iconCache, bool editor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#createTableItem

    Parameters
    ----------

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem
    #      *qdesigner_internal::ItemData::createTableItem(DesignerIconCache
    #      *iconCache, bool editor) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ItemData15createTableItemEPNS_17Des'
        'ignerIconCacheEb',
        self._addressOf(iconCache), editor,
    )
    from ..QtWidgets import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::ItemData::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#isValid
    """
    #  bool qdesigner_internal::ItemData::isValid() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ItemData7isValidEv',
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

  @overload(THIS)
  def __eq__(self, rhs: ItemData) -> bool:
    """
    Calls Qt's 'bool operator==(const ItemData &lhs, const ItemData &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#operator==

    Parameters
    ----------

    rhs : ItemData
      Passed on as a value: Qt reads the C++ qdesigner_internal::ItemData,
      which stays Python's own.
    """
    #  bool operator==(const ItemData &lhs, const ItemData &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_8ItemDataES2_',
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
  def __ne__(self, rhs: ItemData) -> bool:
    """
    Calls Qt's 'bool operator!=(const ItemData &lhs, const ItemData &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#operator!=

    Parameters
    ----------

    rhs : ItemData
      Passed on as a value: Qt reads the C++ qdesigner_internal::ItemData,
      which stays Python's own.
    """
    #  bool operator!=(const ItemData &lhs, const ItemData &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_8ItemDataES2_',
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
    Notes what was given, for Qt's
    'qdesigner_internal::ItemData::ItemData()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#ItemData
    """
    #  qdesigner_internal::ItemData::ItemData()
    self._noteCreation(ItemData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal8ItemDataC1Ev',
    ))

  @overload(QListWidgetItem, bool)
  @overload(NoneType, bool)
  def __init__(self, item: Optional[QListWidgetItem], editor: bool) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ItemData::ItemData(const QListWidgetItem *item, bool
    editor)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#ItemData

    Parameters
    ----------

    item : Optional[QListWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  qdesigner_internal::ItemData::ItemData(const QListWidgetItem *item,
    #      bool editor)
    self._noteCreation(ItemData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal8ItemDataC1EPK15QListWidgetItemb',
        self._addressOf(item), editor,
    ))

  @overload(QTableWidgetItem, bool)
  def __init__(self, item: Optional[QTableWidgetItem], editor: bool) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ItemData::ItemData(const QTableWidgetItem *item,
    bool editor)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#ItemData

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  qdesigner_internal::ItemData::ItemData(const QTableWidgetItem *item,
    #      bool editor)
    self._noteCreation(ItemData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal8ItemDataC1EPK16QTableWidgetItemb',
        self._addressOf(item), editor,
    ))

  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def __init__(self, item: Optional[QTreeWidgetItem], column: int) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ItemData::ItemData(const QTreeWidgetItem *item, int
    column)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html#ItemData

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.
    """
    #  qdesigner_internal::ItemData::ItemData(const QTreeWidgetItem *item,
    #      int column)
    self._noteCreation(ItemData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal8ItemDataC1EPK15QTreeWidgetItemi',
        self._addressOf(item), column,
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

  @overload(
      QTreeWidgetItem, int, WAIT['qdesigner_internal.DesignerIconCache'],
  )
  @overload(QTreeWidgetItem, int, NoneType)
  @overload(NoneType, int, WAIT['qdesigner_internal.DesignerIconCache'])
  @overload(NoneType, int, NoneType)
  def fillTreeItemColumn(
      self,
      item: Optional[QTreeWidgetItem],
      column: int,
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ItemData::fillTreeItemColumn(QTreeWidgetItem *item,
    int column, DesignerIconCache *iconCache) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-itemdata.html

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ItemData::fillTreeItemColumn(QTreeWidgetItem
    #      *item, int column, DesignerIconCache *iconCache) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ItemData18fillTreeItemColumnEP15QTr'
        'eeWidgetItemiPNS_17DesignerIconCacheE',
        self._addressOf(item), column, self._addressOf(iconCache),
    )
