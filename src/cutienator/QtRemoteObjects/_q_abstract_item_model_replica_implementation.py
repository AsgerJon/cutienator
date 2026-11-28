"""
QAbstractItemModelReplicaImplementation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstractItemModelReplicaImplementation to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QRemoteObjectReplica

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import CacheData, CacheEntry, QRemoteObjectPendingCallWatcher
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QRemoteObjectPendingCallWatcher = WAIT['QRemoteObjectPendingCallWatcher']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemModelReplicaImplementation(QRemoteObjectReplica):
  """
  The cute side of Qt's QAbstractItemModelReplicaImplementation: a plain
  Python object standing in front of one C++
  QAbstractItemModelReplicaImplementation.

  It is built on the cute 'QRemoteObjectReplica', as Qt's
  QAbstractItemModelReplicaImplementation is built on Qt's
  QRemoteObjectReplica, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemModelReplicaImplementation that has a
  ritual and that Python can call so far, 18 names in all: 'metaObject',
  'initialize', 'availableRolesChanged', 'modelReset', 'headerDataChanged',
  'onHeaderDataChanged', 'onModelReset', 'requestedData',
  'requestedHeaderData', 'init', 'fetchPendingData',
  'fetchPendingHeaderData', 'handleInitDone', 'handleModelResetDone',
  'handleSizeDone', 'onReplicaCurrentChanged', 'cacheData', 'cacheEntry'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractItemModelReplicaImplementation::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QAbstractItemModelReplicaImplementation::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractItemModelReplicaImplementation::
    ~QAbstractItemModelReplicaImplementation()': the destructor: Python never
    removes a C++ QAbstractItemModelReplicaImplementation.
  - Qt's 'const QList<int>
    &QAbstractItemModelReplicaImplementation::availableRoles() const': gives
    a type Python has no way to take yet.
  - Qt's 'bool QAbstractItemModelReplicaImplementation::clearCache(const
    QtPrivate::IndexList &start, const QtPrivate::IndexList &end, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::dataChanged(QtPrivate::IndexList
    topLeft, QtPrivate::IndexList bottomRight, QList<int> roles)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::rowsInserted(QtPrivate::
    IndexList parent, int first, int last)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::rowsRemoved(QtPrivate::IndexList
    parent, int first, int last)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::rowsMoved(QtPrivate::IndexList
    parent, int start, int end, QtPrivate::IndexList destination, int row)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::currentChanged(QtPrivate::
    IndexList current, QtPrivate::IndexList previous)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::columnsInserted(QtPrivate::
    IndexList parent, int first, int last)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::layoutChanged(QtPrivate::
    IndexList parents, QAbstractItemModel::LayoutChangeHint hint)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QAbstractItemModelReplicaImplementation::onDataChanged(const
    QtPrivate::IndexList &start, const QtPrivate::IndexList &end, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
  - Qt's 'void QAbstractItemModelReplicaImplementation::onRowsInserted(const
    QtPrivate::IndexList &parent, int start, int end)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QAbstractItemModelReplicaImplementation::onRowsRemoved(const
    QtPrivate::IndexList &parent, int start, int end)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::onColumnsInserted(const
    QtPrivate::IndexList &parent, int start, int end)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::onRowsMoved(QtPrivate::IndexList
    srcParent, int srcRow, int count, QtPrivate::IndexList destParent, int
    destRow)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelReplicaImplementation::onCurrentChanged(QtPrivate::
    IndexList current, QtPrivate::IndexList previous)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QAbstractItemModelReplicaImplementation::fillCache(const
    QtPrivate::IndexValuePair &pair, const QList<int> &roles)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QAbstractItemModelReplicaImplementation::onLayoutChanged(const
    QtPrivate::IndexList &parents, QAbstractItemModel::LayoutChangeHint
    hint)': takes a type Python has no way to hand over yet.
  - Qt's 'CacheData *QAbstractItemModelReplicaImplementation::cacheData(const
    QtPrivate::IndexList &index) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'CacheData
    *QAbstractItemModelReplicaImplementation::createCacheData(const
    QtPrivate::IndexList &index) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'CacheEntry
    *QAbstractItemModelReplicaImplementation::cacheEntry(const
    QtPrivate::IndexList &index) const': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  16 of the 57 functions Qt declares: 5 leans on
  'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray const&)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken; 4 leans on
  'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken; 3 leans on 'QAbstractItemModelReplicaImplementation; 2 not a gap;
  2 leans on 'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray
  const&)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken.

  What to expect
  --------------

  - The C++ QAbstractItemModelReplicaImplementation is created at the first
    use, not by 'QAbstractItemModelReplicaImplementation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemModelReplicaImplementation.
  - Qt tells when it has removed the C++
    QAbstractItemModelReplicaImplementation. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QAbstractItemModelReplicaImplementation that has no
    cute function yet, '__init__', 'availableRoles', 'clearCache',
    'columnsInserted', 'createCacheData', 'currentChanged', 'dataChanged',
    'doModelReset', 'fillCache', 'initializeModelConnections',
    'layoutChanged', 'onColumnsInserted', 'onCurrentChanged',
    'onDataChanged', 'onLayoutChanged', 'onRowsInserted', 'onRowsMoved',
    'onRowsRemoved', 'registerMetatypes', 'replicaCacheRequest',
    'replicaHeaderRequest', 'replicaRowRequest', 'replicaSetCurrentIndex',
    'replicaSetData', 'replicaSizeRequest', 'roleNames', 'rowsInserted',
    'rowsMoved', 'rowsRemoved', 'setModel', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemModelReplicaImplementation'

  #  A C++ QAbstractItemModelReplicaImplementation Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractItemModelReplicaImplementation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QAbstractItemModelReplicaImplementation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QAbstractItemModelReplicaImplementation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK39QAbstractItemModelReplicaImplementation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def cacheData(self, index: QModelIndex) -> Optional[CacheData]:
    """
    Calls Qt's 'CacheData
    *QAbstractItemModelReplicaImplementation::cacheData(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[CacheData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  CacheData *QAbstractItemModelReplicaImplementation::cacheData(const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK39QAbstractItemModelReplicaImplementation9cacheDataERK11'
        'QModelIndex',
        self._valueOf(index),
    )
    from . import CacheData
    return CacheData._cuteAt(address)

  @overload(QModelIndex)
  def cacheEntry(self, index: QModelIndex) -> Optional[CacheEntry]:
    """
    Calls Qt's 'CacheEntry
    *QAbstractItemModelReplicaImplementation::cacheEntry(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[CacheEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  CacheEntry *QAbstractItemModelReplicaImplementation::cacheEntry(const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK39QAbstractItemModelReplicaImplementation10cacheEntryERK'
        '11QModelIndex',
        self._valueOf(index),
    )
    from . import CacheEntry
    return CacheEntry._cuteAt(address)

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
    - Qt's 'QAbstractItemModelReplicaImplementation::
      QAbstractItemModelReplicaImplementation()': leans on
      'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'QAbstractItemModelReplicaImplementation::
      QAbstractItemModelReplicaImplementation(QRemoteObjectNode *node, const
      QString &name)': leans on
      'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.__init__' has no cute "
        "function yet. Qt's "
        "'QAbstractItemModelReplicaImplementation::QAbstractItemModelReplica"
        "Implementation()': leans on "
        "'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's "
        "'QAbstractItemModelReplicaImplementation::QAbstractItemModelReplica"
        "Implementation(QRemoteObjectNode *node, const QString &name)': "
        "leans on 'qRegisterNormalizedMetaType_QIntHash(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplicaImplementation::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html
    """
    #  void QAbstractItemModelReplicaImplementation::initialize()
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation10initializeEv',
    )

  def availableRolesChanged(self) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::availableRolesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html
    """
    #  void QAbstractItemModelReplicaImplementation::availableRolesChanged()
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation21availableRoles'
        'ChangedEv',
    )

  def modelReset(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplicaImplementation::modelReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html
    """
    #  void QAbstractItemModelReplicaImplementation::modelReset()
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation10modelResetEv',
    )

  @overload(Qt.Orientation, int, int)
  def headerDataChanged(self, a0: Qt.Orientation, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::headerDataChanged(Qt::
    Orientation a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QAbstractItemModelReplicaImplementation::headerDataChanged(Qt::
    #      Orientation a0, int a1, int a2)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation17headerDataChan'
        'gedEN2Qt11OrientationEii',
        a0.value, a1, a2,
    )

  @overload(Qt.Orientation, int, int)
  def onHeaderDataChanged(
      self,
      orientation: Qt.Orientation,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::onHeaderDataChanged(Qt::
    Orientation orientation, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelReplicaImplementation::onHeaderDataChanged(Qt::
    #      Orientation orientation, int first, int last)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation19onHeaderDataCh'
        'angedEN2Qt11OrientationEii',
        orientation.value, first, last,
    )

  def onModelReset(self) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::onModelReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html
    """
    #  void QAbstractItemModelReplicaImplementation::onModelReset()
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation12onModelResetEv',
    )

  @overload(QRemoteObjectPendingCallWatcher)
  @overload(NoneType)
  def requestedData(
      self,
      a0: Optional[QRemoteObjectPendingCallWatcher],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplicaImplementation::requestedData(
    QRemoteObjectPendingCallWatcher *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectPendingCallWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemModelReplicaImplementation::requestedData(
    #      QRemoteObjectPendingCallWatcher *a0)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation13requestedDataE'
        'P31QRemoteObjectPendingCallWatcher',
        self._addressOf(a0),
    )

  @overload(QRemoteObjectPendingCallWatcher)
  @overload(NoneType)
  def requestedHeaderData(
      self,
      a0: Optional[QRemoteObjectPendingCallWatcher],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::requestedHeaderData(
    QRemoteObjectPendingCallWatcher *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectPendingCallWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemModelReplicaImplementation::requestedHeaderData(
    #      QRemoteObjectPendingCallWatcher *a0)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation19requestedHeade'
        'rDataEP31QRemoteObjectPendingCallWatcher',
        self._addressOf(a0),
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplicaImplementation::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html#init
    """
    #  void QAbstractItemModelReplicaImplementation::init()
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation4initEv',
    )

  def fetchPendingData(self) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::fetchPendingData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html
    """
    #  void QAbstractItemModelReplicaImplementation::fetchPendingData()
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation16fetchPendingDa'
        'taEv',
    )

  def fetchPendingHeaderData(self) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::fetchPendingHeaderData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html
    """
    #  void QAbstractItemModelReplicaImplementation::fetchPendingHeaderData()
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation22fetchPendingHe'
        'aderDataEv',
    )

  @overload(QRemoteObjectPendingCallWatcher)
  @overload(NoneType)
  def handleInitDone(
      self,
      watcher: Optional[QRemoteObjectPendingCallWatcher],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplicaImplementation::handleInitDone(
    QRemoteObjectPendingCallWatcher *watcher)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    watcher : Optional[QRemoteObjectPendingCallWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemModelReplicaImplementation::handleInitDone(
    #      QRemoteObjectPendingCallWatcher *watcher)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation14handleInitDone'
        'EP31QRemoteObjectPendingCallWatcher',
        self._addressOf(watcher),
    )

  @overload(QRemoteObjectPendingCallWatcher)
  @overload(NoneType)
  def handleModelResetDone(
      self,
      watcher: Optional[QRemoteObjectPendingCallWatcher],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::handleModelResetDone(
    QRemoteObjectPendingCallWatcher *watcher)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    watcher : Optional[QRemoteObjectPendingCallWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemModelReplicaImplementation::handleModelResetDone(
    #      QRemoteObjectPendingCallWatcher *watcher)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation20handleModelRes'
        'etDoneEP31QRemoteObjectPendingCallWatcher',
        self._addressOf(watcher),
    )

  @overload(QRemoteObjectPendingCallWatcher)
  @overload(NoneType)
  def handleSizeDone(
      self,
      watcher: Optional[QRemoteObjectPendingCallWatcher],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplicaImplementation::handleSizeDone(
    QRemoteObjectPendingCallWatcher *watcher)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    watcher : Optional[QRemoteObjectPendingCallWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemModelReplicaImplementation::handleSizeDone(
    #      QRemoteObjectPendingCallWatcher *watcher)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation14handleSizeDone'
        'EP31QRemoteObjectPendingCallWatcher',
        self._addressOf(watcher),
    )

  @overload(QModelIndex, QModelIndex)
  def onReplicaCurrentChanged(
      self,
      current: QModelIndex,
      previous: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelReplicaImplementation::onReplicaCurrentChanged(const
    QModelIndex &current, const QModelIndex &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplicaimplementation.html

    Parameters
    ----------

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    previous : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemModelReplicaImplementation::onReplicaCurrentChanged(
    #      const QModelIndex &current, const QModelIndex &previous)
    self.uglySide.call(
        'ritual_ZN39QAbstractItemModelReplicaImplementation23onReplicaCurre'
        'ntChangedERK11QModelIndexS2_',
        self._valueOf(current), self._valueOf(previous),
    )

  @staticmethod
  def availableRoles(*__, **_) -> Never:
    """
    Qt's 'const QList<int>
    &QAbstractItemModelReplicaImplementation::availableRoles() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.availableRoles' has no "
        "cute function yet. Qt's 'const QList<int> "
        "&QAbstractItemModelReplicaImplementation::availableRoles() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def clearCache(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractItemModelReplicaImplementation::clearCache(const
    QtPrivate::IndexList &start, const QtPrivate::IndexList &end, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.clearCache' has no cute "
        "function yet. Qt's 'bool "
        "QAbstractItemModelReplicaImplementation::clearCache(const "
        "QtPrivate::IndexList &start, const QtPrivate::IndexList &end, "
        "const QList<int> &roles)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def columnsInserted(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::columnsInserted(QtPrivate::
    IndexList parent, int first, int last)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.columnsInserted' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::columnsInserted(QtPrivate:"
        ":IndexList parent, int first, int last)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def createCacheData(*__, **_) -> Never:
    """
    Qt's 'CacheData
    *QAbstractItemModelReplicaImplementation::createCacheData(const
    QtPrivate::IndexList &index) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.createCacheData' has no "
        "cute function yet. Qt's 'CacheData "
        "*QAbstractItemModelReplicaImplementation::createCacheData(const "
        "QtPrivate::IndexList &index) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def currentChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::currentChanged(QtPrivate::
    IndexList current, QtPrivate::IndexList previous)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.currentChanged' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::currentChanged(QtPrivate::"
        "IndexList current, QtPrivate::IndexList previous)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::dataChanged(QtPrivate::IndexList
    topLeft, QtPrivate::IndexList bottomRight, QList<int> roles)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.dataChanged' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::dataChanged(QtPrivate::Ind"
        "exList topLeft, QtPrivate::IndexList bottomRight, QList<int> "
        "roles)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def doModelReset(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectPendingCallWatcher
    *QAbstractItemModelReplicaImplementation::doModelReset()': leans on
    'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.doModelReset' has no cute "
        "function yet. Qt's 'QRemoteObjectPendingCallWatcher "
        "*QAbstractItemModelReplicaImplementation::doModelReset()': leans "
        "on 'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def fillCache(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelReplicaImplementation::fillCache(const
    QtPrivate::IndexValuePair &pair, const QList<int> &roles)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.fillCache' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::fillCache(const "
        "QtPrivate::IndexValuePair &pair, const QList<int> &roles)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def initializeModelConnections(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::initializeModelConnections()':
    leans on 'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.initializeModelConnections"
        "' has no cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::initializeModelConnections"
        "()': leans on "
        "'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def layoutChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::layoutChanged(QtPrivate::
    IndexList parents, QAbstractItemModel::LayoutChangeHint hint)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.layoutChanged' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::layoutChanged(QtPrivate::I"
        "ndexList parents, QAbstractItemModel::LayoutChangeHint hint)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def onColumnsInserted(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::onColumnsInserted(const
    QtPrivate::IndexList &parent, int start, int end)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.onColumnsInserted' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::onColumnsInserted(const "
        "QtPrivate::IndexList &parent, int start, int end)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def onCurrentChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::onCurrentChanged(QtPrivate::
    IndexList current, QtPrivate::IndexList previous)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.onCurrentChanged' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::onCurrentChanged(QtPrivate"
        "::IndexList current, QtPrivate::IndexList previous)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def onDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelReplicaImplementation::onDataChanged(const
    QtPrivate::IndexList &start, const QtPrivate::IndexList &end, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.onDataChanged' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::onDataChanged(const "
        "QtPrivate::IndexList &start, const QtPrivate::IndexList &end, "
        "const QList<int> &roles)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def onLayoutChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelReplicaImplementation::onLayoutChanged(const
    QtPrivate::IndexList &parents, QAbstractItemModel::LayoutChangeHint
    hint)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.onLayoutChanged' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::onLayoutChanged(const "
        "QtPrivate::IndexList &parents, "
        "QAbstractItemModel::LayoutChangeHint hint)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def onRowsInserted(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelReplicaImplementation::onRowsInserted(const
    QtPrivate::IndexList &parent, int start, int end)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.onRowsInserted' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::onRowsInserted(const "
        "QtPrivate::IndexList &parent, int start, int end)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def onRowsMoved(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::onRowsMoved(QtPrivate::IndexList
    srcParent, int srcRow, int count, QtPrivate::IndexList destParent, int
    destRow)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.onRowsMoved' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::onRowsMoved(QtPrivate::Ind"
        "exList srcParent, int srcRow, int count, QtPrivate::IndexList "
        "destParent, int destRow)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def onRowsRemoved(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelReplicaImplementation::onRowsRemoved(const
    QtPrivate::IndexList &parent, int start, int end)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.onRowsRemoved' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::onRowsRemoved(const "
        "QtPrivate::IndexList &parent, int start, int end)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def registerMetatypes(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelReplicaImplementation::registerMetatypes()':
    leans on 'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.registerMetatypes' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::registerMetatypes()': "
        "leans on 'qRegisterNormalizedMetaType_QIntHash(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def replicaCacheRequest(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectPendingReply<QtPrivate::MetaAndDataEntries>
    QAbstractItemModelReplicaImplementation::replicaCacheRequest(size_t size,
    QList<int> roles)': leans on
    'QAbstractItemModelReplicaImplementation::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.replicaCacheRequest' has "
        "no cute function yet. Qt's "
        "'QRemoteObjectPendingReply<QtPrivate::MetaAndDataEntries> "
        "QAbstractItemModelReplicaImplementation::replicaCacheRequest(size_t"
        " size, QList<int> roles)': leans on "
        "'QAbstractItemModelReplicaImplementation::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def replicaHeaderRequest(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectPendingReply<QVariantList>
    QAbstractItemModelReplicaImplementation::replicaHeaderRequest(QList<Qt::
    Orientation> orientations, QList<int> sections, QList<int> roles)': leans
    on 'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.replicaHeaderRequest' has "
        "no cute function yet. Qt's "
        "'QRemoteObjectPendingReply<QVariantList> "
        "QAbstractItemModelReplicaImplementation::replicaHeaderRequest(QList"
        "<Qt::Orientation> orientations, QList<int> sections, QList<int> "
        "roles)': leans on "
        "'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def replicaRowRequest(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectPendingReply<QtPrivate::DataEntries>
    QAbstractItemModelReplicaImplementation::replicaRowRequest(QtPrivate::
    IndexList start, QtPrivate::IndexList end, QList<int> roles)': leans on
    'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.replicaRowRequest' has no "
        "cute function yet. Qt's "
        "'QRemoteObjectPendingReply<QtPrivate::DataEntries> "
        "QAbstractItemModelReplicaImplementation::replicaRowRequest(QtPrivat"
        "e::IndexList start, QtPrivate::IndexList end, QList<int> roles)': "
        "leans on "
        "'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def replicaSetCurrentIndex(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::replicaSetCurrentIndex(
    QtPrivate::IndexList index, QItemSelectionModel::SelectionFlags
    command)': leans on
    'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.replicaSetCurrentIndex' "
        "has no cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::replicaSetCurrentIndex(QtP"
        "rivate::IndexList index, QItemSelectionModel::SelectionFlags "
        "command)': leans on "
        "'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def replicaSetData(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::replicaSetData(QtPrivate::
    IndexList index, const QVariant &value, int role)': leans on
    'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.replicaSetData' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::replicaSetData(QtPrivate::"
        "IndexList index, const QVariant &value, int role)': leans on "
        "'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def replicaSizeRequest(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectPendingReply<QSize>
    QAbstractItemModelReplicaImplementation::replicaSizeRequest(QtPrivate::
    IndexList parentList)': leans on
    'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.replicaSizeRequest' has "
        "no cute function yet. Qt's 'QRemoteObjectPendingReply<QSize> "
        "QAbstractItemModelReplicaImplementation::replicaSizeRequest(QtPriva"
        "te::IndexList parentList)': leans on "
        "'qRegisterNormalizedMetaType_QtPrivate__IndexList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def roleNames(*__, **_) -> Never:
    """
    Qt's 'QHash<int, QByteArray>
    QAbstractItemModelReplicaImplementation::roleNames() const': leans on
    'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.roleNames' has no cute "
        "function yet. Qt's 'QHash<int, QByteArray> "
        "QAbstractItemModelReplicaImplementation::roleNames() const': leans "
        "on 'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def rowsInserted(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::rowsInserted(QtPrivate::
    IndexList parent, int first, int last)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.rowsInserted' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::rowsInserted(QtPrivate::In"
        "dexList parent, int first, int last)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def rowsMoved(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::rowsMoved(QtPrivate::IndexList
    parent, int start, int end, QtPrivate::IndexList destination, int row)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.rowsMoved' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::rowsMoved(QtPrivate::Index"
        "List parent, int start, int end, QtPrivate::IndexList destination, "
        "int row)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def rowsRemoved(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelReplicaImplementation::rowsRemoved(QtPrivate::IndexList
    parent, int first, int last)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.rowsRemoved' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::rowsRemoved(QtPrivate::Ind"
        "exList parent, int first, int last)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def setModel(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelReplicaImplementation::setModel(
    QAbstractItemModelReplica *model)': leans on
    'QAbstractItemModelReplicaImplementation::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplicaImplementation.setModel' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelReplicaImplementation::setModel(QAbstractItemMode"
        "lReplica *model)': leans on "
        "'QAbstractItemModelReplicaImplementation::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
