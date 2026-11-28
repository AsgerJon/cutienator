"""
QQuick3DParticleSystemLogging binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystemlogging_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleSystemLogging to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleSystemLogging(QObject):
  """
  The cute side of Qt's QQuick3DParticleSystemLogging: a plain Python object
  standing in front of one C++ QQuick3DParticleSystemLogging.

  It is built on the cute 'QObject', as Qt's QQuick3DParticleSystemLogging is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleSystemLogging that has a ritual and
  that Python can call so far, 19 names in all: 'metaObject', 'tr',
  'loggingInterval', 'updates', 'particlesMax', 'particlesUsed', 'time',
  'timeAverage', 'timeDeviation', 'setLoggingInterval',
  'loggingIntervalChanged', 'updatesChanged', 'particlesMaxChanged',
  'particlesUsedChanged', 'timeChanged', 'timeAverageChanged',
  'timeDeviationChanged', 'updateTimes', 'resetData'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleSystemLogging::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleSystemLogging::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DParticleSystemLogging::qt_qmlMarker_anonymous()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleSystemLogging is created at the first use, not by
    'QQuick3DParticleSystemLogging(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleSystemLogging.
  - Qt tells when it has removed the C++ QQuick3DParticleSystemLogging. Every
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
    Calls Qt's 'QString QQuick3DParticleSystemLogging::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#tr

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
    #  QString QQuick3DParticleSystemLogging::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuick3DParticleSystemLogging2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleSystemLogging'

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
    *QQuick3DParticleSystemLogging::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleSystemLogging::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def loggingInterval(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystemLogging::loggingInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#loggingInterval
    """
    #  int QQuick3DParticleSystemLogging::loggingInterval() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging15loggingIntervalEv',
    )

  def updates(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystemLogging::updates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#updates
    """
    #  int QQuick3DParticleSystemLogging::updates() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging7updatesEv',
    )

  def particlesMax(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystemLogging::particlesMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#particlesMax
    """
    #  int QQuick3DParticleSystemLogging::particlesMax() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging12particlesMaxEv',
    )

  def particlesUsed(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystemLogging::particlesUsed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#particlesUsed
    """
    #  int QQuick3DParticleSystemLogging::particlesUsed() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging13particlesUsedEv',
    )

  def time(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSystemLogging::time() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#time
    """
    #  float QQuick3DParticleSystemLogging::time() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging4timeEv',
    )

  def timeAverage(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSystemLogging::timeAverage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#timeAverage
    """
    #  float QQuick3DParticleSystemLogging::timeAverage() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging11timeAverageEv',
    )

  def timeDeviation(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSystemLogging::timeDeviation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#timeDeviation
    """
    #  float QQuick3DParticleSystemLogging::timeDeviation() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleSystemLogging13timeDeviationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLoggingInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::setLoggingInterval(int
    interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSystemLogging::setLoggingInterval(int interval)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging18setLoggingIntervalEi',
        interval,
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
    'QQuick3DParticleSystemLogging::QQuick3DParticleSystemLogging(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleSystemLogging::QQuick3DParticleSystemLogging(QObject
    #      *parent)
    self._noteCreation(QQuick3DParticleSystemLogging, lambda: Rituals.call(
        'ritual_ZN29QQuick3DParticleSystemLoggingC1EP7QObject',
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

  def loggingIntervalChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSystemLogging::loggingIntervalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html
    """
    #  void QQuick3DParticleSystemLogging::loggingIntervalChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging22loggingIntervalChangedEv',
    )

  def updatesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::updatesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#updatesChanged
    """
    #  void QQuick3DParticleSystemLogging::updatesChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging14updatesChangedEv',
    )

  def particlesMaxChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::particlesMaxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html
    """
    #  void QQuick3DParticleSystemLogging::particlesMaxChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging19particlesMaxChangedEv',
    )

  def particlesUsedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::particlesUsedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html
    """
    #  void QQuick3DParticleSystemLogging::particlesUsedChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging20particlesUsedChangedEv',
    )

  def timeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::timeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#timeChanged
    """
    #  void QQuick3DParticleSystemLogging::timeChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging11timeChangedEv',
    )

  def timeAverageChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::timeAverageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html
    """
    #  void QQuick3DParticleSystemLogging::timeAverageChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging18timeAverageChangedEv',
    )

  def timeDeviationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::timeDeviationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html
    """
    #  void QQuick3DParticleSystemLogging::timeDeviationChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging20timeDeviationChangedEv',
    )

  @overload(int)
  def updateTimes(self, time: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::updateTimes(qint64
    time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#updateTimes

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSystemLogging::updateTimes(qint64 time)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging11updateTimesEx', time,
    )

  def resetData(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystemLogging::resetData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystemlogging.html#resetData
    """
    #  void QQuick3DParticleSystemLogging::resetData()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleSystemLogging9resetDataEv',
    )
