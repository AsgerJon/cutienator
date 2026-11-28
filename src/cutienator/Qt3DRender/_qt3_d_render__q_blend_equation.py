"""
Qt3DRender::QBlendEquation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qblendequation.h, Qt 6.12.0. Changes made here are lost.
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


class QBlendEquation(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QBlendEquation: a plain Python object
  standing in front of one C++ Qt3DRender::QBlendEquation.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QBlendEquation is built on Qt's Qt3DRender::QRenderState, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QBlendEquation that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'blendFunction', 'setBlendFunction', 'blendFunctionChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QBlendEquation::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QBlendEquation::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QBlendEquation::~QBlendEquation()': the destructor:
    Python never removes a C++ Qt3DRender::QBlendEquation.
  - Qt's 'const QBlendEquationPrivate *Qt3DRender::QBlendEquation::d_func()
    const': takes in Python what 'QBlendEquationPrivate
    *Qt3DRender::QBlendEquation::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QBlendEquation is created at the first use, not by
    'Qt3DRender::QBlendEquation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QBlendEquation.
  - Qt tells when it has removed the C++ Qt3DRender::QBlendEquation. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QBlendEquation, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class BlendFunction(CuteNum):
    """
    The enum 'Qt3DRender::QBlendEquation::BlendFunction' of Qt, with the 5
    names Qt gives in it.
    """

    Add = Kee[int](32774)
    Subtract = Kee[int](32778)
    ReverseSubtract = Kee[int](32779)
    Min = Kee[int](32775)
    Max = Kee[int](32776)

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
    Calls Qt's 'QString Qt3DRender::QBlendEquation::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qblendequation.html#tr

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
    #  QString Qt3DRender::QBlendEquation::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QBlendEquation2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QBlendEquation'

  #  A C++ Qt3DRender::QBlendEquation Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QBlendEquation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QBlendEquation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QBlendEquation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QBlendEquation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def blendFunction(self) -> BlendFunction:
    """
    Calls Qt's 'BlendFunction Qt3DRender::QBlendEquation::blendFunction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequation.html#blendFunction

    Returns
    -------

    BlendFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendFunction(number)'
      gives.
    """
    #  BlendFunction Qt3DRender::QBlendEquation::blendFunction() const
    return QBlendEquation.BlendFunction(self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QBlendEquation13blendFunctionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BlendFunction)
  def setBlendFunction(self, blendFunction: BlendFunction) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquation::setBlendFunction(BlendFunction
    blendFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequation.html#setBlendFunction

    Parameters
    ----------

    blendFunction : BlendFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquation::setBlendFunction(BlendFunction
    #      blendFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QBlendEquation16setBlendFunctionENS0_13Blen'
        'dFunctionE',
        blendFunction.value,
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
    'Qt3DRender::QBlendEquation::QBlendEquation(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequation.html#QBlendEquation

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QBlendEquation::QBlendEquation(Qt3DCore::QNode *parent)
    self._noteCreation(QBlendEquation, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QBlendEquationC1EPN8Qt3DCore5QNodeE',
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

  @overload(BlendFunction)
  def blendFunctionChanged(self, blendFunction: BlendFunction) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlendEquation::blendFunctionChanged(BlendFunction
    blendFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequation.html

    Parameters
    ----------

    blendFunction : BlendFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QBlendEquation::blendFunctionChanged(BlendFunction
    #      blendFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QBlendEquation20blendFunctionChangedENS0_13'
        'BlendFunctionE',
        blendFunction.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QBlendEquationPrivate]:
    """
    Calls Qt's 'QBlendEquationPrivate *Qt3DRender::QBlendEquation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequation.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QBlendEquationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlendEquationPrivate *Qt3DRender::QBlendEquation::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QBlendEquation6d_funcEv',
    )
    return Qt3DRender.QBlendEquationPrivate._cuteAt(address)
