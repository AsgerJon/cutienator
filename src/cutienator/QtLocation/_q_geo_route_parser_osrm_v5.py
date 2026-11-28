"""
QGeoRouteParserOsrmV5 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeorouteparserosrmv5_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoRouteParserOsrmV5 to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGeoRouteParser

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QGeoRouteParserOsrmV5Extension
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoRouteParserOsrmV5Extension = WAIT['QGeoRouteParserOsrmV5Extension']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoRouteParserOsrmV5(QGeoRouteParser):
  """
  The cute side of Qt's QGeoRouteParserOsrmV5: a plain Python object standing
  in front of one C++ QGeoRouteParserOsrmV5.

  It is built on the cute 'QGeoRouteParser', as Qt's QGeoRouteParserOsrmV5 is
  built on Qt's QGeoRouteParser, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoRouteParserOsrmV5 that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'tr', 'setExtension'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoRouteParserOsrmV5::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGeoRouteParserOsrmV5::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoRouteParserOsrmV5Private *QGeoRouteParserOsrmV5::d_func()':
    gives 'QGeoRouteParserOsrmV5Private', which has no cute class yet.
  - Qt's 'const QGeoRouteParserOsrmV5Private *QGeoRouteParserOsrmV5::d_func()
    const': gives 'QGeoRouteParserOsrmV5Private', which has no cute class
    yet.
  - Qt's 'QGeoRouteParserOsrmV5::~QGeoRouteParserOsrmV5()': the destructor:
    Python never removes a C++ QGeoRouteParserOsrmV5.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoRouteParserOsrmV5 is created at the first use, not by
    'QGeoRouteParserOsrmV5(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRouteParserOsrmV5.
  - Qt tells when it has removed the C++ QGeoRouteParserOsrmV5. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QGeoRouteParserOsrmV5::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteparserosrmv5.html#tr

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
    #  QString QGeoRouteParserOsrmV5::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QGeoRouteParserOsrmV52trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteParserOsrmV5'

  #  A C++ QGeoRouteParserOsrmV5 Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoRouteParserOsrmV5'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoRouteParserOsrmV5::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteparserosrmv5.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoRouteParserOsrmV5::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QGeoRouteParserOsrmV510metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoRouteParserOsrmV5Extension)
  @overload(NoneType)
  def setExtension(
      self,
      extension: Optional[QGeoRouteParserOsrmV5Extension],
  ) -> None:
    """
    Calls Qt's 'void QGeoRouteParserOsrmV5::setExtension(const
    QGeoRouteParserOsrmV5Extension *extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteparserosrmv5.html#setExtension

    Parameters
    ----------

    extension : Optional[QGeoRouteParserOsrmV5Extension]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoRouteParserOsrmV5::setExtension(const
    #      QGeoRouteParserOsrmV5Extension *extension)
    self.uglySide.call(
        'ritual_ZN21QGeoRouteParserOsrmV512setExtensionEPK30QGeoRouteParser'
        'OsrmV5Extension',
        self._addressOf(extension),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGeoRouteParserOsrmV5::QGeoRouteParserOsrmV5(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteparserosrmv5.html#QGeoRouteParserOsrmV5

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoRouteParserOsrmV5::QGeoRouteParserOsrmV5(QObject *parent)
    self._noteCreation(QGeoRouteParserOsrmV5, lambda: Rituals.call(
        'ritual_ZN21QGeoRouteParserOsrmV5C1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
