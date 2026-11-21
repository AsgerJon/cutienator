"""
QStylePainter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstylepainter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QPainter, QPalette
from . import QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from ..QtGui import QPaintDevice, QPixmap
  from . import QStyleOption, QStyleOptionComplex, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintDevice = WAIT['QPaintDevice']
  QPixmap = WAIT['QPixmap']
  QRect = WAIT['QRect']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStylePainter(QPainter):
  """
  The cute side of Qt's QStylePainter: a plain Python object standing in
  front of one C++ QStylePainter.

  It is built on the cute 'QPainter', as Qt's QStylePainter is built on Qt's
  QPainter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStylePainter that has a ritual and that Python can
  call so far, 7 names in all: 'begin', 'drawPrimitive', 'drawControl',
  'drawComplexControl', 'drawItemText', 'drawItemPixmap', 'style'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QStylePainter is created at the first use, not by
    'QStylePainter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStylePainter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStylePainter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def style(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QStylePainter::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QStylePainter::style() const
    address = self.uglySide.call('ritual_ZNK13QStylePainter5styleEv')
    return QStyle._cuteAt(address)

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
    Notes what was given, for Qt's 'QStylePainter::QStylePainter()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#QStylePainter
    """
    #  QStylePainter::QStylePainter()
    self._noteCreation(QStylePainter, lambda: Rituals.call(
        'ritual_ZN13QStylePainterC1Ev',
    ))

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, w: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's 'QStylePainter::QStylePainter(QWidget
    *w)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#QStylePainter

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStylePainter::QStylePainter(QWidget *w)
    self._noteCreation(QStylePainter, lambda: Rituals.call(
        'ritual_ZN13QStylePainterC1EP7QWidget', self._addressOf(w),
    ))

  @overload(QPaintDevice, QWidget)
  @overload(QPaintDevice, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      pd: Optional[QPaintDevice],
      w: Optional[QWidget],
  ) -> None:
    """
    Notes what was given, for Qt's 'QStylePainter::QStylePainter(QPaintDevice
    *pd, QWidget *w)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#QStylePainter

    Parameters
    ----------

    pd : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStylePainter::QStylePainter(QPaintDevice *pd, QWidget *w)
    self._noteCreation(QStylePainter, lambda: Rituals.call(
        'ritual_ZN13QStylePainterC1EP12QPaintDeviceP7QWidget',
        self._addressOf(pd), self._addressOf(w),
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

  @overload(QWidget)
  @overload(NoneType)
  def begin(self, w: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QStylePainter::begin(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#begin

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStylePainter::begin(QWidget *w)
    return self.uglySide.call(
        'ritual_ZN13QStylePainter5beginEP7QWidget', self._addressOf(w),
    )

  @overload(QPaintDevice, QWidget)
  @overload(QPaintDevice, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def begin(self, pd: Optional[QPaintDevice], w: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QStylePainter::begin(QPaintDevice *pd, QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#begin

    Parameters
    ----------

    pd : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStylePainter::begin(QPaintDevice *pd, QWidget *w)
    return self.uglySide.call(
        'ritual_ZN13QStylePainter5beginEP12QPaintDeviceP7QWidget',
        self._addressOf(pd), self._addressOf(w),
    )

  @overload(QStyle.PrimitiveElement, QStyleOption)
  def drawPrimitive(
      self,
      pe: QStyle.PrimitiveElement,
      opt: QStyleOption,
  ) -> None:
    """
    Calls Qt's 'void QStylePainter::drawPrimitive(QStyle::PrimitiveElement
    pe, const QStyleOption &opt)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#drawPrimitive

    Parameters
    ----------

    pe : QStyle.PrimitiveElement
      Passed on as its number.

    opt : QStyleOption
      Passed on as a value: Qt reads the C++ QStyleOption, which stays
      Python's own.
    """
    #  void QStylePainter::drawPrimitive(QStyle::PrimitiveElement pe, const
    #      QStyleOption &opt)
    self.uglySide.call(
        'ritual_ZN13QStylePainter13drawPrimitiveEN6QStyle16PrimitiveElement'
        'ERK12QStyleOption',
        pe.value, self._valueOf(opt),
    )

  @overload(QStyle.ControlElement, QStyleOption)
  def drawControl(
      self,
      ce: QStyle.ControlElement,
      opt: QStyleOption,
  ) -> None:
    """
    Calls Qt's 'void QStylePainter::drawControl(QStyle::ControlElement ce,
    const QStyleOption &opt)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#drawControl

    Parameters
    ----------

    ce : QStyle.ControlElement
      Passed on as its number.

    opt : QStyleOption
      Passed on as a value: Qt reads the C++ QStyleOption, which stays
      Python's own.
    """
    #  void QStylePainter::drawControl(QStyle::ControlElement ce, const
    #      QStyleOption &opt)
    self.uglySide.call(
        'ritual_ZN13QStylePainter11drawControlEN6QStyle14ControlElementERK1'
        '2QStyleOption',
        ce.value, self._valueOf(opt),
    )

  @overload(QStyle.ComplexControl, QStyleOptionComplex)
  def drawComplexControl(
      self,
      cc: QStyle.ComplexControl,
      opt: QStyleOptionComplex,
  ) -> None:
    """
    Calls Qt's 'void QStylePainter::drawComplexControl(QStyle::ComplexControl
    cc, const QStyleOptionComplex &opt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylepainter.html#drawComplexControl

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : QStyleOptionComplex
      Passed on as a value: Qt reads the C++ QStyleOptionComplex, which stays
      Python's own.
    """
    #  void QStylePainter::drawComplexControl(QStyle::ComplexControl cc,
    #      const QStyleOptionComplex &opt)
    self.uglySide.call(
        'ritual_ZN13QStylePainter18drawComplexControlEN6QStyle14ComplexCont'
        'rolERK19QStyleOptionComplex',
        cc.value, self._valueOf(opt),
    )

  @overload(QRect, int, QPalette, bool, str)
  @overload(QRect, int, QPalette, bool, str, QPalette.ColorRole)
  def drawItemText(
      self,
      r: QRect,
      flags: int,
      pal: QPalette,
      enabled: bool,
      text: str,
      textRole: QPalette.ColorRole = QPalette.ColorRole.NoRole,
  ) -> None:
    """
    Calls Qt's 'void QStylePainter::drawItemText(const QRect &r, int flags,
    const QPalette &pal, bool enabled, const QString &text,
    QPalette::ColorRole textRole)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#drawItemText

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    enabled : bool
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    textRole : QPalette.ColorRole
      Passed on as its number. May be left out, as in Qt: it is then
      QPalette.ColorRole.NoRole.
    """
    #  void QStylePainter::drawItemText(const QRect &r, int flags, const
    #      QPalette &pal, bool enabled, const QString &text,
    #      QPalette::ColorRole textRole)
    self.uglySide.call(
        'ritual_ZN13QStylePainter12drawItemTextERK5QRectiRK8QPalettebRK7QSt'
        'ringNS3_9ColorRoleE',
        self._valueOf(r), flags, self._valueOf(pal), enabled, text,
        textRole.value,
    )

  @overload(QRect, int, QPixmap)
  def drawItemPixmap(self, r: QRect, flags: int, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QStylePainter::drawItemPixmap(const QRect &r, int flags,
    const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylepainter.html#drawItemPixmap

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QStylePainter::drawItemPixmap(const QRect &r, int flags, const
    #      QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN13QStylePainter14drawItemPixmapERK5QRectiRK7QPixmap',
        self._valueOf(r), flags, self._valueOf(pixmap),
    )
