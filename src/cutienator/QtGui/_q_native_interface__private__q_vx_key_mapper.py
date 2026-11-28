"""
QNativeInterface::Private::QVxKeyMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qkeymapper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QNativeInterface::Private::QVxKeyMapper to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QVxKeyMapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::Private::QVxKeyMapper: a plain
  Python object standing in front of one C++
  QNativeInterface::Private::QVxKeyMapper.

  What exists
  -----------

  Every function of Qt's QNativeInterface::Private::QVxKeyMapper that has a
  ritual and that Python can call so far, 2 names in all: 'loadKeymap',
  'switchLang'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::Private::QVxKeyMapper::~QVxKeyMapper()': the
    destructor: Python never removes a C++
    QNativeInterface::Private::QVxKeyMapper.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QNativeInterface::Private::QVxKeyMapper is created at the first
    use, not by 'QNativeInterface::Private::QVxKeyMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::Private::QVxKeyMapper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeInterface::Private::QVxKeyMapper'

  #  A C++ QNativeInterface::Private::QVxKeyMapper Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_Private_QVxKeyMapper'

  #  The functions Qt calls itself that
  #  QNativeInterface::Private::QVxKeyMapper is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'loadKeymap': (
          ('_ZN16QNativeInterface7Private12QVxKeyMapper10loadKeymapERK7QStr'
           'ing',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'switchLang': (
          ('_ZN16QNativeInterface7Private12QVxKeyMapper10switchLangEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

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
    'QNativeInterface::Private::QVxKeyMapper::QVxKeyMapper()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvxkeymapper.html
    """
    #  QNativeInterface::Private::QVxKeyMapper::QVxKeyMapper()
    self._noteCreation(QVxKeyMapper, lambda: Rituals.call(
        'ritual_ZN16QNativeInterface7Private12QVxKeyMapperC1Ev',
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

  @overload(str)
  def loadKeymap(self, filename: str) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QVxKeyMapper::loadKeymap(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvxkeymapper.html

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNativeInterface::Private::QVxKeyMapper::loadKeymap(const QString
    #      &filename)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private12QVxKeyMapper10loadKeymapERK7Q'
        'String',
        filename,
    )

  def switchLang(self) -> None:
    """
    Calls Qt's 'void QNativeInterface::Private::QVxKeyMapper::switchLang()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvxkeymapper.html
    """
    #  void QNativeInterface::Private::QVxKeyMapper::switchLang()
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private12QVxKeyMapper10switchLangEv',
    )
