"""
QGeoRouteParserPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeorouteparser_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoRouteParserPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QGeoRouteParser, QGeoRouteRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoRouteRequest = WAIT['QGeoRouteRequest']


class QGeoRouteParserPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGeoRouteParserPrivate: a plain Python object
  standing in front of one C++ QGeoRouteParserPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGeoRouteParserPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoRouteParserPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'requestUrl'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGeoRouteParser *QGeoRouteParserPrivate::q_func() const':
    takes in Python what 'QGeoRouteParser *QGeoRouteParserPrivate::q_func()'
    takes.
  - Qt's 'QGeoRouteParserPrivate::~QGeoRouteParserPrivate()': the destructor:
    Python never removes a C++ QGeoRouteParserPrivate.
  - Qt's 'QGeoRouteReply::Error
    QGeoRouteParserPrivate::parseReply(QList<QGeoRoute> &routes, QString
    &errorString, const QByteArray &reply) const': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QGeoRouteParserPrivate is created at the first use, not by
    'QGeoRouteParserPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRouteParserPrivate.
  - Each name of Qt's QGeoRouteParserPrivate that has no cute function yet,
    '__init__', 'parseReply', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteParserPrivate'

  #  A C++ QGeoRouteParserPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoRouteParserPrivate'

  #  The functions Qt calls itself that QGeoRouteParserPrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'parseReply': (
          'QGeoRouteReply::Error '
          'QGeoRouteParserPrivate::parseReply(QList<QGeoRoute> &, QString '
          '&, const QByteArray &) const',
      ),
  }

  #  The functions Qt calls itself that QGeoRouteParserPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'requestUrl': (
          ('_ZNK22QGeoRouteParserPrivate10requestUrlERK16QGeoRouteRequestRK'
           '7QString',
           ('address', 'value', 'QtCore:QUrl'),
           (
               ('address', 'value', 'QtLocation:QGeoRouteRequest'),
               ('address', 'text', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoRouteRequest, str)
  def requestUrl(self, request: QGeoRouteRequest, prefix: str) -> QUrl:
    """
    Calls Qt's 'QUrl QGeoRouteParserPrivate::requestUrl(const
    QGeoRouteRequest &request, const QString &prefix) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteparserprivate.html#requestUrl

    Parameters
    ----------

    request : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QGeoRouteParserPrivate::requestUrl(const QGeoRouteRequest
    #      &request, const QString &prefix) const
    address = self.uglySide.call(
        'ritual_ZNK22QGeoRouteParserPrivate10requestUrlERK16QGeoRouteReques'
        'tRK7QString',
        self._valueOf(request), prefix,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
    Qt's 'QGeoRouteParserPrivate::QGeoRouteParserPrivate()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QGeoRouteParserPrivate.__init__' has no cute function yet. Qt's "
        "'QGeoRouteParserPrivate::QGeoRouteParserPrivate()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def q_func(self) -> Optional[QGeoRouteParser]:
    """
    Calls Qt's 'QGeoRouteParser *QGeoRouteParserPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteparserprivate.html#q_func

    Returns
    -------

    Optional[QGeoRouteParser]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoRouteParser *QGeoRouteParserPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QGeoRouteParserPrivate6q_funcEv',
    )
    from . import QGeoRouteParser
    return QGeoRouteParser._cuteAt(address)

  @staticmethod
  def parseReply(*__, **_) -> Never:
    """
    Qt's 'QGeoRouteReply::Error
    QGeoRouteParserPrivate::parseReply(QList<QGeoRoute> &routes, QString
    &errorString, const QByteArray &reply) const': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteParserPrivate.parseReply' has no cute function yet. Qt's "
        "'QGeoRouteReply::Error "
        "QGeoRouteParserPrivate::parseReply(QList<QGeoRoute> &routes, "
        "QString &errorString, const QByteArray &reply) const': takes a "
        "type Python has no way to hand over yet.")
