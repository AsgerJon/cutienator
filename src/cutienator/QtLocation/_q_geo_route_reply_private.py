"""
QGeoRouteReplyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeoroutereply_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoRouteReplyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QGeoRouteReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QGeoRouteRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoRouteRequest = WAIT['QGeoRouteRequest']


class QGeoRouteReplyPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoRouteReplyPrivate: a plain Python object standing
  in front of one C++ QGeoRouteReplyPrivate.

  What exists
  -----------

  No function of Qt's QGeoRouteReplyPrivate yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoRouteReplyPrivate is created at the first use, not by
    'QGeoRouteReplyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRouteReplyPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteReplyPrivate'

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

  @overload(QGeoRouteRequest)
  def __init__(self, request: QGeoRouteRequest) -> None:
    """
    Notes what was given, for Qt's
    'QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(const QGeoRouteRequest
    &request)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutereplyprivate.html#QGeoRouteReplyPrivate

    Parameters
    ----------

    request : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.
    """
    #  QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(const QGeoRouteRequest
    #      &request)
    self._noteCreation(QGeoRouteReplyPrivate, lambda: Rituals.call(
        'ritual_ZN21QGeoRouteReplyPrivateC1ERK16QGeoRouteRequest',
        self._valueOf(request),
    ))

  @overload(QGeoRouteReply.Error, str)
  def __init__(self, error: QGeoRouteReply.Error, errorString: str) -> None:
    """
    Notes what was given, for Qt's
    'QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(QGeoRouteReply::Error
    error, QString errorString)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutereplyprivate.html#QGeoRouteReplyPrivate

    Parameters
    ----------

    error : QGeoRouteReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(QGeoRouteReply::Error
    #      error, QString errorString)
    self._noteCreation(QGeoRouteReplyPrivate, lambda: Rituals.call(
        'ritual_ZN21QGeoRouteReplyPrivateC1EN14QGeoRouteReply5ErrorE7QStrin'
        'g',
        error.value, errorString,
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
