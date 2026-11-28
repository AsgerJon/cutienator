"""
QBindingObserverPtr binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QBindingObserverPtr to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPropertyBindingPrivate, QPropertyObserver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPropertyObserver = WAIT['QPropertyObserver']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBindingObserverPtr(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBindingObserverPtr: a plain Python object standing
  in front of one C++ QBindingObserverPtr.

  What exists
  -----------

  Every function of Qt's QBindingObserverPtr that has a ritual and that
  Python can call so far, 1 name in all: 'binding'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QBindingObserverPtr::swap(QBindingObserverPtr &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QBindingObserverPtr::QBindingObserverPtr(QBindingObserverPtr
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QBindingObserverPtr
    &QBindingObserverPtr::operator=(QBindingObserverPtr &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QBindingObserverPtr::~QBindingObserverPtr()': the destructor:
    Python never removes a C++ QBindingObserverPtr.
  - Qt's 'QPropertyObserver *QBindingObserverPtr::operator->()': an operator
    Python has no name for.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QBindingObserverPtr is created at the first use, not by
    'QBindingObserverPtr(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBindingObserverPtr.
  - Each name of Qt's QBindingObserverPtr that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBindingObserverPtr'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def binding(self) -> Optional[QPropertyBindingPrivate]:
    """
    Calls Qt's 'QPropertyBindingPrivate *QBindingObserverPtr::binding()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbindingobserverptr.html#binding

    Returns
    -------

    Optional[QPropertyBindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyBindingPrivate *QBindingObserverPtr::binding() const
    address = self.uglySide.call('ritual_ZNK19QBindingObserverPtr7bindingEv')
    from . import QPropertyBindingPrivate
    return QPropertyBindingPrivate._cuteAt(address)

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
    'QBindingObserverPtr::QBindingObserverPtr()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbindingobserverptr.html#QBindingObserverPtr
    """
    #  QBindingObserverPtr::QBindingObserverPtr()
    self._noteCreation(QBindingObserverPtr, lambda: Rituals.call(
        'ritual_ZN19QBindingObserverPtrC1Ev',
    ))

  @overload(QPropertyObserver)
  @overload(NoneType)
  def __init__(self, observer: Optional[QPropertyObserver]) -> None:
    """
    Notes what was given, for Qt's
    'QBindingObserverPtr::QBindingObserverPtr(QPropertyObserver *observer)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbindingobserverptr.html#QBindingObserverPtr

    Parameters
    ----------

    observer : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBindingObserverPtr::QBindingObserverPtr(QPropertyObserver *observer)
    self._noteCreation(QBindingObserverPtr, lambda: Rituals.call(
        'ritual_ZN19QBindingObserverPtrC1EP17QPropertyObserver',
        self._addressOf(observer),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QBindingObserverPtr::swap(QBindingObserverPtr &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBindingObserverPtr.swap' has no cute function yet. Qt's 'void "
        "QBindingObserverPtr::swap(QBindingObserverPtr &other)': takes a "
        "type Python has no way to hand over yet.")
