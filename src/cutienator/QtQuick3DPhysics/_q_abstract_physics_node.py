"""
QAbstractPhysicsNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qabstractphysicsnode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstractPhysicsNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractPhysicsNode(QQuick3DNode):
  """
  The cute side of Qt's QAbstractPhysicsNode: a plain Python object standing
  in front of one C++ QAbstractPhysicsNode.

  It is built on the cute 'QQuick3DNode', as Qt's QAbstractPhysicsNode is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractPhysicsNode that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr',
  'sendContactReports', 'setSendContactReports', 'receiveContactReports',
  'setReceiveContactReports', 'sendTriggerReports', 'setSendTriggerReports',
  'receiveTriggerReports', 'setReceiveTriggerReports', 'hasStaticShapes',
  'filterGroup', 'setfilterGroup', 'filterIgnoreGroups',
  'setFilterIgnoreGroups', 'onShapeDestroyed', 'onShapeNeedsRebuild',
  'sendContactReportsChanged', 'receiveContactReportsChanged',
  'sendTriggerReportsChanged', 'receiveTriggerReportsChanged',
  'enteredTriggerBody', 'exitedTriggerBody', 'filterGroupChanged',
  'filterIgnoreGroupsChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractPhysicsNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractPhysicsNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QAbstractPhysicsNode::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QAbstractPhysicsNode::~QAbstractPhysicsNode()': the destructor:
    Python never removes a C++ QAbstractPhysicsNode.
  - Qt's 'QQmlListProperty<QAbstractCollisionShape>
    QAbstractPhysicsNode::collisionShapes()': gives a type Python has no way
    to take yet.
  - Qt's 'const QVector<QAbstractCollisionShape *>
    &QAbstractPhysicsNode::getCollisionShapesList() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QAbstractPhysicsNode::updateFromPhysicsTransform(const
    physx::PxTransform &transform)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QAbstractPhysicsNode::registerContact(QAbstractPhysicsNode
    *body, const QVector<QVector3D> &positions, const QVector<QVector3D>
    &impulses, const QVector<QVector3D> &normals)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QAbstractPhysXNode *QAbstractPhysicsNode::createPhysXBackend()':
    gives 'QAbstractPhysXNode', which has no cute class yet.
  - Qt's 'void QAbstractPhysicsNode::bodyContact(QAbstractPhysicsNode *body,
    const QVector<QVector3D> &positions, const QVector<QVector3D> &impulses,
    const QVector<QVector3D> &normals)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QAbstractPhysicsNode::qmlAppendShape(
    QQmlListProperty<QAbstractCollisionShape> *list, QAbstractCollisionShape
    *shape)': names 'QQmlListProperty<QAbstractCollisionShape>', which has no
    cute class yet.
  - Qt's 'QAbstractCollisionShape *QAbstractPhysicsNode::qmlShapeAt(
    QQmlListProperty<QAbstractCollisionShape> *list, qsizetype index)': names
    'QQmlListProperty<QAbstractCollisionShape>', which has no cute class yet.
  - Qt's 'qsizetype QAbstractPhysicsNode::qmlShapeCount(
    QQmlListProperty<QAbstractCollisionShape> *list)': names
    'QQmlListProperty<QAbstractCollisionShape>', which has no cute class yet.
  - Qt's 'void QAbstractPhysicsNode::qmlClearShapes(
    QQmlListProperty<QAbstractCollisionShape> *list)': names
    'QQmlListProperty<QAbstractCollisionShape>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 42 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractPhysicsNode is created at the first use, not by
    'QAbstractPhysicsNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractPhysicsNode.
  - Qt tells when it has removed the C++ QAbstractPhysicsNode. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractPhysicsNode that has no cute function yet,
    'bodyContact', 'collisionShapes', 'createPhysXBackend',
    'getCollisionShapesList', 'qmlAppendShape', 'qmlClearShapes',
    'qmlShapeAt', 'qmlShapeCount', 'registerContact',
    'updateFromPhysicsTransform', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QAbstractPhysicsNode::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractphysicsnode.html#tr

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
    #  QString QAbstractPhysicsNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QAbstractPhysicsNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractPhysicsNode'

  #  A C++ QAbstractPhysicsNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractPhysicsNode'

  #  The functions Qt calls itself that QAbstractPhysicsNode is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createPhysXBackend': (
          'QAbstractPhysXNode *QAbstractPhysicsNode::createPhysXBackend()',
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
    Calls Qt's 'const QMetaObject *QAbstractPhysicsNode::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractPhysicsNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sendContactReports(self) -> bool:
    """
    Calls Qt's 'bool QAbstractPhysicsNode::sendContactReports() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#sendContactReports
    """
    #  bool QAbstractPhysicsNode::sendContactReports() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode18sendContactReportsEv',
    )

  def receiveContactReports(self) -> bool:
    """
    Calls Qt's 'bool QAbstractPhysicsNode::receiveContactReports() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#receiveContactReports
    """
    #  bool QAbstractPhysicsNode::receiveContactReports() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode21receiveContactReportsEv',
    )

  def sendTriggerReports(self) -> bool:
    """
    Calls Qt's 'bool QAbstractPhysicsNode::sendTriggerReports() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#sendTriggerReports
    """
    #  bool QAbstractPhysicsNode::sendTriggerReports() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode18sendTriggerReportsEv',
    )

  def receiveTriggerReports(self) -> bool:
    """
    Calls Qt's 'bool QAbstractPhysicsNode::receiveTriggerReports() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#receiveTriggerReports
    """
    #  bool QAbstractPhysicsNode::receiveTriggerReports() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode21receiveTriggerReportsEv',
    )

  def hasStaticShapes(self) -> bool:
    """
    Calls Qt's 'bool QAbstractPhysicsNode::hasStaticShapes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#hasStaticShapes
    """
    #  bool QAbstractPhysicsNode::hasStaticShapes() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode15hasStaticShapesEv',
    )

  def filterGroup(self) -> int:
    """
    Calls Qt's 'int QAbstractPhysicsNode::filterGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#filterGroup
    """
    #  int QAbstractPhysicsNode::filterGroup() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode11filterGroupEv',
    )

  def filterIgnoreGroups(self) -> int:
    """
    Calls Qt's 'int QAbstractPhysicsNode::filterIgnoreGroups() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#filterIgnoreGroups
    """
    #  int QAbstractPhysicsNode::filterIgnoreGroups() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsNode18filterIgnoreGroupsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSendContactReports(self, sendContactReports: bool) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::setSendContactReports(bool
    sendContactReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#setSendContactReports

    Parameters
    ----------

    sendContactReports : bool
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::setSendContactReports(bool
    #      sendContactReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode21setSendContactReportsEb',
        sendContactReports,
    )

  @overload(bool)
  def setReceiveContactReports(self, receiveContactReports: bool) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::setReceiveContactReports(bool
    receiveContactReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#setReceiveContactReports

    Parameters
    ----------

    receiveContactReports : bool
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::setReceiveContactReports(bool
    #      receiveContactReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode24setReceiveContactReportsEb',
        receiveContactReports,
    )

  @overload(bool)
  def setSendTriggerReports(self, sendTriggerReports: bool) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::setSendTriggerReports(bool
    sendTriggerReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#setSendTriggerReports

    Parameters
    ----------

    sendTriggerReports : bool
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::setSendTriggerReports(bool
    #      sendTriggerReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode21setSendTriggerReportsEb',
        sendTriggerReports,
    )

  @overload(bool)
  def setReceiveTriggerReports(self, receiveTriggerReports: bool) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::setReceiveTriggerReports(bool
    receiveTriggerReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#setReceiveTriggerReports

    Parameters
    ----------

    receiveTriggerReports : bool
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::setReceiveTriggerReports(bool
    #      receiveTriggerReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode24setReceiveTriggerReportsEb',
        receiveTriggerReports,
    )

  @overload(int)
  def setFilterIgnoreGroups(self, newFilterIgnoreGroups: int) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::setFilterIgnoreGroups(int
    newFilterIgnoreGroups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#setFilterIgnoreGroups

    Parameters
    ----------

    newFilterIgnoreGroups : int
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::setFilterIgnoreGroups(int
    #      newFilterIgnoreGroups)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode21setFilterIgnoreGroupsEi',
        newFilterIgnoreGroups,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractPhysicsNode::QAbstractPhysicsNode()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#QAbstractPhysicsNode
    """
    #  QAbstractPhysicsNode::QAbstractPhysicsNode()
    self._noteCreation(QAbstractPhysicsNode, lambda: Rituals.call(
        'ritual_ZN20QAbstractPhysicsNodeC1Ev',
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

  @overload(int)
  def setfilterGroup(self, newfilterGroup: int) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::setfilterGroup(int
    newfilterGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#setfilterGroup

    Parameters
    ----------

    newfilterGroup : int
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::setfilterGroup(int newfilterGroup)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode14setfilterGroupEi', newfilterGroup,
    )

  @overload(QObject)
  @overload(NoneType)
  def onShapeDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::onShapeDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#onShapeDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractPhysicsNode::onShapeDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode16onShapeDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def onShapeNeedsRebuild(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::onShapeNeedsRebuild(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#onShapeNeedsRebuild

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractPhysicsNode::onShapeNeedsRebuild(QObject *object)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode19onShapeNeedsRebuildEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(float)
  def sendContactReportsChanged(self, sendContactReports: float) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::sendContactReportsChanged(float
    sendContactReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html

    Parameters
    ----------

    sendContactReports : float
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::sendContactReportsChanged(float
    #      sendContactReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode25sendContactReportsChangedEf',
        sendContactReports,
    )

  @overload(float)
  def receiveContactReportsChanged(
      self,
      receiveContactReports: float,
  ) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::receiveContactReportsChanged(float
    receiveContactReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html

    Parameters
    ----------

    receiveContactReports : float
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::receiveContactReportsChanged(float
    #      receiveContactReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode28receiveContactReportsChangedEf',
        receiveContactReports,
    )

  @overload(float)
  def sendTriggerReportsChanged(self, sendTriggerReports: float) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::sendTriggerReportsChanged(float
    sendTriggerReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html

    Parameters
    ----------

    sendTriggerReports : float
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::sendTriggerReportsChanged(float
    #      sendTriggerReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode25sendTriggerReportsChangedEf',
        sendTriggerReports,
    )

  @overload(float)
  def receiveTriggerReportsChanged(
      self,
      receiveTriggerReports: float,
  ) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::receiveTriggerReportsChanged(float
    receiveTriggerReports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html

    Parameters
    ----------

    receiveTriggerReports : float
      Passed on as it is.
    """
    #  void QAbstractPhysicsNode::receiveTriggerReportsChanged(float
    #      receiveTriggerReports)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode28receiveTriggerReportsChangedEf',
        receiveTriggerReports,
    )

  @overload(THIS)
  @overload(NoneType)
  def enteredTriggerBody(self, body: Optional[QAbstractPhysicsNode]) -> None:
    """
    Calls Qt's 'void
    QAbstractPhysicsNode::enteredTriggerBody(QAbstractPhysicsNode *body)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#enteredTriggerBody

    Parameters
    ----------

    body : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractPhysicsNode::enteredTriggerBody(QAbstractPhysicsNode
    #      *body)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode18enteredTriggerBodyEPS_',
        self._addressOf(body),
    )

  @overload(THIS)
  @overload(NoneType)
  def exitedTriggerBody(self, body: Optional[QAbstractPhysicsNode]) -> None:
    """
    Calls Qt's 'void
    QAbstractPhysicsNode::exitedTriggerBody(QAbstractPhysicsNode *body)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#exitedTriggerBody

    Parameters
    ----------

    body : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractPhysicsNode::exitedTriggerBody(QAbstractPhysicsNode
    #      *body)
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode17exitedTriggerBodyEPS_',
        self._addressOf(body),
    )

  def filterGroupChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::filterGroupChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html#filterGroupChanged
    """
    #  void QAbstractPhysicsNode::filterGroupChanged()
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode18filterGroupChangedEv',
    )

  def filterIgnoreGroupsChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsNode::filterIgnoreGroupsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsnode.html
    """
    #  void QAbstractPhysicsNode::filterIgnoreGroupsChanged()
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsNode25filterIgnoreGroupsChangedEv',
    )

  @staticmethod
  def bodyContact(*__, **_) -> Never:
    """
    Qt's 'void QAbstractPhysicsNode::bodyContact(QAbstractPhysicsNode *body,
    const QVector<QVector3D> &positions, const QVector<QVector3D> &impulses,
    const QVector<QVector3D> &normals)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.bodyContact' has no cute function yet. Qt's "
        "'void QAbstractPhysicsNode::bodyContact(QAbstractPhysicsNode "
        "*body, const QVector<QVector3D> &positions, const "
        "QVector<QVector3D> &impulses, const QVector<QVector3D> &normals)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def collisionShapes(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QAbstractCollisionShape>
    QAbstractPhysicsNode::collisionShapes()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.collisionShapes' has no cute function yet. "
        "Qt's 'QQmlListProperty<QAbstractCollisionShape> "
        "QAbstractPhysicsNode::collisionShapes()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def createPhysXBackend(*__, **_) -> Never:
    """
    Qt's 'QAbstractPhysXNode *QAbstractPhysicsNode::createPhysXBackend()':
    gives 'QAbstractPhysXNode', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.createPhysXBackend' has no cute function "
        "yet. Qt's 'QAbstractPhysXNode "
        "*QAbstractPhysicsNode::createPhysXBackend()': gives "
        "'QAbstractPhysXNode', which has no cute class yet.")

  @staticmethod
  def getCollisionShapesList(*__, **_) -> Never:
    """
    Qt's 'const QVector<QAbstractCollisionShape *>
    &QAbstractPhysicsNode::getCollisionShapesList() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.getCollisionShapesList' has no cute function "
        "yet. Qt's 'const QVector<QAbstractCollisionShape *> "
        "&QAbstractPhysicsNode::getCollisionShapesList() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def qmlAppendShape(*__, **_) -> Never:
    """
    Qt's 'void QAbstractPhysicsNode::qmlAppendShape(
    QQmlListProperty<QAbstractCollisionShape> *list, QAbstractCollisionShape
    *shape)': names 'QQmlListProperty<QAbstractCollisionShape>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.qmlAppendShape' has no cute function yet. "
        "Qt's 'void "
        "QAbstractPhysicsNode::qmlAppendShape(QQmlListProperty<QAbstractColl"
        "isionShape> *list, QAbstractCollisionShape *shape)': names "
        "'QQmlListProperty<QAbstractCollisionShape>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlClearShapes(*__, **_) -> Never:
    """
    Qt's 'void QAbstractPhysicsNode::qmlClearShapes(
    QQmlListProperty<QAbstractCollisionShape> *list)': names
    'QQmlListProperty<QAbstractCollisionShape>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.qmlClearShapes' has no cute function yet. "
        "Qt's 'void "
        "QAbstractPhysicsNode::qmlClearShapes(QQmlListProperty<QAbstractColl"
        "isionShape> *list)': names "
        "'QQmlListProperty<QAbstractCollisionShape>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlShapeAt(*__, **_) -> Never:
    """
    Qt's 'QAbstractCollisionShape *QAbstractPhysicsNode::qmlShapeAt(
    QQmlListProperty<QAbstractCollisionShape> *list, qsizetype index)': names
    'QQmlListProperty<QAbstractCollisionShape>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.qmlShapeAt' has no cute function yet. Qt's "
        "'QAbstractCollisionShape "
        "*QAbstractPhysicsNode::qmlShapeAt(QQmlListProperty<QAbstractCollisi"
        "onShape> *list, qsizetype index)': names "
        "'QQmlListProperty<QAbstractCollisionShape>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlShapeCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QAbstractPhysicsNode::qmlShapeCount(
    QQmlListProperty<QAbstractCollisionShape> *list)': names
    'QQmlListProperty<QAbstractCollisionShape>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.qmlShapeCount' has no cute function yet. "
        "Qt's 'qsizetype "
        "QAbstractPhysicsNode::qmlShapeCount(QQmlListProperty<QAbstractColli"
        "sionShape> *list)': names "
        "'QQmlListProperty<QAbstractCollisionShape>', which has no cute "
        "class yet.")

  @staticmethod
  def registerContact(*__, **_) -> Never:
    """
    Qt's 'void QAbstractPhysicsNode::registerContact(QAbstractPhysicsNode
    *body, const QVector<QVector3D> &positions, const QVector<QVector3D>
    &impulses, const QVector<QVector3D> &normals)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.registerContact' has no cute function yet. "
        "Qt's 'void "
        "QAbstractPhysicsNode::registerContact(QAbstractPhysicsNode *body, "
        "const QVector<QVector3D> &positions, const QVector<QVector3D> "
        "&impulses, const QVector<QVector3D> &normals)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def updateFromPhysicsTransform(*__, **_) -> Never:
    """
    Qt's 'void QAbstractPhysicsNode::updateFromPhysicsTransform(const
    physx::PxTransform &transform)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsNode.updateFromPhysicsTransform' has no cute "
        "function yet. Qt's 'void "
        "QAbstractPhysicsNode::updateFromPhysicsTransform(const "
        "physx::PxTransform &transform)': takes a type Python has no way to "
        "hand over yet.")
