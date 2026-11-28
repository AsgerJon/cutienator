"""
QQuickDropEventEx binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDropEventEx to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QDropEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDropEventEx(QDropEvent):
  """
  The cute side of Qt's QQuickDropEventEx: a plain Python object standing in
  front of one C++ QQuickDropEventEx.

  It is built on the cute 'QDropEvent', as Qt's QQuickDropEventEx is built on
  Qt's QDropEvent, and has everything that class has.

  C++ hands a QQuickDropEventEx around as a copy, so every C++
  QQuickDropEventEx behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickDropEventEx that has a ritual and that Python
  can call so far, 1 name in all: 'setProposedAction'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickDropEventEx::copyActions(const QDropEvent &from)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQuickDropEventEx::copyActions(QDropEvent *to, const
    QDropEvent &from)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickDropEventEx::~QQuickDropEventEx()': the destructor: Python
    removes its C++ QQuickDropEventEx by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickDropEventEx is created at the first use, not by
    'QQuickDropEventEx(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDropEventEx back gives a copy the ritual made
    for Python, in a new cute QQuickDropEventEx.
  - Each name of Qt's QQuickDropEventEx that has no cute function yet,
    'copyActions', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QQuickDropEventEx'

  #  A C++ QQuickDropEventEx Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDropEventEx'

  #  Qt's '~QQuickDropEventEx()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickDropEventEx behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQuickDropEventExD1Ev'

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

  @overload(Qt.DropAction)
  def setProposedAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QQuickDropEventEx::setProposedAction(Qt::DropAction
    action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdropeventex.html#setProposedAction

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QQuickDropEventEx::setProposedAction(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN17QQuickDropEventEx17setProposedActionEN2Qt10DropActionE',
        action.value,
    )

  @staticmethod
  @overload(QDropEvent, Qt.DropAction)
  @overload(NoneType, Qt.DropAction)
  def setProposedAction(
      event: Optional[QDropEvent],
      action: Qt.DropAction,
  ) -> None:
    """
    Calls Qt's 'void QQuickDropEventEx::setProposedAction(QDropEvent *event,
    Qt::DropAction action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdropeventex.html#setProposedAction

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QQuickDropEventEx::setProposedAction(QDropEvent *event,
    #      Qt::DropAction action)
    Rituals.call(
        'ritual_ZN17QQuickDropEventEx17setProposedActionEP10QDropEventN2Qt1'
        '0DropActionE',
        CuteMixin._addressOf(event), action.value,
    )

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

  @staticmethod
  def copyActions(*__, **_) -> Never:
    """
    - Qt's 'void QQuickDropEventEx::copyActions(const QDropEvent &from)':
      takes a type Python has no way to hand over yet.
    - Qt's 'void QQuickDropEventEx::copyActions(QDropEvent *to, const
      QDropEvent &from)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDropEventEx.copyActions' has no cute function yet. Qt's "
        "'void QQuickDropEventEx::copyActions(const QDropEvent &from)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QQuickDropEventEx::copyActions(QDropEvent *to, const QDropEvent "
        "&from)': takes a type Python has no way to hand over yet.")
