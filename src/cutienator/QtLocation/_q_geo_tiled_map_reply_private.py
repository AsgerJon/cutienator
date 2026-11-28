"""
QGeoTiledMapReplyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmapreply_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTiledMapReplyPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QGeoTiledMapReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QGeoTileSpec
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoTileSpec = WAIT['QGeoTileSpec']


class QGeoTiledMapReplyPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoTiledMapReplyPrivate: a plain Python object
  standing in front of one C++ QGeoTiledMapReplyPrivate.

  C++ hands a QGeoTiledMapReplyPrivate around as a copy, so every C++
  QGeoTiledMapReplyPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QGeoTiledMapReplyPrivate yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoTiledMapReplyPrivate::~QGeoTiledMapReplyPrivate()': the
    destructor: Python removes its C++ QGeoTiledMapReplyPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QGeoTiledMapReplyPrivate is created at the first use, not by
    'QGeoTiledMapReplyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoTiledMapReplyPrivate back gives a copy the ritual
    made for Python, in a new cute QGeoTiledMapReplyPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMapReplyPrivate'

  #  Qt's '~QGeoTiledMapReplyPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoTiledMapReplyPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QGeoTiledMapReplyPrivateD1Ev'

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

  @overload(QGeoTileSpec)
  def __init__(self, spec: QGeoTileSpec) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(const QGeoTileSpec
    &spec)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreplyprivate.html

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(const QGeoTileSpec
    #      &spec)
    self._noteCreation(QGeoTiledMapReplyPrivate, lambda: Rituals.call(
        'ritual_ZN24QGeoTiledMapReplyPrivateC1ERK12QGeoTileSpec',
        self._valueOf(spec),
    ))

  @overload(QGeoTiledMapReply.Error, str)
  def __init__(
      self,
      error: QGeoTiledMapReply.Error,
      errorString: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(QGeoTiledMapReply::
    Error error, const QString &errorString)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreplyprivate.html

    Parameters
    ----------

    error : QGeoTiledMapReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(
    #      QGeoTiledMapReply::Error error, const QString &errorString)
    self._noteCreation(QGeoTiledMapReplyPrivate, lambda: Rituals.call(
        'ritual_ZN24QGeoTiledMapReplyPrivateC1EN17QGeoTiledMapReply5ErrorER'
        'K7QString',
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
