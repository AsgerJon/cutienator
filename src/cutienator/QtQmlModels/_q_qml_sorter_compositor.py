"""
QQmlSorterCompositor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortercompositor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlSorterCompositor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex, QPartialOrdering
  from . import QQmlSortFilterProxyModel, QQmlSorterCompositorPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlSorterCompositor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSorterCompositor: a plain Python object standing
  in front of one C++ QQmlSorterCompositor.

  What exists
  -----------

  Every function of Qt's QQmlSorterCompositor that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'compare',
  'lessThan', 'updateSorters', 'updateEffectiveSorters', 'count', 'clear',
  'updateCache', 'd_func'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlSorterCompositor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlSorterCompositor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlSorterCompositor::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'QQmlSorterCompositor::~QQmlSorterCompositor()': the destructor:
    Python never removes a C++ QQmlSorterCompositor.
  - Qt's 'QList<QQmlSorterBase *> QQmlSorterCompositor::sorters()': gives a
    list of 'QQmlSorterBase', which has no cute class yet.
  - Qt's 'qsizetype
    QQmlSorterCompositor::count(QQmlListProperty<QQmlSorterBase>
    *sorterComp)': names 'QQmlListProperty<QQmlSorterBase>', which has no
    cute class yet.
  - Qt's 'QQmlSorterBase
    *QQmlSorterCompositor::at(QQmlListProperty<QQmlSorterBase> *sorterComp,
    qsizetype index)': names 'QQmlListProperty<QQmlSorterBase>', which has no
    cute class yet.
  - Qt's 'void QQmlSorterCompositor::clear(QQmlListProperty<QQmlSorterBase>
    *sorterComp)': names 'QQmlListProperty<QQmlSorterBase>', which has no
    cute class yet.
  - Qt's 'QQmlSorterBase *QQmlSorterCompositor::at(qsizetype index)': gives
    'QQmlSorterBase', which has no cute class yet.
  - Qt's 'const QQmlSorterCompositorPrivate *QQmlSorterCompositor::d_func()
    const': takes in Python what 'QQmlSorterCompositorPrivate
    *QQmlSorterCompositor::d_func()' takes.

  What has no ritual
  ------------------

  7 of the 26 functions Qt declares: 5 leans on 'QQmlSorterCompositor; 2 not
  a gap.

  What to expect
  --------------

  - The C++ QQmlSorterCompositor is created at the first use, not by
    'QQmlSorterCompositor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSorterCompositor.
  - Qt tells when it has removed the C++ QQmlSorterCompositor. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlSorterCompositor that has no cute function yet,
    '__init__', 'append', 'at', 'sorters', 'sortersListProperty', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSorterCompositor'

  #  A C++ QQmlSorterCompositor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSorterCompositor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlSorterCompositor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortercompositor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlSorterCompositor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlSorterCompositor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex, QModelIndex, QQmlSortFilterProxyModel)
  @overload(QModelIndex, QModelIndex, NoneType)
  def compare(
      self,
      a0: QModelIndex,
      a1: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> QPartialOrdering:
    """
    Calls Qt's 'QPartialOrdering QQmlSorterCompositor::compare(const
    QModelIndex &a0, const QModelIndex &a1, const QQmlSortFilterProxyModel
    *a2) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortercompositor.html#compare

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPartialOrdering
      A new cute QPartialOrdering around the copy Qt gave back. Python owns
      it.
    """
    #  QPartialOrdering QQmlSorterCompositor::compare(const QModelIndex &a0,
    #      const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK20QQmlSorterCompositor7compareERK11QModelIndexS2_PK24QQm'
        'lSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQmlSorterCompositor7compareERK11QModelIndexS2_P'
          'K24QQmlSortFilterProxyModel')
    address = self.uglySide.call(
        ritual, self._valueOf(a0), self._valueOf(a1), self._addressOf(a2),
    )
    from ..QtCore import QPartialOrdering
    return QPartialOrdering._cuteOwning(address)

  @overload(QModelIndex, QModelIndex, QQmlSortFilterProxyModel)
  @overload(QModelIndex, QModelIndex, NoneType)
  def lessThan(
      self,
      sourceLeft: QModelIndex,
      sourceRight: QModelIndex,
      proxyModel: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSorterCompositor::lessThan(const QModelIndex
    &sourceLeft, const QModelIndex &sourceRight, const
    QQmlSortFilterProxyModel *proxyModel) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortercompositor.html#lessThan

    Parameters
    ----------

    sourceLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    proxyModel : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlSorterCompositor::lessThan(const QModelIndex &sourceLeft,
    #      const QModelIndex &sourceRight, const QQmlSortFilterProxyModel
    #      *proxyModel) const
    return self.uglySide.call(
        'ritual_ZNK20QQmlSorterCompositor8lessThanERK11QModelIndexS2_PK24QQ'
        'mlSortFilterProxyModel',
        self._valueOf(sourceLeft), self._valueOf(sourceRight),
        self._addressOf(proxyModel),
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
    Qt's 'QQmlSorterCompositor::QQmlSorterCompositor(QObject *parent)': leans
    on 'QQmlSorterCompositor::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlSorterCompositor.__init__' has no cute function yet. Qt's "
        "'QQmlSorterCompositor::QQmlSorterCompositor(QObject *parent)': "
        "leans on 'QQmlSorterCompositor::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def updateSorters(self) -> None:
    """
    Calls Qt's 'void QQmlSorterCompositor::updateSorters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortercompositor.html#updateSorters
    """
    #  void QQmlSorterCompositor::updateSorters()
    self.uglySide.call('ritual_ZN20QQmlSorterCompositor13updateSortersEv')

  def updateEffectiveSorters(self) -> None:
    """
    Calls Qt's 'void QQmlSorterCompositor::updateEffectiveSorters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortercompositor.html#updateEffectiveSorters
    """
    #  void QQmlSorterCompositor::updateEffectiveSorters()
    self.uglySide.call(
        'ritual_ZN20QQmlSorterCompositor22updateEffectiveSortersEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlSorterCompositor::count()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortercompositor.html#count
    """
    #  qsizetype QQmlSorterCompositor::count()
    return self.uglySide.call('ritual_ZN20QQmlSorterCompositor5countEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlSorterCompositor::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortercompositor.html#clear
    """
    #  void QQmlSorterCompositor::clear()
    self.uglySide.call('ritual_ZN20QQmlSorterCompositor5clearEv')

  def updateCache(self) -> None:
    """
    Calls Qt's 'void QQmlSorterCompositor::updateCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortercompositor.html#updateCache
    """
    #  void QQmlSorterCompositor::updateCache()
    self.uglySide.call('ritual_ZN20QQmlSorterCompositor11updateCacheEv')

  def d_func(self) -> Optional[QQmlSorterCompositorPrivate]:
    """
    Calls Qt's 'QQmlSorterCompositorPrivate *QQmlSorterCompositor::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortercompositor.html#d_func

    Returns
    -------

    Optional[QQmlSorterCompositorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlSorterCompositorPrivate *QQmlSorterCompositor::d_func()
    address = self.uglySide.call('ritual_ZN20QQmlSorterCompositor6d_funcEv')
    from . import QQmlSorterCompositorPrivate
    return QQmlSorterCompositorPrivate._cuteAt(address)

  @staticmethod
  def append(*__, **_) -> Never:
    """
    - Qt's 'void
      QQmlSorterCompositor::append(QQmlListProperty<QQmlSorterBase>
      *sorterComp, QQmlSorterBase *sorter)': leans on
      'QQmlSorterCompositor::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    - Qt's 'void QQmlSorterCompositor::append(QQmlSorterBase *sorter)': leans
      on 'QQmlSorterCompositor::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlSorterCompositor.append' has no cute function yet. Qt's 'void "
        "QQmlSorterCompositor::append(QQmlListProperty<QQmlSorterBase> "
        "*sorterComp, QQmlSorterBase *sorter)': leans on "
        "'QQmlSorterCompositor::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QQmlSorterCompositor::append(QQmlSorterBase "
        "*sorter)': leans on 'QQmlSorterCompositor::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def at(*__, **_) -> Never:
    """
    - Qt's 'QQmlSorterBase
      *QQmlSorterCompositor::at(QQmlListProperty<QQmlSorterBase> *sorterComp,
      qsizetype index)': names 'QQmlListProperty<QQmlSorterBase>', which has
      no cute class yet.
    - Qt's 'QQmlSorterBase *QQmlSorterCompositor::at(qsizetype index)': gives
      'QQmlSorterBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlSorterCompositor.at' has no cute function yet. Qt's "
        "'QQmlSorterBase "
        "*QQmlSorterCompositor::at(QQmlListProperty<QQmlSorterBase> "
        "*sorterComp, qsizetype index)': names "
        "'QQmlListProperty<QQmlSorterBase>', which has no cute class yet. "
        "Qt's 'QQmlSorterBase *QQmlSorterCompositor::at(qsizetype index)': "
        "gives 'QQmlSorterBase', which has no cute class yet.")

  @staticmethod
  def sorters(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlSorterBase *> QQmlSorterCompositor::sorters()': gives a
    list of 'QQmlSorterBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlSorterCompositor.sorters' has no cute function yet. Qt's "
        "'QList<QQmlSorterBase *> QQmlSorterCompositor::sorters()': gives a "
        "list of 'QQmlSorterBase', which has no cute class yet.")

  @staticmethod
  def sortersListProperty(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlSorterBase>
    QQmlSorterCompositor::sortersListProperty()': leans on
    'QQmlSorterCompositor::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlSorterCompositor.sortersListProperty' has no cute function "
        "yet. Qt's 'QQmlListProperty<QQmlSorterBase> "
        "QQmlSorterCompositor::sortersListProperty()': leans on "
        "'QQmlSorterCompositor::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
