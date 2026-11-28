"""
Qt3DAnimation::QAdditiveClipBlend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qadditiveclipblend.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAdditiveClipBlend(Qt3DAnimation.QAbstractClipBlendNode):
  """
  The cute side of Qt's Qt3DAnimation::QAdditiveClipBlend: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAdditiveClipBlend.

  It is built on the cute 'Qt3DAnimation::QAbstractClipBlendNode', as Qt's
  Qt3DAnimation::QAdditiveClipBlend is built on Qt's
  Qt3DAnimation::QAbstractClipBlendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAdditiveClipBlend that has a ritual
  and that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'additiveFactor', 'baseClip', 'additiveClip', 'setAdditiveFactor',
  'setBaseClip', 'setAdditiveClip', 'additiveFactorChanged',
  'baseClipChanged', 'additiveClipChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAdditiveClipBlend::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QAdditiveClipBlend::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QAdditiveClipBlend::~QAdditiveClipBlend()': the
    destructor: Python never removes a C++ Qt3DAnimation::QAdditiveClipBlend.
  - Qt's 'Qt3DAnimation::QAdditiveClipBlend::QAdditiveClipBlend(
    QAdditiveClipBlendPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QAdditiveClipBlendPrivate
    *Qt3DAnimation::QAdditiveClipBlend::d_func() const': takes in Python what
    'QAdditiveClipBlendPrivate *Qt3DAnimation::QAdditiveClipBlend::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAdditiveClipBlend is created at the first use,
    not by 'Qt3DAnimation::QAdditiveClipBlend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAdditiveClipBlend.
  - Qt tells when it has removed the C++ Qt3DAnimation::QAdditiveClipBlend.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DAnimation::QAdditiveClipBlend::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html#tr

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
    #  QString Qt3DAnimation::QAdditiveClipBlend::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAdditiveClipBlend'

  #  A C++ Qt3DAnimation::QAdditiveClipBlend Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAdditiveClipBlend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DAnimation::QAdditiveClipBlend::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QAdditiveClipBlend::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def additiveFactor(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAdditiveClipBlend::additiveFactor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html
    """
    #  float Qt3DAnimation::QAdditiveClipBlend::additiveFactor() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend14additiveFactorEv',
    )

  def baseClip(self) -> Optional[Qt3DAnimation.QAbstractClipBlendNode]:
    """
    Calls Qt's 'Qt3DAnimation::QAbstractClipBlendNode
    *Qt3DAnimation::QAdditiveClipBlend::baseClip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html#baseClip

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractClipBlendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DAnimation::QAbstractClipBlendNode
    #      *Qt3DAnimation::QAdditiveClipBlend::baseClip() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend8baseClipEv',
    )
    return Qt3DAnimation.QAbstractClipBlendNode._cuteAt(address)

  def additiveClip(self) -> Optional[Qt3DAnimation.QAbstractClipBlendNode]:
    """
    Calls Qt's 'Qt3DAnimation::QAbstractClipBlendNode
    *Qt3DAnimation::QAdditiveClipBlend::additiveClip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html#additiveClip

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractClipBlendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DAnimation::QAbstractClipBlendNode
    #      *Qt3DAnimation::QAdditiveClipBlend::additiveClip() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend12additiveClipEv',
    )
    return Qt3DAnimation.QAbstractClipBlendNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setAdditiveFactor(self, additiveFactor: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAdditiveClipBlend::setAdditiveFactor(float
    additiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html

    Parameters
    ----------

    additiveFactor : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAdditiveClipBlend::setAdditiveFactor(float
    #      additiveFactor)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend17setAdditiveFactorEf',
        additiveFactor,
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def setBaseClip(
      self,
      baseClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAdditiveClipBlend::setBaseClip(Qt3DAnimation::
    QAbstractClipBlendNode *baseClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html#setBaseClip

    Parameters
    ----------

    baseClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAdditiveClipBlend::setBaseClip(Qt3DAnimation::
    #      QAbstractClipBlendNode *baseClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend11setBaseClipEPNS_22QA'
        'bstractClipBlendNodeE',
        self._addressOf(baseClip),
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def setAdditiveClip(
      self,
      additiveClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAdditiveClipBlend::setAdditiveClip(Qt3DAnimation::
    QAbstractClipBlendNode *additiveClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html

    Parameters
    ----------

    additiveClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAdditiveClipBlend::setAdditiveClip(
    #      Qt3DAnimation::QAbstractClipBlendNode *additiveClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend15setAdditiveClipEPNS_'
        '22QAbstractClipBlendNodeE',
        self._addressOf(additiveClip),
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
    Notes what was given, for Qt's
    'Qt3DAnimation::QAdditiveClipBlend::QAdditiveClipBlend(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QAdditiveClipBlend::QAdditiveClipBlend(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QAdditiveClipBlend, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlendC1EPN8Qt3DCore5QNodeE',
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
  def additiveFactorChanged(self, additiveFactor: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAdditiveClipBlend::additiveFactorChanged(float
    additiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html

    Parameters
    ----------

    additiveFactor : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAdditiveClipBlend::additiveFactorChanged(float
    #      additiveFactor)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend21additiveFactorChange'
        'dEf',
        additiveFactor,
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def baseClipChanged(
      self,
      baseClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAdditiveClipBlend::baseClipChanged(Qt3DAnimation::
    QAbstractClipBlendNode *baseClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html

    Parameters
    ----------

    baseClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAdditiveClipBlend::baseClipChanged(
    #      Qt3DAnimation::QAbstractClipBlendNode *baseClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend15baseClipChangedEPNS_'
        '22QAbstractClipBlendNodeE',
        self._addressOf(baseClip),
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def additiveClipChanged(
      self,
      additiveClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAdditiveClipBlend::additiveClipChanged(Qt3DAnimation::
    QAbstractClipBlendNode *additiveClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html

    Parameters
    ----------

    additiveClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAdditiveClipBlend::additiveClipChanged(
    #      Qt3DAnimation::QAbstractClipBlendNode *additiveClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend19additiveClipChangedE'
        'PNS_22QAbstractClipBlendNodeE',
        self._addressOf(additiveClip),
    )

  def d_func(self) -> Optional[Qt3DAnimation.QAdditiveClipBlendPrivate]:
    """
    Calls Qt's 'QAdditiveClipBlendPrivate
    *Qt3DAnimation::QAdditiveClipBlend::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qadditiveclipblend.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAdditiveClipBlendPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAdditiveClipBlendPrivate *Qt3DAnimation::QAdditiveClipBlend::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAdditiveClipBlend6d_funcEv',
    )
    return Qt3DAnimation.QAdditiveClipBlendPrivate._cuteAt(address)
