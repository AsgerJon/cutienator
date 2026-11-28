"""
QGeoSatelliteInfoSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeosatelliteinfosource.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QGeoSatelliteInfo, QGeoSatelliteInfoSourcePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoSatelliteInfo = WAIT['QGeoSatelliteInfo']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoSatelliteInfoSource(QObject):
  """
  The cute side of Qt's QGeoSatelliteInfoSource: a plain Python object
  standing in front of one C++ QGeoSatelliteInfoSource.

  It is built on the cute 'QObject', as Qt's QGeoSatelliteInfoSource is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoSatelliteInfoSource that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'createDefaultSource', 'createSource', 'availableSources', 'sourceName',
  'setUpdateInterval', 'updateInterval', 'minimumUpdateInterval', 'error',
  'setBackendProperty', 'backendProperty', 'startUpdates', 'stopUpdates',
  'requestUpdate', 'satellitesInViewUpdated', 'satellitesInUseUpdated',
  'errorOccurred', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoSatelliteInfoSource::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGeoSatelliteInfoSource::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoSatelliteInfoSource::~QGeoSatelliteInfoSource()': the
    destructor: Python never removes a C++ QGeoSatelliteInfoSource.
  - Qt's 'QBindable<int> QGeoSatelliteInfoSource::bindableUpdateInterval()':
    gives a type Python has no way to take yet.
  - Qt's 'QGeoSatelliteInfoSource::QGeoSatelliteInfoSource(
    QGeoSatelliteInfoSourcePrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QGeoSatelliteInfoSourcePrivate
    *QGeoSatelliteInfoSource::d_func() const': takes in Python what
    'QGeoSatelliteInfoSourcePrivate *QGeoSatelliteInfoSource::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 32 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoSatelliteInfoSource is created at the first use, not by
    'QGeoSatelliteInfoSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoSatelliteInfoSource.
  - Qt tells when it has removed the C++ QGeoSatelliteInfoSource. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoSatelliteInfoSource that has no cute function yet,
    'bindableUpdateInterval', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoSatelliteInfoSource, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QGeoSatelliteInfoSource::Error' of Qt, with the 5 names Qt
    gives in it.
    """

    AccessError = Kee[int](0)
    ClosedError = Kee[int](1)
    NoError = Kee[int](2)
    UnknownSourceError = Kee[int](-1)
    UpdateTimeoutError = Kee[int](3)

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
    Calls Qt's 'QString QGeoSatelliteInfoSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#tr

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
    #  QString QGeoSatelliteInfoSource::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QGeoSatelliteInfoSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def createDefaultSource(
      parent: Optional[QObject],
  ) -> Optional[QGeoSatelliteInfoSource]:
    """
    Calls Qt's 'QGeoSatelliteInfoSource
    *QGeoSatelliteInfoSource::createDefaultSource(QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#createDefaultSource

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoSatelliteInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoSatelliteInfoSource
    #      *QGeoSatelliteInfoSource::createDefaultSource(QObject *parent)
    address = Rituals.call(
        'ritual_ZN23QGeoSatelliteInfoSource19createDefaultSourceEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoSatelliteInfoSource._cuteAt(address)

  @staticmethod
  @overload(QMap[str, QVariant], QObject)
  @overload(QMap[str, QVariant], NoneType)
  def createDefaultSource(
      parameters: QMap[str, QVariant],
      parent: Optional[QObject],
  ) -> Optional[QGeoSatelliteInfoSource]:
    """
    Calls Qt's 'QGeoSatelliteInfoSource
    *QGeoSatelliteInfoSource::createDefaultSource(const QVariantMap
    &parameters, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#createDefaultSource

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

    Optional[QGeoSatelliteInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoSatelliteInfoSource
    #      *QGeoSatelliteInfoSource::createDefaultSource(const QVariantMap
    #      &parameters, QObject *parent)
    address = Rituals.call(
        'ritual_ZN23QGeoSatelliteInfoSource19createDefaultSourceERK4QMapI7Q'
        'String8QVariantEP7QObject',
        CuteMixin._valueOf(parameters), CuteMixin._addressOf(parent,
        'QObject'),
    )
    return QGeoSatelliteInfoSource._cuteAt(address)

  @staticmethod
  @overload(str, QObject)
  @overload(str, NoneType)
  def createSource(
      sourceName: str,
      parent: Optional[QObject],
  ) -> Optional[QGeoSatelliteInfoSource]:
    """
    Calls Qt's 'QGeoSatelliteInfoSource
    *QGeoSatelliteInfoSource::createSource(const QString &sourceName, QObject
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#createSource

    Parameters
    ----------

    sourceName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoSatelliteInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoSatelliteInfoSource *QGeoSatelliteInfoSource::createSource(const
    #      QString &sourceName, QObject *parent)
    address = Rituals.call(
        'ritual_ZN23QGeoSatelliteInfoSource12createSourceERK7QStringP7QObje'
        'ct',
        sourceName, CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoSatelliteInfoSource._cuteAt(address)

  @staticmethod
  @overload(str, QMap[str, QVariant], QObject)
  @overload(str, QMap[str, QVariant], NoneType)
  def createSource(
      sourceName: str,
      parameters: QMap[str, QVariant],
      parent: Optional[QObject],
  ) -> Optional[QGeoSatelliteInfoSource]:
    """
    Calls Qt's 'QGeoSatelliteInfoSource
    *QGeoSatelliteInfoSource::createSource(const QString &sourceName, const
    QVariantMap &parameters, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#createSource

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

    Optional[QGeoSatelliteInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoSatelliteInfoSource *QGeoSatelliteInfoSource::createSource(const
    #      QString &sourceName, const QVariantMap &parameters, QObject
    #      *parent)
    address = Rituals.call(
        'ritual_ZN23QGeoSatelliteInfoSource12createSourceERK7QStringRK4QMap'
        'IS0_8QVariantEP7QObject',
        sourceName, CuteMixin._valueOf(parameters),
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoSatelliteInfoSource._cuteAt(address)

  @staticmethod
  def availableSources() -> QStringList:
    """
    Calls Qt's 'QStringList QGeoSatelliteInfoSource::availableSources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#availableSources

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGeoSatelliteInfoSource::availableSources()
    address = Rituals.call(
        'ritual_ZN23QGeoSatelliteInfoSource16availableSourcesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoSatelliteInfoSource'

  #  A C++ QGeoSatelliteInfoSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoSatelliteInfoSource'

  #  The functions Qt calls itself that QGeoSatelliteInfoSource is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setUpdateInterval': (
          ('_ZN23QGeoSatelliteInfoSource17setUpdateIntervalEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'minimumUpdateInterval': (
          ('_ZNK23QGeoSatelliteInfoSource21minimumUpdateIntervalEv',
           ('int', 'number', ''),
           ()),
      ),
      'error': (
          ('_ZNK23QGeoSatelliteInfoSource5errorEv',
           ('int', 'enum', 'QtPositioning:QGeoSatelliteInfoSource.Error'),
           ()),
      ),
      'setBackendProperty': (
          ('_ZN23QGeoSatelliteInfoSource18setBackendPropertyERK7QStringRK8Q'
           'Variant',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'backendProperty': (
          ('_ZNK23QGeoSatelliteInfoSource15backendPropertyERK7QString',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
           )),
      ),
      'startUpdates': (
          ('_ZN23QGeoSatelliteInfoSource12startUpdatesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stopUpdates': (
          ('_ZN23QGeoSatelliteInfoSource11stopUpdatesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'requestUpdate': (
          ('_ZN23QGeoSatelliteInfoSource13requestUpdateEi',
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
    Calls Qt's 'const QMetaObject *QGeoSatelliteInfoSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoSatelliteInfoSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QGeoSatelliteInfoSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceName(self) -> str:
    """
    Calls Qt's 'QString QGeoSatelliteInfoSource::sourceName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#sourceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoSatelliteInfoSource::sourceName() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoSatelliteInfoSource10sourceNameEv',
    )

  def updateInterval(self) -> int:
    """
    Calls Qt's 'int QGeoSatelliteInfoSource::updateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#updateInterval
    """
    #  int QGeoSatelliteInfoSource::updateInterval() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoSatelliteInfoSource14updateIntervalEv',
    )

  def minimumUpdateInterval(self) -> int:
    """
    Calls Qt's 'int QGeoSatelliteInfoSource::minimumUpdateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#minimumUpdateInterval
    """
    #  int QGeoSatelliteInfoSource::minimumUpdateInterval() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoSatelliteInfoSource21minimumUpdateIntervalEv',
    )

  def error(self) -> Error:
    """
    Calls Qt's 'Error QGeoSatelliteInfoSource::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoSatelliteInfoSource::error() const
    return QGeoSatelliteInfoSource.Error(self.uglySide.call(
        'ritual_ZNK23QGeoSatelliteInfoSource5errorEv',
    ))

  @overload(str)
  def backendProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QGeoSatelliteInfoSource::backendProperty(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#backendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGeoSatelliteInfoSource::backendProperty(const QString &name)
    #      const
    ritual = (
        'ritual_ZNK23QGeoSatelliteInfoSource15backendPropertyERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QGeoSatelliteInfoSource15backendPropertyERK7QStr'
          'ing')
    address = self.uglySide.call(ritual, name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setUpdateInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfoSource::setUpdateInterval(int msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#setUpdateInterval

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QGeoSatelliteInfoSource::setUpdateInterval(int msec)
    ritual = 'ritual_ZN23QGeoSatelliteInfoSource17setUpdateIntervalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QGeoSatelliteInfoSource17setUpdateIntervalEi'
    self.uglySide.call(ritual, msec)

  @overload(str, QVariant)
  def setBackendProperty(self, name: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QGeoSatelliteInfoSource::setBackendProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#setBackendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QGeoSatelliteInfoSource::setBackendProperty(const QString &name,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN23QGeoSatelliteInfoSource18setBackendPropertyERK7QStringR'
        'K8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QGeoSatelliteInfoSource18setBackendPropertyERK7QS'
          'tringRK8QVariant')
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
    'QGeoSatelliteInfoSource::QGeoSatelliteInfoSource(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoSatelliteInfoSource::QGeoSatelliteInfoSource(QObject *parent)
    self._noteCreation(QGeoSatelliteInfoSource, lambda: Rituals.call(
        'ritual_ZN23QGeoSatelliteInfoSourceC1EP7QObject',
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
    Calls Qt's 'void QGeoSatelliteInfoSource::startUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#startUpdates
    """
    #  void QGeoSatelliteInfoSource::startUpdates()
    self.uglySide.call('ritual_ZN23QGeoSatelliteInfoSource12startUpdatesEv')

  def stopUpdates(self) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfoSource::stopUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#stopUpdates
    """
    #  void QGeoSatelliteInfoSource::stopUpdates()
    self.uglySide.call('ritual_ZN23QGeoSatelliteInfoSource11stopUpdatesEv')

  @overload()
  @overload(int)
  def requestUpdate(self, timeout: int = 0) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfoSource::requestUpdate(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#requestUpdate

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QGeoSatelliteInfoSource::requestUpdate(int timeout)
    self.uglySide.call(
        'ritual_ZN23QGeoSatelliteInfoSource13requestUpdateEi', timeout,
    )

  @overload(QList[QGeoSatelliteInfo])
  def satellitesInViewUpdated(
      self,
      satellites: QList[QGeoSatelliteInfo],
  ) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfoSource::satellitesInViewUpdated(const
    QList<QGeoSatelliteInfo> &satellites)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html

    Parameters
    ----------

    satellites : QList[QGeoSatelliteInfo]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoSatelliteInfoSource::satellitesInViewUpdated(const
    #      QList<QGeoSatelliteInfo> &satellites)
    self.uglySide.call(
        'ritual_ZN23QGeoSatelliteInfoSource23satellitesInViewUpdatedERK5QLi'
        'stI17QGeoSatelliteInfoE',
        self._valueOf(satellites),
    )

  @overload(QList[QGeoSatelliteInfo])
  def satellitesInUseUpdated(
      self,
      satellites: QList[QGeoSatelliteInfo],
  ) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfoSource::satellitesInUseUpdated(const
    QList<QGeoSatelliteInfo> &satellites)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html

    Parameters
    ----------

    satellites : QList[QGeoSatelliteInfo]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoSatelliteInfoSource::satellitesInUseUpdated(const
    #      QList<QGeoSatelliteInfo> &satellites)
    self.uglySide.call(
        'ritual_ZN23QGeoSatelliteInfoSource22satellitesInUseUpdatedERK5QLis'
        'tI17QGeoSatelliteInfoE',
        self._valueOf(satellites),
    )

  @overload(Error)
  def errorOccurred(self, a0: Error) -> None:
    """
    Calls Qt's 'void
    QGeoSatelliteInfoSource::errorOccurred(QGeoSatelliteInfoSource::Error
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#errorOccurred

    Parameters
    ----------

    a0 : Error
      Passed on as its number.
    """
    #  void QGeoSatelliteInfoSource::errorOccurred(QGeoSatelliteInfoSource::
    #      Error a0)
    self.uglySide.call(
        'ritual_ZN23QGeoSatelliteInfoSource13errorOccurredENS_5ErrorE',
        a0.value,
    )

  def d_func(self) -> Optional[QGeoSatelliteInfoSourcePrivate]:
    """
    Calls Qt's 'QGeoSatelliteInfoSourcePrivate
    *QGeoSatelliteInfoSource::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfosource.html#d_func

    Returns
    -------

    Optional[QGeoSatelliteInfoSourcePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoSatelliteInfoSourcePrivate *QGeoSatelliteInfoSource::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QGeoSatelliteInfoSource6d_funcEv',
    )
    from . import QGeoSatelliteInfoSourcePrivate
    return QGeoSatelliteInfoSourcePrivate._cuteAt(address)

  @staticmethod
  def bindableUpdateInterval(*__, **_) -> Never:
    """
    Qt's 'QBindable<int> QGeoSatelliteInfoSource::bindableUpdateInterval()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoSatelliteInfoSource.bindableUpdateInterval' has no cute "
        "function yet. Qt's 'QBindable<int> "
        "QGeoSatelliteInfoSource::bindableUpdateInterval()': gives a type "
        "Python has no way to take yet.")
