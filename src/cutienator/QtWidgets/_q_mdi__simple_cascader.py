"""
QMdi::SimpleCascader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMdi::SimpleCascader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QMdi


class SimpleCascader(QMdi.Rearranger):
  """
  The cute side of Qt's QMdi::SimpleCascader: a plain Python object standing
  in front of one C++ QMdi::SimpleCascader.

  It is built on the cute 'QMdi::Rearranger', as Qt's QMdi::SimpleCascader is
  built on Qt's QMdi::Rearranger, and has everything that class has.

  C++ hands a QMdi::SimpleCascader around as a copy, so every C++
  QMdi::SimpleCascader behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMdi::SimpleCascader that has a ritual and that
  Python can call so far, 1 name in all: 'type'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMdi::SimpleCascader::rearrange(QList<QWidget *> &widgets,
    const QRect &domain) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QMdi::SimpleCascader::~SimpleCascader()': the destructor: Python
    removes its C++ QMdi::SimpleCascader by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMdi::SimpleCascader is created at the first use, not by
    'QMdi::SimpleCascader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMdi::SimpleCascader back gives a copy the ritual
    made for Python, in a new cute QMdi::SimpleCascader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdi::SimpleCascader'

  #  Qt's '~QMdi::SimpleCascader()'. Naming it makes this a value class:
  #  Python owns every C++ QMdi::SimpleCascader behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QMdi14SimpleCascaderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QMdi.Rearranger.Type:
    """
    Calls Qt's 'Type QMdi::SimpleCascader::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdi-simplecascader.html#type

    Returns
    -------

    QMdi.Rearranger.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMdi.Rearranger.Type(number)' gives.
    """
    #  Type QMdi::SimpleCascader::type() const
    ritual = 'ritual_ZNK4QMdi14SimpleCascader4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK4QMdi14SimpleCascader4typeEv'
    return QMdi.Rearranger.Type(self.uglySide.call(ritual))

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
