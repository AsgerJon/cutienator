"""
QGnomeThemePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgnometheme_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QGnomeThemePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt
from . import QGenericUnixThemePrivate


class QGnomeThemePrivate(QGenericUnixThemePrivate):
  """
  The cute side of Qt's QGnomeThemePrivate: a plain Python object standing in
  front of one C++ QGnomeThemePrivate.

  It is built on the cute 'QGenericUnixThemePrivate', as Qt's
  QGnomeThemePrivate is built on Qt's QGenericUnixThemePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGnomeThemePrivate that has a ritual and that Python
  can call so far, 3 names in all: 'configureFonts', 'colorScheme',
  'hasRequestedColorScheme'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGnomeThemePrivate::~QGnomeThemePrivate()': the destructor: Python
    never removes a C++ QGnomeThemePrivate.

  What to expect
  --------------

  - The C++ QGnomeThemePrivate is created at the first use, not by
    'QGnomeThemePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGnomeThemePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGnomeThemePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QGnomeThemePrivate::colorScheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomethemeprivate.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QGnomeThemePrivate::colorScheme() const
    return Qt.ColorScheme(self.uglySide.call(
        'ritual_ZNK18QGnomeThemePrivate11colorSchemeEv',
    ))

  def hasRequestedColorScheme(self) -> bool:
    """
    Calls Qt's 'bool QGnomeThemePrivate::hasRequestedColorScheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomethemeprivate.html#hasRequestedColorScheme
    """
    #  bool QGnomeThemePrivate::hasRequestedColorScheme() const
    return self.uglySide.call(
        'ritual_ZNK18QGnomeThemePrivate23hasRequestedColorSchemeEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QGnomeThemePrivate::QGnomeThemePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomethemeprivate.html#QGnomeThemePrivate
    """
    #  QGnomeThemePrivate::QGnomeThemePrivate()
    self._noteCreation(QGnomeThemePrivate, lambda: Rituals.call(
        'ritual_ZN18QGnomeThemePrivateC1Ev',
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

  @overload(str)
  def configureFonts(self, gtkFontName: str) -> None:
    """
    Calls Qt's 'void QGnomeThemePrivate::configureFonts(const QString
    &gtkFontName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomethemeprivate.html#configureFonts

    Parameters
    ----------

    gtkFontName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGnomeThemePrivate::configureFonts(const QString &gtkFontName)
    #      const
    self.uglySide.call(
        'ritual_ZNK18QGnomeThemePrivate14configureFontsERK7QString',
        gtkFontName,
    )
