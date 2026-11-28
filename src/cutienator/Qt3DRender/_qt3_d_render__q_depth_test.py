"""
Qt3DRender::QDepthTest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qdepthtest.h, Qt 6.12.0. Changes made here are lost.
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


class QDepthTest(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QDepthTest: a plain Python object
  standing in front of one C++ Qt3DRender::QDepthTest.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QDepthTest is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QDepthTest that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'depthFunction', 'setDepthFunction', 'depthFunctionChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QDepthTest::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QDepthTest::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QDepthTest::~QDepthTest()': the destructor: Python
    never removes a C++ Qt3DRender::QDepthTest.
  - Qt's 'const QDepthTestPrivate *Qt3DRender::QDepthTest::d_func() const':
    takes in Python what 'QDepthTestPrivate
    *Qt3DRender::QDepthTest::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QDepthTest is created at the first use, not by
    'Qt3DRender::QDepthTest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QDepthTest.
  - Qt tells when it has removed the C++ Qt3DRender::QDepthTest. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QDepthTest, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class DepthFunction(CuteNum):
    """
    The enum 'Qt3DRender::QDepthTest::DepthFunction' of Qt, with the 8 names
    Qt gives in it.
    """

    Never = Kee[int](512)
    Always = Kee[int](519)
    Less = Kee[int](513)
    LessOrEqual = Kee[int](515)
    Equal = Kee[int](514)
    GreaterOrEqual = Kee[int](518)
    Greater = Kee[int](516)
    NotEqual = Kee[int](517)

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
    Calls Qt's 'QString Qt3DRender::QDepthTest::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qdepthtest.html#tr

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
    #  QString Qt3DRender::QDepthTest::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QDepthTest2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QDepthTest'

  #  A C++ Qt3DRender::QDepthTest Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QDepthTest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QDepthTest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthtest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QDepthTest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QDepthTest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def depthFunction(self) -> DepthFunction:
    """
    Calls Qt's 'DepthFunction Qt3DRender::QDepthTest::depthFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthtest.html#depthFunction

    Returns
    -------

    DepthFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DepthFunction(number)'
      gives.
    """
    #  DepthFunction Qt3DRender::QDepthTest::depthFunction() const
    return QDepthTest.DepthFunction(self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QDepthTest13depthFunctionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DepthFunction)
  def setDepthFunction(self, depthFunction: DepthFunction) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDepthTest::setDepthFunction(DepthFunction
    depthFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthtest.html#setDepthFunction

    Parameters
    ----------

    depthFunction : DepthFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QDepthTest::setDepthFunction(DepthFunction
    #      depthFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QDepthTest16setDepthFunctionENS0_13DepthFun'
        'ctionE',
        depthFunction.value,
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
    'Qt3DRender::QDepthTest::QDepthTest(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthtest.html#QDepthTest

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QDepthTest::QDepthTest(Qt3DCore::QNode *parent)
    self._noteCreation(QDepthTest, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QDepthTestC1EPN8Qt3DCore5QNodeE',
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

  @overload(DepthFunction)
  def depthFunctionChanged(self, depthFunction: DepthFunction) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QDepthTest::depthFunctionChanged(DepthFunction
    depthFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthtest.html#depthFunctionChanged

    Parameters
    ----------

    depthFunction : DepthFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QDepthTest::depthFunctionChanged(DepthFunction
    #      depthFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QDepthTest20depthFunctionChangedENS0_13Dept'
        'hFunctionE',
        depthFunction.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QDepthTestPrivate]:
    """
    Calls Qt's 'QDepthTestPrivate *Qt3DRender::QDepthTest::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qdepthtest.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QDepthTestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDepthTestPrivate *Qt3DRender::QDepthTest::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QDepthTest6d_funcEv',
    )
    return Qt3DRender.QDepthTestPrivate._cuteAt(address)
