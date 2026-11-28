"""
QAbstractLayoutStyleInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qabstractlayoutstyleinfo_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractLayoutStyleInfo to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayoutPolicy


class QAbstractLayoutStyleInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractLayoutStyleInfo: a plain Python object
  standing in front of one C++ QAbstractLayoutStyleInfo.

  What exists
  -----------

  Every function of Qt's QAbstractLayoutStyleInfo that has a ritual and that
  Python can call so far, 7 names in all: 'combinedLayoutSpacing',
  'perItemSpacing', 'spacing', 'hasChangedCore', 'invalidate',
  'windowMargin', 'isWindow'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractLayoutStyleInfo::~QAbstractLayoutStyleInfo()': the
    destructor: Python never removes a C++ QAbstractLayoutStyleInfo.

  What to expect
  --------------

  - The C++ QAbstractLayoutStyleInfo is created at the first use, not by
    'QAbstractLayoutStyleInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractLayoutStyleInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractLayoutStyleInfo'

  #  A C++ QAbstractLayoutStyleInfo Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractLayoutStyleInfo'

  #  The functions Qt calls itself that QAbstractLayoutStyleInfo is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'combinedLayoutSpacing': (
          ('_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN'
           '13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE',
           ('double', 'number', ''),
           (
               ('int', 'flags', 'QtGui:QLayoutPolicy.ControlType'),
               ('int', 'flags', 'QtGui:QLayoutPolicy.ControlType'),
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
      'perItemSpacing': (
          ('_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy'
           '11ControlTypeES1_N2Qt11OrientationE',
           ('double', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QLayoutPolicy.ControlType'),
               ('int', 'enum', 'QtGui:QLayoutPolicy.ControlType'),
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
      'spacing': (
          ('_ZNK24QAbstractLayoutStyleInfo7spacingEN2Qt11OrientationE',
           ('double', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
      'hasChangedCore': (
          ('_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv',
           ('bool', 'number', ''),
           ()),
      ),
      'invalidate': (
          ('_ZN24QAbstractLayoutStyleInfo10invalidateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'windowMargin': (
          ('_ZNK24QAbstractLayoutStyleInfo12windowMarginEN2Qt11OrientationE',
           ('double', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      QLayoutPolicy.ControlTypes, QLayoutPolicy.ControlTypes, Qt.Orientation,
  )
  def combinedLayoutSpacing(
      self,
      a0: QLayoutPolicy.ControlTypes,
      a1: QLayoutPolicy.ControlTypes,
      a2: Qt.Orientation,
  ) -> float:
    """
    Calls Qt's 'qreal
    QAbstractLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::
    ControlTypes a0, QLayoutPolicy::ControlTypes a1, Qt::Orientation a2)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html

    Parameters
    ----------

    a0 : QLayoutPolicy.ControlTypes
      Passed on as its number.

    a1 : QLayoutPolicy.ControlTypes
      Passed on as its number.

    a2 : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QAbstractLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::
    #      ControlTypes a0, QLayoutPolicy::ControlTypes a1, Qt::Orientation
    #      a2) const
    ritual = (
        'ritual_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE6QFlag'
        'sIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE'
          '6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE')
    return self.uglySide.call(ritual, a0.value, a1.value, a2.value)

  @overload(
      QLayoutPolicy.ControlType, QLayoutPolicy.ControlType, Qt.Orientation,
  )
  def perItemSpacing(
      self,
      a0: QLayoutPolicy.ControlType,
      a1: QLayoutPolicy.ControlType,
      a2: Qt.Orientation,
  ) -> float:
    """
    Calls Qt's 'qreal
    QAbstractLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlType a0,
    QLayoutPolicy::ControlType a1, Qt::Orientation a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html#perItemSpacing

    Parameters
    ----------

    a0 : QLayoutPolicy.ControlType
      Passed on as its number.

    a1 : QLayoutPolicy.ControlType
      Passed on as its number.

    a2 : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QAbstractLayoutStyleInfo::perItemSpacing(QLayoutPolicy::
    #      ControlType a0, QLayoutPolicy::ControlType a1, Qt::Orientation a2)
    #      const
    ritual = (
        'ritual_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLayoutPol'
        'icy11ControlTypeES1_N2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLay'
          'outPolicy11ControlTypeES1_N2Qt11OrientationE')
    return self.uglySide.call(ritual, a0.value, a1.value, a2.value)

  @overload(Qt.Orientation)
  def spacing(self, orientation: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal QAbstractLayoutStyleInfo::spacing(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html#spacing

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QAbstractLayoutStyleInfo::spacing(Qt::Orientation orientation)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractLayoutStyleInfo7spacingEN2Qt11OrientationE',
        orientation.value,
    )

  def hasChangedCore(self) -> bool:
    """
    Calls Qt's 'bool QAbstractLayoutStyleInfo::hasChangedCore() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html#hasChangedCore
    """
    #  bool QAbstractLayoutStyleInfo::hasChangedCore() const
    ritual = 'ritual_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv'
    return self.uglySide.call(ritual)

  @overload(Qt.Orientation)
  def windowMargin(self, orientation: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal QAbstractLayoutStyleInfo::windowMargin(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html#windowMargin

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QAbstractLayoutStyleInfo::windowMargin(Qt::Orientation
    #      orientation) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractLayoutStyleInfo12windowMarginEN2Qt11Orientati'
        'onE',
        orientation.value,
    )

  def isWindow(self) -> bool:
    """
    Calls Qt's 'bool QAbstractLayoutStyleInfo::isWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html#isWindow
    """
    #  bool QAbstractLayoutStyleInfo::isWindow() const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractLayoutStyleInfo8isWindowEv',
    )

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
    'QAbstractLayoutStyleInfo::QAbstractLayoutStyleInfo()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html
    """
    #  QAbstractLayoutStyleInfo::QAbstractLayoutStyleInfo()
    self._noteCreation(QAbstractLayoutStyleInfo, lambda: Rituals.call(
        'ritual_ZN24QAbstractLayoutStyleInfoC1Ev',
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QAbstractLayoutStyleInfo::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlayoutstyleinfo.html#invalidate
    """
    #  void QAbstractLayoutStyleInfo::invalidate()
    ritual = 'ritual_ZN24QAbstractLayoutStyleInfo10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QAbstractLayoutStyleInfo10invalidateEv'
    self.uglySide.call(ritual)
