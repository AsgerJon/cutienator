"""
QtPrivate::CompatPropertySafePoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtPrivate::CompatPropertySafePoint to be private: it declares the
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

  from . import QBindingStatus, QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBindingStatus = WAIT['QBindingStatus']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CompatPropertySafePoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::CompatPropertySafePoint: a plain Python
  object standing in front of one C++ QtPrivate::CompatPropertySafePoint.

  C++ hands a QtPrivate::CompatPropertySafePoint around as a copy, so every
  C++ QtPrivate::CompatPropertySafePoint behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QtPrivate::CompatPropertySafePoint yet. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::CompatPropertySafePoint::~CompatPropertySafePoint()':
    the destructor: Python removes its C++ QtPrivate::CompatPropertySafePoint
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::CompatPropertySafePoint is created at the first use,
    not by 'QtPrivate::CompatPropertySafePoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::CompatPropertySafePoint back gives a copy
    the ritual made for Python, in a new cute
    QtPrivate::CompatPropertySafePoint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::CompatPropertySafePoint'

  #  Qt's '~QtPrivate::CompatPropertySafePoint()'. Naming it makes this a
  #  value class: Python owns every C++ QtPrivate::CompatPropertySafePoint
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate23CompatPropertySafePointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QBindingStatus, QUntypedPropertyData)
  @overload(QBindingStatus, NoneType)
  @overload(NoneType, QUntypedPropertyData)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      status: Optional[QBindingStatus],
      property: Optional[QUntypedPropertyData],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::CompatPropertySafePoint::CompatPropertySafePoint(
    QBindingStatus *status, QUntypedPropertyData *property)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-compatpropertysafepoint.html

    Parameters
    ----------

    status : Optional[QBindingStatus]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtPrivate::CompatPropertySafePoint::CompatPropertySafePoint(
    #      QBindingStatus *status, QUntypedPropertyData *property)
    self._noteCreation(CompatPropertySafePoint, lambda: Rituals.call(
        'ritual_ZN9QtPrivate23CompatPropertySafePointC1EP14QBindingStatusP2'
        '0QUntypedPropertyData',
        self._addressOf(status), self._addressOf(property),
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
