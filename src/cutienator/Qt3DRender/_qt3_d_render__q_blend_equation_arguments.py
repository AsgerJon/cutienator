"""
Qt3DRender::QBlendEquationArguments binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qblendequationarguments.h, Qt 6.12.0. Changes made here are
#  lost.
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


class QBlendEquationArguments(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QBlendEquationArguments: a plain Python
  object standing in front of one C++ Qt3DRender::QBlendEquationArguments.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QBlendEquationArguments is built on Qt's
  Qt3DRender::QRenderState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QBlendEquationArguments that has a
  ritual and that Python can call so far, 22 names in all: 'metaObject',
  'tr', 'sourceRgb', 'destinationRgb', 'sourceAlpha', 'destinationAlpha',
  'bufferIndex', 'setSourceRgb', 'setDestinationRgb', 'setSourceAlpha',
  'setDestinationAlpha', 'setSourceRgba', 'setDestinationRgba',
  'setBufferIndex', 'sourceRgbChanged', 'sourceAlphaChanged',
  'destinationRgbChanged', 'destinationAlphaChanged', 'sourceRgbaChanged',
  'destinationRgbaChanged', 'bufferIndexChanged', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QBlendEquationArguments::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::QBlendEquationArguments::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QBlendEquationArguments::~QBlendEquationArguments()':
    the destructor: Python never removes a C++
    Qt3DRender::QBlendEquationArguments.
  - Qt's 'Qt3DRender::QBlendEquationArguments::QBlendEquationArguments(
    QBlendEquationArgumentsPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QBlendEquationArgumentsPrivate
    *Qt3DRender::QBlendEquationArguments::d_func() const': takes in Python
    what 'QBlendEquationArgumentsPrivate
    *Qt3DRender::QBlendEquationArguments::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QBlendEquationArguments is created at the first use,
    not by 'Qt3DRender::QBlendEquationArguments(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QBlendEquationArguments.
  - Qt tells when it has removed the C++ Qt3DRender::QBlendEquationArguments.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QBlendEquationArguments, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Blending(CuteNum):
    """
    The enum 'Qt3DRender::QBlendEquationArguments::Blending' of Qt, with the
    20 names Qt gives in it.
    """

    Zero = Kee[int](0)
    One = Kee[int](1)
    SourceColor = Kee[int](768)
    SourceAlpha = Kee[int](770)
    Source1Alpha = Kee[int](771)
    Source1Color = Kee[int](772)
    DestinationColor = Kee[int](774)
    DestinationAlpha = Kee[int](772)
    SourceAlphaSaturate = Kee[int](776)
    ConstantColor = Kee[int](32769)
    ConstantAlpha = Kee[int](32771)
    OneMinusSourceColor = Kee[int](769)
    OneMinusSourceAlpha = Kee[int](771)
    OneMinusDestinationAlpha = Kee[int](773)
    OneMinusDestinationColor = Kee[int](775)
    OneMinusConstantColor = Kee[int](32770)
    OneMinusConstantAlpha = Kee[int](32772)
    OneMinusSource1Alpha = Kee[int](32773)
    OneMinusSource1Color = Kee[int](32774)
    OneMinusSource1Color0 = Kee[int](32774)

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
    Calls Qt's 'QString Qt3DRender::QBlendEquationArguments::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html#tr

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
    #  QString Qt3DRender::QBlendEquationArguments::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QBlendEquationArguments'

  #  A C++ Qt3DRender::QBlendEquationArguments Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QBlendEquationArguments'

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
    *Qt3DRender::QBlendEquationArguments::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QBlendEquationArguments::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QBlendEquationArguments10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceRgb(self) -> Blending:
    """
    Calls Qt's 'Blending Qt3DRender::QBlendEquationArguments::sourceRgb()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html#sourceRgb

    Returns
    -------

    Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Blending(number)' gives.
    """
    #  Blending Qt3DRender::QBlendEquationArguments::sourceRgb() const
    return QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QBlendEquationArguments9sourceRgbEv',
    ))

  def destinationRgb(self) -> Blending:
    """
    Calls Qt's 'Blending
    Qt3DRender::QBlendEquationArguments::destinationRgb() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Returns
    -------

    Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Blending(number)' gives.
    """
    #  Blending Qt3DRender::QBlendEquationArguments::destinationRgb() const
    return QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QBlendEquationArguments14destinationRgbEv',
    ))

  def sourceAlpha(self) -> Blending:
    """
    Calls Qt's 'Blending Qt3DRender::QBlendEquationArguments::sourceAlpha()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Returns
    -------

    Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Blending(number)' gives.
    """
    #  Blending Qt3DRender::QBlendEquationArguments::sourceAlpha() const
    return QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QBlendEquationArguments11sourceAlphaEv',
    ))

  def destinationAlpha(self) -> Blending:
    """
    Calls Qt's 'Blending
    Qt3DRender::QBlendEquationArguments::destinationAlpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Returns
    -------

    Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Blending(number)' gives.
    """
    #  Blending Qt3DRender::QBlendEquationArguments::destinationAlpha() const
    return QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QBlendEquationArguments16destinationAlphaE'
        'v',
    ))

  def bufferIndex(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QBlendEquationArguments::bufferIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html
    """
    #  int Qt3DRender::QBlendEquationArguments::bufferIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QBlendEquationArguments11bufferIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Blending)
  def setSourceRgb(self, sourceRgb: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::setSourceRgb(Blending sourceRgb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    sourceRgb : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::setSourceRgb(Blending
    #      sourceRgb)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments12setSourceRgbENS0_8'
        'BlendingE',
        sourceRgb.value,
    )

  @overload(Blending)
  def setDestinationRgb(self, destinationRgb: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::setDestinationRgb(Blending
    destinationRgb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    destinationRgb : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::setDestinationRgb(Blending
    #      destinationRgb)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments17setDestinationRgbE'
        'NS0_8BlendingE',
        destinationRgb.value,
    )

  @overload(Blending)
  def setSourceAlpha(self, sourceAlpha: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::setSourceAlpha(Blending
    sourceAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    sourceAlpha : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::setSourceAlpha(Blending
    #      sourceAlpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments14setSourceAlphaENS0'
        '_8BlendingE',
        sourceAlpha.value,
    )

  @overload(Blending)
  def setDestinationAlpha(self, destinationAlpha: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::setDestinationAlpha(Blending
    destinationAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    destinationAlpha : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::setDestinationAlpha(Blending
    #      destinationAlpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments19setDestinationAlph'
        'aENS0_8BlendingE',
        destinationAlpha.value,
    )

  @overload(Blending)
  def setSourceRgba(self, sourceRgba: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::setSourceRgba(Blending sourceRgba)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    sourceRgba : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::setSourceRgba(Blending
    #      sourceRgba)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments13setSourceRgbaENS0_'
        '8BlendingE',
        sourceRgba.value,
    )

  @overload(Blending)
  def setDestinationRgba(self, destinationRgba: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::setDestinationRgba(Blending
    destinationRgba)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    destinationRgba : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::setDestinationRgba(Blending
    #      destinationRgba)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments18setDestinationRgba'
        'ENS0_8BlendingE',
        destinationRgba.value,
    )

  @overload(int)
  def setBufferIndex(self, index: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlendEquationArguments::setBufferIndex(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DRender::QBlendEquationArguments::setBufferIndex(int index)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments14setBufferIndexEi',
        index,
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
    'Qt3DRender::QBlendEquationArguments::QBlendEquationArguments(Qt3DCore::
    QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QBlendEquationArguments::QBlendEquationArguments(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QBlendEquationArguments, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArgumentsC1EPN8Qt3DCore5QNode'
        'E',
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

  @overload(Blending)
  def sourceRgbChanged(self, sourceRgb: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::sourceRgbChanged(Blending
    sourceRgb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    sourceRgb : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::sourceRgbChanged(Blending
    #      sourceRgb)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments16sourceRgbChangedEN'
        'S0_8BlendingE',
        sourceRgb.value,
    )

  @overload(Blending)
  def sourceAlphaChanged(self, sourceAlpha: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::sourceAlphaChanged(Blending
    sourceAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    sourceAlpha : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::sourceAlphaChanged(Blending
    #      sourceAlpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments18sourceAlphaChanged'
        'ENS0_8BlendingE',
        sourceAlpha.value,
    )

  @overload(Blending)
  def destinationRgbChanged(self, destinationRgb: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::destinationRgbChanged(Blending
    destinationRgb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    destinationRgb : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::destinationRgbChanged(
    #      Blending destinationRgb)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments21destinationRgbChan'
        'gedENS0_8BlendingE',
        destinationRgb.value,
    )

  @overload(Blending)
  def destinationAlphaChanged(self, destinationAlpha: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::destinationAlphaChanged(Blending
    destinationAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    destinationAlpha : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::destinationAlphaChanged(
    #      Blending destinationAlpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments23destinationAlphaCh'
        'angedENS0_8BlendingE',
        destinationAlpha.value,
    )

  @overload(Blending)
  def sourceRgbaChanged(self, sourceRgba: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::sourceRgbaChanged(Blending
    sourceRgba)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    sourceRgba : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::sourceRgbaChanged(Blending
    #      sourceRgba)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments17sourceRgbaChangedE'
        'NS0_8BlendingE',
        sourceRgba.value,
    )

  @overload(Blending)
  def destinationRgbaChanged(self, destinationRgba: Blending) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::destinationRgbaChanged(Blending
    destinationRgba)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    destinationRgba : Blending
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquationArguments::destinationRgbaChanged(
    #      Blending destinationRgba)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments22destinationRgbaCha'
        'ngedENS0_8BlendingE',
        destinationRgba.value,
    )

  @overload(int)
  def bufferIndexChanged(self, index: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquationArguments::bufferIndexChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DRender::QBlendEquationArguments::bufferIndexChanged(int
    #      index)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments18bufferIndexChanged'
        'Ei',
        index,
    )

  def d_func(self) -> Optional[Qt3DRender.QBlendEquationArgumentsPrivate]:
    """
    Calls Qt's 'QBlendEquationArgumentsPrivate
    *Qt3DRender::QBlendEquationArguments::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationarguments.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QBlendEquationArgumentsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlendEquationArgumentsPrivate
    #      *Qt3DRender::QBlendEquationArguments::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender23QBlendEquationArguments6d_funcEv',
    )
    return Qt3DRender.QBlendEquationArgumentsPrivate._cuteAt(address)
