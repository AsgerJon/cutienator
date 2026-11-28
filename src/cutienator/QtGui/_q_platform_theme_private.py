"""
QPlatformThemePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformtheme_p.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QPlatformThemePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformThemePrivate: a plain Python object standing
  in front of one C++ QPlatformThemePrivate.

  C++ hands a QPlatformThemePrivate around as a copy, so every C++
  QPlatformThemePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformThemePrivate that has a ritual and that
  Python can call so far, 2 names in all: 'initializeSystemPalette',
  'currentKeyPlatforms'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformThemePrivate::~QPlatformThemePrivate()': the destructor:
    Python removes its C++ QPlatformThemePrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPlatformThemePrivate is created at the first use, not by
    'QPlatformThemePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformThemePrivate back gives a copy the ritual
    made for Python, in a new cute QPlatformThemePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def currentKeyPlatforms() -> int:
    """
    Calls Qt's 'unsigned int QPlatformThemePrivate::currentKeyPlatforms()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformthemeprivate.html#currentKeyPlatforms
    """
    #  unsigned int QPlatformThemePrivate::currentKeyPlatforms()
    return Rituals.call(
        'ritual_ZN21QPlatformThemePrivate19currentKeyPlatformsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformThemePrivate'

  #  Qt's '~QPlatformThemePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformThemePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QPlatformThemePrivateD1Ev'

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
    'QPlatformThemePrivate::QPlatformThemePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformthemeprivate.html#QPlatformThemePrivate
    """
    #  QPlatformThemePrivate::QPlatformThemePrivate()
    self._noteCreation(QPlatformThemePrivate, lambda: Rituals.call(
        'ritual_ZN21QPlatformThemePrivateC1Ev',
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

  def initializeSystemPalette(self) -> None:
    """
    Calls Qt's 'void QPlatformThemePrivate::initializeSystemPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformthemeprivate.html#initializeSystemPalette
    """
    #  void QPlatformThemePrivate::initializeSystemPalette()
    self.uglySide.call(
        'ritual_ZN21QPlatformThemePrivate23initializeSystemPaletteEv',
    )
