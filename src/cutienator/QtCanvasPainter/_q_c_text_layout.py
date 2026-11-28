"""
QCTextLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qctextlayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCTextLayout to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QTextOption
from . import QCanvasPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF
  from ..QtGui import QFontMetricsF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFontMetricsF = WAIT['QFontMetricsF']
  QRectF = WAIT['QRectF']


class QCTextLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCTextLayout: a plain Python object standing in front
  of one C++ QCTextLayout.

  C++ hands a QCTextLayout around as a copy, so every C++ QCTextLayout behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCTextLayout that has a ritual and that Python can
  call so far, 4 names in all: 'convertToQtWrapMode', 'convertToQtAlignment',
  'calculateVerticalAlignment', 'convertToQtDirection'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::pair<float, float>
    QCTextLayout::calculateHorizontalAlignment(QCanvasPainter::TextAlign
    align, const QRectF &rect, float layoutWidth, const QRectF &layoutRect)':
    gives a type Python has no way to take yet.
  - Qt's 'QCTextLayout::~QCTextLayout()': the destructor: Python removes its
    C++ QCTextLayout by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCTextLayout is created at the first use, not by
    'QCTextLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCTextLayout back gives a copy the ritual made for
    Python, in a new cute QCTextLayout.
  - Each name of Qt's QCTextLayout that has no cute function yet,
    'calculateHorizontalAlignment', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanvasPainter.WrapMode)
  def convertToQtWrapMode(
      mode: QCanvasPainter.WrapMode,
  ) -> QTextOption.WrapMode:
    """
    Calls Qt's 'QTextOption::WrapMode
    QCTextLayout::convertToQtWrapMode(QCanvasPainter::WrapMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qctextlayout.html#convertToQtWrapMode

    Parameters
    ----------

    mode : QCanvasPainter.WrapMode
      Passed on as its number.

    Returns
    -------

    QTextOption.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextOption.WrapMode(number)' gives.
    """
    #  QTextOption::WrapMode
    #      QCTextLayout::convertToQtWrapMode(QCanvasPainter::WrapMode mode)
    return QTextOption.WrapMode(Rituals.call(
        'ritual_ZN12QCTextLayout19convertToQtWrapModeEN14QCanvasPainter8Wra'
        'pModeE',
        mode.value,
    ))

  @staticmethod
  @overload(QCanvasPainter.TextAlign)
  def convertToQtAlignment(
      alignment: QCanvasPainter.TextAlign,
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment
    QCTextLayout::convertToQtAlignment(QCanvasPainter::TextAlign alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qctextlayout.html#convertToQtAlignment

    Parameters
    ----------

    alignment : QCanvasPainter.TextAlign
      Passed on as its number.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment
    #      QCTextLayout::convertToQtAlignment(QCanvasPainter::TextAlign
    #      alignment)
    return Qt.Alignment(Rituals.call(
        'ritual_ZN12QCTextLayout20convertToQtAlignmentEN14QCanvasPainter9Te'
        'xtAlignE',
        alignment.value,
    ))

  @staticmethod
  @overload(QCanvasPainter.TextBaseline, QRectF, QFontMetricsF, QRectF)
  def calculateVerticalAlignment(
      baseline: QCanvasPainter.TextBaseline,
      rect: QRectF,
      metrics: QFontMetricsF,
      layoutRect: QRectF,
  ) -> float:
    """
    Calls Qt's 'float
    QCTextLayout::calculateVerticalAlignment(QCanvasPainter::TextBaseline
    baseline, const QRectF &rect, const QFontMetricsF &metrics, const QRectF
    &layoutRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qctextlayout.html#calculateVerticalAlignment

    Parameters
    ----------

    baseline : QCanvasPainter.TextBaseline
      Passed on as its number.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    metrics : QFontMetricsF
      Passed on as a value: Qt reads the C++ QFontMetricsF, which stays
      Python's own.

    layoutRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  float QCTextLayout::calculateVerticalAlignment(QCanvasPainter::
    #      TextBaseline baseline, const QRectF &rect, const QFontMetricsF
    #      &metrics, const QRectF &layoutRect)
    return Rituals.call(
        'ritual_ZN12QCTextLayout26calculateVerticalAlignmentEN14QCanvasPain'
        'ter12TextBaselineERK6QRectFRK13QFontMetricsFS4_',
        baseline.value, CuteMixin._valueOf(rect),
        CuteMixin._valueOf(metrics), CuteMixin._valueOf(layoutRect),
    )

  @staticmethod
  @overload(QCanvasPainter.TextDirection)
  def convertToQtDirection(
      direction: QCanvasPainter.TextDirection,
  ) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection
    QCTextLayout::convertToQtDirection(QCanvasPainter::TextDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qctextlayout.html#convertToQtDirection

    Parameters
    ----------

    direction : QCanvasPainter.TextDirection
      Passed on as its number.

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection
    #      QCTextLayout::convertToQtDirection(QCanvasPainter::TextDirection
    #      direction)
    return Qt.LayoutDirection(Rituals.call(
        'ritual_ZN12QCTextLayout20convertToQtDirectionEN14QCanvasPainter13T'
        'extDirectionE',
        direction.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCTextLayout'

  #  Qt's '~QCTextLayout()'. Naming it makes this a value class: Python owns
  #  every C++ QCTextLayout behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QCTextLayoutD1Ev'

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

  @staticmethod
  def calculateHorizontalAlignment(*__, **_) -> Never:
    """
    Qt's 'std::pair<float, float>
    QCTextLayout::calculateHorizontalAlignment(QCanvasPainter::TextAlign
    align, const QRectF &rect, float layoutWidth, const QRectF &layoutRect)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCTextLayout.calculateHorizontalAlignment' has no cute function "
        "yet. Qt's 'std::pair<float, float> "
        "QCTextLayout::calculateHorizontalAlignment(QCanvasPainter::TextAlig"
        "n align, const QRectF &rect, float layoutWidth, const QRectF "
        "&layoutRect)': gives a type Python has no way to take yet.")
