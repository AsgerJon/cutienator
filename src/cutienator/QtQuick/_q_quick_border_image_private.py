"""
QQuickBorderImagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickborderimage_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickBorderImagePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickImageBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSize, QSizeF
  from . import QQuickBorderImage, QQuickScaleGrid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickScaleGrid = WAIT['QQuickScaleGrid']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBorderImagePrivate(QQuickImageBasePrivate):
  """
  The cute side of Qt's QQuickBorderImagePrivate: a plain Python object
  standing in front of one C++ QQuickBorderImagePrivate.

  It is built on the cute 'QQuickImageBasePrivate', as Qt's
  QQuickBorderImagePrivate is built on Qt's QQuickImageBasePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickBorderImagePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'getScaleGrid',
  'calculateRects'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickBorderImage *QQuickBorderImagePrivate::q_func() const':
    takes in Python what 'QQuickBorderImage
    *QQuickBorderImagePrivate::q_func()' takes.
  - Qt's 'QQuickBorderImagePrivate::~QQuickBorderImagePrivate()': the
    destructor: Python never removes a C++ QQuickBorderImagePrivate.

  What to expect
  --------------

  - The C++ QQuickBorderImagePrivate is created at the first use, not by
    'QQuickBorderImagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBorderImagePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, QRectF,
      QRectF, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, QRectF,
      QRectF, NoneType,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, QRectF,
      NoneType, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, QRectF,
      NoneType, NoneType,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, NoneType,
      QRectF, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, NoneType,
      QRectF, NoneType,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, NoneType,
      NoneType, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, QRectF, NoneType,
      NoneType, NoneType,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, QRectF,
      QRectF, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, QRectF,
      QRectF, NoneType,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, QRectF,
      NoneType, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, QRectF,
      NoneType, NoneType,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, NoneType,
      QRectF, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, NoneType,
      QRectF, NoneType,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, NoneType,
      NoneType, QRectF,
  )
  @overload(
      QQuickScaleGrid, QSize, QSizeF, int, int, float, NoneType, NoneType,
      NoneType, NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, QRectF, QRectF,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, QRectF, QRectF,
      NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, QRectF, NoneType,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, QRectF, NoneType,
      NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, NoneType, QRectF,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, NoneType, QRectF,
      NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, NoneType, NoneType,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, QRectF, NoneType, NoneType,
      NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, QRectF, QRectF,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, QRectF, QRectF,
      NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, QRectF, NoneType,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, QRectF, NoneType,
      NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, NoneType, QRectF,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, NoneType, QRectF,
      NoneType,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, NoneType, NoneType,
      QRectF,
  )
  @overload(
      NoneType, QSize, QSizeF, int, int, float, NoneType, NoneType, NoneType,
      NoneType,
  )
  def calculateRects(
      border: Optional[QQuickScaleGrid],
      sourceSize: QSize,
      targetSize: QSizeF,
      horizontalTileMode: int,
      verticalTileMode: int,
      devicePixelRatio: float,
      targetRect: Optional[QRectF],
      innerTargetRect: Optional[QRectF],
      innerSourceRect: Optional[QRectF],
      subSourceRect: Optional[QRectF],
  ) -> None:
    """
    Calls Qt's 'void QQuickBorderImagePrivate::calculateRects(const
    QQuickScaleGrid *border, const QSize &sourceSize, const QSizeF
    &targetSize, int horizontalTileMode, int verticalTileMode, qreal
    devicePixelRatio, QRectF *targetRect, QRectF *innerTargetRect, QRectF
    *innerSourceRect, QRectF *subSourceRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimageprivate.html#calculateRects

    Parameters
    ----------

    border : Optional[QQuickScaleGrid]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    targetSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    horizontalTileMode : int
      Passed on as it is.

    verticalTileMode : int
      Passed on as it is.

    devicePixelRatio : float
      Passed on as it is.

    targetRect : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    innerTargetRect : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    innerSourceRect : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    subSourceRect : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBorderImagePrivate::calculateRects(const QQuickScaleGrid
    #      *border, const QSize &sourceSize, const QSizeF &targetSize, int
    #      horizontalTileMode, int verticalTileMode, qreal devicePixelRatio,
    #      QRectF *targetRect, QRectF *innerTargetRect, QRectF
    #      *innerSourceRect, QRectF *subSourceRect)
    Rituals.call(
        'ritual_ZN24QQuickBorderImagePrivate14calculateRectsEPK15QQuickScal'
        'eGridRK5QSizeRK6QSizeFiidP6QRectFSA_SA_SA_',
        CuteMixin._addressOf(border), CuteMixin._valueOf(sourceSize),
        CuteMixin._valueOf(targetSize), horizontalTileMode, verticalTileMode,
        devicePixelRatio, CuteMixin._addressOf(targetRect),
        CuteMixin._addressOf(innerTargetRect),
        CuteMixin._addressOf(innerSourceRect),
        CuteMixin._addressOf(subSourceRect),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBorderImagePrivate'

  #  A C++ QQuickBorderImagePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickBorderImagePrivate'

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
    'QQuickBorderImagePrivate::QQuickBorderImagePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimageprivate.html
    """
    #  QQuickBorderImagePrivate::QQuickBorderImagePrivate()
    self._noteCreation(QQuickBorderImagePrivate, lambda: Rituals.call(
        'ritual_ZN24QQuickBorderImagePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickBorderImage]:
    """
    Calls Qt's 'QQuickBorderImage *QQuickBorderImagePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimageprivate.html#q_func

    Returns
    -------

    Optional[QQuickBorderImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickBorderImage *QQuickBorderImagePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickBorderImagePrivate6q_funcEv',
    )
    from . import QQuickBorderImage
    return QQuickBorderImage._cuteAt(address)

  def getScaleGrid(self) -> Optional[QQuickScaleGrid]:
    """
    Calls Qt's 'QQuickScaleGrid *QQuickBorderImagePrivate::getScaleGrid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimageprivate.html#getScaleGrid

    Returns
    -------

    Optional[QQuickScaleGrid]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScaleGrid *QQuickBorderImagePrivate::getScaleGrid()
    address = self.uglySide.call(
        'ritual_ZN24QQuickBorderImagePrivate12getScaleGridEv',
    )
    from . import QQuickScaleGrid
    return QQuickScaleGrid._cuteAt(address)
