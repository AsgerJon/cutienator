"""
QGeoMappingManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomappingmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoMappingManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject
  from . import QGeoMap, QGeoMapType, QGeoMappingManagerEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoMappingManagerEngine = WAIT['QGeoMappingManagerEngine']
  QLocale = WAIT['QLocale']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoMappingManager(QObject):
  """
  The cute side of Qt's QGeoMappingManager: a plain Python object standing in
  front of one C++ QGeoMappingManager.

  It is built on the cute 'QObject', as Qt's QGeoMappingManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoMappingManager that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'managerName',
  'managerVersion', 'createMap', 'supportedMapTypes', 'isInitialized',
  'setLocale', 'locale', 'initialized', 'supportedMapTypesChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoMappingManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoMappingManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoMappingManager::~QGeoMappingManager()': the destructor: Python
    never removes a C++ QGeoMappingManager.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoMappingManager is created at the first use, not by
    'QGeoMappingManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoMappingManager.
  - Qt tells when it has removed the C++ QGeoMappingManager. Every call on
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
    Calls Qt's 'QString QGeoMappingManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomappingmanager.html#tr

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
    #  QString QGeoMappingManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QGeoMappingManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMappingManager'

  #  A C++ QGeoMappingManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoMappingManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoMappingManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomappingmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoMappingManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QGeoMappingManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QGeoMappingManager::managerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanager.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoMappingManager::managerName() const
    return self.uglySide.call(
        'ritual_ZNK18QGeoMappingManager11managerNameEv',
    )

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QGeoMappingManager::managerVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanager.html#managerVersion
    """
    #  int QGeoMappingManager::managerVersion() const
    return self.uglySide.call(
        'ritual_ZNK18QGeoMappingManager14managerVersionEv',
    )

  def supportedMapTypes(self) -> QList[QGeoMapType]:
    """
    Calls Qt's 'QList<QGeoMapType> QGeoMappingManager::supportedMapTypes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanager.html#supportedMapTypes

    Returns
    -------

    QList[QGeoMapType]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoMapType> QGeoMappingManager::supportedMapTypes() const
    address = self.uglySide.call(
        'ritual_ZNK18QGeoMappingManager17supportedMapTypesEv',
    )
    from . import QGeoMapType
    return QList[QGeoMapType]._cuteOwning(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QGeoMappingManager::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanager.html#isInitialized
    """
    #  bool QGeoMappingManager::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK18QGeoMappingManager13isInitializedEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QGeoMappingManager::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomappingmanager.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QGeoMappingManager::locale() const
    address = self.uglySide.call('ritual_ZNK18QGeoMappingManager6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QGeoMappingManager::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomappingmanager.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QGeoMappingManager::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN18QGeoMappingManager9setLocaleERK7QLocale',
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

  @overload(QGeoMappingManagerEngine)
  @overload(NoneType)
  @overload(QGeoMappingManagerEngine, QObject)
  @overload(QGeoMappingManagerEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QGeoMappingManagerEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoMappingManager::QGeoMappingManager(QGeoMappingManagerEngine *engine,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanager.html#QGeoMappingManager

    Parameters
    ----------

    engine : Optional[QGeoMappingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoMappingManager::QGeoMappingManager(QGeoMappingManagerEngine
    #      *engine, QObject *parent)
    self._noteCreation(QGeoMappingManager, lambda: Rituals.call(
        'ritual_ZN18QGeoMappingManagerC1EP24QGeoMappingManagerEngineP7QObje'
        'ct',
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

  @overload(QObject)
  @overload(NoneType)
  def createMap(self, parent: Optional[QObject]) -> Optional[QGeoMap]:
    """
    Calls Qt's 'QGeoMap *QGeoMappingManager::createMap(QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomappingmanager.html#createMap

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMap *QGeoMappingManager::createMap(QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN18QGeoMappingManager9createMapEP7QObject',
        self._addressOf(parent, 'QObject'),
    )
    from . import QGeoMap
    return QGeoMap._cuteAt(address)

  def initialized(self) -> None:
    """
    Calls Qt's 'void QGeoMappingManager::initialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanager.html#initialized
    """
    #  void QGeoMappingManager::initialized()
    self.uglySide.call('ritual_ZN18QGeoMappingManager11initializedEv')

  def supportedMapTypesChanged(self) -> None:
    """
    Calls Qt's 'void QGeoMappingManager::supportedMapTypesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanager.html#supportedMapTypesChanged
    """
    #  void QGeoMappingManager::supportedMapTypesChanged()
    self.uglySide.call(
        'ritual_ZN18QGeoMappingManager24supportedMapTypesChangedEv',
    )
