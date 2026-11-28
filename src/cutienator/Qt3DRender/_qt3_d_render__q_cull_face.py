"""
Qt3DRender::QCullFace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qcullface.h, Qt 6.12.0. Changes made here are lost.
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


class QCullFace(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QCullFace: a plain Python object standing
  in front of one C++ Qt3DRender::QCullFace.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QCullFace is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QCullFace that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'mode',
  'setMode', 'modeChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QCullFace::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QCullFace::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QCullFace::~QCullFace()': the destructor: Python never
    removes a C++ Qt3DRender::QCullFace.
  - Qt's 'const QCullFacePrivate *Qt3DRender::QCullFace::d_func() const':
    takes in Python what 'QCullFacePrivate *Qt3DRender::QCullFace::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QCullFace is created at the first use, not by
    'Qt3DRender::QCullFace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QCullFace.
  - Qt tells when it has removed the C++ Qt3DRender::QCullFace. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QCullFace, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class CullingMode(CuteNum):
    """
    The enum 'Qt3DRender::QCullFace::CullingMode' of Qt, with the 4 names Qt
    gives in it.
    """

    NoCulling = Kee[int](0)
    Front = Kee[int](1028)
    Back = Kee[int](1029)
    FrontAndBack = Kee[int](1032)

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
    Calls Qt's 'QString Qt3DRender::QCullFace::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcullface.html#tr

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
    #  QString Qt3DRender::QCullFace::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender9QCullFace2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QCullFace'

  #  A C++ Qt3DRender::QCullFace Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QCullFace'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QCullFace::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcullface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QCullFace::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender9QCullFace10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mode(self) -> CullingMode:
    """
    Calls Qt's 'CullingMode Qt3DRender::QCullFace::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcullface.html#mode

    Returns
    -------

    CullingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CullingMode(number)'
      gives.
    """
    #  CullingMode Qt3DRender::QCullFace::mode() const
    return QCullFace.CullingMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender9QCullFace4modeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(CullingMode)
  def setMode(self, mode: CullingMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCullFace::setMode(CullingMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcullface.html#setMode

    Parameters
    ----------

    mode : CullingMode
      Passed on as its number.
    """
    #  void Qt3DRender::QCullFace::setMode(CullingMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QCullFace7setModeENS0_11CullingModeE',
        mode.value,
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
    'Qt3DRender::QCullFace::QCullFace(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcullface.html#QCullFace

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QCullFace::QCullFace(Qt3DCore::QNode *parent)
    self._noteCreation(QCullFace, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender9QCullFaceC1EPN8Qt3DCore5QNodeE',
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

  @overload(CullingMode)
  def modeChanged(self, mode: CullingMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCullFace::modeChanged(CullingMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcullface.html#modeChanged

    Parameters
    ----------

    mode : CullingMode
      Passed on as its number.
    """
    #  void Qt3DRender::QCullFace::modeChanged(CullingMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QCullFace11modeChangedENS0_11CullingModeE',
        mode.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QCullFacePrivate]:
    """
    Calls Qt's 'QCullFacePrivate *Qt3DRender::QCullFace::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcullface.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QCullFacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCullFacePrivate *Qt3DRender::QCullFace::d_func()
    address = self.uglySide.call('ritual_ZN10Qt3DRender9QCullFace6d_funcEv')
    return Qt3DRender.QCullFacePrivate._cuteAt(address)
