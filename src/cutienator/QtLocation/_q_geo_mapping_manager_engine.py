"""
QGeoMappingManagerEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomappingmanagerengine_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoMappingManagerEngine to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLocale, QMetaObject
  from . import QGeoCameraCapabilities, QGeoMap, QGeoMapType
  from . import QGeoMappingManagerEnginePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCameraCapabilities = WAIT['QGeoCameraCapabilities']
  QGeoMapType = WAIT['QGeoMapType']
  QLocale = WAIT['QLocale']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoMappingManagerEngine(QObject):
  """
  The cute side of Qt's QGeoMappingManagerEngine: a plain Python object
  standing in front of one C++ QGeoMappingManagerEngine.

  It is built on the cute 'QObject', as Qt's QGeoMappingManagerEngine is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoMappingManagerEngine that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'createMap',
  'managerName', 'managerVersion', 'supportedMapTypes', 'cameraCapabilities',
  'setLocale', 'locale', 'isInitialized', 'initialized',
  'supportedMapTypesChanged', 'setSupportedMapTypes',
  'setCameraCapabilities', 'engineInitialized', 'setManagerName',
  'setManagerVersion', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoMappingManagerEngine::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QGeoMappingManagerEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoMappingManagerEngine::~QGeoMappingManagerEngine()': the
    destructor: Python never removes a C++ QGeoMappingManagerEngine.
  - Qt's 'const QGeoMappingManagerEnginePrivate
    *QGeoMappingManagerEngine::d_func() const': takes in Python what
    'QGeoMappingManagerEnginePrivate *QGeoMappingManagerEngine::d_func()'
    takes.

  What has no ritual
  ------------------

  5 of the 28 functions Qt declares: 2 not a gap; 2 forbidden; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QGeoMappingManagerEngine is created at the first use, not by
    'QGeoMappingManagerEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoMappingManagerEngine.
  - Qt tells when it has removed the C++ QGeoMappingManagerEngine. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoMappingManagerEngine that has no cute function yet,
    'parameters', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QGeoMappingManagerEngine::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#tr

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
    #  QString QGeoMappingManagerEngine::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QGeoMappingManagerEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMappingManagerEngine'

  #  A C++ QGeoMappingManagerEngine Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoMappingManagerEngine'

  #  The functions Qt calls itself that QGeoMappingManagerEngine is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createMap': (
          ('_ZN24QGeoMappingManagerEngine9createMapEv',
           ('address', 'address', 'QtLocation:QGeoMap'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoMappingManagerEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoMappingManagerEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QGeoMappingManagerEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QGeoMappingManagerEngine::managerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoMappingManagerEngine::managerName() const
    return self.uglySide.call(
        'ritual_ZNK24QGeoMappingManagerEngine11managerNameEv',
    )

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QGeoMappingManagerEngine::managerVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#managerVersion
    """
    #  int QGeoMappingManagerEngine::managerVersion() const
    return self.uglySide.call(
        'ritual_ZNK24QGeoMappingManagerEngine14managerVersionEv',
    )

  def supportedMapTypes(self) -> QList[QGeoMapType]:
    """
    Calls Qt's 'QList<QGeoMapType>
    QGeoMappingManagerEngine::supportedMapTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#supportedMapTypes

    Returns
    -------

    QList[QGeoMapType]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoMapType> QGeoMappingManagerEngine::supportedMapTypes() const
    address = self.uglySide.call(
        'ritual_ZNK24QGeoMappingManagerEngine17supportedMapTypesEv',
    )
    from . import QGeoMapType
    return QList[QGeoMapType]._cuteOwning(address)

  @overload()
  @overload(int)
  def cameraCapabilities(self, mapId: int = 0) -> QGeoCameraCapabilities:
    """
    Calls Qt's 'QGeoCameraCapabilities
    QGeoMappingManagerEngine::cameraCapabilities(int mapId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#cameraCapabilities

    Parameters
    ----------

    mapId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QGeoCameraCapabilities
      A new cute QGeoCameraCapabilities around the copy Qt gave back. Python
      owns it.
    """
    #  QGeoCameraCapabilities
    #      QGeoMappingManagerEngine::cameraCapabilities(int mapId) const
    address = self.uglySide.call(
        'ritual_ZNK24QGeoMappingManagerEngine18cameraCapabilitiesEi', mapId,
    )
    from . import QGeoCameraCapabilities
    return QGeoCameraCapabilities._cuteOwning(address)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QGeoMappingManagerEngine::locale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QGeoMappingManagerEngine::locale() const
    address = self.uglySide.call(
        'ritual_ZNK24QGeoMappingManagerEngine6localeEv',
    )
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QGeoMappingManagerEngine::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#isInitialized
    """
    #  bool QGeoMappingManagerEngine::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK24QGeoMappingManagerEngine13isInitializedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::setLocale(const QLocale
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QGeoMappingManagerEngine::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QList[QGeoMapType])
  def setSupportedMapTypes(
      self,
      supportedMapTypes: QList[QGeoMapType],
  ) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::setSupportedMapTypes(const
    QList<QGeoMapType> &supportedMapTypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#setSupportedMapTypes

    Parameters
    ----------

    supportedMapTypes : QList[QGeoMapType]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoMappingManagerEngine::setSupportedMapTypes(const
    #      QList<QGeoMapType> &supportedMapTypes)
    self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine20setSupportedMapTypesERK5QList'
        'I11QGeoMapTypeE',
        self._valueOf(supportedMapTypes),
    )

  @overload(QGeoCameraCapabilities)
  def setCameraCapabilities(
      self,
      capabilities: QGeoCameraCapabilities,
  ) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::setCameraCapabilities(const
    QGeoCameraCapabilities &capabilities)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html

    Parameters
    ----------

    capabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  void QGeoMappingManagerEngine::setCameraCapabilities(const
    #      QGeoCameraCapabilities &capabilities)
    self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine21setCameraCapabilitiesERK22QGe'
        'oCameraCapabilities',
        self._valueOf(capabilities),
    )

  @overload(str)
  def setManagerName(self, managerName: str) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::setManagerName(const QString
    &managerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#setManagerName

    Parameters
    ----------

    managerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoMappingManagerEngine::setManagerName(const QString
    #      &managerName)
    self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine14setManagerNameERK7QString',
        managerName,
    )

  @overload(int)
  def setManagerVersion(self, managerVersion: int) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::setManagerVersion(int
    managerVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#setManagerVersion

    Parameters
    ----------

    managerVersion : int
      Passed on as it is.
    """
    #  void QGeoMappingManagerEngine::setManagerVersion(int managerVersion)
    self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine17setManagerVersionEi',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGeoMappingManagerEngine::QGeoMappingManagerEngine(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoMappingManagerEngine::QGeoMappingManagerEngine(QObject *parent)
    self._noteCreation(QGeoMappingManagerEngine, lambda: Rituals.call(
        'ritual_ZN24QGeoMappingManagerEngineC1EP7QObject',
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

  def createMap(self) -> Optional[QGeoMap]:
    """
    Calls Qt's 'QGeoMap *QGeoMappingManagerEngine::createMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#createMap

    Returns
    -------

    Optional[QGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMap *QGeoMappingManagerEngine::createMap()
    address = self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine9createMapEv',
    )
    from . import QGeoMap
    return QGeoMap._cuteAt(address)

  def initialized(self) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::initialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#initialized
    """
    #  void QGeoMappingManagerEngine::initialized()
    self.uglySide.call('ritual_ZN24QGeoMappingManagerEngine11initializedEv')

  def supportedMapTypesChanged(self) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::supportedMapTypesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html
    """
    #  void QGeoMappingManagerEngine::supportedMapTypesChanged()
    self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine24supportedMapTypesChangedEv',
    )

  def engineInitialized(self) -> None:
    """
    Calls Qt's 'void QGeoMappingManagerEngine::engineInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#engineInitialized
    """
    #  void QGeoMappingManagerEngine::engineInitialized()
    self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine17engineInitializedEv',
    )

  def d_func(self) -> Optional[QGeoMappingManagerEnginePrivate]:
    """
    Calls Qt's 'QGeoMappingManagerEnginePrivate
    *QGeoMappingManagerEngine::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappingmanagerengine.html#d_func

    Returns
    -------

    Optional[QGeoMappingManagerEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMappingManagerEnginePrivate *QGeoMappingManagerEngine::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QGeoMappingManagerEngine6d_funcEv',
    )
    from . import QGeoMappingManagerEnginePrivate
    return QGeoMappingManagerEnginePrivate._cuteAt(address)

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QVariantMap QGeoMappingManagerEngine::parameters() const': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QGeoMappingManagerEngine.parameters' has no cute function yet. "
        "Qt's 'QVariantMap QGeoMappingManagerEngine::parameters() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
