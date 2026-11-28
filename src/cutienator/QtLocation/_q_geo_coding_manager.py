"""
QGeoCodingManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeocodingmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGeoCodeReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject
  from ..QtPositioning import QGeoAddress, QGeoCoordinate, QGeoShape
  from . import QGeoCodingManagerEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoAddress = WAIT['QGeoAddress']
  QGeoCodingManagerEngine = WAIT['QGeoCodingManagerEngine']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoShape = WAIT['QGeoShape']
  QLocale = WAIT['QLocale']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoCodingManager(QObject):
  """
  The cute side of Qt's QGeoCodingManager: a plain Python object standing in
  front of one C++ QGeoCodingManager.

  It is built on the cute 'QObject', as Qt's QGeoCodingManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoCodingManager that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'managerName',
  'managerVersion', 'geocode', 'reverseGeocode', 'setLocale', 'locale',
  'finished', 'errorOccurred'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoCodingManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoCodingManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoCodingManager::~QGeoCodingManager()': the destructor: Python
    never removes a C++ QGeoCodingManager.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoCodingManager is created at the first use, not by
    'QGeoCodingManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoCodingManager.
  - Qt tells when it has removed the C++ QGeoCodingManager. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGeoCodingManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#tr

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
    #  QString QGeoCodingManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QGeoCodingManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCodingManager'

  #  A C++ QGeoCodingManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoCodingManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoCodingManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoCodingManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGeoCodingManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QGeoCodingManager::managerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoCodingManager::managerName() const
    return self.uglySide.call('ritual_ZNK17QGeoCodingManager11managerNameEv')

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QGeoCodingManager::managerVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanager.html#managerVersion
    """
    #  int QGeoCodingManager::managerVersion() const
    return self.uglySide.call(
        'ritual_ZNK17QGeoCodingManager14managerVersionEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QGeoCodingManager::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QGeoCodingManager::locale() const
    address = self.uglySide.call('ritual_ZNK17QGeoCodingManager6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QGeoCodingManager::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QGeoCodingManager::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN17QGeoCodingManager9setLocaleERK7QLocale',
        self._valueOf(locale),
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

  @overload(QGeoCodingManagerEngine)
  @overload(NoneType)
  @overload(QGeoCodingManagerEngine, QObject)
  @overload(QGeoCodingManagerEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QGeoCodingManagerEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCodingManager::QGeoCodingManager(QGeoCodingManagerEngine *engine,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanager.html#QGeoCodingManager

    Parameters
    ----------

    engine : Optional[QGeoCodingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoCodingManager::QGeoCodingManager(QGeoCodingManagerEngine *engine,
    #      QObject *parent)
    self._noteCreation(QGeoCodingManager, lambda: Rituals.call(
        'ritual_ZN17QGeoCodingManagerC1EP23QGeoCodingManagerEngineP7QObject',
        self._addressOf(engine), self._addressOf(parent, 'QObject'),
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

  @overload(QGeoAddress)
  @overload(QGeoAddress, QGeoShape)
  def geocode(
      self,
      address: QGeoAddress,
      bounds: Optional[QGeoShape] = None,
  ) -> Optional[QGeoCodeReply]:
    """
    Calls Qt's 'QGeoCodeReply *QGeoCodingManager::geocode(const QGeoAddress
    &address, const QGeoShape &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#geocode

    Parameters
    ----------

    address : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.

    bounds : Optional[QGeoShape]
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own. May be left out, as in Qt: a new 'QGeoShape()' is then passed on.

    Returns
    -------

    Optional[QGeoCodeReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCodeReply *QGeoCodingManager::geocode(const QGeoAddress &address,
    #      const QGeoShape &bounds)
    if bounds is None:
      from ..QtPositioning import QGeoShape
      bounds = QGeoShape()
    address = self.uglySide.call(
        'ritual_ZN17QGeoCodingManager7geocodeERK11QGeoAddressRK9QGeoShape',
        self._valueOf(address), self._valueOf(bounds),
    )
    return QGeoCodeReply._cuteAt(address)

  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  @overload(str, int, int, QGeoShape)
  def geocode(
      self,
      searchString: str,
      limit: int = -1,
      offset: int = 0,
      bounds: Optional[QGeoShape] = None,
  ) -> Optional[QGeoCodeReply]:
    """
    Calls Qt's 'QGeoCodeReply *QGeoCodingManager::geocode(const QString
    &searchString, int limit, int offset, const QGeoShape &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#geocode

    Parameters
    ----------

    searchString : str
      Passed on as it is: a QString is made of it for the call.

    limit : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    bounds : Optional[QGeoShape]
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own. May be left out, as in Qt: a new 'QGeoShape()' is then passed on.

    Returns
    -------

    Optional[QGeoCodeReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCodeReply *QGeoCodingManager::geocode(const QString &searchString,
    #      int limit, int offset, const QGeoShape &bounds)
    if bounds is None:
      from ..QtPositioning import QGeoShape
      bounds = QGeoShape()
    address = self.uglySide.call(
        'ritual_ZN17QGeoCodingManager7geocodeERK7QStringiiRK9QGeoShape',
        searchString, limit, offset, self._valueOf(bounds),
    )
    return QGeoCodeReply._cuteAt(address)

  @overload(QGeoCoordinate)
  @overload(QGeoCoordinate, QGeoShape)
  def reverseGeocode(
      self,
      coordinate: QGeoCoordinate,
      bounds: Optional[QGeoShape] = None,
  ) -> Optional[QGeoCodeReply]:
    """
    Calls Qt's 'QGeoCodeReply *QGeoCodingManager::reverseGeocode(const
    QGeoCoordinate &coordinate, const QGeoShape &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanager.html#reverseGeocode

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    bounds : Optional[QGeoShape]
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own. May be left out, as in Qt: a new 'QGeoShape()' is then passed on.

    Returns
    -------

    Optional[QGeoCodeReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCodeReply *QGeoCodingManager::reverseGeocode(const QGeoCoordinate
    #      &coordinate, const QGeoShape &bounds)
    if bounds is None:
      from ..QtPositioning import QGeoShape
      bounds = QGeoShape()
    address = self.uglySide.call(
        'ritual_ZN17QGeoCodingManager14reverseGeocodeERK14QGeoCoordinateRK9'
        'QGeoShape',
        self._valueOf(coordinate), self._valueOf(bounds),
    )
    return QGeoCodeReply._cuteAt(address)

  @overload(QGeoCodeReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QGeoCodeReply]) -> None:
    """
    Calls Qt's 'void QGeoCodingManager::finished(QGeoCodeReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodingmanager.html#finished

    Parameters
    ----------

    reply : Optional[QGeoCodeReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoCodingManager::finished(QGeoCodeReply *reply)
    self.uglySide.call(
        'ritual_ZN17QGeoCodingManager8finishedEP13QGeoCodeReply',
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
    Calls Qt's 'void QGeoCodingManager::errorOccurred(QGeoCodeReply *reply,
    QGeoCodeReply::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocodingmanager.html#errorOccurred

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
    #  void QGeoCodingManager::errorOccurred(QGeoCodeReply *reply,
    #      QGeoCodeReply::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN17QGeoCodingManager13errorOccurredEP13QGeoCodeReplyNS0_5E'
        'rrorERK7QString',
        self._addressOf(reply), error.value, errorString,
    )
