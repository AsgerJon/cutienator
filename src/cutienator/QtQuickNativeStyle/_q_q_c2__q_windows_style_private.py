"""
QQC2::QWindowsStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsstyle_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QWindowsStylePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQC2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsStylePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QWindowsStylePrivate: a plain Python object
  standing in front of one C++ QQC2::QWindowsStylePrivate.

  What exists
  -----------

  Every function of Qt's QQC2::QWindowsStylePrivate that has a ritual and
  that Python can call so far, 7 names in all: 'q_func',
  'pixelMetricFromSystemDp', 'fixedPixelMetric', 'devicePixelRatio',
  'nativeMetricScaleFactor', 'isDarkMode', 'appDevicePixelRatio'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWindowsStyle *QQC2::QWindowsStylePrivate::q_func() const':
    takes in Python what 'QWindowsStyle
    *QQC2::QWindowsStylePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQC2::QWindowsStylePrivate is created at the first use, not by
    'QQC2::QWindowsStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQC2::QWindowsStylePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQC2.QStyle.PixelMetric)
  @overload(QQC2.QStyle.PixelMetric, WAIT['QQC2.QStyleOption'])
  @overload(QQC2.QStyle.PixelMetric, NoneType)
  def pixelMetricFromSystemDp(
      pm: QQC2.QStyle.PixelMetric,
      option: Optional[QQC2.QStyleOption] = None,
  ) -> int:
    """
    Calls Qt's 'int
    QQC2::QWindowsStylePrivate::pixelMetricFromSystemDp(QStyle::PixelMetric
    pm, const QStyleOption *option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html

    Parameters
    ----------

    pm : QQC2.QStyle.PixelMetric
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QWindowsStylePrivate::pixelMetricFromSystemDp(QStyle::
    #      PixelMetric pm, const QStyleOption *option)
    return Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivate23pixelMetricFromSystemDpENS_6'
        'QStyle11PixelMetricEPKNS_12QStyleOptionE',
        pm.value, CuteMixin._addressOf(option),
    )

  @staticmethod
  @overload(QQC2.QStyle.PixelMetric)
  def fixedPixelMetric(pm: QQC2.QStyle.PixelMetric) -> int:
    """
    Calls Qt's 'int
    QQC2::QWindowsStylePrivate::fixedPixelMetric(QStyle::PixelMetric pm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html#fixedPixelMetric

    Parameters
    ----------

    pm : QQC2.QStyle.PixelMetric
      Passed on as its number.
    """
    #  int QQC2::QWindowsStylePrivate::fixedPixelMetric(QStyle::PixelMetric
    #      pm)
    return Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivate16fixedPixelMetricENS_6QStyle1'
        '1PixelMetricE',
        pm.value,
    )

  @staticmethod
  @overload()
  @overload(WAIT['QQC2.QStyleOption'])
  @overload(NoneType)
  def devicePixelRatio(option: Optional[QQC2.QStyleOption] = None) -> float:
    """
    Calls Qt's 'qreal QQC2::QWindowsStylePrivate::devicePixelRatio(const
    QStyleOption *option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html#devicePixelRatio

    Parameters
    ----------

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qreal QQC2::QWindowsStylePrivate::devicePixelRatio(const QStyleOption
    #      *option)
    return Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivate16devicePixelRatioEPKNS_12QSty'
        'leOptionE',
        CuteMixin._addressOf(option),
    )

  @staticmethod
  @overload(QWindow)
  def devicePixelRatio(win: Optional[QWindow]) -> float:
    """
    Calls Qt's 'qreal QQC2::QWindowsStylePrivate::devicePixelRatio(const
    QWindow *win)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html#devicePixelRatio

    Parameters
    ----------

    win : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qreal QQC2::QWindowsStylePrivate::devicePixelRatio(const QWindow *win)
    return Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivate16devicePixelRatioEPK7QWindow',
        CuteMixin._addressOf(win),
    )

  @staticmethod
  @overload()
  @overload(WAIT['QQC2.QStyleOption'])
  @overload(NoneType)
  def nativeMetricScaleFactor(
      option: Optional[QQC2.QStyleOption] = None,
  ) -> float:
    """
    Calls Qt's 'qreal
    QQC2::QWindowsStylePrivate::nativeMetricScaleFactor(const QStyleOption
    *option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html

    Parameters
    ----------

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qreal QQC2::QWindowsStylePrivate::nativeMetricScaleFactor(const
    #      QStyleOption *option)
    return Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivate23nativeMetricScaleFactorEPKNS'
        '_12QStyleOptionE',
        CuteMixin._addressOf(option),
    )

  @staticmethod
  @overload(QWindow)
  def nativeMetricScaleFactor(win: Optional[QWindow]) -> float:
    """
    Calls Qt's 'qreal
    QQC2::QWindowsStylePrivate::nativeMetricScaleFactor(const QWindow *win)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html

    Parameters
    ----------

    win : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qreal QQC2::QWindowsStylePrivate::nativeMetricScaleFactor(const
    #      QWindow *win)
    return Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivate23nativeMetricScaleFactorEPK7Q'
        'Window',
        CuteMixin._addressOf(win),
    )

  @staticmethod
  def isDarkMode() -> bool:
    """
    Calls Qt's 'bool QQC2::QWindowsStylePrivate::isDarkMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html#isDarkMode
    """
    #  bool QQC2::QWindowsStylePrivate::isDarkMode()
    return Rituals.call('ritual_ZN4QQC220QWindowsStylePrivate10isDarkModeEv')

  @staticmethod
  def appDevicePixelRatio() -> float:
    """
    Calls Qt's 'qreal QQC2::QWindowsStylePrivate::appDevicePixelRatio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html#appDevicePixelRatio
    """
    #  qreal QQC2::QWindowsStylePrivate::appDevicePixelRatio()
    return Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivate19appDevicePixelRatioEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QWindowsStylePrivate'

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
    'QQC2::QWindowsStylePrivate::QWindowsStylePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html
    """
    #  QQC2::QWindowsStylePrivate::QWindowsStylePrivate()
    self._noteCreation(QWindowsStylePrivate, lambda: Rituals.call(
        'ritual_ZN4QQC220QWindowsStylePrivateC1Ev',
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

  def q_func(self) -> Optional[QQC2.QWindowsStyle]:
    """
    Calls Qt's 'QWindowsStyle *QQC2::QWindowsStylePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyleprivate.html#q_func

    Returns
    -------

    Optional[QQC2.QWindowsStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowsStyle *QQC2::QWindowsStylePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN4QQC220QWindowsStylePrivate6q_funcEv',
    )
    return QQC2.QWindowsStyle._cuteAt(address)
