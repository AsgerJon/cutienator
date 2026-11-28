"""
QQuick3DParticleAttractor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleattractor_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleAttractor to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode
from . import QQuick3DParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from . import QQuick3DParticleAbstractShape, QQuick3DParticleData
  from . import QQuick3DParticleDataCurrent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticleAbstractShape = WAIT['QQuick3DParticleAbstractShape']
  QQuick3DParticleData = WAIT['QQuick3DParticleData']
  QQuick3DParticleDataCurrent = WAIT['QQuick3DParticleDataCurrent']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleAttractor(QQuick3DParticleAffector):
  """
  The cute side of Qt's QQuick3DParticleAttractor: a plain Python object
  standing in front of one C++ QQuick3DParticleAttractor.

  It is built on the cute 'QQuick3DParticleAffector', as Qt's
  QQuick3DParticleAttractor is built on Qt's QQuick3DParticleAffector, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleAttractor that has a ritual and that
  Python can call so far, 26 names in all: 'metaObject', 'tr',
  'positionVariation', 'shape', 'duration', 'durationVariation', 'hideAtEnd',
  'useCachedPositions', 'positionsAmount', 'setPositionVariation',
  'setShape', 'setDuration', 'setDurationVariation', 'setHideAtEnd',
  'setUseCachedPositions', 'setPositionsAmount', 'positionVariationChanged',
  'shapeChanged', 'durationChanged', 'durationVariationChanged',
  'hideAtEndChanged', 'useCachedPositionsChanged', 'positionsAmountChanged',
  'prepareToAffect', 'affectParticle', 'updateShapePositions'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleAttractor::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleAttractor::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleAttractor is created at the first use, not by
    'QQuick3DParticleAttractor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleAttractor.
  - Qt tells when it has removed the C++ QQuick3DParticleAttractor. Every
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
    Calls Qt's 'QString QQuick3DParticleAttractor::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleattractor.html#tr

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
    #  QString QQuick3DParticleAttractor::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuick3DParticleAttractor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleAttractor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleAttractor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleAttractor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def positionVariation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleAttractor::positionVariation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#positionVariation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleAttractor::positionVariation() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor17positionVariationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def shape(self) -> Optional[QQuick3DParticleAbstractShape]:
    """
    Calls Qt's 'QQuick3DParticleAbstractShape
    *QQuick3DParticleAttractor::shape() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#shape

    Returns
    -------

    Optional[QQuick3DParticleAbstractShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleAbstractShape *QQuick3DParticleAttractor::shape()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor5shapeEv',
    )
    from . import QQuick3DParticleAbstractShape
    return QQuick3DParticleAbstractShape._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleAttractor::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#duration
    """
    #  int QQuick3DParticleAttractor::duration() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor8durationEv',
    )

  def durationVariation(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleAttractor::durationVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#durationVariation
    """
    #  int QQuick3DParticleAttractor::durationVariation() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor17durationVariationEv',
    )

  def hideAtEnd(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleAttractor::hideAtEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#hideAtEnd
    """
    #  bool QQuick3DParticleAttractor::hideAtEnd() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor9hideAtEndEv',
    )

  def useCachedPositions(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleAttractor::useCachedPositions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#useCachedPositions
    """
    #  bool QQuick3DParticleAttractor::useCachedPositions() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor18useCachedPositionsEv',
    )

  def positionsAmount(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleAttractor::positionsAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#positionsAmount
    """
    #  int QQuick3DParticleAttractor::positionsAmount() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleAttractor15positionsAmountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPositionVariation(self, positionVariation: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::setPositionVariation(const
    QVector3D &positionVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html

    Parameters
    ----------

    positionVariation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleAttractor::setPositionVariation(const QVector3D
    #      &positionVariation)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor20setPositionVariationERK9QVec'
        'tor3D',
        self._valueOf(positionVariation),
    )

  @overload(QQuick3DParticleAbstractShape)
  @overload(NoneType)
  def setShape(self, shape: Optional[QQuick3DParticleAbstractShape]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleAttractor::setShape(QQuick3DParticleAbstractShape
    *shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#setShape

    Parameters
    ----------

    shape : Optional[QQuick3DParticleAbstractShape]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleAttractor::setShape(QQuick3DParticleAbstractShape
    #      *shape)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor8setShapeEP29QQuick3DParticleA'
        'bstractShape',
        self._addressOf(shape),
    )

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::setDuration(int duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleAttractor::setDuration(int duration)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor11setDurationEi', duration,
    )

  @overload(int)
  def setDurationVariation(self, durationVariation: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::setDurationVariation(int
    durationVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html

    Parameters
    ----------

    durationVariation : int
      Passed on as it is.
    """
    #  void QQuick3DParticleAttractor::setDurationVariation(int
    #      durationVariation)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor20setDurationVariationEi',
        durationVariation,
    )

  @overload(bool)
  def setHideAtEnd(self, hideAtEnd: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::setHideAtEnd(bool
    hideAtEnd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#setHideAtEnd

    Parameters
    ----------

    hideAtEnd : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleAttractor::setHideAtEnd(bool hideAtEnd)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor12setHideAtEndEb', hideAtEnd,
    )

  @overload(bool)
  def setUseCachedPositions(self, useCachedPositions: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::setUseCachedPositions(bool
    useCachedPositions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html

    Parameters
    ----------

    useCachedPositions : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleAttractor::setUseCachedPositions(bool
    #      useCachedPositions)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor21setUseCachedPositionsEb',
        useCachedPositions,
    )

  @overload(int)
  def setPositionsAmount(self, positionsAmount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::setPositionsAmount(int
    positionsAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#setPositionsAmount

    Parameters
    ----------

    positionsAmount : int
      Passed on as it is.
    """
    #  void QQuick3DParticleAttractor::setPositionsAmount(int
    #      positionsAmount)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor18setPositionsAmountEi',
        positionsAmount,
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
    'QQuick3DParticleAttractor::QQuick3DParticleAttractor(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleAttractor::QQuick3DParticleAttractor(QQuick3DNode
    #      *parent)
    self._noteCreation(QQuick3DParticleAttractor, lambda: Rituals.call(
        'ritual_ZN25QQuick3DParticleAttractorC1EP12QQuick3DNode',
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

  def positionVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::positionVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html
    """
    #  void QQuick3DParticleAttractor::positionVariationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor24positionVariationChangedEv',
    )

  def shapeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::shapeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#shapeChanged
    """
    #  void QQuick3DParticleAttractor::shapeChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor12shapeChangedEv',
    )

  def durationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::durationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#durationChanged
    """
    #  void QQuick3DParticleAttractor::durationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor15durationChangedEv',
    )

  def durationVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::durationVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html
    """
    #  void QQuick3DParticleAttractor::durationVariationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor24durationVariationChangedEv',
    )

  def hideAtEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::hideAtEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#hideAtEndChanged
    """
    #  void QQuick3DParticleAttractor::hideAtEndChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor16hideAtEndChangedEv',
    )

  def useCachedPositionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::useCachedPositionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html
    """
    #  void QQuick3DParticleAttractor::useCachedPositionsChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor25useCachedPositionsChangedEv',
    )

  def positionsAmountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::positionsAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html
    """
    #  void QQuick3DParticleAttractor::positionsAmountChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor22positionsAmountChangedEv',
    )

  def prepareToAffect(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::prepareToAffect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#prepareToAffect
    """
    #  void QQuick3DParticleAttractor::prepareToAffect()
    ritual = 'ritual_ZN25QQuick3DParticleAttractor15prepareToAffectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuick3DParticleAttractor15prepareToAffectEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DParticleData, QQuick3DParticleDataCurrent, float)
  @overload(QQuick3DParticleData, NoneType, float)
  def affectParticle(
      self,
      sd: QQuick3DParticleData,
      d: Optional[QQuick3DParticleDataCurrent],
      time: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::affectParticle(const
    QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html#affectParticle

    Parameters
    ----------

    sd : QQuick3DParticleData
      Passed on as a value: Qt reads the C++ QQuick3DParticleData, which
      stays Python's own.

    d : Optional[QQuick3DParticleDataCurrent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : float
      Passed on as it is.
    """
    #  void QQuick3DParticleAttractor::affectParticle(const
    #      QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float
    #      time)
    ritual = (
        'ritual_ZN25QQuick3DParticleAttractor14affectParticleERK20QQuick3DP'
        'articleDataP27QQuick3DParticleDataCurrentf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuick3DParticleAttractor14affectParticleERK20QQu'
          'ick3DParticleDataP27QQuick3DParticleDataCurrentf')
    self.uglySide.call(ritual, self._valueOf(sd), self._addressOf(d), time)

  def updateShapePositions(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAttractor::updateShapePositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleattractor.html
    """
    #  void QQuick3DParticleAttractor::updateShapePositions()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleAttractor20updateShapePositionsEv',
    )
