"""
QQuick3DParticleShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleShape to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuick3DParticleAbstractShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleShape(QQuick3DParticleAbstractShape):
  """
  The cute side of Qt's QQuick3DParticleShape: a plain Python object standing
  in front of one C++ QQuick3DParticleShape.

  It is built on the cute 'QQuick3DParticleAbstractShape', as Qt's
  QQuick3DParticleShape is built on Qt's QQuick3DParticleAbstractShape, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleShape that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'fill',
  'type', 'extents', 'getPosition', 'getSurfaceNormal', 'setFill', 'setType',
  'setExtents', 'fillChanged', 'typeChanged', 'extentsChanged',
  'randomPositionCube', 'randomPositionSphere', 'randomPositionCylinder'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleShape::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DParticleShape::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleShape is created at the first use, not by
    'QQuick3DParticleShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleShape.
  - Qt tells when it has removed the C++ QQuick3DParticleShape. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DParticleShape, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ShapeType(CuteNum):
    """
    The enum 'QQuick3DParticleShape::ShapeType' of Qt, with the 3 names Qt
    gives in it.
    """

    Cube = Kee[int](0)
    Sphere = Kee[int](1)
    Cylinder = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DParticleShape::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleshape.html#tr

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
    #  QString QQuick3DParticleShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DParticleShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleShape::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DParticleShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fill(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleShape::fill() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleshape.html#fill
    """
    #  bool QQuick3DParticleShape::fill() const
    return self.uglySide.call('ritual_ZNK21QQuick3DParticleShape4fillEv')

  def type(self) -> ShapeType:
    """
    Calls Qt's 'ShapeType QQuick3DParticleShape::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleshape.html#type

    Returns
    -------

    ShapeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShapeType(number)' gives.
    """
    #  ShapeType QQuick3DParticleShape::type() const
    return QQuick3DParticleShape.ShapeType(self.uglySide.call(
        'ritual_ZNK21QQuick3DParticleShape4typeEv',
    ))

  def extents(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleShape::extents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleshape.html#extents

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleShape::extents() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DParticleShape7extentsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def randomPositionCube(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleShape::randomPositionCube(int
    particleIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#randomPositionCube

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleShape::randomPositionCube(int particleIndex)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DParticleShape18randomPositionCubeEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def randomPositionSphere(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleShape::randomPositionSphere(int
    particleIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#randomPositionSphere

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleShape::randomPositionSphere(int
    #      particleIndex) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DParticleShape20randomPositionSphereEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def randomPositionCylinder(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleShape::randomPositionCylinder(int
    particleIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#randomPositionCylinder

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleShape::randomPositionCylinder(int
    #      particleIndex) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DParticleShape22randomPositionCylinderEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFill(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleShape::setFill(bool fill)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleshape.html#setFill

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleShape::setFill(bool fill)
    self.uglySide.call('ritual_ZN21QQuick3DParticleShape7setFillEb', fill)

  @overload(ShapeType)
  def setType(self, type: ShapeType) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleShape::setType(QQuick3DParticleShape::ShapeType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleshape.html#setType

    Parameters
    ----------

    type : ShapeType
      Passed on as its number.
    """
    #  void QQuick3DParticleShape::setType(QQuick3DParticleShape::ShapeType
    #      type)
    self.uglySide.call(
        'ritual_ZN21QQuick3DParticleShape7setTypeENS_9ShapeTypeE',
        type.value,
    )

  @overload(QVector3D)
  def setExtents(self, extends: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleShape::setExtents(QVector3D extends)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#setExtents

    Parameters
    ----------

    extends : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleShape::setExtents(QVector3D extends)
    self.uglySide.call(
        'ritual_ZN21QQuick3DParticleShape10setExtentsE9QVector3D',
        self._valueOf(extends),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleShape::QQuick3DParticleShape(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#QQuick3DParticleShape

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleShape::QQuick3DParticleShape(QObject *parent)
    self._noteCreation(QQuick3DParticleShape, lambda: Rituals.call(
        'ritual_ZN21QQuick3DParticleShapeC1EP7QObject',
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

  @overload(int)
  def getPosition(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleShape::getPosition(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#getPosition

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleShape::getPosition(int particleIndex)
    ritual = 'ritual_ZN21QQuick3DParticleShape11getPositionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuick3DParticleShape11getPositionEi'
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def getSurfaceNormal(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleShape::getSurfaceNormal(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#getSurfaceNormal

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleShape::getSurfaceNormal(int particleIndex)
    ritual = 'ritual_ZN21QQuick3DParticleShape16getSurfaceNormalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuick3DParticleShape16getSurfaceNormalEi'
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def fillChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleShape::fillChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#fillChanged
    """
    #  void QQuick3DParticleShape::fillChanged()
    self.uglySide.call('ritual_ZN21QQuick3DParticleShape11fillChangedEv')

  def typeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleShape::typeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#typeChanged
    """
    #  void QQuick3DParticleShape::typeChanged()
    self.uglySide.call('ritual_ZN21QQuick3DParticleShape11typeChangedEv')

  def extentsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleShape::extentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleshape.html#extentsChanged
    """
    #  void QQuick3DParticleShape::extentsChanged()
    self.uglySide.call('ritual_ZN21QQuick3DParticleShape14extentsChangedEv')
