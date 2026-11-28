"""
QQmlListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlListModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QObject
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from ..QtQml import QJSValue, QQmlV4Function
  from . import ListModel, QQmlListModelWorkerAgent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ListModel = WAIT['ListModel']
  QJSValue = WAIT['QJSValue']
  QModelIndex = WAIT['QModelIndex']
  QQmlListModelWorkerAgent = WAIT['QQmlListModelWorkerAgent']
  QQmlV4Function = WAIT['QQmlV4Function']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlListModel(QAbstractListModel):
  """
  The cute side of Qt's QQmlListModel: a plain Python object standing in
  front of one C++ QQmlListModel.

  It is built on the cute 'QAbstractListModel', as Qt's QQmlListModel is
  built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlListModel that has a ritual and that Python can
  call so far, 29 names in all: 'metaObject', 'tr', 'index', 'rowCount',
  'data', 'setData', 'roleNames', 'count', 'clear', 'remove', 'append',
  'insert', 'get', 'set', 'setProperty', 'move', 'sync', 'agent',
  'dynamicRoles', 'setDynamicRoles', 'listModel', 'countChanged', 'engine',
  'canMove', 'createWithOwner', 'emitItemsAboutToBeInserted',
  'emitItemsInserted', 'removeElements', 'updateTranslations'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlListModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlListModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListModel::~QQmlListModel()': the destructor: Python never
    removes a C++ QQmlListModel.
  - Qt's 'void QQmlListModel::emitItemsChanged(int index, int count, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 40 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlListModel is created at the first use, not by
    'QQmlListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlListModel.
  - Qt tells when it has removed the C++ QQmlListModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlListModel that has no cute function yet,
    'emitItemsChanged', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQmlListModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#tr

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
    #  QString QQmlListModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQmlListModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def createWithOwner(
      newOwner: Optional[QQmlListModel],
  ) -> Optional[QQmlListModel]:
    """
    Calls Qt's 'QQmlListModel *QQmlListModel::createWithOwner(QQmlListModel
    *newOwner)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#createWithOwner

    Parameters
    ----------

    newOwner : Optional[QQmlListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlListModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlListModel *QQmlListModel::createWithOwner(QQmlListModel *newOwner)
    address = Rituals.call(
        'ritual_ZN13QQmlListModel15createWithOwnerEPS_',
        CuteMixin._addressOf(newOwner),
    )
    return QQmlListModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlListModel'

  #  A C++ QQmlListModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlListModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlListModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQmlListModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, int, QModelIndex)
  def index(self, row: int, column: int, parent: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlListModel::index(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlListModel::index(int row, int column, const
    #      QModelIndex &parent) const
    ritual = 'ritual_ZNK13QQmlListModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlListModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QQmlListModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQmlListModel::rowCount(const QModelIndex &parent) const
    ritual = 'ritual_ZNK13QQmlListModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlListModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlListModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlListModel::data(const QModelIndex &index, int role) const
    ritual = 'ritual_ZNK13QQmlListModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlListModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, int)
  def data(self, index: int, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlListModel::data(int index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#data

    Parameters
    ----------

    index : int
      Passed on as it is.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlListModel::data(int index, int role) const
    address = self.uglySide.call(
        'ritual_ZNK13QQmlListModel4dataEii', index, role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQmlListModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQmlListModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK13QQmlListModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlListModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#count
    """
    #  int QQmlListModel::count() const
    return self.uglySide.call('ritual_ZNK13QQmlListModel5countEv')

  @overload(int)
  def get(self, index: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlListModel::get(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#get

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlListModel::get(int index) const
    address = self.uglySide.call('ritual_ZNK13QQmlListModel3getEi', index)
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def dynamicRoles(self) -> bool:
    """
    Calls Qt's 'bool QQmlListModel::dynamicRoles() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#dynamicRoles
    """
    #  bool QQmlListModel::dynamicRoles() const
    return self.uglySide.call('ritual_ZNK13QQmlListModel12dynamicRolesEv')

  def listModel(self) -> Optional[ListModel]:
    """
    Calls Qt's 'ListModel *QQmlListModel::listModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#listModel

    Returns
    -------

    Optional[ListModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ListModel *QQmlListModel::listModel() const
    address = self.uglySide.call('ritual_ZNK13QQmlListModel9listModelEv')
    from . import ListModel
    return ListModel._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQmlListModel::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQmlListModel::engine() const
    address = self.uglySide.call('ritual_ZNK13QQmlListModel6engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  @overload(int, int, int)
  def canMove(self, from_: int, to: int, n: int) -> bool:
    """
    Calls Qt's 'bool QQmlListModel::canMove(int from, int to, int n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#canMove

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    n : int
      Passed on as it is.
    """
    #  bool QQmlListModel::canMove(int from, int to, int n) const
    return self.uglySide.call(
        'ritual_ZNK13QQmlListModel7canMoveEiii', from_, to, n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlListModel::setData(const QModelIndex &index, const
    QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#setData

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
    #  bool QQmlListModel::setData(const QModelIndex &index, const QVariant
    #      &value, int role)
    ritual = 'ritual_ZN13QQmlListModel7setDataERK11QModelIndexRK8QVarianti'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQmlListModel7setDataERK11QModelIndexRK8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(int, str, QVariant)
  def setProperty(self, index: int, property: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlListModel::setProperty(int index, const QString
    &property, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#setProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    property : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlListModel::setProperty(int index, const QString &property,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel11setPropertyEiRK7QStringRK8QVariant',
        index, property, self._valueOf(value),
    )

  @overload(bool)
  def setDynamicRoles(self, enableDynamicRoles: bool) -> None:
    """
    Calls Qt's 'void QQmlListModel::setDynamicRoles(bool
    enableDynamicRoles)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#setDynamicRoles

    Parameters
    ----------

    enableDynamicRoles : bool
      Passed on as it is.
    """
    #  void QQmlListModel::setDynamicRoles(bool enableDynamicRoles)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel15setDynamicRolesEb', enableDynamicRoles,
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
    Notes what was given, for Qt's 'QQmlListModel::QQmlListModel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#QQmlListModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlListModel::QQmlListModel(QObject *parent)
    self._noteCreation(QQmlListModel, lambda: Rituals.call(
        'ritual_ZN13QQmlListModelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(THIS, QQmlListModelWorkerAgent)
  @overload(THIS, NoneType)
  @overload(NoneType, QQmlListModelWorkerAgent)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      orig: Optional[QQmlListModel],
      agent: Optional[QQmlListModelWorkerAgent],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlListModel::QQmlListModel(QQmlListModel *orig,
    QQmlListModelWorkerAgent *agent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#QQmlListModel

    Parameters
    ----------

    orig : Optional[QQmlListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    agent : Optional[QQmlListModelWorkerAgent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlListModel::QQmlListModel(QQmlListModel *orig,
    #      QQmlListModelWorkerAgent *agent)
    self._noteCreation(QQmlListModel, lambda: Rituals.call(
        'ritual_ZN13QQmlListModelC1EPS_P24QQmlListModelWorkerAgent',
        self._addressOf(orig), self._addressOf(agent),
    ))

  @overload(THIS, ListModel, WAIT['QV4.ExecutionEngine'])
  @overload(THIS, ListModel, NoneType)
  @overload(THIS, NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(THIS, NoneType, NoneType)
  @overload(NoneType, ListModel, WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, ListModel, NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, NoneType, NoneType)
  @overload(THIS, ListModel, WAIT['QV4.ExecutionEngine'], QObject)
  @overload(THIS, ListModel, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(THIS, ListModel, NoneType, QObject)
  @overload(THIS, ListModel, NoneType, NoneType)
  @overload(THIS, NoneType, WAIT['QV4.ExecutionEngine'], QObject)
  @overload(THIS, NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(THIS, NoneType, NoneType, QObject)
  @overload(THIS, NoneType, NoneType, NoneType)
  @overload(NoneType, ListModel, WAIT['QV4.ExecutionEngine'], QObject)
  @overload(NoneType, ListModel, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, ListModel, NoneType, QObject)
  @overload(NoneType, ListModel, NoneType, NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.ExecutionEngine'], QObject)
  @overload(NoneType, NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      owner: Optional[QQmlListModel],
      data: Optional[ListModel],
      engine: Optional[QV4.ExecutionEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlListModel::QQmlListModel(const
    QQmlListModel *owner, ListModel *data, QV4::ExecutionEngine *engine,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#QQmlListModel

    Parameters
    ----------

    owner : Optional[QQmlListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[ListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlListModel::QQmlListModel(const QQmlListModel *owner, ListModel
    #      *data, QV4::ExecutionEngine *engine, QObject *parent)
    self._noteCreation(QQmlListModel, lambda: Rituals.call(
        'ritual_ZN13QQmlListModelC1EPKS_P9ListModelPN3QV415ExecutionEngineE'
        'P7QObject',
        self._addressOf(owner), self._addressOf(data),
        self._addressOf(engine), self._addressOf(parent, 'QObject'),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlListModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#clear
    """
    #  void QQmlListModel::clear()
    self.uglySide.call('ritual_ZN13QQmlListModel5clearEv')

  @overload(QQmlV4Function)
  @overload(NoneType)
  def remove(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlListModel::remove(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#remove

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlListModel::remove(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel6removeEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def append(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlListModel::append(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#append

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlListModel::append(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel6appendEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def insert(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlListModel::insert(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#insert

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlListModel::insert(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel6insertEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(int, QJSValue)
  def set(self, index: int, value: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlListModel::set(int index, const QJSValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#set

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlListModel::set(int index, const QJSValue &value)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel3setEiRK8QJSValue',
        index, self._valueOf(value),
    )

  @overload(int, int, int)
  def move(self, from_: int, to: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlListModel::move(int from, int to, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#move

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlListModel::move(int from, int to, int count)
    self.uglySide.call('ritual_ZN13QQmlListModel4moveEiii', from_, to, count)

  @overload()
  def sync(self) -> None:
    """
    Calls Qt's 'void QQmlListModel::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#sync
    """
    #  void QQmlListModel::sync()
    self.uglySide.call('ritual_ZN13QQmlListModel4syncEv')

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def sync(
      src: Optional[QQmlListModel],
      target: Optional[QQmlListModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlListModel::sync(QQmlListModel *src, QQmlListModel
    *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#sync

    Parameters
    ----------

    src : Optional[QQmlListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QQmlListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlListModel::sync(QQmlListModel *src, QQmlListModel *target)
    return Rituals.call(
        'ritual_ZN13QQmlListModel4syncEPS_S0_',
        CuteMixin._addressOf(src), CuteMixin._addressOf(target),
    )

  def agent(self) -> Optional[QQmlListModelWorkerAgent]:
    """
    Calls Qt's 'QQmlListModelWorkerAgent *QQmlListModel::agent()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#agent

    Returns
    -------

    Optional[QQmlListModelWorkerAgent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlListModelWorkerAgent *QQmlListModel::agent()
    address = self.uglySide.call('ritual_ZN13QQmlListModel5agentEv')
    from . import QQmlListModelWorkerAgent
    return QQmlListModelWorkerAgent._cuteAt(address)

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQmlListModel::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#countChanged
    """
    #  void QQmlListModel::countChanged()
    self.uglySide.call('ritual_ZN13QQmlListModel12countChangedEv')

  @overload(int, int)
  def emitItemsAboutToBeInserted(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlListModel::emitItemsAboutToBeInserted(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodel.html#emitItemsAboutToBeInserted

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlListModel::emitItemsAboutToBeInserted(int index, int count)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel26emitItemsAboutToBeInsertedEii',
        index, count,
    )

  def emitItemsInserted(self) -> None:
    """
    Calls Qt's 'void QQmlListModel::emitItemsInserted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodel.html#emitItemsInserted
    """
    #  void QQmlListModel::emitItemsInserted()
    self.uglySide.call('ritual_ZN13QQmlListModel17emitItemsInsertedEv')

  @overload(int, int)
  def removeElements(self, index: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QQmlListModel::removeElements(int index, int
    removeCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodel.html#removeElements

    Parameters
    ----------

    index : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QQmlListModel::removeElements(int index, int removeCount)
    self.uglySide.call(
        'ritual_ZN13QQmlListModel14removeElementsEii', index, removeCount,
    )

  def updateTranslations(self) -> None:
    """
    Calls Qt's 'void QQmlListModel::updateTranslations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodel.html#updateTranslations
    """
    #  void QQmlListModel::updateTranslations()
    self.uglySide.call('ritual_ZN13QQmlListModel18updateTranslationsEv')

  @staticmethod
  def emitItemsChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlListModel::emitItemsChanged(int index, int count, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlListModel.emitItemsChanged' has no cute function yet. Qt's "
        "'void QQmlListModel::emitItemsChanged(int index, int count, const "
        "QList<int> &roles)': takes a type Python has no way to hand over "
        "yet.")
