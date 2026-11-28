"""
QQmlDelegateModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QQmlDelegateModelGroupEmitter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from ..QtQml import QQmlComponent
  from . import QQDMIncubationTask, QQmlChangeSet, QQmlDelegateModel
  from . import QQmlDelegateModelItem, QQuickPackage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQDMIncubationTask = WAIT['QQDMIncubationTask']
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQmlDelegateModel = WAIT['QQmlDelegateModel']
  QQmlDelegateModelItem = WAIT['QQmlDelegateModelItem']
  QQuickPackage = WAIT['QQuickPackage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelPrivate(QObjectPrivate, QQmlDelegateModelGroupEmitter):
  """
  The cute side of Qt's QQmlDelegateModelPrivate: a plain Python object
  standing in front of one C++ QQmlDelegateModelPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQmlDelegateModelPrivate
  is built on Qt's QObjectPrivate, and has everything that class has. It is
  built on the cute 'QQmlDelegateModelGroupEmitter' as well, as Qt's
  QQmlDelegateModelPrivate is built on Qt's QQmlDelegateModelGroupEmitter
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelPrivate that has a ritual and that
  Python can call so far, 16 names in all: 'q_func', 'get', 'init',
  'connectToAbstractItemModel', 'disconnectFromAbstractItemModel',
  'requestMoreIfNecessary', 'emitCreatedPackage', 'emitCreatedItem',
  'emitInitItem', 'emitDestroyingItem', 'destroyCacheItem',
  'drainReusableItemsPool', 'resolveDelegate', 'emitModelUpdated',
  'adaptorModelCount', 'releaseIncubator'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlDelegateModel *QQmlDelegateModelPrivate::q_func() const':
    takes in Python what 'QQmlDelegateModel
    *QQmlDelegateModelPrivate::q_func()' takes.
  - Qt's 'QQmlDelegateModelPrivate::~QQmlDelegateModelPrivate()': the
    destructor: Python never removes a C++ QQmlDelegateModelPrivate.
  - Qt's 'void QQmlDelegateModelPrivate::itemsInserted(const
    QList<Compositor::Insert> &inserts)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlDelegateModelPrivate::itemsChanged(const
    QList<Compositor::Change> &changes)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlDelegateModelPrivate::group_append(
    QQmlListProperty<QQmlDelegateModelGroup> *property,
    QQmlDelegateModelGroup *group)': names
    'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute class yet.
  - Qt's 'qsizetype QQmlDelegateModelPrivate::group_count(
    QQmlListProperty<QQmlDelegateModelGroup> *property)': names
    'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute class yet.
  - Qt's 'QQmlDelegateModelGroup *QQmlDelegateModelPrivate::group_at(
    QQmlListProperty<QQmlDelegateModelGroup> *property, qsizetype index)':
    names 'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute class
    yet.

  What has no ritual
  ------------------

  23 of the 46 functions Qt declares: 11 leans on 'QQmlListCompositor; 3 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 2 leans on 'QQDMIncubationTask; 2 leans on
  'QQmlDelegateModelGroupPrivate; 2 leans on 'QQmlDelegateModelAttached; 1
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 1 leans on 'non-virtual thunk to QQmlDelegateModelPrivate; 1 leans
  on 'QQmlPartsModel.

  What to expect
  --------------

  - The C++ QQmlDelegateModelPrivate is created at the first use, not by
    'QQmlDelegateModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelPrivate.
  - Each name of Qt's QQmlDelegateModelPrivate that has no cute function yet,
    '__init__', 'addCacheItem', 'addGroups', 'connectModel',
    'delegateChanged', 'emitChanges', 'emitDestroyingPackage',
    'emitInitPackage', 'group_append', 'group_at', 'group_count',
    'incubatorStatusChanged', 'insert', 'itemsChanged', 'itemsInserted',
    'itemsMoved', 'itemsRemoved', 'object', 'release', 'removeCacheItem',
    'removeGroups', 'reuseItem', 'setGroups', 'setInitialState',
    'updateFilterGroup', 'variantValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlDelegateModelPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class InsertionResult(CuteNum, scoped=True):
    """
    The enum 'QQmlDelegateModelPrivate::InsertionResult' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Success = Kee[int](0)
    Error = Kee[int](1)
    Retry = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlDelegateModel)
  @overload(NoneType)
  def get(
      m: Optional[QQmlDelegateModel],
  ) -> Optional[QQmlDelegateModelPrivate]:
    """
    Calls Qt's 'QQmlDelegateModelPrivate
    *QQmlDelegateModelPrivate::get(QQmlDelegateModel *m)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#get

    Parameters
    ----------

    m : Optional[QQmlDelegateModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlDelegateModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelPrivate
    #      *QQmlDelegateModelPrivate::get(QQmlDelegateModel *m)
    address = Rituals.call(
        'ritual_ZN24QQmlDelegateModelPrivate3getEP17QQmlDelegateModel',
        CuteMixin._addressOf(m),
    )
    return QQmlDelegateModelPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelPrivate'

  #  Qt's QQmlDelegateModelPrivate is built on more than one class. The part
  #  of a C++ QQmlDelegateModelPrivate that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlDelegateModelGroupEmitter':
          'ritual_cast_QQmlDelegateModelPrivate_QQmlDelegateModelGroupEmitter',
  }

  #  A C++ QQmlDelegateModelPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelegateModelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def adaptorModelCount(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelPrivate::adaptorModelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#adaptorModelCount
    """
    #  int QQmlDelegateModelPrivate::adaptorModelCount() const
    return self.uglySide.call(
        'ritual_ZNK24QQmlDelegateModelPrivate17adaptorModelCountEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModelPrivate::QQmlDelegateModelPrivate(QQmlContext
    *a0)': leans on 'non-virtual thunk to
    QQmlDelegateModelPrivate::emitModelUpdated(QQmlChangeSet const&, bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.__init__' has no cute function yet. Qt's "
        "'QQmlDelegateModelPrivate::QQmlDelegateModelPrivate(QQmlContext "
        "*a0)': leans on 'non-virtual thunk to "
        "QQmlDelegateModelPrivate::emitModelUpdated(QQmlChangeSet const&, "
        "bool)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QQmlDelegateModel]:
    """
    Calls Qt's 'QQmlDelegateModel *QQmlDelegateModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#q_func

    Returns
    -------

    Optional[QQmlDelegateModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModel *QQmlDelegateModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate6q_funcEv',
    )
    from . import QQmlDelegateModel
    return QQmlDelegateModel._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#init
    """
    #  void QQmlDelegateModelPrivate::init()
    self.uglySide.call('ritual_ZN24QQmlDelegateModelPrivate4initEv')

  def connectToAbstractItemModel(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelPrivate::connectToAbstractItemModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html
    """
    #  void QQmlDelegateModelPrivate::connectToAbstractItemModel()
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate26connectToAbstractItemModelEv',
    )

  def disconnectFromAbstractItemModel(self) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelPrivate::disconnectFromAbstractItemModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html
    """
    #  void QQmlDelegateModelPrivate::disconnectFromAbstractItemModel()
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate31disconnectFromAbstractItemMod'
        'elEv',
    )

  def requestMoreIfNecessary(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelPrivate::requestMoreIfNecessary()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html
    """
    #  void QQmlDelegateModelPrivate::requestMoreIfNecessary()
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate22requestMoreIfNecessaryEv',
    )

  @overload(QQDMIncubationTask, QQuickPackage)
  @overload(QQDMIncubationTask, NoneType)
  @overload(NoneType, QQuickPackage)
  @overload(NoneType, NoneType)
  def emitCreatedPackage(
      self,
      incubationTask: Optional[QQDMIncubationTask],
      package: Optional[QQuickPackage],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelPrivate::emitCreatedPackage(QQDMIncubationTask
    *incubationTask, QQuickPackage *package)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#emitCreatedPackage

    Parameters
    ----------

    incubationTask : Optional[QQDMIncubationTask]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    package : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelPrivate::emitCreatedPackage(QQDMIncubationTask
    #      *incubationTask, QQuickPackage *package)
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate18emitCreatedPackageEP18QQDMInc'
        'ubationTaskP13QQuickPackage',
        self._addressOf(incubationTask), self._addressOf(package),
    )

  @overload(QQDMIncubationTask, QObject)
  @overload(QQDMIncubationTask, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def emitCreatedItem(
      self,
      incubationTask: Optional[QQDMIncubationTask],
      item: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelPrivate::emitCreatedItem(QQDMIncubationTask
    *incubationTask, QObject *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#emitCreatedItem

    Parameters
    ----------

    incubationTask : Optional[QQDMIncubationTask]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelPrivate::emitCreatedItem(QQDMIncubationTask
    #      *incubationTask, QObject *item)
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate15emitCreatedItemEP18QQDMIncuba'
        'tionTaskP7QObject',
        self._addressOf(incubationTask), self._addressOf(item, 'QObject'),
    )

  @overload(QQDMIncubationTask, QObject)
  @overload(QQDMIncubationTask, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def emitInitItem(
      self,
      incubationTask: Optional[QQDMIncubationTask],
      item: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelPrivate::emitInitItem(QQDMIncubationTask
    *incubationTask, QObject *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#emitInitItem

    Parameters
    ----------

    incubationTask : Optional[QQDMIncubationTask]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelPrivate::emitInitItem(QQDMIncubationTask
    #      *incubationTask, QObject *item)
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate12emitInitItemEP18QQDMIncubatio'
        'nTaskP7QObject',
        self._addressOf(incubationTask), self._addressOf(item, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def emitDestroyingItem(self, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelPrivate::emitDestroyingItem(QObject
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#emitDestroyingItem

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelPrivate::emitDestroyingItem(QObject *item)
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate18emitDestroyingItemEP7QObject',
        self._addressOf(item, 'QObject'),
    )

  @overload(QQmlDelegateModelItem)
  @overload(NoneType)
  def destroyCacheItem(
      self,
      cacheItem: Optional[QQmlDelegateModelItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelPrivate::destroyCacheItem(QQmlDelegateModelItem
    *cacheItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#destroyCacheItem

    Parameters
    ----------

    cacheItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelPrivate::destroyCacheItem(QQmlDelegateModelItem
    #      *cacheItem)
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate16destroyCacheItemEP21QQmlDeleg'
        'ateModelItem',
        self._addressOf(cacheItem),
    )

  @overload(int)
  def drainReusableItemsPool(self, maxPoolTime: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelPrivate::drainReusableItemsPool(int
    maxPoolTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html

    Parameters
    ----------

    maxPoolTime : int
      Passed on as it is.
    """
    #  void QQmlDelegateModelPrivate::drainReusableItemsPool(int maxPoolTime)
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate22drainReusableItemsPoolEi',
        maxPoolTime,
    )

  @overload(int)
  def resolveDelegate(self, index: int) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlDelegateModelPrivate::resolveDelegate(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#resolveDelegate

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
    #  QQmlComponent *QQmlDelegateModelPrivate::resolveDelegate(int index)
    address = self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate15resolveDelegateEi', index,
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  @overload(QQmlChangeSet, bool)
  def emitModelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelPrivate::emitModelUpdated(const
    QQmlChangeSet &changeSet, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#emitModelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQmlDelegateModelPrivate::emitModelUpdated(const QQmlChangeSet
    #      &changeSet, bool reset)
    ritual = (
        'ritual_ZN24QQmlDelegateModelPrivate16emitModelUpdatedERK13QQmlChan'
        'geSetb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlDelegateModelPrivate16emitModelUpdatedERK13QQ'
          'mlChangeSetb')
    self.uglySide.call(ritual, self._valueOf(changeSet), reset)

  @overload(QQDMIncubationTask)
  @overload(NoneType)
  def releaseIncubator(
      self,
      incubationTask: Optional[QQDMIncubationTask],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelPrivate::releaseIncubator(QQDMIncubationTask
    *incubationTask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelprivate.html#releaseIncubator

    Parameters
    ----------

    incubationTask : Optional[QQDMIncubationTask]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelPrivate::releaseIncubator(QQDMIncubationTask
    #      *incubationTask)
    self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPrivate16releaseIncubatorEP18QQDMIncub'
        'ationTask',
        self._addressOf(incubationTask),
    )

  @staticmethod
  def addCacheItem(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::addCacheItem(QQmlDelegateModelItem
    *item, Compositor::iterator it)': leans on
    'QQmlListCompositor::setFlags(QQmlListCompositor::iterator, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Insert>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.addCacheItem' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelPrivate::addCacheItem(QQmlDelegateModelItem "
        "*item, Compositor::iterator it)': leans on "
        "'QQmlListCompositor::setFlags(QQmlListCompositor::iterator, int, "
        "QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Insert>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def addGroups(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::addGroups(Compositor::iterator from,
    int count, Compositor::Group group, int groupFlags)': leans on
    'QQmlListCompositor::setFlags(QQmlListCompositor::iterator, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Insert>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.addGroups' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelPrivate::addGroups(Compositor::iterator from, int "
        "count, Compositor::Group group, int groupFlags)': leans on "
        "'QQmlListCompositor::setFlags(QQmlListCompositor::iterator, int, "
        "QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Insert>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def connectModel(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::connectModel(QQmlAdaptorModel
    *model)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.connectModel' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelPrivate::connectModel(QQmlAdaptorModel "
        "*model)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def delegateChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::delegateChanged(bool add, bool
    remove)': leans on 'QQmlDelegateModelAttached::groupsChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.delegateChanged' has no cute function "
        "yet. Qt's 'void QQmlDelegateModelPrivate::delegateChanged(bool "
        "add, bool remove)': leans on "
        "'QQmlDelegateModelAttached::groupsChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def emitChanges(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::emitChanges()': leans on
    'QQmlDelegateModelAttached::groupsChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.emitChanges' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelPrivate::emitChanges()': leans on "
        "'QQmlDelegateModelAttached::groupsChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def emitDestroyingPackage(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::emitDestroyingPackage(QQuickPackage
    *package)': leans on
    'QQmlDelegateModelGroupPrivate::destroyingPackage(QQuickPackage*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.emitDestroyingPackage' has no cute "
        "function yet. Qt's 'void "
        "QQmlDelegateModelPrivate::emitDestroyingPackage(QQuickPackage "
        "*package)': leans on "
        "'QQmlDelegateModelGroupPrivate::destroyingPackage(QQuickPackage*)',"
        " which Qt's source does not mark for use from outside Qt and has "
        "no code for that could be taken.")

  @staticmethod
  def emitInitPackage(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::emitInitPackage(QQDMIncubationTask
    *incubationTask, QQuickPackage *package)': leans on
    'QQmlDelegateModelGroupPrivate::initPackage(int, QQuickPackage*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.emitInitPackage' has no cute function "
        "yet. Qt's 'void "
        "QQmlDelegateModelPrivate::emitInitPackage(QQDMIncubationTask "
        "*incubationTask, QQuickPackage *package)': leans on "
        "'QQmlDelegateModelGroupPrivate::initPackage(int, QQuickPackage*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def group_append(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::group_append(
    QQmlListProperty<QQmlDelegateModelGroup> *property,
    QQmlDelegateModelGroup *group)': names
    'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.group_append' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelPrivate::group_append(QQmlListProperty<QQmlDelegat"
        "eModelGroup> *property, QQmlDelegateModelGroup *group)': names "
        "'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute "
        "class yet.")

  @staticmethod
  def group_at(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModelGroup *QQmlDelegateModelPrivate::group_at(
    QQmlListProperty<QQmlDelegateModelGroup> *property, qsizetype index)':
    names 'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.group_at' has no cute function yet. Qt's "
        "'QQmlDelegateModelGroup "
        "*QQmlDelegateModelPrivate::group_at(QQmlListProperty<QQmlDelegateMo"
        "delGroup> *property, qsizetype index)': names "
        "'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute "
        "class yet.")

  @staticmethod
  def group_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQmlDelegateModelPrivate::group_count(
    QQmlListProperty<QQmlDelegateModelGroup> *property)': names
    'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.group_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQmlDelegateModelPrivate::group_count(QQmlListProperty<QQmlDelegate"
        "ModelGroup> *property)': names "
        "'QQmlListProperty<QQmlDelegateModelGroup>', which has no cute "
        "class yet.")

  @staticmethod
  def incubatorStatusChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDelegateModelPrivate::incubatorStatusChanged(QQDMIncubationTask
    *incubationTask, QQmlIncubator::Status status)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'isDoneIncubating'.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.incubatorStatusChanged' has no cute "
        "function yet. Qt's 'void "
        "QQmlDelegateModelPrivate::incubatorStatusChanged(QQDMIncubationTask"
        " *incubationTask, QQmlIncubator::Status status)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'isDoneIncubating'.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    Qt's 'InsertionResult
    QQmlDelegateModelPrivate::insert(Compositor::insert_iterator &before,
    const QV4::Value &object, int groups)': leans on
    'QQmlListCompositor::insert(QQmlListCompositor::iterator, void*, int,
    int, unsigned int, QList<QQmlListCompositor::Insert>*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.insert' has no cute function yet. Qt's "
        "'InsertionResult "
        "QQmlDelegateModelPrivate::insert(Compositor::insert_iterator "
        "&before, const QV4::Value &object, int groups)': leans on "
        "'QQmlListCompositor::insert(QQmlListCompositor::iterator, void*, "
        "int, int, unsigned int, QList<QQmlListCompositor::Insert>*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def itemsChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::itemsChanged(const
    QList<Compositor::Change> &changes)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.itemsChanged' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelPrivate::itemsChanged(const "
        "QList<Compositor::Change> &changes)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def itemsInserted(*__, **_) -> Never:
    """
    - Qt's 'void QQmlDelegateModelPrivate::itemsInserted(const
      QList<Compositor::Insert> &inserts)': takes a type Python has no way to
      hand over yet.
    - Qt's 'void QQmlDelegateModelPrivate::itemsInserted(const
      QList<Compositor::Insert> &inserts,
      QVarLengthArray<QList<QQmlChangeSet::Change>,
      Compositor::MaximumGroupCount> *translatedInserts, QHash<int,
      QList<QQmlDelegateModelItem *>> *movedItems)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'incrementIndexes'.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.itemsInserted' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelPrivate::itemsInserted(const "
        "QList<Compositor::Insert> &inserts)': takes a type Python has no "
        "way to hand over yet. Qt's 'void "
        "QQmlDelegateModelPrivate::itemsInserted(const "
        "QList<Compositor::Insert> &inserts, "
        "QVarLengthArray<QList<QQmlChangeSet::Change>, "
        "Compositor::MaximumGroupCount> *translatedInserts, QHash<int, "
        "QList<QQmlDelegateModelItem *>> *movedItems)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'incrementIndexes'.")

  @staticmethod
  def itemsMoved(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::itemsMoved(const
    QList<Compositor::Remove> &removes, const QList<Compositor::Insert>
    &inserts)': leans on
    'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.itemsMoved' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelPrivate::itemsMoved(const "
        "QList<Compositor::Remove> &removes, const "
        "QList<Compositor::Insert> &inserts)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def itemsRemoved(*__, **_) -> Never:
    """
    - Qt's 'void QQmlDelegateModelPrivate::itemsRemoved(const
      QList<Compositor::Remove> &removes,
      QVarLengthArray<QList<QQmlChangeSet::Change>,
      Compositor::MaximumGroupCount> *translatedRemoves, QHash<int,
      QList<QQmlDelegateModelItem *>> *movedItems)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'incrementIndexes'.
    - Qt's 'void QQmlDelegateModelPrivate::itemsRemoved(const
      QList<Compositor::Remove> &removes)': leans on
      'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
      QQmlListCompositor::Group, unsigned int,
      QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.itemsRemoved' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelPrivate::itemsRemoved(const "
        "QList<Compositor::Remove> &removes, "
        "QVarLengthArray<QList<QQmlChangeSet::Change>, "
        "Compositor::MaximumGroupCount> *translatedRemoves, QHash<int, "
        "QList<QQmlDelegateModelItem *>> *movedItems)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'incrementIndexes'. "
        "Qt's 'void QQmlDelegateModelPrivate::itemsRemoved(const "
        "QList<Compositor::Remove> &removes)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def object(*__, **_) -> Never:
    """
    Qt's 'QObject *QQmlDelegateModelPrivate::object(Compositor::Group group,
    int index, QQmlIncubator::IncubationMode incubationMode)': leans on
    'QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModelItem*,
    QObject*, QQmlDelegateModel::DelegateModelAccess)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.object' has no cute function yet. Qt's "
        "'QObject *QQmlDelegateModelPrivate::object(Compositor::Group "
        "group, int index, QQmlIncubator::IncubationMode incubationMode)': "
        "leans on "
        "'QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModel"
        "Item*, QObject*, QQmlDelegateModel::DelegateModelAccess)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModel::ReleaseFlags
    QQmlDelegateModelPrivate::release(QObject *object,
    QQmlInstanceModel::ReusableFlag reusable)': leans on
    'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.release' has no cute function yet. Qt's "
        "'QQmlDelegateModel::ReleaseFlags "
        "QQmlDelegateModelPrivate::release(QObject *object, "
        "QQmlInstanceModel::ReusableFlag reusable)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def removeCacheItem(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDelegateModelPrivate::removeCacheItem(QQmlDelegateModelItem
    *cacheItem)': leans on
    'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.removeCacheItem' has no cute function "
        "yet. Qt's 'void "
        "QQmlDelegateModelPrivate::removeCacheItem(QQmlDelegateModelItem "
        "*cacheItem)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def removeGroups(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::removeGroups(Compositor::iterator
    from, int count, Compositor::Group group, int groupFlags)': leans on
    'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.removeGroups' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelPrivate::removeGroups(Compositor::iterator from, "
        "int count, Compositor::Group group, int groupFlags)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def reuseItem(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::reuseItem(QQmlDelegateModelItem
    *item, int newModelIndex, int newGroups)': leans on
    'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.reuseItem' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelPrivate::reuseItem(QQmlDelegateModelItem *item, "
        "int newModelIndex, int newGroups)': leans on "
        "'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setGroups(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::setGroups(Compositor::iterator from,
    int count, Compositor::Group group, int groupFlags)': leans on
    'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
    QQmlListCompositor::Group, unsigned int,
    QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.setGroups' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelPrivate::setGroups(Compositor::iterator from, int "
        "count, Compositor::Group group, int groupFlags)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setInitialState(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::setInitialState(QQDMIncubationTask
    *incubationTask, QObject *o)': leans on
    'QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModelItem*,
    QObject*, QQmlDelegateModel::DelegateModelAccess)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.setInitialState' has no cute function "
        "yet. Qt's 'void "
        "QQmlDelegateModelPrivate::setInitialState(QQDMIncubationTask "
        "*incubationTask, QObject *o)': leans on "
        "'QQDMIncubationTask::initializeRequiredProperties(QQmlDelegateModel"
        "Item*, QObject*, QQmlDelegateModel::DelegateModelAccess)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def updateFilterGroup(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelPrivate::updateFilterGroup()': leans on
    'QQmlPartsModel::filterGroupChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.updateFilterGroup' has no cute function "
        "yet. Qt's 'void QQmlDelegateModelPrivate::updateFilterGroup()': "
        "leans on 'QQmlPartsModel::filterGroupChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def variantValue(*__, **_) -> Never:
    """
    Qt's 'QVariant QQmlDelegateModelPrivate::variantValue(Compositor::Group
    group, int index, const QString &name)': leans on
    'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPrivate.variantValue' has no cute function yet. "
        "Qt's 'QVariant "
        "QQmlDelegateModelPrivate::variantValue(Compositor::Group group, "
        "int index, const QString &name)': leans on "
        "'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
