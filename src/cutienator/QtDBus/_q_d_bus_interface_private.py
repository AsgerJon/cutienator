"""
QDBusInterfacePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusinterface_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusInterfacePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QDBusAbstractInterfacePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDBusInterface


class QDBusInterfacePrivate(QDBusAbstractInterfacePrivate):
  """
  The cute side of Qt's QDBusInterfacePrivate: a plain Python object standing
  in front of one C++ QDBusInterfacePrivate.

  It is built on the cute 'QDBusAbstractInterfacePrivate', as Qt's
  QDBusInterfacePrivate is built on Qt's QDBusAbstractInterfacePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusInterfacePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDBusInterface *QDBusInterfacePrivate::q_func() const': takes
    in Python what 'QDBusInterface *QDBusInterfacePrivate::q_func()' takes.
  - Qt's 'QDBusInterfacePrivate::~QDBusInterfacePrivate()': the destructor:
    Python never removes a C++ QDBusInterfacePrivate.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QDBusConnectionPrivate.

  What to expect
  --------------

  - The C++ QDBusInterfacePrivate is created at the first use, not by
    'QDBusInterfacePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusInterfacePrivate.
  - Each name of Qt's QDBusInterfacePrivate that has no cute function yet,
    '__init__', 'metacall', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusInterfacePrivate'

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
    Qt's 'QDBusInterfacePrivate::QDBusInterfacePrivate(const QString &serv,
    const QString &p, const QString &iface, const QDBusConnection &con)':
    leans on 'QDBusConnectionPrivate::sendWithReply(QDBusMessage const&,
    QDBus::CallMode, int)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusInterfacePrivate.__init__' has no cute function yet. Qt's "
        "'QDBusInterfacePrivate::QDBusInterfacePrivate(const QString &serv, "
        "const QString &p, const QString &iface, const QDBusConnection "
        "&con)': leans on "
        "'QDBusConnectionPrivate::sendWithReply(QDBusMessage const&, "
        "QDBus::CallMode, int)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QDBusInterface]:
    """
    Calls Qt's 'QDBusInterface *QDBusInterfacePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusinterfaceprivate.html#q_func

    Returns
    -------

    Optional[QDBusInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusInterface *QDBusInterfacePrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QDBusInterfacePrivate6q_funcEv')
    from . import QDBusInterface
    return QDBusInterface._cuteAt(address)

  @staticmethod
  def metacall(*__, **_) -> Never:
    """
    Qt's 'int QDBusInterfacePrivate::metacall(QMetaObject::Call c, int id,
    void **argv)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'copyArgument'.
    """
    raise NotImplementedError(
        "'QDBusInterfacePrivate.metacall' has no cute function yet. Qt's "
        "'int QDBusInterfacePrivate::metacall(QMetaObject::Call c, int id, "
        "void **argv)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'copyArgument'.")
