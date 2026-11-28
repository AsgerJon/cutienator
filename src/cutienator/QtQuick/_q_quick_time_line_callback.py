"""
QQuickTimeLineCallback binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTimeLineCallback to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickTimeLineObject


class QQuickTimeLineCallback(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickTimeLineCallback: a plain Python object
  standing in front of one C++ QQuickTimeLineCallback.

  C++ hands a QQuickTimeLineCallback around as a copy, so every C++
  QQuickTimeLineCallback behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickTimeLineCallback that has a ritual and that
  Python can call so far, 1 name in all: 'callbackObject'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickTimeLineCallback::QQuickTimeLineCallback(QQuickTimeLineObject
    *b, Callback a1, void *a2)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQuickTimeLineCallback &QQuickTimeLineCallback::operator=(const
    QQuickTimeLineCallback &o)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQuickTimeLineCallback::~QQuickTimeLineCallback()': the destructor:
    Python removes its C++ QQuickTimeLineCallback by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickTimeLineCallback is created at the first use, not by
    'QQuickTimeLineCallback(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickTimeLineCallback back gives a copy the ritual
    made for Python, in a new cute QQuickTimeLineCallback.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTimeLineCallback'

  #  Qt's '~QQuickTimeLineCallback()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickTimeLineCallback behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QQuickTimeLineCallbackD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def callbackObject(self) -> Optional[QQuickTimeLineObject]:
    """
    Calls Qt's 'QQuickTimeLineObject
    *QQuickTimeLineCallback::callbackObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelinecallback.html#callbackObject

    Returns
    -------

    Optional[QQuickTimeLineObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTimeLineObject *QQuickTimeLineCallback::callbackObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTimeLineCallback14callbackObjectEv',
    )
    from . import QQuickTimeLineObject
    return QQuickTimeLineObject._cuteAt(address)

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
    'QQuickTimeLineCallback::QQuickTimeLineCallback()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelinecallback.html#QQuickTimeLineCallback
    """
    #  QQuickTimeLineCallback::QQuickTimeLineCallback()
    self._noteCreation(QQuickTimeLineCallback, lambda: Rituals.call(
        'ritual_ZN22QQuickTimeLineCallbackC1Ev',
    ))

  @overload(THIS)
  def __init__(self, o: QQuickTimeLineCallback) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTimeLineCallback::QQuickTimeLineCallback(const
    QQuickTimeLineCallback &o)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelinecallback.html#QQuickTimeLineCallback

    Parameters
    ----------

    o : QQuickTimeLineCallback
      Passed on as a value: Qt reads the C++ QQuickTimeLineCallback, which
      stays Python's own.
    """
    #  QQuickTimeLineCallback::QQuickTimeLineCallback(const
    #      QQuickTimeLineCallback &o)
    self._noteCreation(QQuickTimeLineCallback, lambda: Rituals.call(
        'ritual_ZN22QQuickTimeLineCallbackC1ERKS_', self._valueOf(o),
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
