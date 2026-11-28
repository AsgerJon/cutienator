"""
Qt3DCore::QGeometryFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qgeometryfactory_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QGeometryFactory to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QGeometryFactory(Qt3DCore.QAbstractFunctor):
  """
  The cute side of Qt's Qt3DCore::QGeometryFactory: a plain Python object
  standing in front of one C++ Qt3DCore::QGeometryFactory.

  It is built on the cute 'Qt3DCore::QAbstractFunctor', as Qt's
  Qt3DCore::QGeometryFactory is built on Qt's Qt3DCore::QAbstractFunctor, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QGeometryFactory that has a ritual and
  that Python can call so far, 1 name in all: '__call__'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QGeometryFactory::~QGeometryFactory()': the destructor:
    Python never removes a C++ Qt3DCore::QGeometryFactory.
  - Qt's 'bool Qt3DCore::QGeometryFactory::equals(const QGeometryFactory
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool operator==(const QGeometryFactory &lhs, const QGeometryFactory
    &rhs)': an operator between other classes, written inside this one.

  What to expect
  --------------

  - The C++ Qt3DCore::QGeometryFactory is created at the first use, not by
    'Qt3DCore::QGeometryFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QGeometryFactory.
  - Each name of Qt's Qt3DCore::QGeometryFactory that has no cute function
    yet, 'equals', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QGeometryFactory'

  #  A C++ Qt3DCore::QGeometryFactory Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QGeometryFactory'

  #  The functions Qt calls itself that Qt3DCore::QGeometryFactory is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'equals': (
          'bool Qt3DCore::QGeometryFactory::equals(const QGeometryFactory '
          '&) const',
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

  def __call__(self) -> Optional[Qt3DCore.QGeometry]:
    """
    Calls Qt's 'QGeometry *Qt3DCore::QGeometryFactory::operator()()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometryfactory.html#operator()

    Returns
    -------

    Optional[Qt3DCore.QGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometry *Qt3DCore::QGeometryFactory::operator()()
    address = self.uglySide.call('ritual_ZN8Qt3DCore16QGeometryFactoryclEv')
    return Qt3DCore.QGeometry._cuteAt(address)

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
  def equals(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DCore::QGeometryFactory::equals(const QGeometryFactory
    &other) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QGeometryFactory.equals' has no cute function yet. Qt's "
        "'bool Qt3DCore::QGeometryFactory::equals(const QGeometryFactory "
        "&other) const': takes a type Python has no way to hand over yet.")
