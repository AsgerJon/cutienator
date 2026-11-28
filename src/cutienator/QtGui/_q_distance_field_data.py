"""
QDistanceFieldData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdistancefield_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDistanceFieldData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QSize = WAIT['QSize']


class QDistanceFieldData(QSharedData):
  """
  The cute side of Qt's QDistanceFieldData: a plain Python object standing in
  front of one C++ QDistanceFieldData.

  It is built on the cute 'QSharedData', as Qt's QDistanceFieldData is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QDistanceFieldData around as a copy, so every C++
  QDistanceFieldData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDistanceFieldData that has a ritual and that Python
  can call so far, 1 name in all: 'create'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDistanceFieldData::~QDistanceFieldData()': the destructor: Python
    removes its C++ QDistanceFieldData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDistanceFieldData is created at the first use, not by
    'QDistanceFieldData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDistanceFieldData back gives a copy the ritual made
    for Python, in a new cute QDistanceFieldData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSize)
  def create(size: QSize) -> Optional[QDistanceFieldData]:
    """
    Calls Qt's 'QDistanceFieldData *QDistanceFieldData::create(const QSize
    &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefielddata.html#create

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    Optional[QDistanceFieldData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDistanceFieldData *QDistanceFieldData::create(const QSize &size)
    address = Rituals.call(
        'ritual_ZN18QDistanceFieldData6createERK5QSize',
        CuteMixin._valueOf(size),
    )
    return QDistanceFieldData._cuteAt(address)

  @staticmethod
  @overload(QPainterPath, bool)
  def create(
      path: QPainterPath,
      doubleResolution: bool,
  ) -> Optional[QDistanceFieldData]:
    """
    Calls Qt's 'QDistanceFieldData *QDistanceFieldData::create(const
    QPainterPath &path, bool doubleResolution)'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefielddata.html#create

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    doubleResolution : bool
      Passed on as it is.

    Returns
    -------

    Optional[QDistanceFieldData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDistanceFieldData *QDistanceFieldData::create(const QPainterPath
    #      &path, bool doubleResolution)
    address = Rituals.call(
        'ritual_ZN18QDistanceFieldData6createERK12QPainterPathb',
        CuteMixin._valueOf(path), doubleResolution,
    )
    return QDistanceFieldData._cuteAt(address)

  @staticmethod
  @overload(QSize, QPainterPath, bool)
  def create(
      size: QSize,
      path: QPainterPath,
      doubleResolution: bool,
  ) -> Optional[QDistanceFieldData]:
    """
    Calls Qt's 'QDistanceFieldData *QDistanceFieldData::create(QSize size,
    const QPainterPath &path, bool doubleResolution)'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefielddata.html#create

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    doubleResolution : bool
      Passed on as it is.

    Returns
    -------

    Optional[QDistanceFieldData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDistanceFieldData *QDistanceFieldData::create(QSize size, const
    #      QPainterPath &path, bool doubleResolution)
    address = Rituals.call(
        'ritual_ZN18QDistanceFieldData6createE5QSizeRK12QPainterPathb',
        CuteMixin._valueOf(size), CuteMixin._valueOf(path), doubleResolution,
    )
    return QDistanceFieldData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDistanceFieldData'

  #  Qt's '~QDistanceFieldData()'. Naming it makes this a value class: Python
  #  owns every C++ QDistanceFieldData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QDistanceFieldDataD1Ev'

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
    'QDistanceFieldData::QDistanceFieldData()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdistancefielddata.html#QDistanceFieldData
    """
    #  QDistanceFieldData::QDistanceFieldData()
    self._noteCreation(QDistanceFieldData, lambda: Rituals.call(
        'ritual_ZN18QDistanceFieldDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDistanceFieldData) -> None:
    """
    Notes what was given, for Qt's
    'QDistanceFieldData::QDistanceFieldData(const QDistanceFieldData
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdistancefielddata.html#QDistanceFieldData

    Parameters
    ----------

    other : QDistanceFieldData
      Passed on as a value: Qt reads the C++ QDistanceFieldData, which stays
      Python's own.
    """
    #  QDistanceFieldData::QDistanceFieldData(const QDistanceFieldData
    #      &other)
    self._noteCreation(QDistanceFieldData, lambda: Rituals.call(
        'ritual_ZN18QDistanceFieldDataC1ERKS_', self._valueOf(other),
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
