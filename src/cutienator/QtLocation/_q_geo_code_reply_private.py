"""
QGeoCodeReplyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeocodereply_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoCodeReplyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QGeoCodeReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGeoCodeReplyPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoCodeReplyPrivate: a plain Python object standing
  in front of one C++ QGeoCodeReplyPrivate.

  What exists
  -----------

  No function of Qt's QGeoCodeReplyPrivate yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGeoCodeReplyPrivate *QGeoCodeReplyPrivate::get(const
    QGeoCodeReply &reply)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoCodeReplyPrivate *QGeoCodeReplyPrivate::get(QGeoCodeReply
    &reply)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoCodeReplyPrivate is created at the first use, not by
    'QGeoCodeReplyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoCodeReplyPrivate.
  - Each name of Qt's QGeoCodeReplyPrivate that has no cute function yet,
    'get', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCodeReplyPrivate'

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
    'QGeoCodeReplyPrivate::QGeoCodeReplyPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodereplyprivate.html#QGeoCodeReplyPrivate
    """
    #  QGeoCodeReplyPrivate::QGeoCodeReplyPrivate()
    self._noteCreation(QGeoCodeReplyPrivate, lambda: Rituals.call(
        'ritual_ZN20QGeoCodeReplyPrivateC1Ev',
    ))

  @overload(QGeoCodeReply.Error, str)
  def __init__(self, error: QGeoCodeReply.Error, errorString: str) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCodeReplyPrivate::QGeoCodeReplyPrivate(QGeoCodeReply::Error error,
    const QString &errorString)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodereplyprivate.html#QGeoCodeReplyPrivate

    Parameters
    ----------

    error : QGeoCodeReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QGeoCodeReplyPrivate::QGeoCodeReplyPrivate(QGeoCodeReply::Error error,
    #      const QString &errorString)
    self._noteCreation(QGeoCodeReplyPrivate, lambda: Rituals.call(
        'ritual_ZN20QGeoCodeReplyPrivateC1EN13QGeoCodeReply5ErrorERK7QStrin'
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

  @staticmethod
  def get(*__, **_) -> Never:
    """
    - Qt's 'const QGeoCodeReplyPrivate *QGeoCodeReplyPrivate::get(const
      QGeoCodeReply &reply)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QGeoCodeReplyPrivate *QGeoCodeReplyPrivate::get(QGeoCodeReply
      &reply)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoCodeReplyPrivate.get' has no cute function yet. Qt's 'const "
        "QGeoCodeReplyPrivate *QGeoCodeReplyPrivate::get(const "
        "QGeoCodeReply &reply)': takes a type Python has no way to hand "
        "over yet. Qt's 'QGeoCodeReplyPrivate "
        "*QGeoCodeReplyPrivate::get(QGeoCodeReply &reply)': takes a type "
        "Python has no way to hand over yet.")
