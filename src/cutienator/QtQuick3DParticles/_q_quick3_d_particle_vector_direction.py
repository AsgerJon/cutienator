"""
QQuick3DParticleVectorDirection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlevectordirection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleVectorDirection to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuick3DParticleDirection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from . import QQuick3DParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticleData = WAIT['QQuick3DParticleData']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleVectorDirection(QQuick3DParticleDirection):
  """
  The cute side of Qt's QQuick3DParticleVectorDirection: a plain Python
  object standing in front of one C++ QQuick3DParticleVectorDirection.

  It is built on the cute 'QQuick3DParticleDirection', as Qt's
  QQuick3DParticleVectorDirection is built on Qt's QQuick3DParticleDirection,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleVectorDirection that has a ritual
  and that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'direction', 'directionVariation', 'normalized', 'setDirection',
  'setDirectionVariation', 'setNormalized', 'directionChanged',
  'directionVariationChanged', 'normalizedChanged', 'sample'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleVectorDirection::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleVectorDirection::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleVectorDirection is created at the first use, not
    by 'QQuick3DParticleVectorDirection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleVectorDirection.
  - Qt tells when it has removed the C++ QQuick3DParticleVectorDirection.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DParticleVectorDirection::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html#tr

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
    #  QString QQuick3DParticleVectorDirection::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QQuick3DParticleVectorDirection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleVectorDirection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuick3DParticleVectorDirection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleVectorDirection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleVectorDirection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def direction(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleVectorDirection::direction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html#direction

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleVectorDirection::direction() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleVectorDirection9directionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def directionVariation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuick3DParticleVectorDirection::directionVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleVectorDirection::directionVariation() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleVectorDirection18directionVariationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def normalized(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleVectorDirection::normalized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html#normalized
    """
    #  bool QQuick3DParticleVectorDirection::normalized() const
    return self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleVectorDirection10normalizedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setDirection(self, direction: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleVectorDirection::setDirection(const
    QVector3D &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html#setDirection

    Parameters
    ----------

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleVectorDirection::setDirection(const QVector3D
    #      &direction)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleVectorDirection12setDirectionERK9QVecto'
        'r3D',
        self._valueOf(direction),
    )

  @overload(QVector3D)
  def setDirectionVariation(self, directionVariation: QVector3D) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleVectorDirection::setDirectionVariation(const QVector3D
    &directionVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html

    Parameters
    ----------

    directionVariation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleVectorDirection::setDirectionVariation(const
    #      QVector3D &directionVariation)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleVectorDirection21setDirectionVariationE'
        'RK9QVector3D',
        self._valueOf(directionVariation),
    )

  @overload(bool)
  def setNormalized(self, normalized: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleVectorDirection::setNormalized(bool
    normalized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html#setNormalized

    Parameters
    ----------

    normalized : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleVectorDirection::setNormalized(bool normalized)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleVectorDirection13setNormalizedEb',
        normalized,
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
    'QQuick3DParticleVectorDirection::QQuick3DParticleVectorDirection(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleVectorDirection::QQuick3DParticleVectorDirection(
    #      QObject *parent)
    self._noteCreation(QQuick3DParticleVectorDirection, lambda: Rituals.call(
        'ritual_ZN31QQuick3DParticleVectorDirectionC1EP7QObject',
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

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleVectorDirection::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html
    """
    #  void QQuick3DParticleVectorDirection::directionChanged()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleVectorDirection16directionChangedEv',
    )

  def directionVariationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleVectorDirection::directionVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html
    """
    #  void QQuick3DParticleVectorDirection::directionVariationChanged()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleVectorDirection25directionVariationChan'
        'gedEv',
    )

  def normalizedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleVectorDirection::normalizedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html
    """
    #  void QQuick3DParticleVectorDirection::normalizedChanged()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleVectorDirection17normalizedChangedEv',
    )

  @overload(QQuick3DParticleData)
  def sample(self, d: QQuick3DParticleData) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleVectorDirection::sample(const
    QQuick3DParticleData &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlevectordirection.html#sample

    Parameters
    ----------

    d : QQuick3DParticleData
      Passed on as a value: Qt reads the C++ QQuick3DParticleData, which
      stays Python's own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleVectorDirection::sample(const
    #      QQuick3DParticleData &d)
    ritual = (
        'ritual_ZN31QQuick3DParticleVectorDirection6sampleERK20QQuick3DPart'
        'icleData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQuick3DParticleVectorDirection6sampleERK20QQuick'
          '3DParticleData')
    address = self.uglySide.call(ritual, self._valueOf(d))
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)
