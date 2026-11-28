"""
QPainterClipInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPainterClipInfo to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRect, QRectF
  from . import QPainterPath, QRegion, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']
  QTransform = WAIT['QTransform']


class QPainterClipInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPainterClipInfo: a plain Python object standing in
  front of one C++ QPainterClipInfo.

  C++ hands a QPainterClipInfo around as a copy, so every C++
  QPainterClipInfo behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QPainterClipInfo yet. It can be made from Python, in 5
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPainterClipInfo::~QPainterClipInfo()': the destructor: Python
    removes its C++ QPainterClipInfo by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPainterClipInfo is created at the first use, not by
    'QPainterClipInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPainterClipInfo back gives a copy the ritual made
    for Python, in a new cute QPainterClipInfo.
  """

  #  The enums Qt writes inside QPainterClipInfo, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ClipType(CuteNum):
    """
    The enum 'QPainterClipInfo::ClipType' of Qt, with the 4 names Qt gives in
    it.
    """

    RegionClip = Kee[int](0)
    PathClip = Kee[int](1)
    RectClip = Kee[int](2)
    RectFClip = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainterClipInfo'

  #  Qt's '~QPainterClipInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QPainterClipInfo behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QPainterClipInfoD1Ev'

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
    Notes what was given, for Qt's 'QPainterClipInfo::QPainterClipInfo()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterclipinfo.html#QPainterClipInfo
    """
    #  QPainterClipInfo::QPainterClipInfo()
    self._noteCreation(QPainterClipInfo, lambda: Rituals.call(
        'ritual_ZN16QPainterClipInfoC1Ev',
    ))

  @overload(QPainterPath, Qt.ClipOperation, QTransform)
  def __init__(
      self,
      p: QPainterPath,
      op: Qt.ClipOperation,
      m: QTransform,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPainterClipInfo::QPainterClipInfo(const
    QPainterPath &p, Qt::ClipOperation op, const QTransform &m)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterclipinfo.html#QPainterClipInfo

    Parameters
    ----------

    p : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    op : Qt.ClipOperation
      Passed on as its number.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QPainterClipInfo::QPainterClipInfo(const QPainterPath &p,
    #      Qt::ClipOperation op, const QTransform &m)
    self._noteCreation(QPainterClipInfo, lambda: Rituals.call(
        'ritual_ZN16QPainterClipInfoC1ERK12QPainterPathN2Qt13ClipOperationE'
        'RK10QTransform',
        self._valueOf(p), op.value, self._valueOf(m),
    ))

  @overload(QRegion, Qt.ClipOperation, QTransform)
  def __init__(
      self,
      r: QRegion,
      op: Qt.ClipOperation,
      m: QTransform,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPainterClipInfo::QPainterClipInfo(const
    QRegion &r, Qt::ClipOperation op, const QTransform &m)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterclipinfo.html#QPainterClipInfo

    Parameters
    ----------

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    op : Qt.ClipOperation
      Passed on as its number.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QPainterClipInfo::QPainterClipInfo(const QRegion &r, Qt::ClipOperation
    #      op, const QTransform &m)
    self._noteCreation(QPainterClipInfo, lambda: Rituals.call(
        'ritual_ZN16QPainterClipInfoC1ERK7QRegionN2Qt13ClipOperationERK10QT'
        'ransform',
        self._valueOf(r), op.value, self._valueOf(m),
    ))

  @overload(QRect, Qt.ClipOperation, QTransform)
  def __init__(self, r: QRect, op: Qt.ClipOperation, m: QTransform) -> None:
    """
    Notes what was given, for Qt's 'QPainterClipInfo::QPainterClipInfo(const
    QRect &r, Qt::ClipOperation op, const QTransform &m)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterclipinfo.html#QPainterClipInfo

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    op : Qt.ClipOperation
      Passed on as its number.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QPainterClipInfo::QPainterClipInfo(const QRect &r, Qt::ClipOperation
    #      op, const QTransform &m)
    self._noteCreation(QPainterClipInfo, lambda: Rituals.call(
        'ritual_ZN16QPainterClipInfoC1ERK5QRectN2Qt13ClipOperationERK10QTra'
        'nsform',
        self._valueOf(r), op.value, self._valueOf(m),
    ))

  @overload(QRectF, Qt.ClipOperation, QTransform)
  def __init__(self, r: QRectF, op: Qt.ClipOperation, m: QTransform) -> None:
    """
    Notes what was given, for Qt's 'QPainterClipInfo::QPainterClipInfo(const
    QRectF &r, Qt::ClipOperation op, const QTransform &m)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterclipinfo.html#QPainterClipInfo

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    op : Qt.ClipOperation
      Passed on as its number.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QPainterClipInfo::QPainterClipInfo(const QRectF &r, Qt::ClipOperation
    #      op, const QTransform &m)
    self._noteCreation(QPainterClipInfo, lambda: Rituals.call(
        'ritual_ZN16QPainterClipInfoC1ERK6QRectFN2Qt13ClipOperationERK10QTr'
        'ansform',
        self._valueOf(r), op.value, self._valueOf(m),
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
