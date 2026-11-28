"""
Qt3DCore::QComponent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qcomponent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComponent(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DCore::QComponent: a plain Python object standing
  in front of one C++ Qt3DCore::QComponent.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DCore::QComponent is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QComponent that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'isShareable',
  'setShareable', 'shareableChanged', 'addedToEntity', 'removedFromEntity',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QComponent::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QComponent::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QComponent::~QComponent()': the destructor: Python never
    removes a C++ Qt3DCore::QComponent.
  - Qt's 'QList<QEntity *> Qt3DCore::QComponent::entities() const': gives a
    type Python has no way to take yet.
  - Qt's 'Qt3DCore::QComponent::QComponent(QComponentPrivate &dd, QNode
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QComponentPrivate *Qt3DCore::QComponent::d_func() const':
    takes in Python what 'QComponentPrivate *Qt3DCore::QComponent::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QComponent is created at the first use, not by
    'Qt3DCore::QComponent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QComponent.
  - Qt tells when it has removed the C++ Qt3DCore::QComponent. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QComponent that has no cute function yet,
    'entities', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString Qt3DCore::QComponent::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#tr

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
    #  QString Qt3DCore::QComponent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QComponent2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QComponent'

  #  A C++ Qt3DCore::QComponent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QComponent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QComponent::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QComponent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QComponent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isShareable(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QComponent::isShareable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#isShareable
    """
    #  bool Qt3DCore::QComponent::isShareable() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QComponent11isShareableEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setShareable(self, isShareable: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QComponent::setShareable(bool isShareable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#setShareable

    Parameters
    ----------

    isShareable : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QComponent::setShareable(bool isShareable)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QComponent12setShareableEb', isShareable,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QComponent::QComponent(QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#QComponent

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QComponent::QComponent(QNode *parent)
    self._noteCreation(QComponent, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore10QComponentC1EPNS_5QNodeE',
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

  @overload(bool)
  def shareableChanged(self, isShareable: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QComponent::shareableChanged(bool
    isShareable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#shareableChanged

    Parameters
    ----------

    isShareable : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QComponent::shareableChanged(bool isShareable)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QComponent16shareableChangedEb', isShareable,
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def addedToEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QComponent::addedToEntity(QEntity *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#addedToEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QComponent::addedToEntity(QEntity *entity)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QComponent13addedToEntityEPNS_7QEntityE',
        self._addressOf(entity),
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def removedFromEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QComponent::removedFromEntity(QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#removedFromEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QComponent::removedFromEntity(QEntity *entity)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QComponent17removedFromEntityEPNS_7QEntityE',
        self._addressOf(entity),
    )

  def d_func(self) -> Optional[Qt3DCore.QComponentPrivate]:
    """
    Calls Qt's 'QComponentPrivate *Qt3DCore::QComponent::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qcomponent.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QComponentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QComponentPrivate *Qt3DCore::QComponent::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore10QComponent6d_funcEv')
    return Qt3DCore.QComponentPrivate._cuteAt(address)

  @staticmethod
  def entities(*__, **_) -> Never:
    """
    Qt's 'QList<QEntity *> Qt3DCore::QComponent::entities() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QComponent.entities' has no cute function yet. Qt's "
        "'QList<QEntity *> Qt3DCore::QComponent::entities() const': gives a "
        "type Python has no way to take yet.")
