"""
QQuick3DParticleWander binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlewander_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleWander to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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
  from . import QQuick3DParticleData, QQuick3DParticleDataCurrent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticleData = WAIT['QQuick3DParticleData']
  QQuick3DParticleDataCurrent = WAIT['QQuick3DParticleDataCurrent']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleWander(QQuick3DParticleAffector):
  """
  The cute side of Qt's QQuick3DParticleWander: a plain Python object
  standing in front of one C++ QQuick3DParticleWander.

  It is built on the cute 'QQuick3DParticleAffector', as Qt's
  QQuick3DParticleWander is built on Qt's QQuick3DParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleWander that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'tr',
  'globalAmount', 'globalPace', 'globalPaceStart', 'uniqueAmount',
  'uniquePace', 'uniqueAmountVariation', 'uniquePaceVariation',
  'fadeInDuration', 'fadeOutDuration', 'setGlobalAmount', 'setGlobalPace',
  'setGlobalPaceStart', 'setUniqueAmount', 'setUniquePace',
  'setUniqueAmountVariation', 'setUniquePaceVariation', 'setFadeInDuration',
  'setFadeOutDuration', 'globalAmountChanged', 'globalPaceChanged',
  'globalPaceStartChanged', 'uniqueAmountChanged', 'uniquePaceChanged',
  'uniqueAmountVariationChanged', 'uniquePaceVariationChanged',
  'fadeInDurationChanged', 'fadeOutDurationChanged', 'affectParticle'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleWander::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DParticleWander::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleWander is created at the first use, not by
    'QQuick3DParticleWander(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleWander.
  - Qt tells when it has removed the C++ QQuick3DParticleWander. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DParticleWander::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlewander.html#tr

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
    #  QString QQuick3DParticleWander::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuick3DParticleWander2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleWander'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleWander::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleWander::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def globalAmount(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QQuick3DParticleWander::globalAmount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#globalAmount

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QQuick3DParticleWander::globalAmount() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander12globalAmountEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def globalPace(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QQuick3DParticleWander::globalPace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#globalPace

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QQuick3DParticleWander::globalPace() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander10globalPaceEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def globalPaceStart(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QQuick3DParticleWander::globalPaceStart()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#globalPaceStart

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QQuick3DParticleWander::globalPaceStart() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander15globalPaceStartEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def uniqueAmount(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QQuick3DParticleWander::uniqueAmount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#uniqueAmount

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QQuick3DParticleWander::uniqueAmount() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander12uniqueAmountEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def uniquePace(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QQuick3DParticleWander::uniquePace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#uniquePace

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QQuick3DParticleWander::uniquePace() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander10uniquePaceEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def uniqueAmountVariation(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleWander::uniqueAmountVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#uniqueAmountVariation
    """
    #  float QQuick3DParticleWander::uniqueAmountVariation() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander21uniqueAmountVariationEv',
    )

  def uniquePaceVariation(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleWander::uniquePaceVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#uniquePaceVariation
    """
    #  float QQuick3DParticleWander::uniquePaceVariation() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander19uniquePaceVariationEv',
    )

  def fadeInDuration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleWander::fadeInDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#fadeInDuration
    """
    #  int QQuick3DParticleWander::fadeInDuration() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander14fadeInDurationEv',
    )

  def fadeOutDuration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleWander::fadeOutDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#fadeOutDuration
    """
    #  int QQuick3DParticleWander::fadeOutDuration() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleWander15fadeOutDurationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setGlobalAmount(self, globalAmount: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setGlobalAmount(const QVector3D
    &globalAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setGlobalAmount

    Parameters
    ----------

    globalAmount : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleWander::setGlobalAmount(const QVector3D
    #      &globalAmount)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander15setGlobalAmountERK9QVector3D',
        self._valueOf(globalAmount),
    )

  @overload(QVector3D)
  def setGlobalPace(self, globalPace: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setGlobalPace(const QVector3D
    &globalPace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setGlobalPace

    Parameters
    ----------

    globalPace : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleWander::setGlobalPace(const QVector3D
    #      &globalPace)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander13setGlobalPaceERK9QVector3D',
        self._valueOf(globalPace),
    )

  @overload(QVector3D)
  def setGlobalPaceStart(self, globalPaceStart: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setGlobalPaceStart(const
    QVector3D &globalPaceStart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setGlobalPaceStart

    Parameters
    ----------

    globalPaceStart : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleWander::setGlobalPaceStart(const QVector3D
    #      &globalPaceStart)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander18setGlobalPaceStartERK9QVector3D',
        self._valueOf(globalPaceStart),
    )

  @overload(QVector3D)
  def setUniqueAmount(self, uniqueAmount: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setUniqueAmount(const QVector3D
    &uniqueAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setUniqueAmount

    Parameters
    ----------

    uniqueAmount : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleWander::setUniqueAmount(const QVector3D
    #      &uniqueAmount)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander15setUniqueAmountERK9QVector3D',
        self._valueOf(uniqueAmount),
    )

  @overload(QVector3D)
  def setUniquePace(self, uniquePace: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setUniquePace(const QVector3D
    &uniquePace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setUniquePace

    Parameters
    ----------

    uniquePace : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleWander::setUniquePace(const QVector3D
    #      &uniquePace)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander13setUniquePaceERK9QVector3D',
        self._valueOf(uniquePace),
    )

  @overload(float)
  def setUniqueAmountVariation(self, uniqueAmountVariation: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setUniqueAmountVariation(float
    uniqueAmountVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html

    Parameters
    ----------

    uniqueAmountVariation : float
      Passed on as it is.
    """
    #  void QQuick3DParticleWander::setUniqueAmountVariation(float
    #      uniqueAmountVariation)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander24setUniqueAmountVariationEf',
        uniqueAmountVariation,
    )

  @overload(float)
  def setUniquePaceVariation(self, uniquePaceVariation: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setUniquePaceVariation(float
    uniquePaceVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setUniquePaceVariation

    Parameters
    ----------

    uniquePaceVariation : float
      Passed on as it is.
    """
    #  void QQuick3DParticleWander::setUniquePaceVariation(float
    #      uniquePaceVariation)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander22setUniquePaceVariationEf',
        uniquePaceVariation,
    )

  @overload(int)
  def setFadeInDuration(self, fadeInDuration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setFadeInDuration(int
    fadeInDuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setFadeInDuration

    Parameters
    ----------

    fadeInDuration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleWander::setFadeInDuration(int fadeInDuration)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander17setFadeInDurationEi',
        fadeInDuration,
    )

  @overload(int)
  def setFadeOutDuration(self, fadeOutDuration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::setFadeOutDuration(int
    fadeOutDuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#setFadeOutDuration

    Parameters
    ----------

    fadeOutDuration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleWander::setFadeOutDuration(int fadeOutDuration)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander18setFadeOutDurationEi',
        fadeOutDuration,
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
    'QQuick3DParticleWander::QQuick3DParticleWander(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#QQuick3DParticleWander

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleWander::QQuick3DParticleWander(QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleWander, lambda: Rituals.call(
        'ritual_ZN22QQuick3DParticleWanderC1EP12QQuick3DNode',
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

  def globalAmountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::globalAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#globalAmountChanged
    """
    #  void QQuick3DParticleWander::globalAmountChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander19globalAmountChangedEv',
    )

  def globalPaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::globalPaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#globalPaceChanged
    """
    #  void QQuick3DParticleWander::globalPaceChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander17globalPaceChangedEv',
    )

  def globalPaceStartChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::globalPaceStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#globalPaceStartChanged
    """
    #  void QQuick3DParticleWander::globalPaceStartChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander22globalPaceStartChangedEv',
    )

  def uniqueAmountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::uniqueAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#uniqueAmountChanged
    """
    #  void QQuick3DParticleWander::uniqueAmountChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander19uniqueAmountChangedEv',
    )

  def uniquePaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::uniquePaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#uniquePaceChanged
    """
    #  void QQuick3DParticleWander::uniquePaceChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander17uniquePaceChangedEv',
    )

  def uniqueAmountVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::uniqueAmountVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html
    """
    #  void QQuick3DParticleWander::uniqueAmountVariationChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander28uniqueAmountVariationChangedEv',
    )

  def uniquePaceVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::uniquePaceVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html
    """
    #  void QQuick3DParticleWander::uniquePaceVariationChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander26uniquePaceVariationChangedEv',
    )

  def fadeInDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::fadeInDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#fadeInDurationChanged
    """
    #  void QQuick3DParticleWander::fadeInDurationChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander21fadeInDurationChangedEv',
    )

  def fadeOutDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::fadeOutDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#fadeOutDurationChanged
    """
    #  void QQuick3DParticleWander::fadeOutDurationChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleWander22fadeOutDurationChangedEv',
    )

  @overload(QQuick3DParticleData, QQuick3DParticleDataCurrent, float)
  @overload(QQuick3DParticleData, NoneType, float)
  def affectParticle(
      self,
      sd: QQuick3DParticleData,
      d: Optional[QQuick3DParticleDataCurrent],
      time: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleWander::affectParticle(const
    QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlewander.html#affectParticle

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
    #  void QQuick3DParticleWander::affectParticle(const QQuick3DParticleData
    #      &sd, QQuick3DParticleDataCurrent *d, float time)
    ritual = (
        'ritual_ZN22QQuick3DParticleWander14affectParticleERK20QQuick3DPart'
        'icleDataP27QQuick3DParticleDataCurrentf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuick3DParticleWander14affectParticleERK20QQuick'
          '3DParticleDataP27QQuick3DParticleDataCurrentf')
    self.uglySide.call(ritual, self._valueOf(sd), self._addressOf(d), time)
