"""
VideoTransformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideotransformation_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means VideoTransformation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QtVideo


class VideoTransformation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's VideoTransformation: a plain Python object standing
  in front of one C++ VideoTransformation.

  C++ hands a VideoTransformation around as a copy, so every C++
  VideoTransformation behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's VideoTransformation that has a ritual and that
  Python can call so far, 5 names in all: 'rotate', 'mirrorHorizontally',
  'mirrorVertically', 'rotationIndex', 'appendRotation'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'VideoTransformation::~VideoTransformation()': the destructor:
    Python removes its C++ VideoTransformation by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ VideoTransformation is created at the first use, not by
    'VideoTransformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a VideoTransformation back gives a copy the ritual made
    for Python, in a new cute VideoTransformation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'VideoTransformation'

  #  Qt's '~VideoTransformation()'. Naming it makes this a value class:
  #  Python owns every C++ VideoTransformation behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19VideoTransformationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rotationIndex(self) -> int:
    """
    Calls Qt's 'int VideoTransformation::rotationIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/videotransformation.html#rotationIndex
    """
    #  int VideoTransformation::rotationIndex() const
    return self.uglySide.call(
        'ritual_ZNK19VideoTransformation13rotationIndexEv',
    )

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

  @overload(QtVideo.Rotation)
  def rotate(self, rotation: QtVideo.Rotation) -> None:
    """
    Calls Qt's 'void VideoTransformation::rotate(QtVideo::Rotation
    rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/videotransformation.html#rotate

    Parameters
    ----------

    rotation : QtVideo.Rotation
      Passed on as its number.
    """
    #  void VideoTransformation::rotate(QtVideo::Rotation rotation)
    self.uglySide.call(
        'ritual_ZN19VideoTransformation6rotateEN7QtVideo8RotationE',
        rotation.value,
    )

  @overload()
  @overload(bool)
  def mirrorHorizontally(self, mirror: bool = True) -> None:
    """
    Calls Qt's 'void VideoTransformation::mirrorHorizontally(bool mirror)'.

    Qt's own words:
    https://doc.qt.io/qt-6/videotransformation.html#mirrorHorizontally

    Parameters
    ----------

    mirror : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void VideoTransformation::mirrorHorizontally(bool mirror)
    self.uglySide.call(
        'ritual_ZN19VideoTransformation18mirrorHorizontallyEb', mirror,
    )

  @overload()
  @overload(bool)
  def mirrorVertically(self, mirror: bool = True) -> None:
    """
    Calls Qt's 'void VideoTransformation::mirrorVertically(bool mirror)'.

    Qt's own words:
    https://doc.qt.io/qt-6/videotransformation.html#mirrorVertically

    Parameters
    ----------

    mirror : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void VideoTransformation::mirrorVertically(bool mirror)
    self.uglySide.call(
        'ritual_ZN19VideoTransformation16mirrorVerticallyEb', mirror,
    )

  @overload(int)
  def appendRotation(self, angle: int) -> None:
    """
    Calls Qt's 'void VideoTransformation::appendRotation(quint32 angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/videotransformation.html#appendRotation

    Parameters
    ----------

    angle : int
      Passed on as it is.
    """
    #  void VideoTransformation::appendRotation(quint32 angle)
    self.uglySide.call(
        'ritual_ZN19VideoTransformation14appendRotationEj', angle,
    )
