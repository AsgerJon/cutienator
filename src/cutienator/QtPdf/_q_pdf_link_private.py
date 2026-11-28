"""
QPdfLinkPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/6.12.0/QtPdf/private/qpdflink_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPdfLinkPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']


class QPdfLinkPrivate(QSharedData):
  """
  The cute side of Qt's QPdfLinkPrivate: a plain Python object standing in
  front of one C++ QPdfLinkPrivate.

  It is built on the cute 'QSharedData', as Qt's QPdfLinkPrivate is built on
  Qt's QSharedData, and has everything that class has.

  C++ hands a QPdfLinkPrivate around as a copy, so every C++ QPdfLinkPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QPdfLinkPrivate yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdfLinkPrivate::~QPdfLinkPrivate()': the destructor: Python
    removes its C++ QPdfLinkPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPdfLinkPrivate is created at the first use, not by
    'QPdfLinkPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdfLinkPrivate back gives a copy the ritual made for
    Python, in a new cute QPdfLinkPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfLinkPrivate'

  #  Qt's '~QPdfLinkPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QPdfLinkPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QPdfLinkPrivateD1Ev'

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
    Notes what was given, for Qt's 'QPdfLinkPrivate::QPdfLinkPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdflinkprivate.html#QPdfLinkPrivate
    """
    #  QPdfLinkPrivate::QPdfLinkPrivate()
    self._noteCreation(QPdfLinkPrivate, lambda: Rituals.call(
        'ritual_ZN15QPdfLinkPrivateC1Ev',
    ))

  @overload(int, QPointF, float)
  def __init__(self, page: int, location: QPointF, zoom: float) -> None:
    """
    Notes what was given, for Qt's 'QPdfLinkPrivate::QPdfLinkPrivate(int
    page, QPointF location, qreal zoom)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdflinkprivate.html#QPdfLinkPrivate

    Parameters
    ----------

    page : int
      Passed on as it is.

    location : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    zoom : float
      Passed on as it is.
    """
    #  QPdfLinkPrivate::QPdfLinkPrivate(int page, QPointF location, qreal
    #      zoom)
    self._noteCreation(QPdfLinkPrivate, lambda: Rituals.call(
        'ritual_ZN15QPdfLinkPrivateC1Ei7QPointFd',
        page, self._valueOf(location, 'QPointF'), zoom,
    ))

  @overload(int, QList[QRectF], str, str)
  def __init__(
      self,
      page: int,
      rects: QList[QRectF],
      contextBefore: str,
      contextAfter: str,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPdfLinkPrivate::QPdfLinkPrivate(int
    page, QList<QRectF> rects, QString contextBefore, QString contextAfter)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdflinkprivate.html#QPdfLinkPrivate

    Parameters
    ----------

    page : int
      Passed on as it is.

    rects : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    contextBefore : str
      Passed on as it is: a QString is made of it for the call.

    contextAfter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QPdfLinkPrivate::QPdfLinkPrivate(int page, QList<QRectF> rects,
    #      QString contextBefore, QString contextAfter)
    self._noteCreation(QPdfLinkPrivate, lambda: Rituals.call(
        'ritual_ZN15QPdfLinkPrivateC1Ei5QListI6QRectFE7QStringS3_',
        page, self._valueOf(rects), contextBefore, contextAfter,
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
