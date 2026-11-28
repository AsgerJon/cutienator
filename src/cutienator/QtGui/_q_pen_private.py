"""
QPenPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpen_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPenPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']


class QPenPrivate(QSharedData):
  """
  The cute side of Qt's QPenPrivate: a plain Python object standing in front
  of one C++ QPenPrivate.

  It is built on the cute 'QSharedData', as Qt's QPenPrivate is built on Qt's
  QSharedData, and has everything that class has.

  C++ hands a QPenPrivate around as a copy, so every C++ QPenPrivate behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QPenPrivate yet. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPenPrivate::~QPenPrivate()': the destructor: Python removes its
    C++ QPenPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPenPrivate is created at the first use, not by
    'QPenPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPenPrivate back gives a copy the ritual made for
    Python, in a new cute QPenPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPenPrivate'

  #  Qt's '~QPenPrivate()'. Naming it makes this a value class: Python owns
  #  every C++ QPenPrivate behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QPenPrivateD1Ev'

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

  @overload(QBrush, float, Qt.PenStyle, Qt.PenCapStyle, Qt.PenJoinStyle)
  def __init__(
      self,
      brush: QBrush,
      width: float,
      a2: Qt.PenStyle,
      a3: Qt.PenCapStyle,
      _joinStyle: Qt.PenJoinStyle,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPenPrivate::QPenPrivate(const QBrush
    &brush, qreal width, Qt::PenStyle a2, Qt::PenCapStyle a3,
    Qt::PenJoinStyle _joinStyle)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpenprivate.html#QPenPrivate

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    width : float
      Passed on as it is.

    a2 : Qt.PenStyle
      Passed on as its number.

    a3 : Qt.PenCapStyle
      Passed on as its number.

    _joinStyle : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  QPenPrivate::QPenPrivate(const QBrush &brush, qreal width,
    #      Qt::PenStyle a2, Qt::PenCapStyle a3, Qt::PenJoinStyle _joinStyle)
    self._noteCreation(QPenPrivate, lambda: Rituals.call(
        'ritual_ZN11QPenPrivateC1ERK6QBrushdN2Qt8PenStyleENS3_11PenCapStyle'
        'ENS3_12PenJoinStyleE',
        self._valueOf(brush), width, a2.value, a3.value, _joinStyle.value,
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
