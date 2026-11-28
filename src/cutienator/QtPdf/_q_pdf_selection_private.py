"""
QPdfSelectionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/6.12.0/QtPdf/private/qpdfselection_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPdfSelectionPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
  from ..QtGui import QPolygonF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPolygonF = WAIT['QPolygonF']
  QRectF = WAIT['QRectF']


class QPdfSelectionPrivate(QSharedData):
  """
  The cute side of Qt's QPdfSelectionPrivate: a plain Python object standing
  in front of one C++ QPdfSelectionPrivate.

  It is built on the cute 'QSharedData', as Qt's QPdfSelectionPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QPdfSelectionPrivate around as a copy, so every C++
  QPdfSelectionPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QPdfSelectionPrivate yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdfSelectionPrivate::~QPdfSelectionPrivate()': the destructor:
    Python removes its C++ QPdfSelectionPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPdfSelectionPrivate is created at the first use, not by
    'QPdfSelectionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdfSelectionPrivate back gives a copy the ritual
    made for Python, in a new cute QPdfSelectionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfSelectionPrivate'

  #  Qt's '~QPdfSelectionPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPdfSelectionPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QPdfSelectionPrivateD1Ev'

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
    'QPdfSelectionPrivate::QPdfSelectionPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfselectionprivate.html#QPdfSelectionPrivate
    """
    #  QPdfSelectionPrivate::QPdfSelectionPrivate()
    self._noteCreation(QPdfSelectionPrivate, lambda: Rituals.call(
        'ritual_ZN20QPdfSelectionPrivateC1Ev',
    ))

  @overload(str, QList[QPolygonF], QRectF, int, int)
  def __init__(
      self,
      text: str,
      bounds: QList[QPolygonF],
      boundingRect: QRectF,
      startIndex: int,
      endIndex: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPdfSelectionPrivate::QPdfSelectionPrivate(const QString &text,
    QList<QPolygonF> bounds, QRectF boundingRect, int startIndex, int
    endIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfselectionprivate.html#QPdfSelectionPrivate

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    bounds : QList[QPolygonF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    boundingRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    startIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  QPdfSelectionPrivate::QPdfSelectionPrivate(const QString &text,
    #      QList<QPolygonF> bounds, QRectF boundingRect, int startIndex, int
    #      endIndex)
    self._noteCreation(QPdfSelectionPrivate, lambda: Rituals.call(
        'ritual_ZN20QPdfSelectionPrivateC1ERK7QString5QListI9QPolygonFE6QRe'
        'ctFii',
        text, self._valueOf(bounds), self._valueOf(boundingRect), startIndex,
        endIndex,
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
