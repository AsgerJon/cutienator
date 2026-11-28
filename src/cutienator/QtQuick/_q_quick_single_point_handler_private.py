"""
QQuickSinglePointHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksinglepointhandler_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickSinglePointHandlerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickPointerDeviceHandlerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickSinglePointHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickSinglePointHandler = WAIT['QQuickSinglePointHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSinglePointHandlerPrivate(QQuickPointerDeviceHandlerPrivate):
  """
  The cute side of Qt's QQuickSinglePointHandlerPrivate: a plain Python
  object standing in front of one C++ QQuickSinglePointHandlerPrivate.

  It is built on the cute 'QQuickPointerDeviceHandlerPrivate', as Qt's
  QQuickSinglePointHandlerPrivate is built on Qt's
  QQuickPointerDeviceHandlerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSinglePointHandlerPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'q_func', 'get', 'reset'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickSinglePointHandler
    *QQuickSinglePointHandlerPrivate::q_func() const': takes in Python what
    'QQuickSinglePointHandler *QQuickSinglePointHandlerPrivate::q_func()'
    takes.
  - Qt's 'const QQuickSinglePointHandlerPrivate
    *QQuickSinglePointHandlerPrivate::get(const QQuickSinglePointHandler
    *q)': takes in Python what 'QQuickSinglePointHandlerPrivate
    *QQuickSinglePointHandlerPrivate::get(QQuickSinglePointHandler *q)'
    takes.

  What to expect
  --------------

  - The C++ QQuickSinglePointHandlerPrivate is created at the first use, not
    by 'QQuickSinglePointHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSinglePointHandlerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickSinglePointHandler)
  @overload(NoneType)
  def get(
      q: Optional[QQuickSinglePointHandler],
  ) -> Optional[QQuickSinglePointHandlerPrivate]:
    """
    Calls Qt's 'QQuickSinglePointHandlerPrivate
    *QQuickSinglePointHandlerPrivate::get(QQuickSinglePointHandler *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandlerprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickSinglePointHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSinglePointHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSinglePointHandlerPrivate
    #      *QQuickSinglePointHandlerPrivate::get(QQuickSinglePointHandler *q)
    address = Rituals.call(
        'ritual_ZN31QQuickSinglePointHandlerPrivate3getEP24QQuickSinglePoin'
        'tHandler',
        CuteMixin._addressOf(q),
    )
    return QQuickSinglePointHandlerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSinglePointHandlerPrivate'

  #  A C++ QQuickSinglePointHandlerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSinglePointHandlerPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSinglePointHandlerPrivate::QQuickSinglePointHandlerPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandlerprivate.html
    """
    #  QQuickSinglePointHandlerPrivate::QQuickSinglePointHandlerPrivate()
    self._noteCreation(QQuickSinglePointHandlerPrivate, lambda: Rituals.call(
        'ritual_ZN31QQuickSinglePointHandlerPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickSinglePointHandler]:
    """
    Calls Qt's 'QQuickSinglePointHandler
    *QQuickSinglePointHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandlerprivate.html#q_func

    Returns
    -------

    Optional[QQuickSinglePointHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSinglePointHandler *QQuickSinglePointHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN31QQuickSinglePointHandlerPrivate6q_funcEv',
    )
    from . import QQuickSinglePointHandler
    return QQuickSinglePointHandler._cuteAt(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickSinglePointHandlerPrivate::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandlerprivate.html#reset
    """
    #  void QQuickSinglePointHandlerPrivate::reset()
    self.uglySide.call('ritual_ZN31QQuickSinglePointHandlerPrivate5resetEv')
