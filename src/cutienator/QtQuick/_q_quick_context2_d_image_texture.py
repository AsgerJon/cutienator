"""
QQuickContext2DImageTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickContext2DImageTexture to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickCanvasItem, QQuickContext2DTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPaintDevice
  from . import QQuickContext2DTile, QQuickWindow, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickContext2DTile = WAIT['QQuickContext2DTile']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSGTexture = WAIT['QSGTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContext2DImageTexture(QQuickContext2DTexture):
  """
  The cute side of Qt's QQuickContext2DImageTexture: a plain Python object
  standing in front of one C++ QQuickContext2DImageTexture.

  It is built on the cute 'QQuickContext2DTexture', as Qt's
  QQuickContext2DImageTexture is built on Qt's QQuickContext2DTexture, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickContext2DImageTexture that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'renderTarget',
  'createTile', 'beginPainting', 'endPainting', 'compositeTile',
  'textureForNextFrame', 'grabImage'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickContext2DImageTexture::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickContext2DImageTexture::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickContext2DImageTexture::~QQuickContext2DImageTexture()': the
    destructor: Python never removes a C++ QQuickContext2DImageTexture.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickContext2DImageTexture.

  What to expect
  --------------

  - The C++ QQuickContext2DImageTexture is created at the first use, not by
    'QQuickContext2DImageTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContext2DImageTexture.
  - Qt tells when it has removed the C++ QQuickContext2DImageTexture. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickContext2DImageTexture that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContext2DImageTexture'

  #  A C++ QQuickContext2DImageTexture Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContext2DImageTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickContext2DImageTexture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickContext2DImageTexture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickContext2DImageTexture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderTarget(self) -> QQuickCanvasItem.RenderTarget:
    """
    Calls Qt's 'QQuickCanvasItem::RenderTarget
    QQuickContext2DImageTexture::renderTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html#renderTarget

    Returns
    -------

    QQuickCanvasItem.RenderTarget
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickCanvasItem.RenderTarget(number)' gives.
    """
    #  QQuickCanvasItem::RenderTarget
    #      QQuickContext2DImageTexture::renderTarget() const
    ritual = 'ritual_ZNK27QQuickContext2DImageTexture12renderTargetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QQuickContext2DImageTexture12renderTargetEv'
    return QQuickCanvasItem.RenderTarget(self.uglySide.call(ritual))

  def createTile(self) -> Optional[QQuickContext2DTile]:
    """
    Calls Qt's 'QQuickContext2DTile
    *QQuickContext2DImageTexture::createTile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html#createTile

    Returns
    -------

    Optional[QQuickContext2DTile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContext2DTile *QQuickContext2DImageTexture::createTile() const
    ritual = 'ritual_ZNK27QQuickContext2DImageTexture10createTileEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QQuickContext2DImageTexture10createTileEv'
    address = self.uglySide.call(ritual)
    from . import QQuickContext2DTile
    return QQuickContext2DTile._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QQuickContext2DImageTexture::QQuickContext2DImageTexture()': leans
    on 'QQuickContext2DImageTexture::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickContext2DImageTexture.__init__' has no cute function yet. "
        "Qt's 'QQuickContext2DImageTexture::QQuickContext2DImageTexture()': "
        "leans on "
        "'QQuickContext2DImageTexture::qt_metacall(QMetaObject::Call, int, "
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

  def beginPainting(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QQuickContext2DImageTexture::beginPainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html#beginPainting

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QQuickContext2DImageTexture::beginPainting()
    address = self.uglySide.call(
        'ritual_ZN27QQuickContext2DImageTexture13beginPaintingEv',
    )
    from ..QtGui import QPaintDevice
    return QPaintDevice._cuteAt(address)

  def endPainting(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DImageTexture::endPainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html#endPainting
    """
    #  void QQuickContext2DImageTexture::endPainting()
    ritual = 'ritual_ZN27QQuickContext2DImageTexture11endPaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickContext2DImageTexture11endPaintingEv'
    self.uglySide.call(ritual)

  @overload(QQuickContext2DTile)
  @overload(NoneType)
  def compositeTile(self, tile: Optional[QQuickContext2DTile]) -> None:
    """
    Calls Qt's 'void
    QQuickContext2DImageTexture::compositeTile(QQuickContext2DTile *tile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html#compositeTile

    Parameters
    ----------

    tile : Optional[QQuickContext2DTile]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContext2DImageTexture::compositeTile(QQuickContext2DTile
    #      *tile)
    ritual = (
        'ritual_ZN27QQuickContext2DImageTexture13compositeTileEP19QQuickCon'
        'text2DTile')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickContext2DImageTexture13compositeTileEP19QQu'
          'ickContext2DTile')
    self.uglySide.call(ritual, self._addressOf(tile))

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
    *QQuickContext2DImageTexture::textureForNextFrame(QSGTexture *lastFrame,
    QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html

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
    #  QSGTexture
    #      *QQuickContext2DImageTexture::textureForNextFrame(QSGTexture
    #      *lastFrame, QQuickWindow *window)
    ritual = (
        'ritual_ZN27QQuickContext2DImageTexture19textureForNextFrameEP10QSG'
        'TextureP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickContext2DImageTexture19textureForNextFrameE'
          'P10QSGTextureP12QQuickWindow')
    address = self.uglySide.call(
        ritual, self._addressOf(lastFrame), self._addressOf(window),
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload()
  @overload(QRectF)
  def grabImage(self, region: Optional[QRectF] = None) -> None:
    """
    Calls Qt's 'void QQuickContext2DImageTexture::grabImage(const QRectF
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dimagetexture.html#grabImage

    Parameters
    ----------

    region : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickContext2DImageTexture::grabImage(const QRectF &region)
    if region is None:
      from ..QtCore import QRectF
      region = QRectF()
    self.uglySide.call(
        'ritual_ZN27QQuickContext2DImageTexture9grabImageERK6QRectF',
        self._valueOf(region),
    )
