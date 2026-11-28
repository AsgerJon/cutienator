"""
Qt3DCore::QNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNode(QObject):
  """
  The cute side of Qt's Qt3DCore::QNode: a plain Python object standing in
  front of one C++ Qt3DCore::QNode.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QNode is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QNode that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr', 'id', 'parentNode',
  'notificationsBlocked', 'blockNotifications', 'isEnabled', 'setParent',
  'setEnabled', 'parentChanged', 'enabledChanged', 'nodeDestroyed', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QNode::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Qt3DCore::QNode::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QNode::~QNode()': the destructor: Python never removes a
    C++ Qt3DCore::QNode.
  - Qt's 'QNodeVector Qt3DCore::QNode::childNodes() const': gives a type
    Python has no way to take yet.
  - Qt's 'Qt3DCore::QNode::QNode(QNodePrivate &dd, QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QNodePrivate *Qt3DCore::QNode::d_func() const': takes in
    Python what 'QNodePrivate *Qt3DCore::QNode::d_func()' takes.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 2 not a gap; 1 forbidden.

  What to expect
  --------------

  - The C++ Qt3DCore::QNode is created at the first use, not by
    'Qt3DCore::QNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QNode.
  - Qt tells when it has removed the C++ Qt3DCore::QNode. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QNode that has no cute function yet,
    'childNodes', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString Qt3DCore::QNode::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#tr

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
    #  QString Qt3DCore::QNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5QNode2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QNode'

  #  A C++ Qt3DCore::QNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QNode::metaObject() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore5QNode10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def id(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'QNodeId Qt3DCore::QNode::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#id

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  QNodeId Qt3DCore::QNode::id() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore5QNode2idEv')
    return Qt3DCore.QNodeId._cuteOwning(address)

  def parentNode(self) -> Optional[QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QNode::parentNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#parentNode

    Returns
    -------

    Optional[QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QNode::parentNode() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore5QNode10parentNodeEv')
    return QNode._cuteAt(address)

  def notificationsBlocked(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNode::notificationsBlocked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnode.html#notificationsBlocked
    """
    #  bool Qt3DCore::QNode::notificationsBlocked() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5QNode20notificationsBlockedEv',
    )

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNode::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#isEnabled
    """
    #  bool Qt3DCore::QNode::isEnabled() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore5QNode9isEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, parent: Optional[QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNode::setParent(QNode *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#setParent

    Parameters
    ----------

    parent : Optional[QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNode::setParent(QNode *parent)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5QNode9setParentEPS0_', self._addressOf(parent),
    )

  @overload(bool)
  def setEnabled(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNode::setEnabled(bool isEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#setEnabled

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QNode::setEnabled(bool isEnabled)
    self.uglySide.call('ritual_ZN8Qt3DCore5QNode10setEnabledEb', isEnabled)

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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parent: Optional[QNode] = None) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QNode::QNode(QNode *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#QNode

    Parameters
    ----------

    parent : Optional[QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QNode::QNode(QNode *parent)
    self._noteCreation(QNode, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5QNodeC1EPS0_', self._addressOf(parent),
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

  @overload(bool)
  def blockNotifications(self, block: bool) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QNode::blockNotifications(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnode.html#blockNotifications

    Parameters
    ----------

    block : bool
      Passed on as it is.
    """
    #  bool Qt3DCore::QNode::blockNotifications(bool block)
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore5QNode18blockNotificationsEb', block,
    )

  @overload(QObject)
  @overload(NoneType)
  def parentChanged(self, parent: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNode::parentChanged(QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#parentChanged

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNode::parentChanged(QObject *parent)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5QNode13parentChangedEP7QObject',
        self._addressOf(parent, 'QObject'),
    )

  @overload(bool)
  def enabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNode::enabledChanged(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#enabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QNode::enabledChanged(bool enabled)
    self.uglySide.call('ritual_ZN8Qt3DCore5QNode14enabledChangedEb', enabled)

  def nodeDestroyed(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNode::nodeDestroyed()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#nodeDestroyed
    """
    #  void Qt3DCore::QNode::nodeDestroyed()
    self.uglySide.call('ritual_ZN8Qt3DCore5QNode13nodeDestroyedEv')

  def d_func(self) -> Optional[Qt3DCore.QNodePrivate]:
    """
    Calls Qt's 'QNodePrivate *Qt3DCore::QNode::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnode.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNodePrivate *Qt3DCore::QNode::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore5QNode6d_funcEv')
    return Qt3DCore.QNodePrivate._cuteAt(address)

  @staticmethod
  def childNodes(*__, **_) -> Never:
    """
    Qt's 'QNodeVector Qt3DCore::QNode::childNodes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNode.childNodes' has no cute function yet. Qt's "
        "'QNodeVector Qt3DCore::QNode::childNodes() const': gives a type "
        "Python has no way to take yet.")
