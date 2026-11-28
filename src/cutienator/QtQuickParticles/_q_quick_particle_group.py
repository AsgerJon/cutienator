"""
QQuickParticleGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlegroup_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleGroup to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from ..QtQuick import QQuickStochasticState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleSystem = WAIT['QQuickParticleSystem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticleGroup(QQuickStochasticState, QQmlParserStatus):
  """
  The cute side of Qt's QQuickParticleGroup: a plain Python object standing
  in front of one C++ QQuickParticleGroup.

  It is built on the cute 'QQuickStochasticState', as Qt's
  QQuickParticleGroup is built on Qt's QQuickStochasticState, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's QQuickParticleGroup is built on Qt's QQmlParserStatus too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParticleGroup that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'system',
  'setSystem', 'delayRedirect', 'systemChanged', 'componentComplete',
  'classBegin', 'performDelayedRedirects'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickParticleGroup::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickParticleGroup::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> QQuickParticleGroup::particleChildren()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickParticleGroup is created at the first use, not by
    'QQuickParticleGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParticleGroup.
  - Qt tells when it has removed the C++ QQuickParticleGroup. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickParticleGroup that has no cute function yet,
    'particleChildren', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQuickParticleGroup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlegroup.html#tr

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
    #  QString QQuickParticleGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickParticleGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticleGroup'

  #  Qt's QQuickParticleGroup is built on more than one class. The part of a
  #  C++ QQuickParticleGroup that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickParticleGroup_QQmlParserStatus',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickParticleGroup::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickParticleGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickParticleGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def system(self) -> Optional[QQuickParticleSystem]:
    """
    Calls Qt's 'QQuickParticleSystem *QQuickParticleGroup::system() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlegroup.html#system

    Returns
    -------

    Optional[QQuickParticleSystem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleSystem *QQuickParticleGroup::system() const
    address = self.uglySide.call('ritual_ZNK19QQuickParticleGroup6systemEv')
    from . import QQuickParticleSystem
    return QQuickParticleSystem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def setSystem(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void QQuickParticleGroup::setSystem(QQuickParticleSystem
    *arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlegroup.html#setSystem

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleGroup::setSystem(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN19QQuickParticleGroup9setSystemEP20QQuickParticleSystem',
        self._addressOf(arg),
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
    'QQuickParticleGroup::QQuickParticleGroup(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroup.html#QQuickParticleGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickParticleGroup::QQuickParticleGroup(QObject *parent)
    self._noteCreation(QQuickParticleGroup, lambda: Rituals.call(
        'ritual_ZN19QQuickParticleGroupC1EP7QObject',
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

  @overload(QObject)
  @overload(NoneType)
  def delayRedirect(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickParticleGroup::delayRedirect(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroup.html#delayRedirect

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleGroup::delayRedirect(QObject *obj)
    self.uglySide.call(
        'ritual_ZN19QQuickParticleGroup13delayRedirectEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def systemChanged(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void QQuickParticleGroup::systemChanged(QQuickParticleSystem
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroup.html#systemChanged

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleGroup::systemChanged(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN19QQuickParticleGroup13systemChangedEP20QQuickParticleSys'
        'tem',
        self._addressOf(arg),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickParticleGroup::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroup.html#componentComplete
    """
    #  void QQuickParticleGroup::componentComplete()
    ritual = 'ritual_ZN19QQuickParticleGroup17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickParticleGroup17componentCompleteEv'
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickParticleGroup::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroup.html#classBegin
    """
    #  void QQuickParticleGroup::classBegin()
    ritual = 'ritual_ZN19QQuickParticleGroup10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickParticleGroup10classBeginEv'
    self.uglySide.call(ritual)

  def performDelayedRedirects(self) -> None:
    """
    Calls Qt's 'void QQuickParticleGroup::performDelayedRedirects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlegroup.html#performDelayedRedirects
    """
    #  void QQuickParticleGroup::performDelayedRedirects()
    self.uglySide.call(
        'ritual_ZN19QQuickParticleGroup23performDelayedRedirectsEv',
    )

  @staticmethod
  def particleChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickParticleGroup::particleChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickParticleGroup.particleChildren' has no cute function yet. "
        "Qt's 'QQmlListProperty<QObject> "
        "QQuickParticleGroup::particleChildren()': gives a type Python has "
        "no way to take yet.")
