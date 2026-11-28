"""
QQuickParticlePainter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlepainter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticlePainter to be private: it declares the class in a
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
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleData, QQuickParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']
  QQuickParticleSystem = WAIT['QQuickParticleSystem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticlePainter(QQuickItem):
  """
  The cute side of Qt's QQuickParticlePainter: a plain Python object standing
  in front of one C++ QQuickParticlePainter.

  It is built on the cute 'QQuickItem', as Qt's QQuickParticlePainter is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParticlePainter that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'load',
  'reload', 'setCount', 'count', 'performPendingCommits', 'system', 'groups',
  'itemChange', 'countChanged', 'systemChanged', 'groupsChanged',
  'setSystem', 'setGroups', 'calcSystemOffset', 'sceneGraphInvalidated',
  'reset', 'componentComplete', 'initialize', 'commit',
  'recalculateGroupIds'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickParticlePainter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickParticlePainter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickParticlePainter::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickParticlePainter::~QQuickParticlePainter()': the destructor:
    Python never removes a C++ QQuickParticlePainter.
  - Qt's 'const GroupIDs &QQuickParticlePainter::groupIds() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickParticlePainter is created at the first use, not by
    'QQuickParticlePainter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParticlePainter.
  - Qt tells when it has removed the C++ QQuickParticlePainter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickParticlePainter that has no cute function yet,
    'groupIds', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuickParticlePainter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#tr

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
    #  QString QQuickParticlePainter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickParticlePainter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticlePainter'

  #  A C++ QQuickParticlePainter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickParticlePainter'

  #  The functions Qt calls itself that QQuickParticlePainter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'sceneGraphInvalidated': (
          ('_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reset': (
          ('_ZN21QQuickParticlePainter5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initialize': (
          ('_ZN21QQuickParticlePainter10initializeEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'commit': (
          ('_ZN21QQuickParticlePainter6commitEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QQuickParticlePainter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickParticlePainter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticlePainter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickParticlePainter::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#count
    """
    #  int QQuickParticlePainter::count() const
    return self.uglySide.call('ritual_ZNK21QQuickParticlePainter5countEv')

  def system(self) -> Optional[QQuickParticleSystem]:
    """
    Calls Qt's 'QQuickParticleSystem *QQuickParticlePainter::system() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#system

    Returns
    -------

    Optional[QQuickParticleSystem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleSystem *QQuickParticlePainter::system() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticlePainter6systemEv',
    )
    from . import QQuickParticleSystem
    return QQuickParticleSystem._cuteAt(address)

  def groups(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickParticlePainter::groups() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#groups

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickParticlePainter::groups() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticlePainter6groupsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCount(self, c: int) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::setCount(int c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#setCount

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QQuickParticlePainter::setCount(int c)
    self.uglySide.call('ritual_ZN21QQuickParticlePainter8setCountEi', c)

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def setSystem(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::setSystem(QQuickParticleSystem
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#setSystem

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticlePainter::setSystem(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter9setSystemEP20QQuickParticleSystem',
        self._addressOf(arg),
    )

  @overload(QStringList)
  def setGroups(self, arg: QStringList) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::setGroups(const QStringList
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#setGroups

    Parameters
    ----------

    arg : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickParticlePainter::setGroups(const QStringList &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter9setGroupsERK5QListI7QStringE',
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
    'QQuickParticlePainter::QQuickParticlePainter(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#QQuickParticlePainter

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickParticlePainter::QQuickParticlePainter(QQuickItem *parent)
    self._noteCreation(QQuickParticlePainter, lambda: Rituals.call(
        'ritual_ZN21QQuickParticlePainterC1EP10QQuickItem',
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

  @overload(QQuickParticleData)
  @overload(NoneType)
  def load(self, a0: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::load(QQuickParticleData *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#load

    Parameters
    ----------

    a0 : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticlePainter::load(QQuickParticleData *a0)
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter4loadEP18QQuickParticleData',
        self._addressOf(a0),
    )

  @overload(QQuickParticleData)
  @overload(NoneType)
  def reload(self, a0: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::reload(QQuickParticleData *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#reload

    Parameters
    ----------

    a0 : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticlePainter::reload(QQuickParticleData *a0)
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter6reloadEP18QQuickParticleData',
        self._addressOf(a0),
    )

  def performPendingCommits(self) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::performPendingCommits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#performPendingCommits
    """
    #  void QQuickParticlePainter::performPendingCommits()
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter21performPendingCommitsEv',
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickParticlePainter::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN21QQuickParticlePainter10itemChangeEN10QQuickItem10ItemCh'
        'angeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickParticlePainter10itemChangeEN10QQuickItem10'
          'ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#countChanged
    """
    #  void QQuickParticlePainter::countChanged()
    self.uglySide.call('ritual_ZN21QQuickParticlePainter12countChangedEv')

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def systemChanged(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void
    QQuickParticlePainter::systemChanged(QQuickParticleSystem *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#systemChanged

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticlePainter::systemChanged(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter13systemChangedEP20QQuickParticleS'
        'ystem',
        self._addressOf(arg),
    )

  @overload(QStringList)
  def groupsChanged(self, arg: QStringList) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::groupsChanged(const QStringList
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#groupsChanged

    Parameters
    ----------

    arg : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickParticlePainter::groupsChanged(const QStringList &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter13groupsChangedERK5QListI7QStringE',
        self._valueOf(arg),
    )

  @overload()
  @overload(bool)
  def calcSystemOffset(self, resetPending: bool = False) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::calcSystemOffset(bool
    resetPending)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#calcSystemOffset

    Parameters
    ----------

    resetPending : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickParticlePainter::calcSystemOffset(bool resetPending)
    self.uglySide.call(
        'ritual_ZN21QQuickParticlePainter16calcSystemOffsetEb', resetPending,
    )

  def sceneGraphInvalidated(self) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::sceneGraphInvalidated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#sceneGraphInvalidated
    """
    #  void QQuickParticlePainter::sceneGraphInvalidated()
    ritual = 'ritual_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv')
    self.uglySide.call(ritual)

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#reset
    """
    #  void QQuickParticlePainter::reset()
    ritual = 'ritual_ZN21QQuickParticlePainter5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickParticlePainter5resetEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#componentComplete
    """
    #  void QQuickParticlePainter::componentComplete()
    ritual = 'ritual_ZN21QQuickParticlePainter17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickParticlePainter17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def initialize(self, gIdx: int, pIdx: int) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::initialize(int gIdx, int pIdx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#initialize

    Parameters
    ----------

    gIdx : int
      Passed on as it is.

    pIdx : int
      Passed on as it is.
    """
    #  void QQuickParticlePainter::initialize(int gIdx, int pIdx)
    ritual = 'ritual_ZN21QQuickParticlePainter10initializeEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickParticlePainter10initializeEii'
    self.uglySide.call(ritual, gIdx, pIdx)

  @overload(int, int)
  def commit(self, gIdx: int, pIdx: int) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::commit(int gIdx, int pIdx)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlepainter.html#commit

    Parameters
    ----------

    gIdx : int
      Passed on as it is.

    pIdx : int
      Passed on as it is.
    """
    #  void QQuickParticlePainter::commit(int gIdx, int pIdx)
    ritual = 'ritual_ZN21QQuickParticlePainter6commitEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickParticlePainter6commitEii'
    self.uglySide.call(ritual, gIdx, pIdx)

  def recalculateGroupIds(self) -> None:
    """
    Calls Qt's 'void QQuickParticlePainter::recalculateGroupIds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlepainter.html#recalculateGroupIds
    """
    #  void QQuickParticlePainter::recalculateGroupIds() const
    self.uglySide.call(
        'ritual_ZNK21QQuickParticlePainter19recalculateGroupIdsEv',
    )

  @staticmethod
  def groupIds(*__, **_) -> Never:
    """
    Qt's 'const GroupIDs &QQuickParticlePainter::groupIds() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickParticlePainter.groupIds' has no cute function yet. Qt's "
        "'const GroupIDs &QQuickParticlePainter::groupIds() const': gives a "
        "type Python has no way to take yet.")
