"""
QVarLengthGlyphLayoutArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVarLengthGlyphLayoutArray to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QGlyphLayout


class QVarLengthGlyphLayoutArray(QGlyphLayout):
  """
  The cute side of Qt's QVarLengthGlyphLayoutArray: a plain Python object
  standing in front of one C++ QVarLengthGlyphLayoutArray.

  C++ hands a QVarLengthGlyphLayoutArray around as a copy, so every C++
  QVarLengthGlyphLayoutArray behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QVarLengthGlyphLayoutArray that has a ritual and
  that Python can call so far, 1 name in all: 'resize'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVarLengthGlyphLayoutArray::~QVarLengthGlyphLayoutArray()': the
    destructor: Python removes its C++ QVarLengthGlyphLayoutArray by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QVarLengthGlyphLayoutArray is created at the first use, not by
    'QVarLengthGlyphLayoutArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVarLengthGlyphLayoutArray back gives a copy the
    ritual made for Python, in a new cute QVarLengthGlyphLayoutArray.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVarLengthGlyphLayoutArray'

  #  Qt's QVarLengthGlyphLayoutArray is built on more than one class. The
  #  part of a C++ QVarLengthGlyphLayoutArray that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QGlyphLayout': 'ritual_cast_QVarLengthGlyphLayoutArray_QGlyphLayout',
  }

  #  Qt's '~QVarLengthGlyphLayoutArray()'. Naming it makes this a value
  #  class: Python owns every C++ QVarLengthGlyphLayoutArray behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QVarLengthGlyphLayoutArrayD1Ev'

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

  @overload(int)
  def __init__(self, totalGlyphs: int) -> None:
    """
    Notes what was given, for Qt's
    'QVarLengthGlyphLayoutArray::QVarLengthGlyphLayoutArray(int
    totalGlyphs)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvarlengthglyphlayoutarray.html

    Parameters
    ----------

    totalGlyphs : int
      Passed on as it is.
    """
    #  QVarLengthGlyphLayoutArray::QVarLengthGlyphLayoutArray(int
    #      totalGlyphs)
    self._noteCreation(QVarLengthGlyphLayoutArray, lambda: Rituals.call(
        'ritual_ZN26QVarLengthGlyphLayoutArrayC1Ei', totalGlyphs,
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

  @overload(int)
  def resize(self, totalGlyphs: int) -> None:
    """
    Calls Qt's 'void QVarLengthGlyphLayoutArray::resize(int totalGlyphs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvarlengthglyphlayoutarray.html#resize

    Parameters
    ----------

    totalGlyphs : int
      Passed on as it is.
    """
    #  void QVarLengthGlyphLayoutArray::resize(int totalGlyphs)
    self.uglySide.call(
        'ritual_ZN26QVarLengthGlyphLayoutArray6resizeEi', totalGlyphs,
    )
