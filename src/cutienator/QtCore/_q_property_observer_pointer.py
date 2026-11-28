"""
QPropertyObserverPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPropertyObserverPointer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPropertyBindingPrivate, QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPropertyBindingPrivate = WAIT['QPropertyBindingPrivate']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyObserverPointer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPropertyObserverPointer: a plain Python object
  standing in front of one C++ QPropertyObserverPointer.

  C++ hands a QPropertyObserverPointer around as a copy, so every C++
  QPropertyObserverPointer behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPropertyObserverPointer that has a ritual and that
  Python can call so far, 10 names in all: 'unlink', 'unlink_fast',
  'setBindingToNotify', 'setBindingToNotify_unsafe', 'notify',
  'noSelfDependencies', '__bool__', 'nextObserver', 'binding',
  'unlink_common'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QPropertyObserverPointer::setChangeHandler(QPropertyObserver::
    ChangeHandler changeHandler)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QPropertyObserverPointer::evaluateBindings(PendingBindingObserverList
    &bindingObservers, QBindingStatus *status)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QPropertyObserverPointer::~QPropertyObserverPointer()': the
    destructor: Python removes its C++ QPropertyObserverPointer by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 leans on 'QPropertyBindingDataPointer.

  What to expect
  --------------

  - The C++ QPropertyObserverPointer is created at the first use, not by
    'QPropertyObserverPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPropertyObserverPointer back gives a copy the ritual
    made for Python, in a new cute QPropertyObserverPointer.
  - Each name of Qt's QPropertyObserverPointer that has no cute function yet,
    'evaluateBindings', 'observeProperty', 'setChangeHandler', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPropertyObserverPointer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Notify(CuteNum, scoped=True):
    """
    The enum 'QPropertyObserverPointer::Notify' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Everything = Kee[int](0)
    OnlyChangeHandlers = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyObserverPointer'

  #  Qt's '~QPropertyObserverPointer()'. Naming it makes this a value class:
  #  Python owns every C++ QPropertyObserverPointer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QPropertyObserverPointerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nextObserver(self) -> QPropertyObserverPointer:
    """
    Calls Qt's 'QPropertyObserverPointer
    QPropertyObserverPointer::nextObserver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#nextObserver

    Returns
    -------

    QPropertyObserverPointer
      A new cute QPropertyObserverPointer around the copy Qt gave back.
      Python owns it.
    """
    #  QPropertyObserverPointer QPropertyObserverPointer::nextObserver()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QPropertyObserverPointer12nextObserverEv',
    )
    return QPropertyObserverPointer._cuteOwning(address)

  def binding(self) -> Optional[QPropertyBindingPrivate]:
    """
    Calls Qt's 'QPropertyBindingPrivate *QPropertyObserverPointer::binding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#binding

    Returns
    -------

    Optional[QPropertyBindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyBindingPrivate *QPropertyObserverPointer::binding() const
    address = self.uglySide.call(
        'ritual_ZNK24QPropertyObserverPointer7bindingEv',
    )
    from . import QPropertyBindingPrivate
    return QPropertyBindingPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPropertyBindingPrivate)
  @overload(NoneType)
  def setBindingToNotify(
      self,
      binding: Optional[QPropertyBindingPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QPropertyObserverPointer::setBindingToNotify(QPropertyBindingPrivate
    *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#setBindingToNotify

    Parameters
    ----------

    binding : Optional[QPropertyBindingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyObserverPointer::setBindingToNotify(
    #      QPropertyBindingPrivate *binding)
    self.uglySide.call(
        'ritual_ZN24QPropertyObserverPointer18setBindingToNotifyEP23QProper'
        'tyBindingPrivate',
        self._addressOf(binding),
    )

  @overload(QPropertyBindingPrivate)
  @overload(NoneType)
  def setBindingToNotify_unsafe(
      self,
      binding: Optional[QPropertyBindingPrivate],
  ) -> None:
    """
    Calls Qt's 'void QPropertyObserverPointer::setBindingToNotify_unsafe(
    QPropertyBindingPrivate *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html

    Parameters
    ----------

    binding : Optional[QPropertyBindingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyObserverPointer::setBindingToNotify_unsafe(
    #      QPropertyBindingPrivate *binding)
    self.uglySide.call(
        'ritual_ZN24QPropertyObserverPointer25setBindingToNotify_unsafeEP23'
        'QPropertyBindingPrivate',
        self._addressOf(binding),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QPropertyObserverPointer::operator bool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#operator bool
    """
    #  bool QPropertyObserverPointer::operator bool() const
    return self.uglySide.call('ritual_ZNK24QPropertyObserverPointercvbEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def unlink(self) -> None:
    """
    Calls Qt's 'void QPropertyObserverPointer::unlink()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#unlink
    """
    #  void QPropertyObserverPointer::unlink()
    self.uglySide.call('ritual_ZN24QPropertyObserverPointer6unlinkEv')

  def unlink_fast(self) -> None:
    """
    Calls Qt's 'void QPropertyObserverPointer::unlink_fast()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#unlink_fast
    """
    #  void QPropertyObserverPointer::unlink_fast()
    self.uglySide.call('ritual_ZN24QPropertyObserverPointer11unlink_fastEv')

  @overload(QUntypedPropertyData)
  @overload(NoneType)
  def notify(self, propertyDataPtr: Optional[QUntypedPropertyData]) -> None:
    """
    Calls Qt's 'void QPropertyObserverPointer::notify(QUntypedPropertyData
    *propertyDataPtr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#notify

    Parameters
    ----------

    propertyDataPtr : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyObserverPointer::notify(QUntypedPropertyData
    #      *propertyDataPtr)
    self.uglySide.call(
        'ritual_ZN24QPropertyObserverPointer6notifyEP20QUntypedPropertyData',
        self._addressOf(propertyDataPtr),
    )

  @overload(QPropertyBindingPrivate)
  @overload(NoneType)
  def noSelfDependencies(
      self,
      binding: Optional[QPropertyBindingPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QPropertyObserverPointer::noSelfDependencies(QPropertyBindingPrivate
    *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#noSelfDependencies

    Parameters
    ----------

    binding : Optional[QPropertyBindingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyObserverPointer::noSelfDependencies(
    #      QPropertyBindingPrivate *binding)
    self.uglySide.call(
        'ritual_ZN24QPropertyObserverPointer18noSelfDependenciesEP23QProper'
        'tyBindingPrivate',
        self._addressOf(binding),
    )

  def unlink_common(self) -> None:
    """
    Calls Qt's 'void QPropertyObserverPointer::unlink_common()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserverpointer.html#unlink_common
    """
    #  void QPropertyObserverPointer::unlink_common()
    self.uglySide.call(
        'ritual_ZN24QPropertyObserverPointer13unlink_commonEv',
    )

  @staticmethod
  def evaluateBindings(*__, **_) -> Never:
    """
    Qt's 'void
    QPropertyObserverPointer::evaluateBindings(PendingBindingObserverList
    &bindingObservers, QBindingStatus *status)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QPropertyObserverPointer.evaluateBindings' has no cute function "
        "yet. Qt's 'void "
        "QPropertyObserverPointer::evaluateBindings(PendingBindingObserverLi"
        "st &bindingObservers, QBindingStatus *status)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def observeProperty(*__, **_) -> Never:
    """
    Qt's 'void
    QPropertyObserverPointer::observeProperty(QPropertyBindingDataPointer
    property)': leans on
    'QPropertyBindingDataPointer::addObserver(QPropertyObserver*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QPropertyObserverPointer.observeProperty' has no cute function "
        "yet. Qt's 'void "
        "QPropertyObserverPointer::observeProperty(QPropertyBindingDataPoint"
        "er property)': leans on "
        "'QPropertyBindingDataPointer::addObserver(QPropertyObserver*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setChangeHandler(*__, **_) -> Never:
    """
    Qt's 'void QPropertyObserverPointer::setChangeHandler(QPropertyObserver::
    ChangeHandler changeHandler)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QPropertyObserverPointer.setChangeHandler' has no cute function "
        "yet. Qt's 'void "
        "QPropertyObserverPointer::setChangeHandler(QPropertyObserver::Chang"
        "eHandler changeHandler)': takes a type Python has no way to hand "
        "over yet.")
