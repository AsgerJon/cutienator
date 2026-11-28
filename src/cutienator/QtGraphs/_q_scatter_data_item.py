"""
QScatterDataItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qscatterdataitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']


class QScatterDataItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScatterDataItem: a plain Python object standing in
  front of one C++ QScatterDataItem.

  C++ hands a QScatterDataItem around as a copy, so every C++
  QScatterDataItem behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScatterDataItem that has a ritual and that Python
  can call so far, 10 names in all: 'setPosition', 'position', 'setRotation',
  'rotation', 'setX', 'setY', 'setZ', 'x', 'y', 'z'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScatterDataItem::~QScatterDataItem()': the destructor: Python
    removes its C++ QScatterDataItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScatterDataItem is created at the first use, not by
    'QScatterDataItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScatterDataItem back gives a copy the ritual made
    for Python, in a new cute QScatterDataItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatterDataItem'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  Qt's '~QScatterDataItem()'. Naming it makes this a value class: Python
  #  owns every C++ QScatterDataItem behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QScatterDataItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QScatterDataItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QScatterDataItem::position() const
    address = self.uglySide.call('ritual_ZNK16QScatterDataItem8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QScatterDataItem::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QScatterDataItem::rotation() const
    address = self.uglySide.call('ritual_ZNK16QScatterDataItem8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def x(self) -> float:
    """
    Calls Qt's 'float QScatterDataItem::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#x
    """
    #  float QScatterDataItem::x() const
    return self.uglySide.call('ritual_ZNK16QScatterDataItem1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QScatterDataItem::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#y
    """
    #  float QScatterDataItem::y() const
    return self.uglySide.call('ritual_ZNK16QScatterDataItem1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'float QScatterDataItem::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#z
    """
    #  float QScatterDataItem::z() const
    return self.uglySide.call('ritual_ZNK16QScatterDataItem1zEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, pos: QVector3D) -> None:
    """
    Calls Qt's 'void QScatterDataItem::setPosition(QVector3D pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#setPosition

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QScatterDataItem::setPosition(QVector3D pos)
    self.uglySide.call(
        'ritual_ZN16QScatterDataItem11setPositionE9QVector3D',
        self._valueOf(pos),
    )

  @overload(QQuaternion)
  def setRotation(self, rot: QQuaternion) -> None:
    """
    Calls Qt's 'void QScatterDataItem::setRotation(const QQuaternion &rot)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#setRotation

    Parameters
    ----------

    rot : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QScatterDataItem::setRotation(const QQuaternion &rot)
    self.uglySide.call(
        'ritual_ZN16QScatterDataItem11setRotationERK11QQuaternion',
        self._valueOf(rot),
    )

  @overload(float)
  def setX(self, value: float) -> None:
    """
    Calls Qt's 'void QScatterDataItem::setX(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#setX

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QScatterDataItem::setX(float value)
    self.uglySide.call('ritual_ZN16QScatterDataItem4setXEf', value)

  @overload(float)
  def setY(self, value: float) -> None:
    """
    Calls Qt's 'void QScatterDataItem::setY(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#setY

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QScatterDataItem::setY(float value)
    self.uglySide.call('ritual_ZN16QScatterDataItem4setYEf', value)

  @overload(float)
  def setZ(self, value: float) -> None:
    """
    Calls Qt's 'void QScatterDataItem::setZ(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataitem.html#setZ

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QScatterDataItem::setZ(float value)
    self.uglySide.call('ritual_ZN16QScatterDataItem4setZEf', value)

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
    Notes what was given, for Qt's 'QScatterDataItem::QScatterDataItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataitem.html#QScatterDataItem
    """
    #  QScatterDataItem::QScatterDataItem()
    self._noteCreation(QScatterDataItem, lambda: Rituals.call(
        'ritual_ZN16QScatterDataItemC1Ev',
    ))

  @overload(QVector3D)
  def __init__(self, position: QVector3D) -> None:
    """
    Notes what was given, for Qt's
    'QScatterDataItem::QScatterDataItem(QVector3D position)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataitem.html#QScatterDataItem

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QScatterDataItem::QScatterDataItem(QVector3D position)
    self._noteCreation(QScatterDataItem, lambda: Rituals.call(
        'ritual_ZN16QScatterDataItemC1E9QVector3D', self._valueOf(position),
    ))

  @overload(float, float, float)
  def __init__(self, x: float, y: float, z: float) -> None:
    """
    Notes what was given, for Qt's 'QScatterDataItem::QScatterDataItem(float
    x, float y, float z)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataitem.html#QScatterDataItem

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  QScatterDataItem::QScatterDataItem(float x, float y, float z)
    self._noteCreation(QScatterDataItem, lambda: Rituals.call(
        'ritual_ZN16QScatterDataItemC1Efff', x, y, z,
    ))

  @overload(QVector3D, QQuaternion)
  def __init__(self, position: QVector3D, rotation: QQuaternion) -> None:
    """
    Notes what was given, for Qt's
    'QScatterDataItem::QScatterDataItem(QVector3D position, const QQuaternion
    &rotation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataitem.html#QScatterDataItem

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  QScatterDataItem::QScatterDataItem(QVector3D position, const
    #      QQuaternion &rotation)
    self._noteCreation(QScatterDataItem, lambda: Rituals.call(
        'ritual_ZN16QScatterDataItemC1E9QVector3DRK11QQuaternion',
        self._valueOf(position), self._valueOf(rotation),
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


#  Qt's 'QList<QScatterDataItem>': the list of QScatterDataItem, which
#  'QList[QScatterDataItem]' gives. It is made here, so that there is one as
#  soon as there can be a QScatterDataItem. Qt has a name of its own for it.
QScatterDataArray = QList.createKind(
    QScatterDataItem, 'value',
    name='QScatterDataArray',
    make='ritual_list_make_QScatterDataItem',
    add='ritual_list_add_QScatterDataItem',
    size='ritual_list_size_QScatterDataItem',
    at='ritual_list_at_QScatterDataItem',
    drop='ritual_list_drop_QScatterDataItem',
)
