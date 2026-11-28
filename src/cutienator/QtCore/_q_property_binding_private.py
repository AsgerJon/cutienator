"""
QPropertyBindingPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPropertyBindingPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaType, QPropertyBindingError
  from . import QPropertyBindingSourceLocation, QPropertyObserverPointer
  from . import QUntypedPropertyBinding, QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QPropertyBindingSourceLocation = WAIT['QPropertyBindingSourceLocation']
  QPropertyObserverPointer = WAIT['QPropertyObserverPointer']
  QUntypedPropertyBinding = WAIT['QUntypedPropertyBinding']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyBindingPrivate(QtPrivate.RefCounted):
  """
  The cute side of Qt's QPropertyBindingPrivate: a plain Python object
  standing in front of one C++ QPropertyBindingPrivate.

  It is built on the cute 'QtPrivate::RefCounted', as Qt's
  QPropertyBindingPrivate is built on Qt's QtPrivate::RefCounted, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPropertyBindingPrivate that has a ritual and that
  Python can call so far, 24 names in all: 'getSizeEnsuringAlignment',
  'bindingFunctionVTable', 'isUpdating', 'setSticky', 'isSticky',
  'scheduleNotify', 'setProperty', 'prependObserver', 'takeObservers',
  'clearDependencyObservers', 'allocateDependencyObserver',
  'allocateDependencyObserver_slow', 'sourceLocation', 'bindingError',
  'valueMetaType', 'unlinkAndDeref', 'notifyNonRecursive', 'get',
  'makeUntyped', 'detachFromProperty', 'currentlyEvaluatingBinding',
  'hasCustomVTable', 'isQmlBinding', 'destroyAndFreeMemory'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPropertyBindingPrivate::~QPropertyBindingPrivate()': the
    destructor: Python never removes a C++ QPropertyBindingPrivate.
  - Qt's 'void QPropertyBindingPrivate::setStaticObserver(QtPrivate::
    QPropertyObserverCallback callback, QtPrivate::QPropertyBindingWrapper
    bindingWrapper)': takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QPropertyBindingPrivate::evaluateRecursive(PendingBindingObserverList
    &bindingObservers, QBindingStatus *status)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QPropertyBindingPrivate::evaluateRecursive_inline(
    PendingBindingObserverList &bindingObservers, QBindingStatus *status)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QPropertyBindingPrivate::notifyNonRecursive(const
    PendingBindingObserverList &bindingObservers)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QPropertyBindingPrivate::setError(QPropertyBindingError &&e)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QPropertyBindingPrivate is created at the first use, not by
    'QPropertyBindingPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPropertyBindingPrivate.
  - Each name of Qt's QPropertyBindingPrivate that has no cute function yet,
    'evaluateRecursive', 'evaluateRecursive_inline', 'setError',
    'setStaticObserver', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QPropertyBindingPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class NotificationState(CuteNum):
    """
    The enum 'QPropertyBindingPrivate::NotificationState' of Qt, with the 2
    names Qt gives in it.
    """

    Delayed = Kee[int](0)
    Sent = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getSizeEnsuringAlignment() -> int:
    """
    Calls Qt's 'size_t QPropertyBindingPrivate::getSizeEnsuringAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html
    """
    #  size_t QPropertyBindingPrivate::getSizeEnsuringAlignment()
    return Rituals.call(
        'ritual_ZN23QPropertyBindingPrivate24getSizeEnsuringAlignmentEv',
    )

  @staticmethod
  @overload(QUntypedPropertyBinding)
  def get(
      binding: QUntypedPropertyBinding,
  ) -> Optional[QPropertyBindingPrivate]:
    """
    Calls Qt's 'QPropertyBindingPrivate *QPropertyBindingPrivate::get(const
    QUntypedPropertyBinding &binding)'.

    Qt's own words: https://doc.qt.io/qt-6/qpropertybindingprivate.html#get

    Parameters
    ----------

    binding : QUntypedPropertyBinding
      Passed on as a value: Qt reads the C++ QUntypedPropertyBinding, which
      stays Python's own.

    Returns
    -------

    Optional[QPropertyBindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyBindingPrivate *QPropertyBindingPrivate::get(const
    #      QUntypedPropertyBinding &binding)
    address = Rituals.call(
        'ritual_ZN23QPropertyBindingPrivate3getERK23QUntypedPropertyBinding',
        CuteMixin._valueOf(binding),
    )
    return QPropertyBindingPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def makeUntyped(
      d: Optional[QPropertyBindingPrivate],
  ) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding
    QPropertyBindingPrivate::makeUntyped(QPropertyBindingPrivate *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#makeUntyped

    Parameters
    ----------

    d : Optional[QPropertyBindingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding
    #      QPropertyBindingPrivate::makeUntyped(QPropertyBindingPrivate *d)
    address = Rituals.call(
        'ritual_ZN23QPropertyBindingPrivate11makeUntypedEPS_',
        CuteMixin._addressOf(d),
    )
    from . import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  @staticmethod
  def currentlyEvaluatingBinding() -> Optional[QPropertyBindingPrivate]:
    """
    Calls Qt's 'QPropertyBindingPrivate
    *QPropertyBindingPrivate::currentlyEvaluatingBinding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html

    Returns
    -------

    Optional[QPropertyBindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyBindingPrivate
    #      *QPropertyBindingPrivate::currentlyEvaluatingBinding()
    address = Rituals.call(
        'ritual_ZN23QPropertyBindingPrivate26currentlyEvaluatingBindingEv',
    )
    return QPropertyBindingPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def destroyAndFreeMemory(priv: Optional[QPropertyBindingPrivate]) -> None:
    """
    Calls Qt's 'void
    QPropertyBindingPrivate::destroyAndFreeMemory(QPropertyBindingPrivate
    *priv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#destroyAndFreeMemory

    Parameters
    ----------

    priv : Optional[QPropertyBindingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyBindingPrivate::destroyAndFreeMemory(
    #      QPropertyBindingPrivate *priv)
    Rituals.call(
        'ritual_ZN23QPropertyBindingPrivate20destroyAndFreeMemoryEPS_',
        CuteMixin._addressOf(priv),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyBindingPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bindingFunctionVTable(
      self,
  ) -> Optional[QtPrivate.BindingFunctionVTable]:
    """
    Calls Qt's 'const QtPrivate::BindingFunctionVTable
    *QPropertyBindingPrivate::bindingFunctionVTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#bindingFunctionVTable

    Returns
    -------

    Optional[QtPrivate.BindingFunctionVTable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtPrivate::BindingFunctionVTable
    #      *QPropertyBindingPrivate::bindingFunctionVTable() const
    address = self.uglySide.call(
        'ritual_ZNK23QPropertyBindingPrivate21bindingFunctionVTableEv',
    )
    return QtPrivate.BindingFunctionVTable._cuteAt(address)

  def sourceLocation(self) -> QPropertyBindingSourceLocation:
    """
    Calls Qt's 'QPropertyBindingSourceLocation
    QPropertyBindingPrivate::sourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#sourceLocation

    Returns
    -------

    QPropertyBindingSourceLocation
      A new cute QPropertyBindingSourceLocation around the copy Qt gave back.
      Python owns it.
    """
    #  QPropertyBindingSourceLocation
    #      QPropertyBindingPrivate::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK23QPropertyBindingPrivate14sourceLocationEv',
    )
    from . import QPropertyBindingSourceLocation
    return QPropertyBindingSourceLocation._cuteOwning(address)

  def bindingError(self) -> QPropertyBindingError:
    """
    Calls Qt's 'QPropertyBindingError QPropertyBindingPrivate::bindingError()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#bindingError

    Returns
    -------

    QPropertyBindingError
      A new cute QPropertyBindingError around the copy Qt gave back. Python
      owns it.
    """
    #  QPropertyBindingError QPropertyBindingPrivate::bindingError() const
    address = self.uglySide.call(
        'ritual_ZNK23QPropertyBindingPrivate12bindingErrorEv',
    )
    from . import QPropertyBindingError
    return QPropertyBindingError._cuteOwning(address)

  def valueMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QPropertyBindingPrivate::valueMetaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#valueMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QPropertyBindingPrivate::valueMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK23QPropertyBindingPrivate13valueMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def hasCustomVTable(self) -> bool:
    """
    Calls Qt's 'bool QPropertyBindingPrivate::hasCustomVTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#hasCustomVTable
    """
    #  bool QPropertyBindingPrivate::hasCustomVTable() const
    return self.uglySide.call(
        'ritual_ZNK23QPropertyBindingPrivate15hasCustomVTableEv',
    )

  def isQmlBinding(self) -> bool:
    """
    Calls Qt's 'bool QPropertyBindingPrivate::isQmlBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#isQmlBinding
    """
    #  bool QPropertyBindingPrivate::isQmlBinding() const
    return self.uglySide.call(
        'ritual_ZNK23QPropertyBindingPrivate12isQmlBindingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  def setSticky(self, keep: bool = True) -> None:
    """
    Calls Qt's 'void QPropertyBindingPrivate::setSticky(bool keep)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#setSticky

    Parameters
    ----------

    keep : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPropertyBindingPrivate::setSticky(bool keep)
    self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate9setStickyEb', keep,
    )

  @overload(QUntypedPropertyData)
  @overload(NoneType)
  def setProperty(self, propertyPtr: Optional[QUntypedPropertyData]) -> None:
    """
    Calls Qt's 'void
    QPropertyBindingPrivate::setProperty(QUntypedPropertyData *propertyPtr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#setProperty

    Parameters
    ----------

    propertyPtr : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyBindingPrivate::setProperty(QUntypedPropertyData
    #      *propertyPtr)
    self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate11setPropertyEP20QUntypedPropert'
        'yData',
        self._addressOf(propertyPtr),
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

  @overload(
      QMetaType, WAIT['QtPrivate.BindingFunctionVTable'],
      QPropertyBindingSourceLocation,
  )
  @overload(QMetaType, NoneType, QPropertyBindingSourceLocation)
  @overload(
      QMetaType, WAIT['QtPrivate.BindingFunctionVTable'],
      QPropertyBindingSourceLocation, bool,
  )
  @overload(QMetaType, NoneType, QPropertyBindingSourceLocation, bool)
  def __init__(
      self,
      metaType: QMetaType,
      vtable: Optional[QtPrivate.BindingFunctionVTable],
      location: QPropertyBindingSourceLocation,
      isQQmlPropertyBinding: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyBindingPrivate::QPropertyBindingPrivate(QMetaType metaType,
    const QtPrivate::BindingFunctionVTable *vtable, const
    QPropertyBindingSourceLocation &location, bool isQQmlPropertyBinding)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    vtable : Optional[QtPrivate.BindingFunctionVTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    location : QPropertyBindingSourceLocation
      Passed on as a value: Qt reads the C++ QPropertyBindingSourceLocation,
      which stays Python's own.

    isQQmlPropertyBinding : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QPropertyBindingPrivate::QPropertyBindingPrivate(QMetaType metaType,
    #      const QtPrivate::BindingFunctionVTable *vtable, const
    #      QPropertyBindingSourceLocation &location, bool
    #      isQQmlPropertyBinding)
    self._noteCreation(QPropertyBindingPrivate, lambda: Rituals.call(
        'ritual_ZN23QPropertyBindingPrivateC1E9QMetaTypePKN9QtPrivate21Bind'
        'ingFunctionVTableERK30QPropertyBindingSourceLocationb',
        self._valueOf(metaType), self._addressOf(vtable),
        self._valueOf(location), isQQmlPropertyBinding,
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

  def isUpdating(self) -> bool:
    """
    Calls Qt's 'bool QPropertyBindingPrivate::isUpdating()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#isUpdating
    """
    #  bool QPropertyBindingPrivate::isUpdating()
    return self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate10isUpdatingEv',
    )

  def isSticky(self) -> bool:
    """
    Calls Qt's 'bool QPropertyBindingPrivate::isSticky()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#isSticky
    """
    #  bool QPropertyBindingPrivate::isSticky()
    return self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate8isStickyEv',
    )

  def scheduleNotify(self) -> None:
    """
    Calls Qt's 'void QPropertyBindingPrivate::scheduleNotify()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#scheduleNotify
    """
    #  void QPropertyBindingPrivate::scheduleNotify()
    self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate14scheduleNotifyEv',
    )

  @overload(QPropertyObserverPointer)
  def prependObserver(self, observer: QPropertyObserverPointer) -> None:
    """
    Calls Qt's 'void
    QPropertyBindingPrivate::prependObserver(QPropertyObserverPointer
    observer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#prependObserver

    Parameters
    ----------

    observer : QPropertyObserverPointer
      Passed on as a value: Qt reads the C++ QPropertyObserverPointer, which
      stays Python's own.
    """
    #  void QPropertyBindingPrivate::prependObserver(QPropertyObserverPointer
    #      observer)
    self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate15prependObserverE24QPropertyObs'
        'erverPointer',
        self._valueOf(observer),
    )

  def takeObservers(self) -> QPropertyObserverPointer:
    """
    Calls Qt's 'QPropertyObserverPointer
    QPropertyBindingPrivate::takeObservers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#takeObservers

    Returns
    -------

    QPropertyObserverPointer
      A new cute QPropertyObserverPointer around the copy Qt gave back.
      Python owns it.
    """
    #  QPropertyObserverPointer QPropertyBindingPrivate::takeObservers()
    address = self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate13takeObserversEv',
    )
    from . import QPropertyObserverPointer
    return QPropertyObserverPointer._cuteOwning(address)

  def clearDependencyObservers(self) -> None:
    """
    Calls Qt's 'void QPropertyBindingPrivate::clearDependencyObservers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html
    """
    #  void QPropertyBindingPrivate::clearDependencyObservers()
    self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate24clearDependencyObserversEv',
    )

  def allocateDependencyObserver(self) -> QPropertyObserverPointer:
    """
    Calls Qt's 'QPropertyObserverPointer
    QPropertyBindingPrivate::allocateDependencyObserver()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html

    Returns
    -------

    QPropertyObserverPointer
      A new cute QPropertyObserverPointer around the copy Qt gave back.
      Python owns it.
    """
    #  QPropertyObserverPointer
    #      QPropertyBindingPrivate::allocateDependencyObserver()
    address = self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate26allocateDependencyObserverEv',
    )
    from . import QPropertyObserverPointer
    return QPropertyObserverPointer._cuteOwning(address)

  def allocateDependencyObserver_slow(self) -> QPropertyObserverPointer:
    """
    Calls Qt's 'QPropertyObserverPointer
    QPropertyBindingPrivate::allocateDependencyObserver_slow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html

    Returns
    -------

    QPropertyObserverPointer
      A new cute QPropertyObserverPointer around the copy Qt gave back.
      Python owns it.
    """
    #  QPropertyObserverPointer
    #      QPropertyBindingPrivate::allocateDependencyObserver_slow()
    address = self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate31allocateDependencyObserver_slo'
        'wEv',
    )
    from . import QPropertyObserverPointer
    return QPropertyObserverPointer._cuteOwning(address)

  def unlinkAndDeref(self) -> None:
    """
    Calls Qt's 'void QPropertyBindingPrivate::unlinkAndDeref()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#unlinkAndDeref
    """
    #  void QPropertyBindingPrivate::unlinkAndDeref()
    self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate14unlinkAndDerefEv',
    )

  def notifyNonRecursive(self) -> NotificationState:
    """
    Calls Qt's 'NotificationState
    QPropertyBindingPrivate::notifyNonRecursive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#notifyNonRecursive

    Returns
    -------

    NotificationState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'NotificationState(number)' gives.
    """
    #  NotificationState QPropertyBindingPrivate::notifyNonRecursive()
    return QPropertyBindingPrivate.NotificationState(self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate18notifyNonRecursiveEv',
    ))

  def detachFromProperty(self) -> None:
    """
    Calls Qt's 'void QPropertyBindingPrivate::detachFromProperty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingprivate.html#detachFromProperty
    """
    #  void QPropertyBindingPrivate::detachFromProperty()
    self.uglySide.call(
        'ritual_ZN23QPropertyBindingPrivate18detachFromPropertyEv',
    )

  @staticmethod
  def evaluateRecursive(*__, **_) -> Never:
    """
    Qt's 'bool
    QPropertyBindingPrivate::evaluateRecursive(PendingBindingObserverList
    &bindingObservers, QBindingStatus *status)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QPropertyBindingPrivate.evaluateRecursive' has no cute function "
        "yet. Qt's 'bool "
        "QPropertyBindingPrivate::evaluateRecursive(PendingBindingObserverLi"
        "st &bindingObservers, QBindingStatus *status)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def evaluateRecursive_inline(*__, **_) -> Never:
    """
    Qt's 'bool QPropertyBindingPrivate::evaluateRecursive_inline(
    PendingBindingObserverList &bindingObservers, QBindingStatus *status)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPropertyBindingPrivate.evaluateRecursive_inline' has no cute "
        "function yet. Qt's 'bool "
        "QPropertyBindingPrivate::evaluateRecursive_inline(PendingBindingObs"
        "erverList &bindingObservers, QBindingStatus *status)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setError(*__, **_) -> Never:
    """
    Qt's 'void QPropertyBindingPrivate::setError(QPropertyBindingError &&e)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPropertyBindingPrivate.setError' has no cute function yet. Qt's "
        "'void QPropertyBindingPrivate::setError(QPropertyBindingError "
        "&&e)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setStaticObserver(*__, **_) -> Never:
    """
    Qt's 'void QPropertyBindingPrivate::setStaticObserver(QtPrivate::
    QPropertyObserverCallback callback, QtPrivate::QPropertyBindingWrapper
    bindingWrapper)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPropertyBindingPrivate.setStaticObserver' has no cute function "
        "yet. Qt's 'void "
        "QPropertyBindingPrivate::setStaticObserver(QtPrivate::QPropertyObse"
        "rverCallback callback, QtPrivate::QPropertyBindingWrapper "
        "bindingWrapper)': takes a type Python has no way to hand over yet.")
