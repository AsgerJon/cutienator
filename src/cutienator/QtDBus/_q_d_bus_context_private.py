"""
QDBusContextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbuscontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusContextPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QDBusConnection, QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']
  QDBusMessage = WAIT['QDBusMessage']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusContextPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusContextPrivate: a plain Python object standing
  in front of one C++ QDBusContextPrivate.

  C++ hands a QDBusContextPrivate around as a copy, so every C++
  QDBusContextPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusContextPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'set'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusContextPrivate::~QDBusContextPrivate()': the destructor:
    Python removes its C++ QDBusContextPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QDBusContextPrivate is created at the first use, not by
    'QDBusContextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusContextPrivate back gives a copy the ritual made
    for Python, in a new cute QDBusContextPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject, THIS)
  @overload(QObject, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def set(
      obj: Optional[QObject],
      newContext: Optional[QDBusContextPrivate],
  ) -> Optional[QDBusContextPrivate]:
    """
    Calls Qt's 'QDBusContextPrivate *QDBusContextPrivate::set(QObject *obj,
    QDBusContextPrivate *newContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontextprivate.html#set

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newContext : Optional[QDBusContextPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDBusContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusContextPrivate *QDBusContextPrivate::set(QObject *obj,
    #      QDBusContextPrivate *newContext)
    address = Rituals.call(
        'ritual_ZN19QDBusContextPrivate3setEP7QObjectPS_',
        CuteMixin._addressOf(obj, 'QObject'),
        CuteMixin._addressOf(newContext),
    )
    return QDBusContextPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusContextPrivate'

  #  Qt's '~QDBusContextPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QDBusContextPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDBusContextPrivateD1Ev'

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

  @overload(QDBusConnection, QDBusMessage)
  def __init__(self, conn: QDBusConnection, msg: QDBusMessage) -> None:
    """
    Notes what was given, for Qt's
    'QDBusContextPrivate::QDBusContextPrivate(const QDBusConnection &conn,
    const QDBusMessage &msg)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuscontextprivate.html#QDBusContextPrivate

    Parameters
    ----------

    conn : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  QDBusContextPrivate::QDBusContextPrivate(const QDBusConnection &conn,
    #      const QDBusMessage &msg)
    self._noteCreation(QDBusContextPrivate, lambda: Rituals.call(
        'ritual_ZN19QDBusContextPrivateC1ERK15QDBusConnectionRK12QDBusMessa'
        'ge',
        self._valueOf(conn), self._valueOf(msg),
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
