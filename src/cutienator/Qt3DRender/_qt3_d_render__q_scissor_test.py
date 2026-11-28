"""
Qt3DRender::QScissorTest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qscissortest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScissorTest(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QScissorTest: a plain Python object
  standing in front of one C++ Qt3DRender::QScissorTest.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QScissorTest is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QScissorTest that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'left',
  'bottom', 'width', 'height', 'setLeft', 'setBottom', 'setWidth',
  'setHeight', 'leftChanged', 'bottomChanged', 'widthChanged',
  'heightChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QScissorTest::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QScissorTest::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QScissorTest::~QScissorTest()': the destructor: Python
    never removes a C++ Qt3DRender::QScissorTest.
  - Qt's 'const QScissorTestPrivate *Qt3DRender::QScissorTest::d_func()
    const': takes in Python what 'QScissorTestPrivate
    *Qt3DRender::QScissorTest::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QScissorTest is created at the first use, not by
    'Qt3DRender::QScissorTest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QScissorTest.
  - Qt tells when it has removed the C++ Qt3DRender::QScissorTest. Every call
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
    Calls Qt's 'QString Qt3DRender::QScissorTest::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qscissortest.html#tr

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
    #  QString Qt3DRender::QScissorTest::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender12QScissorTest2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QScissorTest'

  #  A C++ Qt3DRender::QScissorTest Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QScissorTest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QScissorTest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QScissorTest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QScissorTest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def left(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QScissorTest::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qscissortest.html#left
    """
    #  int Qt3DRender::QScissorTest::left() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender12QScissorTest4leftEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QScissorTest::bottom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#bottom
    """
    #  int Qt3DRender::QScissorTest::bottom() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QScissorTest6bottomEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QScissorTest::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qscissortest.html#width
    """
    #  int Qt3DRender::QScissorTest::width() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender12QScissorTest5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QScissorTest::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#height
    """
    #  int Qt3DRender::QScissorTest::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QScissorTest6heightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLeft(self, left: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::setLeft(int left)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#setLeft

    Parameters
    ----------

    left : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::setLeft(int left)
    self.uglySide.call('ritual_ZN10Qt3DRender12QScissorTest7setLeftEi', left)

  @overload(int)
  def setBottom(self, bottom: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::setBottom(int bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#setBottom

    Parameters
    ----------

    bottom : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::setBottom(int bottom)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest9setBottomEi', bottom,
    )

  @overload(int)
  def setWidth(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::setWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#setWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::setWidth(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest8setWidthEi', width,
    )

  @overload(int)
  def setHeight(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::setHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#setHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::setHeight(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest9setHeightEi', height,
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
    'Qt3DRender::QScissorTest::QScissorTest(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#QScissorTest

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QScissorTest::QScissorTest(Qt3DCore::QNode *parent)
    self._noteCreation(QScissorTest, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender12QScissorTestC1EPN8Qt3DCore5QNodeE',
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

  @overload(int)
  def leftChanged(self, left: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::leftChanged(int left)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#leftChanged

    Parameters
    ----------

    left : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::leftChanged(int left)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest11leftChangedEi', left,
    )

  @overload(int)
  def bottomChanged(self, bottom: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::bottomChanged(int bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#bottomChanged

    Parameters
    ----------

    bottom : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::bottomChanged(int bottom)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest13bottomChangedEi', bottom,
    )

  @overload(int)
  def widthChanged(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::widthChanged(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#widthChanged

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::widthChanged(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest12widthChangedEi', width,
    )

  @overload(int)
  def heightChanged(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScissorTest::heightChanged(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#heightChanged

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DRender::QScissorTest::heightChanged(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest13heightChangedEi', height,
    )

  def d_func(self) -> Optional[Qt3DRender.QScissorTestPrivate]:
    """
    Calls Qt's 'QScissorTestPrivate *Qt3DRender::QScissorTest::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscissortest.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QScissorTestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScissorTestPrivate *Qt3DRender::QScissorTest::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender12QScissorTest6d_funcEv',
    )
    return Qt3DRender.QScissorTestPrivate._cuteAt(address)
