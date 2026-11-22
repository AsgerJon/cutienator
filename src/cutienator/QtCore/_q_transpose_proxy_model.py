"""
QTransposeProxyModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtransposeproxymodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel, QAbstractProxyModel, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject, QModelIndex, QSize, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTransposeProxyModel(QAbstractProxyModel):
  """
  The cute side of Qt's QTransposeProxyModel: a plain Python object standing
  in front of one C++ QTransposeProxyModel.

  It is built on the cute 'QAbstractProxyModel', as Qt's QTransposeProxyModel
  is built on Qt's QAbstractProxyModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTransposeProxyModel that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'setSourceModel', 'rowCount', 'columnCount', 'headerData', 'setHeaderData',
  'span', 'mapFromSource', 'mapToSource', 'parent', 'index', 'insertRows',
  'removeRows', 'moveRows', 'insertColumns', 'removeColumns', 'moveColumns',
  'sort'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTransposeProxyModel::~QTransposeProxyModel()': the destructor:
    Python never removes a C++ QTransposeProxyModel.

  What has no ritual
  ------------------

  11 of the 32 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QTransposeProxyModel is created at the first use, not by
    'QTransposeProxyModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTransposeProxyModel.
  - Qt tells when it has removed the C++ QTransposeProxyModel. Every call on
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
    Calls Qt's 'QString QTransposeProxyModel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransposeproxymodel.html#tr

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
    #  QString QTransposeProxyModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QTransposeProxyModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTransposeProxyModel'

  #  A C++ QTransposeProxyModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTransposeProxyModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTransposeProxyModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTransposeProxyModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QTransposeProxyModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QTransposeProxyModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransposeproxymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QTransposeProxyModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK20QTransposeProxyModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QTransposeProxyModel8rowCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QTransposeProxyModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QTransposeProxyModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK20QTransposeProxyModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QTransposeProxyModel11columnCountERK11QModelInde'
          'x')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(int, Qt.Orientation)
  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QTransposeProxyModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#headerData

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
    #  QVariant QTransposeProxyModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = (
        'ritual_ZNK20QTransposeProxyModel10headerDataEiN2Qt11OrientationEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QTransposeProxyModel10headerDataEiN2Qt11Orientat'
          'ionEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def span(self, index: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QTransposeProxyModel::span(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransposeproxymodel.html#span

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
    #  QSize QTransposeProxyModel::span(const QModelIndex &index) const
    ritual = 'ritual_ZNK20QTransposeProxyModel4spanERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QTransposeProxyModel4spanERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QSize
    return QSize._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTransposeProxyModel::mapFromSource(const
    QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#mapFromSource

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
    #  QModelIndex QTransposeProxyModel::mapFromSource(const QModelIndex
    #      &sourceIndex) const
    ritual = (
        'ritual_ZNK20QTransposeProxyModel13mapFromSourceERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QTransposeProxyModel13mapFromSourceERK11QModelIn'
          'dex')
    address = self.uglySide.call(ritual, self._valueOf(sourceIndex))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTransposeProxyModel::mapToSource(const
    QModelIndex &proxyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#mapToSource

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
    #  QModelIndex QTransposeProxyModel::mapToSource(const QModelIndex
    #      &proxyIndex) const
    ritual = 'ritual_ZNK20QTransposeProxyModel11mapToSourceERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QTransposeProxyModel11mapToSourceERK11QModelInde'
          'x')
    address = self.uglySide.call(ritual, self._valueOf(proxyIndex))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTransposeProxyModel::parent(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransposeproxymodel.html#parent

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
    #  QModelIndex QTransposeProxyModel::parent(const QModelIndex &index)
    #      const
    ritual = 'ritual_ZNK20QTransposeProxyModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QTransposeProxyModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTransposeProxyModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransposeproxymodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTransposeProxyModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK20QTransposeProxyModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QTransposeProxyModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setSourceModel(
      self,
      newSourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void QTransposeProxyModel::setSourceModel(QAbstractItemModel
    *newSourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#setSourceModel

    Parameters
    ----------

    newSourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTransposeProxyModel::setSourceModel(QAbstractItemModel
    #      *newSourceModel)
    ritual = (
        'ritual_ZN20QTransposeProxyModel14setSourceModelEP18QAbstractItemMo'
        'del')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel14setSourceModelEP18QAbstract'
          'ItemModel')
    self.uglySide.call(ritual, self._addressOf(newSourceModel))

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
    Calls Qt's 'bool QTransposeProxyModel::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#setHeaderData

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
    #  bool QTransposeProxyModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    ritual = (
        'ritual_ZN20QTransposeProxyModel13setHeaderDataEiN2Qt11OrientationE'
        'RK8QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel13setHeaderDataEiN2Qt11Orient'
          'ationERK8QVarianti')
    return self.uglySide.call(
        ritual, section, orientation.value, self._valueOf(value), role,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QTransposeProxyModel::QTransposeProxyModel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#QTransposeProxyModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTransposeProxyModel::QTransposeProxyModel(QObject *parent)
    self._noteCreation(QTransposeProxyModel, lambda: Rituals.call(
        'ritual_ZN20QTransposeProxyModelC1EP7QObject',
        self._addressOf(parent),
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
  @overload(int, int, QModelIndex)
  def insertRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QTransposeProxyModel::insertRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QTransposeProxyModel::insertRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN20QTransposeProxyModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel10insertRowsEiiRK11QModelInde'
          'x')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QTransposeProxyModel::removeRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#removeRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QTransposeProxyModel::removeRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN20QTransposeProxyModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel10removeRowsEiiRK11QModelInde'
          'x')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveRows(
      self,
      sourceParent: QModelIndex,
      sourceRow: int,
      count: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QTransposeProxyModel::moveRows(const QModelIndex
    &sourceParent, int sourceRow, int count, const QModelIndex
    &destinationParent, int destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransposeproxymodel.html#moveRows

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRow : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QTransposeProxyModel::moveRows(const QModelIndex &sourceParent,
    #      int sourceRow, int count, const QModelIndex &destinationParent,
    #      int destinationChild)
    ritual = 'ritual_ZN20QTransposeProxyModel8moveRowsERK11QModelIndexiiS2_i'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel8moveRowsERK11QModelIndexiiS2'
          '_i')
    return self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceRow, count,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QTransposeProxyModel::insertColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QTransposeProxyModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN20QTransposeProxyModel13insertColumnsEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel13insertColumnsEiiRK11QModelI'
          'ndex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QTransposeProxyModel::removeColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#removeColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QTransposeProxyModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN20QTransposeProxyModel13removeColumnsEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel13removeColumnsEiiRK11QModelI'
          'ndex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveColumns(
      self,
      sourceParent: QModelIndex,
      sourceColumn: int,
      count: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QTransposeProxyModel::moveColumns(const QModelIndex
    &sourceParent, int sourceColumn, int count, const QModelIndex
    &destinationParent, int destinationChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodel.html#moveColumns

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceColumn : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QTransposeProxyModel::moveColumns(const QModelIndex
    #      &sourceParent, int sourceColumn, int count, const QModelIndex
    #      &destinationParent, int destinationChild)
    ritual = (
        'ritual_ZN20QTransposeProxyModel11moveColumnsERK11QModelIndexiiS2_i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QTransposeProxyModel11moveColumnsERK11QModelIndex'
          'iiS2_i')
    return self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceColumn, count,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QTransposeProxyModel::sort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransposeproxymodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QTransposeProxyModel::sort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN20QTransposeProxyModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QTransposeProxyModel4sortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)
