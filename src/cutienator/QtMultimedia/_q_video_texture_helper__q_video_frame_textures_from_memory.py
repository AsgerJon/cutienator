"""
QVideoTextureHelper::QVideoFrameTexturesFromMemory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QVideoTextureHelper::QVideoFrameTexturesFromMemory to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QVideoTextureHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVideoFrame = WAIT['QVideoFrame']


class QVideoFrameTexturesFromMemory(QVideoTextureHelper.QVideoFrameTexturesFromRhiTextureArray):
  """
  The cute side of Qt's QVideoTextureHelper::QVideoFrameTexturesFromMemory: a
  plain Python object standing in front of one C++
  QVideoTextureHelper::QVideoFrameTexturesFromMemory.

  It is built on the cute
  'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray', as Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromMemory is built on Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QVideoTextureHelper::QVideoFrameTexturesFromMemory
  that has a ritual and that Python can call so far, 2 names in all:
  'setMappedFrame', 'onFrameEndInvoked'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoTextureHelper::QVideoFrameTexturesFromMemory::
    ~QVideoFrameTexturesFromMemory()': the destructor: Python never removes a
    C++ QVideoTextureHelper::QVideoFrameTexturesFromMemory.

  What to expect
  --------------

  - The C++ QVideoTextureHelper::QVideoFrameTexturesFromMemory is created at
    the first use, not by
    'QVideoTextureHelper::QVideoFrameTexturesFromMemory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QVideoTextureHelper::QVideoFrameTexturesFromMemory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoTextureHelper::QVideoFrameTexturesFromMemory'

  #  A C++ QVideoTextureHelper::QVideoFrameTexturesFromMemory Python makes is
  #  of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoTextureHelper_QVideoFrameTexturesFromMemory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVideoFrame)
  def setMappedFrame(self, mappedFrame: QVideoFrame) -> None:
    """
    Calls Qt's 'void
    QVideoTextureHelper::QVideoFrameTexturesFromMemory::setMappedFrame(
    QVideoFrame mappedFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-qvideoframetexturesfrommemory.html

    Parameters
    ----------

    mappedFrame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QVideoTextureHelper::QVideoFrameTexturesFromMemory::
    #      setMappedFrame(QVideoFrame mappedFrame)
    self.uglySide.call(
        'ritual_ZN19QVideoTextureHelper29QVideoFrameTexturesFromMemory14set'
        'MappedFrameE11QVideoFrame',
        self._valueOf(mappedFrame),
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
    Calls Qt's 'void
    QVideoTextureHelper::QVideoFrameTexturesFromMemory::onFrameEndInvoked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-qvideoframetexturesfrommemory.html
    """
    #  void QVideoTextureHelper::QVideoFrameTexturesFromMemory::
    #      onFrameEndInvoked()
    ritual = (
        'ritual_ZN19QVideoTextureHelper29QVideoFrameTexturesFromMemory17onF'
        'rameEndInvokedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QVideoTextureHelper29QVideoFrameTexturesFromMemor'
          'y17onFrameEndInvokedEv')
    self.uglySide.call(ritual)
