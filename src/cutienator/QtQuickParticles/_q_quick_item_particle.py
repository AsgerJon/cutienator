"""
QQuickItemParticle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickitemparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickItemParticle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickItem
from . import QQuickParticlePainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlComponent
  from ..QtQuick import QSGNode
  from . import QQuickItemParticleAttached, QQuickParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickParticleSystem = WAIT['QQuickParticleSystem']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemParticle(QQuickParticlePainter):
  """
  The cute side of Qt's QQuickItemParticle: a plain Python object standing in
  front of one C++ QQuickItemParticle.

  It is built on the cute 'QQuickParticlePainter', as Qt's QQuickItemParticle
  is built on Qt's QQuickParticlePainter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemParticle that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'fade',
  'updatePaintNode', 'qmlAttachedProperties', 'delegate', 'fadeChanged',
  'delegateChanged', 'freeze', 'unfreeze', 'take', 'give', 'setFade',
  'setDelegate', 'reset', 'commit', 'initialize', 'prepareNextFrame',
  'clockShouldUpdate', 'updateClock', 'reconnectSystem', 'reconnectParent',
  'processDeletables', 'tick'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemParticle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickItemParticle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickItemParticle::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickItemParticle::~QQuickItemParticle()': the destructor: Python
    never removes a C++ QQuickItemParticle.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickItemParticle is created at the first use, not by
    'QQuickItemParticle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemParticle.
  - Qt tells when it has removed the C++ QQuickItemParticle. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickItemParticle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#tr

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
    #  QString QQuickItemParticle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickItemParticle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickItemParticleAttached]:
    """
    Calls Qt's 'QQuickItemParticleAttached
    *QQuickItemParticle::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItemParticleAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemParticleAttached
    #      *QQuickItemParticle::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN18QQuickItemParticle21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickItemParticleAttached
    return QQuickItemParticleAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemParticle'

  #  A C++ QQuickItemParticle Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemParticle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickItemParticle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemParticle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickItemParticle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fade(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemParticle::fade() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#fade
    """
    #  bool QQuickItemParticle::fade() const
    return self.uglySide.call('ritual_ZNK18QQuickItemParticle4fadeEv')

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickItemParticle::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickItemParticle::delegate() const
    address = self.uglySide.call('ritual_ZNK18QQuickItemParticle8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def clockShouldUpdate(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemParticle::clockShouldUpdate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#clockShouldUpdate
    """
    #  bool QQuickItemParticle::clockShouldUpdate() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickItemParticle17clockShouldUpdateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFade(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::setFade(bool arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#setFade

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickItemParticle::setFade(bool arg)
    self.uglySide.call('ritual_ZN18QQuickItemParticle7setFadeEb', arg)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, arg: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::setDelegate(QQmlComponent *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#setDelegate

    Parameters
    ----------

    arg : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemParticle::setDelegate(QQmlComponent *arg)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle11setDelegateEP13QQmlComponent',
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemParticle::QQuickItemParticle(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#QQuickItemParticle

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickItemParticle::QQuickItemParticle(QQuickItem *parent)
    self._noteCreation(QQuickItemParticle, lambda: Rituals.call(
        'ritual_ZN18QQuickItemParticleC1EP10QQuickItem',
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

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickItemParticle::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickItemParticle::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN18QQuickItemParticle15updatePaintNodeEP7QSGNodePN10QQuick'
        'Item19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickItemParticle15updatePaintNodeEP7QSGNodePN10'
          'QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def fadeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::fadeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#fadeChanged
    """
    #  void QQuickItemParticle::fadeChanged()
    self.uglySide.call('ritual_ZN18QQuickItemParticle11fadeChangedEv')

  @overload(QQmlComponent)
  @overload(NoneType)
  def delegateChanged(self, arg: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::delegateChanged(QQmlComponent
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#delegateChanged

    Parameters
    ----------

    arg : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemParticle::delegateChanged(QQmlComponent *arg)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle15delegateChangedEP13QQmlComponent',
        self._addressOf(arg),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def freeze(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::freeze(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#freeze

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemParticle::freeze(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle6freezeEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def unfreeze(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::unfreeze(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#unfreeze

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemParticle::unfreeze(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle8unfreezeEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def take(
      self,
      item: Optional[QQuickItem],
      prioritize: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::take(QQuickItem *item, bool
    prioritize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#take

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prioritize : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickItemParticle::take(QQuickItem *item, bool prioritize)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle4takeEP10QQuickItemb',
        self._addressOf(item), prioritize,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def give(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::give(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#give

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemParticle::give(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle4giveEP10QQuickItem',
        self._addressOf(item),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#reset
    """
    #  void QQuickItemParticle::reset()
    ritual = 'ritual_ZN18QQuickItemParticle5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickItemParticle5resetEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def commit(self, gIdx: int, pIdx: int) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::commit(int gIdx, int pIdx)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#commit

    Parameters
    ----------

    gIdx : int
      Passed on as it is.

    pIdx : int
      Passed on as it is.
    """
    #  void QQuickItemParticle::commit(int gIdx, int pIdx)
    ritual = 'ritual_ZN18QQuickItemParticle6commitEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickItemParticle6commitEii'
    self.uglySide.call(ritual, gIdx, pIdx)

  @overload(int, int)
  def initialize(self, gIdx: int, pIdx: int) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::initialize(int gIdx, int pIdx)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#initialize

    Parameters
    ----------

    gIdx : int
      Passed on as it is.

    pIdx : int
      Passed on as it is.
    """
    #  void QQuickItemParticle::initialize(int gIdx, int pIdx)
    ritual = 'ritual_ZN18QQuickItemParticle10initializeEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickItemParticle10initializeEii'
    self.uglySide.call(ritual, gIdx, pIdx)

  def prepareNextFrame(self) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::prepareNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#prepareNextFrame
    """
    #  void QQuickItemParticle::prepareNextFrame()
    self.uglySide.call('ritual_ZN18QQuickItemParticle16prepareNextFrameEv')

  def updateClock(self) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::updateClock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#updateClock
    """
    #  void QQuickItemParticle::updateClock()
    self.uglySide.call('ritual_ZN18QQuickItemParticle11updateClockEv')

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def reconnectSystem(self, system: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::reconnectSystem(QQuickParticleSystem
    *system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#reconnectSystem

    Parameters
    ----------

    system : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemParticle::reconnectSystem(QQuickParticleSystem *system)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle15reconnectSystemEP20QQuickParticleSy'
        'stem',
        self._addressOf(system),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def reconnectParent(self, parent: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::reconnectParent(QQuickItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#reconnectParent

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemParticle::reconnectParent(QQuickItem *parent)
    self.uglySide.call(
        'ritual_ZN18QQuickItemParticle15reconnectParentEP10QQuickItem',
        self._addressOf(parent),
    )

  def processDeletables(self) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::processDeletables()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticle.html#processDeletables
    """
    #  void QQuickItemParticle::processDeletables()
    self.uglySide.call('ritual_ZN18QQuickItemParticle17processDeletablesEv')

  @overload()
  @overload(int)
  def tick(self, time: int = 0) -> None:
    """
    Calls Qt's 'void QQuickItemParticle::tick(int time)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemparticle.html#tick

    Parameters
    ----------

    time : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickItemParticle::tick(int time)
    self.uglySide.call('ritual_ZN18QQuickItemParticle4tickEi', time)
