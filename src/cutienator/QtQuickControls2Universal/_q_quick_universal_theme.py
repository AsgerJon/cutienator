"""
QQuickUniversalTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Universal/6.12.0/QtQuickControls2Universal/private/qquickuniversaltheme_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickUniversalTheme to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickUniversalStyle
  from ..QtQuickTemplates2 import QQuickTheme
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTheme = WAIT['QQuickTheme']
  QQuickUniversalStyle = WAIT['QQuickUniversalStyle']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickUniversalTheme(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickUniversalTheme: a plain Python object standing
  in front of one C++ QQuickUniversalTheme.

  C++ hands a QQuickUniversalTheme around as a copy, so every C++
  QQuickUniversalTheme behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickUniversalTheme that has a ritual and that
  Python can call so far, 4 names in all: 'initialize',
  'registerSystemStyle', 'unregisterSystemStyle', 'updateTheme'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickUniversalTheme::~QQuickUniversalTheme()': the destructor:
    Python removes its C++ QQuickUniversalTheme by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickUniversalTheme is created at the first use, not by
    'QQuickUniversalTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickUniversalTheme back gives a copy the ritual
    made for Python, in a new cute QQuickUniversalTheme.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTheme)
  @overload(NoneType)
  def initialize(theme: Optional[QQuickTheme]) -> None:
    """
    Calls Qt's 'void QQuickUniversalTheme::initialize(QQuickTheme *theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversaltheme.html#initialize

    Parameters
    ----------

    theme : Optional[QQuickTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickUniversalTheme::initialize(QQuickTheme *theme)
    Rituals.call(
        'ritual_ZN20QQuickUniversalTheme10initializeEP11QQuickTheme',
        CuteMixin._addressOf(theme),
    )

  @staticmethod
  @overload(QQuickUniversalStyle)
  @overload(NoneType)
  def registerSystemStyle(style: Optional[QQuickUniversalStyle]) -> None:
    """
    Calls Qt's 'void
    QQuickUniversalTheme::registerSystemStyle(QQuickUniversalStyle *style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversaltheme.html#registerSystemStyle

    Parameters
    ----------

    style : Optional[QQuickUniversalStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickUniversalTheme::registerSystemStyle(QQuickUniversalStyle
    #      *style)
    Rituals.call(
        'ritual_ZN20QQuickUniversalTheme19registerSystemStyleEP20QQuickUniv'
        'ersalStyle',
        CuteMixin._addressOf(style),
    )

  @staticmethod
  @overload(QQuickUniversalStyle)
  @overload(NoneType)
  def unregisterSystemStyle(style: Optional[QQuickUniversalStyle]) -> None:
    """
    Calls Qt's 'void
    QQuickUniversalTheme::unregisterSystemStyle(QQuickUniversalStyle
    *style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversaltheme.html#unregisterSystemStyle

    Parameters
    ----------

    style : Optional[QQuickUniversalStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickUniversalTheme::unregisterSystemStyle(QQuickUniversalStyle
    #      *style)
    Rituals.call(
        'ritual_ZN20QQuickUniversalTheme21unregisterSystemStyleEP20QQuickUn'
        'iversalStyle',
        CuteMixin._addressOf(style),
    )

  @staticmethod
  def updateTheme() -> None:
    """
    Calls Qt's 'void QQuickUniversalTheme::updateTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversaltheme.html#updateTheme
    """
    #  void QQuickUniversalTheme::updateTheme()
    Rituals.call('ritual_ZN20QQuickUniversalTheme11updateThemeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickUniversalTheme'

  #  Qt's '~QQuickUniversalTheme()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickUniversalTheme behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickUniversalThemeD1Ev'

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
