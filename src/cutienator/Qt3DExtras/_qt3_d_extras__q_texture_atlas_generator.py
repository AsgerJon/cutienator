"""
Qt3DExtras::QTextureAtlasGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QTextureAtlasGenerator to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..Qt3DRender import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QTextureAtlasGenerator(Qt3DRender.QTextureGenerator):
  """
  The cute side of Qt's Qt3DExtras::QTextureAtlasGenerator: a plain Python
  object standing in front of one C++ Qt3DExtras::QTextureAtlasGenerator.

  It is built on the cute 'Qt3DRender::QTextureGenerator', as Qt's
  Qt3DExtras::QTextureAtlasGenerator is built on Qt's
  Qt3DRender::QTextureGenerator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QTextureAtlasGenerator that has a ritual
  and that Python can call so far, 1 name in all: 'id'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DExtras::QTextureAtlasGenerator::~QTextureAtlasGenerator()': the
    destructor: Python never removes a C++
    Qt3DExtras::QTextureAtlasGenerator.
  - Qt's 'Qt3DRender::QTextureDataPtr
    Qt3DExtras::QTextureAtlasGenerator::operator()()': gives a type Python
    has no way to take yet.
  - Qt's 'bool Qt3DExtras::QTextureAtlasGenerator::operator==(const
    QTextureGenerator &other) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'Qt3DExtras.

  What to expect
  --------------

  - The C++ Qt3DExtras::QTextureAtlasGenerator is created at the first use,
    not by 'Qt3DExtras::QTextureAtlasGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QTextureAtlasGenerator.
  - Each name of Qt's Qt3DExtras::QTextureAtlasGenerator that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DExtras::QTextureAtlasGenerator'

  #  A C++ Qt3DExtras::QTextureAtlasGenerator Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QTextureAtlasGenerator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'qintptr Qt3DExtras::QTextureAtlasGenerator::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlasgenerator.html#id
    """
    #  qintptr Qt3DExtras::QTextureAtlasGenerator::id() const
    ritual = 'ritual_ZNK10Qt3DExtras22QTextureAtlasGenerator2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DExtras22QTextureAtlasGenerator2idEv'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DExtras::QTextureAtlasGenerator::QTextureAtlasGenerator(const
    QTextureAtlasPrivate *texAtlas)': leans on
    'Qt3DExtras::QTextureAtlasGenerator::operator()()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QTextureAtlasGenerator.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DExtras::QTextureAtlasGenerator::QTextureAtlasGenerator(const "
        "QTextureAtlasPrivate *texAtlas)': leans on "
        "'Qt3DExtras::QTextureAtlasGenerator::operator()()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
