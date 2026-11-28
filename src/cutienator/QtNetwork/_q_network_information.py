"""
QNetworkInformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkinformation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QNetworkInformationBackend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkInformationBackend = WAIT['QNetworkInformationBackend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkInformation(QObject):
  """
  The cute side of Qt's QNetworkInformation: a plain Python object standing
  in front of one C++ QNetworkInformation.

  It is built on the cute 'QObject', as Qt's QNetworkInformation is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkInformation that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'reachability', 'isBehindCaptivePortal', 'transportMedium', 'isMetered',
  'backendName', 'supports', 'supportedFeatures', 'loadDefaultBackend',
  'loadBackendByName', 'loadBackendByFeatures', 'load', 'availableBackends',
  'instance', 'reachabilityChanged', 'isBehindCaptivePortalChanged',
  'transportMediumChanged', 'isMeteredChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkInformation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNetworkInformation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkInformationPrivate *QNetworkInformation::d_func()': gives
    'QNetworkInformationPrivate', which has no cute class yet.
  - Qt's 'const QNetworkInformationPrivate *QNetworkInformation::d_func()
    const': gives 'QNetworkInformationPrivate', which has no cute class yet.
  - Qt's 'QNetworkInformation::~QNetworkInformation()': the destructor:
    Python never removes a C++ QNetworkInformation.

  What has no ritual
  ------------------

  6 of the 32 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QNetworkInformation is created at the first use, not by
    'QNetworkInformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkInformation.
  - Qt tells when it has removed the C++ QNetworkInformation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QNetworkInformation, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Feature(CuteFlags, scoped=True):
    """
    The flags enum 'QNetworkInformation::Feature' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QNetworkInformation::Features'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    Reachability = 0x1
    CaptivePortal = 0x2
    TransportMedium = 0x4
    Metered = 0x8

  Features = Feature

  class Reachability(CuteNum, scoped=True):
    """
    The enum 'QNetworkInformation::Reachability' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    Disconnected = Kee[int](1)
    Local = Kee[int](2)
    Site = Kee[int](3)
    Online = Kee[int](4)

  class TransportMedium(CuteNum, scoped=True):
    """
    The enum 'QNetworkInformation::TransportMedium' of Qt, with the 5 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    Ethernet = Kee[int](1)
    Cellular = Kee[int](2)
    WiFi = Kee[int](3)
    Bluetooth = Kee[int](4)

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
    Calls Qt's 'QString QNetworkInformation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinformation.html#tr

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
    #  QString QNetworkInformation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QNetworkInformation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def loadDefaultBackend() -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::loadDefaultBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#loadDefaultBackend
    """
    #  bool QNetworkInformation::loadDefaultBackend()
    return Rituals.call(
        'ritual_ZN19QNetworkInformation18loadDefaultBackendEv',
    )

  @staticmethod
  @overload(str)
  def loadBackendByName(backend: str) -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::loadBackendByName(QStringView
    backend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#loadBackendByName

    Parameters
    ----------

    backend : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QNetworkInformation::loadBackendByName(QStringView backend)
    return Rituals.call(
        'ritual_ZN19QNetworkInformation17loadBackendByNameE11QStringView',
        backend,
    )

  @staticmethod
  @overload(Features)
  def loadBackendByFeatures(features: Features) -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::loadBackendByFeatures(Features
    features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#loadBackendByFeatures

    Parameters
    ----------

    features : Features
      Passed on as its number.
    """
    #  bool QNetworkInformation::loadBackendByFeatures(Features features)
    return Rituals.call(
        'ritual_ZN19QNetworkInformation21loadBackendByFeaturesE6QFlagsINS_7'
        'FeatureEE',
        features.value,
    )

  @staticmethod
  @overload(str)
  def load(backend: str) -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::load(QStringView backend)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinformation.html#load

    Parameters
    ----------

    backend : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QNetworkInformation::load(QStringView backend)
    return Rituals.call(
        'ritual_ZN19QNetworkInformation4loadE11QStringView', backend,
    )

  @staticmethod
  @overload(Features)
  def load(features: Features) -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::load(Features features)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinformation.html#load

    Parameters
    ----------

    features : Features
      Passed on as its number.
    """
    #  bool QNetworkInformation::load(Features features)
    return Rituals.call(
        'ritual_ZN19QNetworkInformation4loadE6QFlagsINS_7FeatureEE',
        features.value,
    )

  @staticmethod
  def availableBackends() -> QStringList:
    """
    Calls Qt's 'QStringList QNetworkInformation::availableBackends()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#availableBackends

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QNetworkInformation::availableBackends()
    address = Rituals.call(
        'ritual_ZN19QNetworkInformation17availableBackendsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def instance() -> Optional[QNetworkInformation]:
    """
    Calls Qt's 'QNetworkInformation *QNetworkInformation::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinformation.html#instance

    Returns
    -------

    Optional[QNetworkInformation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkInformation *QNetworkInformation::instance()
    address = Rituals.call('ritual_ZN19QNetworkInformation8instanceEv')
    return QNetworkInformation._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkInformation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkInformation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkInformation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QNetworkInformation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reachability(self) -> Reachability:
    """
    Calls Qt's 'Reachability QNetworkInformation::reachability() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#reachability

    Returns
    -------

    Reachability
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Reachability(number)'
      gives.
    """
    #  Reachability QNetworkInformation::reachability() const
    return QNetworkInformation.Reachability(self.uglySide.call(
        'ritual_ZNK19QNetworkInformation12reachabilityEv',
    ))

  def isBehindCaptivePortal(self) -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::isBehindCaptivePortal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#isBehindCaptivePortal
    """
    #  bool QNetworkInformation::isBehindCaptivePortal() const
    return self.uglySide.call(
        'ritual_ZNK19QNetworkInformation21isBehindCaptivePortalEv',
    )

  def transportMedium(self) -> TransportMedium:
    """
    Calls Qt's 'TransportMedium QNetworkInformation::transportMedium()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#transportMedium

    Returns
    -------

    TransportMedium
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransportMedium(number)'
      gives.
    """
    #  TransportMedium QNetworkInformation::transportMedium() const
    return QNetworkInformation.TransportMedium(self.uglySide.call(
        'ritual_ZNK19QNetworkInformation15transportMediumEv',
    ))

  def isMetered(self) -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::isMetered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinformation.html#isMetered
    """
    #  bool QNetworkInformation::isMetered() const
    return self.uglySide.call('ritual_ZNK19QNetworkInformation9isMeteredEv')

  def backendName(self) -> str:
    """
    Calls Qt's 'QString QNetworkInformation::backendName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#backendName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkInformation::backendName() const
    return self.uglySide.call(
        'ritual_ZNK19QNetworkInformation11backendNameEv',
    )

  @overload(Features)
  def supports(self, features: Features) -> bool:
    """
    Calls Qt's 'bool QNetworkInformation::supports(Features features) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinformation.html#supports

    Parameters
    ----------

    features : Features
      Passed on as its number.
    """
    #  bool QNetworkInformation::supports(Features features) const
    return self.uglySide.call(
        'ritual_ZNK19QNetworkInformation8supportsE6QFlagsINS_7FeatureEE',
        features.value,
    )

  def supportedFeatures(self) -> Features:
    """
    Calls Qt's 'Features QNetworkInformation::supportedFeatures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#supportedFeatures

    Returns
    -------

    Features
      The value standing for the combination Qt gave back.
    """
    #  Features QNetworkInformation::supportedFeatures() const
    return QNetworkInformation.Features(self.uglySide.call(
        'ritual_ZNK19QNetworkInformation17supportedFeaturesEv',
    ))

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

  @overload(QNetworkInformationBackend)
  @overload(NoneType)
  def __init__(self, backend: Optional[QNetworkInformationBackend]) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkInformation::QNetworkInformation(QNetworkInformationBackend
    *backend)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#QNetworkInformation

    Parameters
    ----------

    backend : Optional[QNetworkInformationBackend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QNetworkInformation::QNetworkInformation(QNetworkInformationBackend
    #      *backend)
    self._noteCreation(QNetworkInformation, lambda: Rituals.call(
        'ritual_ZN19QNetworkInformationC1EP26QNetworkInformationBackend',
        self._addressOf(backend),
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

  @overload(Reachability)
  def reachabilityChanged(self, newReachability: Reachability) -> None:
    """
    Calls Qt's 'void
    QNetworkInformation::reachabilityChanged(QNetworkInformation::
    Reachability newReachability)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#reachabilityChanged

    Parameters
    ----------

    newReachability : Reachability
      Passed on as its number.
    """
    #  void QNetworkInformation::reachabilityChanged(QNetworkInformation::
    #      Reachability newReachability)
    self.uglySide.call(
        'ritual_ZN19QNetworkInformation19reachabilityChangedENS_12Reachabil'
        'ityE',
        newReachability.value,
    )

  @overload(bool)
  def isBehindCaptivePortalChanged(self, state: bool) -> None:
    """
    Calls Qt's 'void QNetworkInformation::isBehindCaptivePortalChanged(bool
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void QNetworkInformation::isBehindCaptivePortalChanged(bool state)
    self.uglySide.call(
        'ritual_ZN19QNetworkInformation28isBehindCaptivePortalChangedEb',
        state,
    )

  @overload(TransportMedium)
  def transportMediumChanged(self, current: TransportMedium) -> None:
    """
    Calls Qt's 'void
    QNetworkInformation::transportMediumChanged(QNetworkInformation::
    TransportMedium current)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#transportMediumChanged

    Parameters
    ----------

    current : TransportMedium
      Passed on as its number.
    """
    #  void QNetworkInformation::transportMediumChanged(QNetworkInformation::
    #      TransportMedium current)
    self.uglySide.call(
        'ritual_ZN19QNetworkInformation22transportMediumChangedENS_15Transp'
        'ortMediumE',
        current.value,
    )

  @overload(bool)
  def isMeteredChanged(self, isMetered: bool) -> None:
    """
    Calls Qt's 'void QNetworkInformation::isMeteredChanged(bool isMetered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformation.html#isMeteredChanged

    Parameters
    ----------

    isMetered : bool
      Passed on as it is.
    """
    #  void QNetworkInformation::isMeteredChanged(bool isMetered)
    self.uglySide.call(
        'ritual_ZN19QNetworkInformation16isMeteredChangedEb', isMetered,
    )
