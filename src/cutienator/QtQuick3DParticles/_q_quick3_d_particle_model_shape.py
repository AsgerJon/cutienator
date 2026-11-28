"""
QQuick3DParticleModelShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleModelShape to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuick3DParticleAbstractShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from ..QtQml import QQmlComponent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleModelShape(QQuick3DParticleAbstractShape):
  """
  The cute side of Qt's QQuick3DParticleModelShape: a plain Python object
  standing in front of one C++ QQuick3DParticleModelShape.

  It is built on the cute 'QQuick3DParticleAbstractShape', as Qt's
  QQuick3DParticleModelShape is built on Qt's QQuick3DParticleAbstractShape,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleModelShape that has a ritual and
  that Python can call so far, 14 names in all: 'metaObject', 'tr', 'fill',
  'delegate', 'setFill', 'setDelegate', 'getPosition', 'getSurfaceNormal',
  'fillChanged', 'delegateChanged', 'randomPositionModel', 'createModel',
  'clearModelVertexPositions', 'calculateModelVertexPositions'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleModelShape::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleModelShape::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleModelShape::~QQuick3DParticleModelShape()': the
    destructor: Python never removes a C++ QQuick3DParticleModelShape.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleModelShape is created at the first use, not by
    'QQuick3DParticleModelShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleModelShape.
  - Qt tells when it has removed the C++ QQuick3DParticleModelShape. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DParticleModelShape::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#tr

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
    #  QString QQuick3DParticleModelShape::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuick3DParticleModelShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleModelShape'

  #  A C++ QQuick3DParticleModelShape Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleModelShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleModelShape::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleModelShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleModelShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fill(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleModelShape::fill() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#fill
    """
    #  bool QQuick3DParticleModelShape::fill() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleModelShape4fillEv',
    )

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuick3DParticleModelShape::delegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuick3DParticleModelShape::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleModelShape8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFill(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelShape::setFill(bool fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#setFill

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleModelShape::setFill(bool fill)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape7setFillEb', fill,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelShape::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleModelShape::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape11setDelegateEP13QQmlComponen'
        't',
        self._addressOf(delegate),
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
    'QQuick3DParticleModelShape::QQuick3DParticleModelShape(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleModelShape::QQuick3DParticleModelShape(QObject
    #      *parent)
    self._noteCreation(QQuick3DParticleModelShape, lambda: Rituals.call(
        'ritual_ZN26QQuick3DParticleModelShapeC1EP7QObject',
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
    Calls Qt's 'QVector3D QQuick3DParticleModelShape::getPosition(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#getPosition

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleModelShape::getPosition(int particleIndex)
    ritual = 'ritual_ZN26QQuick3DParticleModelShape11getPositionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuick3DParticleModelShape11getPositionEi'
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def getSurfaceNormal(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleModelShape::getSurfaceNormal(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#getSurfaceNormal

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleModelShape::getSurfaceNormal(int
    #      particleIndex)
    ritual = 'ritual_ZN26QQuick3DParticleModelShape16getSurfaceNormalEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuick3DParticleModelShape16getSurfaceNormalEi')
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def fillChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelShape::fillChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#fillChanged
    """
    #  void QQuick3DParticleModelShape::fillChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape11fillChangedEv',
    )

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelShape::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#delegateChanged
    """
    #  void QQuick3DParticleModelShape::delegateChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape15delegateChangedEv',
    )

  @overload(int)
  def randomPositionModel(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleModelShape::randomPositionModel(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleModelShape::randomPositionModel(int
    #      particleIndex)
    address = self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape19randomPositionModelEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def createModel(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelShape::createModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html#createModel
    """
    #  void QQuick3DParticleModelShape::createModel()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape11createModelEv',
    )

  def clearModelVertexPositions(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelShape::clearModelVertexPositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html
    """
    #  void QQuick3DParticleModelShape::clearModelVertexPositions()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape25clearModelVertexPositionsEv',
    )

  def calculateModelVertexPositions(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelShape::calculateModelVertexPositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelshape.html
    """
    #  void QQuick3DParticleModelShape::calculateModelVertexPositions()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleModelShape29calculateModelVertexPositio'
        'nsEv',
    )
