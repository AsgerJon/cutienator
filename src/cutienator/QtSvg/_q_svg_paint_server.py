"""
QSvgPaintServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSvgPaintServer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSvgPaintServer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgPaintServer: a plain Python object standing in
  front of one C++ QSvgPaintServer.

  What exists
  -----------

  Every function of Qt's QSvgPaintServer that has a ritual and that Python
  can call so far, 1 name in all: 'type'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgPaintServer::~QSvgPaintServer()': the destructor: Python never
    removes a C++ QSvgPaintServer.
  - Qt's 'QBrush QSvgPaintServer::brush(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  5 of the 8 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QSvgPaintServer is created at the first use, not by
    'QSvgPaintServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgPaintServer.
  - Each name of Qt's QSvgPaintServer that has no cute function yet,
    '__init__', 'brush', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSvgPaintServer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QSvgPaintServer::Type' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    SolidColor = Kee[int](0)
    Gradient = Kee[int](1)
    Pattern = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgPaintServer'

  #  A C++ QSvgPaintServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgPaintServer'

  #  The functions Qt calls itself that QSvgPaintServer is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'brush': (
          'QBrush QSvgPaintServer::brush(QPainter *, const QSvgNode *, '
          'QSvgExtraStates &)',
      ),
  }

  #  The functions Qt calls itself that QSvgPaintServer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK15QSvgPaintServer4typeEv',
           ('int', 'enum', 'QtSvg:QSvgPaintServer.Type'),
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
    Calls Qt's 'Type QSvgPaintServer::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpaintserver.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QSvgPaintServer::type() const
    return QSvgPaintServer.Type(self.uglySide.call(
        'ritual_ZNK15QSvgPaintServer4typeEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSvgPaintServer::QSvgPaintServer()': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QSvgPaintServer.__init__' has no cute function yet. Qt's "
        "'QSvgPaintServer::QSvgPaintServer()': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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
  def brush(*__, **_) -> Never:
    """
    Qt's 'QBrush QSvgPaintServer::brush(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSvgPaintServer.brush' has no cute function yet. Qt's 'QBrush "
        "QSvgPaintServer::brush(QPainter *p, const QSvgNode *node, "
        "QSvgExtraStates &states)': takes a type Python has no way to hand "
        "over yet.")
