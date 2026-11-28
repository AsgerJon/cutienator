"""
Qt3DRender::QFrontFace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qfrontface.h, Qt 6.12.0. Changes made here are lost.
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


class QFrontFace(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QFrontFace: a plain Python object
  standing in front of one C++ Qt3DRender::QFrontFace.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QFrontFace is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QFrontFace that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'direction',
  'setDirection', 'directionChanged', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QFrontFace::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QFrontFace::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QFrontFace::~QFrontFace()': the destructor: Python
    never removes a C++ Qt3DRender::QFrontFace.
  - Qt's 'const QFrontFacePrivate *Qt3DRender::QFrontFace::d_func() const':
    takes in Python what 'QFrontFacePrivate
    *Qt3DRender::QFrontFace::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QFrontFace is created at the first use, not by
    'Qt3DRender::QFrontFace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QFrontFace.
  - Qt tells when it has removed the C++ Qt3DRender::QFrontFace. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QFrontFace, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class WindingDirection(CuteNum):
    """
    The enum 'Qt3DRender::QFrontFace::WindingDirection' of Qt, with the 2
    names Qt gives in it.
    """

    ClockWise = Kee[int](2304)
    CounterClockWise = Kee[int](2305)

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
    Calls Qt's 'QString Qt3DRender::QFrontFace::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qfrontface.html#tr

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
    #  QString Qt3DRender::QFrontFace::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QFrontFace2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QFrontFace'

  #  A C++ Qt3DRender::QFrontFace Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QFrontFace'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QFrontFace::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfrontface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QFrontFace::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QFrontFace10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def direction(self) -> WindingDirection:
    """
    Calls Qt's 'WindingDirection Qt3DRender::QFrontFace::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfrontface.html#direction

    Returns
    -------

    WindingDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WindingDirection(number)'
      gives.
    """
    #  WindingDirection Qt3DRender::QFrontFace::direction() const
    return QFrontFace.WindingDirection(self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QFrontFace9directionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WindingDirection)
  def setDirection(self, direction: WindingDirection) -> None:
    """
    Calls Qt's 'void Qt3DRender::QFrontFace::setDirection(WindingDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfrontface.html#setDirection

    Parameters
    ----------

    direction : WindingDirection
      Passed on as its number.
    """
    #  void Qt3DRender::QFrontFace::setDirection(WindingDirection direction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFrontFace12setDirectionENS0_16WindingDirec'
        'tionE',
        direction.value,
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
    'Qt3DRender::QFrontFace::QFrontFace(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfrontface.html#QFrontFace

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QFrontFace::QFrontFace(Qt3DCore::QNode *parent)
    self._noteCreation(QFrontFace, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QFrontFaceC1EPN8Qt3DCore5QNodeE',
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

  @overload(WindingDirection)
  def directionChanged(self, direction: WindingDirection) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QFrontFace::directionChanged(WindingDirection direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfrontface.html#directionChanged

    Parameters
    ----------

    direction : WindingDirection
      Passed on as its number.
    """
    #  void Qt3DRender::QFrontFace::directionChanged(WindingDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFrontFace16directionChangedENS0_16WindingD'
        'irectionE',
        direction.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QFrontFacePrivate]:
    """
    Calls Qt's 'QFrontFacePrivate *Qt3DRender::QFrontFace::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qfrontface.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QFrontFacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFrontFacePrivate *Qt3DRender::QFrontFace::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFrontFace6d_funcEv',
    )
    return Qt3DRender.QFrontFacePrivate._cuteAt(address)
