"""
QPropertyBindingDataPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPropertyBindingDataPointer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPropertyBindingPrivate, QPropertyObserver
  from . import QPropertyObserverPointer, QPropertyProxyBindingData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPropertyObserver = WAIT['QPropertyObserver']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyBindingDataPointer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPropertyBindingDataPointer: a plain Python object
  standing in front of one C++ QPropertyBindingDataPointer.

  C++ hands a QPropertyBindingDataPointer around as a copy, so every C++
  QPropertyBindingDataPointer behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QPropertyBindingDataPointer that has a ritual and
  that Python can call so far, 7 names in all: 'binding', 'setObservers',
  'fixupAfterMove', 'setFirstObserver', 'firstObserver', 'proxyData',
  'observerCount'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPropertyBindingDataPointer::~QPropertyBindingDataPointer()': the
    destructor: Python removes its C++ QPropertyBindingDataPointer by it, and
    has no other use for it.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 1 a template; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QPropertyBindingDataPointer is created at the first use, not by
    'QPropertyBindingDataPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPropertyBindingDataPointer back gives a copy the
    ritual made for Python, in a new cute QPropertyBindingDataPointer.
  - Each name of Qt's QPropertyBindingDataPointer that has no cute function
    yet, 'addObserver', 'get', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QtPrivate.QPropertyBindingData'])
  @overload(NoneType)
  def fixupAfterMove(ptr: Optional[QtPrivate.QPropertyBindingData]) -> None:
    """
    Calls Qt's 'void QPropertyBindingDataPointer::fixupAfterMove(QtPrivate::
    QPropertyBindingData *ptr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingdatapointer.html#fixupAfterMove

    Parameters
    ----------

    ptr : Optional[QtPrivate.QPropertyBindingData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyBindingDataPointer::fixupAfterMove(QtPrivate::
    #      QPropertyBindingData *ptr)
    Rituals.call(
        'ritual_ZN27QPropertyBindingDataPointer14fixupAfterMoveEPN9QtPrivat'
        'e20QPropertyBindingDataE',
        CuteMixin._addressOf(ptr),
    )

  @staticmethod
  @overload(WAIT['QtPrivate.QPropertyBindingData'])
  @overload(NoneType)
  def proxyData(
      ptr: Optional[QtPrivate.QPropertyBindingData],
  ) -> Optional[QPropertyProxyBindingData]:
    """
    Calls Qt's 'QPropertyProxyBindingData
    *QPropertyBindingDataPointer::proxyData(QtPrivate::QPropertyBindingData
    *ptr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingdatapointer.html#proxyData

    Parameters
    ----------

    ptr : Optional[QtPrivate.QPropertyBindingData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPropertyProxyBindingData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyProxyBindingData
    #      *QPropertyBindingDataPointer::proxyData(QtPrivate::
    #      QPropertyBindingData *ptr)
    address = Rituals.call(
        'ritual_ZN27QPropertyBindingDataPointer9proxyDataEPN9QtPrivate20QPr'
        'opertyBindingDataE',
        CuteMixin._addressOf(ptr),
    )
    from . import QPropertyProxyBindingData
    return QPropertyProxyBindingData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyBindingDataPointer'

  #  Qt's '~QPropertyBindingDataPointer()'. Naming it makes this a value
  #  class: Python owns every C++ QPropertyBindingDataPointer behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QPropertyBindingDataPointerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def binding(self) -> Optional[QPropertyBindingPrivate]:
    """
    Calls Qt's 'QPropertyBindingPrivate
    *QPropertyBindingDataPointer::binding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingdatapointer.html#binding

    Returns
    -------

    Optional[QPropertyBindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyBindingPrivate *QPropertyBindingDataPointer::binding() const
    address = self.uglySide.call(
        'ritual_ZNK27QPropertyBindingDataPointer7bindingEv',
    )
    from . import QPropertyBindingPrivate
    return QPropertyBindingPrivate._cuteAt(address)

  def firstObserver(self) -> QPropertyObserverPointer:
    """
    Calls Qt's 'QPropertyObserverPointer
    QPropertyBindingDataPointer::firstObserver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingdatapointer.html#firstObserver

    Returns
    -------

    QPropertyObserverPointer
      A new cute QPropertyObserverPointer around the copy Qt gave back.
      Python owns it.
    """
    #  QPropertyObserverPointer QPropertyBindingDataPointer::firstObserver()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QPropertyBindingDataPointer13firstObserverEv',
    )
    from . import QPropertyObserverPointer
    return QPropertyObserverPointer._cuteOwning(address)

  def observerCount(self) -> int:
    """
    Calls Qt's 'int QPropertyBindingDataPointer::observerCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingdatapointer.html#observerCount
    """
    #  int QPropertyBindingDataPointer::observerCount() const
    return self.uglySide.call(
        'ritual_ZNK27QPropertyBindingDataPointer13observerCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPropertyObserver)
  @overload(NoneType)
  def setObservers(self, observer: Optional[QPropertyObserver]) -> None:
    """
    Calls Qt's 'void
    QPropertyBindingDataPointer::setObservers(QPropertyObserver *observer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingdatapointer.html#setObservers

    Parameters
    ----------

    observer : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyBindingDataPointer::setObservers(QPropertyObserver
    #      *observer)
    self.uglySide.call(
        'ritual_ZN27QPropertyBindingDataPointer12setObserversEP17QPropertyO'
        'bserver',
        self._addressOf(observer),
    )

  @overload(QPropertyObserver)
  @overload(NoneType)
  def setFirstObserver(self, observer: Optional[QPropertyObserver]) -> None:
    """
    Calls Qt's 'void
    QPropertyBindingDataPointer::setFirstObserver(QPropertyObserver
    *observer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingdatapointer.html#setFirstObserver

    Parameters
    ----------

    observer : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyBindingDataPointer::setFirstObserver(QPropertyObserver
    #      *observer)
    self.uglySide.call(
        'ritual_ZN27QPropertyBindingDataPointer16setFirstObserverEP17QPrope'
        'rtyObserver',
        self._addressOf(observer),
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

  @staticmethod
  def addObserver(*__, **_) -> Never:
    """
    Qt's 'void QPropertyBindingDataPointer::addObserver(QPropertyObserver
    *observer)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'QPropertyBindingData'; did you mean 'QtPrivate::QPropertyBindingData'?.
    """
    raise NotImplementedError(
        "'QPropertyBindingDataPointer.addObserver' has no cute function "
        "yet. Qt's 'void "
        "QPropertyBindingDataPointer::addObserver(QPropertyObserver "
        "*observer)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QPropertyBindingData'; did you mean "
        "'QtPrivate::QPropertyBindingData'?.")

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QPropertyBindingDataPointer::get': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QPropertyBindingDataPointer.get' has no cute function yet. Qt's "
        "'QPropertyBindingDataPointer::get': a template: a pattern and no "
        "single function.")
