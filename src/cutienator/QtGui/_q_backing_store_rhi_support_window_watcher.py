"""
QBackingStoreRhiSupportWindowWatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qbackingstorerhisupport_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBackingStoreRhiSupportWindowWatcher to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent
  from . import QBackingStoreRhiSupport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBackingStoreRhiSupport = WAIT['QBackingStoreRhiSupport']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBackingStoreRhiSupportWindowWatcher(QObject):
  """
  The cute side of Qt's QBackingStoreRhiSupportWindowWatcher: a plain Python
  object standing in front of one C++ QBackingStoreRhiSupportWindowWatcher.

  It is built on the cute 'QObject', as Qt's
  QBackingStoreRhiSupportWindowWatcher is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBackingStoreRhiSupportWindowWatcher that has a
  ritual and that Python can call so far, 1 name in all: 'eventFilter'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QBackingStoreRhiSupportWindowWatcher is created at the first use,
    not by 'QBackingStoreRhiSupportWindowWatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBackingStoreRhiSupportWindowWatcher.
  - Qt tells when it has removed the C++
    QBackingStoreRhiSupportWindowWatcher. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBackingStoreRhiSupportWindowWatcher'

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

  @overload(QBackingStoreRhiSupport)
  @overload(NoneType)
  def __init__(self, rhiSupport: Optional[QBackingStoreRhiSupport]) -> None:
    """
    Notes what was given, for Qt's 'QBackingStoreRhiSupportWindowWatcher::
    QBackingStoreRhiSupportWindowWatcher(QBackingStoreRhiSupport
    *rhiSupport)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupportwindowwatcher.html

    Parameters
    ----------

    rhiSupport : Optional[QBackingStoreRhiSupport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBackingStoreRhiSupportWindowWatcher::
    #      QBackingStoreRhiSupportWindowWatcher(QBackingStoreRhiSupport
    #      *rhiSupport)
    self._noteCreation(
        QBackingStoreRhiSupportWindowWatcher, lambda: Rituals.call(
            'ritual_ZN36QBackingStoreRhiSupportWindowWatcherC1EP23QBackingS'
            'toreRhiSupport',
            self._addressOf(rhiSupport),
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      obj: Optional[QObject],
      ev: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QBackingStoreRhiSupportWindowWatcher::eventFilter(QObject *obj, QEvent
    *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupportwindowwatcher.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ev : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBackingStoreRhiSupportWindowWatcher::eventFilter(QObject *obj,
    #      QEvent *ev)
    ritual = (
        'ritual_ZN36QBackingStoreRhiSupportWindowWatcher11eventFilterEP7QOb'
        'jectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QBackingStoreRhiSupportWindowWatcher11eventFilter'
          'EP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(obj, 'QObject'), self._addressOf(ev),
    )
