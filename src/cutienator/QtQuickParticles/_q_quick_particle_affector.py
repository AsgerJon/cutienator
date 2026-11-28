"""
QQuickParticleAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticleaffector_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleAffector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleData, QQuickParticleExtruder
  from . import QQuickParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']
  QQuickParticleExtruder = WAIT['QQuickParticleExtruder']
  QQuickParticleSystem = WAIT['QQuickParticleSystem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticleAffector(QQuickItem):
  """
  The cute side of Qt's QQuickParticleAffector: a plain Python object
  standing in front of one C++ QQuickParticleAffector.

  It is built on the cute 'QQuickItem', as Qt's QQuickParticleAffector is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParticleAffector that has a ritual and that
  Python can call so far, 31 names in all: 'metaObject', 'tr',
  'affectSystem', 'reset', 'system', 'groups', 'enabled', 'onceOff', 'shape',
  'whenCollidingWith', 'systemChanged', 'groupsChanged', 'enabledChanged',
  'onceChanged', 'shapeChanged', 'affected', 'whenCollidingWithChanged',
  'setSystem', 'setGroups', 'setEnabled', 'setOnceOff', 'setShape',
  'setWhenCollidingWith', 'updateOffsets', 'affectParticle', 'activeGroup',
  'shouldAffect', 'postAffect', 'componentComplete', 'isAffectedConnected',
  'isColliding'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickParticleAffector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickParticleAffector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickParticleAffector::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickParticleAffector is created at the first use, not by
    'QQuickParticleAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParticleAffector.
  - Qt tells when it has removed the C++ QQuickParticleAffector. Every call
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
    Calls Qt's 'QString QQuickParticleAffector::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleaffector.html#tr

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
    #  QString QQuickParticleAffector::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickParticleAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticleAffector'

  #  The functions Qt calls itself that QQuickParticleAffector is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'affectSystem': (
          ('_ZN22QQuickParticleAffector12affectSystemEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'reset': (
          ('_ZN22QQuickParticleAffector5resetEP18QQuickParticleData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuickParticles:QQuickParticleData'),
           )),
      ),
      'affectParticle': (
          ('_ZN22QQuickParticleAffector14affectParticleEP18QQuickParticleDa'
           'tad',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuickParticles:QQuickParticleData'),
               ('double', 'number', ''),
           )),
      ),
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
    Calls Qt's 'const QMetaObject *QQuickParticleAffector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickParticleAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickParticleAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def system(self) -> Optional[QQuickParticleSystem]:
    """
    Calls Qt's 'QQuickParticleSystem *QQuickParticleAffector::system()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleaffector.html#system

    Returns
    -------

    Optional[QQuickParticleSystem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleSystem *QQuickParticleAffector::system() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickParticleAffector6systemEv',
    )
    from . import QQuickParticleSystem
    return QQuickParticleSystem._cuteAt(address)

  def groups(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickParticleAffector::groups() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleaffector.html#groups

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickParticleAffector::groups() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickParticleAffector6groupsEv',
    )
    return QStringList._cuteOwning(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleAffector::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#enabled
    """
    #  bool QQuickParticleAffector::enabled() const
    return self.uglySide.call('ritual_ZNK22QQuickParticleAffector7enabledEv')

  def onceOff(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleAffector::onceOff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#onceOff
    """
    #  bool QQuickParticleAffector::onceOff() const
    return self.uglySide.call('ritual_ZNK22QQuickParticleAffector7onceOffEv')

  def shape(self) -> Optional[QQuickParticleExtruder]:
    """
    Calls Qt's 'QQuickParticleExtruder *QQuickParticleAffector::shape()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleaffector.html#shape

    Returns
    -------

    Optional[QQuickParticleExtruder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleExtruder *QQuickParticleAffector::shape() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickParticleAffector5shapeEv',
    )
    from . import QQuickParticleExtruder
    return QQuickParticleExtruder._cuteAt(address)

  def whenCollidingWith(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickParticleAffector::whenCollidingWith()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#whenCollidingWith

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickParticleAffector::whenCollidingWith() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickParticleAffector17whenCollidingWithEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QQuickParticleData)
  @overload(NoneType)
  def isColliding(self, d: Optional[QQuickParticleData]) -> bool:
    """
    Calls Qt's 'bool QQuickParticleAffector::isColliding(QQuickParticleData
    *d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#isColliding

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickParticleAffector::isColliding(QQuickParticleData *d) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickParticleAffector11isCollidingEP18QQuickParticleD'
        'ata',
        self._addressOf(d),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def setSystem(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::setSystem(QQuickParticleSystem
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#setSystem

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleAffector::setSystem(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector9setSystemEP20QQuickParticleSyste'
        'm',
        self._addressOf(arg),
    )

  @overload(QStringList)
  def setGroups(self, arg: QStringList) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::setGroups(const QStringList
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#setGroups

    Parameters
    ----------

    arg : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickParticleAffector::setGroups(const QStringList &arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector9setGroupsERK5QListI7QStringE',
        self._valueOf(arg),
    )

  @overload(bool)
  def setEnabled(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::setEnabled(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#setEnabled

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleAffector::setEnabled(bool arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector10setEnabledEb', arg,
    )

  @overload(bool)
  def setOnceOff(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::setOnceOff(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#setOnceOff

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleAffector::setOnceOff(bool arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector10setOnceOffEb', arg,
    )

  @overload(QQuickParticleExtruder)
  @overload(NoneType)
  def setShape(self, arg: Optional[QQuickParticleExtruder]) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::setShape(QQuickParticleExtruder
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#setShape

    Parameters
    ----------

    arg : Optional[QQuickParticleExtruder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleAffector::setShape(QQuickParticleExtruder *arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector8setShapeEP22QQuickParticleExtrud'
        'er',
        self._addressOf(arg),
    )

  @overload(QStringList)
  def setWhenCollidingWith(self, arg: QStringList) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::setWhenCollidingWith(const
    QStringList &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#setWhenCollidingWith

    Parameters
    ----------

    arg : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickParticleAffector::setWhenCollidingWith(const QStringList
    #      &arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector20setWhenCollidingWithERK5QListI7'
        'QStringE',
        self._valueOf(arg),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickParticleAffector::QQuickParticleAffector(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#QQuickParticleAffector

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickParticleAffector::QQuickParticleAffector(QQuickItem *parent)
    self._noteCreation(QQuickParticleAffector, lambda: Rituals.call(
        'ritual_ZN22QQuickParticleAffectorC1EP10QQuickItem',
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

  @overload(float)
  def affectSystem(self, dt: float) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::affectSystem(qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#affectSystem

    Parameters
    ----------

    dt : float
      Passed on as it is.
    """
    #  void QQuickParticleAffector::affectSystem(qreal dt)
    ritual = 'ritual_ZN22QQuickParticleAffector12affectSystemEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickParticleAffector12affectSystemEd'
    self.uglySide.call(ritual, dt)

  @overload(QQuickParticleData)
  @overload(NoneType)
  def reset(self, a0: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::reset(QQuickParticleData *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleaffector.html#reset

    Parameters
    ----------

    a0 : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleAffector::reset(QQuickParticleData *a0)
    ritual = 'ritual_ZN22QQuickParticleAffector5resetEP18QQuickParticleData'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickParticleAffector5resetEP18QQuickParticleDat'
          'a')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def systemChanged(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleAffector::systemChanged(QQuickParticleSystem *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#systemChanged

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleAffector::systemChanged(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector13systemChangedEP20QQuickParticle'
        'System',
        self._addressOf(arg),
    )

  @overload(QStringList)
  def groupsChanged(self, arg: QStringList) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::groupsChanged(const QStringList
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#groupsChanged

    Parameters
    ----------

    arg : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickParticleAffector::groupsChanged(const QStringList &arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector13groupsChangedERK5QListI7QString'
        'E',
        self._valueOf(arg),
    )

  @overload(bool)
  def enabledChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::enabledChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#enabledChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleAffector::enabledChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector14enabledChangedEb', arg,
    )

  @overload(bool)
  def onceChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::onceChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#onceChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleAffector::onceChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector11onceChangedEb', arg,
    )

  @overload(QQuickParticleExtruder)
  @overload(NoneType)
  def shapeChanged(self, arg: Optional[QQuickParticleExtruder]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleAffector::shapeChanged(QQuickParticleExtruder *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#shapeChanged

    Parameters
    ----------

    arg : Optional[QQuickParticleExtruder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleAffector::shapeChanged(QQuickParticleExtruder *arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector12shapeChangedEP22QQuickParticleE'
        'xtruder',
        self._addressOf(arg),
    )

  @overload(float, float)
  def affected(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::affected(qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#affected

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickParticleAffector::affected(qreal x, qreal y)
    self.uglySide.call('ritual_ZN22QQuickParticleAffector8affectedEdd', x, y)

  @overload(QStringList)
  def whenCollidingWithChanged(self, arg: QStringList) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::whenCollidingWithChanged(const
    QStringList &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html

    Parameters
    ----------

    arg : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickParticleAffector::whenCollidingWithChanged(const
    #      QStringList &arg)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector24whenCollidingWithChangedERK5QLi'
        'stI7QStringE',
        self._valueOf(arg),
    )

  def updateOffsets(self) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::updateOffsets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#updateOffsets
    """
    #  void QQuickParticleAffector::updateOffsets()
    self.uglySide.call('ritual_ZN22QQuickParticleAffector13updateOffsetsEv')

  @overload(QQuickParticleData, float)
  @overload(NoneType, float)
  def affectParticle(
      self,
      d: Optional[QQuickParticleData],
      dt: float,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickParticleAffector::affectParticle(QQuickParticleData *d, qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickParticleAffector::affectParticle(QQuickParticleData *d,
    #      qreal dt)
    ritual = (
        'ritual_ZN22QQuickParticleAffector14affectParticleEP18QQuickParticl'
        'eDatad')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickParticleAffector14affectParticleEP18QQuickP'
          'articleDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)

  @overload(int)
  def activeGroup(self, g: int) -> bool:
    """
    Calls Qt's 'bool QQuickParticleAffector::activeGroup(int g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#activeGroup

    Parameters
    ----------

    g : int
      Passed on as it is.
    """
    #  bool QQuickParticleAffector::activeGroup(int g)
    return self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector11activeGroupEi', g,
    )

  @overload(QQuickParticleData)
  @overload(NoneType)
  def shouldAffect(self, datum: Optional[QQuickParticleData]) -> bool:
    """
    Calls Qt's 'bool QQuickParticleAffector::shouldAffect(QQuickParticleData
    *datum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#shouldAffect

    Parameters
    ----------

    datum : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickParticleAffector::shouldAffect(QQuickParticleData *datum)
    return self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector12shouldAffectEP18QQuickParticleD'
        'ata',
        self._addressOf(datum),
    )

  @overload(QQuickParticleData)
  @overload(NoneType)
  def postAffect(self, datum: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::postAffect(QQuickParticleData
    *datum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#postAffect

    Parameters
    ----------

    datum : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleAffector::postAffect(QQuickParticleData *datum)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector10postAffectEP18QQuickParticleDat'
        'a',
        self._addressOf(datum),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickParticleAffector::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#componentComplete
    """
    #  void QQuickParticleAffector::componentComplete()
    ritual = 'ritual_ZN22QQuickParticleAffector17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickParticleAffector17componentCompleteEv'
    self.uglySide.call(ritual)

  def isAffectedConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleAffector::isAffectedConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleaffector.html#isAffectedConnected
    """
    #  bool QQuickParticleAffector::isAffectedConnected()
    return self.uglySide.call(
        'ritual_ZN22QQuickParticleAffector19isAffectedConnectedEv',
    )
