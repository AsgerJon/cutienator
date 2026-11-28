"""
QPdf::Stroker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPdf::Stroker to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPen = WAIT['QPen']


class Stroker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdf::Stroker: a plain Python object standing in
  front of one C++ QPdf::Stroker.

  What exists
  -----------

  Every function of Qt's QPdf::Stroker that has a ritual and that Python can
  call so far, 1 name in all: 'setPen'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 2 leans on 'QPdf.

  What to expect
  --------------

  - The C++ QPdf::Stroker is created at the first use, not by
    'QPdf::Stroker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdf::Stroker.
  - Each name of Qt's QPdf::Stroker that has no cute function yet,
    '__init__', 'strokePath', holds a function that raises
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
  __qt_class__ = 'QPdf::Stroker'

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

  @overload(QPen, QPainter.RenderHints)
  def setPen(self, pen: QPen, hints: QPainter.RenderHints) -> None:
    """
    Calls Qt's 'void QPdf::Stroker::setPen(const QPen &pen,
    QPainter::RenderHints hints)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-stroker.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.

    hints : QPainter.RenderHints
      Passed on as its number.
    """
    #  void QPdf::Stroker::setPen(const QPen &pen, QPainter::RenderHints
    #      hints)
    self.uglySide.call(
        'ritual_ZN4QPdf7Stroker6setPenERK4QPen6QFlagsIN8QPainter10RenderHin'
        'tEE',
        self._valueOf(pen), hints.value,
    )

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
    Qt's 'QPdf::Stroker::Stroker()': leans on
    'QPdf::ByteStream::operator<<(char const*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QPdf.Stroker.__init__' has no cute function yet. Qt's "
        "'QPdf::Stroker::Stroker()': leans on "
        "'QPdf::ByteStream::operator<<(char const*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  @staticmethod
  def strokePath(*__, **_) -> Never:
    """
    Qt's 'void QPdf::Stroker::strokePath(const QPainterPath &path)': leans on
    'QPdf::ByteStream::operator<<(char const*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QPdf.Stroker.strokePath' has no cute function yet. Qt's 'void "
        "QPdf::Stroker::strokePath(const QPainterPath &path)': leans on "
        "'QPdf::ByteStream::operator<<(char const*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
