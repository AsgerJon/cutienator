"""
QWindowsStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwindowsstyle_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QWindowsStylePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QCommonStylePrivate, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QStyleOption, QWidget, QWindowsStyle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QStyleOption = WAIT['QStyleOption']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsStylePrivate(QCommonStylePrivate):
  """
  The cute side of Qt's QWindowsStylePrivate: a plain Python object standing
  in front of one C++ QWindowsStylePrivate.

  It is built on the cute 'QCommonStylePrivate', as Qt's QWindowsStylePrivate
  is built on Qt's QCommonStylePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowsStylePrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func',
  'pixelMetricFromSystemDp', 'fixedPixelMetric', 'nativeMetricScaleFactor',
  'hasSeenAlt', 'altDown'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWindowsStyle *QWindowsStylePrivate::q_func() const': takes
    in Python what 'QWindowsStyle *QWindowsStylePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QWindowsStylePrivate is created at the first use, not by
    'QWindowsStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowsStylePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QStyle.PixelMetric)
  @overload(QStyle.PixelMetric, QStyleOption)
  @overload(QStyle.PixelMetric, NoneType)
  @overload(QStyle.PixelMetric, QStyleOption, QWidget)
  @overload(QStyle.PixelMetric, QStyleOption, NoneType)
  @overload(QStyle.PixelMetric, NoneType, QWidget)
  @overload(QStyle.PixelMetric, NoneType, NoneType)
  def pixelMetricFromSystemDp(
      pm: QStyle.PixelMetric,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int
    QWindowsStylePrivate::pixelMetricFromSystemDp(QStyle::PixelMetric pm,
    const QStyleOption *option, const QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsstyleprivate.html#pixelMetricFromSystemDp

    Parameters
    ----------

    pm : QStyle.PixelMetric
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QWindowsStylePrivate::pixelMetricFromSystemDp(QStyle::PixelMetric
    #      pm, const QStyleOption *option, const QWidget *widget)
    return Rituals.call(
        'ritual_ZN20QWindowsStylePrivate23pixelMetricFromSystemDpEN6QStyle1'
        '1PixelMetricEPK12QStyleOptionPK7QWidget',
        pm.value, CuteMixin._addressOf(option), CuteMixin._addressOf(widget),
    )

  @staticmethod
  @overload(QStyle.PixelMetric)
  def fixedPixelMetric(pm: QStyle.PixelMetric) -> int:
    """
    Calls Qt's 'int
    QWindowsStylePrivate::fixedPixelMetric(QStyle::PixelMetric pm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsstyleprivate.html#fixedPixelMetric

    Parameters
    ----------

    pm : QStyle.PixelMetric
      Passed on as its number.
    """
    #  int QWindowsStylePrivate::fixedPixelMetric(QStyle::PixelMetric pm)
    return Rituals.call(
        'ritual_ZN20QWindowsStylePrivate16fixedPixelMetricEN6QStyle11PixelM'
        'etricE',
        pm.value,
    )

  @staticmethod
  @overload()
  @overload(QWidget)
  @overload(NoneType)
  def nativeMetricScaleFactor(widget: Optional[QWidget] = None) -> float:
    """
    Calls Qt's 'qreal QWindowsStylePrivate::nativeMetricScaleFactor(const
    QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsstyleprivate.html#nativeMetricScaleFactor

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qreal QWindowsStylePrivate::nativeMetricScaleFactor(const QWidget
    #      *widget)
    return Rituals.call(
        'ritual_ZN20QWindowsStylePrivate23nativeMetricScaleFactorEPK7QWidge'
        't',
        CuteMixin._addressOf(widget),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowsStylePrivate'

  #  A C++ QWindowsStylePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowsStylePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def hasSeenAlt(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QWindowsStylePrivate::hasSeenAlt(const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsstyleprivate.html#hasSeenAlt

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWindowsStylePrivate::hasSeenAlt(const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK20QWindowsStylePrivate10hasSeenAltEPK7QWidget',
        self._addressOf(widget),
    )

  def altDown(self) -> bool:
    """
    Calls Qt's 'bool QWindowsStylePrivate::altDown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyleprivate.html#altDown
    """
    #  bool QWindowsStylePrivate::altDown() const
    return self.uglySide.call('ritual_ZNK20QWindowsStylePrivate7altDownEv')

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
    'QWindowsStylePrivate::QWindowsStylePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsstyleprivate.html#QWindowsStylePrivate
    """
    #  QWindowsStylePrivate::QWindowsStylePrivate()
    self._noteCreation(QWindowsStylePrivate, lambda: Rituals.call(
        'ritual_ZN20QWindowsStylePrivateC1Ev',
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

  def q_func(self) -> Optional[QWindowsStyle]:
    """
    Calls Qt's 'QWindowsStyle *QWindowsStylePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyleprivate.html#q_func

    Returns
    -------

    Optional[QWindowsStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowsStyle *QWindowsStylePrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QWindowsStylePrivate6q_funcEv')
    from . import QWindowsStyle
    return QWindowsStyle._cuteAt(address)
