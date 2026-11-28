"""
QQuickMultiPointHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickmultipointhandler_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickMultiPointHandlerPrivate to be private: it declares the
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
  from typing import Never, Optional

  from . import QQuickMultiPointHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickMultiPointHandler = WAIT['QQuickMultiPointHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMultiPointHandlerPrivate(QQuickPointerDeviceHandlerPrivate):
  """
  The cute side of Qt's QQuickMultiPointHandlerPrivate: a plain Python object
  standing in front of one C++ QQuickMultiPointHandlerPrivate.

  It is built on the cute 'QQuickPointerDeviceHandlerPrivate', as Qt's
  QQuickMultiPointHandlerPrivate is built on Qt's
  QQuickPointerDeviceHandlerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMultiPointHandlerPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func', 'get'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMultiPointHandler
    *QQuickMultiPointHandlerPrivate::q_func() const': takes in Python what
    'QQuickMultiPointHandler *QQuickMultiPointHandlerPrivate::q_func()'
    takes.
  - Qt's 'const QQuickMultiPointHandlerPrivate
    *QQuickMultiPointHandlerPrivate::get(const QQuickMultiPointHandler *q)':
    takes in Python what 'QQuickMultiPointHandlerPrivate
    *QQuickMultiPointHandlerPrivate::get(QQuickMultiPointHandler *q)' takes.
  - Qt's 'QMetaProperty &QQuickMultiPointHandlerPrivate::xMetaProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QMetaProperty &QQuickMultiPointHandlerPrivate::yMetaProperty()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QQuickMultiPointHandlerPrivate is created at the first use, not
    by 'QQuickMultiPointHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMultiPointHandlerPrivate.
  - Each name of Qt's QQuickMultiPointHandlerPrivate that has no cute
    function yet, 'xMetaProperty', 'yMetaProperty', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickMultiPointHandler)
  @overload(NoneType)
  def get(
      q: Optional[QQuickMultiPointHandler],
  ) -> Optional[QQuickMultiPointHandlerPrivate]:
    """
    Calls Qt's 'QQuickMultiPointHandlerPrivate
    *QQuickMultiPointHandlerPrivate::get(QQuickMultiPointHandler *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandlerprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickMultiPointHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMultiPointHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMultiPointHandlerPrivate
    #      *QQuickMultiPointHandlerPrivate::get(QQuickMultiPointHandler *q)
    address = Rituals.call(
        'ritual_ZN30QQuickMultiPointHandlerPrivate3getEP23QQuickMultiPointH'
        'andler',
        CuteMixin._addressOf(q),
    )
    return QQuickMultiPointHandlerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMultiPointHandlerPrivate'

  #  A C++ QQuickMultiPointHandlerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMultiPointHandlerPrivate'

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

  @overload(int, int)
  def __init__(self, minPointCount: int, maxPointCount: int) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMultiPointHandlerPrivate::QQuickMultiPointHandlerPrivate(int
    minPointCount, int maxPointCount)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandlerprivate.html

    Parameters
    ----------

    minPointCount : int
      Passed on as it is.

    maxPointCount : int
      Passed on as it is.
    """
    #  QQuickMultiPointHandlerPrivate::QQuickMultiPointHandlerPrivate(int
    #      minPointCount, int maxPointCount)
    self._noteCreation(QQuickMultiPointHandlerPrivate, lambda: Rituals.call(
        'ritual_ZN30QQuickMultiPointHandlerPrivateC1Eii',
        minPointCount, maxPointCount,
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

  def q_func(self) -> Optional[QQuickMultiPointHandler]:
    """
    Calls Qt's 'QQuickMultiPointHandler
    *QQuickMultiPointHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointhandlerprivate.html#q_func

    Returns
    -------

    Optional[QQuickMultiPointHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMultiPointHandler *QQuickMultiPointHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickMultiPointHandlerPrivate6q_funcEv',
    )
    from . import QQuickMultiPointHandler
    return QQuickMultiPointHandler._cuteAt(address)

  @staticmethod
  def xMetaProperty(*__, **_) -> Never:
    """
    Qt's 'QMetaProperty &QQuickMultiPointHandlerPrivate::xMetaProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandlerPrivate.xMetaProperty' has no cute "
        "function yet. Qt's 'QMetaProperty "
        "&QQuickMultiPointHandlerPrivate::xMetaProperty() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def yMetaProperty(*__, **_) -> Never:
    """
    Qt's 'QMetaProperty &QQuickMultiPointHandlerPrivate::yMetaProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointHandlerPrivate.yMetaProperty' has no cute "
        "function yet. Qt's 'QMetaProperty "
        "&QQuickMultiPointHandlerPrivate::yMetaProperty() const': gives a "
        "type Python has no way to take yet.")
