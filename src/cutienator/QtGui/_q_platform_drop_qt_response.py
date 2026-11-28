"""
QPlatformDropQtResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdrag.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt


class QPlatformDropQtResponse(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformDropQtResponse: a plain Python object
  standing in front of one C++ QPlatformDropQtResponse.

  C++ hands a QPlatformDropQtResponse around as a copy, so every C++
  QPlatformDropQtResponse behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformDropQtResponse that has a ritual and that
  Python can call so far, 2 names in all: 'isAccepted', 'acceptedAction'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformDropQtResponse::~QPlatformDropQtResponse()': the
    destructor: Python removes its C++ QPlatformDropQtResponse by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QPlatformDropQtResponse is created at the first use, not by
    'QPlatformDropQtResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformDropQtResponse back gives a copy the ritual
    made for Python, in a new cute QPlatformDropQtResponse.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformDropQtResponse'

  #  Qt's '~QPlatformDropQtResponse()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformDropQtResponse behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QPlatformDropQtResponseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QPlatformDropQtResponse::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdropqtresponse.html#isAccepted
    """
    #  bool QPlatformDropQtResponse::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformDropQtResponse10isAcceptedEv',
    )

  def acceptedAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QPlatformDropQtResponse::acceptedAction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdropqtresponse.html#acceptedAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QPlatformDropQtResponse::acceptedAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK23QPlatformDropQtResponse14acceptedActionEv',
    ))

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

  @overload(bool, Qt.DropAction)
  def __init__(self, accepted: bool, acceptedAction: Qt.DropAction) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformDropQtResponse::QPlatformDropQtResponse(bool accepted,
    Qt::DropAction acceptedAction)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdropqtresponse.html

    Parameters
    ----------

    accepted : bool
      Passed on as it is.

    acceptedAction : Qt.DropAction
      Passed on as its number.
    """
    #  QPlatformDropQtResponse::QPlatformDropQtResponse(bool accepted,
    #      Qt::DropAction acceptedAction)
    self._noteCreation(QPlatformDropQtResponse, lambda: Rituals.call(
        'ritual_ZN23QPlatformDropQtResponseC1EbN2Qt10DropActionE',
        accepted, acceptedAction.value,
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
