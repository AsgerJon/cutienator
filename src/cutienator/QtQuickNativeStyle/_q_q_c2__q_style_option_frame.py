"""
QQC2::QStyleOptionFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionFrame to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionFrame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionFrame: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionFrame.

  C++ hands a QQC2::QStyleOptionFrame around as a copy, so every C++
  QQC2::QStyleOptionFrame behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionFrame yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionFrame &QQC2::QStyleOptionFrame::operator=(const
    QStyleOptionFrame &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionFrame::~QStyleOptionFrame()': the destructor:
    Python removes its C++ QQC2::QStyleOptionFrame by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionFrame is created at the first use, not by
    'QQC2::QStyleOptionFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionFrame back gives a copy the ritual
    made for Python, in a new cute QQC2::QStyleOptionFrame.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionFrame, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class FrameFeature(CuteFlags):
    """
    The flags enum 'QQC2::QStyleOptionFrame::FrameFeature' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QQC2::QStyleOptionFrame::FrameFeatures'.
    """

    NULL = 0x0
    Flat = 0x1
    Rounded = 0x2

  FrameFeatures = FrameFeature

  class Shadow(CuteNum):
    """
    The enum 'QQC2::QStyleOptionFrame::Shadow' of Qt, with the 3 names Qt
    gives in it.
    """

    Plain = Kee[int](16)
    Raised = Kee[int](32)
    Sunken = Kee[int](48)

  class Shape(CuteNum):
    """
    The enum 'QQC2::QStyleOptionFrame::Shape' of Qt, with the 7 names Qt
    gives in it.
    """

    NoFrame = Kee[int](0)
    Box = Kee[int](1)
    Panel = Kee[int](2)
    WinPanel = Kee[int](3)
    HLine = Kee[int](4)
    VLine = Kee[int](5)
    StyledPanel = Kee[int](6)

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionFrame::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](5)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionFrame::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QStyleOptionFrame'

  #  Qt's '~QQC2::QStyleOptionFrame()'. Naming it makes this a value class:
  #  Python owns every C++ QQC2::QStyleOptionFrame behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC217QStyleOptionFrameD1Ev'

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
    'QQC2::QStyleOptionFrame::QStyleOptionFrame()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionframe.html#QStyleOptionFrame
    """
    #  QQC2::QStyleOptionFrame::QStyleOptionFrame()
    self._noteCreation(QStyleOptionFrame, lambda: Rituals.call(
        'ritual_ZN4QQC217QStyleOptionFrameC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionFrame) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionFrame::QStyleOptionFrame(const QStyleOptionFrame
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionframe.html#QStyleOptionFrame

    Parameters
    ----------

    other : QStyleOptionFrame
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionFrame, which
      stays Python's own.
    """
    #  QQC2::QStyleOptionFrame::QStyleOptionFrame(const QStyleOptionFrame
    #      &other)
    self._noteCreation(QStyleOptionFrame, lambda: Rituals.call(
        'ritual_ZN4QQC217QStyleOptionFrameC1ERKS0_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionFrame::QStyleOptionFrame(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionframe.html#QStyleOptionFrame

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionFrame::QStyleOptionFrame(int version)
    self._noteCreation(QStyleOptionFrame, lambda: Rituals.call(
        'ritual_ZN4QQC217QStyleOptionFrameC1Ei', version,
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
