"""
QHeaderDataProxyModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QHeaderDataProxyModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QHash, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHeaderDataProxyModel(QAbstractItemModel):
  """
  The cute side of Qt's QHeaderDataProxyModel: a plain Python object standing
  in front of one C++ QHeaderDataProxyModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QHeaderDataProxyModel
  is built on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHeaderDataProxyModel that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr',
  'setSourceModel', 'index', 'parent', 'sibling', 'rowCount', 'columnCount',
  'data', 'setData', 'hasChildren', 'roleNames', 'variantValue',
  'orientation', 'setOrientation', 'connectToModel', 'disconnectFromModel'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHeaderDataProxyModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHeaderDataProxyModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHeaderDataProxyModel::~QHeaderDataProxyModel()': the destructor:
    Python never removes a C++ QHeaderDataProxyModel.
  - Qt's 'QPointer<QAbstractItemModel> QHeaderDataProxyModel::sourceModel()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QHeaderDataProxyModel is created at the first use, not by
    'QHeaderDataProxyModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHeaderDataProxyModel.
  - Qt tells when it has removed the C++ QHeaderDataProxyModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHeaderDataProxyModel that has no cute function yet,
    'sourceModel', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QHeaderDataProxyModel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderdataproxymodel.html#tr

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
    #  QString QHeaderDataProxyModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QHeaderDataProxyModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHeaderDataProxyModel'

  #  A C++ QHeaderDataProxyModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHeaderDataProxyModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHeaderDataProxyModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHeaderDataProxyModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QHeaderDataProxyModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QHeaderDataProxyModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderdataproxymodel.html#index

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
    #  QModelIndex QHeaderDataProxyModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK21QHeaderDataProxyModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QHeaderDataProxyModel5indexEiiRK11QModelIndex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QHeaderDataProxyModel::parent(const QModelIndex
    &child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderdataproxymodel.html#parent

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
    #  QModelIndex QHeaderDataProxyModel::parent(const QModelIndex &child)
    #      const
    ritual = 'ritual_ZNK21QHeaderDataProxyModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QHeaderDataProxyModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(child))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QHeaderDataProxyModel::sibling(int row, int
    column, const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderdataproxymodel.html#sibling

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
    #  QModelIndex QHeaderDataProxyModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    ritual = 'ritual_ZNK21QHeaderDataProxyModel7siblingEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QHeaderDataProxyModel7siblingEiiRK11QModelIndex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(idx))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QHeaderDataProxyModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QHeaderDataProxyModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK21QHeaderDataProxyModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QHeaderDataProxyModel8rowCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QHeaderDataProxyModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QHeaderDataProxyModel::columnCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK21QHeaderDataProxyModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QHeaderDataProxyModel11columnCountERK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QHeaderDataProxyModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderdataproxymodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QHeaderDataProxyModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK21QHeaderDataProxyModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QHeaderDataProxyModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QHeaderDataProxyModel::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QHeaderDataProxyModel::hasChildren(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK21QHeaderDataProxyModel11hasChildrenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QHeaderDataProxyModel11hasChildrenERK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QHeaderDataProxyModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QHeaderDataProxyModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK21QHeaderDataProxyModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def variantValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QHeaderDataProxyModel::variantValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#variantValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QHeaderDataProxyModel::variantValue() const
    address = self.uglySide.call(
        'ritual_ZNK21QHeaderDataProxyModel12variantValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QHeaderDataProxyModel::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QHeaderDataProxyModel::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK21QHeaderDataProxyModel11orientationEv',
    ))

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
    Calls Qt's 'void QHeaderDataProxyModel::setSourceModel(QAbstractItemModel
    *newSourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#setSourceModel

    Parameters
    ----------

    newSourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHeaderDataProxyModel::setSourceModel(QAbstractItemModel
    #      *newSourceModel)
    self.uglySide.call(
        'ritual_ZN21QHeaderDataProxyModel14setSourceModelEP18QAbstractItemM'
        'odel',
        self._addressOf(newSourceModel),
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
    Calls Qt's 'bool QHeaderDataProxyModel::setData(const QModelIndex &index,
    const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderdataproxymodel.html#setData

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
    #  bool QHeaderDataProxyModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    ritual = (
        'ritual_ZN21QHeaderDataProxyModel7setDataERK11QModelIndexRK8QVarian'
        'ti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QHeaderDataProxyModel7setDataERK11QModelIndexRK8Q'
          'Varianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, o: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QHeaderDataProxyModel::setOrientation(Qt::Orientation
    o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#setOrientation

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.
    """
    #  void QHeaderDataProxyModel::setOrientation(Qt::Orientation o)
    self.uglySide.call(
        'ritual_ZN21QHeaderDataProxyModel14setOrientationEN2Qt11Orientation'
        'E',
        o.value,
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
    'QHeaderDataProxyModel::QHeaderDataProxyModel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#QHeaderDataProxyModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHeaderDataProxyModel::QHeaderDataProxyModel(QObject *parent)
    self._noteCreation(QHeaderDataProxyModel, lambda: Rituals.call(
        'ritual_ZN21QHeaderDataProxyModelC1EP7QObject',
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

  def connectToModel(self) -> None:
    """
    Calls Qt's 'void QHeaderDataProxyModel::connectToModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#connectToModel
    """
    #  void QHeaderDataProxyModel::connectToModel()
    self.uglySide.call('ritual_ZN21QHeaderDataProxyModel14connectToModelEv')

  def disconnectFromModel(self) -> None:
    """
    Calls Qt's 'void QHeaderDataProxyModel::disconnectFromModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderdataproxymodel.html#disconnectFromModel
    """
    #  void QHeaderDataProxyModel::disconnectFromModel()
    self.uglySide.call(
        'ritual_ZN21QHeaderDataProxyModel19disconnectFromModelEv',
    )

  @staticmethod
  def sourceModel(*__, **_) -> Never:
    """
    Qt's 'QPointer<QAbstractItemModel> QHeaderDataProxyModel::sourceModel()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHeaderDataProxyModel.sourceModel' has no cute function yet. Qt's "
        "'QPointer<QAbstractItemModel> QHeaderDataProxyModel::sourceModel() "
        "const': gives a type Python has no way to take yet.")
