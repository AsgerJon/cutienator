"""
QQmlTableInstanceModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlTableInstanceModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlIncubator
from . import QQmlDelegateModel, QQmlInstanceModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QByteArray, QMetaObject
  from ..QtCore import QModelIndex, QTypeRevision, QVariant
  from ..QtQml import QQmlComponent, QQmlContext
  from . import QQmlDelegateModelItem, QQmlTableInstanceModelIncubationTask
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QModelIndex = WAIT['QModelIndex']
  QQmlComponent = WAIT['QQmlComponent']
  QQmlContext = WAIT['QQmlContext']
  QQmlDelegateModelItem = WAIT['QQmlDelegateModelItem']
  QQmlTableInstanceModelIncubationTask = WAIT['QQmlTableInstanceModelIncubationTask']
  QTypeRevision = WAIT['QTypeRevision']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTableInstanceModel(QQmlInstanceModel):
  """
  The cute side of Qt's QQmlTableInstanceModel: a plain Python object
  standing in front of one C++ QQmlTableInstanceModel.

  It is built on the cute 'QQmlInstanceModel', as Qt's QQmlTableInstanceModel
  is built on Qt's QQmlInstanceModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlTableInstanceModel that has a ritual and that
  Python can call so far, 43 names in all: 'metaObject', 'tr',
  'useImportVersion', 'count', 'rows', 'columns', 'isValid', 'canFetchMore',
  'fetchMore', 'model', 'setModel', 'delegate', 'setDelegate',
  'delegateModelAccess', 'setDelegateModelAccess', 'abstractItemModel',
  'object', 'incubateModelItemIfNeeded', 'restoreFromReleasedItemsCache',
  'commitReleasedItems', 'release', 'dispose', 'cancel',
  'drainReusableItemsPool', 'poolSize', 'reuseItem', 'incubationStatus',
  'setRequiredProperty', 'variantValue', 'setWatchedRoles', 'indexOf',
  'getModelItem', 'modelChanged', 'resolveDelegate', 'incubateModelItem',
  'incubatorStatusChanged', 'deleteIncubationTaskLater',
  'deleteAllFinishedIncubationTasks', 'resolveModelItem',
  'modelAboutToBeResetCallback', 'forceSetModel', 'isDoneIncubating',
  'deleteModelItemLater'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlTableInstanceModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlTableInstanceModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlTableInstanceModel::~QQmlTableInstanceModel()': the destructor:
    Python never removes a C++ QQmlTableInstanceModel.
  - Qt's 'void QQmlTableInstanceModel::destroyModelItem(QQmlDelegateModelItem
    *modelItem, DestructionMode mode)': names the enum
    'QQmlTableInstanceModel::DestructionMode', whose class cannot be named
    here.
  - Qt's 'void QQmlTableInstanceModel::dataChangedCallback(const QModelIndex
    &begin, const QModelIndex &end, const QList<int> &roles)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlTableInstanceModel is created at the first use, not by
    'QQmlTableInstanceModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTableInstanceModel.
  - Qt tells when it has removed the C++ QQmlTableInstanceModel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlTableInstanceModel that has no cute function yet,
    'dataChangedCallback', 'destroyModelItem', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlTableInstanceModel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltableinstancemodel.html#tr

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
    #  QString QQmlTableInstanceModel::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQmlTableInstanceModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQmlDelegateModelItem)
  @overload(NoneType)
  def isDoneIncubating(modelItem: Optional[QQmlDelegateModelItem]) -> bool:
    """
    Calls Qt's 'bool
    QQmlTableInstanceModel::isDoneIncubating(QQmlDelegateModelItem
    *modelItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#isDoneIncubating

    Parameters
    ----------

    modelItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlTableInstanceModel::isDoneIncubating(QQmlDelegateModelItem
    #      *modelItem)
    return Rituals.call(
        'ritual_ZN22QQmlTableInstanceModel16isDoneIncubatingEP21QQmlDelegat'
        'eModelItem',
        CuteMixin._addressOf(modelItem),
    )

  @staticmethod
  @overload(QQmlDelegateModelItem)
  @overload(NoneType)
  def deleteModelItemLater(
      modelItem: Optional[QQmlDelegateModelItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTableInstanceModel::deleteModelItemLater(QQmlDelegateModelItem
    *modelItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#deleteModelItemLater

    Parameters
    ----------

    modelItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQmlTableInstanceModel::deleteModelItemLater(QQmlDelegateModelItem
    #      *modelItem)
    Rituals.call(
        'ritual_ZN22QQmlTableInstanceModel20deleteModelItemLaterEP21QQmlDel'
        'egateModelItem',
        CuteMixin._addressOf(modelItem),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTableInstanceModel'

  #  A C++ QQmlTableInstanceModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlTableInstanceModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlTableInstanceModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTableInstanceModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlTableInstanceModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlTableInstanceModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltableinstancemodel.html#count
    """
    #  int QQmlTableInstanceModel::count() const
    ritual = 'ritual_ZNK22QQmlTableInstanceModel5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQmlTableInstanceModel5countEv'
    return self.uglySide.call(ritual)

  def rows(self) -> int:
    """
    Calls Qt's 'int QQmlTableInstanceModel::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltableinstancemodel.html#rows
    """
    #  int QQmlTableInstanceModel::rows() const
    return self.uglySide.call('ritual_ZNK22QQmlTableInstanceModel4rowsEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int QQmlTableInstanceModel::columns() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#columns
    """
    #  int QQmlTableInstanceModel::columns() const
    return self.uglySide.call('ritual_ZNK22QQmlTableInstanceModel7columnsEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlTableInstanceModel::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#isValid
    """
    #  bool QQmlTableInstanceModel::isValid() const
    ritual = 'ritual_ZNK22QQmlTableInstanceModel7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQmlTableInstanceModel7isValidEv'
    return self.uglySide.call(ritual)

  def canFetchMore(self) -> bool:
    """
    Calls Qt's 'bool QQmlTableInstanceModel::canFetchMore() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#canFetchMore
    """
    #  bool QQmlTableInstanceModel::canFetchMore() const
    return self.uglySide.call(
        'ritual_ZNK22QQmlTableInstanceModel12canFetchMoreEv',
    )

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTableInstanceModel::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltableinstancemodel.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTableInstanceModel::model() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlTableInstanceModel5modelEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlTableInstanceModel::delegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlTableInstanceModel::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlTableInstanceModel8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def delegateModelAccess(self) -> QQmlDelegateModel.DelegateModelAccess:
    """
    Calls Qt's 'QQmlDelegateModel::DelegateModelAccess
    QQmlTableInstanceModel::delegateModelAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#delegateModelAccess

    Returns
    -------

    QQmlDelegateModel.DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlDelegateModel.DelegateModelAccess(number)' gives.
    """
    #  QQmlDelegateModel::DelegateModelAccess
    #      QQmlTableInstanceModel::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK22QQmlTableInstanceModel19delegateModelAccessEv',
    ))

  def abstractItemModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel
    *QQmlTableInstanceModel::abstractItemModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#abstractItemModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QQmlTableInstanceModel::abstractItemModel()
    #      const
    ritual = 'ritual_ZNK22QQmlTableInstanceModel17abstractItemModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQmlTableInstanceModel17abstractItemModelEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def indexOf(self, a0: Optional[QObject], a1: Optional[QObject]) -> int:
    """
    Calls Qt's 'int QQmlTableInstanceModel::indexOf(QObject *a0, QObject *a1)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#indexOf

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlTableInstanceModel::indexOf(QObject *a0, QObject *a1) const
    ritual = 'ritual_ZNK22QQmlTableInstanceModel7indexOfEP7QObjectS1_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQmlTableInstanceModel7indexOfEP7QObjectS1_'
    return self.uglySide.call(
        ritual,
        self._addressOf(a0, 'QObject'), self._addressOf(a1, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::setModel(const QVariant
    &model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#setModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTableInstanceModel::setModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel8setModelERK8QVariant',
        self._valueOf(model),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::setDelegate(QQmlComponent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTableInstanceModel::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel11setDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(QQmlDelegateModel.DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: QQmlDelegateModel.DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTableInstanceModel::setDelegateModelAccess(QQmlDelegateModel::
    DelegateModelAccess delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#setDelegateModelAccess

    Parameters
    ----------

    delegateModelAccess : QQmlDelegateModel.DelegateModelAccess
      Passed on as its number.
    """
    #  void QQmlTableInstanceModel::setDelegateModelAccess(
    #      QQmlDelegateModel::DelegateModelAccess delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel22setDelegateModelAccessEN17QQmlD'
        'elegateModel19DelegateModelAccessE',
        delegateModelAccess.value,
    )

  @overload(int, str, QVariant)
  def setRequiredProperty(
      self,
      index: int,
      name: str,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlTableInstanceModel::setRequiredProperty(int index,
    const QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#setRequiredProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQmlTableInstanceModel::setRequiredProperty(int index, const
    #      QString &name, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel19setRequiredPropertyEiRK7QString'
        'RK8QVariant',
        index, name, self._valueOf(value),
    )

  @overload(QList[QByteArray])
  def setWatchedRoles(self, a0: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::setWatchedRoles(const
    QList<QByteArray> &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#setWatchedRoles

    Parameters
    ----------

    a0 : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlTableInstanceModel::setWatchedRoles(const QList<QByteArray>
    #      &a0)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel15setWatchedRolesERK5QListI10QByt'
        'eArrayE',
        self._valueOf(a0),
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

  @overload(QQmlContext)
  @overload(NoneType)
  @overload(QQmlContext, QObject)
  @overload(QQmlContext, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      qmlContext: Optional[QQmlContext],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTableInstanceModel::QQmlTableInstanceModel(QQmlContext *qmlContext,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#QQmlTableInstanceModel

    Parameters
    ----------

    qmlContext : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTableInstanceModel::QQmlTableInstanceModel(QQmlContext
    #      *qmlContext, QObject *parent)
    self._noteCreation(QQmlTableInstanceModel, lambda: Rituals.call(
        'ritual_ZN22QQmlTableInstanceModelC1EP11QQmlContextP7QObject',
        self._addressOf(qmlContext), self._addressOf(parent, 'QObject'),
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

  @overload(QTypeRevision)
  def useImportVersion(self, version: QTypeRevision) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::useImportVersion(QTypeRevision
    version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#useImportVersion

    Parameters
    ----------

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlTableInstanceModel::useImportVersion(QTypeRevision version)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel16useImportVersionE13QTypeRevisio'
        'n',
        self._valueOf(version),
    )

  def fetchMore(self) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::fetchMore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#fetchMore
    """
    #  void QQmlTableInstanceModel::fetchMore()
    self.uglySide.call('ritual_ZN22QQmlTableInstanceModel9fetchMoreEv')

  @overload(int)
  @overload(int, QQmlIncubator.IncubationMode)
  def object(
      self,
      index: int,
      incubationMode: QQmlIncubator.IncubationMode = (
          QQmlIncubator.IncubationMode.AsynchronousIfNested),
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlTableInstanceModel::object(int index,
    QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltableinstancemodel.html#object

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
    #  QObject *QQmlTableInstanceModel::object(int index,
    #      QQmlIncubator::IncubationMode incubationMode)
    ritual = (
        'ritual_ZN22QQmlTableInstanceModel6objectEiN13QQmlIncubator14Incuba'
        'tionModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQmlTableInstanceModel6objectEiN13QQmlIncubator14'
          'IncubationModeE')
    address = self.uglySide.call(ritual, index, incubationMode.value)
    return QObject._cuteAt(address)

  @overload(QQmlDelegateModelItem, QQmlIncubator.IncubationMode)
  @overload(NoneType, QQmlIncubator.IncubationMode)
  def incubateModelItemIfNeeded(
      self,
      modelItem: Optional[QQmlDelegateModelItem],
      incubationMode: QQmlIncubator.IncubationMode,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QQmlTableInstanceModel::incubateModelItemIfNeeded(QQmlDelegateModelItem
    *modelItem, QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html

    Parameters
    ----------

    modelItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlTableInstanceModel::incubateModelItemIfNeeded(
    #      QQmlDelegateModelItem *modelItem, QQmlIncubator::IncubationMode
    #      incubationMode)
    address = self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel25incubateModelItemIfNeededEP21QQ'
        'mlDelegateModelItemN13QQmlIncubator14IncubationModeE',
        self._addressOf(modelItem), incubationMode.value,
    )
    return QObject._cuteAt(address)

  @overload(QQmlDelegateModelItem, int)
  @overload(NoneType, int)
  def restoreFromReleasedItemsCache(
      self,
      item: Optional[QQmlDelegateModelItem],
      newFlatIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::restoreFromReleasedItemsCache(
    QQmlDelegateModelItem *item, int newFlatIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html

    Parameters
    ----------

    item : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newFlatIndex : int
      Passed on as it is.
    """
    #  void QQmlTableInstanceModel::restoreFromReleasedItemsCache(
    #      QQmlDelegateModelItem *item, int newFlatIndex)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel29restoreFromReleasedItemsCacheEP'
        '21QQmlDelegateModelItemi',
        self._addressOf(item), newFlatIndex,
    )

  def commitReleasedItems(self) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::commitReleasedItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#commitReleasedItems
    """
    #  void QQmlTableInstanceModel::commitReleasedItems()
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel19commitReleasedItemsEv',
    )

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QQmlInstanceModel.ReusableFlag)
  @overload(NoneType, QQmlInstanceModel.ReusableFlag)
  def release(
      self,
      object: Optional[QObject],
      reusable: QQmlInstanceModel.ReusableFlag = (
          QQmlInstanceModel.ReusableFlag.NotReusable),
  ) -> QQmlInstanceModel.ReleaseFlags:
    """
    Calls Qt's 'ReleaseFlags QQmlTableInstanceModel::release(QObject *object,
    ReusableFlag reusable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#release

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reusable : QQmlInstanceModel.ReusableFlag
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlInstanceModel.ReusableFlag.NotReusable.

    Returns
    -------

    QQmlInstanceModel.ReleaseFlags
      The value standing for the combination Qt gave back.
    """
    #  ReleaseFlags QQmlTableInstanceModel::release(QObject *object,
    #      ReusableFlag reusable)
    ritual = (
        'ritual_ZN22QQmlTableInstanceModel7releaseEP7QObjectN17QQmlInstance'
        'Model12ReusableFlagE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQmlTableInstanceModel7releaseEP7QObjectN17QQmlIn'
          'stanceModel12ReusableFlagE')
    return QQmlInstanceModel.ReleaseFlags(self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), reusable.value,
    ))

  @overload(QObject)
  @overload(NoneType)
  def dispose(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::dispose(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#dispose

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTableInstanceModel::dispose(QObject *object)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel7disposeEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(int)
  def cancel(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::cancel(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltableinstancemodel.html#cancel

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlTableInstanceModel::cancel(int a0)
    ritual = 'ritual_ZN22QQmlTableInstanceModel6cancelEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQmlTableInstanceModel6cancelEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def drainReusableItemsPool(self, maxPoolTime: int) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::drainReusableItemsPool(int
    maxPoolTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#drainReusableItemsPool

    Parameters
    ----------

    maxPoolTime : int
      Passed on as it is.
    """
    #  void QQmlTableInstanceModel::drainReusableItemsPool(int maxPoolTime)
    ritual = 'ritual_ZN22QQmlTableInstanceModel22drainReusableItemsPoolEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQmlTableInstanceModel22drainReusableItemsPoolEi')
    self.uglySide.call(ritual, maxPoolTime)

  def poolSize(self) -> int:
    """
    Calls Qt's 'int QQmlTableInstanceModel::poolSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#poolSize
    """
    #  int QQmlTableInstanceModel::poolSize()
    ritual = 'ritual_ZN22QQmlTableInstanceModel8poolSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQmlTableInstanceModel8poolSizeEv'
    return self.uglySide.call(ritual)

  @overload(QQmlDelegateModelItem, int)
  @overload(NoneType, int)
  def reuseItem(
      self,
      item: Optional[QQmlDelegateModelItem],
      newModelIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::reuseItem(QQmlDelegateModelItem
    *item, int newModelIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#reuseItem

    Parameters
    ----------

    item : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newModelIndex : int
      Passed on as it is.
    """
    #  void QQmlTableInstanceModel::reuseItem(QQmlDelegateModelItem *item,
    #      int newModelIndex)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel9reuseItemEP21QQmlDelegateModelIt'
        'emi',
        self._addressOf(item), newModelIndex,
    )

  @overload(int)
  def incubationStatus(self, index: int) -> QQmlIncubator.Status:
    """
    Calls Qt's 'QQmlIncubator::Status
    QQmlTableInstanceModel::incubationStatus(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#incubationStatus

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
    #  QQmlIncubator::Status QQmlTableInstanceModel::incubationStatus(int
    #      index)
    ritual = 'ritual_ZN22QQmlTableInstanceModel16incubationStatusEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQmlTableInstanceModel16incubationStatusEi'
    return QQmlIncubator.Status(self.uglySide.call(ritual, index))

  @overload(int, str)
  def variantValue(self, a0: int, a1: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTableInstanceModel::variantValue(int a0, const
    QString &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#variantValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTableInstanceModel::variantValue(int a0, const QString
    #      &a1)
    ritual = 'ritual_ZN22QQmlTableInstanceModel12variantValueEiRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQmlTableInstanceModel12variantValueEiRK7QString')
    address = self.uglySide.call(ritual, a0, a1)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def getModelItem(self, index: int) -> Optional[QQmlDelegateModelItem]:
    """
    Calls Qt's 'QQmlDelegateModelItem
    *QQmlTableInstanceModel::getModelItem(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#getModelItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlDelegateModelItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelItem *QQmlTableInstanceModel::getModelItem(int index)
    address = self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel12getModelItemEi', index,
    )
    from . import QQmlDelegateModelItem
    return QQmlDelegateModelItem._cuteAt(address)

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#modelChanged
    """
    #  void QQmlTableInstanceModel::modelChanged()
    self.uglySide.call('ritual_ZN22QQmlTableInstanceModel12modelChangedEv')

  @overload(int)
  def resolveDelegate(self, index: int) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlTableInstanceModel::resolveDelegate(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#resolveDelegate

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlTableInstanceModel::resolveDelegate(int index)
    address = self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel15resolveDelegateEi', index,
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  @overload(QQmlDelegateModelItem, QQmlIncubator.IncubationMode)
  @overload(NoneType, QQmlIncubator.IncubationMode)
  def incubateModelItem(
      self,
      modelItem: Optional[QQmlDelegateModelItem],
      incubationMode: QQmlIncubator.IncubationMode,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTableInstanceModel::incubateModelItem(QQmlDelegateModelItem
    *modelItem, QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#incubateModelItem

    Parameters
    ----------

    modelItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number.
    """
    #  void QQmlTableInstanceModel::incubateModelItem(QQmlDelegateModelItem
    #      *modelItem, QQmlIncubator::IncubationMode incubationMode)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel17incubateModelItemEP21QQmlDelega'
        'teModelItemN13QQmlIncubator14IncubationModeE',
        self._addressOf(modelItem), incubationMode.value,
    )

  @overload(QQmlTableInstanceModelIncubationTask, QQmlIncubator.Status)
  @overload(NoneType, QQmlIncubator.Status)
  def incubatorStatusChanged(
      self,
      dmIncubationTask: Optional[QQmlTableInstanceModelIncubationTask],
      status: QQmlIncubator.Status,
  ) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::incubatorStatusChanged(
    QQmlTableInstanceModelIncubationTask *dmIncubationTask,
    QQmlIncubator::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#incubatorStatusChanged

    Parameters
    ----------

    dmIncubationTask : Optional[QQmlTableInstanceModelIncubationTask]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    status : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQmlTableInstanceModel::incubatorStatusChanged(
    #      QQmlTableInstanceModelIncubationTask *dmIncubationTask,
    #      QQmlIncubator::Status status)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel22incubatorStatusChangedEP36QQmlT'
        'ableInstanceModelIncubationTaskN13QQmlIncubator6StatusE',
        self._addressOf(dmIncubationTask), status.value,
    )

  @overload(QQmlIncubator)
  @overload(NoneType)
  def deleteIncubationTaskLater(
      self,
      incubationTask: Optional[QQmlIncubator],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTableInstanceModel::deleteIncubationTaskLater(QQmlIncubator
    *incubationTask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html

    Parameters
    ----------

    incubationTask : Optional[QQmlIncubator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTableInstanceModel::deleteIncubationTaskLater(QQmlIncubator
    #      *incubationTask)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel25deleteIncubationTaskLaterEP13QQ'
        'mlIncubator',
        self._addressOf(incubationTask),
    )

  def deleteAllFinishedIncubationTasks(self) -> None:
    """
    Calls Qt's 'void
    QQmlTableInstanceModel::deleteAllFinishedIncubationTasks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html
    """
    #  void QQmlTableInstanceModel::deleteAllFinishedIncubationTasks()
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel32deleteAllFinishedIncubationTask'
        'sEv',
    )

  @overload(int, QModelIndex)
  def resolveModelItem(
      self,
      flatIndex: int,
      modelIndex: QModelIndex,
  ) -> Optional[QQmlDelegateModelItem]:
    """
    Calls Qt's 'QQmlDelegateModelItem
    *QQmlTableInstanceModel::resolveModelItem(int flatIndex, const
    QModelIndex &modelIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#resolveModelItem

    Parameters
    ----------

    flatIndex : int
      Passed on as it is.

    modelIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlDelegateModelItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelItem *QQmlTableInstanceModel::resolveModelItem(int
    #      flatIndex, const QModelIndex &modelIndex)
    address = self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel16resolveModelItemEiRK11QModelInd'
        'ex',
        flatIndex, self._valueOf(modelIndex),
    )
    from . import QQmlDelegateModelItem
    return QQmlDelegateModelItem._cuteAt(address)

  def modelAboutToBeResetCallback(self) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::modelAboutToBeResetCallback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html
    """
    #  void QQmlTableInstanceModel::modelAboutToBeResetCallback()
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel27modelAboutToBeResetCallbackEv',
    )

  @overload(QVariant)
  def forceSetModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTableInstanceModel::forceSetModel(const QVariant
    &model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltableinstancemodel.html#forceSetModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTableInstanceModel::forceSetModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN22QQmlTableInstanceModel13forceSetModelERK8QVariant',
        self._valueOf(model),
    )

  @staticmethod
  def dataChangedCallback(*__, **_) -> Never:
    """
    Qt's 'void QQmlTableInstanceModel::dataChangedCallback(const QModelIndex
    &begin, const QModelIndex &end, const QList<int> &roles)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTableInstanceModel.dataChangedCallback' has no cute function "
        "yet. Qt's 'void QQmlTableInstanceModel::dataChangedCallback(const "
        "QModelIndex &begin, const QModelIndex &end, const QList<int> "
        "&roles)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def destroyModelItem(*__, **_) -> Never:
    """
    Qt's 'void QQmlTableInstanceModel::destroyModelItem(QQmlDelegateModelItem
    *modelItem, DestructionMode mode)': names the enum
    'QQmlTableInstanceModel::DestructionMode', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQmlTableInstanceModel.destroyModelItem' has no cute function "
        "yet. Qt's 'void "
        "QQmlTableInstanceModel::destroyModelItem(QQmlDelegateModelItem "
        "*modelItem, DestructionMode mode)': names the enum "
        "'QQmlTableInstanceModel::DestructionMode', whose class cannot be "
        "named here.")
