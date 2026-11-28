"""
QCanvasImagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasimage_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasImagePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCanvasImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasImage = WAIT['QCanvasImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasImagePrivate(QSharedData):
  """
  The cute side of Qt's QCanvasImagePrivate: a plain Python object standing
  in front of one C++ QCanvasImagePrivate.

  It is built on the cute 'QSharedData', as Qt's QCanvasImagePrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QCanvasImagePrivate around as a copy, so every C++
  QCanvasImagePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasImagePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'get'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCanvasImagePrivate *QCanvasImagePrivate::get(const
    QCanvasImage *image)': takes in Python what 'QCanvasImagePrivate
    *QCanvasImagePrivate::get(QCanvasImage *image)' takes.
  - Qt's 'QCanvasImagePrivate::~QCanvasImagePrivate()': the destructor:
    Python removes its C++ QCanvasImagePrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QCanvasImagePrivate is created at the first use, not by
    'QCanvasImagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasImagePrivate back gives a copy the ritual made
    for Python, in a new cute QCanvasImagePrivate.
  """

  #  The enums Qt writes inside QCanvasImagePrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DataType(CuteNum, scoped=True):
    """
    The enum 'QCanvasImagePrivate::DataType' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unknown = Kee[int](0)
    GradientTextureFromImage = Kee[int](1)
    TextureFromImage = Kee[int](2)
    ImportedTexture = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanvasImage)
  @overload(NoneType)
  def get(image: Optional[QCanvasImage]) -> Optional[QCanvasImagePrivate]:
    """
    Calls Qt's 'QCanvasImagePrivate *QCanvasImagePrivate::get(QCanvasImage
    *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimageprivate.html#get

    Parameters
    ----------

    image : Optional[QCanvasImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasImagePrivate *QCanvasImagePrivate::get(QCanvasImage *image)
    address = Rituals.call(
        'ritual_ZN19QCanvasImagePrivate3getEP12QCanvasImage',
        CuteMixin._addressOf(image),
    )
    return QCanvasImagePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasImagePrivate'

  #  Qt's '~QCanvasImagePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasImagePrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QCanvasImagePrivateD1Ev'

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasImagePrivate::QCanvasImagePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimageprivate.html#QCanvasImagePrivate
    """
    #  QCanvasImagePrivate::QCanvasImagePrivate()
    self._noteCreation(QCanvasImagePrivate, lambda: Rituals.call(
        'ritual_ZN19QCanvasImagePrivateC1Ev',
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
