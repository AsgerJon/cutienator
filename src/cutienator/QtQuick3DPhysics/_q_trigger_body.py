"""
QTriggerBody binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtriggerbody_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QTriggerBody to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QAbstractPhysicsNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTriggerBody(QAbstractPhysicsNode):
  """
  The cute side of Qt's QTriggerBody: a plain Python object standing in front
  of one C++ QTriggerBody.

  It is built on the cute 'QAbstractPhysicsNode', as Qt's QTriggerBody is
  built on Qt's QAbstractPhysicsNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTriggerBody that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'registerCollision',
  'deregisterCollision', 'collisionCount', 'bodyEntered', 'bodyExited',
  'collisionCountChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTriggerBody::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTriggerBody::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractPhysXNode *QTriggerBody::createPhysXBackend()': gives
    'QAbstractPhysXNode', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QTriggerBody is created at the first use, not by
    'QTriggerBody(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTriggerBody.
  - Qt tells when it has removed the C++ QTriggerBody. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QTriggerBody::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtriggerbody.html#tr

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
    #  QString QTriggerBody::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QTriggerBody2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTriggerBody'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTriggerBody::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtriggerbody.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTriggerBody::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QTriggerBody10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def collisionCount(self) -> int:
    """
    Calls Qt's 'int QTriggerBody::collisionCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtriggerbody.html#collisionCount
    """
    #  int QTriggerBody::collisionCount() const
    return self.uglySide.call('ritual_ZNK12QTriggerBody14collisionCountEv')

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
    Notes what was given, for Qt's 'QTriggerBody::QTriggerBody()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtriggerbody.html#QTriggerBody
    """
    #  QTriggerBody::QTriggerBody()
    self._noteCreation(QTriggerBody, lambda: Rituals.call(
        'ritual_ZN12QTriggerBodyC1Ev',
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

  @overload(QAbstractPhysicsNode)
  @overload(NoneType)
  def registerCollision(
      self,
      collision: Optional[QAbstractPhysicsNode],
  ) -> None:
    """
    Calls Qt's 'void QTriggerBody::registerCollision(QAbstractPhysicsNode
    *collision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtriggerbody.html#registerCollision

    Parameters
    ----------

    collision : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTriggerBody::registerCollision(QAbstractPhysicsNode *collision)
    self.uglySide.call(
        'ritual_ZN12QTriggerBody17registerCollisionEP20QAbstractPhysicsNode',
        self._addressOf(collision),
    )

  @overload(QAbstractPhysicsNode)
  @overload(NoneType)
  def deregisterCollision(
      self,
      collision: Optional[QAbstractPhysicsNode],
  ) -> None:
    """
    Calls Qt's 'void QTriggerBody::deregisterCollision(QAbstractPhysicsNode
    *collision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtriggerbody.html#deregisterCollision

    Parameters
    ----------

    collision : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTriggerBody::deregisterCollision(QAbstractPhysicsNode
    #      *collision)
    self.uglySide.call(
        'ritual_ZN12QTriggerBody19deregisterCollisionEP20QAbstractPhysicsNo'
        'de',
        self._addressOf(collision),
    )

  @overload(QAbstractPhysicsNode)
  @overload(NoneType)
  def bodyEntered(self, body: Optional[QAbstractPhysicsNode]) -> None:
    """
    Calls Qt's 'void QTriggerBody::bodyEntered(QAbstractPhysicsNode *body)'.

    Qt's own words: https://doc.qt.io/qt-6/qtriggerbody.html#bodyEntered

    Parameters
    ----------

    body : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTriggerBody::bodyEntered(QAbstractPhysicsNode *body)
    self.uglySide.call(
        'ritual_ZN12QTriggerBody11bodyEnteredEP20QAbstractPhysicsNode',
        self._addressOf(body),
    )

  @overload(QAbstractPhysicsNode)
  @overload(NoneType)
  def bodyExited(self, body: Optional[QAbstractPhysicsNode]) -> None:
    """
    Calls Qt's 'void QTriggerBody::bodyExited(QAbstractPhysicsNode *body)'.

    Qt's own words: https://doc.qt.io/qt-6/qtriggerbody.html#bodyExited

    Parameters
    ----------

    body : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTriggerBody::bodyExited(QAbstractPhysicsNode *body)
    self.uglySide.call(
        'ritual_ZN12QTriggerBody10bodyExitedEP20QAbstractPhysicsNode',
        self._addressOf(body),
    )

  def collisionCountChanged(self) -> None:
    """
    Calls Qt's 'void QTriggerBody::collisionCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtriggerbody.html#collisionCountChanged
    """
    #  void QTriggerBody::collisionCountChanged()
    self.uglySide.call('ritual_ZN12QTriggerBody21collisionCountChangedEv')
