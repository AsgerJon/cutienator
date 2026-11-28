"""
QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QVideoTextureHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QVideoFrameTexturesFromHandlesSet(QVideoTextureHelper.QVideoFrameTexturesFromRhiTextureArray):
  """
  The cute side of Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet: a plain Python
  object standing in front of one C++
  QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet.

  It is built on the cute
  'QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray', as Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet is built on Qt's
  QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray, and has
  everything that class has.

  What exists
  -----------

  No function of Qt's QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet
  yet. None can be made from Python: one comes out of a function of another
  class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet::
    ~QVideoFrameTexturesFromHandlesSet()': the destructor: Python never
    removes a C++ QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet.
  - Qt's 'QVideoFrameTexturesHandlesUPtr
    QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet::takeHandles()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet is created
    at the first use, not by
    'QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet.
  - Each name of Qt's QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet
    that has no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet'

  #  A C++ QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoTextureHelper_QVideoFrameTexturesFromHandlesSet'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet::
    QVideoFrameTexturesFromHandlesSet(RhiTextureArray &&rhiTextures,
    QVideoFrameTexturesHandlesUPtr handles)': the compiler refuses its ritual
    as it would be written here: call to deleted constructor of
    'QVideoFrameTexturesHandlesUPtr' (aka
    'std::unique_ptr<QVideoFrameTexturesHandles>').
    """
    raise NotImplementedError(
        "'QVideoTextureHelper.QVideoFrameTexturesFromHandlesSet.__init__' "
        "has no cute function yet. Qt's "
        "'QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet::QVideoFram"
        "eTexturesFromHandlesSet(RhiTextureArray &&rhiTextures, "
        "QVideoFrameTexturesHandlesUPtr handles)': the compiler refuses its "
        "ritual as it would be written here: call to deleted constructor of "
        "'QVideoFrameTexturesHandlesUPtr' (aka "
        "'std::unique_ptr<QVideoFrameTexturesHandles>').")

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
