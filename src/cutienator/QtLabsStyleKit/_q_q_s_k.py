"""
QQSK binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQSK to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQSK(QObject):
  """
  The cute side of Qt's QQSK: a plain Python object standing in front of one
  C++ QQSK.

  It is built on the cute 'QObject', as Qt's QQSK is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQSK that has a ritual and that Python can call so
  far, 1 name in all: 'metaObject'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQSK::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QQSK::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 7 functions Qt declares: 2 not a gap; 1 a template; 1 leans on
  'QQSK.

  What to expect
  --------------

  - The C++ QQSK is created at the first use, not by 'QQSK(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQSK.
  - Qt tells when it has removed the C++ QQSK. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QQSK that has no cute function yet, 'lazyCreate', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQSK, each a class in here as in C++, and the
  #  names Qt has for the combinations of its flags enums.

  class Delegate(CuteFlags, scoped=True):
    """
    The flags enum 'QQSK::Delegate' of Qt, with the 12 names Qt gives in it.
    Qt names the type of its combinations 'QQSK::Delegates'. C++ keeps these
    names inside the enum, so the class that holds the enum does not have
    them.
    """

    NoDelegate = 0x0
    Control = 0x1
    Background = 0x2
    Handle = 0x4
    HandleFirst = 0x8
    HandleSecond = 0x10
    Indicator = 0x20
    IndicatorForeground = 0x40
    IndicatorFirst = 0x80
    IndicatorFirstForeground = 0x100
    IndicatorSecond = 0x200
    IndicatorSecondForeground = 0x400

  Delegates = Delegate

  class Property(CuteNum, scoped=True):
    """
    The enum 'QQSK::Property' of Qt, with the 45 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    NoProperty = Kee[int](0)
    BottomLeftRadius = Kee[int](1)
    BottomMargin = Kee[int](2)
    BottomPadding = Kee[int](3)
    BottomRightRadius = Kee[int](4)
    Clip = Kee[int](5)
    Color = Kee[int](6)
    Data = Kee[int](7)
    Delegate = Kee[int](8)
    FillMode = Kee[int](9)
    FillWidth = Kee[int](10)
    FillHeight = Kee[int](11)
    Gradient = Kee[int](12)
    HOffset = Kee[int](13)
    Image = Kee[int](14)
    LeftMargin = Kee[int](15)
    LeftPadding = Kee[int](16)
    Margins = Kee[int](17)
    MinimumWidth = Kee[int](18)
    MinimumHeight = Kee[int](19)
    Opacity = Kee[int](20)
    Padding = Kee[int](21)
    Radius = Kee[int](22)
    RightMargin = Kee[int](23)
    RightPadding = Kee[int](24)
    Rotation = Kee[int](25)
    Scale = Kee[int](26)
    Source = Kee[int](27)
    Spacing = Kee[int](28)
    TopLeftRadius = Kee[int](29)
    TopMargin = Kee[int](30)
    TopPadding = Kee[int](31)
    TopRightRadius = Kee[int](32)
    Transition = Kee[int](33)
    Variations = Kee[int](34)
    Visible = Kee[int](35)
    VOffset = Kee[int](36)
    Width = Kee[int](37)
    Height = Kee[int](38)
    Blur = Kee[int](39)
    Alignment = Kee[int](40)
    Bold = Kee[int](41)
    Italic = Kee[int](42)
    PointSize = Kee[int](43)
    COUNT = Kee[int](44)

  class PropertyGroup(CuteNum, scoped=True):
    """
    The enum 'QQSK::PropertyGroup' of Qt, with the 15 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Control = Kee[int](0)
    Background = Kee[int](1)
    Foreground = Kee[int](2)
    Border = Kee[int](3)
    Handle = Kee[int](4)
    Image = Kee[int](5)
    Indicator = Kee[int](6)
    Shadow = Kee[int](7)
    Text = Kee[int](8)
    PATH_ID_GROUP_COUNT = Kee[int](9)
    DelegateSubtype0 = Kee[int](10)
    DelegateSubtype1 = Kee[int](11)
    DelegateSubtype2 = Kee[int](12)
    GlobalFlag = Kee[int](13)
    Unspecified = Kee[int](14)

  class PropertyPathFlag(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QQSK::PropertyPathFlag' of Qt, with the 5 names Qt gives
    in it. Qt names the type of its combinations 'QQSK::PropertyPathFlags'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoFlags = 0x0
    DelegateSubtype0 = 0x1
    DelegateSubtype1 = 0x2
    DelegateSubtype2 = 0x4
    Global = 0x8

  PropertyPathFlags = PropertyPathFlag

  class StateFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QQSK::StateFlag' of Qt, with the 10 names Qt gives in it.
    Qt names the type of its combinations 'QQSK::State'. C++ keeps these
    names inside the enum, so the class that holds the enum does not have
    them.
    """

    Unspecified = 0x0
    Normal = 0x1
    Pressed = 0x2
    Hovered = 0x4
    Highlighted = 0x8
    Focused = 0x10
    Checked = 0x20
    Vertical = 0x40
    Disabled = 0x80
    MAX_STATE = 0x100

  State = StateFlag

  class Subclass(CuteNum, scoped=True):
    """
    The enum 'QQSK::Subclass' of Qt, with the 2 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    QQStyleKitState = Kee[int](0)
    QQStyleKitReader = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQSK'

  #  A C++ QQSK Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQSK'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQSK::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqsk.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQSK::metaObject() const
    address = self.uglySide.call('ritual_ZNK4QQSK10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def lazyCreate(*__, **_) -> Never:
    """
    Qt's 'QQSK::lazyCreate': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQSK.lazyCreate' has no cute function yet. Qt's "
        "'QQSK::lazyCreate': a template: a pattern and no single function.")
