"""
QPathClipper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPathClipper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from . import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPathClipper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPathClipper: a plain Python object standing in front
  of one C++ QPathClipper.

  What exists
  -----------

  Every function of Qt's QPathClipper that has a ritual and that Python can
  call so far, 4 names in all: 'clip', 'intersect', 'contains', 'pathToRect'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QPathClipper::handleCrossingEdges(QWingedEdge &list, qreal y,
    ClipperMode mode)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QPathClipper::doClip(QWingedEdge &list, ClipperMode mode)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPathClipper is created at the first use, not by
    'QPathClipper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPathClipper.
  - Each name of Qt's QPathClipper that has no cute function yet, 'doClip',
    'handleCrossingEdges', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPathClipper, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Operation(CuteNum):
    """
    The enum 'QPathClipper::Operation' of Qt, with the 4 names Qt gives in
    it.
    """

    BoolAnd = Kee[int](0)
    BoolOr = Kee[int](1)
    BoolSub = Kee[int](2)
    Simplify = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPainterPath)
  @overload(QPainterPath, QRectF)
  @overload(QPainterPath, NoneType)
  def pathToRect(path: QPainterPath, rect: Optional[QRectF] = None) -> bool:
    """
    Calls Qt's 'bool QPathClipper::pathToRect(const QPainterPath &path,
    QRectF *rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpathclipper.html#pathToRect

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    rect : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QPathClipper::pathToRect(const QPainterPath &path, QRectF *rect)
    return Rituals.call(
        'ritual_ZN12QPathClipper10pathToRectERK12QPainterPathP6QRectF',
        CuteMixin._valueOf(path), CuteMixin._addressOf(rect),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPathClipper'

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

  @overload(QPainterPath, QPainterPath)
  def __init__(self, subject: QPainterPath, clip: QPainterPath) -> None:
    """
    Notes what was given, for Qt's 'QPathClipper::QPathClipper(const
    QPainterPath &subject, const QPainterPath &clip)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qpathclipper.html#QPathClipper

    Parameters
    ----------

    subject : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    clip : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  QPathClipper::QPathClipper(const QPainterPath &subject, const
    #      QPainterPath &clip)
    self._noteCreation(QPathClipper, lambda: Rituals.call(
        'ritual_ZN12QPathClipperC1ERK12QPainterPathS2_',
        self._valueOf(subject), self._valueOf(clip),
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

  @overload()
  @overload(Operation)
  def clip(self, op: Operation = Operation.BoolAnd) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPathClipper::clip(Operation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpathclipper.html#clip

    Parameters
    ----------

    op : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.BoolAnd.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPathClipper::clip(Operation op)
    address = self.uglySide.call(
        'ritual_ZN12QPathClipper4clipENS_9OperationE', op.value,
    )
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload()
  def intersect(self) -> bool:
    """
    Calls Qt's 'bool QPathClipper::intersect()'.

    Qt's own words: https://doc.qt.io/qt-6/qpathclipper.html#intersect
    """
    #  bool QPathClipper::intersect()
    return self.uglySide.call('ritual_ZN12QPathClipper9intersectEv')

  @staticmethod
  @overload(QPainterPath, QRectF)
  def intersect(path: QPainterPath, rect: QRectF) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPathClipper::intersect(const QPainterPath
    &path, const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpathclipper.html#intersect

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPathClipper::intersect(const QPainterPath &path, const
    #      QRectF &rect)
    address = Rituals.call(
        'ritual_ZN12QPathClipper9intersectERK12QPainterPathRK6QRectF',
        CuteMixin._valueOf(path), CuteMixin._valueOf(rect),
    )
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  def contains(self) -> bool:
    """
    Calls Qt's 'bool QPathClipper::contains()'.

    Qt's own words: https://doc.qt.io/qt-6/qpathclipper.html#contains
    """
    #  bool QPathClipper::contains()
    return self.uglySide.call('ritual_ZN12QPathClipper8containsEv')

  @staticmethod
  def doClip(*__, **_) -> Never:
    """
    Qt's 'bool QPathClipper::doClip(QWingedEdge &list, ClipperMode mode)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPathClipper.doClip' has no cute function yet. Qt's 'bool "
        "QPathClipper::doClip(QWingedEdge &list, ClipperMode mode)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def handleCrossingEdges(*__, **_) -> Never:
    """
    Qt's 'bool QPathClipper::handleCrossingEdges(QWingedEdge &list, qreal y,
    ClipperMode mode)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPathClipper.handleCrossingEdges' has no cute function yet. Qt's "
        "'bool QPathClipper::handleCrossingEdges(QWingedEdge &list, qreal "
        "y, ClipperMode mode)': takes a type Python has no way to hand over "
        "yet.")
