"""
Qt3DCore::QAbstractAspectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QAbstractAspectPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAspectPrivate(QObjectPrivate, Qt3DCore.QAspectJobProviderInterface):
  """
  The cute side of Qt's Qt3DCore::QAbstractAspectPrivate: a plain Python
  object standing in front of one C++ Qt3DCore::QAbstractAspectPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DCore::QAbstractAspectPrivate is built on Qt's QObjectPrivate, and has
  everything that class has. It is built on the cute
  'Qt3DCore::QAspectJobProviderInterface' as well, as Qt's
  Qt3DCore::QAbstractAspectPrivate is built on Qt's
  Qt3DCore::QAspectJobProviderInterface too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractAspectPrivate that has a ritual
  and that Python can call so far, 11 names in all: 'services', 'jobManager',
  'jobsDone', 'frameDone', 'createBackendNode', 'clearBackendNode',
  'syncDirtyFrontEndNode', 'onEngineAboutToShutdown',
  'unregisterBackendType', 'q_func', 'get'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QAbstractAspectPrivate::~QAbstractAspectPrivate()': the
    destructor: Python never removes a C++ Qt3DCore::QAbstractAspectPrivate.
  - Qt's 'void
    Qt3DCore::QAbstractAspectPrivate::setRootAndCreateNodes(QEntity
    *rootObject, const QList<NodeTreeChange> &nodesTreeChanges)': takes a
    type Python has no way to hand over yet.
  - Qt's 'std::vector<QAspectJobPtr>
    Qt3DCore::QAbstractAspectPrivate::jobsToExecute(qint64 time)': gives a
    type Python has no way to take yet.
  - Qt's 'void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNodes(const
    QList<QNode *> &nodes)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    Qt3DCore::QAbstractAspectPrivate::syncDirtyEntityComponentNodes(const
    QList<ComponentRelationshipChange> &nodes)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QAbstractAspect *Qt3DCore::QAbstractAspectPrivate::q_func()
    const': takes in Python what 'QAbstractAspect
    *Qt3DCore::QAbstractAspectPrivate::q_func()' takes.
  - Qt's 'QBackendNodeMapperPtr
    Qt3DCore::QAbstractAspectPrivate::mapperForNode(const QMetaObject
    *metaObj) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractAspectPrivate is created at the first use, not
    by 'Qt3DCore::QAbstractAspectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractAspectPrivate.
  - Each name of Qt's Qt3DCore::QAbstractAspectPrivate that has no cute
    function yet, 'mapperForNode', 'setRootAndCreateNodes',
    'syncDirtyEntityComponentNodes', 'syncDirtyFrontEndNodes', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def get(
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> Optional[QAbstractAspectPrivate]:
    """
    Calls Qt's 'QAbstractAspectPrivate
    *Qt3DCore::QAbstractAspectPrivate::get(QAbstractAspect *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html#get

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspectPrivate
    #      *Qt3DCore::QAbstractAspectPrivate::get(QAbstractAspect *aspect)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore22QAbstractAspectPrivate3getEPNS_15QAbstractAspe'
        'ctE',
        CuteMixin._addressOf(aspect),
    )
    return QAbstractAspectPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractAspectPrivate'

  #  Qt's Qt3DCore::QAbstractAspectPrivate is built on more than one class.
  #  The part of a C++ Qt3DCore::QAbstractAspectPrivate that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'Qt3DCore::QAspectJobProviderInterface':
          'ritual_cast_Qt3DCore_QAbstractAspectPrivate_Qt3DCore_QAspectJobProviderInterface',
  }

  #  A C++ Qt3DCore::QAbstractAspectPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAbstractAspectPrivate'

  #  The functions Qt calls itself that Qt3DCore::QAbstractAspectPrivate is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'syncDirtyFrontEndNode': (
          ('_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPN'
           'S_5QNodeEPNS_12QBackendNodeEb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QNode'),
               ('address', 'address', 'Qt3DCore:Qt3DCore.QBackendNode'),
               ('bool', 'number', ''),
           )),
      ),
      'onEngineAboutToShutdown': (
          ('_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv',
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

  def services(self) -> Optional[Qt3DCore.QServiceLocator]:
    """
    Calls Qt's 'QServiceLocator *Qt3DCore::QAbstractAspectPrivate::services()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html#services

    Returns
    -------

    Optional[Qt3DCore.QServiceLocator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QServiceLocator *Qt3DCore::QAbstractAspectPrivate::services() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore22QAbstractAspectPrivate8servicesEv',
    )
    return Qt3DCore.QServiceLocator._cuteAt(address)

  def jobManager(self) -> Optional[Qt3DCore.QAbstractAspectJobManager]:
    """
    Calls Qt's 'QAbstractAspectJobManager
    *Qt3DCore::QAbstractAspectPrivate::jobManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html#jobManager

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspectJobManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspectJobManager
    #      *Qt3DCore::QAbstractAspectPrivate::jobManager() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore22QAbstractAspectPrivate10jobManagerEv',
    )
    return Qt3DCore.QAbstractAspectJobManager._cuteAt(address)

  @overload(WAIT['Qt3DCore.NodeTreeChange'])
  def createBackendNode(
      self,
      change: Qt3DCore.NodeTreeChange,
  ) -> Optional[Qt3DCore.QBackendNode]:
    """
    Calls Qt's 'QBackendNode
    *Qt3DCore::QAbstractAspectPrivate::createBackendNode(const NodeTreeChange
    &change) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html

    Parameters
    ----------

    change : Qt3DCore.NodeTreeChange
      Passed on as a value: Qt reads the C++ Qt3DCore::NodeTreeChange, which
      stays Python's own.

    Returns
    -------

    Optional[Qt3DCore.QBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBackendNode
    #      *Qt3DCore::QAbstractAspectPrivate::createBackendNode(const
    #      NodeTreeChange &change) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore22QAbstractAspectPrivate17createBackendNodeERKN'
        'S_14NodeTreeChangeE',
        self._valueOf(change),
    )
    return Qt3DCore.QBackendNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'Qt3DCore::QAbstractAspectPrivate::QAbstractAspectPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html
    """
    #  Qt3DCore::QAbstractAspectPrivate::QAbstractAspectPrivate()
    self._noteCreation(QAbstractAspectPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore22QAbstractAspectPrivateC1Ev',
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

  def jobsDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspectPrivate::jobsDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html#jobsDone
    """
    #  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
    ritual = 'ritual_ZN8Qt3DCore22QAbstractAspectPrivate8jobsDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate8jobsDoneEv'
    self.uglySide.call(ritual)

  def frameDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspectPrivate::frameDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html#frameDone
    """
    #  void Qt3DCore::QAbstractAspectPrivate::frameDone()
    ritual = 'ritual_ZN8Qt3DCore22QAbstractAspectPrivate9frameDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate9frameDoneEv'
    self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.NodeTreeChange'])
  def clearBackendNode(self, change: Qt3DCore.NodeTreeChange) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspectPrivate::clearBackendNode(const
    NodeTreeChange &change) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html

    Parameters
    ----------

    change : Qt3DCore.NodeTreeChange
      Passed on as a value: Qt reads the C++ Qt3DCore::NodeTreeChange, which
      stays Python's own.
    """
    #  void Qt3DCore::QAbstractAspectPrivate::clearBackendNode(const
    #      NodeTreeChange &change) const
    self.uglySide.call(
        'ritual_ZNK8Qt3DCore22QAbstractAspectPrivate16clearBackendNodeERKNS'
        '_14NodeTreeChangeE',
        self._valueOf(change),
    )

  @overload(WAIT['Qt3DCore.QNode'], WAIT['Qt3DCore.QBackendNode'], bool)
  @overload(WAIT['Qt3DCore.QNode'], NoneType, bool)
  @overload(NoneType, WAIT['Qt3DCore.QBackendNode'], bool)
  @overload(NoneType, NoneType, bool)
  def syncDirtyFrontEndNode(
      self,
      node: Optional[Qt3DCore.QNode],
      backend: Optional[Qt3DCore.QBackendNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode *node,
    QBackendNode *backend, bool firstTime) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    backend : Optional[Qt3DCore.QBackendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
    #      *node, QBackendNode *backend, bool firstTime) const
    ritual = (
        'ritual_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNode'
        'EPNS_5QNodeEPNS_12QBackendNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontE'
          'ndNodeEPNS_5QNodeEPNS_12QBackendNodeEb')
    self.uglySide.call(
        ritual, self._addressOf(node), self._addressOf(backend), firstTime,
    )

  def onEngineAboutToShutdown(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html
    """
    #  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
    ritual = (
        'ritual_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdow'
        'nEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToS'
          'hutdownEv')
    self.uglySide.call(ritual)

  @overload(QMetaObject)
  def unregisterBackendType(self, mo: QMetaObject) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAbstractAspectPrivate::unregisterBackendType(const QMetaObject
    &mo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html

    Parameters
    ----------

    mo : QMetaObject
      Passed on as a value: Qt reads the C++ QMetaObject, which stays
      Python's own.
    """
    #  void Qt3DCore::QAbstractAspectPrivate::unregisterBackendType(const
    #      QMetaObject &mo)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QAbstractAspectPrivate21unregisterBackendTypeE'
        'RK11QMetaObject',
        self._valueOf(mo, 'QMetaObject'),
    )

  def q_func(self) -> Optional[Qt3DCore.QAbstractAspect]:
    """
    Calls Qt's 'QAbstractAspect *Qt3DCore::QAbstractAspectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspect *Qt3DCore::QAbstractAspectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore22QAbstractAspectPrivate6q_funcEv',
    )
    return Qt3DCore.QAbstractAspect._cuteAt(address)

  @staticmethod
  def mapperForNode(*__, **_) -> Never:
    """
    Qt's 'QBackendNodeMapperPtr
    Qt3DCore::QAbstractAspectPrivate::mapperForNode(const QMetaObject
    *metaObj) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspectPrivate.mapperForNode' has no cute "
        "function yet. Qt's 'QBackendNodeMapperPtr "
        "Qt3DCore::QAbstractAspectPrivate::mapperForNode(const QMetaObject "
        "*metaObj) const': gives a type Python has no way to take yet.")

  @staticmethod
  def setRootAndCreateNodes(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::QAbstractAspectPrivate::setRootAndCreateNodes(QEntity
    *rootObject, const QList<NodeTreeChange> &nodesTreeChanges)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspectPrivate.setRootAndCreateNodes' has no "
        "cute function yet. Qt's 'void "
        "Qt3DCore::QAbstractAspectPrivate::setRootAndCreateNodes(QEntity "
        "*rootObject, const QList<NodeTreeChange> &nodesTreeChanges)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def syncDirtyEntityComponentNodes(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::QAbstractAspectPrivate::syncDirtyEntityComponentNodes(const
    QList<ComponentRelationshipChange> &nodes)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspectPrivate.syncDirtyEntityComponentNodes' "
        "has no cute function yet. Qt's 'void "
        "Qt3DCore::QAbstractAspectPrivate::syncDirtyEntityComponentNodes(con"
        "st QList<ComponentRelationshipChange> &nodes)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def syncDirtyFrontEndNodes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNodes(const
    QList<QNode *> &nodes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspectPrivate.syncDirtyFrontEndNodes' has no "
        "cute function yet. Qt's 'void "
        "Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNodes(const "
        "QList<QNode *> &nodes)': takes a type Python has no way to hand "
        "over yet.")
