"""
QQuickPointerDeviceHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpointerdevicehandler_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPointerDeviceHandlerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickPointerHandlerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickPointerDeviceHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPointerDeviceHandler = WAIT['QQuickPointerDeviceHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPointerDeviceHandlerPrivate(QQuickPointerHandlerPrivate):
  """
  The cute side of Qt's QQuickPointerDeviceHandlerPrivate: a plain Python
  object standing in front of one C++ QQuickPointerDeviceHandlerPrivate.

  It is built on the cute 'QQuickPointerHandlerPrivate', as Qt's
  QQuickPointerDeviceHandlerPrivate is built on Qt's
  QQuickPointerHandlerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPointerDeviceHandlerPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'q_func', 'get'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPointerDeviceHandler
    *QQuickPointerDeviceHandlerPrivate::q_func() const': takes in Python what
    'QQuickPointerDeviceHandler *QQuickPointerDeviceHandlerPrivate::q_func()'
    takes.
  - Qt's 'const QQuickPointerDeviceHandlerPrivate
    *QQuickPointerDeviceHandlerPrivate::get(const QQuickPointerDeviceHandler
    *q)': takes in Python what 'QQuickPointerDeviceHandlerPrivate
    *QQuickPointerDeviceHandlerPrivate::get(QQuickPointerDeviceHandler *q)'
    takes.

  What to expect
  --------------

  - The C++ QQuickPointerDeviceHandlerPrivate is created at the first use,
    not by 'QQuickPointerDeviceHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPointerDeviceHandlerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickPointerDeviceHandler)
  @overload(NoneType)
  def get(
      q: Optional[QQuickPointerDeviceHandler],
  ) -> Optional[QQuickPointerDeviceHandlerPrivate]:
    """
    Calls Qt's 'QQuickPointerDeviceHandlerPrivate
    *QQuickPointerDeviceHandlerPrivate::get(QQuickPointerDeviceHandler *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandlerprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickPointerDeviceHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPointerDeviceHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointerDeviceHandlerPrivate
    #      *QQuickPointerDeviceHandlerPrivate::get(QQuickPointerDeviceHandler
    #      *q)
    address = Rituals.call(
        'ritual_ZN33QQuickPointerDeviceHandlerPrivate3getEP26QQuickPointerD'
        'eviceHandler',
        CuteMixin._addressOf(q),
    )
    return QQuickPointerDeviceHandlerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPointerDeviceHandlerPrivate'

  #  A C++ QQuickPointerDeviceHandlerPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPointerDeviceHandlerPrivate'

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

  def q_func(self) -> Optional[QQuickPointerDeviceHandler]:
    """
    Calls Qt's 'QQuickPointerDeviceHandler
    *QQuickPointerDeviceHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandlerprivate.html#q_func

    Returns
    -------

    Optional[QQuickPointerDeviceHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointerDeviceHandler
    #      *QQuickPointerDeviceHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN33QQuickPointerDeviceHandlerPrivate6q_funcEv',
    )
    from . import QQuickPointerDeviceHandler
    return QQuickPointerDeviceHandler._cuteAt(address)
