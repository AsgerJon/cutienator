"""
QGeoRouteParserOsrmV5Extension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeorouteparserosrmv5_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoRouteParserOsrmV5Extension to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGeoRouteParserOsrmV5Extension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoRouteParserOsrmV5Extension: a plain Python object
  standing in front of one C++ QGeoRouteParserOsrmV5Extension.

  What exists
  -----------

  No function of Qt's QGeoRouteParserOsrmV5Extension yet. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoRouteParserOsrmV5Extension::~QGeoRouteParserOsrmV5Extension()':
    the destructor: Python never removes a C++
    QGeoRouteParserOsrmV5Extension.
  - Qt's 'void QGeoRouteParserOsrmV5Extension::updateQuery(QUrlQuery &query)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QGeoRouteParserOsrmV5Extension::updateSegment(QGeoRouteSegment
    &segment, const QJsonObject &step, const QJsonObject &maneuver) const':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QGeoRouteParserOsrmV5Extension is created at the first use, not
    by 'QGeoRouteParserOsrmV5Extension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRouteParserOsrmV5Extension.
  - Each name of Qt's QGeoRouteParserOsrmV5Extension that has no cute
    function yet, '__init__', 'updateQuery', 'updateSegment', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteParserOsrmV5Extension'

  #  The functions Qt calls itself that QGeoRouteParserOsrmV5Extension is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'updateQuery': (
          'void QGeoRouteParserOsrmV5Extension::updateQuery(QUrlQuery &) '
          'const',
      ),
      'updateSegment': (
          'void '
          'QGeoRouteParserOsrmV5Extension::updateSegment(QGeoRouteSegment '
          '&, const QJsonObject &, const QJsonObject &) const',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGeoRouteParserOsrmV5Extension::QGeoRouteParserOsrmV5Extension()':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QGeoRouteParserOsrmV5Extension.__init__' has no cute function "
        "yet. Qt's "
        "'QGeoRouteParserOsrmV5Extension::QGeoRouteParserOsrmV5Extension()':"
        " the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
  def updateQuery(*__, **_) -> Never:
    """
    Qt's 'void QGeoRouteParserOsrmV5Extension::updateQuery(QUrlQuery &query)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteParserOsrmV5Extension.updateQuery' has no cute function "
        "yet. Qt's 'void "
        "QGeoRouteParserOsrmV5Extension::updateQuery(QUrlQuery &query) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateSegment(*__, **_) -> Never:
    """
    Qt's 'void QGeoRouteParserOsrmV5Extension::updateSegment(QGeoRouteSegment
    &segment, const QJsonObject &step, const QJsonObject &maneuver) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteParserOsrmV5Extension.updateSegment' has no cute "
        "function yet. Qt's 'void "
        "QGeoRouteParserOsrmV5Extension::updateSegment(QGeoRouteSegment "
        "&segment, const QJsonObject &step, const QJsonObject &maneuver) "
        "const': takes a type Python has no way to hand over yet.")
