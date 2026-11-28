"""
Qt3DRender::Render::StringToInt binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/stringtoint_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::StringToInt to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']


class StringToInt(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::StringToInt: a plain Python
  object standing in front of one C++ Qt3DRender::Render::StringToInt.

  C++ hands a Qt3DRender::Render::StringToInt around as a copy, so every C++
  Qt3DRender::Render::StringToInt behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::StringToInt that has a ritual
  and that Python can call so far, 2 names in all: 'lookupId',
  'lookupString'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::StringToInt::~StringToInt()': the destructor:
    Python removes its C++ Qt3DRender::Render::StringToInt by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::StringToInt is created at the first use, not
    by 'Qt3DRender::Render::StringToInt(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::StringToInt back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::Render::StringToInt.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def lookupId(str: str) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::StringToInt::lookupId(const QString
    &str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-stringtoint.html#lookupId

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DRender::Render::StringToInt::lookupId(const QString &str)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render11StringToInt8lookupIdERK7QString', str,
    )

  @staticmethod
  @overload(QLatin1String)
  def lookupId(str: QLatin1String) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::StringToInt::lookupId(QLatin1String
    str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-stringtoint.html#lookupId

    Parameters
    ----------

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  int Qt3DRender::Render::StringToInt::lookupId(QLatin1String str)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render11StringToInt8lookupIdE13QLatin1String',
        CuteMixin._valueOf(str),
    )

  @staticmethod
  @overload(int)
  def lookupString(idx: int) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::StringToInt::lookupString(int
    idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-stringtoint.html#lookupString

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::StringToInt::lookupString(int idx)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render11StringToInt12lookupStringEi', idx,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::StringToInt'

  #  Qt's '~Qt3DRender::Render::StringToInt()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::Render::StringToInt behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render11StringToIntD1Ev'

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
