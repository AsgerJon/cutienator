"""
QSvgGlyph binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgfont_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgGlyph to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']


class QSvgGlyph(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgGlyph: a plain Python object standing in front of
  one C++ QSvgGlyph.

  C++ hands a QSvgGlyph around as a copy, so every C++ QSvgGlyph behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSvgGlyph yet. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgGlyph::~QSvgGlyph()': the destructor: Python removes its C++
    QSvgGlyph by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSvgGlyph is created at the first use, not by 'QSvgGlyph(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgGlyph back gives a copy the ritual made for
    Python, in a new cute QSvgGlyph.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgGlyph'

  #  Qt's '~QSvgGlyph()'. Naming it makes this a value class: Python owns
  #  every C++ QSvgGlyph behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSvgGlyphD1Ev'

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

  @overload(str, QPainterPath, float)
  def __init__(
      self,
      unicode: str,
      path: QPainterPath,
      horizAdvX: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgGlyph::QSvgGlyph(const QString
    &unicode, const QPainterPath &path, qreal horizAdvX)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgglyph.html#QSvgGlyph

    Parameters
    ----------

    unicode : str
      Passed on as it is: a QString is made of it for the call.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    horizAdvX : float
      Passed on as it is.
    """
    #  QSvgGlyph::QSvgGlyph(const QString &unicode, const QPainterPath &path,
    #      qreal horizAdvX)
    self._noteCreation(QSvgGlyph, lambda: Rituals.call(
        'ritual_ZN9QSvgGlyphC1ERK7QStringRK12QPainterPathd',
        unicode, self._valueOf(path), horizAdvX,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSvgGlyph::QSvgGlyph()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgglyph.html#QSvgGlyph
    """
    #  QSvgGlyph::QSvgGlyph()
    self._noteCreation(QSvgGlyph, lambda: Rituals.call(
        'ritual_ZN9QSvgGlyphC1Ev',
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
