"""
QGeoCoordinateObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeocoordinateobject_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoCoordinateObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoCoordinateObject(QObject):
  """
  The cute side of Qt's QGeoCoordinateObject: a plain Python object standing
  in front of one C++ QGeoCoordinateObject.

  It is built on the cute 'QObject', as Qt's QGeoCoordinateObject is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoCoordinateObject that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', '__eq__',
  '__ne__', 'coordinate', 'setCoordinate', 'coordinateChanged',
  '_qt_property_m_coordinate_offset'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoCoordinateObject::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGeoCoordinateObject::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoCoordinateObject::~QGeoCoordinateObject()': the destructor:
    Python never removes a C++ QGeoCoordinateObject.
  - Qt's 'bool QGeoCoordinateObject::operator==(const QGeoCoordinateObject
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QGeoCoordinateObject::operator!=(const QGeoCoordinateObject
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'QBindable<QGeoCoordinate>
    QGeoCoordinateObject::bindableCoordinate()': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGeoCoordinateObject is created at the first use, not by
    'QGeoCoordinateObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoCoordinateObject.
  - Qt tells when it has removed the C++ QGeoCoordinateObject. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoCoordinateObject that has no cute function yet,
    'bindableCoordinate', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QGeoCoordinateObject::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinateobject.html#tr

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
    #  QString QGeoCoordinateObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QGeoCoordinateObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_coordinate_offset() -> int:
    """
    Calls Qt's 'size_t
    QGeoCoordinateObject::_qt_property_m_coordinate_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html
    """
    #  size_t QGeoCoordinateObject::_qt_property_m_coordinate_offset()
    return Rituals.call(
        'ritual_ZN20QGeoCoordinateObject32_qt_property_m_coordinate_offsetE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCoordinateObject'

  #  A C++ QGeoCoordinateObject Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoCoordinateObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoCoordinateObject::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoCoordinateObject::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QGeoCoordinateObject10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def coordinate(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoCoordinateObject::coordinate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#coordinate

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoCoordinateObject::coordinate() const
    address = self.uglySide.call(
        'ritual_ZNK20QGeoCoordinateObject10coordinateEv',
    )
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def setCoordinate(self, c: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoCoordinateObject::setCoordinate(const QGeoCoordinate
    &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#setCoordinate

    Parameters
    ----------

    c : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoCoordinateObject::setCoordinate(const QGeoCoordinate &c)
    self.uglySide.call(
        'ritual_ZN20QGeoCoordinateObject13setCoordinateERK14QGeoCoordinate',
        self._valueOf(c),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def __eq__(self, other: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoCoordinateObject::operator==(const QGeoCoordinate
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#operator==

    Parameters
    ----------

    other : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoCoordinateObject::operator==(const QGeoCoordinate &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QGeoCoordinateObjecteqERK14QGeoCoordinate',
        self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QGeoCoordinate)
  def __ne__(self, other: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoCoordinateObject::operator!=(const QGeoCoordinate
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#operator!=

    Parameters
    ----------

    other : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoCoordinateObject::operator!=(const QGeoCoordinate &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QGeoCoordinateObjectneERK14QGeoCoordinate',
        self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCoordinateObject::QGeoCoordinateObject(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#QGeoCoordinateObject

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoCoordinateObject::QGeoCoordinateObject(QObject *parent)
    self._noteCreation(QGeoCoordinateObject, lambda: Rituals.call(
        'ritual_ZN20QGeoCoordinateObjectC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QGeoCoordinate)
  @overload(QGeoCoordinate, QObject)
  @overload(QGeoCoordinate, NoneType)
  def __init__(
      self,
      c: QGeoCoordinate,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCoordinateObject::QGeoCoordinateObject(const QGeoCoordinate &c,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#QGeoCoordinateObject

    Parameters
    ----------

    c : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoCoordinateObject::QGeoCoordinateObject(const QGeoCoordinate &c,
    #      QObject *parent)
    self._noteCreation(QGeoCoordinateObject, lambda: Rituals.call(
        'ritual_ZN20QGeoCoordinateObjectC1ERK14QGeoCoordinateP7QObject',
        self._valueOf(c), self._addressOf(parent, 'QObject'),
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

  def coordinateChanged(self) -> None:
    """
    Calls Qt's 'void QGeoCoordinateObject::coordinateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinateobject.html#coordinateChanged
    """
    #  void QGeoCoordinateObject::coordinateChanged()
    self.uglySide.call(
        'ritual_ZN20QGeoCoordinateObject17coordinateChangedEv',
    )

  @staticmethod
  def bindableCoordinate(*__, **_) -> Never:
    """
    Qt's 'QBindable<QGeoCoordinate>
    QGeoCoordinateObject::bindableCoordinate()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGeoCoordinateObject.bindableCoordinate' has no cute function "
        "yet. Qt's 'QBindable<QGeoCoordinate> "
        "QGeoCoordinateObject::bindableCoordinate()': gives a type Python "
        "has no way to take yet.")
