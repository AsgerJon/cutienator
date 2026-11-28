"""
QtROExternalIoDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnectionfactories_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtROExternalIoDevicePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QtROIoDeviceBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QtROExternalIoDevice


class QtROExternalIoDevicePrivate(QtROIoDeviceBasePrivate):
  """
  The cute side of Qt's QtROExternalIoDevicePrivate: a plain Python object
  standing in front of one C++ QtROExternalIoDevicePrivate.

  It is built on the cute 'QtROIoDeviceBasePrivate', as Qt's
  QtROExternalIoDevicePrivate is built on Qt's QtROIoDeviceBasePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtROExternalIoDevicePrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QtROExternalIoDevice *QtROExternalIoDevicePrivate::q_func()
    const': takes in Python what 'QtROExternalIoDevice
    *QtROExternalIoDevicePrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on 'QtROIoDeviceBasePrivate.

  What to expect
  --------------

  - The C++ QtROExternalIoDevicePrivate is created at the first use, not by
    'QtROExternalIoDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtROExternalIoDevicePrivate.
  - Each name of Qt's QtROExternalIoDevicePrivate that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROExternalIoDevicePrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtROExternalIoDevicePrivate::QtROExternalIoDevicePrivate(QIODevice
    *device)': leans on 'QtROIoDeviceBasePrivate::QtROIoDeviceBasePrivate()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QtROExternalIoDevicePrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QtROExternalIoDevicePrivate::QtROExternalIoDevicePrivate(QIODevice"
        " *device)': leans on "
        "'QtROIoDeviceBasePrivate::QtROIoDeviceBasePrivate()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def q_func(self) -> Optional[QtROExternalIoDevice]:
    """
    Calls Qt's 'QtROExternalIoDevice *QtROExternalIoDevicePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroexternaliodeviceprivate.html#q_func

    Returns
    -------

    Optional[QtROExternalIoDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROExternalIoDevice *QtROExternalIoDevicePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QtROExternalIoDevicePrivate6q_funcEv',
    )
    from . import QtROExternalIoDevice
    return QtROExternalIoDevice._cuteAt(address)
