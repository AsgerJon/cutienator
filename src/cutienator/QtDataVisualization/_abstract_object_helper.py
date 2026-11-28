"""
AbstractObjectHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/abstractobjecthelper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means AbstractObjectHelper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtGui import QOpenGLFunctions


class AbstractObjectHelper(QOpenGLFunctions):
  """
  The cute side of Qt's AbstractObjectHelper: a plain Python object standing
  in front of one C++ AbstractObjectHelper.

  It is built on the cute 'QOpenGLFunctions', as Qt's AbstractObjectHelper is
  built on Qt's QOpenGLFunctions, and has everything that class has.

  C++ hands a AbstractObjectHelper around as a copy, so every C++
  AbstractObjectHelper behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's AbstractObjectHelper that has a ritual and that
  Python can call so far, 5 names in all: 'vertexBuf', 'normalBuf', 'uvBuf',
  'elementBuf', 'indexCount'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'AbstractObjectHelper::~AbstractObjectHelper()': the destructor:
    Python removes its C++ AbstractObjectHelper by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ AbstractObjectHelper is created at the first use, not by
    'AbstractObjectHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a AbstractObjectHelper back gives a copy the ritual
    made for Python, in a new cute AbstractObjectHelper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AbstractObjectHelper'

  #  A C++ AbstractObjectHelper Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AbstractObjectHelper'

  #  The functions Qt calls itself that AbstractObjectHelper is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'uvBuf': (
          ('_ZN20AbstractObjectHelper5uvBufEv',
           ('unsigned int', 'number', ''),
           ()),
      ),
  }

  #  Qt's '~AbstractObjectHelper()'. Naming it makes this a value class:
  #  Python owns every C++ AbstractObjectHelper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20AbstractObjectHelperD1Ev'

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
    'AbstractObjectHelper::AbstractObjectHelper()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractobjecthelper.html#AbstractObjectHelper
    """
    #  AbstractObjectHelper::AbstractObjectHelper()
    self._noteCreation(AbstractObjectHelper, lambda: Rituals.call(
        'ritual_ZN20AbstractObjectHelperC1Ev',
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

  def vertexBuf(self) -> int:
    """
    Calls Qt's 'GLuint AbstractObjectHelper::vertexBuf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractobjecthelper.html#vertexBuf
    """
    #  GLuint AbstractObjectHelper::vertexBuf()
    return self.uglySide.call('ritual_ZN20AbstractObjectHelper9vertexBufEv')

  def normalBuf(self) -> int:
    """
    Calls Qt's 'GLuint AbstractObjectHelper::normalBuf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractobjecthelper.html#normalBuf
    """
    #  GLuint AbstractObjectHelper::normalBuf()
    return self.uglySide.call('ritual_ZN20AbstractObjectHelper9normalBufEv')

  def uvBuf(self) -> int:
    """
    Calls Qt's 'GLuint AbstractObjectHelper::uvBuf()'.

    Qt's own words: https://doc.qt.io/qt-6/abstractobjecthelper.html#uvBuf
    """
    #  GLuint AbstractObjectHelper::uvBuf()
    ritual = 'ritual_ZN20AbstractObjectHelper5uvBufEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20AbstractObjectHelper5uvBufEv'
    return self.uglySide.call(ritual)

  def elementBuf(self) -> int:
    """
    Calls Qt's 'GLuint AbstractObjectHelper::elementBuf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractobjecthelper.html#elementBuf
    """
    #  GLuint AbstractObjectHelper::elementBuf()
    return self.uglySide.call(
        'ritual_ZN20AbstractObjectHelper10elementBufEv',
    )

  def indexCount(self) -> int:
    """
    Calls Qt's 'GLuint AbstractObjectHelper::indexCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractobjecthelper.html#indexCount
    """
    #  GLuint AbstractObjectHelper::indexCount()
    return self.uglySide.call(
        'ritual_ZN20AbstractObjectHelper10indexCountEv',
    )
