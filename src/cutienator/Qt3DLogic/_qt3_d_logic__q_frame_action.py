"""
Qt3DLogic::QFrameAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DLogic/qframeaction.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DLogic

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFrameAction(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DLogic::QFrameAction: a plain Python object
  standing in front of one C++ Qt3DLogic::QFrameAction.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DLogic::QFrameAction is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DLogic::QFrameAction that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'triggered',
  'd_func', 'onTriggered'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DLogic::QFrameAction::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DLogic::QFrameAction::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DLogic::QFrameAction::~QFrameAction()': the destructor: Python
    never removes a C++ Qt3DLogic::QFrameAction.
  - Qt's 'Qt3DLogic::QFrameAction::QFrameAction(QFrameActionPrivate &dd,
    QNode *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QFrameActionPrivate *Qt3DLogic::QFrameAction::d_func()
    const': takes in Python what 'QFrameActionPrivate
    *Qt3DLogic::QFrameAction::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DLogic::QFrameAction is created at the first use, not by
    'Qt3DLogic::QFrameAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DLogic::QFrameAction.
  - Qt tells when it has removed the C++ Qt3DLogic::QFrameAction. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DLogic::QFrameAction::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dlogic-qframeaction.html#tr

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
    #  QString Qt3DLogic::QFrameAction::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DLogic12QFrameAction2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DLogic::QFrameAction'

  #  A C++ Qt3DLogic::QFrameAction Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DLogic_QFrameAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DLogic::QFrameAction::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-qframeaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DLogic::QFrameAction::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DLogic12QFrameAction10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's
    'Qt3DLogic::QFrameAction::QFrameAction(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-qframeaction.html#QFrameAction

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DLogic::QFrameAction::QFrameAction(Qt3DCore::QNode *parent)
    self._noteCreation(QFrameAction, lambda: Rituals.call(
        'ritual_ZN9Qt3DLogic12QFrameActionC1EPN8Qt3DCore5QNodeE',
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

  @overload(float)
  def triggered(self, dt: float) -> None:
    """
    Calls Qt's 'void Qt3DLogic::QFrameAction::triggered(float dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-qframeaction.html#triggered

    Parameters
    ----------

    dt : float
      Passed on as it is.
    """
    #  void Qt3DLogic::QFrameAction::triggered(float dt)
    self.uglySide.call('ritual_ZN9Qt3DLogic12QFrameAction9triggeredEf', dt)

  def d_func(self) -> Optional[Qt3DLogic.QFrameActionPrivate]:
    """
    Calls Qt's 'QFrameActionPrivate *Qt3DLogic::QFrameAction::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dlogic-qframeaction.html#d_func

    Returns
    -------

    Optional[Qt3DLogic.QFrameActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFrameActionPrivate *Qt3DLogic::QFrameAction::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DLogic12QFrameAction6d_funcEv',
    )
    return Qt3DLogic.QFrameActionPrivate._cuteAt(address)

  @overload(float)
  def onTriggered(self, dt: float) -> None:
    """
    Calls Qt's 'void Qt3DLogic::QFrameAction::onTriggered(float dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-qframeaction.html#onTriggered

    Parameters
    ----------

    dt : float
      Passed on as it is.
    """
    #  void Qt3DLogic::QFrameAction::onTriggered(float dt)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic12QFrameAction11onTriggeredEf', dt,
    )
