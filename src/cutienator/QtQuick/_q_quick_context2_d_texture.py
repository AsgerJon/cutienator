"""
QQuickContext2DTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickContext2DTexture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QEvent, QObject
from . import QQuickCanvasItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QRectF, QSize
  from ..QtGui import QPaintDevice, QVector2D
  from . import QQuickContext2DCommandBuffer, QQuickContext2DTile
  from . import QQuickWindow, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQuickContext2DCommandBuffer = WAIT['QQuickContext2DCommandBuffer']
  QQuickContext2DTile = WAIT['QQuickContext2DTile']
  QQuickWindow = WAIT['QQuickWindow']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSGTexture = WAIT['QSGTexture']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContext2DTexture(QObject):
  """
  The cute side of Qt's QQuickContext2DTexture: a plain Python object
  standing in front of one C++ QQuickContext2DTexture.

  It is built on the cute 'QObject', as Qt's QQuickContext2DTexture is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickContext2DTexture that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'renderTarget',
  'tiledRect', 'setCanvasSize', 'setTileSize', 'setSmooth',
  'setAntialiasing', 'setDirtyRect', 'canvasDestroyed', 'setOnCustomThread',
  'isOnCustomThread', 'textureForNextFrame', 'event', 'textureChanged',
  'canvasChanged', 'paint', 'markDirtyTexture', 'setItem', 'grabImage',
  'scaleFactor', 'beginPainting', 'endPainting', 'createTile',
  'compositeTile', 'clearTiles', 'adjustedTileSize', 'createTiles'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickContext2DTexture::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickContext2DTexture::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickContext2DTexture::~QQuickContext2DTexture()': the destructor:
    Python never removes a C++ QQuickContext2DTexture.

  What has no ritual
  ------------------

  6 of the 36 functions Qt declares: 3 leans on 'QQuickContext2DTexture; 2
  not a gap; 1 Qt's library has no name for it, and its code in Qt's source
  does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickContext2DTexture is created at the first use, not by
    'QQuickContext2DTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContext2DTexture.
  - Qt tells when it has removed the C++ QQuickContext2DTexture. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickContext2DTexture that has no cute function yet,
    '__init__', 'paintWithoutTiles', 'setCanvasWindow', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuickContext2DTexture, each a class in
  #  here as in C++.

  class CanvasChangeEvent(QEvent):
    """
    The cute side of Qt's QQuickContext2DTexture::CanvasChangeEvent: a plain
    Python object standing in front of one C++
    QQuickContext2DTexture::CanvasChangeEvent.

    It is built on the cute 'QEvent', as Qt's
    QQuickContext2DTexture::CanvasChangeEvent is built on Qt's QEvent, and
    has everything that class has.

    C++ hands a QQuickContext2DTexture::CanvasChangeEvent around as a copy,
    so every C++ QQuickContext2DTexture::CanvasChangeEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickContext2DTexture::CanvasChangeEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickContext2DTexture::CanvasChangeEvent::~CanvasChangeEvent()':
      the destructor: Python removes its C++
      QQuickContext2DTexture::CanvasChangeEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuickContext2DTexture::CanvasChangeEvent is created at the
      first use, not by 'QQuickContext2DTexture::CanvasChangeEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickContext2DTexture::CanvasChangeEvent back
      gives a copy the ritual made for Python, in a new cute
      QQuickContext2DTexture::CanvasChangeEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRect = WAIT['QRect']
      QSize = WAIT['QSize']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickContext2DTexture::CanvasChangeEvent'

    #  A C++ QQuickContext2DTexture::CanvasChangeEvent Python makes is of a
    #  C++ class of ours, in which Python can take functions over. This
    #  ritual hands one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQuickContext2DTexture_CanvasChangeEvent'

    #  Qt's '~QQuickContext2DTexture::CanvasChangeEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQuickContext2DTexture::CanvasChangeEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QQuickContext2DTexture17CanvasChangeEventD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QSize, QSize, QRect, QRect, bool, bool)
    def __init__(
        self,
        cSize: QSize,
        tSize: QSize,
        cWindow: QRect,
        dRect: QRect,
        sm: bool,
        aa: bool,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QQuickContext2DTexture::CanvasChangeEvent::CanvasChangeEvent(const
      QSize &cSize, const QSize &tSize, const QRect &cWindow, const QRect
      &dRect, bool sm, bool aa)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickcontext2dtexture-canvaschangeevent.html

      Parameters
      ----------

      cSize : QSize
        Passed on as a value: Qt reads the C++ QSize, which stays Python's
        own.

      tSize : QSize
        Passed on as a value: Qt reads the C++ QSize, which stays Python's
        own.

      cWindow : QRect
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own.

      dRect : QRect
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own.

      sm : bool
        Passed on as it is.

      aa : bool
        Passed on as it is.
      """
      #  QQuickContext2DTexture::CanvasChangeEvent::CanvasChangeEvent(const
      #      QSize &cSize, const QSize &tSize, const QRect &cWindow, const
      #      QRect &dRect, bool sm, bool aa)
      self._noteCreation(
          QQuickContext2DTexture.CanvasChangeEvent, lambda: Rituals.call(
              'ritual_ZN22QQuickContext2DTexture17CanvasChangeEventC1ERK5QS'
              'izeS3_RK5QRectS6_bb',
              self._valueOf(cSize), self._valueOf(tSize),
              self._valueOf(cWindow), self._valueOf(dRect), sm, aa,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class PaintEvent(QEvent):
    """
    The cute side of Qt's QQuickContext2DTexture::PaintEvent: a plain Python
    object standing in front of one C++ QQuickContext2DTexture::PaintEvent.

    It is built on the cute 'QEvent', as Qt's
    QQuickContext2DTexture::PaintEvent is built on Qt's QEvent, and has
    everything that class has.

    C++ hands a QQuickContext2DTexture::PaintEvent around as a copy, so every
    C++ QQuickContext2DTexture::PaintEvent behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickContext2DTexture::PaintEvent yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickContext2DTexture::PaintEvent::~PaintEvent()': the
      destructor: Python removes its C++ QQuickContext2DTexture::PaintEvent
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickContext2DTexture::PaintEvent is created at the first use,
      not by 'QQuickContext2DTexture::PaintEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickContext2DTexture::PaintEvent back gives a
      copy the ritual made for Python, in a new cute
      QQuickContext2DTexture::PaintEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQuickContext2DCommandBuffer = WAIT['QQuickContext2DCommandBuffer']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickContext2DTexture::PaintEvent'

    #  A C++ QQuickContext2DTexture::PaintEvent Python makes is of a C++
    #  class of ours, in which Python can take functions over. This ritual
    #  hands one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQuickContext2DTexture_PaintEvent'

    #  Qt's '~QQuickContext2DTexture::PaintEvent()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickContext2DTexture::PaintEvent
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickContext2DTexture10PaintEventD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QQuickContext2DCommandBuffer)
    @overload(NoneType)
    def __init__(self, b: Optional[QQuickContext2DCommandBuffer]) -> None:
      """
      Notes what was given, for Qt's
      'QQuickContext2DTexture::PaintEvent::PaintEvent(
      QQuickContext2DCommandBuffer *b)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickcontext2dtexture-paintevent.html

      Parameters
      ----------

      b : Optional[QQuickContext2DCommandBuffer]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQuickContext2DTexture::PaintEvent::PaintEvent(
      #      QQuickContext2DCommandBuffer *b)
      self._noteCreation(
          QQuickContext2DTexture.PaintEvent, lambda: Rituals.call(
              'ritual_ZN22QQuickContext2DTexture10PaintEventC1EP28QQuickCon'
              'text2DCommandBuffer',
              self._addressOf(b),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRectF, QSize)
  def tiledRect(window: QRectF, tileSize: QSize) -> QRect:
    """
    Calls Qt's 'QRect QQuickContext2DTexture::tiledRect(const QRectF &window,
    const QSize &tileSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#tiledRect

    Parameters
    ----------

    window : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    tileSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickContext2DTexture::tiledRect(const QRectF &window, const
    #      QSize &tileSize)
    address = Rituals.call(
        'ritual_ZN22QQuickContext2DTexture9tiledRectERK6QRectFRK5QSize',
        CuteMixin._valueOf(window), CuteMixin._valueOf(tileSize),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContext2DTexture'

  #  A C++ QQuickContext2DTexture Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContext2DTexture'

  #  The functions Qt calls itself that QQuickContext2DTexture is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'renderTarget': (
          ('_ZNK22QQuickContext2DTexture12renderTargetEv',
           ('int', 'enum', 'QtQuick:QQuickCanvasItem.RenderTarget'),
           ()),
      ),
      'textureForNextFrame': (
          ('_ZN22QQuickContext2DTexture19textureForNextFrameEP10QSGTextureP'
           '12QQuickWindow',
           ('address', 'address', 'QtQuick:QSGTexture'),
           (
               ('address', 'address', 'QtQuick:QSGTexture'),
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'grabImage': (
          ('_ZN22QQuickContext2DTexture9grabImageERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'scaleFactor': (
          ('_ZNK22QQuickContext2DTexture11scaleFactorEv',
           ('address', 'value', 'QtGui:QVector2D'),
           ()),
      ),
      'beginPainting': (
          ('_ZN22QQuickContext2DTexture13beginPaintingEv',
           ('address', 'address', 'QtGui:QPaintDevice'),
           ()),
      ),
      'endPainting': (
          ('_ZN22QQuickContext2DTexture11endPaintingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createTile': (
          ('_ZNK22QQuickContext2DTexture10createTileEv',
           ('address', 'address', 'QtQuick:QQuickContext2DTile'),
           ()),
      ),
      'compositeTile': (
          ('_ZN22QQuickContext2DTexture13compositeTileEP19QQuickContext2DTi'
           'le',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickContext2DTile'),
           )),
      ),
      'adjustedTileSize': (
          ('_ZN22QQuickContext2DTexture16adjustedTileSizeERK5QSize',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('address', 'value', 'QtCore:QSize'),
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
    Calls Qt's 'const QMetaObject *QQuickContext2DTexture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickContext2DTexture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickContext2DTexture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderTarget(self) -> QQuickCanvasItem.RenderTarget:
    """
    Calls Qt's 'QQuickCanvasItem::RenderTarget
    QQuickContext2DTexture::renderTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#renderTarget

    Returns
    -------

    QQuickCanvasItem.RenderTarget
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickCanvasItem.RenderTarget(number)' gives.
    """
    #  QQuickCanvasItem::RenderTarget QQuickContext2DTexture::renderTarget()
    #      const
    return QQuickCanvasItem.RenderTarget(self.uglySide.call(
        'ritual_ZNK22QQuickContext2DTexture12renderTargetEv',
    ))

  def isOnCustomThread(self) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DTexture::isOnCustomThread() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#isOnCustomThread
    """
    #  bool QQuickContext2DTexture::isOnCustomThread() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickContext2DTexture16isOnCustomThreadEv',
    )

  def scaleFactor(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickContext2DTexture::scaleFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#scaleFactor

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickContext2DTexture::scaleFactor() const
    ritual = 'ritual_ZNK22QQuickContext2DTexture11scaleFactorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickContext2DTexture11scaleFactorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def createTile(self) -> Optional[QQuickContext2DTile]:
    """
    Calls Qt's 'QQuickContext2DTile *QQuickContext2DTexture::createTile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#createTile

    Returns
    -------

    Optional[QQuickContext2DTile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContext2DTile *QQuickContext2DTexture::createTile() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickContext2DTexture10createTileEv',
    )
    from . import QQuickContext2DTile
    return QQuickContext2DTile._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setCanvasSize(self, size: QSize) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DTexture::setCanvasSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#setCanvasSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool QQuickContext2DTexture::setCanvasSize(const QSize &size)
    return self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture13setCanvasSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QSize)
  def setTileSize(self, size: QSize) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DTexture::setTileSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#setTileSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool QQuickContext2DTexture::setTileSize(const QSize &size)
    return self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture11setTileSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(bool)
  def setSmooth(self, smooth: bool) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::setSmooth(bool smooth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#setSmooth

    Parameters
    ----------

    smooth : bool
      Passed on as it is.
    """
    #  void QQuickContext2DTexture::setSmooth(bool smooth)
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture9setSmoothEb', smooth,
    )

  @overload(bool)
  def setAntialiasing(self, antialiasing: bool) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::setAntialiasing(bool
    antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#setAntialiasing

    Parameters
    ----------

    antialiasing : bool
      Passed on as it is.
    """
    #  void QQuickContext2DTexture::setAntialiasing(bool antialiasing)
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture15setAntialiasingEb', antialiasing,
    )

  @overload(QRect)
  def setDirtyRect(self, dirtyRect: QRect) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DTexture::setDirtyRect(const QRect
    &dirtyRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#setDirtyRect

    Parameters
    ----------

    dirtyRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QQuickContext2DTexture::setDirtyRect(const QRect &dirtyRect)
    return self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture12setDirtyRectERK5QRect',
        self._valueOf(dirtyRect),
    )

  @overload(bool)
  def setOnCustomThread(self, is_: bool) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::setOnCustomThread(bool is)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#setOnCustomThread

    Parameters
    ----------

    is_ : bool
      Passed on as it is.
    """
    #  void QQuickContext2DTexture::setOnCustomThread(bool is)
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture17setOnCustomThreadEb', is_,
    )

  @overload(QQuickCanvasItem)
  @overload(NoneType)
  def setItem(self, item: Optional[QQuickCanvasItem]) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::setItem(QQuickCanvasItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#setItem

    Parameters
    ----------

    item : Optional[QQuickCanvasItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContext2DTexture::setItem(QQuickCanvasItem *item)
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture7setItemEP16QQuickCanvasItem',
        self._addressOf(item),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickContext2DTexture::QQuickContext2DTexture()': leans on
    'QQuickContext2DTexture::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickContext2DTexture.__init__' has no cute function yet. Qt's "
        "'QQuickContext2DTexture::QQuickContext2DTexture()': leans on "
        "'QQuickContext2DTexture::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def canvasDestroyed(self) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DTexture::canvasDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#canvasDestroyed
    """
    #  bool QQuickContext2DTexture::canvasDestroyed()
    return self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture15canvasDestroyedEv',
    )

  @overload(QSGTexture, QQuickWindow)
  @overload(QSGTexture, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def textureForNextFrame(
      self,
      lastFrame: Optional[QSGTexture],
      window: Optional[QQuickWindow],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QQuickContext2DTexture::textureForNextFrame(QSGTexture *lastFrame,
    QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#textureForNextFrame

    Parameters
    ----------

    lastFrame : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QQuickContext2DTexture::textureForNextFrame(QSGTexture
    #      *lastFrame, QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture19textureForNextFrameEP10QSGTextu'
        'reP12QQuickWindow',
        self._addressOf(lastFrame), self._addressOf(window),
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DTexture::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2dtexture.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickContext2DTexture::event(QEvent *e)
    return self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture5eventEP6QEvent',
        self._addressOf(e),
    )

  def textureChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::textureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#textureChanged
    """
    #  void QQuickContext2DTexture::textureChanged()
    self.uglySide.call('ritual_ZN22QQuickContext2DTexture14textureChangedEv')

  @overload(QSize, QSize, QRect, QRect, bool, bool)
  def canvasChanged(
      self,
      canvasSize: QSize,
      tileSize: QSize,
      canvasWindow: QRect,
      dirtyRect: QRect,
      smooth: bool,
      antialiasing: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::canvasChanged(const QSize
    &canvasSize, const QSize &tileSize, const QRect &canvasWindow, const
    QRect &dirtyRect, bool smooth, bool antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#canvasChanged

    Parameters
    ----------

    canvasSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    tileSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    canvasWindow : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    dirtyRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    smooth : bool
      Passed on as it is.

    antialiasing : bool
      Passed on as it is.
    """
    #  void QQuickContext2DTexture::canvasChanged(const QSize &canvasSize,
    #      const QSize &tileSize, const QRect &canvasWindow, const QRect
    #      &dirtyRect, bool smooth, bool antialiasing)
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture13canvasChangedERK5QSizeS2_RK5QRe'
        'ctS5_bb',
        self._valueOf(canvasSize), self._valueOf(tileSize),
        self._valueOf(canvasWindow), self._valueOf(dirtyRect), smooth,
        antialiasing,
    )

  @overload(QQuickContext2DCommandBuffer)
  @overload(NoneType)
  def paint(self, ccb: Optional[QQuickContext2DCommandBuffer]) -> None:
    """
    Calls Qt's 'void
    QQuickContext2DTexture::paint(QQuickContext2DCommandBuffer *ccb)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2dtexture.html#paint

    Parameters
    ----------

    ccb : Optional[QQuickContext2DCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContext2DTexture::paint(QQuickContext2DCommandBuffer *ccb)
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture5paintEP28QQuickContext2DCommandB'
        'uffer',
        self._addressOf(ccb),
    )

  def markDirtyTexture(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::markDirtyTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#markDirtyTexture
    """
    #  void QQuickContext2DTexture::markDirtyTexture()
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture16markDirtyTextureEv',
    )

  @overload()
  @overload(QRectF)
  def grabImage(self, region: Optional[QRectF] = None) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::grabImage(const QRectF
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#grabImage

    Parameters
    ----------

    region : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickContext2DTexture::grabImage(const QRectF &region)
    if region is None:
      from ..QtCore import QRectF
      region = QRectF()
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture9grabImageERK6QRectF',
        self._valueOf(region),
    )

  def beginPainting(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QQuickContext2DTexture::beginPainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#beginPainting

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QQuickContext2DTexture::beginPainting()
    ritual = 'ritual_ZN22QQuickContext2DTexture13beginPaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickContext2DTexture13beginPaintingEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPaintDevice
    return QPaintDevice._cuteAt(address)

  def endPainting(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::endPainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#endPainting
    """
    #  void QQuickContext2DTexture::endPainting()
    ritual = 'ritual_ZN22QQuickContext2DTexture11endPaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickContext2DTexture11endPaintingEv'
    self.uglySide.call(ritual)

  @overload(QQuickContext2DTile)
  @overload(NoneType)
  def compositeTile(self, tile: Optional[QQuickContext2DTile]) -> None:
    """
    Calls Qt's 'void
    QQuickContext2DTexture::compositeTile(QQuickContext2DTile *tile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#compositeTile

    Parameters
    ----------

    tile : Optional[QQuickContext2DTile]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContext2DTexture::compositeTile(QQuickContext2DTile *tile)
    self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture13compositeTileEP19QQuickContext2'
        'DTile',
        self._addressOf(tile),
    )

  def clearTiles(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DTexture::clearTiles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#clearTiles
    """
    #  void QQuickContext2DTexture::clearTiles()
    self.uglySide.call('ritual_ZN22QQuickContext2DTexture10clearTilesEv')

  @overload(QSize)
  def adjustedTileSize(self, ts: QSize) -> QSize:
    """
    Calls Qt's 'QSize QQuickContext2DTexture::adjustedTileSize(const QSize
    &ts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#adjustedTileSize

    Parameters
    ----------

    ts : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickContext2DTexture::adjustedTileSize(const QSize &ts)
    ritual = 'ritual_ZN22QQuickContext2DTexture16adjustedTileSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickContext2DTexture16adjustedTileSizeERK5QSize')
    address = self.uglySide.call(ritual, self._valueOf(ts))
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRect)
  def createTiles(self, window: QRect) -> QRect:
    """
    Calls Qt's 'QRect QQuickContext2DTexture::createTiles(const QRect
    &window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtexture.html#createTiles

    Parameters
    ----------

    window : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickContext2DTexture::createTiles(const QRect &window)
    address = self.uglySide.call(
        'ritual_ZN22QQuickContext2DTexture11createTilesERK5QRect',
        self._valueOf(window),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  def paintWithoutTiles(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickContext2DTexture::paintWithoutTiles(QQuickContext2DCommandBuffer
    *ccb)': leans on 'QQuickContext2DTexture::textureChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickContext2DTexture.paintWithoutTiles' has no cute function "
        "yet. Qt's 'void "
        "QQuickContext2DTexture::paintWithoutTiles(QQuickContext2DCommandBuf"
        "fer *ccb)': leans on 'QQuickContext2DTexture::textureChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setCanvasWindow(*__, **_) -> Never:
    """
    Qt's 'bool QQuickContext2DTexture::setCanvasWindow(const QRect
    &canvasWindow)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'lcCanvas'.
    """
    raise NotImplementedError(
        "'QQuickContext2DTexture.setCanvasWindow' has no cute function yet. "
        "Qt's 'bool QQuickContext2DTexture::setCanvasWindow(const QRect "
        "&canvasWindow)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'lcCanvas'.")
