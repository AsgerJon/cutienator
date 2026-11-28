"""
Qt3DRender::QSubtreeEnabler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qsubtreeenabler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSubtreeEnabler(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QSubtreeEnabler: a plain Python object
  standing in front of one C++ Qt3DRender::QSubtreeEnabler.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QSubtreeEnabler is built on Qt's Qt3DRender::QFrameGraphNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSubtreeEnabler that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'enablement', 'setEnablement', 'requestUpdate', 'enablementChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QSubtreeEnabler::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QSubtreeEnabler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QSubtreeEnabler::~QSubtreeEnabler()': the destructor:
    Python never removes a C++ Qt3DRender::QSubtreeEnabler.
  - Qt's 'const QSubtreeEnablerPrivate *Qt3DRender::QSubtreeEnabler::d_func()
    const': takes in Python what 'QSubtreeEnablerPrivate
    *Qt3DRender::QSubtreeEnabler::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QSubtreeEnabler is created at the first use, not by
    'Qt3DRender::QSubtreeEnabler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSubtreeEnabler.
  - Qt tells when it has removed the C++ Qt3DRender::QSubtreeEnabler. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QSubtreeEnabler, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Enablement(CuteNum):
    """
    The enum 'Qt3DRender::QSubtreeEnabler::Enablement' of Qt, with the 2
    names Qt gives in it.
    """

    Persistent = Kee[int](0)
    SingleShot = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QSubtreeEnabler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#tr

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
    #  QString Qt3DRender::QSubtreeEnabler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender15QSubtreeEnabler2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSubtreeEnabler'

  #  A C++ Qt3DRender::QSubtreeEnabler Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSubtreeEnabler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QSubtreeEnabler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QSubtreeEnabler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QSubtreeEnabler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enablement(self) -> Enablement:
    """
    Calls Qt's 'Enablement Qt3DRender::QSubtreeEnabler::enablement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#enablement

    Returns
    -------

    Enablement
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Enablement(number)'
      gives.
    """
    #  Enablement Qt3DRender::QSubtreeEnabler::enablement() const
    return QSubtreeEnabler.Enablement(self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QSubtreeEnabler10enablementEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Enablement)
  def setEnablement(self, enablement: Enablement) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSubtreeEnabler::setEnablement(Enablement
    enablement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#setEnablement

    Parameters
    ----------

    enablement : Enablement
      Passed on as its number.
    """
    #  void Qt3DRender::QSubtreeEnabler::setEnablement(Enablement enablement)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QSubtreeEnabler13setEnablementENS0_10Enable'
        'mentE',
        enablement.value,
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
    'Qt3DRender::QSubtreeEnabler::QSubtreeEnabler(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#QSubtreeEnabler

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QSubtreeEnabler::QSubtreeEnabler(Qt3DCore::QNode *parent)
    self._noteCreation(QSubtreeEnabler, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender15QSubtreeEnablerC1EPN8Qt3DCore5QNodeE',
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

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSubtreeEnabler::requestUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#requestUpdate
    """
    #  void Qt3DRender::QSubtreeEnabler::requestUpdate()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QSubtreeEnabler13requestUpdateEv',
    )

  @overload(Enablement)
  def enablementChanged(self, enablement: Enablement) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QSubtreeEnabler::enablementChanged(Qt3DRender::
    QSubtreeEnabler::Enablement enablement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#enablementChanged

    Parameters
    ----------

    enablement : Enablement
      Passed on as its number.
    """
    #  void Qt3DRender::QSubtreeEnabler::enablementChanged(Qt3DRender::
    #      QSubtreeEnabler::Enablement enablement)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QSubtreeEnabler17enablementChangedENS0_10En'
        'ablementE',
        enablement.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QSubtreeEnablerPrivate]:
    """
    Calls Qt's 'QSubtreeEnablerPrivate
    *Qt3DRender::QSubtreeEnabler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsubtreeenabler.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QSubtreeEnablerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSubtreeEnablerPrivate *Qt3DRender::QSubtreeEnabler::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender15QSubtreeEnabler6d_funcEv',
    )
    return Qt3DRender.QSubtreeEnablerPrivate._cuteAt(address)
