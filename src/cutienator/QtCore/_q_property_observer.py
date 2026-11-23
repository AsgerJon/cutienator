"""
QPropertyObserver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPropertyObserverBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyObserver(QPropertyObserverBase):
  """
  The cute side of Qt's QPropertyObserver: a plain Python object standing in
  front of one C++ QPropertyObserver.

  It is built on the cute 'QPropertyObserverBase', as Qt's QPropertyObserver
  is built on Qt's QPropertyObserverBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPropertyObserver that has a ritual and that Python
  can call so far, 1 name in all: 'aliasedProperty'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPropertyObserver::~QPropertyObserver()': the destructor: Python
    never removes a C++ QPropertyObserver.

  What has no ritual
  ------------------

  7 of the 11 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QPropertyObserver is created at the first use, not by
    'QPropertyObserver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPropertyObserver.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyObserver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def aliasedProperty(self) -> Optional[QUntypedPropertyData]:
    """
    Calls Qt's 'QUntypedPropertyData *QPropertyObserver::aliasedProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserver.html#aliasedProperty

    Returns
    -------

    Optional[QUntypedPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUntypedPropertyData *QPropertyObserver::aliasedProperty() const
    address = self.uglySide.call(
        'ritual_ZNK17QPropertyObserver15aliasedPropertyEv',
    )
    from . import QUntypedPropertyData
    return QUntypedPropertyData._cuteAt(address)

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
    Notes what was given, for Qt's 'QPropertyObserver::QPropertyObserver()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserver.html#QPropertyObserver
    """
    #  QPropertyObserver::QPropertyObserver()
    self._noteCreation(QPropertyObserver, lambda: Rituals.call(
        'ritual_ZN17QPropertyObserverC1Ev',
    ))

  @overload(QUntypedPropertyData)
  @overload(NoneType)
  def __init__(
      self,
      aliasedPropertyPtr: Optional[QUntypedPropertyData],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyObserver::QPropertyObserver(QUntypedPropertyData
    *aliasedPropertyPtr)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyobserver.html#QPropertyObserver

    Parameters
    ----------

    aliasedPropertyPtr : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPropertyObserver::QPropertyObserver(QUntypedPropertyData
    #      *aliasedPropertyPtr)
    self._noteCreation(QPropertyObserver, lambda: Rituals.call(
        'ritual_ZN17QPropertyObserverC1EP20QUntypedPropertyData',
        self._addressOf(aliasedPropertyPtr),
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
