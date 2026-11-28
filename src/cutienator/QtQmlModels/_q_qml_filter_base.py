"""
QQmlFilterBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfilterbase_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlFilterBase to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QQmlFilterBasePrivate, QQmlSortFilterProxyModel
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


class QQmlFilterBase(QObject):
  """
  The cute side of Qt's QQmlFilterBase: a plain Python object standing in
  front of one C++ QQmlFilterBase.

  It is built on the cute 'QObject', as Qt's QQmlFilterBase is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlFilterBase that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'enabled', 'setEnabled',
  'isInverted', 'setInverted', 'column', 'setColumn',
  'filterAcceptsRowInternal', 'filterAcceptsColumnInternal', 'update',
  'supportColumnFiltering', 'isActive', 'invalidateModel', 'invalidateCache',
  'enabledChanged', 'invertedChanged', 'columnChanged', 'invalidate',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlFilterBase::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlFilterBase::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlFilterBase::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'const QQmlFilterBasePrivate *QQmlFilterBase::d_func() const': takes
    in Python what 'QQmlFilterBasePrivate *QQmlFilterBase::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlFilterBase is created at the first use, not by
    'QQmlFilterBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlFilterBase.
  - Qt tells when it has removed the C++ QQmlFilterBase. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlFilterBase::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#tr

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
    #  QString QQmlFilterBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQmlFilterBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFilterBase'

  #  The functions Qt calls itself that QQmlFilterBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'column': (
          ('_ZNK14QQmlFilterBase6columnEv',
           ('int', 'number', ''),
           ()),
      ),
      'setColumn': (
          ('_ZN14QQmlFilterBase9setColumnEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'filterAcceptsRowInternal': (
          ('_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QModelIndex'
           'PK24QQmlSortFilterProxyModel',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'address',
                'QtQmlModels:QQmlSortFilterProxyModel'),
           )),
      ),
      'filterAcceptsColumnInternal': (
          ('_ZNK14QQmlFilterBase27filterAcceptsColumnInternalEiRK11QModelIn'
           'dexPK24QQmlSortFilterProxyModel',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'address',
                'QtQmlModels:QQmlSortFilterProxyModel'),
           )),
      ),
      'update': (
          ('_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyModel',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQmlModels:QQmlSortFilterProxyModel'),
           )),
      ),
      'supportColumnFiltering': (
          ('_ZNK14QQmlFilterBase22supportColumnFilteringEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isActive': (
          ('_ZNK14QQmlFilterBase8isActiveEv',
           ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QQmlFilterBase::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlFilterBase::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlFilterBase10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQmlFilterBase::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#enabled
    """
    #  bool QQmlFilterBase::enabled() const
    return self.uglySide.call('ritual_ZNK14QQmlFilterBase7enabledEv')

  def isInverted(self) -> bool:
    """
    Calls Qt's 'bool QQmlFilterBase::isInverted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#isInverted
    """
    #  bool QQmlFilterBase::isInverted() const
    return self.uglySide.call('ritual_ZNK14QQmlFilterBase10isInvertedEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QQmlFilterBase::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#column
    """
    #  int QQmlFilterBase::column() const
    ritual = 'ritual_ZNK14QQmlFilterBase6columnEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlFilterBase6columnEv'
    return self.uglySide.call(ritual)

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsRowInternal(
      self,
      a0: int,
      a1: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlFilterBase::filterAcceptsRowInternal(int a0, const
    QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfilterbase.html#filterAcceptsRowInternal

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
    #  bool QQmlFilterBase::filterAcceptsRowInternal(int a0, const
    #      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QModelIn'
        'dexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QM'
          'odelIndexPK24QQmlSortFilterProxyModel')
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
    Calls Qt's 'bool QQmlFilterBase::filterAcceptsColumnInternal(int a0,
    const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfilterbase.html#filterAcceptsColumnInternal

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
    #  bool QQmlFilterBase::filterAcceptsColumnInternal(int a0, const
    #      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK14QQmlFilterBase27filterAcceptsColumnInternalEiRK11QMode'
        'lIndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QQmlFilterBase27filterAcceptsColumnInternalEiRK1'
          '1QModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual, a0, self._valueOf(a1), self._addressOf(a2),
    )

  def supportColumnFiltering(self) -> bool:
    """
    Calls Qt's 'bool QQmlFilterBase::supportColumnFiltering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfilterbase.html#supportColumnFiltering
    """
    #  bool QQmlFilterBase::supportColumnFiltering() const
    ritual = 'ritual_ZNK14QQmlFilterBase22supportColumnFilteringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlFilterBase22supportColumnFilteringEv'
    return self.uglySide.call(ritual)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQmlFilterBase::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#isActive
    """
    #  bool QQmlFilterBase::isActive() const
    ritual = 'ritual_ZNK14QQmlFilterBase8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlFilterBase8isActiveEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, bEnable: bool) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::setEnabled(bool bEnable)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#setEnabled

    Parameters
    ----------

    bEnable : bool
      Passed on as it is.
    """
    #  void QQmlFilterBase::setEnabled(bool bEnable)
    self.uglySide.call('ritual_ZN14QQmlFilterBase10setEnabledEb', bEnable)

  @overload(bool)
  def setInverted(self, bInvert: bool) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::setInverted(bool bInvert)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#setInverted

    Parameters
    ----------

    bInvert : bool
      Passed on as it is.
    """
    #  void QQmlFilterBase::setInverted(bool bInvert)
    self.uglySide.call('ritual_ZN14QQmlFilterBase11setInvertedEb', bInvert)

  @overload(int)
  def setColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::setColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#setColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QQmlFilterBase::setColumn(int column)
    ritual = 'ritual_ZN14QQmlFilterBase9setColumnEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQmlFilterBase9setColumnEi'
    self.uglySide.call(ritual, column)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlFilterBasePrivate, QObject)
  @overload(QQmlFilterBasePrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      privObj: Optional[QQmlFilterBasePrivate],
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlFilterBase::QQmlFilterBase(QQmlFilterBasePrivate *privObj, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#QQmlFilterBase

    Parameters
    ----------

    privObj : Optional[QQmlFilterBasePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlFilterBase::QQmlFilterBase(QQmlFilterBasePrivate *privObj, QObject
    #      *parent)
    self._noteCreation(QQmlFilterBase, lambda: Rituals.call(
        'ritual_ZN14QQmlFilterBaseC1EP21QQmlFilterBasePrivateP7QObject',
        self._addressOf(privObj), self._addressOf(parent, 'QObject'),
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

  @overload(QQmlSortFilterProxyModel)
  @overload(NoneType)
  def update(self, a0: Optional[QQmlSortFilterProxyModel]) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::update(const QQmlSortFilterProxyModel
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#update

    Parameters
    ----------

    a0 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlFilterBase::update(const QQmlSortFilterProxyModel *a0)
    ritual = 'ritual_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyModel'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyMode'
          'l')
    self.uglySide.call(ritual, self._addressOf(a0))

  def invalidateModel(self) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::invalidateModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfilterbase.html#invalidateModel
    """
    #  void QQmlFilterBase::invalidateModel()
    self.uglySide.call('ritual_ZN14QQmlFilterBase15invalidateModelEv')

  @overload(THIS)
  @overload(NoneType)
  def invalidateCache(self, filter: Optional[QQmlFilterBase]) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::invalidateCache(QQmlFilterBase
    *filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfilterbase.html#invalidateCache

    Parameters
    ----------

    filter : Optional[QQmlFilterBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlFilterBase::invalidateCache(QQmlFilterBase *filter)
    self.uglySide.call(
        'ritual_ZN14QQmlFilterBase15invalidateCacheEPS_',
        self._addressOf(filter),
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#enabledChanged
    """
    #  void QQmlFilterBase::enabledChanged()
    self.uglySide.call('ritual_ZN14QQmlFilterBase14enabledChangedEv')

  def invertedChanged(self) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::invertedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfilterbase.html#invertedChanged
    """
    #  void QQmlFilterBase::invertedChanged()
    self.uglySide.call('ritual_ZN14QQmlFilterBase15invertedChangedEv')

  def columnChanged(self) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::columnChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#columnChanged
    """
    #  void QQmlFilterBase::columnChanged()
    self.uglySide.call('ritual_ZN14QQmlFilterBase13columnChangedEv')

  @overload()
  @overload(bool)
  def invalidate(self, updateCache: bool = False) -> None:
    """
    Calls Qt's 'void QQmlFilterBase::invalidate(bool updateCache)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#invalidate

    Parameters
    ----------

    updateCache : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQmlFilterBase::invalidate(bool updateCache)
    self.uglySide.call(
        'ritual_ZN14QQmlFilterBase10invalidateEb', updateCache,
    )

  def d_func(self) -> Optional[QQmlFilterBasePrivate]:
    """
    Calls Qt's 'QQmlFilterBasePrivate *QQmlFilterBase::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfilterbase.html#d_func

    Returns
    -------

    Optional[QQmlFilterBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFilterBasePrivate *QQmlFilterBase::d_func()
    address = self.uglySide.call('ritual_ZN14QQmlFilterBase6d_funcEv')
    from . import QQmlFilterBasePrivate
    return QQmlFilterBasePrivate._cuteAt(address)


#  Qt's 'QList<QQmlFilterBase *>': the list of QQmlFilterBase, which
#  'QList[QQmlFilterBase]' gives. It is made here, so that there is one as
#  soon as there can be a QQmlFilterBase.
QList.createKind(
    QQmlFilterBase, 'address',
    make='ritual_list_make_QQmlFilterBase_ptr',
    add='ritual_list_add_QQmlFilterBase_ptr',
    size='ritual_list_size_QQmlFilterBase_ptr',
    at='ritual_list_at_QQmlFilterBase_ptr',
    drop='ritual_list_drop_QQmlFilterBase_ptr',
)
