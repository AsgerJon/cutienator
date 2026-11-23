"""
QTableWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QItemSelectionModel, QList, QStringList
from . import QAbstractItemView, QTableView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QEvent, QMetaObject, QMimeData
  from ..QtCore import QModelIndex, QPoint, QRect
  from ..QtGui import QDropEvent
  from . import QTableWidgetItem, QTableWidgetSelectionRange
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QTableWidgetItem = WAIT['QTableWidgetItem']
  QTableWidgetSelectionRange = WAIT['QTableWidgetSelectionRange']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTableWidget(QTableView):
  """
  The cute side of Qt's QTableWidget: a plain Python object standing in front
  of one C++ QTableWidget.

  It is built on the cute 'QTableView', as Qt's QTableWidget is built on Qt's
  QTableView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTableWidget that has a ritual and that Python can
  call so far, 63 names in all: 'metaObject', 'tr', 'setRowCount',
  'rowCount', 'setColumnCount', 'columnCount', 'row', 'column', 'item',
  'setItem', 'takeItem', 'items', 'indexFromItem', 'itemFromIndex',
  'verticalHeaderItem', 'setVerticalHeaderItem', 'takeVerticalHeaderItem',
  'horizontalHeaderItem', 'setHorizontalHeaderItem',
  'takeHorizontalHeaderItem', 'setVerticalHeaderLabels',
  'setHorizontalHeaderLabels', 'currentRow', 'currentColumn', 'currentItem',
  'setCurrentItem', 'setCurrentCell', 'sortItems', 'setSortingEnabled',
  'isSortingEnabled', 'editItem', 'openPersistentEditor',
  'closePersistentEditor', 'isPersistentEditorOpen', 'cellWidget',
  'setCellWidget', 'removeCellWidget', 'setRangeSelected', 'selectedRanges',
  'selectedItems', 'findItems', 'visualRow', 'visualColumn', 'itemAt',
  'visualItemRect', 'itemPrototype', 'setItemPrototype',
  'supportedDragActions', 'setSupportedDragActions', 'scrollToItem',
  'insertRow', 'insertColumn', 'removeRow', 'removeColumn', 'clear',
  'clearContents', 'event', 'mimeTypes', 'mimeData', 'dropMimeData',
  'supportedDropActions', 'dropEvent', 'setModel'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTableWidget::~QTableWidget()': the destructor: Python never
    removes a C++ QTableWidget.

  What has no ritual
  ------------------

  23 of the 92 functions Qt declares: 15 a signal; 4 takes or gives a type
  that cannot be passed yet; 2 forbidden; 1 a template; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QTableWidget is created at the first use, not by
    'QTableWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTableWidget.
  - Qt tells when it has removed the C++ QTableWidget. Every call on the cute
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
    Calls Qt's 'QString QTableWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#tr

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
    #  QString QTableWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QTableWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTableWidget'

  #  A C++ QTableWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTableWidget'

  #  The functions Qt calls itself that QTableWidget is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'mimeTypes': (
          'QStringList QTableWidget::mimeTypes() const',
      ),
      'mimeData': (
          'QMimeData *QTableWidget::mimeData(const QList<QTableWidgetItem '
          '*> &) const',
      ),
  }

  #  The functions Qt calls itself that QTableWidget is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'dropMimeData': (
          ('_ZN12QTableWidget12dropMimeDataEiiPK9QMimeDataN2Qt10DropActionE',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QMimeData'),
               ('int', 'enum', 'QtCore:Qt.DropAction'),
           )),
      ),
      'supportedDropActions': (
          ('_ZNK12QTableWidget20supportedDropActionsEv',
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
    Calls Qt's 'const QMetaObject *QTableWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTableWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QTableWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QTableWidget::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#rowCount
    """
    #  int QTableWidget::rowCount() const
    return self.uglySide.call('ritual_ZNK12QTableWidget8rowCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QTableWidget::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#columnCount
    """
    #  int QTableWidget::columnCount() const
    return self.uglySide.call('ritual_ZNK12QTableWidget11columnCountEv')

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def row(self, item: Optional[QTableWidgetItem]) -> int:
    """
    Calls Qt's 'int QTableWidget::row(const QTableWidgetItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#row

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTableWidget::row(const QTableWidgetItem *item) const
    return self.uglySide.call(
        'ritual_ZNK12QTableWidget3rowEPK16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def column(self, item: Optional[QTableWidgetItem]) -> int:
    """
    Calls Qt's 'int QTableWidget::column(const QTableWidgetItem *item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#column

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTableWidget::column(const QTableWidgetItem *item) const
    return self.uglySide.call(
        'ritual_ZNK12QTableWidget6columnEPK16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(int, int)
  def item(self, row: int, column: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::item(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#item

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::item(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget4itemEii', row, column,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(QMimeData)
  @overload(NoneType)
  def items(self, data: Optional[QMimeData]) -> QList[QTableWidgetItem]:
    """
    Calls Qt's 'QList<QTableWidgetItem *> QTableWidget::items(const QMimeData
    *data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#items

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QTableWidgetItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTableWidgetItem *> QTableWidget::items(const QMimeData *data)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget5itemsEPK9QMimeData', self._addressOf(data),
    )
    from . import QTableWidgetItem
    return QList[QTableWidgetItem]._cuteOwning(address)

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def indexFromItem(self, item: Optional[QTableWidgetItem]) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTableWidget::indexFromItem(const
    QTableWidgetItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#indexFromItem

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTableWidget::indexFromItem(const QTableWidgetItem *item)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget13indexFromItemEPK16QTableWidgetItem',
        self._addressOf(item),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def itemFromIndex(self, index: QModelIndex) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::itemFromIndex(const
    QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#itemFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::itemFromIndex(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget13itemFromIndexERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  def verticalHeaderItem(self, row: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::verticalHeaderItem(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#verticalHeaderItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::verticalHeaderItem(int row) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget18verticalHeaderItemEi', row,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  def horizontalHeaderItem(self, column: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::horizontalHeaderItem(int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#horizontalHeaderItem

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::horizontalHeaderItem(int column) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget20horizontalHeaderItemEi', column,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  def currentRow(self) -> int:
    """
    Calls Qt's 'int QTableWidget::currentRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#currentRow
    """
    #  int QTableWidget::currentRow() const
    return self.uglySide.call('ritual_ZNK12QTableWidget10currentRowEv')

  def currentColumn(self) -> int:
    """
    Calls Qt's 'int QTableWidget::currentColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#currentColumn
    """
    #  int QTableWidget::currentColumn() const
    return self.uglySide.call('ritual_ZNK12QTableWidget13currentColumnEv')

  def currentItem(self) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#currentItem

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::currentItem() const
    address = self.uglySide.call('ritual_ZNK12QTableWidget11currentItemEv')
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  def isSortingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTableWidget::isSortingEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#isSortingEnabled
    """
    #  bool QTableWidget::isSortingEnabled() const
    return self.uglySide.call('ritual_ZNK12QTableWidget16isSortingEnabledEv')

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def isPersistentEditorOpen(self, item: Optional[QTableWidgetItem]) -> bool:
    """
    Calls Qt's 'bool QTableWidget::isPersistentEditorOpen(QTableWidgetItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#isPersistentEditorOpen

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTableWidget::isPersistentEditorOpen(QTableWidgetItem *item)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QTableWidget22isPersistentEditorOpenEP16QTableWidgetIt'
        'em',
        self._addressOf(item),
    )

  @overload(int, int)
  def cellWidget(self, row: int, column: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QTableWidget::cellWidget(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#cellWidget

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QTableWidget::cellWidget(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget10cellWidgetEii', row, column,
    )
    return QWidget._cuteAt(address)

  def selectedRanges(self) -> QList[QTableWidgetSelectionRange]:
    """
    Calls Qt's 'QList<QTableWidgetSelectionRange>
    QTableWidget::selectedRanges() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#selectedRanges

    Returns
    -------

    QList[QTableWidgetSelectionRange]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTableWidgetSelectionRange> QTableWidget::selectedRanges() const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget14selectedRangesEv',
    )
    from . import QTableWidgetSelectionRange
    return QList[QTableWidgetSelectionRange]._cuteOwning(address)

  def selectedItems(self) -> QList[QTableWidgetItem]:
    """
    Calls Qt's 'QList<QTableWidgetItem *> QTableWidget::selectedItems()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#selectedItems

    Returns
    -------

    QList[QTableWidgetItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTableWidgetItem *> QTableWidget::selectedItems() const
    address = self.uglySide.call('ritual_ZNK12QTableWidget13selectedItemsEv')
    from . import QTableWidgetItem
    return QList[QTableWidgetItem]._cuteOwning(address)

  @overload(str, Qt.MatchFlags)
  def findItems(
      self,
      text: str,
      flags: Qt.MatchFlags,
  ) -> QList[QTableWidgetItem]:
    """
    Calls Qt's 'QList<QTableWidgetItem *> QTableWidget::findItems(const
    QString &text, Qt::MatchFlags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#findItems

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    flags : Qt.MatchFlags
      Passed on as its number.

    Returns
    -------

    QList[QTableWidgetItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTableWidgetItem *> QTableWidget::findItems(const QString &text,
    #      Qt::MatchFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget9findItemsERK7QString6QFlagsIN2Qt9MatchFla'
        'gEE',
        text, flags.value,
    )
    from . import QTableWidgetItem
    return QList[QTableWidgetItem]._cuteOwning(address)

  @overload(int)
  def visualRow(self, logicalRow: int) -> int:
    """
    Calls Qt's 'int QTableWidget::visualRow(int logicalRow) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#visualRow

    Parameters
    ----------

    logicalRow : int
      Passed on as it is.
    """
    #  int QTableWidget::visualRow(int logicalRow) const
    return self.uglySide.call(
        'ritual_ZNK12QTableWidget9visualRowEi', logicalRow,
    )

  @overload(int)
  def visualColumn(self, logicalColumn: int) -> int:
    """
    Calls Qt's 'int QTableWidget::visualColumn(int logicalColumn) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#visualColumn

    Parameters
    ----------

    logicalColumn : int
      Passed on as it is.
    """
    #  int QTableWidget::visualColumn(int logicalColumn) const
    return self.uglySide.call(
        'ritual_ZNK12QTableWidget12visualColumnEi', logicalColumn,
    )

  @overload(QPoint)
  def itemAt(self, p: QPoint) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::itemAt(const QPoint &p)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#itemAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::itemAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget6itemAtERK6QPoint', self._valueOf(p),
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int, int)
  def itemAt(self, x: int, y: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::itemAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#itemAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::itemAt(int x, int y) const
    address = self.uglySide.call('ritual_ZNK12QTableWidget6itemAtEii', x, y)
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def visualItemRect(self, item: Optional[QTableWidgetItem]) -> QRect:
    """
    Calls Qt's 'QRect QTableWidget::visualItemRect(const QTableWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#visualItemRect

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTableWidget::visualItemRect(const QTableWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget14visualItemRectEPK16QTableWidgetItem',
        self._addressOf(item),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def itemPrototype(self) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'const QTableWidgetItem *QTableWidget::itemPrototype() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#itemPrototype

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QTableWidgetItem *QTableWidget::itemPrototype() const
    address = self.uglySide.call('ritual_ZNK12QTableWidget13itemPrototypeEv')
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTableWidget::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTableWidget::supportedDragActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK12QTableWidget20supportedDragActionsEv',
    ))

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QTableWidget::mimeTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTableWidget::mimeTypes() const
    address = self.uglySide.call('ritual_ZNK12QTableWidget9mimeTypesEv')
    return QStringList._cuteOwning(address)

  @overload(QList[QTableWidgetItem])
  def mimeData(self, items: QList[QTableWidgetItem]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QTableWidget::mimeData(const
    QList<QTableWidgetItem *> &items) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#mimeData

    Parameters
    ----------

    items : QList[QTableWidgetItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QTableWidget::mimeData(const QList<QTableWidgetItem *>
    #      &items) const
    address = self.uglySide.call(
        'ritual_ZNK12QTableWidget8mimeDataERK5QListIP16QTableWidgetItemE',
        self._valueOf(items),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTableWidget::supportedDropActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTableWidget::supportedDropActions() const
    ritual = 'ritual_ZNK12QTableWidget20supportedDropActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QTableWidget20supportedDropActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRowCount(self, rows: int) -> None:
    """
    Calls Qt's 'void QTableWidget::setRowCount(int rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setRowCount

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void QTableWidget::setRowCount(int rows)
    self.uglySide.call('ritual_ZN12QTableWidget11setRowCountEi', rows)

  @overload(int)
  def setColumnCount(self, columns: int) -> None:
    """
    Calls Qt's 'void QTableWidget::setColumnCount(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setColumnCount

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QTableWidget::setColumnCount(int columns)
    self.uglySide.call('ritual_ZN12QTableWidget14setColumnCountEi', columns)

  @overload(int, int, QTableWidgetItem)
  @overload(int, int, NoneType)
  def setItem(
      self,
      row: int,
      column: int,
      item: Optional[QTableWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::setItem(int row, int column,
    QTableWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::setItem(int row, int column, QTableWidgetItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget7setItemEiiP16QTableWidgetItem',
        row, column, self._addressOf(item),
    )

  @overload(int, QTableWidgetItem)
  @overload(int, NoneType)
  def setVerticalHeaderItem(
      self,
      row: int,
      item: Optional[QTableWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::setVerticalHeaderItem(int row,
    QTableWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#setVerticalHeaderItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::setVerticalHeaderItem(int row, QTableWidgetItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget21setVerticalHeaderItemEiP16QTableWidgetIte'
        'm',
        row, self._addressOf(item),
    )

  @overload(int, QTableWidgetItem)
  @overload(int, NoneType)
  def setHorizontalHeaderItem(
      self,
      column: int,
      item: Optional[QTableWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::setHorizontalHeaderItem(int column,
    QTableWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#setHorizontalHeaderItem

    Parameters
    ----------

    column : int
      Passed on as it is.

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::setHorizontalHeaderItem(int column,
    #      QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget23setHorizontalHeaderItemEiP16QTableWidgetI'
        'tem',
        column, self._addressOf(item),
    )

  @overload(QStringList)
  def setVerticalHeaderLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QTableWidget::setVerticalHeaderLabels(const QStringList
    &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#setVerticalHeaderLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTableWidget::setVerticalHeaderLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN12QTableWidget23setVerticalHeaderLabelsERK5QListI7QString'
        'E',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setHorizontalHeaderLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QTableWidget::setHorizontalHeaderLabels(const
    QStringList &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#setHorizontalHeaderLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTableWidget::setHorizontalHeaderLabels(const QStringList
    #      &labels)
    self.uglySide.call(
        'ritual_ZN12QTableWidget25setHorizontalHeaderLabelsERK5QListI7QStri'
        'ngE',
        self._valueOf(labels),
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def setCurrentItem(self, item: Optional[QTableWidgetItem]) -> None:
    """
    Calls Qt's 'void QTableWidget::setCurrentItem(QTableWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setCurrentItem

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::setCurrentItem(QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget14setCurrentItemEP16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(QTableWidgetItem, QItemSelectionModel.SelectionFlags)
  @overload(NoneType, QItemSelectionModel.SelectionFlags)
  def setCurrentItem(
      self,
      item: Optional[QTableWidgetItem],
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::setCurrentItem(QTableWidgetItem *item,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setCurrentItem

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QTableWidget::setCurrentItem(QTableWidgetItem *item,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN12QTableWidget14setCurrentItemEP16QTableWidgetItem6QFlags'
        'IN19QItemSelectionModel13SelectionFlagEE',
        self._addressOf(item), command.value,
    )

  @overload(int, int)
  def setCurrentCell(self, row: int, column: int) -> None:
    """
    Calls Qt's 'void QTableWidget::setCurrentCell(int row, int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setCurrentCell

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QTableWidget::setCurrentCell(int row, int column)
    self.uglySide.call(
        'ritual_ZN12QTableWidget14setCurrentCellEii', row, column,
    )

  @overload(int, int, QItemSelectionModel.SelectionFlags)
  def setCurrentCell(
      self,
      row: int,
      column: int,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::setCurrentCell(int row, int column,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setCurrentCell

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QTableWidget::setCurrentCell(int row, int column,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN12QTableWidget14setCurrentCellEii6QFlagsIN19QItemSelectio'
        'nModel13SelectionFlagEE',
        row, column, command.value,
    )

  @overload(bool)
  def setSortingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTableWidget::setSortingEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#setSortingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTableWidget::setSortingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN12QTableWidget17setSortingEnabledEb', enable,
    )

  @overload(int, int, QWidget)
  @overload(int, int, NoneType)
  def setCellWidget(
      self,
      row: int,
      column: int,
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::setCellWidget(int row, int column, QWidget
    *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setCellWidget

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::setCellWidget(int row, int column, QWidget *widget)
    self.uglySide.call(
        'ritual_ZN12QTableWidget13setCellWidgetEiiP7QWidget',
        row, column, self._addressOf(widget),
    )

  @overload(QTableWidgetSelectionRange, bool)
  def setRangeSelected(
      self,
      range: QTableWidgetSelectionRange,
      select: bool,
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::setRangeSelected(const
    QTableWidgetSelectionRange &range, bool select)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setRangeSelected

    Parameters
    ----------

    range : QTableWidgetSelectionRange
      Passed on as a value: Qt reads the C++ QTableWidgetSelectionRange,
      which stays Python's own.

    select : bool
      Passed on as it is.
    """
    #  void QTableWidget::setRangeSelected(const QTableWidgetSelectionRange
    #      &range, bool select)
    self.uglySide.call(
        'ritual_ZN12QTableWidget16setRangeSelectedERK26QTableWidgetSelectio'
        'nRangeb',
        self._valueOf(range), select,
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def setItemPrototype(self, item: Optional[QTableWidgetItem]) -> None:
    """
    Calls Qt's 'void QTableWidget::setItemPrototype(const QTableWidgetItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setItemPrototype

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::setItemPrototype(const QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget16setItemPrototypeEPK16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(Qt.DropActions)
  def setSupportedDragActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QTableWidget::setSupportedDragActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#setSupportedDragActions

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QTableWidget::setSupportedDragActions(Qt::DropActions actions)
    self.uglySide.call(
        'ritual_ZN12QTableWidget23setSupportedDragActionsE6QFlagsIN2Qt10Dro'
        'pActionEE',
        actions.value,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QTableWidget::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::setModel(QAbstractItemModel *model)
    ritual = 'ritual_ZN12QTableWidget8setModelEP18QAbstractItemModel'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTableWidget8setModelEP18QAbstractItemModel'
    self.uglySide.call(ritual, self._addressOf(model))

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
    Notes what was given, for Qt's 'QTableWidget::QTableWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#QTableWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTableWidget::QTableWidget(QWidget *parent)
    self._noteCreation(QTableWidget, lambda: Rituals.call(
        'ritual_ZN12QTableWidgetC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(int, int)
  @overload(int, int, QWidget)
  @overload(int, int, NoneType)
  def __init__(
      self,
      rows: int,
      columns: int,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTableWidget::QTableWidget(int rows, int
    columns, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#QTableWidget

    Parameters
    ----------

    rows : int
      Passed on as it is.

    columns : int
      Passed on as it is.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTableWidget::QTableWidget(int rows, int columns, QWidget *parent)
    self._noteCreation(QTableWidget, lambda: Rituals.call(
        'ritual_ZN12QTableWidgetC1EiiP7QWidget',
        rows, columns, self._addressOf(parent),
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

  @overload(int, int)
  def takeItem(self, row: int, column: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::takeItem(int row, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#takeItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::takeItem(int row, int column)
    address = self.uglySide.call(
        'ritual_ZN12QTableWidget8takeItemEii', row, column,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  def takeVerticalHeaderItem(self, row: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::takeVerticalHeaderItem(int
    row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#takeVerticalHeaderItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::takeVerticalHeaderItem(int row)
    address = self.uglySide.call(
        'ritual_ZN12QTableWidget22takeVerticalHeaderItemEi', row,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  def takeHorizontalHeaderItem(
      self,
      column: int,
  ) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidget::takeHorizontalHeaderItem(int
    column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#takeHorizontalHeaderItem

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidget::takeHorizontalHeaderItem(int column)
    address = self.uglySide.call(
        'ritual_ZN12QTableWidget24takeHorizontalHeaderItemEi', column,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sortItems(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::sortItems(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#sortItems

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QTableWidget::sortItems(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN12QTableWidget9sortItemsEiN2Qt9SortOrderE',
        column, order.value,
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def editItem(self, item: Optional[QTableWidgetItem]) -> None:
    """
    Calls Qt's 'void QTableWidget::editItem(QTableWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#editItem

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::editItem(QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget8editItemEP16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def openPersistentEditor(self, item: Optional[QTableWidgetItem]) -> None:
    """
    Calls Qt's 'void QTableWidget::openPersistentEditor(QTableWidgetItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#openPersistentEditor

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::openPersistentEditor(QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget20openPersistentEditorEP16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def closePersistentEditor(self, item: Optional[QTableWidgetItem]) -> None:
    """
    Calls Qt's 'void QTableWidget::closePersistentEditor(QTableWidgetItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidget.html#closePersistentEditor

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::closePersistentEditor(QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN12QTableWidget21closePersistentEditorEP16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(int, int)
  def removeCellWidget(self, row: int, column: int) -> None:
    """
    Calls Qt's 'void QTableWidget::removeCellWidget(int row, int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#removeCellWidget

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QTableWidget::removeCellWidget(int row, int column)
    self.uglySide.call(
        'ritual_ZN12QTableWidget16removeCellWidgetEii', row, column,
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  @overload(QTableWidgetItem, QAbstractItemView.ScrollHint)
  @overload(NoneType, QAbstractItemView.ScrollHint)
  def scrollToItem(
      self,
      item: Optional[QTableWidgetItem],
      hint: QAbstractItemView.ScrollHint = (
          QAbstractItemView.ScrollHint.EnsureVisible),
  ) -> None:
    """
    Calls Qt's 'void QTableWidget::scrollToItem(const QTableWidgetItem *item,
    QAbstractItemView::ScrollHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#scrollToItem

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemView.ScrollHint.EnsureVisible.
    """
    #  void QTableWidget::scrollToItem(const QTableWidgetItem *item,
    #      QAbstractItemView::ScrollHint hint)
    self.uglySide.call(
        'ritual_ZN12QTableWidget12scrollToItemEPK16QTableWidgetItemN17QAbst'
        'ractItemView10ScrollHintE',
        self._addressOf(item), hint.value,
    )

  @overload(int)
  def insertRow(self, row: int) -> None:
    """
    Calls Qt's 'void QTableWidget::insertRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QTableWidget::insertRow(int row)
    self.uglySide.call('ritual_ZN12QTableWidget9insertRowEi', row)

  @overload(int)
  def insertColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QTableWidget::insertColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#insertColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTableWidget::insertColumn(int column)
    self.uglySide.call('ritual_ZN12QTableWidget12insertColumnEi', column)

  @overload(int)
  def removeRow(self, row: int) -> None:
    """
    Calls Qt's 'void QTableWidget::removeRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#removeRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QTableWidget::removeRow(int row)
    self.uglySide.call('ritual_ZN12QTableWidget9removeRowEi', row)

  @overload(int)
  def removeColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QTableWidget::removeColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#removeColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTableWidget::removeColumn(int column)
    self.uglySide.call('ritual_ZN12QTableWidget12removeColumnEi', column)

  def clear(self) -> None:
    """
    Calls Qt's 'void QTableWidget::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#clear
    """
    #  void QTableWidget::clear()
    self.uglySide.call('ritual_ZN12QTableWidget5clearEv')

  def clearContents(self) -> None:
    """
    Calls Qt's 'void QTableWidget::clearContents()'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#clearContents
    """
    #  void QTableWidget::clearContents()
    self.uglySide.call('ritual_ZN12QTableWidget13clearContentsEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QTableWidget::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTableWidget::event(QEvent *e)
    ritual = 'ritual_ZN12QTableWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTableWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(int, int, QMimeData, Qt.DropAction)
  @overload(int, int, NoneType, Qt.DropAction)
  def dropMimeData(
      self,
      row: int,
      column: int,
      data: Optional[QMimeData],
      action: Qt.DropAction,
  ) -> bool:
    """
    Calls Qt's 'bool QTableWidget::dropMimeData(int row, int column, const
    QMimeData *data, Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#dropMimeData

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.
    """
    #  bool QTableWidget::dropMimeData(int row, int column, const QMimeData
    #      *data, Qt::DropAction action)
    ritual = (
        'ritual_ZN12QTableWidget12dropMimeDataEiiPK9QMimeDataN2Qt10DropActi'
        'onE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QTableWidget12dropMimeDataEiiPK9QMimeDataN2Qt10Dr'
          'opActionE')
    return self.uglySide.call(
        ritual, row, column, self._addressOf(data), action.value,
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QTableWidget::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidget.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableWidget::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN12QTableWidget9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTableWidget9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))
