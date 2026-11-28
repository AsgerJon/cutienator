"""
QQuick3DXrSpatialAnchor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrSpatialAnchor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtCore import QList, QObject
from . import QtQuick3DXr

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUuid
  from ..QtGui import QQuaternion, QVector2D, QVector3D


class QQuick3DXrSpatialAnchor(QObject):
  """
  The cute side of Qt's QQuick3DXrSpatialAnchor: a plain Python object
  standing in front of one C++ QQuick3DXrSpatialAnchor.

  It is built on the cute 'QObject', as Qt's QQuick3DXrSpatialAnchor is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrSpatialAnchor that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'offset3D',
  'extent3D', 'position', 'rotation', 'classification',
  'classificationString', 'has2DBounds', 'has3DBounds', 'offset2D',
  'extent2D', 'identifier', 'space', 'offset3DChanged', 'extent3DChanged',
  'positionChanged', 'rotationChanged', 'classificationChanged',
  'classificationStringChanged', 'has2DBoundsChanged', 'has3DBoundsChanged',
  'offset2DChanged', 'extent2DChanged', 'uuid'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrSpatialAnchor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrSpatialAnchor::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DXrSpatialAnchor::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuick3DXrSpatialAnchor::~QQuick3DXrSpatialAnchor()': the
    destructor: Python never removes a C++ QQuick3DXrSpatialAnchor.
  - Qt's 'QSet<QUuid> QQuick3DXrSpatialAnchor::roomLayoutUuids() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QQuick3DXrSpatialAnchor::setRoomLayoutUuids(const QSet<QUuid>
    &newRoomLayoutUuids)': takes a type Python has no way to hand over yet.
  - Qt's 'QSet<QUuid> QQuick3DXrSpatialAnchor::spaceContainerUuids() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QQuick3DXrSpatialAnchor::setSpaceContainerUuids(const
    QSet<QUuid> &newSpaceContainerUuids)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  12 of the 44 functions Qt declares: 10 leans on 'QQuick3DXrSpatialAnchor; 2
  not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrSpatialAnchor is created at the first use, not by
    'QQuick3DXrSpatialAnchor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrSpatialAnchor.
  - Qt tells when it has removed the C++ QQuick3DXrSpatialAnchor. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrSpatialAnchor that has no cute function yet,
    '__init__', 'roomLayoutUuids', 'setBounds2D', 'setBounds3D',
    'setClassification', 'setClassificationString', 'setExtent3D',
    'setOffset3D', 'setPosition', 'setRoomLayoutUuids', 'setRotation',
    'setSpaceContainerUuids', 'spaceContainerUuids', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DXrSpatialAnchor, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Classification(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrSpatialAnchor::Classification' of Qt, with the 9
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    Wall = Kee[int](1)
    Ceiling = Kee[int](2)
    Floor = Kee[int](3)
    Table = Kee[int](4)
    Seat = Kee[int](5)
    Window = Kee[int](6)
    Door = Kee[int](7)
    Other = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrSpatialAnchor'

  #  A C++ QQuick3DXrSpatialAnchor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DXrSpatialAnchor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrSpatialAnchor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrSpatialAnchor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def offset3D(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DXrSpatialAnchor::offset3D() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#offset3D

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DXrSpatialAnchor::offset3D() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor8offset3DEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def extent3D(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DXrSpatialAnchor::extent3D() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#extent3D

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DXrSpatialAnchor::extent3D() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor8extent3DEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DXrSpatialAnchor::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DXrSpatialAnchor::position() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor8positionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DXrSpatialAnchor::rotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DXrSpatialAnchor::rotation() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor8rotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def classification(self) -> Classification:
    """
    Calls Qt's 'Classification QQuick3DXrSpatialAnchor::classification()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#classification

    Returns
    -------

    Classification
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Classification(number)'
      gives.
    """
    #  Classification QQuick3DXrSpatialAnchor::classification() const
    return QQuick3DXrSpatialAnchor.Classification(self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor14classificationEv',
    ))

  def classificationString(self) -> str:
    """
    Calls Qt's 'QString QQuick3DXrSpatialAnchor::classificationString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#classificationString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DXrSpatialAnchor::classificationString() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor20classificationStringEv',
    )

  def has2DBounds(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrSpatialAnchor::has2DBounds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#has2DBounds
    """
    #  bool QQuick3DXrSpatialAnchor::has2DBounds() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor11has2DBoundsEv',
    )

  def has3DBounds(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrSpatialAnchor::has3DBounds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#has3DBounds
    """
    #  bool QQuick3DXrSpatialAnchor::has3DBounds() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor11has3DBoundsEv',
    )

  def offset2D(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuick3DXrSpatialAnchor::offset2D() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#offset2D

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuick3DXrSpatialAnchor::offset2D() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor8offset2DEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def extent2D(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuick3DXrSpatialAnchor::extent2D() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#extent2D

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuick3DXrSpatialAnchor::extent2D() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor8extent2DEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def identifier(self) -> str:
    """
    Calls Qt's 'QString QQuick3DXrSpatialAnchor::identifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#identifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DXrSpatialAnchor::identifier() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor10identifierEv',
    )

  def space(self) -> QtQuick3DXr.XrSpaceId:
    """
    Calls Qt's 'QtQuick3DXr::XrSpaceId QQuick3DXrSpatialAnchor::space()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#space

    Returns
    -------

    QtQuick3DXr.XrSpaceId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtQuick3DXr.XrSpaceId(number)' gives.
    """
    #  QtQuick3DXr::XrSpaceId QQuick3DXrSpatialAnchor::space() const
    return QtQuick3DXr.XrSpaceId(self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor5spaceEv',
    ))

  def uuid(self) -> QUuid:
    """
    Calls Qt's 'QUuid QQuick3DXrSpatialAnchor::uuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#uuid

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QQuick3DXrSpatialAnchor::uuid() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrSpatialAnchor4uuidEv',
    )
    from ..QtCore import QUuid
    return QUuid._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QQuick3DXrSpatialAnchor::QQuick3DXrSpatialAnchor(QtQuick3DXr::XrSpaceId
    space, QUuid &uuid, QObject *parent)': leans on
    'QQuick3DXrSpatialAnchor::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrSpatialAnchor::QQuick3DXrSpatialAnchor(QtQuick3DXr::XrSp"
        "aceId space, QUuid &uuid, QObject *parent)': leans on "
        "'QQuick3DXrSpatialAnchor::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def offset3DChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::offset3DChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#offset3DChanged
    """
    #  void QQuick3DXrSpatialAnchor::offset3DChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor15offset3DChangedEv',
    )

  def extent3DChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::extent3DChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#extent3DChanged
    """
    #  void QQuick3DXrSpatialAnchor::extent3DChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor15extent3DChangedEv',
    )

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#positionChanged
    """
    #  void QQuick3DXrSpatialAnchor::positionChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor15positionChangedEv',
    )

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::rotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#rotationChanged
    """
    #  void QQuick3DXrSpatialAnchor::rotationChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor15rotationChangedEv',
    )

  def classificationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::classificationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#classificationChanged
    """
    #  void QQuick3DXrSpatialAnchor::classificationChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor21classificationChangedEv',
    )

  def classificationStringChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::classificationStringChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html
    """
    #  void QQuick3DXrSpatialAnchor::classificationStringChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor27classificationStringChangedEv',
    )

  def has2DBoundsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::has2DBoundsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#has2DBoundsChanged
    """
    #  void QQuick3DXrSpatialAnchor::has2DBoundsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor18has2DBoundsChangedEv',
    )

  def has3DBoundsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::has3DBoundsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#has3DBoundsChanged
    """
    #  void QQuick3DXrSpatialAnchor::has3DBoundsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor18has3DBoundsChangedEv',
    )

  def offset2DChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::offset2DChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#offset2DChanged
    """
    #  void QQuick3DXrSpatialAnchor::offset2DChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor15offset2DChangedEv',
    )

  def extent2DChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchor::extent2DChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchor.html#extent2DChanged
    """
    #  void QQuick3DXrSpatialAnchor::extent2DChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrSpatialAnchor15extent2DChangedEv',
    )

  @staticmethod
  def roomLayoutUuids(*__, **_) -> Never:
    """
    Qt's 'QSet<QUuid> QQuick3DXrSpatialAnchor::roomLayoutUuids() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.roomLayoutUuids' has no cute function "
        "yet. Qt's 'QSet<QUuid> QQuick3DXrSpatialAnchor::roomLayoutUuids() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setBounds2D(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setBounds2D(const QVector2D &offset,
    const QVector2D &extent)': leans on
    'QQuick3DXrSpatialAnchor::has2DBoundsChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setBounds2D' has no cute function yet. "
        "Qt's 'void QQuick3DXrSpatialAnchor::setBounds2D(const QVector2D "
        "&offset, const QVector2D &extent)': leans on "
        "'QQuick3DXrSpatialAnchor::has2DBoundsChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setBounds3D(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setBounds3D(const QVector3D &offset,
    const QVector3D &extent)': leans on
    'QQuick3DXrSpatialAnchor::has3DBoundsChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setBounds3D' has no cute function yet. "
        "Qt's 'void QQuick3DXrSpatialAnchor::setBounds3D(const QVector3D "
        "&offset, const QVector3D &extent)': leans on "
        "'QQuick3DXrSpatialAnchor::has3DBoundsChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setClassification(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setClassification(Classification
    newClassification)': leans on
    'QQuick3DXrSpatialAnchor::classificationChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setClassification' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DXrSpatialAnchor::setClassification(Classification "
        "newClassification)': leans on "
        "'QQuick3DXrSpatialAnchor::classificationChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setClassificationString(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setClassificationString(const QString
    &newClassificationString)': leans on
    'QQuick3DXrSpatialAnchor::classificationStringChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setClassificationString' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrSpatialAnchor::setClassificationString(const QString "
        "&newClassificationString)': leans on "
        "'QQuick3DXrSpatialAnchor::classificationStringChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setExtent3D(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setExtent3D(const QVector3D
    &newExtent)': leans on 'QQuick3DXrSpatialAnchor::extent3DChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setExtent3D' has no cute function yet. "
        "Qt's 'void QQuick3DXrSpatialAnchor::setExtent3D(const QVector3D "
        "&newExtent)': leans on "
        "'QQuick3DXrSpatialAnchor::extent3DChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setOffset3D(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setOffset3D(const QVector3D
    &newOffset)': leans on 'QQuick3DXrSpatialAnchor::offset3DChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setOffset3D' has no cute function yet. "
        "Qt's 'void QQuick3DXrSpatialAnchor::setOffset3D(const QVector3D "
        "&newOffset)': leans on "
        "'QQuick3DXrSpatialAnchor::offset3DChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setPosition(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setPosition(const QVector3D
    &newPosition)': leans on 'QQuick3DXrSpatialAnchor::positionChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setPosition' has no cute function yet. "
        "Qt's 'void QQuick3DXrSpatialAnchor::setPosition(const QVector3D "
        "&newPosition)': leans on "
        "'QQuick3DXrSpatialAnchor::positionChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setRoomLayoutUuids(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setRoomLayoutUuids(const QSet<QUuid>
    &newRoomLayoutUuids)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setRoomLayoutUuids' has no cute function "
        "yet. Qt's 'void QQuick3DXrSpatialAnchor::setRoomLayoutUuids(const "
        "QSet<QUuid> &newRoomLayoutUuids)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setRotation(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setRotation(const QQuaternion
    &newRotation)': leans on 'QQuick3DXrSpatialAnchor::rotationChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setRotation' has no cute function yet. "
        "Qt's 'void QQuick3DXrSpatialAnchor::setRotation(const QQuaternion "
        "&newRotation)': leans on "
        "'QQuick3DXrSpatialAnchor::rotationChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setSpaceContainerUuids(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchor::setSpaceContainerUuids(const
    QSet<QUuid> &newSpaceContainerUuids)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.setSpaceContainerUuids' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrSpatialAnchor::setSpaceContainerUuids(const QSet<QUuid> "
        "&newSpaceContainerUuids)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def spaceContainerUuids(*__, **_) -> Never:
    """
    Qt's 'QSet<QUuid> QQuick3DXrSpatialAnchor::spaceContainerUuids() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchor.spaceContainerUuids' has no cute function "
        "yet. Qt's 'QSet<QUuid> "
        "QQuick3DXrSpatialAnchor::spaceContainerUuids() const': gives a "
        "type Python has no way to take yet.")


#  Qt's 'QList<QQuick3DXrSpatialAnchor *>': the list of
#  QQuick3DXrSpatialAnchor, which 'QList[QQuick3DXrSpatialAnchor]' gives. It
#  is made here, so that there is one as soon as there can be a
#  QQuick3DXrSpatialAnchor.
QList.createKind(
    QQuick3DXrSpatialAnchor, 'address',
    make='ritual_list_make_QQuick3DXrSpatialAnchor_ptr',
    add='ritual_list_add_QQuick3DXrSpatialAnchor_ptr',
    size='ritual_list_size_QQuick3DXrSpatialAnchor_ptr',
    at='ritual_list_at_QQuick3DXrSpatialAnchor_ptr',
    drop='ritual_list_drop_QQuick3DXrSpatialAnchor_ptr',
)
