"""
QIdentityProxyModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qidentityproxymodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel, QAbstractProxyModel, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QItemSelection, QMetaObject, QMimeData, QModelIndex, QVariant
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


class QIdentityProxyModel(QAbstractProxyModel):
  """
  The cute side of Qt's QIdentityProxyModel: a plain Python object standing
  in front of one C++ QIdentityProxyModel.

  It is built on the cute 'QAbstractProxyModel', as Qt's QIdentityProxyModel
  is built on Qt's QAbstractProxyModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIdentityProxyModel that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'columnCount',
  'index', 'mapFromSource', 'mapToSource', 'parent', 'rowCount',
  'headerData', 'dropMimeData', 'sibling', 'mapSelectionFromSource',
  'mapSelectionToSource', 'match', 'setSourceModel', 'insertColumns',
  'insertRows', 'removeColumns', 'removeRows', 'moveRows', 'moveColumns',
  'handleSourceLayoutChanges', 'handleSourceDataChanges',
  'setHandleSourceLayoutChanges', 'setHandleSourceDataChanges'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIdentityProxyModel::~QIdentityProxyModel()': the destructor:
    Python never removes a C++ QIdentityProxyModel.

  What has no ritual
  ------------------

  9 of the 36 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QIdentityProxyModel is created at the first use, not by
    'QIdentityProxyModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIdentityProxyModel.
  - Qt tells when it has removed the C++ QIdentityProxyModel. Every call on
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
    Calls Qt's 'QString QIdentityProxyModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qidentityproxymodel.html#tr

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
    #  QString QIdentityProxyModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QIdentityProxyModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIdentityProxyModel'

  #  A C++ QIdentityProxyModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIdentityProxyModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QIdentityProxyModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QIdentityProxyModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QIdentityProxyModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QIdentityProxyModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QIdentityProxyModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK19QIdentityProxyModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QIdentityProxyModel11columnCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QIdentityProxyModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qidentityproxymodel.html#index

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
    #  QModelIndex QIdentityProxyModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK19QIdentityProxyModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QIdentityProxyModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QIdentityProxyModel::mapFromSource(const
    QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#mapFromSource

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
    #  QModelIndex QIdentityProxyModel::mapFromSource(const QModelIndex
    #      &sourceIndex) const
    ritual = 'ritual_ZNK19QIdentityProxyModel13mapFromSourceERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QIdentityProxyModel13mapFromSourceERK11QModelInd'
          'ex')
    address = self.uglySide.call(ritual, self._valueOf(sourceIndex))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QIdentityProxyModel::mapToSource(const
    QModelIndex &proxyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#mapToSource

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
    #  QModelIndex QIdentityProxyModel::mapToSource(const QModelIndex
    #      &proxyIndex) const
    ritual = 'ritual_ZNK19QIdentityProxyModel11mapToSourceERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QIdentityProxyModel11mapToSourceERK11QModelIndex')
    address = self.uglySide.call(ritual, self._valueOf(proxyIndex))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QIdentityProxyModel::parent(const QModelIndex
    &child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qidentityproxymodel.html#parent

    Parameters
    ----------

    child : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QIdentityProxyModel::parent(const QModelIndex &child)
    #      const
    ritual = 'ritual_ZNK19QIdentityProxyModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QIdentityProxyModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(child))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QIdentityProxyModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qidentityproxymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QIdentityProxyModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK19QIdentityProxyModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QIdentityProxyModel8rowCountERK11QModelIndex'
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
    Calls Qt's 'QVariant QIdentityProxyModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#headerData

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
    #  QVariant QIdentityProxyModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = (
        'ritual_ZNK19QIdentityProxyModel10headerDataEiN2Qt11OrientationEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QIdentityProxyModel10headerDataEiN2Qt11Orientati'
          'onEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QIdentityProxyModel::sibling(int row, int column,
    const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qidentityproxymodel.html#sibling

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
    #  QModelIndex QIdentityProxyModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    ritual = 'ritual_ZNK19QIdentityProxyModel7siblingEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QIdentityProxyModel7siblingEiiRK11QModelIndex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(idx))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionFromSource(
      self,
      selection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QIdentityProxyModel::mapSelectionFromSource(const QItemSelection
    &selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#mapSelectionFromSource

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
    #  QItemSelection QIdentityProxyModel::mapSelectionFromSource(const
    #      QItemSelection &selection) const
    ritual = (
        'ritual_ZNK19QIdentityProxyModel22mapSelectionFromSourceERK14QItemS'
        'election')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QIdentityProxyModel22mapSelectionFromSourceERK14'
          'QItemSelection')
    address = self.uglySide.call(ritual, self._valueOf(selection))
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionToSource(
      self,
      selection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QIdentityProxyModel::mapSelectionToSource(const QItemSelection
    &selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#mapSelectionToSource

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
    #  QItemSelection QIdentityProxyModel::mapSelectionToSource(const
    #      QItemSelection &selection) const
    ritual = (
        'ritual_ZNK19QIdentityProxyModel20mapSelectionToSourceERK14QItemSel'
        'ection')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QIdentityProxyModel20mapSelectionToSourceERK14QI'
          'temSelection')
    address = self.uglySide.call(ritual, self._valueOf(selection))
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QModelIndex, int, QVariant)
  @overload(QModelIndex, int, QVariant, int)
  @overload(QModelIndex, int, QVariant, int, Qt.MatchFlags)
  def match(
      self,
      start: QModelIndex,
      role: int,
      value: QVariant,
      hits: int = 1,
      flags: Qt.MatchFlags = (
          Qt.MatchFlags.MatchStartsWith | Qt.MatchFlags.MatchWrap),
  ) -> QList[QModelIndex]:
    """
    Calls Qt's 'QModelIndexList QIdentityProxyModel::match(const QModelIndex
    &start, int role, const QVariant &value, int hits, Qt::MatchFlags flags)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qidentityproxymodel.html#match

    Parameters
    ----------

    start : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    hits : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    flags : Qt.MatchFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MatchFlags.MatchStartsWith | Qt.MatchFlags.MatchWrap.

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QModelIndexList QIdentityProxyModel::match(const QModelIndex &start,
    #      int role, const QVariant &value, int hits, Qt::MatchFlags flags)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QIdentityProxyModel5matchERK11QModelIndexiRK8QVarianti'
        '6QFlagsIN2Qt9MatchFlagEE',
        self._valueOf(start), role, self._valueOf(value), hits, flags.value,
    )
    from . import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  def handleSourceLayoutChanges(self) -> bool:
    """
    Calls Qt's 'bool QIdentityProxyModel::handleSourceLayoutChanges() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#handleSourceLayoutChanges
    """
    #  bool QIdentityProxyModel::handleSourceLayoutChanges() const
    return self.uglySide.call(
        'ritual_ZNK19QIdentityProxyModel25handleSourceLayoutChangesEv',
    )

  def handleSourceDataChanges(self) -> bool:
    """
    Calls Qt's 'bool QIdentityProxyModel::handleSourceDataChanges() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#handleSourceDataChanges
    """
    #  bool QIdentityProxyModel::handleSourceDataChanges() const
    return self.uglySide.call(
        'ritual_ZNK19QIdentityProxyModel23handleSourceDataChangesEv',
    )

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
    Calls Qt's 'void QIdentityProxyModel::setSourceModel(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#setSourceModel

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QIdentityProxyModel::setSourceModel(QAbstractItemModel
    #      *sourceModel)
    ritual = (
        'ritual_ZN19QIdentityProxyModel14setSourceModelEP18QAbstractItemMod'
        'el')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel14setSourceModelEP18QAbstractI'
          'temModel')
    self.uglySide.call(ritual, self._addressOf(sourceModel))

  @overload(bool)
  def setHandleSourceLayoutChanges(self, a0: bool) -> None:
    """
    Calls Qt's 'void QIdentityProxyModel::setHandleSourceLayoutChanges(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QIdentityProxyModel::setHandleSourceLayoutChanges(bool a0)
    self.uglySide.call(
        'ritual_ZN19QIdentityProxyModel28setHandleSourceLayoutChangesEb', a0,
    )

  @overload(bool)
  def setHandleSourceDataChanges(self, a0: bool) -> None:
    """
    Calls Qt's 'void QIdentityProxyModel::setHandleSourceDataChanges(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QIdentityProxyModel::setHandleSourceDataChanges(bool a0)
    self.uglySide.call(
        'ritual_ZN19QIdentityProxyModel26setHandleSourceDataChangesEb', a0,
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
    'QIdentityProxyModel::QIdentityProxyModel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#QIdentityProxyModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QIdentityProxyModel::QIdentityProxyModel(QObject *parent)
    self._noteCreation(QIdentityProxyModel, lambda: Rituals.call(
        'ritual_ZN19QIdentityProxyModelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'bool QIdentityProxyModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#dropMimeData

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
    #  bool QIdentityProxyModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    ritual = (
        'ritual_ZN19QIdentityProxyModel12dropMimeDataEPK9QMimeDataN2Qt10Dro'
        'pActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel12dropMimeDataEPK9QMimeDataN2Q'
          't10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
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
    Calls Qt's 'bool QIdentityProxyModel::insertColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#insertColumns

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
    #  bool QIdentityProxyModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN19QIdentityProxyModel13insertColumnsEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel13insertColumnsEiiRK11QModelIn'
          'dex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QIdentityProxyModel::insertRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#insertRows

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
    #  bool QIdentityProxyModel::insertRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN19QIdentityProxyModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel10insertRowsEiiRK11QModelIndex')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QIdentityProxyModel::removeColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#removeColumns

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
    #  bool QIdentityProxyModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN19QIdentityProxyModel13removeColumnsEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel13removeColumnsEiiRK11QModelIn'
          'dex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QIdentityProxyModel::removeRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#removeRows

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
    #  bool QIdentityProxyModel::removeRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN19QIdentityProxyModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel10removeRowsEiiRK11QModelIndex')
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
    Calls Qt's 'bool QIdentityProxyModel::moveRows(const QModelIndex
    &sourceParent, int sourceRow, int count, const QModelIndex
    &destinationParent, int destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qidentityproxymodel.html#moveRows

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
    #  bool QIdentityProxyModel::moveRows(const QModelIndex &sourceParent,
    #      int sourceRow, int count, const QModelIndex &destinationParent,
    #      int destinationChild)
    ritual = 'ritual_ZN19QIdentityProxyModel8moveRowsERK11QModelIndexiiS2_i'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel8moveRowsERK11QModelIndexiiS2_'
          'i')
    return self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceRow, count,
        self._valueOf(destinationParent), destinationChild,
    )

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
    Calls Qt's 'bool QIdentityProxyModel::moveColumns(const QModelIndex
    &sourceParent, int sourceColumn, int count, const QModelIndex
    &destinationParent, int destinationChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodel.html#moveColumns

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
    #  bool QIdentityProxyModel::moveColumns(const QModelIndex &sourceParent,
    #      int sourceColumn, int count, const QModelIndex &destinationParent,
    #      int destinationChild)
    ritual = (
        'ritual_ZN19QIdentityProxyModel11moveColumnsERK11QModelIndexiiS2_i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QIdentityProxyModel11moveColumnsERK11QModelIndexi'
          'iS2_i')
    return self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceColumn, count,
        self._valueOf(destinationParent), destinationChild,
    )
