"""
QCursorData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcursor_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QCursorData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QCursorData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCursorData: a plain Python object standing in front
  of one C++ QCursorData.

  C++ hands a QCursorData around as a copy, so every C++ QCursorData behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCursorData that has a ritual and that Python can
  call so far, 1 name in all: 'update'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCursorData::~QCursorData()': the destructor: Python removes its
    C++ QCursorData by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 6 functions Qt declares: 3 leans on 'QCursorData.

  What to expect
  --------------

  - The C++ QCursorData is created at the first use, not by
    'QCursorData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCursorData back gives a copy the ritual made for
    Python, in a new cute QCursorData.
  - Each name of Qt's QCursorData that has no cute function yet, 'cleanup',
    'initialize', 'setBitmap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCursorData'

  #  Qt's '~QCursorData()'. Naming it makes this a value class: Python owns
  #  every C++ QCursorData behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QCursorDataD1Ev'

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
  @overload(Qt.CursorShape)
  def __init__(self, s: Qt.CursorShape = Qt.CursorShape.ArrowCursor) -> None:
    """
    Notes what was given, for Qt's 'QCursorData::QCursorData(Qt::CursorShape
    s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcursordata.html#QCursorData

    Parameters
    ----------

    s : Qt.CursorShape
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CursorShape.ArrowCursor.
    """
    #  QCursorData::QCursorData(Qt::CursorShape s)
    self._noteCreation(QCursorData, lambda: Rituals.call(
        'ritual_ZN11QCursorDataC1EN2Qt11CursorShapeE', s.value,
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

  def update(self) -> None:
    """
    Calls Qt's 'void QCursorData::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qcursordata.html#update
    """
    #  void QCursorData::update()
    self.uglySide.call('ritual_ZN11QCursorData6updateEv')

  @staticmethod
  def cleanup(*__, **_) -> Never:
    """
    Qt's 'void QCursorData::cleanup()': leans on 'QCursorData::initialized',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCursorData.cleanup' has no cute function yet. Qt's 'void "
        "QCursorData::cleanup()': leans on 'QCursorData::initialized', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QCursorData::initialize()': leans on
    'QCursorData::initialized', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCursorData.initialize' has no cute function yet. Qt's 'void "
        "QCursorData::initialize()': leans on 'QCursorData::initialized', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setBitmap(*__, **_) -> Never:
    """
    Qt's 'QCursorData *QCursorData::setBitmap(const QBitmap &bitmap, const
    QBitmap &mask, int hotX, int hotY, qreal devicePixelRatio)': leans on
    'QCursorData::initialized', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCursorData.setBitmap' has no cute function yet. Qt's "
        "'QCursorData *QCursorData::setBitmap(const QBitmap &bitmap, const "
        "QBitmap &mask, int hotX, int hotY, qreal devicePixelRatio)': leans "
        "on 'QCursorData::initialized', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
