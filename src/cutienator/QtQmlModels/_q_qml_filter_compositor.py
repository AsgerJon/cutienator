"""
QQmlFilterCompositor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfiltercompositor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlFilterCompositor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQmlFilterBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QQmlFilterBasePrivate, QQmlFilterCompositorPrivate
  from . import QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQmlFilterBasePrivate = WAIT['QQmlFilterBasePrivate']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlFilterCompositor(QQmlFilterBase):
  """
  The cute side of Qt's QQmlFilterCompositor: a plain Python object standing
  in front of one C++ QQmlFilterCompositor.

  It is built on the cute 'QQmlFilterBase', as Qt's QQmlFilterCompositor is
  built on Qt's QQmlFilterBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlFilterCompositor that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'filters',
  'filterAcceptsRowInternal', 'filterAcceptsColumnInternal', 'updateFilters',
  'append', 'count', 'at', 'clear', 'refreshCache', 'd_func'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlFilterCompositor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlFilterCompositor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlFilterCompositor::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'QQmlListProperty<QQmlFilterBase>
    QQmlFilterCompositor::filtersListProperty()': gives a type Python has no
    way to take yet.
  - Qt's 'void QQmlFilterCompositor::append(QQmlListProperty<QQmlFilterBase>
    *filterComp, QQmlFilterBase *filter)': names
    'QQmlListProperty<QQmlFilterBase>', which has no cute class yet.
  - Qt's 'qsizetype
    QQmlFilterCompositor::count(QQmlListProperty<QQmlFilterBase>
    *filterComp)': names 'QQmlListProperty<QQmlFilterBase>', which has no
    cute class yet.
  - Qt's 'QQmlFilterBase
    *QQmlFilterCompositor::at(QQmlListProperty<QQmlFilterBase> *filterComp,
    qsizetype index)': names 'QQmlListProperty<QQmlFilterBase>', which has no
    cute class yet.
  - Qt's 'void QQmlFilterCompositor::clear(QQmlListProperty<QQmlFilterBase>
    *filterComp)': names 'QQmlListProperty<QQmlFilterBase>', which has no
    cute class yet.
  - Qt's 'const QQmlFilterCompositorPrivate *QQmlFilterCompositor::d_func()
    const': takes in Python what 'QQmlFilterCompositorPrivate
    *QQmlFilterCompositor::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlFilterCompositor is created at the first use, not by
    'QQmlFilterCompositor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlFilterCompositor.
  - Qt tells when it has removed the C++ QQmlFilterCompositor. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlFilterCompositor that has no cute function yet,
    'filtersListProperty', holds a function that raises
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
    Calls Qt's 'QString QQmlFilterCompositor::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfiltercompositor.html#tr

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
    #  QString QQmlFilterCompositor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQmlFilterCompositor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFilterCompositor'

  #  The functions Qt calls itself that QQmlFilterCompositor is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'refreshCache': (
          ('_ZN20QQmlFilterCompositor12refreshCacheEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlFilterCompositor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfiltercompositor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlFilterCompositor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlFilterCompositor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsRowInternal(
      self,
      a0: int,
      a1: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlFilterCompositor::filterAcceptsRowInternal(int a0,
    const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfiltercompositor.html#filterAcceptsRowInternal

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlFilterCompositor::filterAcceptsRowInternal(int a0, const
    #      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK20QQmlFilterCompositor24filterAcceptsRowInternalEiRK11QM'
        'odelIndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQmlFilterCompositor24filterAcceptsRowInternalEi'
          'RK11QModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual, a0, self._valueOf(a1), self._addressOf(a2),
    )

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsColumnInternal(
      self,
      a0: int,
      a1: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlFilterCompositor::filterAcceptsColumnInternal(int
    a0, const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfiltercompositor.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlFilterCompositor::filterAcceptsColumnInternal(int a0, const
    #      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK20QQmlFilterCompositor27filterAcceptsColumnInternalEiRK1'
        '1QModelIndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQmlFilterCompositor27filterAcceptsColumnInterna'
          'lEiRK11QModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual, a0, self._valueOf(a1), self._addressOf(a2),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlFilterCompositor::QQmlFilterCompositor(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfiltercompositor.html#QQmlFilterCompositor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlFilterCompositor::QQmlFilterCompositor(QObject *parent)
    self._noteCreation(QQmlFilterCompositor, lambda: Rituals.call(
        'ritual_ZN20QQmlFilterCompositorC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlFilterBasePrivate, QObject)
  @overload(QQmlFilterBasePrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      priv: Optional[QQmlFilterBasePrivate],
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlFilterCompositor::QQmlFilterCompositor(QQmlFilterBasePrivate *priv,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfiltercompositor.html#QQmlFilterCompositor

    Parameters
    ----------

    priv : Optional[QQmlFilterBasePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlFilterCompositor::QQmlFilterCompositor(QQmlFilterBasePrivate
    #      *priv, QObject *parent)
    self._noteCreation(QQmlFilterCompositor, lambda: Rituals.call(
        'ritual_ZN20QQmlFilterCompositorC1EP21QQmlFilterBasePrivateP7QObjec'
        't',
        self._addressOf(priv), self._addressOf(parent, 'QObject'),
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

  def filters(self) -> QList[QQmlFilterBase]:
    """
    Calls Qt's 'QList<QQmlFilterBase *> QQmlFilterCompositor::filters()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfiltercompositor.html#filters

    Returns
    -------

    QList[QQmlFilterBase]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlFilterBase *> QQmlFilterCompositor::filters()
    address = self.uglySide.call('ritual_ZN20QQmlFilterCompositor7filtersEv')
    return QList[QQmlFilterBase]._cuteOwning(address)

  def updateFilters(self) -> None:
    """
    Calls Qt's 'void QQmlFilterCompositor::updateFilters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfiltercompositor.html#updateFilters
    """
    #  void QQmlFilterCompositor::updateFilters()
    self.uglySide.call('ritual_ZN20QQmlFilterCompositor13updateFiltersEv')

  @overload(QQmlFilterBase)
  @overload(NoneType)
  def append(self, a0: Optional[QQmlFilterBase]) -> None:
    """
    Calls Qt's 'void QQmlFilterCompositor::append(QQmlFilterBase *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfiltercompositor.html#append

    Parameters
    ----------

    a0 : Optional[QQmlFilterBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlFilterCompositor::append(QQmlFilterBase *a0)
    self.uglySide.call(
        'ritual_ZN20QQmlFilterCompositor6appendEP14QQmlFilterBase',
        self._addressOf(a0),
    )

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlFilterCompositor::count()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfiltercompositor.html#count
    """
    #  qsizetype QQmlFilterCompositor::count()
    return self.uglySide.call('ritual_ZN20QQmlFilterCompositor5countEv')

  @overload(int)
  def at(self, a0: int) -> Optional[QQmlFilterBase]:
    """
    Calls Qt's 'QQmlFilterBase *QQmlFilterCompositor::at(qsizetype a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfiltercompositor.html#at

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlFilterBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFilterBase *QQmlFilterCompositor::at(qsizetype a0)
    address = self.uglySide.call('ritual_ZN20QQmlFilterCompositor2atEx', a0)
    return QQmlFilterBase._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlFilterCompositor::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfiltercompositor.html#clear
    """
    #  void QQmlFilterCompositor::clear()
    self.uglySide.call('ritual_ZN20QQmlFilterCompositor5clearEv')

  def refreshCache(self) -> None:
    """
    Calls Qt's 'void QQmlFilterCompositor::refreshCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfiltercompositor.html#refreshCache
    """
    #  void QQmlFilterCompositor::refreshCache()
    ritual = 'ritual_ZN20QQmlFilterCompositor12refreshCacheEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlFilterCompositor12refreshCacheEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQmlFilterCompositorPrivate]:
    """
    Calls Qt's 'QQmlFilterCompositorPrivate *QQmlFilterCompositor::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfiltercompositor.html#d_func

    Returns
    -------

    Optional[QQmlFilterCompositorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFilterCompositorPrivate *QQmlFilterCompositor::d_func()
    address = self.uglySide.call('ritual_ZN20QQmlFilterCompositor6d_funcEv')
    from . import QQmlFilterCompositorPrivate
    return QQmlFilterCompositorPrivate._cuteAt(address)

  @staticmethod
  def filtersListProperty(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlFilterBase>
    QQmlFilterCompositor::filtersListProperty()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlFilterCompositor.filtersListProperty' has no cute function "
        "yet. Qt's 'QQmlListProperty<QQmlFilterBase> "
        "QQmlFilterCompositor::filtersListProperty()': gives a type Python "
        "has no way to take yet.")
