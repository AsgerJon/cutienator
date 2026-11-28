"""
Qt3DRender::QPaintedTextureImageDataGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qpaintedtextureimage_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QPaintedTextureImageDataGenerator to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']


class QPaintedTextureImageDataGenerator(Qt3DRender.QTextureImageDataGenerator):
  """
  The cute side of Qt's Qt3DRender::QPaintedTextureImageDataGenerator: a
  plain Python object standing in front of one C++
  Qt3DRender::QPaintedTextureImageDataGenerator.

  It is built on the cute 'Qt3DRender::QTextureImageDataGenerator', as Qt's
  Qt3DRender::QPaintedTextureImageDataGenerator is built on Qt's
  Qt3DRender::QTextureImageDataGenerator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPaintedTextureImageDataGenerator that
  has a ritual and that Python can call so far, 1 name in all: 'id'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QPaintedTextureImageDataGenerator::
    ~QPaintedTextureImageDataGenerator()': the destructor: Python never
    removes a C++ Qt3DRender::QPaintedTextureImageDataGenerator.
  - Qt's 'QTextureImageDataPtr
    Qt3DRender::QPaintedTextureImageDataGenerator::operator()()': gives a
    type Python has no way to take yet.
  - Qt's 'bool
    Qt3DRender::QPaintedTextureImageDataGenerator::operator==(const
    QTextureImageDataGenerator &other) const': takes a type Python has no way
    to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::QPaintedTextureImageDataGenerator is created at the
    first use, not by 'Qt3DRender::QPaintedTextureImageDataGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::QPaintedTextureImageDataGenerator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPaintedTextureImageDataGenerator'

  #  A C++ Qt3DRender::QPaintedTextureImageDataGenerator Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QPaintedTextureImageDataGenerator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimagedatagenerator.html
    """
    #  qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id() const
    ritual = 'ritual_ZNK10Qt3DRender33QPaintedTextureImageDataGenerator2idEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10Qt3DRender33QPaintedTextureImageDataGenerator2id'
          'Ev')
    return self.uglySide.call(ritual)

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

  @overload(QImage, int, WAIT['Qt3DCore.QNodeId'])
  def __init__(
      self,
      image: QImage,
      gen: int,
      texId: Qt3DCore.QNodeId,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QPaintedTextureImageDataGenerator::
    QPaintedTextureImageDataGenerator(const QImage &image, int gen,
    Qt3DCore::QNodeId texId)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpaintedtextureimagedatagenerator.html

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    gen : int
      Passed on as it is.

    texId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  Qt3DRender::QPaintedTextureImageDataGenerator::
    #      QPaintedTextureImageDataGenerator(const QImage &image, int gen,
    #      Qt3DCore::QNodeId texId)
    self._noteCreation(
        QPaintedTextureImageDataGenerator, lambda: Rituals.call(
            'ritual_ZN10Qt3DRender33QPaintedTextureImageDataGeneratorC1ERK6'
            'QImageiN8Qt3DCore7QNodeIdE',
            self._valueOf(image), gen, self._valueOf(texId),
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
