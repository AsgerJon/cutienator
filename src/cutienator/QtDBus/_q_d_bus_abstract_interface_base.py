"""
QDBusAbstractInterfaceBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusabstractinterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDBusAbstractInterfacePrivate


class QDBusAbstractInterfaceBase(QObject):
  """
  The cute side of Qt's QDBusAbstractInterfaceBase: a plain Python object
  standing in front of one C++ QDBusAbstractInterfaceBase.

  It is built on the cute 'QObject', as Qt's QDBusAbstractInterfaceBase is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusAbstractInterfaceBase that has a ritual and
  that Python can call so far, 1 name in all: 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QDBusAbstractInterfaceBase::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusAbstractInterfaceBase::QDBusAbstractInterfaceBase(
    QDBusAbstractInterfacePrivate &dd, QObject *parent)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QDBusAbstractInterfacePrivate
    *QDBusAbstractInterfaceBase::d_func() const': takes in Python what
    'QDBusAbstractInterfacePrivate *QDBusAbstractInterfaceBase::d_func()'
    takes.

  What to expect
  --------------

  - The C++ QDBusAbstractInterfaceBase is created at the first use, not by
    'QDBusAbstractInterfaceBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusAbstractInterfaceBase.
  - Qt tells when it has removed the C++ QDBusAbstractInterfaceBase. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusAbstractInterfaceBase that has no cute function
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
  __qt_class__ = 'QDBusAbstractInterfaceBase'

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
    Qt's 'QDBusAbstractInterfaceBase::QDBusAbstractInterfaceBase(
    QDBusAbstractInterfacePrivate &dd, QObject *parent)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusAbstractInterfaceBase.__init__' has no cute function yet. "
        "Qt's "
        "'QDBusAbstractInterfaceBase::QDBusAbstractInterfaceBase(QDBusAbstra"
        "ctInterfacePrivate &dd, QObject *parent)': takes a type Python has "
        "no way to hand over yet.")

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

  def d_func(self) -> Optional[QDBusAbstractInterfacePrivate]:
    """
    Calls Qt's 'QDBusAbstractInterfacePrivate
    *QDBusAbstractInterfaceBase::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterfacebase.html#d_func

    Returns
    -------

    Optional[QDBusAbstractInterfacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusAbstractInterfacePrivate *QDBusAbstractInterfaceBase::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QDBusAbstractInterfaceBase6d_funcEv',
    )
    from . import QDBusAbstractInterfacePrivate
    return QDBusAbstractInterfacePrivate._cuteAt(address)
