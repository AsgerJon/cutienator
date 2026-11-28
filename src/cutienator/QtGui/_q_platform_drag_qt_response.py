"""
QPlatformDragQtResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdrag.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPlatformDropQtResponse

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']


class QPlatformDragQtResponse(QPlatformDropQtResponse):
  """
  The cute side of Qt's QPlatformDragQtResponse: a plain Python object
  standing in front of one C++ QPlatformDragQtResponse.

  It is built on the cute 'QPlatformDropQtResponse', as Qt's
  QPlatformDragQtResponse is built on Qt's QPlatformDropQtResponse, and has
  everything that class has.

  C++ hands a QPlatformDragQtResponse around as a copy, so every C++
  QPlatformDragQtResponse behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformDragQtResponse that has a ritual and that
  Python can call so far, 1 name in all: 'answerRect'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformDragQtResponse::~QPlatformDragQtResponse()': the
    destructor: Python removes its C++ QPlatformDragQtResponse by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QPlatformDragQtResponse is created at the first use, not by
    'QPlatformDragQtResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformDragQtResponse back gives a copy the ritual
    made for Python, in a new cute QPlatformDragQtResponse.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformDragQtResponse'

  #  Qt's '~QPlatformDragQtResponse()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformDragQtResponse behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QPlatformDragQtResponseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def answerRect(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformDragQtResponse::answerRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdragqtresponse.html#answerRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformDragQtResponse::answerRect() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformDragQtResponse10answerRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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

  @overload(bool, Qt.DropAction, QRect)
  def __init__(
      self,
      accepted: bool,
      acceptedAction: Qt.DropAction,
      answerRect: QRect,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformDragQtResponse::QPlatformDragQtResponse(bool accepted,
    Qt::DropAction acceptedAction, QRect answerRect)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdragqtresponse.html

    Parameters
    ----------

    accepted : bool
      Passed on as it is.

    acceptedAction : Qt.DropAction
      Passed on as its number.

    answerRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QPlatformDragQtResponse::QPlatformDragQtResponse(bool accepted,
    #      Qt::DropAction acceptedAction, QRect answerRect)
    self._noteCreation(QPlatformDragQtResponse, lambda: Rituals.call(
        'ritual_ZN23QPlatformDragQtResponseC1EbN2Qt10DropActionE5QRect',
        accepted, acceptedAction.value, self._valueOf(answerRect),
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
