"""
QtParseTimeZone::ParsedZone binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtparsetimezone_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QtParseTimeZone::ParsedZone to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QDateTime, QtParseCommon


class ParsedZone(QtParseCommon.ParsedText):
  """
  The cute side of Qt's QtParseTimeZone::ParsedZone: a plain Python object
  standing in front of one C++ QtParseTimeZone::ParsedZone.

  It is built on the cute 'QtParseCommon::ParsedText', as Qt's
  QtParseTimeZone::ParsedZone is built on Qt's QtParseCommon::ParsedText, and
  has everything that class has.

  C++ hands a QtParseTimeZone::ParsedZone around as a copy, so every C++
  QtParseTimeZone::ParsedZone behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtParseTimeZone::ParsedZone that has a ritual and
  that Python can call so far, 1 name in all: 'resolveType'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtParseTimeZone::ParsedZone::~ParsedZone()': the destructor: Python
    removes its C++ QtParseTimeZone::ParsedZone by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QtParseTimeZone::ParsedZone is created at the first use, not by
    'QtParseTimeZone::ParsedZone(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtParseTimeZone::ParsedZone back gives a copy the
    ritual made for Python, in a new cute QtParseTimeZone::ParsedZone.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtParseTimeZone::ParsedZone'

  #  Qt's '~QtParseTimeZone::ParsedZone()'. Naming it makes this a value
  #  class: Python owns every C++ QtParseTimeZone::ParsedZone behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN15QtParseTimeZone10ParsedZoneD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resolveType(self) -> QDateTime.TransitionResolution:
    """
    Calls Qt's 'QDateTime::TransitionResolution
    QtParseTimeZone::ParsedZone::resolveType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtparsetimezone-parsedzone.html#resolveType

    Returns
    -------

    QDateTime.TransitionResolution
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDateTime.TransitionResolution(number)' gives.
    """
    #  QDateTime::TransitionResolution
    #      QtParseTimeZone::ParsedZone::resolveType() const
    return QDateTime.TransitionResolution(self.uglySide.call(
        'ritual_ZNK15QtParseTimeZone10ParsedZone11resolveTypeEv',
    ))

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
