"""
QAbstractProxyModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractproxymodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QItemSelection, QMetaObject, QMimeData, QModelIndex, QSize
  from . import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelection = WAIT['QItemSelection']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractProxyModel(QAbstractItemModel):
  """
  The cute side of Qt's QAbstractProxyModel: a plain Python object standing
  in front of one C++ QAbstractProxyModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QAbstractProxyModel
  is built on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractProxyModel that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'tr',
  'setSourceModel', 'sourceModel', 'mapToSource', 'mapFromSource',
  'mapSelectionToSource', 'mapSelectionFromSource', 'submit', 'revert',
  'data', 'headerData', 'flags', 'setData', 'setHeaderData', 'clearItemData',
  'buddy', 'canFetchMore', 'fetchMore', 'sort', 'span', 'hasChildren',
  'sibling', 'canDropMimeData', 'dropMimeData', 'supportedDragActions',
  'supportedDropActions'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractProxyModel::~QAbstractProxyModel()': the destructor:
    Python never removes a C++ QAbstractProxyModel.

  What has no ritual
  ------------------

  18 of the 46 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 3 private; 2 protected; 2 forbidden; 1 a template; 1 the class
  is abstract, so C++ cannot make one; 1 a signal.

  What to expect
  --------------

  - The C++ QAbstractProxyModel is created at the first use, not by
    'QAbstractProxyModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractProxyModel.
  - Qt tells when it has removed the C++ QAbstractProxyModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QAbstractProxyModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#tr

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
    #  QString QAbstractProxyModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QAbstractProxyModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractProxyModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractProxyModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractProxyModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QAbstractProxyModel::sourceModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#sourceModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QAbstractProxyModel::sourceModel() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel11sourceModelEv',
    )
    return QAbstractItemModel._cuteAt(address)

  @overload(QModelIndex)
  def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractProxyModel::mapToSource(const
    QModelIndex &proxyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#mapToSource

    Parameters
    ----------

    proxyIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractProxyModel::mapToSource(const QModelIndex
    #      &proxyIndex) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex',
        self._valueOf(proxyIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractProxyModel::mapFromSource(const
    QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#mapFromSource

    Parameters
    ----------

    sourceIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractProxyModel::mapFromSource(const QModelIndex
    #      &sourceIndex) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex',
        self._valueOf(sourceIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionToSource(
      self,
      selection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QAbstractProxyModel::mapSelectionToSource(const QItemSelection
    &selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#mapSelectionToSource

    Parameters
    ----------

    selection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection QAbstractProxyModel::mapSelectionToSource(const
    #      QItemSelection &selection) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSel'
        'ection',
        self._valueOf(selection),
    )
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionFromSource(
      self,
      selection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QAbstractProxyModel::mapSelectionFromSource(const QItemSelection
    &selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#mapSelectionFromSource

    Parameters
    ----------

    selection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection QAbstractProxyModel::mapSelectionFromSource(const
    #      QItemSelection &selection) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemS'
        'election',
        self._valueOf(selection),
    )
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, proxyIndex: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractProxyModel::data(const QModelIndex
    &proxyIndex, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#data

    Parameters
    ----------

    proxyIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractProxyModel::data(const QModelIndex &proxyIndex, int
    #      role) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel4dataERK11QModelIndexi',
        self._valueOf(proxyIndex), role,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, Qt.Orientation)
  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractProxyModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#headerData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractProxyModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel10headerDataEiN2Qt11OrientationEi',
        section, orientation.value, role,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#flags

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index)
    #      const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel5flagsERK11QModelIndex',
        self._valueOf(index),
    ))

  @overload(QModelIndex)
  def buddy(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractProxyModel::buddy(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#buddy

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel5buddyERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def canFetchMore(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::canFetchMore(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#canFetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel12canFetchMoreERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  def span(self, index: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QAbstractProxyModel::span(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#span

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractProxyModel::span(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel4spanERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QSize
    return QSize._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractProxyModel::hasChildren(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel11hasChildrenERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractProxyModel::sibling(int row, int column,
    const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#sibling

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractProxyModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel7siblingEiiRK11QModelIndex',
        row, column, self._valueOf(idx),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def canDropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::canDropMimeData(const QMimeData
    *data, Qt::DropAction action, int row, int column, const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#canDropMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractProxyModel::canDropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent) const
    return self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel15canDropMimeDataEPK9QMimeDataN2Qt1'
        '0DropActionEiiRK11QModelIndex',
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QAbstractProxyModel::supportedDragActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel20supportedDragActionsEv',
    ))

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QAbstractProxyModel::supportedDropActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK19QAbstractProxyModel20supportedDropActionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setSourceModel(
      self,
      sourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void QAbstractProxyModel::setSourceModel(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#setSourceModel

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractProxyModel::setSourceModel(QAbstractItemModel
    #      *sourceModel)
    self.uglySide.call(
        'ritual_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemMod'
        'el',
        self._addressOf(sourceModel),
    )

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::setData(const QModelIndex &index,
    const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QAbstractProxyModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    return self.uglySide.call(
        'ritual_ZN19QAbstractProxyModel7setDataERK11QModelIndexRK8QVarianti',
        self._valueOf(index), self._valueOf(value), role,
    )

  @overload(int, Qt.Orientation, QVariant)
  @overload(int, Qt.Orientation, QVariant, int)
  def setHeaderData(
      self,
      section: int,
      orientation: Qt.Orientation,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#setHeaderData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QAbstractProxyModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    return self.uglySide.call(
        'ritual_ZN19QAbstractProxyModel13setHeaderDataEiN2Qt11OrientationER'
        'K8QVarianti',
        section, orientation.value, self._valueOf(value), role,
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

  def submit(self) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::submit()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#submit
    """
    #  bool QAbstractProxyModel::submit()
    return self.uglySide.call('ritual_ZN19QAbstractProxyModel6submitEv')

  def revert(self) -> None:
    """
    Calls Qt's 'void QAbstractProxyModel::revert()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#revert
    """
    #  void QAbstractProxyModel::revert()
    self.uglySide.call('ritual_ZN19QAbstractProxyModel6revertEv')

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::clearItemData(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN19QAbstractProxyModel13clearItemDataERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def fetchMore(self, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractProxyModel::fetchMore(const QModelIndex
    &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#fetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
    self.uglySide.call(
        'ritual_ZN19QAbstractProxyModel9fetchMoreERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QAbstractProxyModel::sort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractproxymodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QAbstractProxyModel::sort(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN19QAbstractProxyModel4sortEiN2Qt9SortOrderE',
        column, order.value,
    )

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def dropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodel.html#dropMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    return self.uglySide.call(
        'ritual_ZN19QAbstractProxyModel12dropMimeDataEPK9QMimeDataN2Qt10Dro'
        'pActionEiiRK11QModelIndex',
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )
