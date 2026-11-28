"""
QQuickIconPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickIconPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QQuickIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickIcon = WAIT['QQuickIcon']


class QQuickIconPrivate(QSharedData):
  """
  The cute side of Qt's QQuickIconPrivate: a plain Python object standing in
  front of one C++ QQuickIconPrivate.

  It is built on the cute 'QSharedData', as Qt's QQuickIconPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QQuickIconPrivate around as a copy, so every C++
  QQuickIconPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickIconPrivate that has a ritual and that Python
  can call so far, 1 name in all: 'isResolved'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickIconPrivate::~QQuickIconPrivate()': the destructor: Python
    removes its C++ QQuickIconPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickIconPrivate is created at the first use, not by
    'QQuickIconPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickIconPrivate back gives a copy the ritual made
    for Python, in a new cute QQuickIconPrivate.
  """

  #  The enums Qt writes inside QQuickIconPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ResolveProperties(CuteNum):
    """
    The enum 'QQuickIconPrivate::ResolveProperties' of Qt, with the 7 names
    Qt gives in it.
    """

    NameResolved = Kee[int](1)
    SourceResolved = Kee[int](2)
    WidthResolved = Kee[int](4)
    HeightResolved = Kee[int](8)
    ColorResolved = Kee[int](16)
    CacheResolved = Kee[int](32)
    AllPropertiesResolved = Kee[int](131071)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickIcon, int)
  def isResolved(icon: QQuickIcon, resolveMask: int) -> bool:
    """
    Calls Qt's 'bool QQuickIconPrivate::isResolved(const QQuickIcon &icon,
    int resolveMask)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconprivate.html#isResolved

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.

    resolveMask : int
      Passed on as it is.
    """
    #  bool QQuickIconPrivate::isResolved(const QQuickIcon &icon, int
    #      resolveMask)
    return Rituals.call(
        'ritual_ZN17QQuickIconPrivate10isResolvedERK10QQuickIconi',
        CuteMixin._valueOf(icon), resolveMask,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIconPrivate'

  #  Qt's '~QQuickIconPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickIconPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQuickIconPrivateD1Ev'

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
