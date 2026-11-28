"""
QQuick3DParticleTrailEmitter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticletrailemitter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleTrailEmitter to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode
from . import QQuick3DParticleEmitter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from . import QQuick3DParticle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticle = WAIT['QQuick3DParticle']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleTrailEmitter(QQuick3DParticleEmitter):
  """
  The cute side of Qt's QQuick3DParticleTrailEmitter: a plain Python object
  standing in front of one C++ QQuick3DParticleTrailEmitter.

  It is built on the cute 'QQuick3DParticleEmitter', as Qt's
  QQuick3DParticleTrailEmitter is built on Qt's QQuick3DParticleEmitter, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleTrailEmitter that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'tr', 'follow',
  'burst', 'setFollow', 'followChanged', 'emitTrailParticles', 'hasBursts',
  'clearBursts'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleTrailEmitter::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleTrailEmitter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleTrailEmitter is created at the first use, not by
    'QQuick3DParticleTrailEmitter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleTrailEmitter.
  - Qt tells when it has removed the C++ QQuick3DParticleTrailEmitter. Every
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
    Calls Qt's 'QString QQuick3DParticleTrailEmitter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#tr

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
    #  QString QQuick3DParticleTrailEmitter::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuick3DParticleTrailEmitter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleTrailEmitter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleTrailEmitter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleTrailEmitter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleTrailEmitter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def follow(self) -> Optional[QQuick3DParticle]:
    """
    Calls Qt's 'QQuick3DParticle *QQuick3DParticleTrailEmitter::follow()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#follow

    Returns
    -------

    Optional[QQuick3DParticle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticle *QQuick3DParticleTrailEmitter::follow() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleTrailEmitter6followEv',
    )
    from . import QQuick3DParticle
    return QQuick3DParticle._cuteAt(address)

  def hasBursts(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleTrailEmitter::hasBursts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#hasBursts
    """
    #  bool QQuick3DParticleTrailEmitter::hasBursts() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleTrailEmitter9hasBurstsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DParticle)
  @overload(NoneType)
  def setFollow(self, follow: Optional[QQuick3DParticle]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTrailEmitter::setFollow(QQuick3DParticle
    *follow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#setFollow

    Parameters
    ----------

    follow : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleTrailEmitter::setFollow(QQuick3DParticle *follow)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleTrailEmitter9setFollowEP16QQuick3DParti'
        'cle',
        self._addressOf(follow),
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleTrailEmitter::QQuick3DParticleTrailEmitter(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleTrailEmitter::QQuick3DParticleTrailEmitter(
    #      QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleTrailEmitter, lambda: Rituals.call(
        'ritual_ZN28QQuick3DParticleTrailEmitterC1EP12QQuick3DNode',
        self._addressOf(parent),
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
  def burst(self, count: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTrailEmitter::burst(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#burst

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuick3DParticleTrailEmitter::burst(int count)
    ritual = 'ritual_ZN28QQuick3DParticleTrailEmitter5burstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QQuick3DParticleTrailEmitter5burstEi'
    self.uglySide.call(ritual, count)

  def followChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTrailEmitter::followChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#followChanged
    """
    #  void QQuick3DParticleTrailEmitter::followChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleTrailEmitter13followChangedEv',
    )

  @overload(QVector3D, int, int, QVector3D, QVector3D)
  def emitTrailParticles(
      self,
      centerPos: QVector3D,
      emitAmount: int,
      triggerType: int,
      normal: QVector3D,
      velocity: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTrailEmitter::emitTrailParticles(const
    QVector3D &centerPos, int emitAmount, int triggerType, const QVector3D
    &normal, const QVector3D &velocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html

    Parameters
    ----------

    centerPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    emitAmount : int
      Passed on as it is.

    triggerType : int
      Passed on as it is.

    normal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    velocity : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleTrailEmitter::emitTrailParticles(const QVector3D
    #      &centerPos, int emitAmount, int triggerType, const QVector3D
    #      &normal, const QVector3D &velocity)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleTrailEmitter18emitTrailParticlesERK9QVe'
        'ctor3DiiS2_S2_',
        self._valueOf(centerPos), emitAmount, triggerType,
        self._valueOf(normal), self._valueOf(velocity),
    )

  def clearBursts(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTrailEmitter::clearBursts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletrailemitter.html#clearBursts
    """
    #  void QQuick3DParticleTrailEmitter::clearBursts()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleTrailEmitter11clearBurstsEv',
    )
