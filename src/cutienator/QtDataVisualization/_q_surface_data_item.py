"""
QSurfaceDataItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qsurfacedataitem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class QSurfaceDataItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSurfaceDataItem: a plain Python object standing in
  front of one C++ QSurfaceDataItem.

  C++ hands a QSurfaceDataItem around as a copy, so every C++
  QSurfaceDataItem behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSurfaceDataItem that has a ritual and that Python
  can call so far, 9 names in all: 'setPosition', 'position', 'setX', 'setY',
  'setZ', 'x', 'y', 'z', 'createExtraData'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSurfaceDataItem::~QSurfaceDataItem()': the destructor: Python
    removes its C++ QSurfaceDataItem by it, and has no other use for it.
  - Qt's 'QSurfaceDataItem &QSurfaceDataItem::operator=(const
    QSurfaceDataItem &other)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QSurfaceDataItem is created at the first use, not by
    'QSurfaceDataItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSurfaceDataItem back gives a copy the ritual made
    for Python, in a new cute QSurfaceDataItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSurfaceDataItem'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  Qt's '~QSurfaceDataItem()'. Naming it makes this a value class: Python
  #  owns every C++ QSurfaceDataItem behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QSurfaceDataItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSurfaceDataItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSurfaceDataItem::position() const
    address = self.uglySide.call('ritual_ZNK16QSurfaceDataItem8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def x(self) -> float:
    """
    Calls Qt's 'float QSurfaceDataItem::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#x
    """
    #  float QSurfaceDataItem::x() const
    return self.uglySide.call('ritual_ZNK16QSurfaceDataItem1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QSurfaceDataItem::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#y
    """
    #  float QSurfaceDataItem::y() const
    return self.uglySide.call('ritual_ZNK16QSurfaceDataItem1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'float QSurfaceDataItem::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#z
    """
    #  float QSurfaceDataItem::z() const
    return self.uglySide.call('ritual_ZNK16QSurfaceDataItem1zEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, pos: QVector3D) -> None:
    """
    Calls Qt's 'void QSurfaceDataItem::setPosition(const QVector3D &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#setPosition

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSurfaceDataItem::setPosition(const QVector3D &pos)
    self.uglySide.call(
        'ritual_ZN16QSurfaceDataItem11setPositionERK9QVector3D',
        self._valueOf(pos),
    )

  @overload(float)
  def setX(self, value: float) -> None:
    """
    Calls Qt's 'void QSurfaceDataItem::setX(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#setX

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QSurfaceDataItem::setX(float value)
    self.uglySide.call('ritual_ZN16QSurfaceDataItem4setXEf', value)

  @overload(float)
  def setY(self, value: float) -> None:
    """
    Calls Qt's 'void QSurfaceDataItem::setY(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#setY

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QSurfaceDataItem::setY(float value)
    self.uglySide.call('ritual_ZN16QSurfaceDataItem4setYEf', value)

  @overload(float)
  def setZ(self, value: float) -> None:
    """
    Calls Qt's 'void QSurfaceDataItem::setZ(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataitem.html#setZ

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QSurfaceDataItem::setZ(float value)
    self.uglySide.call('ritual_ZN16QSurfaceDataItem4setZEf', value)

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
    Notes what was given, for Qt's 'QSurfaceDataItem::QSurfaceDataItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataitem.html#QSurfaceDataItem
    """
    #  QSurfaceDataItem::QSurfaceDataItem()
    self._noteCreation(QSurfaceDataItem, lambda: Rituals.call(
        'ritual_ZN16QSurfaceDataItemC1Ev',
    ))

  @overload(QVector3D)
  def __init__(self, position: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QSurfaceDataItem::QSurfaceDataItem(const
    QVector3D &position)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataitem.html#QSurfaceDataItem

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QSurfaceDataItem::QSurfaceDataItem(const QVector3D &position)
    self._noteCreation(QSurfaceDataItem, lambda: Rituals.call(
        'ritual_ZN16QSurfaceDataItemC1ERK9QVector3D',
        self._valueOf(position),
    ))

  @overload(THIS)
  def __init__(self, other: QSurfaceDataItem) -> None:
    """
    Notes what was given, for Qt's 'QSurfaceDataItem::QSurfaceDataItem(const
    QSurfaceDataItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataitem.html#QSurfaceDataItem

    Parameters
    ----------

    other : QSurfaceDataItem
      Passed on as a value: Qt reads the C++ QSurfaceDataItem, which stays
      Python's own.
    """
    #  QSurfaceDataItem::QSurfaceDataItem(const QSurfaceDataItem &other)
    self._noteCreation(QSurfaceDataItem, lambda: Rituals.call(
        'ritual_ZN16QSurfaceDataItemC1ERKS_', self._valueOf(other),
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

  def createExtraData(self) -> None:
    """
    Calls Qt's 'void QSurfaceDataItem::createExtraData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataitem.html#createExtraData
    """
    #  void QSurfaceDataItem::createExtraData()
    self.uglySide.call('ritual_ZN16QSurfaceDataItem15createExtraDataEv')
