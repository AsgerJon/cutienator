"""
QWidgetPaintContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QWidgetPaintContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from ..QtGui import QPaintDevice, QPainter, QRegion
  from . import QWidgetRepaintManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintDevice = WAIT['QPaintDevice']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QRegion = WAIT['QRegion']
  QWidgetRepaintManager = WAIT['QWidgetRepaintManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetPaintContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWidgetPaintContext: a plain Python object standing
  in front of one C++ QWidgetPaintContext.

  C++ hands a QWidgetPaintContext around as a copy, so every C++
  QWidgetPaintContext behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QWidgetPaintContext yet. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetPaintContext::~QWidgetPaintContext()': the destructor:
    Python removes its C++ QWidgetPaintContext by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QWidgetPaintContext is created at the first use, not by
    'QWidgetPaintContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWidgetPaintContext back gives a copy the ritual made
    for Python, in a new cute QWidgetPaintContext.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetPaintContext'

  #  Qt's '~QWidgetPaintContext()'. Naming it makes this a value class:
  #  Python owns every C++ QWidgetPaintContext behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QWidgetPaintContextD1Ev'

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

  @overload(
      QPaintDevice, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags,
      QPainter, QWidgetRepaintManager,
  )
  @overload(
      QPaintDevice, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags,
      QPainter, NoneType,
  )
  @overload(
      QPaintDevice, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags,
      NoneType, QWidgetRepaintManager,
  )
  @overload(
      QPaintDevice, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags,
      NoneType, NoneType,
  )
  @overload(
      NoneType, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags, QPainter,
      QWidgetRepaintManager,
  )
  @overload(
      NoneType, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags, QPainter,
      NoneType,
  )
  @overload(
      NoneType, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags, NoneType,
      QWidgetRepaintManager,
  )
  @overload(
      NoneType, QRegion, QPoint, QWidgetPrivate.DrawWidgetFlags, NoneType,
      NoneType,
  )
  def __init__(
      self,
      d: Optional[QPaintDevice],
      r: QRegion,
      o: QPoint,
      f: QWidgetPrivate.DrawWidgetFlags,
      p: Optional[QPainter],
      rpm: Optional[QWidgetRepaintManager],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWidgetPaintContext::QWidgetPaintContext(QPaintDevice *d, const QRegion
    &r, const QPoint &o, QWidgetPrivate::DrawWidgetFlags f, QPainter *p,
    QWidgetRepaintManager *rpm)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetpaintcontext.html#QWidgetPaintContext

    Parameters
    ----------

    d : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    o : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    f : QWidgetPrivate.DrawWidgetFlags
      Passed on as its number.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rpm : Optional[QWidgetRepaintManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWidgetPaintContext::QWidgetPaintContext(QPaintDevice *d, const
    #      QRegion &r, const QPoint &o, QWidgetPrivate::DrawWidgetFlags f,
    #      QPainter *p, QWidgetRepaintManager *rpm)
    self._noteCreation(QWidgetPaintContext, lambda: Rituals.call(
        'ritual_ZN19QWidgetPaintContextC1EP12QPaintDeviceRK7QRegionRK6QPoin'
        't6QFlagsIN14QWidgetPrivate14DrawWidgetFlagEEP8QPainterP21QWidgetRe'
        'paintManager',
        self._addressOf(d, 'QPaintDevice'), self._valueOf(r),
        self._valueOf(o), f.value, self._addressOf(p), self._addressOf(rpm),
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
