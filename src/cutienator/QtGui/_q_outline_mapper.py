"""
QOutlineMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qoutlinemapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOutlineMapper to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPointF, QRect
  from . import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QTransform = WAIT['QTransform']


class QOutlineMapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOutlineMapper: a plain Python object standing in
  front of one C++ QOutlineMapper.

  What exists
  -----------

  Every function of Qt's QOutlineMapper that has a ritual and that Python can
  call so far, 8 names in all: 'setMatrix', 'setClipRect', 'beginOutline',
  'endOutline', 'moveTo', 'lineTo', 'curveTo', 'closeSubpath'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOutlineMapper::clipElements(const QPointF *points, const
    QPainterPath::ElementType *types, int count)': names
    'QPainterPath::ElementType', which has no cute class yet.
  - Qt's 'QT_FT_Outline *QOutlineMapper::outline()': gives 'struct
    QT_FT_Outline_', which has no cute class yet.
  - Qt's 'QT_FT_Outline *QOutlineMapper::convertPath(const QPainterPath
    &path)': gives 'struct QT_FT_Outline_', which has no cute class yet.
  - Qt's 'QT_FT_Outline *QOutlineMapper::convertPath(const QVectorPath
    &path)': takes a type Python has no way to hand over yet.
  - Qt's 'QPainterPath::ElementType *QOutlineMapper::elementTypes() const':
    gives 'QPainterPath::ElementType', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 15 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QOutlineMapper is created at the first use, not by
    'QOutlineMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOutlineMapper.
  - Each name of Qt's QOutlineMapper that has no cute function yet,
    'clipElements', 'convertElements', 'convertPath', 'elementTypes',
    'outline', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOutlineMapper'

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

  @overload(QTransform)
  def setMatrix(self, m: QTransform) -> None:
    """
    Calls Qt's 'void QOutlineMapper::setMatrix(const QTransform &m)'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#setMatrix

    Parameters
    ----------

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QOutlineMapper::setMatrix(const QTransform &m)
    self.uglySide.call(
        'ritual_ZN14QOutlineMapper9setMatrixERK10QTransform',
        self._valueOf(m),
    )

  @overload(QRect)
  def setClipRect(self, clipRect: QRect) -> None:
    """
    Calls Qt's 'void QOutlineMapper::setClipRect(QRect clipRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#setClipRect

    Parameters
    ----------

    clipRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QOutlineMapper::setClipRect(QRect clipRect)
    self.uglySide.call(
        'ritual_ZN14QOutlineMapper11setClipRectE5QRect',
        self._valueOf(clipRect),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOutlineMapper::QOutlineMapper()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#QOutlineMapper
    """
    #  QOutlineMapper::QOutlineMapper()
    self._noteCreation(QOutlineMapper, lambda: Rituals.call(
        'ritual_ZN14QOutlineMapperC1Ev',
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

  @overload(Qt.FillRule)
  def beginOutline(self, fillRule: Qt.FillRule) -> None:
    """
    Calls Qt's 'void QOutlineMapper::beginOutline(Qt::FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#beginOutline

    Parameters
    ----------

    fillRule : Qt.FillRule
      Passed on as its number.
    """
    #  void QOutlineMapper::beginOutline(Qt::FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN14QOutlineMapper12beginOutlineEN2Qt8FillRuleE',
        fillRule.value,
    )

  def endOutline(self) -> None:
    """
    Calls Qt's 'void QOutlineMapper::endOutline()'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#endOutline
    """
    #  void QOutlineMapper::endOutline()
    self.uglySide.call('ritual_ZN14QOutlineMapper10endOutlineEv')

  @overload(QPointF)
  def moveTo(self, pt: QPointF) -> None:
    """
    Calls Qt's 'void QOutlineMapper::moveTo(const QPointF &pt)'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#moveTo

    Parameters
    ----------

    pt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QOutlineMapper::moveTo(const QPointF &pt)
    self.uglySide.call(
        'ritual_ZN14QOutlineMapper6moveToERK7QPointF',
        self._valueOf(pt, 'QPointF'),
    )

  @overload(QPointF)
  def lineTo(self, pt: QPointF) -> None:
    """
    Calls Qt's 'void QOutlineMapper::lineTo(const QPointF &pt)'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#lineTo

    Parameters
    ----------

    pt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QOutlineMapper::lineTo(const QPointF &pt)
    self.uglySide.call(
        'ritual_ZN14QOutlineMapper6lineToERK7QPointF',
        self._valueOf(pt, 'QPointF'),
    )

  @overload(QPointF, QPointF, QPointF)
  def curveTo(self, cp1: QPointF, cp2: QPointF, ep: QPointF) -> None:
    """
    Calls Qt's 'void QOutlineMapper::curveTo(const QPointF &cp1, const
    QPointF &cp2, const QPointF &ep)'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#curveTo

    Parameters
    ----------

    cp1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    cp2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ep : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QOutlineMapper::curveTo(const QPointF &cp1, const QPointF &cp2,
    #      const QPointF &ep)
    self.uglySide.call(
        'ritual_ZN14QOutlineMapper7curveToERK7QPointFS2_S2_',
        self._valueOf(cp1, 'QPointF'), self._valueOf(cp2, 'QPointF'),
        self._valueOf(ep, 'QPointF'),
    )

  def closeSubpath(self) -> None:
    """
    Calls Qt's 'void QOutlineMapper::closeSubpath()'.

    Qt's own words: https://doc.qt.io/qt-6/qoutlinemapper.html#closeSubpath
    """
    #  void QOutlineMapper::closeSubpath()
    self.uglySide.call('ritual_ZN14QOutlineMapper12closeSubpathEv')

  @staticmethod
  def clipElements(*__, **_) -> Never:
    """
    Qt's 'void QOutlineMapper::clipElements(const QPointF *points, const
    QPainterPath::ElementType *types, int count)': names
    'QPainterPath::ElementType', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOutlineMapper.clipElements' has no cute function yet. Qt's 'void "
        "QOutlineMapper::clipElements(const QPointF *points, const "
        "QPainterPath::ElementType *types, int count)': names "
        "'QPainterPath::ElementType', which has no cute class yet.")

  @staticmethod
  def convertElements(*__, **_) -> Never:
    """
    Qt's 'void QOutlineMapper::convertElements(const QPointF *points, const
    QPainterPath::ElementType *types, int count)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'qreal_to_fixed_26_6'.
    """
    raise NotImplementedError(
        "'QOutlineMapper.convertElements' has no cute function yet. Qt's "
        "'void QOutlineMapper::convertElements(const QPointF *points, const "
        "QPainterPath::ElementType *types, int count)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qreal_to_fixed_26_6'.")

  @staticmethod
  def convertPath(*__, **_) -> Never:
    """
    - Qt's 'QT_FT_Outline *QOutlineMapper::convertPath(const QPainterPath
      &path)': gives 'struct QT_FT_Outline_', which has no cute class yet.
    - Qt's 'QT_FT_Outline *QOutlineMapper::convertPath(const QVectorPath
      &path)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOutlineMapper.convertPath' has no cute function yet. Qt's "
        "'QT_FT_Outline *QOutlineMapper::convertPath(const QPainterPath "
        "&path)': gives 'struct QT_FT_Outline_', which has no cute class "
        "yet. Qt's 'QT_FT_Outline *QOutlineMapper::convertPath(const "
        "QVectorPath &path)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def elementTypes(*__, **_) -> Never:
    """
    Qt's 'QPainterPath::ElementType *QOutlineMapper::elementTypes() const':
    gives 'QPainterPath::ElementType', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOutlineMapper.elementTypes' has no cute function yet. Qt's "
        "'QPainterPath::ElementType *QOutlineMapper::elementTypes() const': "
        "gives 'QPainterPath::ElementType', which has no cute class yet.")

  @staticmethod
  def outline(*__, **_) -> Never:
    """
    Qt's 'QT_FT_Outline *QOutlineMapper::outline()': gives 'struct
    QT_FT_Outline_', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOutlineMapper.outline' has no cute function yet. Qt's "
        "'QT_FT_Outline *QOutlineMapper::outline()': gives 'struct "
        "QT_FT_Outline_', which has no cute class yet.")
