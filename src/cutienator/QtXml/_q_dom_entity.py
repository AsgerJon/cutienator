"""
QDomEntity binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDomNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomEntityPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomEntityPrivate = WAIT['QDomEntityPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomEntity(QDomNode):
  """
  The cute side of Qt's QDomEntity: a plain Python object standing in front
  of one C++ QDomEntity.

  It is built on the cute 'QDomNode', as Qt's QDomEntity is built on Qt's
  QDomNode, and has everything that class has.

  C++ hands a QDomEntity around as a copy, so every C++ QDomEntity behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomEntity that has a ritual and that Python can
  call so far, 4 names in all: 'publicId', 'systemId', 'notationName',
  'nodeType'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomEntity &QDomEntity::operator=(const QDomEntity &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDomEntity::~QDomEntity()': the destructor: Python removes its C++
    QDomEntity by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomEntity is created at the first use, not by 'QDomEntity(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomEntity back gives a copy the ritual made for
    Python, in a new cute QDomEntity.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomEntity'

  #  Qt's '~QDomEntity()'. Naming it makes this a value class: Python owns
  #  every C++ QDomEntity behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QDomEntityD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def publicId(self) -> str:
    """
    Calls Qt's 'QString QDomEntity::publicId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomentity.html#publicId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomEntity::publicId() const
    return self.uglySide.call('ritual_ZNK10QDomEntity8publicIdEv')

  def systemId(self) -> str:
    """
    Calls Qt's 'QString QDomEntity::systemId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomentity.html#systemId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomEntity::systemId() const
    return self.uglySide.call('ritual_ZNK10QDomEntity8systemIdEv')

  def notationName(self) -> str:
    """
    Calls Qt's 'QString QDomEntity::notationName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomentity.html#notationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomEntity::notationName() const
    return self.uglySide.call('ritual_ZNK10QDomEntity12notationNameEv')

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomEntity::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomentity.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomEntity::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK10QDomEntity8nodeTypeEv',
    ))

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
    Notes what was given, for Qt's 'QDomEntity::QDomEntity()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomentity.html#QDomEntity
    """
    #  QDomEntity::QDomEntity()
    self._noteCreation(QDomEntity, lambda: Rituals.call(
        'ritual_ZN10QDomEntityC1Ev',
    ))

  @overload(THIS)
  def __init__(self, entity: QDomEntity) -> None:
    """
    Notes what was given, for Qt's 'QDomEntity::QDomEntity(const QDomEntity
    &entity)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomentity.html#QDomEntity

    Parameters
    ----------

    entity : QDomEntity
      Passed on as a value: Qt reads the C++ QDomEntity, which stays Python's
      own.
    """
    #  QDomEntity::QDomEntity(const QDomEntity &entity)
    self._noteCreation(QDomEntity, lambda: Rituals.call(
        'ritual_ZN10QDomEntityC1ERKS_', self._valueOf(entity),
    ))

  @overload(QDomEntityPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomEntityPrivate]) -> None:
    """
    Notes what was given, for Qt's 'QDomEntity::QDomEntity(QDomEntityPrivate
    *a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomentity.html#QDomEntity

    Parameters
    ----------

    a0 : Optional[QDomEntityPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomEntity::QDomEntity(QDomEntityPrivate *a0)
    self._noteCreation(QDomEntity, lambda: Rituals.call(
        'ritual_ZN10QDomEntityC1EP17QDomEntityPrivate', self._addressOf(a0),
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
