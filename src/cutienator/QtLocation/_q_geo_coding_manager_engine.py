"""
QGeoCodingManagerEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeocodingmanagerengine.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from . import QGeoCodeReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject, QVariant
  from ..QtPositioning import QGeoAddress, QGeoCoordinate, QGeoShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoAddress = WAIT['QGeoAddress']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoShape = WAIT['QGeoShape']
  QLocale = WAIT['QLocale']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoCodingManagerEngine(QObject):
  """
  The cute side of Qt's QGeoCodingManagerEngine: a plain Python object
  standing in front of one C++ QGeoCodingManagerEngine.

  It is built on the cute 'QObject', as Qt's QGeoCodingManagerEngine is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoCodingManagerEngine that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'managerName',
  'managerVersion', 'geocode', 'reverseGeocode', 'setLocale', 'locale',
  'finished', 'errorOccurred', 'setManagerName', 'setManagerVersion'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoCodingManagerEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGeoCodingManagerEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoCodingManagerEngine::~QGeoCodingManagerEngine()': the
    destructor: Python never removes a C++ QGeoCodingManagerEngine.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoCodingManagerEngine is created at the first use, not by
    'QGeoCodingManagerEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoCodingManagerEngine.
  - Qt tells when it has removed the C++ QGeoCodingManagerEngine. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGeoCodingManagerEngine::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#tr

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
    #  QString QGeoCodingManagerEngine::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QGeoCodingManagerEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCodingManagerEngine'

  #  A C++ QGeoCodingManagerEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoCodingManagerEngine'

  #  The functions Qt calls itself that QGeoCodingManagerEngine is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'geocode': (
          ('_ZN23QGeoCodingManagerEngine7geocodeERK11QGeoAddressRK9QGeoShap'
           'e',
           ('address', 'address', 'QtLocation:QGeoCodeReply'),
           (
               ('address', 'value', 'QtPositioning:QGeoAddress'),
               ('address', 'value', 'QtPositioning:QGeoShape'),
           )),
          ('_ZN23QGeoCodingManagerEngine7geocodeERK7QStringiiRK9QGeoShape',
           ('address', 'address', 'QtLocation:QGeoCodeReply'),
           (
               ('address', 'text', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtPositioning:QGeoShape'),
           )),
      ),
      'reverseGeocode': (
          ('_ZN23QGeoCodingManagerEngine14reverseGeocodeERK14QGeoCoordinate'
           'RK9QGeoShape',
           ('address', 'address', 'QtLocation:QGeoCodeReply'),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
               ('address', 'value', 'QtPositioning:QGeoShape'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoCodingManagerEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoCodingManagerEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QGeoCodingManagerEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QGeoCodingManagerEngine::managerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoCodingManagerEngine::managerName() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoCodingManagerEngine11managerNameEv',
    )

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QGeoCodingManagerEngine::managerVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#managerVersion
    """
    #  int QGeoCodingManagerEngine::managerVersion() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoCodingManagerEngine14managerVersionEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QGeoCodingManagerEngine::locale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QGeoCodingManagerEngine::locale() const
    address = self.uglySide.call(
        'ritual_ZNK23QGeoCodingManagerEngine6localeEv',
    )
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QGeoCodingManagerEngine::setLocale(const QLocale
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QGeoCodingManagerEngine::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN23QGeoCodingManagerEngine9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(str)
  def setManagerName(self, managerName: str) -> None:
    """
    Calls Qt's 'void QGeoCodingManagerEngine::setManagerName(const QString
    &managerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#setManagerName

    Parameters
    ----------

    managerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoCodingManagerEngine::setManagerName(const QString
    #      &managerName)
    self.uglySide.call(
        'ritual_ZN23QGeoCodingManagerEngine14setManagerNameERK7QString',
        managerName,
    )

  @overload(int)
  def setManagerVersion(self, managerVersion: int) -> None:
    """
    Calls Qt's 'void QGeoCodingManagerEngine::setManagerVersion(int
    managerVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#setManagerVersion

    Parameters
    ----------

    managerVersion : int
      Passed on as it is.
    """
    #  void QGeoCodingManagerEngine::setManagerVersion(int managerVersion)
    self.uglySide.call(
        'ritual_ZN23QGeoCodingManagerEngine17setManagerVersionEi',
        managerVersion,
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

  @overload(QMap[str, QVariant])
  @overload(QMap[str, QVariant], QObject)
  @overload(QMap[str, QVariant], NoneType)
  def __init__(
      self,
      parameters: QMap[str, QVariant],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCodingManagerEngine::QGeoCodingManagerEngine(const QVariantMap
    &parameters, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoCodingManagerEngine::QGeoCodingManagerEngine(const QVariantMap
    #      &parameters, QObject *parent)
    self._noteCreation(QGeoCodingManagerEngine, lambda: Rituals.call(
        'ritual_ZN23QGeoCodingManagerEngineC1ERK4QMapI7QString8QVariantEP7Q'
        'Object',
        self._valueOf(parameters), self._addressOf(parent, 'QObject'),
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

  @overload(QGeoAddress, QGeoShape)
  def geocode(
      self,
      address: QGeoAddress,
      bounds: QGeoShape,
  ) -> Optional[QGeoCodeReply]:
    """
    Calls Qt's 'QGeoCodeReply *QGeoCodingManagerEngine::geocode(const
    QGeoAddress &address, const QGeoShape &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#geocode

    Parameters
    ----------

    address : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.

    bounds : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    Optional[QGeoCodeReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QGeoAddress
    #      &address, const QGeoShape &bounds)
    ritual = (
        'ritual_ZN23QGeoCodingManagerEngine7geocodeERK11QGeoAddressRK9QGeoS'
        'hape')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QGeoCodingManagerEngine7geocodeERK11QGeoAddressRK'
          '9QGeoShape')
    address = self.uglySide.call(
        ritual, self._valueOf(address), self._valueOf(bounds),
    )
    return QGeoCodeReply._cuteAt(address)

  @overload(str, int, int, QGeoShape)
  def geocode(
      self,
      address: str,
      limit: int,
      offset: int,
      bounds: QGeoShape,
  ) -> Optional[QGeoCodeReply]:
    """
    Calls Qt's 'QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QString
    &address, int limit, int offset, const QGeoShape &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#geocode

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.

    limit : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    bounds : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    Optional[QGeoCodeReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QString
    #      &address, int limit, int offset, const QGeoShape &bounds)
    ritual = (
        'ritual_ZN23QGeoCodingManagerEngine7geocodeERK7QStringiiRK9QGeoShap'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QGeoCodingManagerEngine7geocodeERK7QStringiiRK9QG'
          'eoShape')
    address = self.uglySide.call(
        ritual, address, limit, offset, self._valueOf(bounds),
    )
    return QGeoCodeReply._cuteAt(address)

  @overload(QGeoCoordinate, QGeoShape)
  def reverseGeocode(
      self,
      coordinate: QGeoCoordinate,
      bounds: QGeoShape,
  ) -> Optional[QGeoCodeReply]:
    """
    Calls Qt's 'QGeoCodeReply *QGeoCodingManagerEngine::reverseGeocode(const
    QGeoCoordinate &coordinate, const QGeoShape &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#reverseGeocode

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    bounds : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    Optional[QGeoCodeReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCodeReply *QGeoCodingManagerEngine::reverseGeocode(const
    #      QGeoCoordinate &coordinate, const QGeoShape &bounds)
    ritual = (
        'ritual_ZN23QGeoCodingManagerEngine14reverseGeocodeERK14QGeoCoordin'
        'ateRK9QGeoShape')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QGeoCodingManagerEngine14reverseGeocodeERK14QGeoC'
          'oordinateRK9QGeoShape')
    address = self.uglySide.call(
        ritual, self._valueOf(coordinate), self._valueOf(bounds),
    )
    return QGeoCodeReply._cuteAt(address)

  @overload(QGeoCodeReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QGeoCodeReply]) -> None:
    """
    Calls Qt's 'void QGeoCodingManagerEngine::finished(QGeoCodeReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#finished

    Parameters
    ----------

    reply : Optional[QGeoCodeReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoCodingManagerEngine::finished(QGeoCodeReply *reply)
    self.uglySide.call(
        'ritual_ZN23QGeoCodingManagerEngine8finishedEP13QGeoCodeReply',
        self._addressOf(reply),
    )

  @overload(QGeoCodeReply, QGeoCodeReply.Error)
  @overload(NoneType, QGeoCodeReply.Error)
  @overload(QGeoCodeReply, QGeoCodeReply.Error, str)
  @overload(NoneType, QGeoCodeReply.Error, str)
  def errorOccurred(
      self,
      reply: Optional[QGeoCodeReply],
      error: QGeoCodeReply.Error,
      errorString: str = '',
  ) -> None:
    """
    Calls Qt's 'void QGeoCodingManagerEngine::errorOccurred(QGeoCodeReply
    *reply, QGeoCodeReply::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanagerengine.html#errorOccurred

    Parameters
    ----------

    reply : Optional[QGeoCodeReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QGeoCodeReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QGeoCodingManagerEngine::errorOccurred(QGeoCodeReply *reply,
    #      QGeoCodeReply::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN23QGeoCodingManagerEngine13errorOccurredEP13QGeoCodeReply'
        'NS0_5ErrorERK7QString',
        self._addressOf(reply), error.value, errorString,
    )
