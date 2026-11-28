"""
Qt3DCore::QEntity binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qentity.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

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


class QEntity(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DCore::QEntity: a plain Python object standing in
  front of one C++ Qt3DCore::QEntity.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DCore::QEntity is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QEntity that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'addComponent',
  'removeComponent', 'parentEntity', 'onParentChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QEntity::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Qt3DCore::QEntity::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QEntity::~QEntity()': the destructor: Python never
    removes a C++ Qt3DCore::QEntity.
  - Qt's 'QComponentVector Qt3DCore::QEntity::components() const': gives a
    type Python has no way to take yet.
  - Qt's 'Qt3DCore::QEntity::QEntity(QEntityPrivate &dd, QNode *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QEntityPrivate *Qt3DCore::QEntity::d_func() const': takes in
    Python what 'QEntityPrivate *Qt3DCore::QEntity::d_func()' takes.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ Qt3DCore::QEntity is created at the first use, not by
    'Qt3DCore::QEntity(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QEntity.
  - Qt tells when it has removed the C++ Qt3DCore::QEntity. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QEntity that has no cute function yet,
    'components', 'componentsOfType', holds a function that raises
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
    Calls Qt's 'QString Qt3DCore::QEntity::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qentity.html#tr

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
    #  QString Qt3DCore::QEntity::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore7QEntity2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QEntity'

  #  A C++ Qt3DCore::QEntity Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QEntity'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QEntity::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qentity.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QEntity::metaObject() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore7QEntity10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def parentEntity(self) -> Optional[QEntity]:
    """
    Calls Qt's 'QEntity *Qt3DCore::QEntity::parentEntity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qentity.html#parentEntity

    Returns
    -------

    Optional[QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEntity *Qt3DCore::QEntity::parentEntity() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore7QEntity12parentEntityEv',
    )
    return QEntity._cuteAt(address)

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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QEntity::QEntity(QNode
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qentity.html#QEntity

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QEntity::QEntity(QNode *parent)
    self._noteCreation(QEntity, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore7QEntityC1EPNS_5QNodeE', self._addressOf(parent),
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

  @overload(WAIT['Qt3DCore.QComponent'])
  @overload(NoneType)
  def addComponent(self, comp: Optional[Qt3DCore.QComponent]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QEntity::addComponent(QComponent *comp)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qentity.html#addComponent

    Parameters
    ----------

    comp : Optional[Qt3DCore.QComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QEntity::addComponent(QComponent *comp)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QEntity12addComponentEPNS_10QComponentE',
        self._addressOf(comp),
    )

  @overload(WAIT['Qt3DCore.QComponent'])
  @overload(NoneType)
  def removeComponent(self, comp: Optional[Qt3DCore.QComponent]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QEntity::removeComponent(QComponent *comp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentity.html#removeComponent

    Parameters
    ----------

    comp : Optional[Qt3DCore.QComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QEntity::removeComponent(QComponent *comp)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QEntity15removeComponentEPNS_10QComponentE',
        self._addressOf(comp),
    )

  @overload(QObject)
  @overload(NoneType)
  def onParentChanged(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QEntity::onParentChanged(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentity.html#onParentChanged

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QEntity::onParentChanged(QObject *a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QEntity15onParentChangedEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  def d_func(self) -> Optional[Qt3DCore.QEntityPrivate]:
    """
    Calls Qt's 'QEntityPrivate *Qt3DCore::QEntity::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qentity.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QEntityPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEntityPrivate *Qt3DCore::QEntity::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore7QEntity6d_funcEv')
    return Qt3DCore.QEntityPrivate._cuteAt(address)

  @staticmethod
  def components(*__, **_) -> Never:
    """
    Qt's 'QComponentVector Qt3DCore::QEntity::components() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QEntity.components' has no cute function yet. Qt's "
        "'QComponentVector Qt3DCore::QEntity::components() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def componentsOfType(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QEntity::componentsOfType': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QEntity.componentsOfType' has no cute function yet. Qt's "
        "'Qt3DCore::QEntity::componentsOfType': a template: a pattern and "
        "no single function.")
