"""
QQuick3DParticleEmitBurst binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleemitburst_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleEmitBurst to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleEmitBurst(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuick3DParticleEmitBurst: a plain Python object
  standing in front of one C++ QQuick3DParticleEmitBurst.

  It is built on the cute 'QObject', as Qt's QQuick3DParticleEmitBurst is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QQuick3DParticleEmitBurst is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleEmitBurst that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'time',
  'amount', 'duration', 'setTime', 'setAmount', 'setDuration', 'timeChanged',
  'amountChanged', 'durationChanged', 'componentComplete', 'classBegin'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleEmitBurst::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleEmitBurst::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleEmitBurst::~QQuick3DParticleEmitBurst()': the
    destructor: Python never removes a C++ QQuick3DParticleEmitBurst.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleEmitBurst is created at the first use, not by
    'QQuick3DParticleEmitBurst(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleEmitBurst.
  - Qt tells when it has removed the C++ QQuick3DParticleEmitBurst. Every
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
    Calls Qt's 'QString QQuick3DParticleEmitBurst::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#tr

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
    #  QString QQuick3DParticleEmitBurst::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuick3DParticleEmitBurst2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleEmitBurst'

  #  Qt's QQuick3DParticleEmitBurst is built on more than one class. The part
  #  of a C++ QQuick3DParticleEmitBurst that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuick3DParticleEmitBurst_QQmlParserStatus',
  }

  #  A C++ QQuick3DParticleEmitBurst Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleEmitBurst'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleEmitBurst::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleEmitBurst::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleEmitBurst10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def time(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleEmitBurst::time() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#time
    """
    #  int QQuick3DParticleEmitBurst::time() const
    return self.uglySide.call('ritual_ZNK25QQuick3DParticleEmitBurst4timeEv')

  def amount(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleEmitBurst::amount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#amount
    """
    #  int QQuick3DParticleEmitBurst::amount() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleEmitBurst6amountEv',
    )

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleEmitBurst::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#duration
    """
    #  int QQuick3DParticleEmitBurst::duration() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DParticleEmitBurst8durationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::setTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#setTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitBurst::setTime(int time)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleEmitBurst7setTimeEi', time,
    )

  @overload(int)
  def setAmount(self, amount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::setAmount(int amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#setAmount

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitBurst::setAmount(int amount)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleEmitBurst9setAmountEi', amount,
    )

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::setDuration(int duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitBurst::setDuration(int duration)
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleEmitBurst11setDurationEi', duration,
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
    'QQuick3DParticleEmitBurst::QQuick3DParticleEmitBurst(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleEmitBurst::QQuick3DParticleEmitBurst(QObject *parent)
    self._noteCreation(QQuick3DParticleEmitBurst, lambda: Rituals.call(
        'ritual_ZN25QQuick3DParticleEmitBurstC1EP7QObject',
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

  def timeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::timeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#timeChanged
    """
    #  void QQuick3DParticleEmitBurst::timeChanged()
    self.uglySide.call('ritual_ZN25QQuick3DParticleEmitBurst11timeChangedEv')

  def amountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::amountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#amountChanged
    """
    #  void QQuick3DParticleEmitBurst::amountChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleEmitBurst13amountChangedEv',
    )

  def durationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::durationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#durationChanged
    """
    #  void QQuick3DParticleEmitBurst::durationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DParticleEmitBurst15durationChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#componentComplete
    """
    #  void QQuick3DParticleEmitBurst::componentComplete()
    ritual = 'ritual_ZN25QQuick3DParticleEmitBurst17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuick3DParticleEmitBurst17componentCompleteEv')
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitBurst::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitburst.html#classBegin
    """
    #  void QQuick3DParticleEmitBurst::classBegin()
    ritual = 'ritual_ZN25QQuick3DParticleEmitBurst10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuick3DParticleEmitBurst10classBeginEv'
    self.uglySide.call(ritual)
