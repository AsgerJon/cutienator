"""
QLoggingCategoryWithEnvironmentOverride binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLoggingCategoryWithEnvironmentOverride to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QLoggingCategory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLoggingCategoryWithEnvironmentOverride(QLoggingCategory):
  """
  The cute side of Qt's QLoggingCategoryWithEnvironmentOverride: a plain
  Python object standing in front of one C++
  QLoggingCategoryWithEnvironmentOverride.

  It is built on the cute 'QLoggingCategory', as Qt's
  QLoggingCategoryWithEnvironmentOverride is built on Qt's QLoggingCategory,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLoggingCategoryWithEnvironmentOverride that has a
  ritual and that Python can call so far, 1 name in all: 'registerOverride'.
  It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QLoggingCategoryWithEnvironmentOverride is created at the first
    use, not by 'QLoggingCategoryWithEnvironmentOverride(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLoggingCategoryWithEnvironmentOverride.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def registerOverride(
      categoryName: Optional[str],
      environment: Optional[str],
  ) -> Optional[str]:
    """
    Calls Qt's 'const char
    *QLoggingCategoryWithEnvironmentOverride::registerOverride(const char
    *categoryName, const char *environment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategorywithenvironmentoverride.html

    Parameters
    ----------

    categoryName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    environment : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QLoggingCategoryWithEnvironmentOverride::registerOverride(const
    #      char *categoryName, const char *environment)
    chars = Rituals.call(
        'ritual_ZN39QLoggingCategoryWithEnvironmentOverride16registerOverri'
        'deEPKcS1_',
        CuteMixin._bytesOf(categoryName), CuteMixin._bytesOf(environment),
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLoggingCategoryWithEnvironmentOverride'

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

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def __init__(self, category: Optional[str], env: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QLoggingCategoryWithEnvironmentOverride::
    QLoggingCategoryWithEnvironmentOverride(const char *category, const char
    *env)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategorywithenvironmentoverride.html

    Parameters
    ----------

    category : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    env : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QLoggingCategoryWithEnvironmentOverride::
    #      QLoggingCategoryWithEnvironmentOverride(const char *category,
    #      const char *env)
    self._noteCreation(
        QLoggingCategoryWithEnvironmentOverride, lambda: Rituals.call(
            'ritual_ZN39QLoggingCategoryWithEnvironmentOverrideC1EPKcS1_',
            self._bytesOf(category), self._bytesOf(env),
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
