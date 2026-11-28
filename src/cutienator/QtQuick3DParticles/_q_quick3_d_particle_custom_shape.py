"""
QQuick3DParticleCustomShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlecustomshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleCustomShape to be private: it declares the class
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

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleCustomShape(QQuick3DParticleAbstractShape):
  """
  The cute side of Qt's QQuick3DParticleCustomShape: a plain Python object
  standing in front of one C++ QQuick3DParticleCustomShape.

  It is built on the cute 'QQuick3DParticleAbstractShape', as Qt's
  QQuick3DParticleCustomShape is built on Qt's QQuick3DParticleAbstractShape,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleCustomShape that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr', 'source',
  'randomizeData', 'getPosition', 'getSurfaceNormal', 'setSource',
  'setRandomizeData', 'sourceChanged', 'randomizeDataChanged',
  'loadFromSource', 'doRandomizeData'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleCustomShape::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleCustomShape::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleCustomShape is created at the first use, not by
    'QQuick3DParticleCustomShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleCustomShape.
  - Qt tells when it has removed the C++ QQuick3DParticleCustomShape. Every
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
    Calls Qt's 'QString QQuick3DParticleCustomShape::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#tr

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
    #  QString QQuick3DParticleCustomShape::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQuick3DParticleCustomShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleCustomShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleCustomShape::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleCustomShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuick3DParticleCustomShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DParticleCustomShape::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DParticleCustomShape::source() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuick3DParticleCustomShape6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def randomizeData(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleCustomShape::randomizeData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#randomizeData
    """
    #  bool QQuick3DParticleCustomShape::randomizeData() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DParticleCustomShape13randomizeDataEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DParticleCustomShape::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DParticleCustomShape::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN27QQuick3DParticleCustomShape9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(bool)
  def setRandomizeData(self, random: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleCustomShape::setRandomizeData(bool
    random)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#setRandomizeData

    Parameters
    ----------

    random : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleCustomShape::setRandomizeData(bool random)
    self.uglySide.call(
        'ritual_ZN27QQuick3DParticleCustomShape16setRandomizeDataEb', random,
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
    'QQuick3DParticleCustomShape::QQuick3DParticleCustomShape(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleCustomShape::QQuick3DParticleCustomShape(QObject
    #      *parent)
    self._noteCreation(QQuick3DParticleCustomShape, lambda: Rituals.call(
        'ritual_ZN27QQuick3DParticleCustomShapeC1EP7QObject',
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
    Calls Qt's 'QVector3D QQuick3DParticleCustomShape::getPosition(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#getPosition

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleCustomShape::getPosition(int particleIndex)
    ritual = 'ritual_ZN27QQuick3DParticleCustomShape11getPositionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuick3DParticleCustomShape11getPositionEi'
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def getSurfaceNormal(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleCustomShape::getSurfaceNormal(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#getSurfaceNormal

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleCustomShape::getSurfaceNormal(int
    #      particleIndex)
    ritual = 'ritual_ZN27QQuick3DParticleCustomShape16getSurfaceNormalEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuick3DParticleCustomShape16getSurfaceNormalEi')
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleCustomShape::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#sourceChanged
    """
    #  void QQuick3DParticleCustomShape::sourceChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DParticleCustomShape13sourceChangedEv',
    )

  def randomizeDataChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleCustomShape::randomizeDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html
    """
    #  void QQuick3DParticleCustomShape::randomizeDataChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DParticleCustomShape20randomizeDataChangedEv',
    )

  def loadFromSource(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleCustomShape::loadFromSource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#loadFromSource
    """
    #  void QQuick3DParticleCustomShape::loadFromSource()
    self.uglySide.call(
        'ritual_ZN27QQuick3DParticleCustomShape14loadFromSourceEv',
    )

  def doRandomizeData(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleCustomShape::doRandomizeData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlecustomshape.html#doRandomizeData
    """
    #  void QQuick3DParticleCustomShape::doRandomizeData()
    self.uglySide.call(
        'ritual_ZN27QQuick3DParticleCustomShape15doRandomizeDataEv',
    )
