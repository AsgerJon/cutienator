"""
Qt3DRender::QPaintedTextureImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qpaintedtextureimage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from ..QtGui import QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPaintedTextureImage(Qt3DRender.QAbstractTextureImage):
  """
  The cute side of Qt's Qt3DRender::QPaintedTextureImage: a plain Python
  object standing in front of one C++ Qt3DRender::QPaintedTextureImage.

  It is built on the cute 'Qt3DRender::QAbstractTextureImage', as Qt's
  Qt3DRender::QPaintedTextureImage is built on Qt's
  Qt3DRender::QAbstractTextureImage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPaintedTextureImage that has a ritual
  and that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'width', 'height', 'size', 'update', 'setWidth', 'setHeight', 'setSize',
  'widthChanged', 'heightChanged', 'sizeChanged', 'paint', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QPaintedTextureImage::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QPaintedTextureImage::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QPaintedTextureImage::~QPaintedTextureImage()': the
    destructor: Python never removes a C++ Qt3DRender::QPaintedTextureImage.
  - Qt's 'const QPaintedTextureImagePrivate
    *Qt3DRender::QPaintedTextureImage::d_func() const': takes in Python what
    'QPaintedTextureImagePrivate *Qt3DRender::QPaintedTextureImage::d_func()'
    takes.
  - Qt's 'QTextureImageDataGeneratorPtr
    Qt3DRender::QPaintedTextureImage::dataGenerator() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QPaintedTextureImage is created at the first use, not
    by 'Qt3DRender::QPaintedTextureImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QPaintedTextureImage.
  - Qt tells when it has removed the C++ Qt3DRender::QPaintedTextureImage.
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
    Calls Qt's 'QString Qt3DRender::QPaintedTextureImage::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#tr

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
    #  QString Qt3DRender::QPaintedTextureImage::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPaintedTextureImage'

  #  A C++ Qt3DRender::QPaintedTextureImage Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QPaintedTextureImage'

  #  The functions Qt calls itself that Qt3DRender::QPaintedTextureImage is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'paint': (
          ('_ZN10Qt3DRender20QPaintedTextureImage5paintEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
  }

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
    *Qt3DRender::QPaintedTextureImage::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QPaintedTextureImage::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender20QPaintedTextureImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QPaintedTextureImage::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#width
    """
    #  int Qt3DRender::QPaintedTextureImage::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender20QPaintedTextureImage5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QPaintedTextureImage::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#height
    """
    #  int Qt3DRender::QPaintedTextureImage::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender20QPaintedTextureImage6heightEv',
    )

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DRender::QPaintedTextureImage::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DRender::QPaintedTextureImage::size() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender20QPaintedTextureImage4sizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setWidth(self, w: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::setWidth(int w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#setWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void Qt3DRender::QPaintedTextureImage::setWidth(int w)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage8setWidthEi', w,
    )

  @overload(int)
  def setHeight(self, h: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::setHeight(int h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#setHeight

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void Qt3DRender::QPaintedTextureImage::setHeight(int h)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage9setHeightEi', h,
    )

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::setSize(QSize size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DRender::QPaintedTextureImage::setSize(QSize size)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage7setSizeE5QSize',
        self._valueOf(size),
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
    'Qt3DRender::QPaintedTextureImage::QPaintedTextureImage(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QPaintedTextureImage::QPaintedTextureImage(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QPaintedTextureImage, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImageC1EPN8Qt3DCore5QNodeE',
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

  @overload()
  @overload(QRect)
  def update(self, rect: Optional[QRect] = None) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::update(const QRect
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#update

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void Qt3DRender::QPaintedTextureImage::update(const QRect &rect)
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage6updateERK5QRect',
        self._valueOf(rect),
    )

  @overload(int)
  def widthChanged(self, w: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::widthChanged(int w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#widthChanged

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void Qt3DRender::QPaintedTextureImage::widthChanged(int w)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage12widthChangedEi', w,
    )

  @overload(int)
  def heightChanged(self, w: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::heightChanged(int w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#heightChanged

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void Qt3DRender::QPaintedTextureImage::heightChanged(int w)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage13heightChangedEi', w,
    )

  @overload(QSize)
  def sizeChanged(self, size: QSize) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::sizeChanged(QSize
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#sizeChanged

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DRender::QPaintedTextureImage::sizeChanged(QSize size)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage11sizeChangedE5QSize',
        self._valueOf(size),
    )

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPaintedTextureImage::paint(QPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QPaintedTextureImage::paint(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage5paintEP8QPainter',
        self._addressOf(painter),
    )

  def d_func(self) -> Optional[Qt3DRender.QPaintedTextureImagePrivate]:
    """
    Calls Qt's 'QPaintedTextureImagePrivate
    *Qt3DRender::QPaintedTextureImage::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimage.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QPaintedTextureImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintedTextureImagePrivate
    #      *Qt3DRender::QPaintedTextureImage::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender20QPaintedTextureImage6d_funcEv',
    )
    return Qt3DRender.QPaintedTextureImagePrivate._cuteAt(address)
