"""
QTreeWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QItemSelectionModel, QList, QStringList
from . import QAbstractItemView, QTreeView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QMimeData, QModelIndex, QPoint
  from ..QtCore import QRect
  from ..QtGui import QDropEvent
  from . import QTreeWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QTreeWidgetItem = WAIT['QTreeWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeWidget(QTreeView):
  """
  The cute side of Qt's QTreeWidget: a plain Python object standing in front
  of one C++ QTreeWidget.

  It is built on the cute 'QTreeView', as Qt's QTreeWidget is built on Qt's
  QTreeView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTreeWidget that has a ritual and that Python can
  call so far, 48 names in all: 'metaObject', 'tr', 'columnCount',
  'setColumnCount', 'invisibleRootItem', 'topLevelItem', 'topLevelItemCount',
  'insertTopLevelItem', 'addTopLevelItem', 'takeTopLevelItem',
  'indexOfTopLevelItem', 'insertTopLevelItems', 'addTopLevelItems',
  'headerItem', 'setHeaderItem', 'setHeaderLabels', 'setHeaderLabel',
  'currentItem', 'currentColumn', 'setCurrentItem', 'itemAt',
  'visualItemRect', 'sortColumn', 'sortItems', 'editItem',
  'openPersistentEditor', 'closePersistentEditor', 'isPersistentEditorOpen',
  'itemWidget', 'setItemWidget', 'removeItemWidget', 'selectedItems',
  'findItems', 'itemAbove', 'itemBelow', 'indexFromItem', 'itemFromIndex',
  'setSelectionModel', 'supportedDragActions', 'setSupportedDragActions',
  'scrollToItem', 'expandItem', 'collapseItem', 'clear', 'event',
  'dropMimeData', 'supportedDropActions', 'dropEvent'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTreeWidget::~QTreeWidget()': the destructor: Python never removes
    a C++ QTreeWidget.

  What has no ritual
  ------------------

  21 of the 74 functions Qt declares: 10 a signal; 4 private; 2 takes or
  gives a type that cannot be passed yet; 2 protected; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QTreeWidget is created at the first use, not by
    'QTreeWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTreeWidget.
  - Qt tells when it has removed the C++ QTreeWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTreeWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTreeWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QTreeWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeWidget'

  #  A C++ QTreeWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTreeWidget'

  #  The functions Qt calls itself that QTreeWidget is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'mimeTypes': (
          'QStringList QTreeWidget::mimeTypes() const',
      ),
      'mimeData': (
          'QMimeData *QTreeWidget::mimeData(const QList<QTreeWidgetItem *> '
          '&) const',
      ),
  }

  #  The functions Qt calls itself that QTreeWidget is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'dropMimeData': (
          ('_ZN11QTreeWidget12dropMimeDataEP15QTreeWidgetItemiPK9QMimeDataN'
           '2Qt10DropActionE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QTreeWidgetItem'),
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QMimeData'),
               ('int', 'enum', 'QtCore:Qt.DropAction'),
           )),
      ),
      'supportedDropActions': (
          ('_ZNK11QTreeWidget20supportedDropActionsEv',
           ('int', 'flags', 'QtCore:Qt.DropAction'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTreeWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTreeWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#columnCount
    """
    #  int QTreeWidget::columnCount() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget11columnCountEv')

  def invisibleRootItem(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::invisibleRootItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#invisibleRootItem

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::invisibleRootItem() const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget17invisibleRootItemEv',
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(int)
  def topLevelItem(self, index: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::topLevelItem(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#topLevelItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::topLevelItem(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget12topLevelItemEi', index,
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  def topLevelItemCount(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::topLevelItemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#topLevelItemCount
    """
    #  int QTreeWidget::topLevelItemCount() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget17topLevelItemCountEv')

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def indexOfTopLevelItem(self, item: Optional[QTreeWidgetItem]) -> int:
    """
    Calls Qt's 'int QTreeWidget::indexOfTopLevelItem(QTreeWidgetItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#indexOfTopLevelItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTreeWidget::indexOfTopLevelItem(QTreeWidgetItem *item) const
    return self.uglySide.call(
        'ritual_ZNK11QTreeWidget19indexOfTopLevelItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  def headerItem(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::headerItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#headerItem

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::headerItem() const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget10headerItemEv')
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  def currentItem(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#currentItem

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::currentItem() const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget11currentItemEv')
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  def currentColumn(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::currentColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#currentColumn
    """
    #  int QTreeWidget::currentColumn() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget13currentColumnEv')

  @overload(QPoint)
  def itemAt(self, p: QPoint) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget6itemAtERK6QPoint', self._valueOf(p),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(int, int)
  def itemAt(self, x: int, y: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemAt(int x, int y) const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget6itemAtEii', x, y)
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def visualItemRect(self, item: Optional[QTreeWidgetItem]) -> QRect:
    """
    Calls Qt's 'QRect QTreeWidget::visualItemRect(const QTreeWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#visualItemRect

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTreeWidget::visualItemRect(const QTreeWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget14visualItemRectEPK15QTreeWidgetItem',
        self._addressOf(item),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def sortColumn(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::sortColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#sortColumn
    """
    #  int QTreeWidget::sortColumn() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget10sortColumnEv')

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def isPersistentEditorOpen(
      self,
      item: Optional[QTreeWidgetItem],
      column: int = 0,
  ) -> bool:
    """
    Calls Qt's 'bool QTreeWidget::isPersistentEditorOpen(QTreeWidgetItem
    *item, int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#isPersistentEditorOpen

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QTreeWidget::isPersistentEditorOpen(QTreeWidgetItem *item, int
    #      column) const
    return self.uglySide.call(
        'ritual_ZNK11QTreeWidget22isPersistentEditorOpenEP15QTreeWidgetItem'
        'i',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def itemWidget(
      self,
      item: Optional[QTreeWidgetItem],
      column: int,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QTreeWidget::itemWidget(QTreeWidgetItem *item, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemWidget

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QTreeWidget::itemWidget(QTreeWidgetItem *item, int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget10itemWidgetEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )
    return QWidget._cuteAt(address)

  def selectedItems(self) -> QList[QTreeWidgetItem]:
    """
    Calls Qt's 'QList<QTreeWidgetItem *> QTreeWidget::selectedItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#selectedItems

    Returns
    -------

    QList[QTreeWidgetItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTreeWidgetItem *> QTreeWidget::selectedItems() const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget13selectedItemsEv')
    from . import QTreeWidgetItem
    return QList[QTreeWidgetItem]._cuteOwning(address)

  @overload(str, Qt.MatchFlags)
  @overload(str, Qt.MatchFlags, int)
  def findItems(
      self,
      text: str,
      flags: Qt.MatchFlags,
      column: int = 0,
  ) -> QList[QTreeWidgetItem]:
    """
    Calls Qt's 'QList<QTreeWidgetItem *> QTreeWidget::findItems(const QString
    &text, Qt::MatchFlags flags, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#findItems

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    flags : Qt.MatchFlags
      Passed on as its number.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QList[QTreeWidgetItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTreeWidgetItem *> QTreeWidget::findItems(const QString &text,
    #      Qt::MatchFlags flags, int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget9findItemsERK7QString6QFlagsIN2Qt9MatchFlag'
        'EEi',
        text, flags.value, column,
    )
    from . import QTreeWidgetItem
    return QList[QTreeWidgetItem]._cuteOwning(address)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def itemAbove(
      self,
      item: Optional[QTreeWidgetItem],
  ) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemAbove(const QTreeWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemAbove

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemAbove(const QTreeWidgetItem *item)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget9itemAboveEPK15QTreeWidgetItem',
        self._addressOf(item),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def itemBelow(
      self,
      item: Optional[QTreeWidgetItem],
  ) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemBelow(const QTreeWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemBelow

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemBelow(const QTreeWidgetItem *item)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget9itemBelowEPK15QTreeWidgetItem',
        self._addressOf(item),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def indexFromItem(
      self,
      item: Optional[QTreeWidgetItem],
      column: int = 0,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem
    *item, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#indexFromItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem *item,
    #      int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget13indexFromItemEPK15QTreeWidgetItemi',
        self._addressOf(item), column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def itemFromIndex(self, index: QModelIndex) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemFromIndex(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemFromIndex(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget13itemFromIndexERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTreeWidget::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTreeWidget::supportedDragActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK11QTreeWidget20supportedDragActionsEv',
    ))

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTreeWidget::supportedDropActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTreeWidget::supportedDropActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_own_ZNK11QTreeWidget20supportedDropActionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setColumnCount(self, columns: int) -> None:
    """
    Calls Qt's 'void QTreeWidget::setColumnCount(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setColumnCount

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QTreeWidget::setColumnCount(int columns)
    self.uglySide.call('ritual_ZN11QTreeWidget14setColumnCountEi', columns)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def setHeaderItem(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidget::setHeaderItem(QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setHeaderItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::setHeaderItem(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget13setHeaderItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(QStringList)
  def setHeaderLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QTreeWidget::setHeaderLabels(const QStringList
    &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setHeaderLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTreeWidget::setHeaderLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget15setHeaderLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(str)
  def setHeaderLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QTreeWidget::setHeaderLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setHeaderLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTreeWidget::setHeaderLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setHeaderLabelERK7QString', label,
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def setCurrentItem(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidget::setCurrentItem(QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def setCurrentItem(
      self,
      item: Optional[QTreeWidgetItem],
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.
    """
    #  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int, QItemSelectionModel.SelectionFlags)
  @overload(NoneType, int, QItemSelectionModel.SelectionFlags)
  def setCurrentItem(
      self,
      item: Optional[QTreeWidgetItem],
      column: int,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int
    column, QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi6QFlagsI'
        'N19QItemSelectionModel13SelectionFlagEE',
        self._addressOf(item), column, command.value,
    )

  @overload(QTreeWidgetItem, int, QWidget)
  @overload(QTreeWidgetItem, int, NoneType)
  @overload(NoneType, int, QWidget)
  @overload(NoneType, int, NoneType)
  def setItemWidget(
      self,
      item: Optional[QTreeWidgetItem],
      column: int,
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::setItemWidget(QTreeWidgetItem *item, int
    column, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setItemWidget

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::setItemWidget(QTreeWidgetItem *item, int column,
    #      QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget13setItemWidgetEP15QTreeWidgetItemiP7QWidget',
        self._addressOf(item), column, self._addressOf(widget),
    )

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::setSelectionModel(QItemSelectionModel
    #      *selectionModel)
    ritual = (
        'ritual_ZN11QTreeWidget17setSelectionModelEP19QItemSelectionModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QTreeWidget17setSelectionModelEP19QItemSelectionM'
          'odel')
    self.uglySide.call(ritual, self._addressOf(selectionModel))

  @overload(Qt.DropActions)
  def setSupportedDragActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QTreeWidget::setSupportedDragActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#setSupportedDragActions

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QTreeWidget::setSupportedDragActions(Qt::DropActions actions)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget23setSupportedDragActionsE6QFlagsIN2Qt10Drop'
        'ActionEE',
        actions.value,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QTreeWidget::QTreeWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#QTreeWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTreeWidget::QTreeWidget(QWidget *parent)
    self._noteCreation(QTreeWidget, lambda: Rituals.call(
        'ritual_ZN11QTreeWidgetC1EP7QWidget', self._addressOf(parent),
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

  @overload(int, QTreeWidgetItem)
  @overload(int, NoneType)
  def insertTopLevelItem(
      self,
      index: int,
      item: Optional[QTreeWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::insertTopLevelItem(int index,
    QTreeWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#insertTopLevelItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::insertTopLevelItem(int index, QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget18insertTopLevelItemEiP15QTreeWidgetItem',
        index, self._addressOf(item),
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def addTopLevelItem(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidget::addTopLevelItem(QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#addTopLevelItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::addTopLevelItem(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget15addTopLevelItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(int)
  def takeTopLevelItem(self, index: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::takeTopLevelItem(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#takeTopLevelItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::takeTopLevelItem(int index)
    address = self.uglySide.call(
        'ritual_ZN11QTreeWidget16takeTopLevelItemEi', index,
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(int, QList[QTreeWidgetItem])
  def insertTopLevelItems(
      self,
      index: int,
      items: QList[QTreeWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::insertTopLevelItems(int index, const
    QList<QTreeWidgetItem *> &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#insertTopLevelItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    items : QList[QTreeWidgetItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTreeWidget::insertTopLevelItems(int index, const
    #      QList<QTreeWidgetItem *> &items)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget19insertTopLevelItemsEiRK5QListIP15QTreeWidg'
        'etItemE',
        index, self._valueOf(items),
    )

  @overload(QList[QTreeWidgetItem])
  def addTopLevelItems(self, items: QList[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidget::addTopLevelItems(const
    QList<QTreeWidgetItem *> &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#addTopLevelItems

    Parameters
    ----------

    items : QList[QTreeWidgetItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTreeWidget::addTopLevelItems(const QList<QTreeWidgetItem *>
    #      &items)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget16addTopLevelItemsERK5QListIP15QTreeWidgetIt'
        'emE',
        self._valueOf(items),
    )

  @overload(int, Qt.SortOrder)
  def sortItems(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTreeWidget::sortItems(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#sortItems

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTreeWidget::sortItems(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget9sortItemsEiN2Qt9SortOrderE',
        column, order.value,
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def editItem(
      self,
      item: Optional[QTreeWidgetItem],
      column: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::editItem(QTreeWidgetItem *item, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#editItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QTreeWidget::editItem(QTreeWidgetItem *item, int column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget8editItemEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def openPersistentEditor(
      self,
      item: Optional[QTreeWidgetItem],
      column: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::openPersistentEditor(QTreeWidgetItem *item,
    int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#openPersistentEditor

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QTreeWidget::openPersistentEditor(QTreeWidgetItem *item, int
    #      column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget20openPersistentEditorEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def closePersistentEditor(
      self,
      item: Optional[QTreeWidgetItem],
      column: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::closePersistentEditor(QTreeWidgetItem
    *item, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#closePersistentEditor

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QTreeWidget::closePersistentEditor(QTreeWidgetItem *item, int
    #      column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget21closePersistentEditorEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def removeItemWidget(
      self,
      item: Optional[QTreeWidgetItem],
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::removeItemWidget(QTreeWidgetItem *item, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#removeItemWidget

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.
    """
    #  void QTreeWidget::removeItemWidget(QTreeWidgetItem *item, int column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget16removeItemWidgetEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  @overload(QTreeWidgetItem, QAbstractItemView.ScrollHint)
  @overload(NoneType, QAbstractItemView.ScrollHint)
  def scrollToItem(
      self,
      item: Optional[QTreeWidgetItem],
      hint: QAbstractItemView.ScrollHint = (
          QAbstractItemView.ScrollHint.EnsureVisible),
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::scrollToItem(const QTreeWidgetItem *item,
    QAbstractItemView::ScrollHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#scrollToItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemView.ScrollHint.EnsureVisible.
    """
    #  void QTreeWidget::scrollToItem(const QTreeWidgetItem *item,
    #      QAbstractItemView::ScrollHint hint)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget12scrollToItemEPK15QTreeWidgetItemN17QAbstra'
        'ctItemView10ScrollHintE',
        self._addressOf(item), hint.value,
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def expandItem(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidget::expandItem(const QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#expandItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::expandItem(const QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget10expandItemEPK15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def collapseItem(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidget::collapseItem(const QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#collapseItem

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::collapseItem(const QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget12collapseItemEPK15QTreeWidgetItem',
        self._addressOf(item),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QTreeWidget::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#clear
    """
    #  void QTreeWidget::clear()
    self.uglySide.call('ritual_ZN11QTreeWidget5clearEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QTreeWidget::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTreeWidget::event(QEvent *e)
    return self.uglySide.call(
        'ritual_own_ZN11QTreeWidget5eventEP6QEvent', self._addressOf(e),
    )

  @overload(QTreeWidgetItem, int, QMimeData, Qt.DropAction)
  @overload(QTreeWidgetItem, int, NoneType, Qt.DropAction)
  @overload(NoneType, int, QMimeData, Qt.DropAction)
  @overload(NoneType, int, NoneType, Qt.DropAction)
  def dropMimeData(
      self,
      parent: Optional[QTreeWidgetItem],
      index: int,
      data: Optional[QMimeData],
      action: Qt.DropAction,
  ) -> bool:
    """
    Calls Qt's 'bool QTreeWidget::dropMimeData(QTreeWidgetItem *parent, int
    index, const QMimeData *data, Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#dropMimeData

    Parameters
    ----------

    parent : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.
    """
    #  bool QTreeWidget::dropMimeData(QTreeWidgetItem *parent, int index,
    #      const QMimeData *data, Qt::DropAction action)
    return self.uglySide.call(
        'ritual_own_ZN11QTreeWidget12dropMimeDataEP15QTreeWidgetItemiPK9QMi'
        'meDataN2Qt10DropActionE',
        self._addressOf(parent), index, self._addressOf(data), action.value,
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QTreeWidget::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::dropEvent(QDropEvent *event)
    self.uglySide.call(
        'ritual_own_ZN11QTreeWidget9dropEventEP10QDropEvent',
        self._addressOf(event),
    )
