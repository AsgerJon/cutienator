"""
QtPrivate::QPropertyBindingData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBindingStorage, QPropertyBindingPrivate
  from . import QPropertyProxyBindingData, QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBindingStorage = WAIT['QBindingStorage']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyBindingData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QPropertyBindingData: a plain Python
  object standing in front of one C++ QtPrivate::QPropertyBindingData.

  What exists
  -----------

  Every function of Qt's QtPrivate::QPropertyBindingData that has a ritual
  and that Python can call so far, 11 names in all: 'hasBinding',
  'isNotificationDelayed', 'binding', 'evaluateIfDirty', 'removeBinding',
  'registerWithCurrentlyEvaluatingBinding', 'notifyObservers', 'd',
  'proxyData', 'registerWithCurrentlyEvaluatingBinding_helper',
  'removeBinding_helper'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::QPropertyBindingData::QPropertyBindingData(
    QPropertyBindingData &&other)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QtPrivate::QPropertyBindingData::~QPropertyBindingData()': the
    destructor: Python never removes a C++ QtPrivate::QPropertyBindingData.
  - Qt's 'QUntypedPropertyBinding
    QtPrivate::QPropertyBindingData::setBinding(const QUntypedPropertyBinding
    &newBinding, QUntypedPropertyData *propertyDataPtr,
    QPropertyObserverCallback staticObserverCallback, QPropertyBindingWrapper
    bindingWrapper)': takes a type Python has no way to hand over yet.
  - Qt's 'NotificationResult
    QtPrivate::QPropertyBindingData::notifyObserver_helper(
    QUntypedPropertyData *propertyDataPtr, QBindingStorage *storage,
    QPropertyObserverPointer observer, PendingBindingObserverList
    &bindingObservers) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 3 forbidden; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QtPrivate::QPropertyBindingData is created at the first use, not
    by 'QtPrivate::QPropertyBindingData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPrivate::QPropertyBindingData.
  - Each name of Qt's QtPrivate::QPropertyBindingData that has no cute
    function yet, 'd_ref', 'notifyObserver_helper', 'setBinding', holds a
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
  __qt_class__ = 'QtPrivate::QPropertyBindingData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasBinding(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QPropertyBindingData::hasBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html#hasBinding
    """
    #  bool QtPrivate::QPropertyBindingData::hasBinding() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData10hasBindingEv',
    )

  def isNotificationDelayed(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QPropertyBindingData::isNotificationDelayed()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html
    """
    #  bool QtPrivate::QPropertyBindingData::isNotificationDelayed() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData21isNotificationDelayedE'
        'v',
    )

  def binding(self) -> Optional[QPropertyBindingPrivate]:
    """
    Calls Qt's 'QPropertyBindingPrivate
    *QtPrivate::QPropertyBindingData::binding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html#binding

    Returns
    -------

    Optional[QPropertyBindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyBindingPrivate *QtPrivate::QPropertyBindingData::binding()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData7bindingEv',
    )
    from . import QPropertyBindingPrivate
    return QPropertyBindingPrivate._cuteAt(address)

  def d(self) -> int:
    """
    Calls Qt's 'quintptr QtPrivate::QPropertyBindingData::d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html#d
    """
    #  quintptr QtPrivate::QPropertyBindingData::d() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData1dEv',
    )

  def proxyData(self) -> Optional[QPropertyProxyBindingData]:
    """
    Calls Qt's 'QPropertyProxyBindingData
    *QtPrivate::QPropertyBindingData::proxyData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html#proxyData

    Returns
    -------

    Optional[QPropertyProxyBindingData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyProxyBindingData
    #      *QtPrivate::QPropertyBindingData::proxyData() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData9proxyDataEv',
    )
    from . import QPropertyProxyBindingData
    return QPropertyProxyBindingData._cuteAt(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QPropertyBindingData::QPropertyBindingData()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html
    """
    #  QtPrivate::QPropertyBindingData::QPropertyBindingData()
    self._noteCreation(QPropertyBindingData, lambda: Rituals.call(
        'ritual_ZN9QtPrivate20QPropertyBindingDataC1Ev',
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

  @overload(QUntypedPropertyData)
  @overload(NoneType)
  def evaluateIfDirty(self, a0: Optional[QUntypedPropertyData]) -> None:
    """
    Calls Qt's 'void QtPrivate::QPropertyBindingData::evaluateIfDirty(const
    QUntypedPropertyData *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html

    Parameters
    ----------

    a0 : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QPropertyBindingData::evaluateIfDirty(const
    #      QUntypedPropertyData *a0) const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData15evaluateIfDirtyEPK20QU'
        'ntypedPropertyData',
        self._addressOf(a0),
    )

  def removeBinding(self) -> None:
    """
    Calls Qt's 'void QtPrivate::QPropertyBindingData::removeBinding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html#removeBinding
    """
    #  void QtPrivate::QPropertyBindingData::removeBinding()
    self.uglySide.call(
        'ritual_ZN9QtPrivate20QPropertyBindingData13removeBindingEv',
    )

  @overload(WAIT['QtPrivate.BindingEvaluationState'])
  @overload(NoneType)
  def registerWithCurrentlyEvaluatingBinding(
      self,
      currentBinding: Optional[QtPrivate.BindingEvaluationState],
  ) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QPropertyBindingData::registerWithCurrentlyEvaluatingBinding(
    QtPrivate::BindingEvaluationState *currentBinding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html

    Parameters
    ----------

    currentBinding : Optional[QtPrivate.BindingEvaluationState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QPropertyBindingData::
    #      registerWithCurrentlyEvaluatingBinding(QtPrivate::
    #      BindingEvaluationState *currentBinding) const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData38registerWithCurrentlyE'
        'valuatingBindingEPNS_22BindingEvaluationStateE',
        self._addressOf(currentBinding),
    )

  @overload()
  def registerWithCurrentlyEvaluatingBinding(self) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QPropertyBindingData::registerWithCurrentlyEvaluatingBinding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html
    """
    #  void QtPrivate::QPropertyBindingData::
    #      registerWithCurrentlyEvaluatingBinding() const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData38registerWithCurrentlyE'
        'valuatingBindingEv',
    )

  @overload(QUntypedPropertyData)
  @overload(NoneType)
  def notifyObservers(
      self,
      propertyDataPtr: Optional[QUntypedPropertyData],
  ) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QPropertyBindingData::notifyObservers(QUntypedPropertyData
    *propertyDataPtr) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html

    Parameters
    ----------

    propertyDataPtr : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QPropertyBindingData::notifyObservers(
    #      QUntypedPropertyData *propertyDataPtr) const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData15notifyObserversEP20QUn'
        'typedPropertyData',
        self._addressOf(propertyDataPtr),
    )

  @overload(QUntypedPropertyData, QBindingStorage)
  @overload(QUntypedPropertyData, NoneType)
  @overload(NoneType, QBindingStorage)
  @overload(NoneType, NoneType)
  def notifyObservers(
      self,
      propertyDataPtr: Optional[QUntypedPropertyData],
      storage: Optional[QBindingStorage],
  ) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QPropertyBindingData::notifyObservers(QUntypedPropertyData
    *propertyDataPtr, QBindingStorage *storage) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html

    Parameters
    ----------

    propertyDataPtr : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    storage : Optional[QBindingStorage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QPropertyBindingData::notifyObservers(
    #      QUntypedPropertyData *propertyDataPtr, QBindingStorage *storage)
    #      const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData15notifyObserversEP20QUn'
        'typedPropertyDataP15QBindingStorage',
        self._addressOf(propertyDataPtr), self._addressOf(storage),
    )

  @overload(WAIT['QtPrivate.BindingEvaluationState'])
  @overload(NoneType)
  def registerWithCurrentlyEvaluatingBinding_helper(
      self,
      currentBinding: Optional[QtPrivate.BindingEvaluationState],
  ) -> None:
    """
    Calls Qt's 'void QtPrivate::QPropertyBindingData::
    registerWithCurrentlyEvaluatingBinding_helper(BindingEvaluationState
    *currentBinding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html

    Parameters
    ----------

    currentBinding : Optional[QtPrivate.BindingEvaluationState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QPropertyBindingData::
    #      registerWithCurrentlyEvaluatingBinding_helper(
    #      BindingEvaluationState *currentBinding) const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate20QPropertyBindingData45registerWithCurrentlyE'
        'valuatingBinding_helperEPNS_22BindingEvaluationStateE',
        self._addressOf(currentBinding),
    )

  def removeBinding_helper(self) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QPropertyBindingData::removeBinding_helper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertybindingdata.html
    """
    #  void QtPrivate::QPropertyBindingData::removeBinding_helper()
    self.uglySide.call(
        'ritual_ZN9QtPrivate20QPropertyBindingData20removeBinding_helperEv',
    )

  @staticmethod
  def d_ref(*__, **_) -> Never:
    """
    Qt's 'quintptr &QtPrivate::QPropertyBindingData::d_ref() const': takes or
    gives a type that cannot be passed yet: quintptr &.
    """
    raise NotImplementedError(
        "'QtPrivate.QPropertyBindingData.d_ref' has no cute function yet. "
        "Qt's 'quintptr &QtPrivate::QPropertyBindingData::d_ref() const': "
        "takes or gives a type that cannot be passed yet: quintptr &.")

  @staticmethod
  def notifyObserver_helper(*__, **_) -> Never:
    """
    Qt's 'NotificationResult
    QtPrivate::QPropertyBindingData::notifyObserver_helper(
    QUntypedPropertyData *propertyDataPtr, QBindingStorage *storage,
    QPropertyObserverPointer observer, PendingBindingObserverList
    &bindingObservers) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QPropertyBindingData.notifyObserver_helper' has no cute "
        "function yet. Qt's 'NotificationResult "
        "QtPrivate::QPropertyBindingData::notifyObserver_helper(QUntypedProp"
        "ertyData *propertyDataPtr, QBindingStorage *storage, "
        "QPropertyObserverPointer observer, PendingBindingObserverList "
        "&bindingObservers) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setBinding(*__, **_) -> Never:
    """
    Qt's 'QUntypedPropertyBinding
    QtPrivate::QPropertyBindingData::setBinding(const QUntypedPropertyBinding
    &newBinding, QUntypedPropertyData *propertyDataPtr,
    QPropertyObserverCallback staticObserverCallback, QPropertyBindingWrapper
    bindingWrapper)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QPropertyBindingData.setBinding' has no cute function "
        "yet. Qt's 'QUntypedPropertyBinding "
        "QtPrivate::QPropertyBindingData::setBinding(const "
        "QUntypedPropertyBinding &newBinding, QUntypedPropertyData "
        "*propertyDataPtr, QPropertyObserverCallback "
        "staticObserverCallback, QPropertyBindingWrapper bindingWrapper)': "
        "takes a type Python has no way to hand over yet.")
