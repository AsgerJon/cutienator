"""
QCustom3DItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qcustom3ditem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage, QQuaternion, QVector3D
  from . import QCustom3DItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCustom3DItemPrivate = WAIT['QtDataVisualization:QCustom3DItemPrivate']
  QImage = WAIT['QImage']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCustom3DItem(QObject):
  """
  The cute side of Qt's QCustom3DItem: a plain Python object standing in
  front of one C++ QCustom3DItem.

  It is built on the cute 'QObject', as Qt's QCustom3DItem is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DItem that has a ritual and that Python can
  call so far, 31 names in all: 'metaObject', 'tr', 'setMeshFile',
  'meshFile', 'setTextureFile', 'textureFile', 'setPosition', 'position',
  'setPositionAbsolute', 'isPositionAbsolute', 'setScaling', 'scaling',
  'setScalingAbsolute', 'isScalingAbsolute', 'setRotation', 'rotation',
  'setVisible', 'isVisible', 'setShadowCasting', 'isShadowCasting',
  'setRotationAxisAndAngle', 'setTextureImage', 'meshFileChanged',
  'textureFileChanged', 'positionChanged', 'positionAbsoluteChanged',
  'scalingChanged', 'rotationChanged', 'visibleChanged',
  'shadowCastingChanged', 'scalingAbsoluteChanged'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustom3DItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCustom3DItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCustom3DItem::~QCustom3DItem()': the destructor: Python never
    removes a C++ QCustom3DItem.

  What has no ritual
  ------------------

  4 of the 41 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCustom3DItem is created at the first use, not by
    'QCustom3DItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustom3DItem.
  - Qt tells when it has removed the C++ QCustom3DItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QCustom3DItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCustom3DItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QCustom3DItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustom3DItem'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QCustom3DItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustom3DItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCustom3DItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustom3DItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QCustom3DItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def meshFile(self) -> str:
    """
    Calls Qt's 'QString QCustom3DItem::meshFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#meshFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCustom3DItem::meshFile() const
    return self.uglySide.call('ritual_ZNK13QCustom3DItem8meshFileEv')

  def textureFile(self) -> str:
    """
    Calls Qt's 'QString QCustom3DItem::textureFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#textureFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCustom3DItem::textureFile() const
    return self.uglySide.call('ritual_ZNK13QCustom3DItem11textureFileEv')

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QCustom3DItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QCustom3DItem::position() const
    address = self.uglySide.call('ritual_ZNK13QCustom3DItem8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isPositionAbsolute(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DItem::isPositionAbsolute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#isPositionAbsolute
    """
    #  bool QCustom3DItem::isPositionAbsolute() const
    return self.uglySide.call(
        'ritual_ZNK13QCustom3DItem18isPositionAbsoluteEv',
    )

  def scaling(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QCustom3DItem::scaling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#scaling

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QCustom3DItem::scaling() const
    address = self.uglySide.call('ritual_ZNK13QCustom3DItem7scalingEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isScalingAbsolute(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DItem::isScalingAbsolute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#isScalingAbsolute
    """
    #  bool QCustom3DItem::isScalingAbsolute() const
    return self.uglySide.call(
        'ritual_ZNK13QCustom3DItem17isScalingAbsoluteEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DItem::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#isVisible
    """
    #  bool QCustom3DItem::isVisible() const
    return self.uglySide.call('ritual_ZNK13QCustom3DItem9isVisibleEv')

  def isShadowCasting(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DItem::isShadowCasting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#isShadowCasting
    """
    #  bool QCustom3DItem::isShadowCasting() const
    return self.uglySide.call('ritual_ZNK13QCustom3DItem15isShadowCastingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setMeshFile(self, meshFile: str) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setMeshFile(const QString &meshFile)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#setMeshFile

    Parameters
    ----------

    meshFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCustom3DItem::setMeshFile(const QString &meshFile)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem11setMeshFileERK7QString', meshFile,
    )

  @overload(str)
  def setTextureFile(self, textureFile: str) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setTextureFile(const QString
    &textureFile)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#setTextureFile

    Parameters
    ----------

    textureFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCustom3DItem::setTextureFile(const QString &textureFile)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem14setTextureFileERK7QString', textureFile,
    )

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setPosition(const QVector3D &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DItem::setPosition(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem11setPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(bool)
  def setPositionAbsolute(self, positionAbsolute: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setPositionAbsolute(bool
    positionAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#setPositionAbsolute

    Parameters
    ----------

    positionAbsolute : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::setPositionAbsolute(bool positionAbsolute)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem19setPositionAbsoluteEb', positionAbsolute,
    )

  @overload(QVector3D)
  def setScaling(self, scaling: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setScaling(const QVector3D &scaling)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#setScaling

    Parameters
    ----------

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DItem::setScaling(const QVector3D &scaling)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem10setScalingERK9QVector3D',
        self._valueOf(scaling),
    )

  @overload(bool)
  def setScalingAbsolute(self, scalingAbsolute: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setScalingAbsolute(bool
    scalingAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#setScalingAbsolute

    Parameters
    ----------

    scalingAbsolute : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::setScalingAbsolute(bool scalingAbsolute)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem18setScalingAbsoluteEb', scalingAbsolute,
    )

  @overload(QQuaternion)
  def setRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setRotation(const QQuaternion
    &rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#setRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QCustom3DItem::setRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem11setRotationERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::setVisible(bool visible)
    self.uglySide.call('ritual_ZN13QCustom3DItem10setVisibleEb', visible)

  @overload(bool)
  def setShadowCasting(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setShadowCasting(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#setShadowCasting

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::setShadowCasting(bool enabled)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem16setShadowCastingEb', enabled,
    )

  @overload(QVector3D, float)
  def setRotationAxisAndAngle(self, axis: QVector3D, angle: float) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setRotationAxisAndAngle(const QVector3D
    &axis, float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#setRotationAxisAndAngle

    Parameters
    ----------

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle : float
      Passed on as it is.
    """
    #  void QCustom3DItem::setRotationAxisAndAngle(const QVector3D &axis,
    #      float angle)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem23setRotationAxisAndAngleERK9QVector3Df',
        self._valueOf(axis), angle,
    )

  @overload(QImage)
  def setTextureImage(self, textureImage: QImage) -> None:
    """
    Calls Qt's 'void QCustom3DItem::setTextureImage(const QImage
    &textureImage)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#setTextureImage

    Parameters
    ----------

    textureImage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QCustom3DItem::setTextureImage(const QImage &textureImage)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem15setTextureImageERK6QImage',
        self._valueOf(textureImage),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCustom3DItemPrivate)
  @overload(QCustom3DItemPrivate, QObject)
  @overload(QCustom3DItemPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QCustom3DItemPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCustom3DItem::QCustom3DItem(QCustom3DItemPrivate *d, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#QCustom3DItem

    Parameters
    ----------

    d : Optional[QCustom3DItemPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCustom3DItem::QCustom3DItem(QCustom3DItemPrivate *d, QObject *parent)
    self._noteCreation(QCustom3DItem, lambda: Rituals.call(
        'ritual_ZN13QCustom3DItemC1EP20QCustom3DItemPrivateP7QObject',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QCustom3DItem::QCustom3DItem(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#QCustom3DItem

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCustom3DItem::QCustom3DItem(QObject *parent)
    self._noteCreation(QCustom3DItem, lambda: Rituals.call(
        'ritual_ZN13QCustom3DItemC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QVector3D, QVector3D, QQuaternion, QImage)
  @overload(str, QVector3D, QVector3D, QQuaternion, QImage, QObject)
  @overload(str, QVector3D, QVector3D, QQuaternion, QImage, NoneType)
  def __init__(
      self,
      meshFile: str,
      position: QVector3D,
      scaling: QVector3D,
      rotation: QQuaternion,
      texture: QImage,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCustom3DItem::QCustom3DItem(const
    QString &meshFile, const QVector3D &position, const QVector3D &scaling,
    const QQuaternion &rotation, const QImage &texture, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#QCustom3DItem

    Parameters
    ----------

    meshFile : str
      Passed on as it is: a QString is made of it for the call.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    texture : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCustom3DItem::QCustom3DItem(const QString &meshFile, const QVector3D
    #      &position, const QVector3D &scaling, const QQuaternion &rotation,
    #      const QImage &texture, QObject *parent)
    self._noteCreation(QCustom3DItem, lambda: Rituals.call(
        'ritual_ZN13QCustom3DItemC1ERK7QStringRK9QVector3DS5_RK11QQuaternio'
        'nRK6QImageP7QObject',
        meshFile, self._valueOf(position), self._valueOf(scaling),
        self._valueOf(rotation), self._valueOf(texture),
        self._addressOf(parent, 'QObject'),
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

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QCustom3DItem::rotation()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QCustom3DItem::rotation()
    address = self.uglySide.call('ritual_ZN13QCustom3DItem8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @overload(str)
  def meshFileChanged(self, meshFile: str) -> None:
    """
    Calls Qt's 'void QCustom3DItem::meshFileChanged(const QString
    &meshFile)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#meshFileChanged

    Parameters
    ----------

    meshFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCustom3DItem::meshFileChanged(const QString &meshFile)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem15meshFileChangedERK7QString', meshFile,
    )

  @overload(str)
  def textureFileChanged(self, textureFile: str) -> None:
    """
    Calls Qt's 'void QCustom3DItem::textureFileChanged(const QString
    &textureFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#textureFileChanged

    Parameters
    ----------

    textureFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCustom3DItem::textureFileChanged(const QString &textureFile)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem18textureFileChangedERK7QString',
        textureFile,
    )

  @overload(QVector3D)
  def positionChanged(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DItem::positionChanged(const QVector3D
    &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#positionChanged

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DItem::positionChanged(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem15positionChangedERK9QVector3D',
        self._valueOf(position),
    )

  @overload(bool)
  def positionAbsoluteChanged(self, positionAbsolute: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::positionAbsoluteChanged(bool
    positionAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#positionAbsoluteChanged

    Parameters
    ----------

    positionAbsolute : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::positionAbsoluteChanged(bool positionAbsolute)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem23positionAbsoluteChangedEb',
        positionAbsolute,
    )

  @overload(QVector3D)
  def scalingChanged(self, scaling: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DItem::scalingChanged(const QVector3D
    &scaling)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#scalingChanged

    Parameters
    ----------

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DItem::scalingChanged(const QVector3D &scaling)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem14scalingChangedERK9QVector3D',
        self._valueOf(scaling),
    )

  @overload(QQuaternion)
  def rotationChanged(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QCustom3DItem::rotationChanged(const QQuaternion
    &rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#rotationChanged

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QCustom3DItem::rotationChanged(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem15rotationChangedERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(bool)
  def visibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::visibleChanged(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditem.html#visibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::visibleChanged(bool visible)
    self.uglySide.call('ritual_ZN13QCustom3DItem14visibleChangedEb', visible)

  @overload(bool)
  def shadowCastingChanged(self, shadowCasting: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::shadowCastingChanged(bool
    shadowCasting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#shadowCastingChanged

    Parameters
    ----------

    shadowCasting : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::shadowCastingChanged(bool shadowCasting)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem20shadowCastingChangedEb', shadowCasting,
    )

  @overload(bool)
  def scalingAbsoluteChanged(self, scalingAbsolute: bool) -> None:
    """
    Calls Qt's 'void QCustom3DItem::scalingAbsoluteChanged(bool
    scalingAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditem.html#scalingAbsoluteChanged

    Parameters
    ----------

    scalingAbsolute : bool
      Passed on as it is.
    """
    #  void QCustom3DItem::scalingAbsoluteChanged(bool scalingAbsolute)
    self.uglySide.call(
        'ritual_ZN13QCustom3DItem22scalingAbsoluteChangedEb',
        scalingAbsolute,
    )


#  Qt's 'QList<QCustom3DItem *>': the list of QCustom3DItem, which
#  'QList[QCustom3DItem]' gives. It is made here, so that there is one as
#  soon as there can be a QCustom3DItem.
QList.createKind(
    QCustom3DItem, 'address',
    make='ritual_list_make_QCustom3DItem_ptr',
    add='ritual_list_add_QCustom3DItem_ptr',
    size='ritual_list_size_QCustom3DItem_ptr',
    at='ritual_list_at_QCustom3DItem_ptr',
    drop='ritual_list_drop_QCustom3DItem_ptr',
)
