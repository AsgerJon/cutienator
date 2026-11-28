"""
QGridLayoutRowData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGridLayoutRowData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QGridLayoutBox


class QGridLayoutRowData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGridLayoutRowData: a plain Python object standing in
  front of one C++ QGridLayoutRowData.

  C++ hands a QGridLayoutRowData around as a copy, so every C++
  QGridLayoutRowData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGridLayoutRowData that has a ritual and that Python
  can call so far, 2 names in all: 'reset', 'totalBox'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QGridLayoutRowData::stealBox(int start, int end, int which,
    qreal *positions, qreal *sizes)': takes a number to change where it is.
  - Qt's 'QGridLayoutRowData::~QGridLayoutRowData()': the destructor: Python
    removes its C++ QGridLayoutRowData by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QGridLayoutRowData.

  What to expect
  --------------

  - The C++ QGridLayoutRowData is created at the first use, not by
    'QGridLayoutRowData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGridLayoutRowData back gives a copy the ritual made
    for Python, in a new cute QGridLayoutRowData.
  - Each name of Qt's QGridLayoutRowData that has no cute function yet,
    'calculateGeometries', 'distributeMultiCells', 'stealBox', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGridLayoutRowData'

  #  Qt's '~QGridLayoutRowData()'. Naming it makes this a value class: Python
  #  owns every C++ QGridLayoutRowData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QGridLayoutRowDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def totalBox(self, start: int, end: int) -> QGridLayoutBox:
    """
    Calls Qt's 'QGridLayoutBox QGridLayoutRowData::totalBox(int start, int
    end) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutrowdata.html#totalBox

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    Returns
    -------

    QGridLayoutBox
      A new cute QGridLayoutBox around the copy Qt gave back. Python owns it.
    """
    #  QGridLayoutBox QGridLayoutRowData::totalBox(int start, int end) const
    address = self.uglySide.call(
        'ritual_ZNK18QGridLayoutRowData8totalBoxEii', start, end,
    )
    from . import QGridLayoutBox
    return QGridLayoutBox._cuteOwning(address)

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

  @overload(int)
  def reset(self, count: int) -> None:
    """
    Calls Qt's 'void QGridLayoutRowData::reset(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutrowdata.html#reset

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QGridLayoutRowData::reset(int count)
    self.uglySide.call('ritual_ZN18QGridLayoutRowData5resetEi', count)

  @staticmethod
  def calculateGeometries(*__, **_) -> Never:
    """
    Qt's 'void QGridLayoutRowData::calculateGeometries(int start, int end,
    qreal targetSize, qreal *positions, qreal *sizes, qreal *descents, const
    QGridLayoutBox &totalBox, const QGridLayoutRowInfo &rowInfo, bool
    snapToPixelGrid)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'LAYOUTITEMSIZE_MAX'; did you mean 'QLAYOUTSIZE_MAX'?.
    """
    raise NotImplementedError(
        "'QGridLayoutRowData.calculateGeometries' has no cute function yet. "
        "Qt's 'void QGridLayoutRowData::calculateGeometries(int start, int "
        "end, qreal targetSize, qreal *positions, qreal *sizes, qreal "
        "*descents, const QGridLayoutBox &totalBox, const "
        "QGridLayoutRowInfo &rowInfo, bool snapToPixelGrid)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'LAYOUTITEMSIZE_MAX'; did you mean 'QLAYOUTSIZE_MAX'?.")

  @staticmethod
  def distributeMultiCells(*__, **_) -> Never:
    """
    Qt's 'void QGridLayoutRowData::distributeMultiCells(const
    QGridLayoutRowInfo &rowInfo, bool snapToPixelGrid)': leans on
    'QGridLayoutRowData::calculateGeometries(int, int, double, double*,
    double*, double*, QGridLayoutBox const&, QGridLayoutRowInfo const&,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGridLayoutRowData.distributeMultiCells' has no cute function "
        "yet. Qt's 'void QGridLayoutRowData::distributeMultiCells(const "
        "QGridLayoutRowInfo &rowInfo, bool snapToPixelGrid)': leans on "
        "'QGridLayoutRowData::calculateGeometries(int, int, double, "
        "double*, double*, double*, QGridLayoutBox const&, "
        "QGridLayoutRowInfo const&, bool)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def stealBox(*__, **_) -> Never:
    """
    Qt's 'void QGridLayoutRowData::stealBox(int start, int end, int which,
    qreal *positions, qreal *sizes)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QGridLayoutRowData.stealBox' has no cute function yet. Qt's 'void "
        "QGridLayoutRowData::stealBox(int start, int end, int which, qreal "
        "*positions, qreal *sizes)': takes a number to change where it is.")
