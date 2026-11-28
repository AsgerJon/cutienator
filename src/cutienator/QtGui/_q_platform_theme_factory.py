"""
QPlatformThemeFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformthemefactory_p.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlatformTheme


class QPlatformThemeFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformThemeFactory: a plain Python object standing
  in front of one C++ QPlatformThemeFactory.

  C++ hands a QPlatformThemeFactory around as a copy, so every C++
  QPlatformThemeFactory behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformThemeFactory that has a ritual and that
  Python can call so far, 2 names in all: 'keys', 'create'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformThemeFactory::~QPlatformThemeFactory()': the destructor:
    Python removes its C++ QPlatformThemeFactory by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPlatformThemeFactory is created at the first use, not by
    'QPlatformThemeFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformThemeFactory back gives a copy the ritual
    made for Python, in a new cute QPlatformThemeFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  @overload(str)
  def keys(platformPluginPath: str = '') -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformThemeFactory::keys(const QString
    &platformPluginPath)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformthemefactory.html#keys

    Parameters
    ----------

    platformPluginPath : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformThemeFactory::keys(const QString
    #      &platformPluginPath)
    address = Rituals.call(
        'ritual_ZN21QPlatformThemeFactory4keysERK7QString',
        platformPluginPath,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, str)
  def create(
      key: str,
      platformPluginPath: str = '',
  ) -> Optional[QPlatformTheme]:
    """
    Calls Qt's 'QPlatformTheme *QPlatformThemeFactory::create(const QString
    &key, const QString &platformPluginPath)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformthemefactory.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    platformPluginPath : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QPlatformTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformTheme *QPlatformThemeFactory::create(const QString &key,
    #      const QString &platformPluginPath)
    address = Rituals.call(
        'ritual_ZN21QPlatformThemeFactory6createERK7QStringS2_',
        key, platformPluginPath,
    )
    from . import QPlatformTheme
    return QPlatformTheme._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformThemeFactory'

  #  Qt's '~QPlatformThemeFactory()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformThemeFactory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QPlatformThemeFactoryD1Ev'

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
