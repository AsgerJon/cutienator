"""
QGeoPositionInfoSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeopositioninfosource.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QGeoPositionInfo, QGeoPositionInfoSourcePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoPositionInfo = WAIT['QGeoPositionInfo']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoPositionInfoSource(QObject):
  """
  The cute side of Qt's QGeoPositionInfoSource: a plain Python object
  standing in front of one C++ QGeoPositionInfoSource.

  It is built on the cute 'QObject', as Qt's QGeoPositionInfoSource is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoPositionInfoSource that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr',
  'setUpdateInterval', 'updateInterval', 'setPreferredPositioningMethods',
  'preferredPositioningMethods', 'lastKnownPosition',
  'supportedPositioningMethods', 'minimumUpdateInterval', 'sourceName',
  'setBackendProperty', 'backendProperty', 'createDefaultSource',
  'createSource', 'availableSources', 'error', 'startUpdates', 'stopUpdates',
  'requestUpdate', 'positionUpdated', 'errorOccurred',
  'supportedPositioningMethodsChanged', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoPositionInfoSource::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGeoPositionInfoSource::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoPositionInfoSource::~QGeoPositionInfoSource()': the destructor:
    Python never removes a C++ QGeoPositionInfoSource.
  - Qt's 'QBindable<int> QGeoPositionInfoSource::bindableUpdateInterval()':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<PositioningMethods>
    QGeoPositionInfoSource::bindablePreferredPositioningMethods()': gives a
    type Python has no way to take yet.
  - Qt's 'QGeoPositionInfoSource::QGeoPositionInfoSource(
    QGeoPositionInfoSourcePrivate &dd, QObject *parent)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QGeoPositionInfoSourcePrivate
    *QGeoPositionInfoSource::d_func() const': takes in Python what
    'QGeoPositionInfoSourcePrivate *QGeoPositionInfoSource::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoPositionInfoSource is created at the first use, not by
    'QGeoPositionInfoSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoPositionInfoSource.
  - Qt tells when it has removed the C++ QGeoPositionInfoSource. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoPositionInfoSource that has no cute function yet,
    'bindablePreferredPositioningMethods', 'bindableUpdateInterval', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoPositionInfoSource, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QGeoPositionInfoSource::Error' of Qt, with the 5 names Qt gives
    in it.
    """

    AccessError = Kee[int](0)
    ClosedError = Kee[int](1)
    UnknownSourceError = Kee[int](2)
    NoError = Kee[int](3)
    UpdateTimeoutError = Kee[int](4)

  class PositioningMethod(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QGeoPositionInfoSource::PositioningMethod' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QGeoPositionInfoSource::PositioningMethods'.
    """

    NoPositioningMethods = 0x0
    SatellitePositioningMethods = 0xff
    NonSatellitePositioningMethods = 0xffffff00
    AllPositioningMethods = 0xffffffff

  PositioningMethods = PositioningMethod

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
    Calls Qt's 'QString QGeoPositionInfoSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfosource.html#tr

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
    #  QString QGeoPositionInfoSource::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QGeoPositionInfoSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def createDefaultSource(
      parent: Optional[QObject],
  ) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QGeoPositionInfoSource::createDefaultSource(QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#createDefaultSource

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource
    #      *QGeoPositionInfoSource::createDefaultSource(QObject *parent)
    address = Rituals.call(
        'ritual_ZN22QGeoPositionInfoSource19createDefaultSourceEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoPositionInfoSource._cuteAt(address)

  @staticmethod
  @overload(QMap[str, QVariant], QObject)
  @overload(QMap[str, QVariant], NoneType)
  def createDefaultSource(
      parameters: QMap[str, QVariant],
      parent: Optional[QObject],
  ) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QGeoPositionInfoSource::createDefaultSource(const QVariantMap
    &parameters, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#createDefaultSource

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource
    #      *QGeoPositionInfoSource::createDefaultSource(const QVariantMap
    #      &parameters, QObject *parent)
    address = Rituals.call(
        'ritual_ZN22QGeoPositionInfoSource19createDefaultSourceERK4QMapI7QS'
        'tring8QVariantEP7QObject',
        CuteMixin._valueOf(parameters), CuteMixin._addressOf(parent,
        'QObject'),
    )
    return QGeoPositionInfoSource._cuteAt(address)

  @staticmethod
  @overload(str, QObject)
  @overload(str, NoneType)
  def createSource(
      sourceName: str,
      parent: Optional[QObject],
  ) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QGeoPositionInfoSource::createSource(const QString &sourceName, QObject
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#createSource

    Parameters
    ----------

    sourceName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource *QGeoPositionInfoSource::createSource(const
    #      QString &sourceName, QObject *parent)
    address = Rituals.call(
        'ritual_ZN22QGeoPositionInfoSource12createSourceERK7QStringP7QObjec'
        't',
        sourceName, CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoPositionInfoSource._cuteAt(address)

  @staticmethod
  @overload(str, QMap[str, QVariant], QObject)
  @overload(str, QMap[str, QVariant], NoneType)
  def createSource(
      sourceName: str,
      parameters: QMap[str, QVariant],
      parent: Optional[QObject],
  ) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QGeoPositionInfoSource::createSource(const QString &sourceName, const
    QVariantMap &parameters, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#createSource

    Parameters
    ----------

    sourceName : str
      Passed on as it is: a QString is made of it for the call.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource *QGeoPositionInfoSource::createSource(const
    #      QString &sourceName, const QVariantMap &parameters, QObject
    #      *parent)
    address = Rituals.call(
        'ritual_ZN22QGeoPositionInfoSource12createSourceERK7QStringRK4QMapI'
        'S0_8QVariantEP7QObject',
        sourceName, CuteMixin._valueOf(parameters),
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoPositionInfoSource._cuteAt(address)

  @staticmethod
  def availableSources() -> QStringList:
    """
    Calls Qt's 'QStringList QGeoPositionInfoSource::availableSources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#availableSources

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGeoPositionInfoSource::availableSources()
    address = Rituals.call(
        'ritual_ZN22QGeoPositionInfoSource16availableSourcesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPositionInfoSource'

  #  A C++ QGeoPositionInfoSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoPositionInfoSource'

  #  The functions Qt calls itself that QGeoPositionInfoSource is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setUpdateInterval': (
          ('_ZN22QGeoPositionInfoSource17setUpdateIntervalEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setPreferredPositioningMethods': (
          ('_ZN22QGeoPositionInfoSource30setPreferredPositioningMethodsE6QF'
           'lagsINS_17PositioningMethodEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtPositioning:QGeoPositionInfoSource.PositioningMethod'),
           )),
      ),
      'lastKnownPosition': (
          ('_ZNK22QGeoPositionInfoSource17lastKnownPositionEb',
           ('address', 'value', 'QtPositioning:QGeoPositionInfo'),
           (
               ('bool', 'number', ''),
           )),
      ),
      'supportedPositioningMethods': (
          ('_ZNK22QGeoPositionInfoSource27supportedPositioningMethodsEv',
           ('int', 'flags',
            'QtPositioning:QGeoPositionInfoSource.PositioningMethod'),
           ()),
      ),
      'minimumUpdateInterval': (
          ('_ZNK22QGeoPositionInfoSource21minimumUpdateIntervalEv',
           ('int', 'number', ''),
           ()),
      ),
      'setBackendProperty': (
          ('_ZN22QGeoPositionInfoSource18setBackendPropertyERK7QStringRK8QV'
           'ariant',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'backendProperty': (
          ('_ZNK22QGeoPositionInfoSource15backendPropertyERK7QString',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
           )),
      ),
      'error': (
          ('_ZNK22QGeoPositionInfoSource5errorEv',
           ('int', 'enum', 'QtPositioning:QGeoPositionInfoSource.Error'),
           ()),
      ),
      'startUpdates': (
          ('_ZN22QGeoPositionInfoSource12startUpdatesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stopUpdates': (
          ('_ZN22QGeoPositionInfoSource11stopUpdatesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'requestUpdate': (
          ('_ZN22QGeoPositionInfoSource13requestUpdateEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QGeoPositionInfoSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoPositionInfoSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def updateInterval(self) -> int:
    """
    Calls Qt's 'int QGeoPositionInfoSource::updateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#updateInterval
    """
    #  int QGeoPositionInfoSource::updateInterval() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource14updateIntervalEv',
    )

  def preferredPositioningMethods(self) -> PositioningMethods:
    """
    Calls Qt's 'PositioningMethods
    QGeoPositionInfoSource::preferredPositioningMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html

    Returns
    -------

    PositioningMethods
      The value standing for the combination Qt gave back.
    """
    #  PositioningMethods
    #      QGeoPositionInfoSource::preferredPositioningMethods() const
    return QGeoPositionInfoSource.PositioningMethods(self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource27preferredPositioningMethodsEv',
    ))

  @overload()
  @overload(bool)
  def lastKnownPosition(
      self,
      fromSatellitePositioningMethodsOnly: bool = False,
  ) -> QGeoPositionInfo:
    """
    Calls Qt's 'QGeoPositionInfo
    QGeoPositionInfoSource::lastKnownPosition(bool
    fromSatellitePositioningMethodsOnly) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#lastKnownPosition

    Parameters
    ----------

    fromSatellitePositioningMethodsOnly : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QGeoPositionInfo
      A new cute QGeoPositionInfo around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoPositionInfo QGeoPositionInfoSource::lastKnownPosition(bool
    #      fromSatellitePositioningMethodsOnly) const
    address = self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource17lastKnownPositionEb',
        fromSatellitePositioningMethodsOnly,
    )
    from . import QGeoPositionInfo
    return QGeoPositionInfo._cuteOwning(address)

  def supportedPositioningMethods(self) -> PositioningMethods:
    """
    Calls Qt's 'PositioningMethods
    QGeoPositionInfoSource::supportedPositioningMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html

    Returns
    -------

    PositioningMethods
      The value standing for the combination Qt gave back.
    """
    #  PositioningMethods
    #      QGeoPositionInfoSource::supportedPositioningMethods() const
    return QGeoPositionInfoSource.PositioningMethods(self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource27supportedPositioningMethodsEv',
    ))

  def minimumUpdateInterval(self) -> int:
    """
    Calls Qt's 'int QGeoPositionInfoSource::minimumUpdateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#minimumUpdateInterval
    """
    #  int QGeoPositionInfoSource::minimumUpdateInterval() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource21minimumUpdateIntervalEv',
    )

  def sourceName(self) -> str:
    """
    Calls Qt's 'QString QGeoPositionInfoSource::sourceName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#sourceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoPositionInfoSource::sourceName() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource10sourceNameEv',
    )

  @overload(str)
  def backendProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QGeoPositionInfoSource::backendProperty(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#backendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGeoPositionInfoSource::backendProperty(const QString &name)
    #      const
    ritual = 'ritual_ZNK22QGeoPositionInfoSource15backendPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QGeoPositionInfoSource15backendPropertyERK7QStri'
          'ng')
    address = self.uglySide.call(ritual, name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QGeoPositionInfoSource::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfosource.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoPositionInfoSource::error() const
    return QGeoPositionInfoSource.Error(self.uglySide.call(
        'ritual_ZNK22QGeoPositionInfoSource5errorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setUpdateInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QGeoPositionInfoSource::setUpdateInterval(int msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#setUpdateInterval

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QGeoPositionInfoSource::setUpdateInterval(int msec)
    ritual = 'ritual_ZN22QGeoPositionInfoSource17setUpdateIntervalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGeoPositionInfoSource17setUpdateIntervalEi'
    self.uglySide.call(ritual, msec)

  @overload(PositioningMethods)
  def setPreferredPositioningMethods(
      self,
      methods: PositioningMethods,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoPositionInfoSource::setPreferredPositioningMethods(PositioningMethods
    methods)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html

    Parameters
    ----------

    methods : PositioningMethods
      Passed on as its number.
    """
    #  void QGeoPositionInfoSource::setPreferredPositioningMethods(
    #      PositioningMethods methods)
    ritual = (
        'ritual_ZN22QGeoPositionInfoSource30setPreferredPositioningMethodsE'
        '6QFlagsINS_17PositioningMethodEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGeoPositionInfoSource30setPreferredPositioningMe'
          'thodsE6QFlagsINS_17PositioningMethodEE')
    self.uglySide.call(ritual, methods.value)

  @overload(str, QVariant)
  def setBackendProperty(self, name: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QGeoPositionInfoSource::setBackendProperty(const QString
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#setBackendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QGeoPositionInfoSource::setBackendProperty(const QString &name,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN22QGeoPositionInfoSource18setBackendPropertyERK7QStringRK'
        '8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGeoPositionInfoSource18setBackendPropertyERK7QSt'
          'ringRK8QVariant')
    return self.uglySide.call(ritual, name, self._valueOf(value))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPositionInfoSource::QGeoPositionInfoSource(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#QGeoPositionInfoSource

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoPositionInfoSource::QGeoPositionInfoSource(QObject *parent)
    self._noteCreation(QGeoPositionInfoSource, lambda: Rituals.call(
        'ritual_ZN22QGeoPositionInfoSourceC1EP7QObject',
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

  def startUpdates(self) -> None:
    """
    Calls Qt's 'void QGeoPositionInfoSource::startUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#startUpdates
    """
    #  void QGeoPositionInfoSource::startUpdates()
    self.uglySide.call('ritual_ZN22QGeoPositionInfoSource12startUpdatesEv')

  def stopUpdates(self) -> None:
    """
    Calls Qt's 'void QGeoPositionInfoSource::stopUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#stopUpdates
    """
    #  void QGeoPositionInfoSource::stopUpdates()
    self.uglySide.call('ritual_ZN22QGeoPositionInfoSource11stopUpdatesEv')

  @overload()
  @overload(int)
  def requestUpdate(self, timeout: int = 0) -> None:
    """
    Calls Qt's 'void QGeoPositionInfoSource::requestUpdate(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#requestUpdate

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QGeoPositionInfoSource::requestUpdate(int timeout)
    self.uglySide.call(
        'ritual_ZN22QGeoPositionInfoSource13requestUpdateEi', timeout,
    )

  @overload(QGeoPositionInfo)
  def positionUpdated(self, update: QGeoPositionInfo) -> None:
    """
    Calls Qt's 'void QGeoPositionInfoSource::positionUpdated(const
    QGeoPositionInfo &update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#positionUpdated

    Parameters
    ----------

    update : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  void QGeoPositionInfoSource::positionUpdated(const QGeoPositionInfo
    #      &update)
    self.uglySide.call(
        'ritual_ZN22QGeoPositionInfoSource15positionUpdatedERK16QGeoPositio'
        'nInfo',
        self._valueOf(update),
    )

  @overload(Error)
  def errorOccurred(self, a0: Error) -> None:
    """
    Calls Qt's 'void
    QGeoPositionInfoSource::errorOccurred(QGeoPositionInfoSource::Error a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html#errorOccurred

    Parameters
    ----------

    a0 : Error
      Passed on as its number.
    """
    #  void QGeoPositionInfoSource::errorOccurred(QGeoPositionInfoSource::
    #      Error a0)
    self.uglySide.call(
        'ritual_ZN22QGeoPositionInfoSource13errorOccurredENS_5ErrorE',
        a0.value,
    )

  def supportedPositioningMethodsChanged(self) -> None:
    """
    Calls Qt's 'void
    QGeoPositionInfoSource::supportedPositioningMethodsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosource.html
    """
    #  void QGeoPositionInfoSource::supportedPositioningMethodsChanged()
    self.uglySide.call(
        'ritual_ZN22QGeoPositionInfoSource34supportedPositioningMethodsChan'
        'gedEv',
    )

  def d_func(self) -> Optional[QGeoPositionInfoSourcePrivate]:
    """
    Calls Qt's 'QGeoPositionInfoSourcePrivate
    *QGeoPositionInfoSource::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfosource.html#d_func

    Returns
    -------

    Optional[QGeoPositionInfoSourcePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSourcePrivate *QGeoPositionInfoSource::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QGeoPositionInfoSource6d_funcEv',
    )
    from . import QGeoPositionInfoSourcePrivate
    return QGeoPositionInfoSourcePrivate._cuteAt(address)

  @staticmethod
  def bindablePreferredPositioningMethods(*__, **_) -> Never:
    """
    Qt's 'QBindable<PositioningMethods>
    QGeoPositionInfoSource::bindablePreferredPositioningMethods()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoPositionInfoSource.bindablePreferredPositioningMethods' has "
        "no cute function yet. Qt's 'QBindable<PositioningMethods> "
        "QGeoPositionInfoSource::bindablePreferredPositioningMethods()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableUpdateInterval(*__, **_) -> Never:
    """
    Qt's 'QBindable<int> QGeoPositionInfoSource::bindableUpdateInterval()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoPositionInfoSource.bindableUpdateInterval' has no cute "
        "function yet. Qt's 'QBindable<int> "
        "QGeoPositionInfoSource::bindableUpdateInterval()': gives a type "
        "Python has no way to take yet.")
