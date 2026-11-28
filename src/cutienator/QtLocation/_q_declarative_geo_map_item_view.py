"""
QDeclarativeGeoMapItemView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoMapItemView to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQuick import QQuickItem
from . import QDeclarativeGeoMapItemGroup
from ..QtQmlModels import QQmlDelegateModel, QQmlInstanceModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlComponent
  from . import QDeclarativeGeoMap, QDeclarativeGeoMapItemBase
  from ..QtQmlModels import QQmlChangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']
  QDeclarativeGeoMapItemBase = WAIT['QDeclarativeGeoMapItemBase']
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQmlComponent = WAIT['QQmlComponent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoMapItemView(QDeclarativeGeoMapItemGroup):
  """
  The cute side of Qt's QDeclarativeGeoMapItemView: a plain Python object
  standing in front of one C++ QDeclarativeGeoMapItemView.

  It is built on the cute 'QDeclarativeGeoMapItemGroup', as Qt's
  QDeclarativeGeoMapItemView is built on Qt's QDeclarativeGeoMapItemGroup,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMapItemView that has a ritual and
  that Python can call so far, 38 names in all: 'metaObject', 'tr', 'model',
  'setModel', 'delegate', 'setDelegate', 'autoFitViewport',
  'setAutoFitViewport', 'setMap', 'removeInstantiatedItems',
  'instantiateAllItems', 'setIncubateDelegates', 'incubateDelegates',
  'delegateModelAccess', 'setDelegateModelAccess', 'mapItems',
  'componentComplete', 'classBegin', 'modelChanged', 'delegateChanged',
  'autoFitViewportChanged', 'incubateDelegatesChanged',
  'delegateModelAccessChanged', 'destroyingItem', 'initItem', 'createdItem',
  'modelUpdated', 'exitTransitionFinished', 'fitViewport',
  'removeDelegateFromMap', 'transitionItemOut', 'terminateExitTransition',
  'disposeDelegate', 'insertInstantiatedItem', 'addItemToMap',
  'addItemViewToMap', 'addItemGroupToMap', 'addDelegateToMap'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoMapItemView::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoMapItemView::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoMapItemView::~QDeclarativeGeoMapItemView()': the
    destructor: Python never removes a C++ QDeclarativeGeoMapItemView.

  What has no ritual
  ------------------

  2 of the 45 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMapItemView is created at the first use, not by
    'QDeclarativeGeoMapItemView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoMapItemView.
  - Qt tells when it has removed the C++ QDeclarativeGeoMapItemView. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QDeclarativeGeoMapItemView::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#tr

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
    #  QString QDeclarativeGeoMapItemView::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QDeclarativeGeoMapItemView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMapItemView'

  #  A C++ QDeclarativeGeoMapItemView Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoMapItemView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoMapItemView::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoMapItemView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeGeoMapItemView::model() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeGeoMapItemView::model() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemView5modelEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QDeclarativeGeoMapItemView::delegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QDeclarativeGeoMapItemView::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemView8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def autoFitViewport(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMapItemView::autoFitViewport() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#autoFitViewport
    """
    #  bool QDeclarativeGeoMapItemView::autoFitViewport() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemView15autoFitViewportEv',
    )

  def incubateDelegates(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMapItemView::incubateDelegates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#incubateDelegates
    """
    #  bool QDeclarativeGeoMapItemView::incubateDelegates() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemView17incubateDelegatesEv',
    )

  def delegateModelAccess(self) -> QQmlDelegateModel.DelegateModelAccess:
    """
    Calls Qt's 'QQmlDelegateModel::DelegateModelAccess
    QDeclarativeGeoMapItemView::delegateModelAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Returns
    -------

    QQmlDelegateModel.DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlDelegateModel.DelegateModelAccess(number)' gives.
    """
    #  QQmlDelegateModel::DelegateModelAccess
    #      QDeclarativeGeoMapItemView::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemView19delegateModelAccessEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::setModel(const QVariant
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#setModel

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapItemView::setModel(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView8setModelERK8QVariant',
        self._valueOf(a0),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::setDelegate(QQmlComponent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView11setDelegateEP13QQmlComponen'
        't',
        self._addressOf(a0),
    )

  @overload(bool)
  def setAutoFitViewport(self, fit: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::setAutoFitViewport(const
    bool &fit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#setAutoFitViewport

    Parameters
    ----------

    fit : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemView::setAutoFitViewport(const bool &fit)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView18setAutoFitViewportERKb', fit,
    )

  @overload(QDeclarativeGeoMap)
  @overload(NoneType)
  def setMap(self, a0: Optional[QDeclarativeGeoMap]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::setMap(QDeclarativeGeoMap
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#setMap

    Parameters
    ----------

    a0 : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::setMap(QDeclarativeGeoMap *a0)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView6setMapEP18QDeclarativeGeoMap',
        self._addressOf(a0),
    )

  @overload(bool)
  def setIncubateDelegates(self, useIncubators: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::setIncubateDelegates(bool
    useIncubators)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    useIncubators : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemView::setIncubateDelegates(bool
    #      useIncubators)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView20setIncubateDelegatesEb',
        useIncubators,
    )

  @overload(QQmlDelegateModel.DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: QQmlDelegateModel.DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemView::setDelegateModelAccess(QQmlDelegateModel::
    DelegateModelAccess delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    delegateModelAccess : QQmlDelegateModel.DelegateModelAccess
      Passed on as its number.
    """
    #  void QDeclarativeGeoMapItemView::setDelegateModelAccess(
    #      QQmlDelegateModel::DelegateModelAccess delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView22setDelegateModelAccessEN17Q'
        'QmlDelegateModel19DelegateModelAccessE',
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
    Notes what was given, for Qt's
    'QDeclarativeGeoMapItemView::QDeclarativeGeoMapItemView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoMapItemView::QDeclarativeGeoMapItemView(QQuickItem
    #      *parent)
    self._noteCreation(QDeclarativeGeoMapItemView, lambda: Rituals.call(
        'ritual_ZN26QDeclarativeGeoMapItemViewC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload()
  @overload(bool)
  def removeInstantiatedItems(self, transition: bool = True) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::removeInstantiatedItems(bool
    transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    transition : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMapItemView::removeInstantiatedItems(bool
    #      transition)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView23removeInstantiatedItemsEb',
        transition,
    )

  def instantiateAllItems(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::instantiateAllItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html
    """
    #  void QDeclarativeGeoMapItemView::instantiateAllItems()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView19instantiateAllItemsEv',
    )

  def mapItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *> QDeclarativeGeoMapItemView::mapItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#mapItems

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QDeclarativeGeoMapItemView::mapItems()
    address = self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView8mapItemsEv',
    )
    return QList[QQuickItem]._cuteOwning(address)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#componentComplete
    """
    #  void QDeclarativeGeoMapItemView::componentComplete()
    ritual = 'ritual_ZN26QDeclarativeGeoMapItemView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativeGeoMapItemView17componentCompleteEv')
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#classBegin
    """
    #  void QDeclarativeGeoMapItemView::classBegin()
    ritual = 'ritual_ZN26QDeclarativeGeoMapItemView10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QDeclarativeGeoMapItemView10classBeginEv'
    self.uglySide.call(ritual)

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#modelChanged
    """
    #  void QDeclarativeGeoMapItemView::modelChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView12modelChangedEv',
    )

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#delegateChanged
    """
    #  void QDeclarativeGeoMapItemView::delegateChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView15delegateChangedEv',
    )

  def autoFitViewportChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::autoFitViewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html
    """
    #  void QDeclarativeGeoMapItemView::autoFitViewportChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView22autoFitViewportChangedEv',
    )

  def incubateDelegatesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::incubateDelegatesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html
    """
    #  void QDeclarativeGeoMapItemView::incubateDelegatesChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView24incubateDelegatesChangedEv',
    )

  def delegateModelAccessChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemView::delegateModelAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html
    """
    #  void QDeclarativeGeoMapItemView::delegateModelAccessChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView26delegateModelAccessChangedE'
        'v',
    )

  @overload(QObject)
  @overload(NoneType)
  def destroyingItem(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::destroyingItem(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#destroyingItem

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::destroyingItem(QObject *object)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView14destroyingItemEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItem(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::initItem(int index, QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#initItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::initItem(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView8initItemEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def createdItem(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::createdItem(int index,
    QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#createdItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::createdItem(int index, QObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView11createdItemEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(QQmlChangeSet, bool)
  def modelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::modelUpdated(const
    QQmlChangeSet &changeSet, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#modelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemView::modelUpdated(const QQmlChangeSet
    #      &changeSet, bool reset)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView12modelUpdatedERK13QQmlChange'
        'Setb',
        self._valueOf(changeSet), reset,
    )

  def exitTransitionFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::exitTransitionFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html
    """
    #  void QDeclarativeGeoMapItemView::exitTransitionFinished()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView22exitTransitionFinishedEv',
    )

  def fitViewport(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::fitViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#fitViewport
    """
    #  void QDeclarativeGeoMapItemView::fitViewport()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView11fitViewportEv',
    )

  @overload(int)
  @overload(int, bool)
  def removeDelegateFromMap(
      self,
      index: int,
      transition: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::removeDelegateFromMap(int
    index, bool transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    transition : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMapItemView::removeDelegateFromMap(int index, bool
    #      transition)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView21removeDelegateFromMapEib',
        index, transition,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def removeDelegateFromMap(self, o: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemView::removeDelegateFromMap(QQuickItem *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    o : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::removeDelegateFromMap(QQuickItem *o)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView21removeDelegateFromMapEP10QQ'
        'uickItem',
        self._addressOf(o),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def transitionItemOut(self, o: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::transitionItemOut(QQuickItem
    *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#transitionItemOut

    Parameters
    ----------

    o : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::transitionItemOut(QQuickItem *o)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView17transitionItemOutEP10QQuick'
        'Item',
        self._addressOf(o),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def terminateExitTransition(self, o: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemView::terminateExitTransition(QQuickItem *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    o : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemView::terminateExitTransition(QQuickItem
    #      *o)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView23terminateExitTransitionEP10'
        'QQuickItem',
        self._addressOf(o),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def disposeDelegate(
      self,
      item: Optional[QQuickItem],
  ) -> QQmlInstanceModel.ReleaseFlags:
    """
    Calls Qt's 'QQmlInstanceModel::ReleaseFlags
    QDeclarativeGeoMapItemView::disposeDelegate(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#disposeDelegate

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlInstanceModel.ReleaseFlags
      The value standing for the combination Qt gave back.
    """
    #  QQmlInstanceModel::ReleaseFlags
    #      QDeclarativeGeoMapItemView::disposeDelegate(QQuickItem *item)
    return QQmlInstanceModel.ReleaseFlags(self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView15disposeDelegateEP10QQuickIt'
        'em',
        self._addressOf(item),
    ))

  @overload(int, QQuickItem, bool)
  @overload(int, NoneType, bool)
  def insertInstantiatedItem(
      self,
      index: int,
      o: Optional[QQuickItem],
      createdItem: bool,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::insertInstantiatedItem(int
    index, QQuickItem *o, bool createdItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    o : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    createdItem : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemView::insertInstantiatedItem(int index,
    #      QQuickItem *o, bool createdItem)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView22insertInstantiatedItemEiP10'
        'QQuickItemb',
        index, self._addressOf(o), createdItem,
    )

  @overload(QDeclarativeGeoMapItemBase, int, bool)
  @overload(NoneType, int, bool)
  def addItemToMap(
      self,
      item: Optional[QDeclarativeGeoMapItemBase],
      index: int,
      createdItem: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemView::addItemToMap(QDeclarativeGeoMapItemBase
    *item, int index, bool createdItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#addItemToMap

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    createdItem : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemView::addItemToMap(
    #      QDeclarativeGeoMapItemBase *item, int index, bool createdItem)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView12addItemToMapEP26QDeclarativ'
        'eGeoMapItemBaseib',
        self._addressOf(item), index, createdItem,
    )

  @overload(THIS, int, bool)
  @overload(NoneType, int, bool)
  def addItemViewToMap(
      self,
      item: Optional[QDeclarativeGeoMapItemView],
      index: int,
      createdItem: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemView::addItemViewToMap(QDeclarativeGeoMapItemView
    *item, int index, bool createdItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#addItemViewToMap

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    createdItem : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemView::addItemViewToMap(
    #      QDeclarativeGeoMapItemView *item, int index, bool createdItem)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView16addItemViewToMapEPS_ib',
        self._addressOf(item), index, createdItem,
    )

  @overload(QDeclarativeGeoMapItemGroup, int, bool)
  @overload(NoneType, int, bool)
  def addItemGroupToMap(
      self,
      item: Optional[QDeclarativeGeoMapItemGroup],
      index: int,
      createdItem: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemView::addItemGroupToMap(QDeclarativeGeoMapItemGroup
    *item, int index, bool createdItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#addItemGroupToMap

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    createdItem : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemView::addItemGroupToMap(
    #      QDeclarativeGeoMapItemGroup *item, int index, bool createdItem)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView17addItemGroupToMapEP27QDecla'
        'rativeGeoMapItemGroupib',
        self._addressOf(item), index, createdItem,
    )

  @overload(QQuickItem, int)
  @overload(NoneType, int)
  @overload(QQuickItem, int, bool)
  @overload(NoneType, int, bool)
  def addDelegateToMap(
      self,
      object: Optional[QQuickItem],
      index: int,
      createdItem: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemView::addDelegateToMap(QQuickItem
    *object, int index, bool createdItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemview.html#addDelegateToMap

    Parameters
    ----------

    object : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    createdItem : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDeclarativeGeoMapItemView::addDelegateToMap(QQuickItem *object,
    #      int index, bool createdItem)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemView16addDelegateToMapEP10QQuickI'
        'temib',
        self._addressOf(object), index, createdItem,
    )
