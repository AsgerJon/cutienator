"""
QQuickWheelHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwheelhandler_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickWheelHandlerPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickSinglePointHandlerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickWheelHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWheelHandler = WAIT['QQuickWheelHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWheelHandlerPrivate(QQuickSinglePointHandlerPrivate):
  """
  The cute side of Qt's QQuickWheelHandlerPrivate: a plain Python object
  standing in front of one C++ QQuickWheelHandlerPrivate.

  It is built on the cute 'QQuickSinglePointHandlerPrivate', as Qt's
  QQuickWheelHandlerPrivate is built on Qt's QQuickSinglePointHandlerPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWheelHandlerPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'get'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickWheelHandler *QQuickWheelHandlerPrivate::q_func()
    const': takes in Python what 'QQuickWheelHandler
    *QQuickWheelHandlerPrivate::q_func()' takes.
  - Qt's 'const QQuickWheelHandlerPrivate
    *QQuickWheelHandlerPrivate::get(const QQuickWheelHandler *q)': takes in
    Python what 'QQuickWheelHandlerPrivate
    *QQuickWheelHandlerPrivate::get(QQuickWheelHandler *q)' takes.
  - Qt's 'QMetaProperty &QQuickWheelHandlerPrivate::targetMetaProperty()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QQuickWheelHandlerPrivate is created at the first use, not by
    'QQuickWheelHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWheelHandlerPrivate.
  - Each name of Qt's QQuickWheelHandlerPrivate that has no cute function
    yet, 'targetMetaProperty', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickWheelHandler)
  @overload(NoneType)
  def get(
      q: Optional[QQuickWheelHandler],
  ) -> Optional[QQuickWheelHandlerPrivate]:
    """
    Calls Qt's 'QQuickWheelHandlerPrivate
    *QQuickWheelHandlerPrivate::get(QQuickWheelHandler *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandlerprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickWheelHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickWheelHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWheelHandlerPrivate
    #      *QQuickWheelHandlerPrivate::get(QQuickWheelHandler *q)
    address = Rituals.call(
        'ritual_ZN25QQuickWheelHandlerPrivate3getEP18QQuickWheelHandler',
        CuteMixin._addressOf(q),
    )
    return QQuickWheelHandlerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWheelHandlerPrivate'

  #  A C++ QQuickWheelHandlerPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWheelHandlerPrivate'

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
    'QQuickWheelHandlerPrivate::QQuickWheelHandlerPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandlerprivate.html
    """
    #  QQuickWheelHandlerPrivate::QQuickWheelHandlerPrivate()
    self._noteCreation(QQuickWheelHandlerPrivate, lambda: Rituals.call(
        'ritual_ZN25QQuickWheelHandlerPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickWheelHandler]:
    """
    Calls Qt's 'QQuickWheelHandler *QQuickWheelHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandlerprivate.html#q_func

    Returns
    -------

    Optional[QQuickWheelHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWheelHandler *QQuickWheelHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickWheelHandlerPrivate6q_funcEv',
    )
    from . import QQuickWheelHandler
    return QQuickWheelHandler._cuteAt(address)

  @staticmethod
  def targetMetaProperty(*__, **_) -> Never:
    """
    Qt's 'QMetaProperty &QQuickWheelHandlerPrivate::targetMetaProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickWheelHandlerPrivate.targetMetaProperty' has no cute "
        "function yet. Qt's 'QMetaProperty "
        "&QQuickWheelHandlerPrivate::targetMetaProperty() const': gives a "
        "type Python has no way to take yet.")
