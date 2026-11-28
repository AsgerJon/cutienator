"""
QQmlDelegateModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractItemModel, QList, QObject
from ..QtQml import QQmlIncubator, QQmlParserStatus
from . import QQmlInstanceModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject, QModelIndex
  from ..QtCore import QPersistentModelIndex, QVariant
  from ..QtQml import QQmlComponent, QQmlContext
  from . import QQmlDelegateModelAttached, QQmlDelegateModelGroup
  from . import QQmlDelegateModelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QQmlComponent = WAIT['QQmlComponent']
  QQmlContext = WAIT['QQmlContext']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModel(QQmlInstanceModel, QQmlParserStatus):
  """
  The cute side of Qt's QQmlDelegateModel: a plain Python object standing in
  front of one C++ QQmlDelegateModel.

  It is built on the cute 'QQmlInstanceModel', as Qt's QQmlDelegateModel is
  built on Qt's QQmlInstanceModel, and has everything that class has. It is
  built on the cute 'QQmlParserStatus' as well, as Qt's QQmlDelegateModel is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModel that has a ritual and that Python
  can call so far, 55 names in all: 'metaObject', 'tr', 'd_func',
  'classBegin', 'componentComplete', 'model', 'setModel', 'delegate',
  'setDelegate', 'rootIndex', 'setRootIndex', 'delegateModelAccess',
  'setDelegateModelAccess', 'modelIndex', 'parentModelIndex', 'count',
  'isValid', 'object', 'release', 'cancel', 'variantValue',
  'setWatchedRoles', 'incubationStatus', 'drainReusableItemsPool',
  'poolSize', 'indexOf', 'filterGroup', 'setFilterGroup', 'resetFilterGroup',
  'items', 'persistedItems', 'parts', 'abstractItemModel', 'event',
  'qmlAttachedProperties', 'filterGroupChanged', 'defaultGroupsChanged',
  'rootIndexChanged', 'delegateChanged', 'delegateModelAccessChanged',
  'modelChanged', '_q_itemsInserted', '_q_itemsRemoved', '_q_itemsMoved',
  '_q_modelAboutToBeReset', '_q_rowsInserted', '_q_columnsInserted',
  '_q_columnsRemoved', '_q_columnsMoved', '_q_rowsAboutToBeRemoved',
  '_q_rowsRemoved', '_q_rowsMoved', '_q_layoutChanged', 'handleModelReset',
  'isDescendantOf'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDelegateModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlDelegateModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQmlDelegateModelPrivate *QQmlDelegateModel::d_func() const':
    takes in Python what 'QQmlDelegateModelPrivate
    *QQmlDelegateModel::d_func()' takes.
  - Qt's 'void QQmlDelegateModel::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQmlDelegateModel::~QQmlDelegateModel()': the destructor: Python
    never removes a C++ QQmlDelegateModel.
  - Qt's 'QQmlListProperty<QQmlDelegateModelGroup>
    QQmlDelegateModel::groups()': gives a type Python has no way to take yet.
  - Qt's 'void QQmlDelegateModel::_q_itemsChanged(int index, int count, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlDelegateModel::_q_dataChanged(const QModelIndex &a0, const
    QModelIndex &a1, const QList<int> &a2)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  7 of the 72 functions Qt declares: 3 a template; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlDelegateModel is created at the first use, not by
    'QQmlDelegateModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModel.
  - Qt tells when it has removed the C++ QQmlDelegateModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDelegateModel that has no cute function yet,
    '_q_dataChanged', '_q_itemsChanged', 'applyDelegateChangeOnView',
    'applyDelegateModelAccessChangeOnView', 'createForView', 'groups', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlDelegateModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DelegateModelAccess(CuteNum):
    """
    The enum 'QQmlDelegateModel::DelegateModelAccess' of Qt, with the 3 names
    Qt gives in it.
    """

    Qt5ReadWrite = Kee[int](0)
    ReadOnly = Kee[int](1)
    ReadWrite = Kee[int](2)

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
    Calls Qt's 'QString QQmlDelegateModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#tr

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
    #  QString QQmlDelegateModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQmlDelegateModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQmlDelegateModelAttached]:
    """
    Calls Qt's 'QQmlDelegateModelAttached
    *QQmlDelegateModel::qmlAttachedProperties(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#qmlAttachedProperties

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlDelegateModelAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelAttached
    #      *QQmlDelegateModel::qmlAttachedProperties(QObject *obj)
    address = Rituals.call(
        'ritual_ZN17QQmlDelegateModel21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    from . import QQmlDelegateModelAttached
    return QQmlDelegateModelAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModel'

  #  Qt's QQmlDelegateModel is built on more than one class. The part of a
  #  C++ QQmlDelegateModel that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlDelegateModel_QQmlParserStatus',
  }

  #  A C++ QQmlDelegateModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelegateModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDelegateModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDelegateModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlDelegateModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDelegateModel::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDelegateModel::model() const
    address = self.uglySide.call('ritual_ZNK17QQmlDelegateModel5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlDelegateModel::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlDelegateModel::delegate() const
    address = self.uglySide.call('ritual_ZNK17QQmlDelegateModel8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def rootIndex(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDelegateModel::rootIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#rootIndex

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDelegateModel::rootIndex() const
    address = self.uglySide.call('ritual_ZNK17QQmlDelegateModel9rootIndexEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegateModelAccess(self) -> DelegateModelAccess:
    """
    Calls Qt's 'DelegateModelAccess QQmlDelegateModel::delegateModelAccess()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#delegateModelAccess

    Returns
    -------

    DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'DelegateModelAccess(number)' gives.
    """
    #  DelegateModelAccess QQmlDelegateModel::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK17QQmlDelegateModel19delegateModelAccessEv',
    ))

  @overload(int)
  def modelIndex(self, idx: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDelegateModel::modelIndex(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#modelIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDelegateModel::modelIndex(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlDelegateModel10modelIndexEi', idx,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def parentModelIndex(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDelegateModel::parentModelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#parentModelIndex

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDelegateModel::parentModelIndex() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlDelegateModel16parentModelIndexEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#count
    """
    #  int QQmlDelegateModel::count() const
    ritual = 'ritual_ZNK17QQmlDelegateModel5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQmlDelegateModel5countEv'
    return self.uglySide.call(ritual)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModel::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#isValid
    """
    #  bool QQmlDelegateModel::isValid() const
    ritual = 'ritual_ZNK17QQmlDelegateModel7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQmlDelegateModel7isValidEv'
    return self.uglySide.call(ritual)

  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def indexOf(
      self,
      object: Optional[QObject],
      objectContext: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'int QQmlDelegateModel::indexOf(QObject *object, QObject
    *objectContext) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#indexOf

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectContext : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlDelegateModel::indexOf(QObject *object, QObject
    #      *objectContext) const
    ritual = 'ritual_ZNK17QQmlDelegateModel7indexOfEP7QObjectS1_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQmlDelegateModel7indexOfEP7QObjectS1_'
    return self.uglySide.call(
        ritual,
        self._addressOf(object, 'QObject'), self._addressOf(objectContext,
        'QObject'),
    )

  def filterGroup(self) -> str:
    """
    Calls Qt's 'QString QQmlDelegateModel::filterGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#filterGroup

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDelegateModel::filterGroup() const
    return self.uglySide.call('ritual_ZNK17QQmlDelegateModel11filterGroupEv')

  def abstractItemModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel
    *QQmlDelegateModel::abstractItemModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#abstractItemModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QQmlDelegateModel::abstractItemModel() const
    ritual = 'ritual_ZNK17QQmlDelegateModel17abstractItemModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQmlDelegateModel17abstractItemModelEv'
    address = self.uglySide.call(ritual)
    return QAbstractItemModel._cuteAt(address)

  @overload(QPersistentModelIndex, QList[QPersistentModelIndex])
  def isDescendantOf(
      self,
      desc: QPersistentModelIndex,
      parents: QList[QPersistentModelIndex],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModel::isDescendantOf(const
    QPersistentModelIndex &desc, const QList<QPersistentModelIndex> &parents)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#isDescendantOf

    Parameters
    ----------

    desc : QPersistentModelIndex
      Passed on as a value: Qt reads the C++ QPersistentModelIndex, which
      stays Python's own.

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QQmlDelegateModel::isDescendantOf(const QPersistentModelIndex
    #      &desc, const QList<QPersistentModelIndex> &parents) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlDelegateModel14isDescendantOfERK21QPersistentModel'
        'IndexRK5QListIS0_E',
        self._valueOf(desc), self._valueOf(parents),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::setModel(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#setModel

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlDelegateModel::setModel(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel8setModelERK8QVariant',
        self._valueOf(a0),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::setDelegate(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModel::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel11setDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(QVariant)
  def setRootIndex(self, root: QVariant) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::setRootIndex(const QVariant &root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#setRootIndex

    Parameters
    ----------

    root : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlDelegateModel::setRootIndex(const QVariant &root)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel12setRootIndexERK8QVariant',
        self._valueOf(root),
    )

  @overload(DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModel::setDelegateModelAccess(DelegateModelAccess
    delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#setDelegateModelAccess

    Parameters
    ----------

    delegateModelAccess : DelegateModelAccess
      Passed on as its number.
    """
    #  void QQmlDelegateModel::setDelegateModelAccess(DelegateModelAccess
    #      delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel22setDelegateModelAccessENS_19Delegate'
        'ModelAccessE',
        delegateModelAccess.value,
    )

  @overload(QList[QByteArray])
  def setWatchedRoles(self, roles: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::setWatchedRoles(const
    QList<QByteArray> &roles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#setWatchedRoles

    Parameters
    ----------

    roles : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlDelegateModel::setWatchedRoles(const QList<QByteArray>
    #      &roles)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel15setWatchedRolesERK5QListI10QByteArra'
        'yE',
        self._valueOf(roles),
    )

  @overload(str)
  def setFilterGroup(self, group: str) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::setFilterGroup(const QString
    &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#setFilterGroup

    Parameters
    ----------

    group : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDelegateModel::setFilterGroup(const QString &group)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel14setFilterGroupERK7QString', group,
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
    Notes what was given, for Qt's 'QQmlDelegateModel::QQmlDelegateModel()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#QQmlDelegateModel
    """
    #  QQmlDelegateModel::QQmlDelegateModel()
    self._noteCreation(QQmlDelegateModel, lambda: Rituals.call(
        'ritual_ZN17QQmlDelegateModelC1Ev',
    ))

  @overload(QQmlContext)
  @overload(NoneType)
  @overload(QQmlContext, QObject)
  @overload(QQmlContext, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlContext],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModel::QQmlDelegateModel(QQmlContext *a0, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#QQmlDelegateModel

    Parameters
    ----------

    a0 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlDelegateModel::QQmlDelegateModel(QQmlContext *a0, QObject *parent)
    self._noteCreation(QQmlDelegateModel, lambda: Rituals.call(
        'ritual_ZN17QQmlDelegateModelC1EP11QQmlContextP7QObject',
        self._addressOf(a0), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QQmlDelegateModelPrivate]:
    """
    Calls Qt's 'QQmlDelegateModelPrivate *QQmlDelegateModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#d_func

    Returns
    -------

    Optional[QQmlDelegateModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelPrivate *QQmlDelegateModel::d_func()
    address = self.uglySide.call('ritual_ZN17QQmlDelegateModel6d_funcEv')
    from . import QQmlDelegateModelPrivate
    return QQmlDelegateModelPrivate._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#classBegin
    """
    #  void QQmlDelegateModel::classBegin()
    ritual = 'ritual_ZN17QQmlDelegateModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#componentComplete
    """
    #  void QQmlDelegateModel::componentComplete()
    ritual = 'ritual_ZN17QQmlDelegateModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(int)
  @overload(int, QQmlIncubator.IncubationMode)
  def object(
      self,
      index: int,
      incubationMode: QQmlIncubator.IncubationMode = (
          QQmlIncubator.IncubationMode.AsynchronousIfNested),
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDelegateModel::object(int index,
    QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#object

    Parameters
    ----------

    index : int
      Passed on as it is.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlIncubator.IncubationMode.AsynchronousIfNested.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDelegateModel::object(int index,
    #      QQmlIncubator::IncubationMode incubationMode)
    ritual = (
        'ritual_ZN17QQmlDelegateModel6objectEiN13QQmlIncubator14IncubationM'
        'odeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlDelegateModel6objectEiN13QQmlIncubator14Incub'
          'ationModeE')
    address = self.uglySide.call(ritual, index, incubationMode.value)
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QQmlInstanceModel.ReusableFlag)
  @overload(NoneType, QQmlInstanceModel.ReusableFlag)
  def release(
      self,
      object: Optional[QObject],
      reusableFlag: QQmlInstanceModel.ReusableFlag = (
          QQmlInstanceModel.ReusableFlag.NotReusable),
  ) -> QQmlInstanceModel.ReleaseFlags:
    """
    Calls Qt's 'ReleaseFlags QQmlDelegateModel::release(QObject *object,
    ReusableFlag reusableFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#release

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reusableFlag : QQmlInstanceModel.ReusableFlag
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlInstanceModel.ReusableFlag.NotReusable.

    Returns
    -------

    QQmlInstanceModel.ReleaseFlags
      The value standing for the combination Qt gave back.
    """
    #  ReleaseFlags QQmlDelegateModel::release(QObject *object, ReusableFlag
    #      reusableFlag)
    ritual = (
        'ritual_ZN17QQmlDelegateModel7releaseEP7QObjectN17QQmlInstanceModel'
        '12ReusableFlagE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlDelegateModel7releaseEP7QObjectN17QQmlInstanc'
          'eModel12ReusableFlagE')
    return QQmlInstanceModel.ReleaseFlags(self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), reusableFlag.value,
    ))

  @overload(int)
  def cancel(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::cancel(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#cancel

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::cancel(int index)
    ritual = 'ritual_ZN17QQmlDelegateModel6cancelEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel6cancelEi'
    self.uglySide.call(ritual, index)

  @overload(int, str)
  def variantValue(self, index: int, role: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDelegateModel::variantValue(int index, const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#variantValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    role : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDelegateModel::variantValue(int index, const QString
    #      &role)
    ritual = 'ritual_ZN17QQmlDelegateModel12variantValueEiRK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel12variantValueEiRK7QString'
    address = self.uglySide.call(ritual, index, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def incubationStatus(self, index: int) -> QQmlIncubator.Status:
    """
    Calls Qt's 'QQmlIncubator::Status QQmlDelegateModel::incubationStatus(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#incubationStatus

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QQmlIncubator.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlIncubator.Status(number)' gives.
    """
    #  QQmlIncubator::Status QQmlDelegateModel::incubationStatus(int index)
    ritual = 'ritual_ZN17QQmlDelegateModel16incubationStatusEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel16incubationStatusEi'
    return QQmlIncubator.Status(self.uglySide.call(ritual, index))

  @overload(int)
  def drainReusableItemsPool(self, maxPoolTime: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::drainReusableItemsPool(int
    maxPoolTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#drainReusableItemsPool

    Parameters
    ----------

    maxPoolTime : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::drainReusableItemsPool(int maxPoolTime)
    ritual = 'ritual_ZN17QQmlDelegateModel22drainReusableItemsPoolEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel22drainReusableItemsPoolEi'
    self.uglySide.call(ritual, maxPoolTime)

  def poolSize(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModel::poolSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#poolSize
    """
    #  int QQmlDelegateModel::poolSize()
    ritual = 'ritual_ZN17QQmlDelegateModel8poolSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel8poolSizeEv'
    return self.uglySide.call(ritual)

  def resetFilterGroup(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::resetFilterGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#resetFilterGroup
    """
    #  void QQmlDelegateModel::resetFilterGroup()
    self.uglySide.call('ritual_ZN17QQmlDelegateModel16resetFilterGroupEv')

  def items(self) -> Optional[QQmlDelegateModelGroup]:
    """
    Calls Qt's 'QQmlDelegateModelGroup *QQmlDelegateModel::items()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#items

    Returns
    -------

    Optional[QQmlDelegateModelGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelGroup *QQmlDelegateModel::items()
    address = self.uglySide.call('ritual_ZN17QQmlDelegateModel5itemsEv')
    from . import QQmlDelegateModelGroup
    return QQmlDelegateModelGroup._cuteAt(address)

  def persistedItems(self) -> Optional[QQmlDelegateModelGroup]:
    """
    Calls Qt's 'QQmlDelegateModelGroup *QQmlDelegateModel::persistedItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#persistedItems

    Returns
    -------

    Optional[QQmlDelegateModelGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelGroup *QQmlDelegateModel::persistedItems()
    address = self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel14persistedItemsEv',
    )
    from . import QQmlDelegateModelGroup
    return QQmlDelegateModelGroup._cuteAt(address)

  def parts(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDelegateModel::parts()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#parts

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDelegateModel::parts()
    address = self.uglySide.call('ritual_ZN17QQmlDelegateModel5partsEv')
    return QObject._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModel::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodel.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlDelegateModel::event(QEvent *a0)
    ritual = 'ritual_ZN17QQmlDelegateModel5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlDelegateModel5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def filterGroupChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::filterGroupChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#filterGroupChanged
    """
    #  void QQmlDelegateModel::filterGroupChanged()
    self.uglySide.call('ritual_ZN17QQmlDelegateModel18filterGroupChangedEv')

  def defaultGroupsChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::defaultGroupsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#defaultGroupsChanged
    """
    #  void QQmlDelegateModel::defaultGroupsChanged()
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel20defaultGroupsChangedEv',
    )

  def rootIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::rootIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#rootIndexChanged
    """
    #  void QQmlDelegateModel::rootIndexChanged()
    self.uglySide.call('ritual_ZN17QQmlDelegateModel16rootIndexChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#delegateChanged
    """
    #  void QQmlDelegateModel::delegateChanged()
    self.uglySide.call('ritual_ZN17QQmlDelegateModel15delegateChangedEv')

  def delegateModelAccessChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::delegateModelAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#delegateModelAccessChanged
    """
    #  void QQmlDelegateModel::delegateModelAccessChanged()
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel26delegateModelAccessChangedEv',
    )

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#modelChanged
    """
    #  void QQmlDelegateModel::modelChanged()
    self.uglySide.call('ritual_ZN17QQmlDelegateModel12modelChangedEv')

  @overload(int, int)
  def _q_itemsInserted(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_itemsInserted(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_itemsInserted

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_itemsInserted(int index, int count)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel16_q_itemsInsertedEii', index, count,
    )

  @overload(int, int)
  def _q_itemsRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_itemsRemoved(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_itemsRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_itemsRemoved(int index, int count)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel15_q_itemsRemovedEii', index, count,
    )

  @overload(int, int, int)
  def _q_itemsMoved(self, from_: int, to: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_itemsMoved(int from, int to, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_itemsMoved

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_itemsMoved(int from, int to, int count)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel13_q_itemsMovedEiii', from_, to, count,
    )

  def _q_modelAboutToBeReset(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_modelAboutToBeReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_modelAboutToBeReset
    """
    #  void QQmlDelegateModel::_q_modelAboutToBeReset()
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel22_q_modelAboutToBeResetEv',
    )

  @overload(QModelIndex, int, int)
  def _q_rowsInserted(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_rowsInserted(const QModelIndex
    &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_rowsInserted

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_rowsInserted(const QModelIndex &a0, int a1,
    #      int a2)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel15_q_rowsInsertedERK11QModelIndexii',
        self._valueOf(a0), a1, a2,
    )

  @overload(QModelIndex, int, int)
  def _q_columnsInserted(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_columnsInserted(const QModelIndex
    &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_columnsInserted

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_columnsInserted(const QModelIndex &a0, int
    #      a1, int a2)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel18_q_columnsInsertedERK11QModelIndexii',
        self._valueOf(a0), a1, a2,
    )

  @overload(QModelIndex, int, int)
  def _q_columnsRemoved(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_columnsRemoved(const QModelIndex
    &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_columnsRemoved

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_columnsRemoved(const QModelIndex &a0, int
    #      a1, int a2)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel17_q_columnsRemovedERK11QModelIndexii',
        self._valueOf(a0), a1, a2,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def _q_columnsMoved(
      self,
      a0: QModelIndex,
      a1: int,
      a2: int,
      a3: QModelIndex,
      a4: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_columnsMoved(const QModelIndex
    &a0, int a1, int a2, const QModelIndex &a3, int a4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_columnsMoved

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a4 : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_columnsMoved(const QModelIndex &a0, int a1,
    #      int a2, const QModelIndex &a3, int a4)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel15_q_columnsMovedERK11QModelIndexiiS2_'
        'i',
        self._valueOf(a0), a1, a2, self._valueOf(a3), a4,
    )

  @overload(QModelIndex, int, int)
  def _q_rowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      begin: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_rowsAboutToBeRemoved(const
    QModelIndex &parent, int begin, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_rowsAboutToBeRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    begin : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_rowsAboutToBeRemoved(const QModelIndex
    #      &parent, int begin, int end)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel23_q_rowsAboutToBeRemovedERK11QModelIn'
        'dexii',
        self._valueOf(parent), begin, end,
    )

  @overload(QModelIndex, int, int)
  def _q_rowsRemoved(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_rowsRemoved(const QModelIndex &a0,
    int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_rowsRemoved

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_rowsRemoved(const QModelIndex &a0, int a1,
    #      int a2)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel14_q_rowsRemovedERK11QModelIndexii',
        self._valueOf(a0), a1, a2,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def _q_rowsMoved(
      self,
      a0: QModelIndex,
      a1: int,
      a2: int,
      a3: QModelIndex,
      a4: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_rowsMoved(const QModelIndex &a0,
    int a1, int a2, const QModelIndex &a3, int a4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_rowsMoved

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a4 : int
      Passed on as it is.
    """
    #  void QQmlDelegateModel::_q_rowsMoved(const QModelIndex &a0, int a1,
    #      int a2, const QModelIndex &a3, int a4)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel12_q_rowsMovedERK11QModelIndexiiS2_i',
        self._valueOf(a0), a1, a2, self._valueOf(a3), a4,
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def _q_layoutChanged(
      self,
      a0: QList[QPersistentModelIndex],
      a1: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::_q_layoutChanged(const
    QList<QPersistentModelIndex> &a0, QAbstractItemModel::LayoutChangeHint
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#_q_layoutChanged

    Parameters
    ----------

    a0 : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    a1 : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QQmlDelegateModel::_q_layoutChanged(const
    #      QList<QPersistentModelIndex> &a0,
    #      QAbstractItemModel::LayoutChangeHint a1)
    self.uglySide.call(
        'ritual_ZN17QQmlDelegateModel16_q_layoutChangedERK5QListI21QPersist'
        'entModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(a0), a1.value,
    )

  def handleModelReset(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModel::handleModelReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodel.html#handleModelReset
    """
    #  void QQmlDelegateModel::handleModelReset()
    self.uglySide.call('ritual_ZN17QQmlDelegateModel16handleModelResetEv')

  @staticmethod
  def _q_dataChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModel::_q_dataChanged(const QModelIndex &a0, const
    QModelIndex &a1, const QList<int> &a2)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModel._q_dataChanged' has no cute function yet. Qt's "
        "'void QQmlDelegateModel::_q_dataChanged(const QModelIndex &a0, "
        "const QModelIndex &a1, const QList<int> &a2)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def _q_itemsChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModel::_q_itemsChanged(int index, int count, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModel._q_itemsChanged' has no cute function yet. Qt's "
        "'void QQmlDelegateModel::_q_itemsChanged(int index, int count, "
        "const QList<int> &roles)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def applyDelegateChangeOnView(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModel::applyDelegateChangeOnView': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlDelegateModel.applyDelegateChangeOnView' has no cute function "
        "yet. Qt's 'QQmlDelegateModel::applyDelegateChangeOnView': a "
        "template: a pattern and no single function.")

  @staticmethod
  def applyDelegateModelAccessChangeOnView(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModel::applyDelegateModelAccessChangeOnView': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlDelegateModel.applyDelegateModelAccessChangeOnView' has no "
        "cute function yet. Qt's "
        "'QQmlDelegateModel::applyDelegateModelAccessChangeOnView': a "
        "template: a pattern and no single function.")

  @staticmethod
  def createForView(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModel::createForView': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlDelegateModel.createForView' has no cute function yet. Qt's "
        "'QQmlDelegateModel::createForView': a template: a pattern and no "
        "single function.")

  @staticmethod
  def groups(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlDelegateModelGroup>
    QQmlDelegateModel::groups()': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModel.groups' has no cute function yet. Qt's "
        "'QQmlListProperty<QQmlDelegateModelGroup> "
        "QQmlDelegateModel::groups()': gives a type Python has no way to "
        "take yet.")
