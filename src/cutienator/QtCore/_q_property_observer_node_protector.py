"""
QPropertyObserverNodeProtector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPropertyObserverNodeProtector to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPropertyObserver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPropertyObserver = WAIT['QPropertyObserver']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyObserverNodeProtector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPropertyObserverNodeProtector: a plain Python object
  standing in front of one C++ QPropertyObserverNodeProtector.

  What exists
  -----------

  Every function of Qt's QPropertyObserverNodeProtector that has a ritual and
  that Python can call so far, 1 name in all: 'next'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPropertyObserverNodeProtector::~QPropertyObserverNodeProtector()':
    the destructor: Python never removes a C++
    QPropertyObserverNodeProtector.

  What has no ritual
  ------------------

  4 of the 7 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPropertyObserverNodeProtector is created at the first use, not
    by 'QPropertyObserverNodeProtector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPropertyObserverNodeProtector.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyObserverNodeProtector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def next(self) -> Optional[QPropertyObserver]:
    """
    Calls Qt's 'QPropertyObserver *QPropertyObserverNodeProtector::next()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobservernodeprotector.html#next

    Returns
    -------

    Optional[QPropertyObserver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyObserver *QPropertyObserverNodeProtector::next() const
    address = self.uglySide.call(
        'ritual_ZNK30QPropertyObserverNodeProtector4nextEv',
    )
    from . import QPropertyObserver
    return QPropertyObserver._cuteAt(address)

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

  @overload(QPropertyObserver)
  @overload(NoneType)
  def __init__(self, observer: Optional[QPropertyObserver]) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyObserverNodeProtector::QPropertyObserverNodeProtector(
    QPropertyObserver *observer)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobservernodeprotector.html

    Parameters
    ----------

    observer : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPropertyObserverNodeProtector::QPropertyObserverNodeProtector(
    #      QPropertyObserver *observer)
    self._noteCreation(QPropertyObserverNodeProtector, lambda: Rituals.call(
        'ritual_ZN30QPropertyObserverNodeProtectorC1EP17QPropertyObserver',
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
