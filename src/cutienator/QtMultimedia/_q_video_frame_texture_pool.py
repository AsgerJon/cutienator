"""
QVideoFrameTexturePool binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturepool_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QVideoFrameTexturePool to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVideoFrame = WAIT['QVideoFrame']


class QVideoFrameTexturePool(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVideoFrameTexturePool: a plain Python object
  standing in front of one C++ QVideoFrameTexturePool.

  What exists
  -----------

  Every function of Qt's QVideoFrameTexturePool that has a ritual and that
  Python can call so far, 5 names in all: 'texturesDirty', 'currentFrame',
  'setCurrentFrame', 'onFrameEndInvoked', 'clearTextures'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoFrameTextures *QVideoFrameTexturePool::updateTextures(QRhi
    &rhi, QRhiResourceUpdateBatch &rub)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QVideoFrameTexturePool is created at the first use, not by
    'QVideoFrameTexturePool(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoFrameTexturePool.
  - Each name of Qt's QVideoFrameTexturePool that has no cute function yet,
    'updateTextures', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QVideoFrameTexturePool'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texturesDirty(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrameTexturePool::texturesDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframetexturepool.html#texturesDirty
    """
    #  bool QVideoFrameTexturePool::texturesDirty() const
    return self.uglySide.call(
        'ritual_ZNK22QVideoFrameTexturePool13texturesDirtyEv',
    )

  def currentFrame(self) -> QVideoFrame:
    """
    Calls Qt's 'const QVideoFrame &QVideoFrameTexturePool::currentFrame()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframetexturepool.html#currentFrame

    Returns
    -------

    QVideoFrame
      A new cute QVideoFrame around the copy Qt gave back. Python owns it.
    """
    #  const QVideoFrame &QVideoFrameTexturePool::currentFrame() const
    address = self.uglySide.call(
        'ritual_ZNK22QVideoFrameTexturePool12currentFrameEv',
    )
    from . import QVideoFrame
    return QVideoFrame._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVideoFrame)
  def setCurrentFrame(self, frame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QVideoFrameTexturePool::setCurrentFrame(QVideoFrame
    frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframetexturepool.html#setCurrentFrame

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QVideoFrameTexturePool::setCurrentFrame(QVideoFrame frame)
    self.uglySide.call(
        'ritual_ZN22QVideoFrameTexturePool15setCurrentFrameE11QVideoFrame',
        self._valueOf(frame),
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

  def onFrameEndInvoked(self) -> None:
    """
    Calls Qt's 'void QVideoFrameTexturePool::onFrameEndInvoked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframetexturepool.html#onFrameEndInvoked
    """
    #  void QVideoFrameTexturePool::onFrameEndInvoked()
    self.uglySide.call(
        'ritual_ZN22QVideoFrameTexturePool17onFrameEndInvokedEv',
    )

  def clearTextures(self) -> None:
    """
    Calls Qt's 'void QVideoFrameTexturePool::clearTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframetexturepool.html#clearTextures
    """
    #  void QVideoFrameTexturePool::clearTextures()
    self.uglySide.call('ritual_ZN22QVideoFrameTexturePool13clearTexturesEv')

  @staticmethod
  def updateTextures(*__, **_) -> Never:
    """
    Qt's 'QVideoFrameTextures *QVideoFrameTexturePool::updateTextures(QRhi
    &rhi, QRhiResourceUpdateBatch &rub)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QVideoFrameTexturePool.updateTextures' has no cute function yet. "
        "Qt's 'QVideoFrameTextures "
        "*QVideoFrameTexturePool::updateTextures(QRhi &rhi, "
        "QRhiResourceUpdateBatch &rub)': takes a type Python has no way to "
        "hand over yet.")
