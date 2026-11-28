"""
Qt3DCore::QNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::QNodePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObject = WAIT['QMetaObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNodePrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DCore::QNodePrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QNodePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's Qt3DCore::QNodePrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QNodePrivate that has a ritual and that
  Python can call so far, 27 names in all: 'init', 'setScene', 'scene',
  'setArbiter', 'notifyPropertyChange', 'notifyDynamicPropertyChange',
  'insertTree', 'update', 'markDirty', 'q_func', 'get', 'nodePtrDeleter',
  'unregisterDestructionHelper', 'findStaticMetaObject',
  '_q_postConstructorInit', '_q_ensureBackendNodeCreated',
  'createBackendNode', 'notifyDestructionChangesAndRemoveFromScene',
  '_q_addChild', '_q_removeChild', '_q_setParentHelper',
  'registerNotifiedProperties', 'unregisterNotifiedProperties',
  'propertyChanged', 'setSceneHelper', 'unsetSceneHelper',
  'addEntityComponentToScene'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QNodePrivate::~QNodePrivate()': the destructor: Python
    never removes a C++ Qt3DCore::QNodePrivate.
  - Qt's 'const QNode *Qt3DCore::QNodePrivate::q_func() const': takes in
    Python what 'QNode *Qt3DCore::QNodePrivate::q_func()' takes.
  - Qt's 'const QNodePrivate *Qt3DCore::QNodePrivate::get(const QNode *q)':
    takes in Python what 'QNodePrivate *Qt3DCore::QNodePrivate::get(QNode
    *q)' takes.

  What has no ritual
  ------------------

  7 of the 38 functions Qt declares: 6 a template; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DCore::QNodePrivate is created at the first use, not by
    'Qt3DCore::QNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QNodePrivate.
  - Each name of Qt's Qt3DCore::QNodePrivate that has no cute function yet,
    'registerDestructionHelper', 'registerPrivateDestructionHelper',
    'updatePropertyTrackMode', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def get(q: Optional[Qt3DCore.QNode]) -> Optional[QNodePrivate]:
    """
    Calls Qt's 'QNodePrivate *Qt3DCore::QNodePrivate::get(QNode *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNodePrivate *Qt3DCore::QNodePrivate::get(QNode *q)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore12QNodePrivate3getEPNS_5QNodeE',
        CuteMixin._addressOf(q),
    )
    return QNodePrivate._cuteAt(address)

  @staticmethod
  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def nodePtrDeleter(q: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::nodePtrDeleter(QNode *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#nodePtrDeleter

    Parameters
    ----------

    q : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::nodePtrDeleter(QNode *q)
    Rituals.call(
        'ritual_ZN8Qt3DCore12QNodePrivate14nodePtrDeleterEPNS_5QNodeE',
        CuteMixin._addressOf(q),
    )

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def findStaticMetaObject(
      metaObject: Optional[QMetaObject],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::QNodePrivate::findStaticMetaObject(const QMetaObject
    *metaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#findStaticMetaObject

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QNodePrivate::findStaticMetaObject(const
    #      QMetaObject *metaObject)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore12QNodePrivate20findStaticMetaObjectEPK11QMetaOb'
        'ject',
        CuteMixin._addressOf(metaObject, 'QMetaObject'),
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QNodePrivate'

  #  A C++ Qt3DCore::QNodePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QNodePrivate'

  #  The functions Qt calls itself that Qt3DCore::QNodePrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setScene': (
          ('_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QScene'),
           )),
      ),
      'update': (
          ('_ZN8Qt3DCore12QNodePrivate6updateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scene(self) -> Optional[Qt3DCore.QScene]:
    """
    Calls Qt's 'QScene *Qt3DCore::QNodePrivate::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#scene

    Returns
    -------

    Optional[Qt3DCore.QScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScene *Qt3DCore::QNodePrivate::scene() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore12QNodePrivate5sceneEv')
    return Qt3DCore.QScene._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QScene'])
  @overload(NoneType)
  def setScene(self, scene: Optional[Qt3DCore.QScene]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::setScene(QScene *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#setScene

    Parameters
    ----------

    scene : Optional[Qt3DCore.QScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
    ritual = 'ritual_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE'
    self.uglySide.call(ritual, self._addressOf(scene))

  @overload(WAIT['Qt3DCore.QChangeArbiter'])
  @overload(NoneType)
  def setArbiter(self, arbiter: Optional[Qt3DCore.QChangeArbiter]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::setArbiter(QChangeArbiter
    *arbiter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#setArbiter

    Parameters
    ----------

    arbiter : Optional[Qt3DCore.QChangeArbiter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::setArbiter(QChangeArbiter *arbiter)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate10setArbiterEPNS_14QChangeArbiterE',
        self._addressOf(arbiter),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def setSceneHelper(self, root: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::setSceneHelper(QNode *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#setSceneHelper

    Parameters
    ----------

    root : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::setSceneHelper(QNode *root)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate14setSceneHelperEPNS_5QNodeE',
        self._addressOf(root),
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
    Notes what was given, for Qt's 'Qt3DCore::QNodePrivate::QNodePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#QNodePrivate
    """
    #  Qt3DCore::QNodePrivate::QNodePrivate()
    self._noteCreation(QNodePrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore12QNodePrivateC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def init(self, parent: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::init(QNode *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#init

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::init(QNode *parent)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate4initEPNS_5QNodeE',
        self._addressOf(parent),
    )

  @overload(str, QVariant)
  @overload(NoneType, QVariant)
  def notifyPropertyChange(
      self,
      name: Optional[str],
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::notifyPropertyChange(const char
    *name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#notifyPropertyChange

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DCore::QNodePrivate::notifyPropertyChange(const char *name,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate20notifyPropertyChangeEPKcRK8QVari'
        'ant',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(QByteArray, QVariant)
  def notifyDynamicPropertyChange(
      self,
      name: QByteArray,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QNodePrivate::notifyDynamicPropertyChange(const QByteArray
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DCore::QNodePrivate::notifyDynamicPropertyChange(const
    #      QByteArray &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate27notifyDynamicPropertyChangeERK10'
        'QByteArrayRK8QVariant',
        self._valueOf(name), self._valueOf(value),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  @overload(WAIT['Qt3DCore.QNode'], int)
  @overload(NoneType, int)
  def insertTree(
      self,
      treeRoot: Optional[Qt3DCore.QNode],
      depth: int = 0,
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::insertTree(QNode *treeRoot, int
    depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#insertTree

    Parameters
    ----------

    treeRoot : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    depth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void Qt3DCore::QNodePrivate::insertTree(QNode *treeRoot, int depth)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate10insertTreeEPNS_5QNodeEi',
        self._addressOf(treeRoot), depth,
    )

  def update(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#update
    """
    #  void Qt3DCore::QNodePrivate::update()
    ritual = 'ritual_ZN8Qt3DCore12QNodePrivate6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore12QNodePrivate6updateEv'
    self.uglySide.call(ritual)

  @overload(Qt3DCore.QScene.DirtyNodeSet)
  def markDirty(self, changes: Qt3DCore.QScene.DirtyNodeSet) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::markDirty(QScene::DirtyNodeSet
    changes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#markDirty

    Parameters
    ----------

    changes : Qt3DCore.QScene.DirtyNodeSet
      Passed on as its number.
    """
    #  void Qt3DCore::QNodePrivate::markDirty(QScene::DirtyNodeSet changes)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate9markDirtyE6QFlagsINS_6QScene13Dir'
        'tyNodeFlagEE',
        changes.value,
    )

  def q_func(self) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QNodePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QNodePrivate::q_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore12QNodePrivate6q_funcEv')
    return Qt3DCore.QNode._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def unregisterDestructionHelper(
      self,
      node: Optional[Qt3DCore.QNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QNodePrivate::unregisterDestructionHelper(QNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::unregisterDestructionHelper(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate27unregisterDestructionHelperEPNS_'
        '5QNodeE',
        self._addressOf(node),
    )

  def _q_postConstructorInit(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::_q_postConstructorInit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#_q_postConstructorInit
    """
    #  void Qt3DCore::QNodePrivate::_q_postConstructorInit()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate22_q_postConstructorInitEv',
    )

  def _q_ensureBackendNodeCreated(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::_q_ensureBackendNodeCreated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html
    """
    #  void Qt3DCore::QNodePrivate::_q_ensureBackendNodeCreated()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate27_q_ensureBackendNodeCreatedEv',
    )

  def createBackendNode(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::createBackendNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#createBackendNode
    """
    #  void Qt3DCore::QNodePrivate::createBackendNode()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate17createBackendNodeEv',
    )

  def notifyDestructionChangesAndRemoveFromScene(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QNodePrivate::notifyDestructionChangesAndRemoveFromScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html
    """
    #  void Qt3DCore::QNodePrivate::
    #      notifyDestructionChangesAndRemoveFromScene()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate42notifyDestructionChangesAndRemov'
        'eFromSceneEv',
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def _q_addChild(self, childNode: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::_q_addChild(QNode *childNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#_q_addChild

    Parameters
    ----------

    childNode : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::_q_addChild(QNode *childNode)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate11_q_addChildEPNS_5QNodeE',
        self._addressOf(childNode),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def _q_removeChild(self, childNode: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::_q_removeChild(QNode
    *childNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#_q_removeChild

    Parameters
    ----------

    childNode : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::_q_removeChild(QNode *childNode)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate14_q_removeChildEPNS_5QNodeE',
        self._addressOf(childNode),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def _q_setParentHelper(self, parent: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::_q_setParentHelper(QNode
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#_q_setParentHelper

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::_q_setParentHelper(QNode *parent)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate18_q_setParentHelperEPNS_5QNodeE',
        self._addressOf(parent),
    )

  def registerNotifiedProperties(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::registerNotifiedProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html
    """
    #  void Qt3DCore::QNodePrivate::registerNotifiedProperties()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate26registerNotifiedPropertiesEv',
    )

  def unregisterNotifiedProperties(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::unregisterNotifiedProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html
    """
    #  void Qt3DCore::QNodePrivate::unregisterNotifiedProperties()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate28unregisterNotifiedPropertiesEv',
    )

  @overload(int)
  def propertyChanged(self, propertyIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::propertyChanged(int
    propertyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#propertyChanged

    Parameters
    ----------

    propertyIndex : int
      Passed on as it is.
    """
    #  void Qt3DCore::QNodePrivate::propertyChanged(int propertyIndex)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate15propertyChangedEi', propertyIndex,
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def unsetSceneHelper(self, root: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::unsetSceneHelper(QNode *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html#unsetSceneHelper

    Parameters
    ----------

    root : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::unsetSceneHelper(QNode *root)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate16unsetSceneHelperEPNS_5QNodeE',
        self._addressOf(root),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def addEntityComponentToScene(
      self,
      root: Optional[Qt3DCore.QNode],
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodePrivate::addEntityComponentToScene(QNode
    *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeprivate.html

    Parameters
    ----------

    root : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodePrivate::addEntityComponentToScene(QNode *root)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodePrivate25addEntityComponentToSceneEPNS_5Q'
        'NodeE',
        self._addressOf(root),
    )

  @staticmethod
  def registerDestructionHelper(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodePrivate::registerDestructionHelper': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodePrivate.registerDestructionHelper' has no cute "
        "function yet. Qt's "
        "'Qt3DCore::QNodePrivate::registerDestructionHelper': a template: a "
        "pattern and no single function.")

  @staticmethod
  def registerPrivateDestructionHelper(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodePrivate::registerPrivateDestructionHelper': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodePrivate.registerPrivateDestructionHelper' has no "
        "cute function yet. Qt's "
        "'Qt3DCore::QNodePrivate::registerPrivateDestructionHelper': a "
        "template: a pattern and no single function.")

  @staticmethod
  def updatePropertyTrackMode(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QNodePrivate::updatePropertyTrackMode()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodePrivate.updatePropertyTrackMode' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QNodePrivate::updatePropertyTrackMode()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
