"""
Qt3DAnimation::QLerpClipBlend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qlerpclipblend.h, Qt 6.12.0. Changes made here are lost.
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


class QLerpClipBlend(Qt3DAnimation.QAbstractClipBlendNode):
  """
  The cute side of Qt's Qt3DAnimation::QLerpClipBlend: a plain Python object
  standing in front of one C++ Qt3DAnimation::QLerpClipBlend.

  It is built on the cute 'Qt3DAnimation::QAbstractClipBlendNode', as Qt's
  Qt3DAnimation::QLerpClipBlend is built on Qt's
  Qt3DAnimation::QAbstractClipBlendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QLerpClipBlend that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'blendFactor', 'startClip', 'endClip', 'setBlendFactor', 'setStartClip',
  'setEndClip', 'blendFactorChanged', 'startClipChanged', 'endClipChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QLerpClipBlend::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DAnimation::QLerpClipBlend::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QLerpClipBlend::~QLerpClipBlend()': the destructor:
    Python never removes a C++ Qt3DAnimation::QLerpClipBlend.
  - Qt's 'Qt3DAnimation::QLerpClipBlend::QLerpClipBlend(QLerpClipBlendPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QLerpClipBlendPrivate
    *Qt3DAnimation::QLerpClipBlend::d_func() const': takes in Python what
    'QLerpClipBlendPrivate *Qt3DAnimation::QLerpClipBlend::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QLerpClipBlend is created at the first use, not by
    'Qt3DAnimation::QLerpClipBlend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QLerpClipBlend.
  - Qt tells when it has removed the C++ Qt3DAnimation::QLerpClipBlend. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DAnimation::QLerpClipBlend::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#tr

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
    #  QString Qt3DAnimation::QLerpClipBlend::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QLerpClipBlend'

  #  A C++ Qt3DAnimation::QLerpClipBlend Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QLerpClipBlend'

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
    *Qt3DAnimation::QLerpClipBlend::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QLerpClipBlend::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation14QLerpClipBlend10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def blendFactor(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QLerpClipBlend::blendFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#blendFactor
    """
    #  float Qt3DAnimation::QLerpClipBlend::blendFactor() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation14QLerpClipBlend11blendFactorEv',
    )

  def startClip(self) -> Optional[Qt3DAnimation.QAbstractClipBlendNode]:
    """
    Calls Qt's 'Qt3DAnimation::QAbstractClipBlendNode
    *Qt3DAnimation::QLerpClipBlend::startClip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#startClip

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractClipBlendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DAnimation::QAbstractClipBlendNode
    #      *Qt3DAnimation::QLerpClipBlend::startClip() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation14QLerpClipBlend9startClipEv',
    )
    return Qt3DAnimation.QAbstractClipBlendNode._cuteAt(address)

  def endClip(self) -> Optional[Qt3DAnimation.QAbstractClipBlendNode]:
    """
    Calls Qt's 'Qt3DAnimation::QAbstractClipBlendNode
    *Qt3DAnimation::QLerpClipBlend::endClip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#endClip

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractClipBlendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DAnimation::QAbstractClipBlendNode
    #      *Qt3DAnimation::QLerpClipBlend::endClip() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation14QLerpClipBlend7endClipEv',
    )
    return Qt3DAnimation.QAbstractClipBlendNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBlendFactor(self, blendFactor: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QLerpClipBlend::setBlendFactor(float
    blendFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#setBlendFactor

    Parameters
    ----------

    blendFactor : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QLerpClipBlend::setBlendFactor(float blendFactor)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend14setBlendFactorEf',
        blendFactor,
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def setStartClip(
      self,
      startClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QLerpClipBlend::setStartClip(Qt3DAnimation::
    QAbstractClipBlendNode *startClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#setStartClip

    Parameters
    ----------

    startClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QLerpClipBlend::setStartClip(Qt3DAnimation::
    #      QAbstractClipBlendNode *startClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend12setStartClipEPNS_22QAbst'
        'ractClipBlendNodeE',
        self._addressOf(startClip),
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def setEndClip(
      self,
      endClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QLerpClipBlend::setEndClip(Qt3DAnimation::
    QAbstractClipBlendNode *endClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#setEndClip

    Parameters
    ----------

    endClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QLerpClipBlend::setEndClip(Qt3DAnimation::
    #      QAbstractClipBlendNode *endClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend10setEndClipEPNS_22QAbstra'
        'ctClipBlendNodeE',
        self._addressOf(endClip),
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
    'Qt3DAnimation::QLerpClipBlend::QLerpClipBlend(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#QLerpClipBlend

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QLerpClipBlend::QLerpClipBlend(Qt3DCore::QNode *parent)
    self._noteCreation(QLerpClipBlend, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlendC1EPN8Qt3DCore5QNodeE',
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
  def blendFactorChanged(self, blendFactor: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QLerpClipBlend::blendFactorChanged(float
    blendFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html

    Parameters
    ----------

    blendFactor : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QLerpClipBlend::blendFactorChanged(float
    #      blendFactor)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend18blendFactorChangedEf',
        blendFactor,
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def startClipChanged(
      self,
      startClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QLerpClipBlend::startClipChanged(Qt3DAnimation::
    QAbstractClipBlendNode *startClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#startClipChanged

    Parameters
    ----------

    startClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QLerpClipBlend::startClipChanged(Qt3DAnimation::
    #      QAbstractClipBlendNode *startClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend16startClipChangedEPNS_22Q'
        'AbstractClipBlendNodeE',
        self._addressOf(startClip),
    )

  @overload(Qt3DAnimation.QAbstractClipBlendNode)
  @overload(NoneType)
  def endClipChanged(
      self,
      endClip: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QLerpClipBlend::endClipChanged(Qt3DAnimation::
    QAbstractClipBlendNode *endClip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#endClipChanged

    Parameters
    ----------

    endClip : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QLerpClipBlend::endClipChanged(Qt3DAnimation::
    #      QAbstractClipBlendNode *endClip)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend14endClipChangedEPNS_22QAb'
        'stractClipBlendNodeE',
        self._addressOf(endClip),
    )

  def d_func(self) -> Optional[Qt3DAnimation.QLerpClipBlendPrivate]:
    """
    Calls Qt's 'QLerpClipBlendPrivate
    *Qt3DAnimation::QLerpClipBlend::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qlerpclipblend.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QLerpClipBlendPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLerpClipBlendPrivate *Qt3DAnimation::QLerpClipBlend::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QLerpClipBlend6d_funcEv',
    )
    return Qt3DAnimation.QLerpClipBlendPrivate._cuteAt(address)
