"""
QMdi::Rearranger binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMdi::Rearranger to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Rearranger(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMdi::Rearranger: a plain Python object standing in
  front of one C++ QMdi::Rearranger.

  What exists
  -----------

  Every function of Qt's QMdi::Rearranger that has a ritual and that Python
  can call so far, 1 name in all: 'type'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMdi::Rearranger::rearrange(QList<QWidget *> &widgets, const
    QRect &domain) const': takes a type Python has no way to hand over yet.
  - Qt's 'QMdi::Rearranger::~Rearranger()': the destructor: Python never
    removes a C++ QMdi::Rearranger.

  What to expect
  --------------

  - The C++ QMdi::Rearranger is created at the first use, not by
    'QMdi::Rearranger(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMdi::Rearranger.
  - Each name of Qt's QMdi::Rearranger that has no cute function yet,
    'rearrange', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QMdi::Rearranger, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QMdi::Rearranger::Type' of Qt, with the 3 names Qt gives in it.
    """

    RegularTiler = Kee[int](0)
    SimpleCascader = Kee[int](1)
    IconTiler = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdi::Rearranger'

  #  A C++ QMdi::Rearranger Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMdi_Rearranger'

  #  The functions Qt calls itself that QMdi::Rearranger is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'rearrange': (
          'void QMdi::Rearranger::rearrange(QList<QWidget *> &, const '
          'QRect &) const',
      ),
  }

  #  The functions Qt calls itself that QMdi::Rearranger is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK4QMdi10Rearranger4typeEv',
           ('int', 'enum', 'QtWidgets:QMdi.Rearranger.Type'),
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

  def type(self) -> Type:
    """
    Calls Qt's 'Type QMdi::Rearranger::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdi-rearranger.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QMdi::Rearranger::type() const
    return Rearranger.Type(self.uglySide.call(
        'ritual_ZNK4QMdi10Rearranger4typeEv',
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

  @staticmethod
  def rearrange(*__, **_) -> Never:
    """
    Qt's 'void QMdi::Rearranger::rearrange(QList<QWidget *> &widgets, const
    QRect &domain) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMdi.Rearranger.rearrange' has no cute function yet. Qt's 'void "
        "QMdi::Rearranger::rearrange(QList<QWidget *> &widgets, const QRect "
        "&domain) const': takes a type Python has no way to hand over yet.")
