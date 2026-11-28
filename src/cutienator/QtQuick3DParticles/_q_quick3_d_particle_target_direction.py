"""
QQuick3DParticleTargetDirection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticletargetdirection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleTargetDirection to be private: it declares the
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


class QQuick3DParticleTargetDirection(QQuick3DParticleDirection):
  """
  The cute side of Qt's QQuick3DParticleTargetDirection: a plain Python
  object standing in front of one C++ QQuick3DParticleTargetDirection.

  It is built on the cute 'QQuick3DParticleDirection', as Qt's
  QQuick3DParticleTargetDirection is built on Qt's QQuick3DParticleDirection,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleTargetDirection that has a ritual
  and that Python can call so far, 18 names in all: 'metaObject', 'tr',
  'position', 'setPosition', 'normalized', 'magnitude', 'magnitudeVariation',
  'positionVariation', 'setPositionVariation', 'setNormalized',
  'setMagnitude', 'setMagnitudeVariation', 'positionChanged',
  'positionVariationChanged', 'normalizedChanged', 'magnitudeChanged',
  'magnitudeChangedVariation', 'sample'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleTargetDirection::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleTargetDirection::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleTargetDirection is created at the first use, not
    by 'QQuick3DParticleTargetDirection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleTargetDirection.
  - Qt tells when it has removed the C++ QQuick3DParticleTargetDirection.
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
    Calls Qt's 'QString QQuick3DParticleTargetDirection::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#tr

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
    #  QString QQuick3DParticleTargetDirection::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QQuick3DParticleTargetDirection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleTargetDirection'

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
    *QQuick3DParticleTargetDirection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleTargetDirection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleTargetDirection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleTargetDirection::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleTargetDirection::position() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleTargetDirection8positionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def normalized(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleTargetDirection::normalized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#normalized
    """
    #  bool QQuick3DParticleTargetDirection::normalized() const
    return self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleTargetDirection10normalizedEv',
    )

  def magnitude(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleTargetDirection::magnitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#magnitude
    """
    #  float QQuick3DParticleTargetDirection::magnitude() const
    return self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleTargetDirection9magnitudeEv',
    )

  def magnitudeVariation(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleTargetDirection::magnitudeVariation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html
    """
    #  float QQuick3DParticleTargetDirection::magnitudeVariation() const
    return self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleTargetDirection18magnitudeVariationEv',
    )

  def positionVariation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuick3DParticleTargetDirection::positionVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleTargetDirection::positionVariation() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuick3DParticleTargetDirection17positionVariationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTargetDirection::setPosition(const
    QVector3D &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleTargetDirection::setPosition(const QVector3D
    #      &position)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection11setPositionERK9QVector'
        '3D',
        self._valueOf(position),
    )

  @overload(QVector3D)
  def setPositionVariation(self, positionVariation: QVector3D) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleTargetDirection::setPositionVariation(const QVector3D
    &positionVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html

    Parameters
    ----------

    positionVariation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleTargetDirection::setPositionVariation(const
    #      QVector3D &positionVariation)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection20setPositionVariationER'
        'K9QVector3D',
        self._valueOf(positionVariation),
    )

  @overload(bool)
  def setNormalized(self, normalized: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTargetDirection::setNormalized(bool
    normalized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#setNormalized

    Parameters
    ----------

    normalized : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleTargetDirection::setNormalized(bool normalized)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection13setNormalizedEb',
        normalized,
    )

  @overload(float)
  def setMagnitude(self, magnitude: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTargetDirection::setMagnitude(float
    magnitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#setMagnitude

    Parameters
    ----------

    magnitude : float
      Passed on as it is.
    """
    #  void QQuick3DParticleTargetDirection::setMagnitude(float magnitude)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection12setMagnitudeEf',
        magnitude,
    )

  @overload(float)
  def setMagnitudeVariation(self, magnitudeVariation: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleTargetDirection::setMagnitudeVariation(float
    magnitudeVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html

    Parameters
    ----------

    magnitudeVariation : float
      Passed on as it is.
    """
    #  void QQuick3DParticleTargetDirection::setMagnitudeVariation(float
    #      magnitudeVariation)
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection21setMagnitudeVariationE'
        'f',
        magnitudeVariation,
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
    'QQuick3DParticleTargetDirection::QQuick3DParticleTargetDirection(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleTargetDirection::QQuick3DParticleTargetDirection(
    #      QObject *parent)
    self._noteCreation(QQuick3DParticleTargetDirection, lambda: Rituals.call(
        'ritual_ZN31QQuick3DParticleTargetDirectionC1EP7QObject',
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTargetDirection::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html
    """
    #  void QQuick3DParticleTargetDirection::positionChanged()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection15positionChangedEv',
    )

  def positionVariationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleTargetDirection::positionVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html
    """
    #  void QQuick3DParticleTargetDirection::positionVariationChanged()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection24positionVariationChang'
        'edEv',
    )

  def normalizedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTargetDirection::normalizedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html
    """
    #  void QQuick3DParticleTargetDirection::normalizedChanged()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection17normalizedChangedEv',
    )

  def magnitudeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleTargetDirection::magnitudeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html
    """
    #  void QQuick3DParticleTargetDirection::magnitudeChanged()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection16magnitudeChangedEv',
    )

  def magnitudeChangedVariation(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleTargetDirection::magnitudeChangedVariation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html
    """
    #  void QQuick3DParticleTargetDirection::magnitudeChangedVariation()
    self.uglySide.call(
        'ritual_ZN31QQuick3DParticleTargetDirection25magnitudeChangedVariat'
        'ionEv',
    )

  @overload(QQuick3DParticleData)
  def sample(self, d: QQuick3DParticleData) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleTargetDirection::sample(const
    QQuick3DParticleData &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticletargetdirection.html#sample

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
    #  QVector3D QQuick3DParticleTargetDirection::sample(const
    #      QQuick3DParticleData &d)
    ritual = (
        'ritual_ZN31QQuick3DParticleTargetDirection6sampleERK20QQuick3DPart'
        'icleData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQuick3DParticleTargetDirection6sampleERK20QQuick'
          '3DParticleData')
    address = self.uglySide.call(ritual, self._valueOf(d))
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)
