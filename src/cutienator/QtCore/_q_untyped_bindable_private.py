"""
QUntypedBindablePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QUntypedBindablePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QUntypedBindable, QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUntypedBindable = WAIT['QUntypedBindable']


class QUntypedBindablePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUntypedBindablePrivate: a plain Python object
  standing in front of one C++ QUntypedBindablePrivate.

  C++ hands a QUntypedBindablePrivate around as a copy, so every C++
  QUntypedBindablePrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUntypedBindablePrivate that has a ritual and that
  Python can call so far, 2 names in all: 'getInterface', 'getPropertyData'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUntypedBindablePrivate::~QUntypedBindablePrivate()': the
    destructor: Python removes its C++ QUntypedBindablePrivate by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QUntypedBindablePrivate is created at the first use, not by
    'QUntypedBindablePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUntypedBindablePrivate back gives a copy the ritual
    made for Python, in a new cute QUntypedBindablePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUntypedBindable)
  def getInterface(
      bindable: QUntypedBindable,
  ) -> Optional[QtPrivate.QBindableInterface]:
    """
    Calls Qt's 'const QtPrivate::QBindableInterface
    *QUntypedBindablePrivate::getInterface(const QUntypedBindable
    &bindable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedbindableprivate.html#getInterface

    Parameters
    ----------

    bindable : QUntypedBindable
      Passed on as a value: Qt reads the C++ QUntypedBindable, which stays
      Python's own.

    Returns
    -------

    Optional[QtPrivate.QBindableInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtPrivate::QBindableInterface
    #      *QUntypedBindablePrivate::getInterface(const QUntypedBindable
    #      &bindable)
    address = Rituals.call(
        'ritual_ZN23QUntypedBindablePrivate12getInterfaceERK16QUntypedBinda'
        'ble',
        CuteMixin._valueOf(bindable),
    )
    return QtPrivate.QBindableInterface._cuteAt(address)

  @staticmethod
  @overload(QUntypedBindable)
  def getPropertyData(
      bindable: QUntypedBindable,
  ) -> Optional[QUntypedPropertyData]:
    """
    Calls Qt's 'QUntypedPropertyData
    *QUntypedBindablePrivate::getPropertyData(const QUntypedBindable
    &bindable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedbindableprivate.html#getPropertyData

    Parameters
    ----------

    bindable : QUntypedBindable
      Passed on as a value: Qt reads the C++ QUntypedBindable, which stays
      Python's own.

    Returns
    -------

    Optional[QUntypedPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUntypedPropertyData *QUntypedBindablePrivate::getPropertyData(const
    #      QUntypedBindable &bindable)
    address = Rituals.call(
        'ritual_ZN23QUntypedBindablePrivate15getPropertyDataERK16QUntypedBi'
        'ndable',
        CuteMixin._valueOf(bindable),
    )
    from . import QUntypedPropertyData
    return QUntypedPropertyData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUntypedBindablePrivate'

  #  Qt's '~QUntypedBindablePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QUntypedBindablePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QUntypedBindablePrivateD1Ev'

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
