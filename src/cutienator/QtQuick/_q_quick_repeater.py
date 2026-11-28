"""
QQuickRepeater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrepeater_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickRepeater to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickItem
from ..QtQmlModels import QQmlDelegateModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlComponent
  from . import QQuickRepeaterPrivate
  from ..QtQmlModels import QQmlChangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQmlComponent = WAIT['QQmlComponent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRepeater(QQuickItem):
  """
  The cute side of Qt's QQuickRepeater: a plain Python object standing in
  front of one C++ QQuickRepeater.

  It is built on the cute 'QQuickItem', as Qt's QQuickRepeater is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRepeater that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'delegate', 'setDelegate', 'count', 'itemAt', 'delegateModelAccess',
  'setDelegateModelAccess', 'modelChanged', 'delegateChanged',
  'countChanged', 'itemAdded', 'itemRemoved', 'delegateModelAccessChanged',
  'clear', 'regenerate', 'componentComplete', 'itemChange', 'createdItem',
  'initItem', 'modelUpdated', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRepeater::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickRepeater::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRepeater::~QQuickRepeater()': the destructor: Python never
    removes a C++ QQuickRepeater.
  - Qt's 'const QQuickRepeaterPrivate *QQuickRepeater::d_func() const': takes
    in Python what 'QQuickRepeaterPrivate *QQuickRepeater::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickRepeater is created at the first use, not by
    'QQuickRepeater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRepeater.
  - Qt tells when it has removed the C++ QQuickRepeater. Every call on the
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
    Calls Qt's 'QString QQuickRepeater::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#tr

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
    #  QString QQuickRepeater::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickRepeater2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRepeater'

  #  A C++ QQuickRepeater Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRepeater'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRepeater::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRepeater::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickRepeater10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickRepeater::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickRepeater::model() const
    address = self.uglySide.call('ritual_ZNK14QQuickRepeater5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickRepeater::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickRepeater::delegate() const
    address = self.uglySide.call('ritual_ZNK14QQuickRepeater8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickRepeater::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#count
    """
    #  int QQuickRepeater::count() const
    return self.uglySide.call('ritual_ZNK14QQuickRepeater5countEv')

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickRepeater::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickRepeater::itemAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickRepeater6itemAtEi', index,
    )
    return QQuickItem._cuteAt(address)

  def delegateModelAccess(self) -> QQmlDelegateModel.DelegateModelAccess:
    """
    Calls Qt's 'QQmlDelegateModel::DelegateModelAccess
    QQuickRepeater::delegateModelAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeater.html#delegateModelAccess

    Returns
    -------

    QQmlDelegateModel.DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlDelegateModel.DelegateModelAccess(number)' gives.
    """
    #  QQmlDelegateModel::DelegateModelAccess
    #      QQuickRepeater::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK14QQuickRepeater19delegateModelAccessEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuickRepeater::setModel(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#setModel

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickRepeater::setModel(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater8setModelERK8QVariant', self._valueOf(a0),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickRepeater::setDelegate(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRepeater::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater11setDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(QQmlDelegateModel.DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: QQmlDelegateModel.DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickRepeater::setDelegateModelAccess(QQmlDelegateModel::
    DelegateModelAccess delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeater.html#setDelegateModelAccess

    Parameters
    ----------

    delegateModelAccess : QQmlDelegateModel.DelegateModelAccess
      Passed on as its number.
    """
    #  void QQuickRepeater::setDelegateModelAccess(QQmlDelegateModel::
    #      DelegateModelAccess delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater22setDelegateModelAccessEN17QQmlDelegateM'
        'odel19DelegateModelAccessE',
        delegateModelAccess.value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickRepeater::QQuickRepeater(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#QQuickRepeater

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRepeater::QQuickRepeater(QQuickItem *parent)
    self._noteCreation(QQuickRepeater, lambda: Rituals.call(
        'ritual_ZN14QQuickRepeaterC1EP10QQuickItem', self._addressOf(parent),
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

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRepeater::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#modelChanged
    """
    #  void QQuickRepeater::modelChanged()
    self.uglySide.call('ritual_ZN14QQuickRepeater12modelChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRepeater::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeater.html#delegateChanged
    """
    #  void QQuickRepeater::delegateChanged()
    self.uglySide.call('ritual_ZN14QQuickRepeater15delegateChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRepeater::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#countChanged
    """
    #  void QQuickRepeater::countChanged()
    self.uglySide.call('ritual_ZN14QQuickRepeater12countChangedEv')

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemAdded(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickRepeater::itemAdded(int index, QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#itemAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRepeater::itemAdded(int index, QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater9itemAddedEiP10QQuickItem',
        index, self._addressOf(item),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemRemoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickRepeater::itemRemoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRepeater::itemRemoved(int index, QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater11itemRemovedEiP10QQuickItem',
        index, self._addressOf(item),
    )

  def delegateModelAccessChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRepeater::delegateModelAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeater.html#delegateModelAccessChanged
    """
    #  void QQuickRepeater::delegateModelAccessChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater26delegateModelAccessChangedEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickRepeater::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#clear
    """
    #  void QQuickRepeater::clear()
    self.uglySide.call('ritual_ZN14QQuickRepeater5clearEv')

  def regenerate(self) -> None:
    """
    Calls Qt's 'void QQuickRepeater::regenerate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#regenerate
    """
    #  void QQuickRepeater::regenerate()
    self.uglySide.call('ritual_ZN14QQuickRepeater10regenerateEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickRepeater::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeater.html#componentComplete
    """
    #  void QQuickRepeater::componentComplete()
    ritual = 'ritual_ZN14QQuickRepeater17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickRepeater17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickRepeater::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickRepeater::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN14QQuickRepeater10itemChangeEN10QQuickItem10ItemChangeERK'
        'NS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickRepeater10itemChangeEN10QQuickItem10ItemCha'
          'ngeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(int, QObject)
  @overload(int, NoneType)
  def createdItem(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickRepeater::createdItem(int index, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#createdItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRepeater::createdItem(int index, QObject *item)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater11createdItemEiP7QObject',
        index, self._addressOf(item, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItem(self, a0: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickRepeater::initItem(int a0, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#initItem

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRepeater::initItem(int a0, QObject *item)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater8initItemEiP7QObject',
        a0, self._addressOf(item, 'QObject'),
    )

  @overload(QQmlChangeSet, bool)
  def modelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQuickRepeater::modelUpdated(const QQmlChangeSet
    &changeSet, bool reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#modelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQuickRepeater::modelUpdated(const QQmlChangeSet &changeSet, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN14QQuickRepeater12modelUpdatedERK13QQmlChangeSetb',
        self._valueOf(changeSet), reset,
    )

  def d_func(self) -> Optional[QQuickRepeaterPrivate]:
    """
    Calls Qt's 'QQuickRepeaterPrivate *QQuickRepeater::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeater.html#d_func

    Returns
    -------

    Optional[QQuickRepeaterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRepeaterPrivate *QQuickRepeater::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickRepeater6d_funcEv')
    from . import QQuickRepeaterPrivate
    return QQuickRepeaterPrivate._cuteAt(address)
