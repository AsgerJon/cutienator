"""
QStandardPaths binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstandardpaths.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_standard_paths_locate_option import LocateOption
from ._q_standard_paths_standard_location import StandardLocation


class QStandardPaths(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStandardPaths: a plain Python object standing in
  front of one C++ QStandardPaths.

  What exists
  -----------

  Every function of Qt's QStandardPaths that has a ritual and that Python can
  call so far, 5 names in all: 'writableLocation', 'locate', 'displayName',
  'setTestModeEnabled', 'isTestModeEnabled'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  8 of the 13 functions Qt declares: 3 private; 3 takes or gives a type that
  cannot be passed yet; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QStandardPaths is created at the first use, not by
    'QStandardPaths(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStandardPaths.
  """

  #  The enums Qt writes inside QStandardPaths, and the names Qt has for the
  #  combinations of its flags enums.
  LocateOption = LocateOption
  LocateOptions = LocateOption
  StandardLocation = StandardLocation

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(StandardLocation)
  def writableLocation(type: StandardLocation) -> str:
    """
    Calls Qt's 'QString QStandardPaths::writableLocation(StandardLocation
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandardpaths.html#writableLocation

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardPaths::writableLocation(StandardLocation type)
    return Rituals.call(
        'ritual_ZN14QStandardPaths16writableLocationENS_16StandardLocationE',
        type.value,
    )

  @staticmethod
  @overload(StandardLocation, str)
  @overload(StandardLocation, str, LocateOptions)
  def locate(
      type: StandardLocation,
      fileName: str,
      options: LocateOptions = LocateOptions.LocateFile,
  ) -> str:
    """
    Calls Qt's 'QString QStandardPaths::locate(StandardLocation type, const
    QString &fileName, LocateOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandardpaths.html#locate

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    options : LocateOptions
      Passed on as its number. May be left out, as in Qt: it is then
      LocateOptions.LocateFile.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardPaths::locate(StandardLocation type, const QString
    #      &fileName, LocateOptions options)
    return Rituals.call(
        'ritual_ZN14QStandardPaths6locateENS_16StandardLocationERK7QString6'
        'QFlagsINS_12LocateOptionEE',
        type.value, fileName, options.value,
    )

  @staticmethod
  @overload(StandardLocation)
  def displayName(type: StandardLocation) -> str:
    """
    Calls Qt's 'QString QStandardPaths::displayName(StandardLocation type)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandardpaths.html#displayName

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardPaths::displayName(StandardLocation type)
    return Rituals.call(
        'ritual_ZN14QStandardPaths11displayNameENS_16StandardLocationE',
        type.value,
    )

  @staticmethod
  @overload(bool)
  def setTestModeEnabled(testMode: bool) -> None:
    """
    Calls Qt's 'void QStandardPaths::setTestModeEnabled(bool testMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandardpaths.html#setTestModeEnabled

    Parameters
    ----------

    testMode : bool
      Passed on as it is.
    """
    #  void QStandardPaths::setTestModeEnabled(bool testMode)
    Rituals.call('ritual_ZN14QStandardPaths18setTestModeEnabledEb', testMode)

  @staticmethod
  def isTestModeEnabled() -> bool:
    """
    Calls Qt's 'bool QStandardPaths::isTestModeEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandardpaths.html#isTestModeEnabled
    """
    #  bool QStandardPaths::isTestModeEnabled()
    return Rituals.call('ritual_ZN14QStandardPaths17isTestModeEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStandardPaths'

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
