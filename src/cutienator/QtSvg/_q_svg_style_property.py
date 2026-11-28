"""
QSvgStyleProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgStyleProperty to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSvgStyleProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgStyleProperty: a plain Python object standing in
  front of one C++ QSvgStyleProperty.

  What exists
  -----------

  Every function of Qt's QSvgStyleProperty that has a ritual and that Python
  can call so far, 2 names in all: 'type', 'isDefault'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgStyleProperty::~QSvgStyleProperty()': the destructor: Python
    never removes a C++ QSvgStyleProperty.
  - Qt's 'void QSvgStyleProperty::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgStyleProperty::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgStyleProperty is created at the first use, not by
    'QSvgStyleProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgStyleProperty.
  - Each name of Qt's QSvgStyleProperty that has no cute function yet,
    'apply', 'revert', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSvgStyleProperty, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QSvgStyleProperty::Type' of Qt, with the 10 names Qt gives in
    it.
    """

    Quality = Kee[int](0)
    Fill = Kee[int](1)
    ViewportFill = Kee[int](2)
    Font = Kee[int](3)
    Stroke = Kee[int](4)
    Transform = Kee[int](5)
    Opacity = Kee[int](6)
    CompOp = Kee[int](7)
    Offset = Kee[int](8)
    NumTypes = Kee[int](9)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgStyleProperty'

  #  A C++ QSvgStyleProperty Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgStyleProperty'

  #  The functions Qt calls itself that QSvgStyleProperty is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'apply': (
          'void QSvgStyleProperty::apply(QPainter *, const QSvgNode *, '
          'QSvgExtraStates &)',
      ),
      'revert': (
          'void QSvgStyleProperty::revert(QPainter *, QSvgExtraStates &)',
      ),
  }

  #  The functions Qt calls itself that QSvgStyleProperty is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK17QSvgStyleProperty4typeEv',
           ('int', 'enum', 'QtSvg:QSvgStyleProperty.Type'),
           ()),
      ),
      'isDefault': (
          ('_ZNK17QSvgStyleProperty9isDefaultEv',
           ('bool', 'number', ''),
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
    Calls Qt's 'Type QSvgStyleProperty::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleproperty.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QSvgStyleProperty::type() const
    return QSvgStyleProperty.Type(self.uglySide.call(
        'ritual_ZNK17QSvgStyleProperty4typeEv',
    ))

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QSvgStyleProperty::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleproperty.html#isDefault
    """
    #  bool QSvgStyleProperty::isDefault() const
    ritual = 'ritual_ZNK17QSvgStyleProperty9isDefaultEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSvgStyleProperty9isDefaultEv'
    return self.uglySide.call(ritual)

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
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QSvgStyleProperty::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSvgStyleProperty.apply' has no cute function yet. Qt's 'void "
        "QSvgStyleProperty::apply(QPainter *p, const QSvgNode *node, "
        "QSvgExtraStates &states)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def revert(*__, **_) -> Never:
    """
    Qt's 'void QSvgStyleProperty::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgStyleProperty.revert' has no cute function yet. Qt's 'void "
        "QSvgStyleProperty::revert(QPainter *p, QSvgExtraStates &states)': "
        "takes a type Python has no way to hand over yet.")
