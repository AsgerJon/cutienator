"""
QGeoRouteParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeorouteparser_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoRouteParser to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QGeoRouteParserPrivate, QGeoRouteRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoRouteRequest = WAIT['QGeoRouteRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoRouteParser(QObject):
  """
  The cute side of Qt's QGeoRouteParser: a plain Python object standing in
  front of one C++ QGeoRouteParser.

  It is built on the cute 'QObject', as Qt's QGeoRouteParser is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoRouteParser that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'd_func',
  'requestUrl', 'trafficSide', 'setTrafficSide', 'trafficSideChanged'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoRouteParser::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoRouteParser::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QGeoRouteParserPrivate *QGeoRouteParser::d_func() const':
    takes in Python what 'QGeoRouteParserPrivate *QGeoRouteParser::d_func()'
    takes.
  - Qt's 'QGeoRouteParser::~QGeoRouteParser()': the destructor: Python never
    removes a C++ QGeoRouteParser.
  - Qt's 'QGeoRouteReply::Error QGeoRouteParser::parseReply(QList<QGeoRoute>
    &routes, QString &errorString, const QByteArray &reply) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QGeoRouteParser::QGeoRouteParser(QGeoRouteParserPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoRouteParser is created at the first use, not by
    'QGeoRouteParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRouteParser.
  - Qt tells when it has removed the C++ QGeoRouteParser. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoRouteParser that has no cute function yet,
    '__init__', 'parseReply', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoRouteParser, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class TrafficSide(CuteNum):
    """
    The enum 'QGeoRouteParser::TrafficSide' of Qt, with the 2 names Qt gives
    in it.
    """

    RightHandTraffic = Kee[int](0)
    LeftHandTraffic = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QGeoRouteParser::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteparser.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoRouteParser::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGeoRouteParser2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteParser'

  #  A C++ QGeoRouteParser Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoRouteParser'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoRouteParser::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteparser.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoRouteParser::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGeoRouteParser10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QGeoRouteRequest, str)
  def requestUrl(self, request: QGeoRouteRequest, prefix: str) -> QUrl:
    """
    Calls Qt's 'QUrl QGeoRouteParser::requestUrl(const QGeoRouteRequest
    &request, const QString &prefix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteparser.html#requestUrl

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
    #  QUrl QGeoRouteParser::requestUrl(const QGeoRouteRequest &request,
    #      const QString &prefix) const
    address = self.uglySide.call(
        'ritual_ZNK15QGeoRouteParser10requestUrlERK16QGeoRouteRequestRK7QSt'
        'ring',
        self._valueOf(request), prefix,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def trafficSide(self) -> TrafficSide:
    """
    Calls Qt's 'TrafficSide QGeoRouteParser::trafficSide() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteparser.html#trafficSide

    Returns
    -------

    TrafficSide
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TrafficSide(number)'
      gives.
    """
    #  TrafficSide QGeoRouteParser::trafficSide() const
    return QGeoRouteParser.TrafficSide(self.uglySide.call(
        'ritual_ZNK15QGeoRouteParser11trafficSideEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TrafficSide)
  def setTrafficSide(self, trafficSide: TrafficSide) -> None:
    """
    Calls Qt's 'void QGeoRouteParser::setTrafficSide(TrafficSide
    trafficSide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteparser.html#setTrafficSide

    Parameters
    ----------

    trafficSide : TrafficSide
      Passed on as its number.
    """
    #  void QGeoRouteParser::setTrafficSide(TrafficSide trafficSide)
    self.uglySide.call(
        'ritual_ZN15QGeoRouteParser14setTrafficSideENS_11TrafficSideE',
        trafficSide.value,
    )

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
    Qt's 'QGeoRouteParser::QGeoRouteParser(QGeoRouteParserPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteParser.__init__' has no cute function yet. Qt's "
        "'QGeoRouteParser::QGeoRouteParser(QGeoRouteParserPrivate &dd, "
        "QObject *parent)': takes a type Python has no way to hand over yet."
    )

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

  def d_func(self) -> Optional[QGeoRouteParserPrivate]:
    """
    Calls Qt's 'QGeoRouteParserPrivate *QGeoRouteParser::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteparser.html#d_func

    Returns
    -------

    Optional[QGeoRouteParserPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoRouteParserPrivate *QGeoRouteParser::d_func()
    address = self.uglySide.call('ritual_ZN15QGeoRouteParser6d_funcEv')
    from . import QGeoRouteParserPrivate
    return QGeoRouteParserPrivate._cuteAt(address)

  @overload(TrafficSide)
  def trafficSideChanged(self, trafficSide: TrafficSide) -> None:
    """
    Calls Qt's 'void QGeoRouteParser::trafficSideChanged(TrafficSide
    trafficSide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteparser.html#trafficSideChanged

    Parameters
    ----------

    trafficSide : TrafficSide
      Passed on as its number.
    """
    #  void QGeoRouteParser::trafficSideChanged(TrafficSide trafficSide)
    self.uglySide.call(
        'ritual_ZN15QGeoRouteParser18trafficSideChangedENS_11TrafficSideE',
        trafficSide.value,
    )

  @staticmethod
  def parseReply(*__, **_) -> Never:
    """
    Qt's 'QGeoRouteReply::Error QGeoRouteParser::parseReply(QList<QGeoRoute>
    &routes, QString &errorString, const QByteArray &reply) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteParser.parseReply' has no cute function yet. Qt's "
        "'QGeoRouteReply::Error "
        "QGeoRouteParser::parseReply(QList<QGeoRoute> &routes, QString "
        "&errorString, const QByteArray &reply) const': takes a type Python "
        "has no way to hand over yet.")
