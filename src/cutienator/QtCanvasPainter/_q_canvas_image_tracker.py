"""
QCanvasImageTracker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainter_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasImageTracker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QCanvasImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasImage = WAIT['QCanvasImage']


class QCanvasImageTracker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasImageTracker: a plain Python object standing
  in front of one C++ QCanvasImageTracker.

  C++ hands a QCanvasImageTracker around as a copy, so every C++
  QCanvasImageTracker behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasImageTracker that has a ritual and that
  Python can call so far, 10 names in all: 'contains', 'image', 'textureId',
  'insert', 'dataAmount', 'size', 'removeTemporaryResources',
  'removeTextureId', 'markTextureIdUsed', 'clear'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasImageTracker::~QCanvasImageTracker()': the destructor:
    Python removes its C++ QCanvasImageTracker by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 leans on 'QCPainterRhiRenderer.

  What to expect
  --------------

  - The C++ QCanvasImageTracker is created at the first use, not by
    'QCanvasImageTracker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasImageTracker back gives a copy the ritual made
    for Python, in a new cute QCanvasImageTracker.
  - Each name of Qt's QCanvasImageTracker that has no cute function yet,
    'handleRemoveTextures', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasImageTracker'

  #  Qt's '~QCanvasImageTracker()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasImageTracker behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QCanvasImageTrackerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def contains(self, key: int) -> bool:
    """
    Calls Qt's 'bool QCanvasImageTracker::contains(qint64 key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagetracker.html#contains

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  bool QCanvasImageTracker::contains(qint64 key) const
    return self.uglySide.call(
        'ritual_ZNK19QCanvasImageTracker8containsEx', key,
    )

  @overload(int)
  def image(self, key: int) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage QCanvasImageTracker::image(qint64 key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagetracker.html#image

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasImageTracker::image(qint64 key) const
    address = self.uglySide.call(
        'ritual_ZNK19QCanvasImageTracker5imageEx', key,
    )
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  @overload(int)
  def textureId(self, key: int) -> int:
    """
    Calls Qt's 'int QCanvasImageTracker::textureId(qint64 key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagetracker.html#textureId

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  int QCanvasImageTracker::textureId(qint64 key) const
    return self.uglySide.call(
        'ritual_ZNK19QCanvasImageTracker9textureIdEx', key,
    )

  def dataAmount(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasImageTracker::dataAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagetracker.html#dataAmount
    """
    #  qsizetype QCanvasImageTracker::dataAmount() const
    return self.uglySide.call(
        'ritual_ZNK19QCanvasImageTracker10dataAmountEv',
    )

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasImageTracker::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagetracker.html#size
    """
    #  qsizetype QCanvasImageTracker::size() const
    return self.uglySide.call('ritual_ZNK19QCanvasImageTracker4sizeEv')

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

  @overload(int, QCanvasImage)
  def insert(self, key: int, image: QCanvasImage) -> None:
    """
    Calls Qt's 'void QCanvasImageTracker::insert(qint64 key, const
    QCanvasImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagetracker.html#insert

    Parameters
    ----------

    key : int
      Passed on as it is.

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.
    """
    #  void QCanvasImageTracker::insert(qint64 key, const QCanvasImage
    #      &image)
    self.uglySide.call(
        'ritual_ZN19QCanvasImageTracker6insertExRK12QCanvasImage',
        key, self._valueOf(image),
    )

  def removeTemporaryResources(self) -> None:
    """
    Calls Qt's 'void QCanvasImageTracker::removeTemporaryResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagetracker.html#removeTemporaryResources
    """
    #  void QCanvasImageTracker::removeTemporaryResources()
    self.uglySide.call(
        'ritual_ZN19QCanvasImageTracker24removeTemporaryResourcesEv',
    )

  @overload(int)
  def removeTextureId(self, imageId: int) -> None:
    """
    Calls Qt's 'void QCanvasImageTracker::removeTextureId(int imageId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagetracker.html#removeTextureId

    Parameters
    ----------

    imageId : int
      Passed on as it is.
    """
    #  void QCanvasImageTracker::removeTextureId(int imageId)
    self.uglySide.call(
        'ritual_ZN19QCanvasImageTracker15removeTextureIdEi', imageId,
    )

  @overload(int)
  def markTextureIdUsed(self, imageId: int) -> None:
    """
    Calls Qt's 'void QCanvasImageTracker::markTextureIdUsed(int imageId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagetracker.html#markTextureIdUsed

    Parameters
    ----------

    imageId : int
      Passed on as it is.
    """
    #  void QCanvasImageTracker::markTextureIdUsed(int imageId)
    self.uglySide.call(
        'ritual_ZN19QCanvasImageTracker17markTextureIdUsedEi', imageId,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QCanvasImageTracker::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagetracker.html#clear
    """
    #  void QCanvasImageTracker::clear()
    self.uglySide.call('ritual_ZN19QCanvasImageTracker5clearEv')

  @staticmethod
  def handleRemoveTextures(*__, **_) -> Never:
    """
    Qt's 'void QCanvasImageTracker::handleRemoveTextures()': leans on
    'QCPainterRhiRenderer::renderDeleteTexture(int)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCanvasImageTracker.handleRemoveTextures' has no cute function "
        "yet. Qt's 'void QCanvasImageTracker::handleRemoveTextures()': "
        "leans on 'QCPainterRhiRenderer::renderDeleteTexture(int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
