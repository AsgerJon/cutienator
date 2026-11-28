"""
QDeclarativeSatelliteSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativesatellitesource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeSatelliteSource to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtPositioning import QGeoSatelliteInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoSatelliteInfo = WAIT['QGeoSatelliteInfo']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeSatelliteSource(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeSatelliteSource: a plain Python object
  standing in front of one C++ QDeclarativeSatelliteSource.

  It is built on the cute 'QObject', as Qt's QDeclarativeSatelliteSource is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QDeclarativeSatelliteSource is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeSatelliteSource that has a ritual and
  that Python can call so far, 34 names in all: 'metaObject', 'tr',
  'isActive', 'isValid', 'updateInterval', 'sourceError', 'name',
  'satellitesInUse', 'satellitesInView', 'setUpdateInterval', 'setActive',
  'setName', 'classBegin', 'componentComplete', 'setBackendProperty',
  'backendProperty', 'update', 'start', 'stop', 'activeChanged',
  'validityChanged', 'updateIntervalChanged', 'sourceErrorChanged',
  'nameChanged', 'satellitesInUseChanged', 'satellitesInViewChanged',
  'onParameterInitialized', 'satellitesInViewUpdateReceived',
  'satellitesInUseUpdateReceived', 'parameterMap', 'createSource',
  'handleSingleUpdateReceived', 'executeStart', 'executeSingleUpdate'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeSatelliteSource::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativeSatelliteSource::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeSatelliteSource::~QDeclarativeSatelliteSource()': the
    destructor: Python never removes a C++ QDeclarativeSatelliteSource.
  - Qt's 'QQmlListProperty<QDeclarativePluginParameter>
    QDeclarativeSatelliteSource::parameters()': gives a type Python has no
    way to take yet.
  - Qt's 'void QDeclarativeSatelliteSource::sourceErrorReceived(const
    QGeoSatelliteInfoSource::Error error)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QDeclarativeSatelliteSource::parameter_append(PluginParameterProperty
    *prop, QDeclarativePluginParameter *parameter)': names
    'QDeclarativeSatelliteSource::PluginParameterProperty', which has no cute
    class yet.
  - Qt's 'qsizetype
    QDeclarativeSatelliteSource::parameter_count(PluginParameterProperty
    *prop)': names 'QDeclarativeSatelliteSource::PluginParameterProperty',
    which has no cute class yet.
  - Qt's 'QDeclarativePluginParameter
    *QDeclarativeSatelliteSource::parameter_at(PluginParameterProperty *prop,
    qsizetype index)': names
    'QDeclarativeSatelliteSource::PluginParameterProperty', which has no cute
    class yet.
  - Qt's 'void
    QDeclarativeSatelliteSource::parameter_clear(PluginParameterProperty
    *prop)': names 'QDeclarativeSatelliteSource::PluginParameterProperty',
    which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeSatelliteSource is created at the first use, not by
    'QDeclarativeSatelliteSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeSatelliteSource.
  - Qt tells when it has removed the C++ QDeclarativeSatelliteSource. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeSatelliteSource that has no cute function
    yet, 'parameter_append', 'parameter_at', 'parameter_clear',
    'parameter_count', 'parameters', 'sourceErrorReceived', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativeSatelliteSource, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SourceError(CuteNum):
    """
    The enum 'QDeclarativeSatelliteSource::SourceError' of Qt, with the 5
    names Qt gives in it.
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
    Calls Qt's 'QString QDeclarativeSatelliteSource::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#tr

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
    #  QString QDeclarativeSatelliteSource::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QDeclarativeSatelliteSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeSatelliteSource'

  #  Qt's QDeclarativeSatelliteSource is built on more than one class. The
  #  part of a C++ QDeclarativeSatelliteSource that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeSatelliteSource_QQmlParserStatus',
  }

  #  A C++ QDeclarativeSatelliteSource Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeSatelliteSource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeSatelliteSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeSatelliteSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeSatelliteSource::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#isActive
    """
    #  bool QDeclarativeSatelliteSource::isActive() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource8isActiveEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeSatelliteSource::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#isValid
    """
    #  bool QDeclarativeSatelliteSource::isValid() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource7isValidEv',
    )

  def updateInterval(self) -> int:
    """
    Calls Qt's 'int QDeclarativeSatelliteSource::updateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#updateInterval
    """
    #  int QDeclarativeSatelliteSource::updateInterval() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource14updateIntervalEv',
    )

  def sourceError(self) -> SourceError:
    """
    Calls Qt's 'SourceError QDeclarativeSatelliteSource::sourceError()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#sourceError

    Returns
    -------

    SourceError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SourceError(number)'
      gives.
    """
    #  SourceError QDeclarativeSatelliteSource::sourceError() const
    return QDeclarativeSatelliteSource.SourceError(self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource11sourceErrorEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeSatelliteSource::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeSatelliteSource::name() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource4nameEv',
    )

  def satellitesInUse(self) -> QList[QGeoSatelliteInfo]:
    """
    Calls Qt's 'QList<QGeoSatelliteInfo>
    QDeclarativeSatelliteSource::satellitesInUse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#satellitesInUse

    Returns
    -------

    QList[QGeoSatelliteInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoSatelliteInfo>
    #      QDeclarativeSatelliteSource::satellitesInUse() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource15satellitesInUseEv',
    )
    from ..QtPositioning import QGeoSatelliteInfo
    return QList[QGeoSatelliteInfo]._cuteOwning(address)

  def satellitesInView(self) -> QList[QGeoSatelliteInfo]:
    """
    Calls Qt's 'QList<QGeoSatelliteInfo>
    QDeclarativeSatelliteSource::satellitesInView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#satellitesInView

    Returns
    -------

    QList[QGeoSatelliteInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoSatelliteInfo>
    #      QDeclarativeSatelliteSource::satellitesInView() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource16satellitesInViewEv',
    )
    from ..QtPositioning import QGeoSatelliteInfo
    return QList[QGeoSatelliteInfo]._cuteOwning(address)

  @overload(str)
  def backendProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeSatelliteSource::backendProperty(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#backendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeSatelliteSource::backendProperty(const QString
    #      &name) const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource15backendPropertyERK7QStrin'
        'g',
        name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def parameterMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QDeclarativeSatelliteSource::parameterMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#parameterMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QDeclarativeSatelliteSource::parameterMap() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSatelliteSource12parameterMapEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setUpdateInterval(self, updateInterval: int) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::setUpdateInterval(int
    updateInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#setUpdateInterval

    Parameters
    ----------

    updateInterval : int
      Passed on as it is.
    """
    #  void QDeclarativeSatelliteSource::setUpdateInterval(int
    #      updateInterval)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource17setUpdateIntervalEi',
        updateInterval,
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QDeclarativeSatelliteSource::setActive(bool active)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource9setActiveEb', active,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSatelliteSource::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource7setNameERK7QString', name,
    )

  @overload(str, QVariant)
  def setBackendProperty(self, name: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QDeclarativeSatelliteSource::setBackendProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QDeclarativeSatelliteSource::setBackendProperty(const QString
    #      &name, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource18setBackendPropertyERK7QStr'
        'ingRK8QVariant',
        name, self._valueOf(value),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeSatelliteSource::QDeclarativeSatelliteSource()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html
    """
    #  QDeclarativeSatelliteSource::QDeclarativeSatelliteSource()
    self._noteCreation(QDeclarativeSatelliteSource, lambda: Rituals.call(
        'ritual_ZN27QDeclarativeSatelliteSourceC1Ev',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#classBegin
    """
    #  void QDeclarativeSatelliteSource::classBegin()
    ritual = 'ritual_ZN27QDeclarativeSatelliteSource10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QDeclarativeSatelliteSource10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#componentComplete
    """
    #  void QDeclarativeSatelliteSource::componentComplete()
    ritual = 'ritual_ZN27QDeclarativeSatelliteSource17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeSatelliteSource17componentCompleteEv')
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def update(self, timeout: int = 0) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::update(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#update

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QDeclarativeSatelliteSource::update(int timeout)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource6updateEi', timeout,
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#start
    """
    #  void QDeclarativeSatelliteSource::start()
    self.uglySide.call('ritual_ZN27QDeclarativeSatelliteSource5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#stop
    """
    #  void QDeclarativeSatelliteSource::stop()
    self.uglySide.call('ritual_ZN27QDeclarativeSatelliteSource4stopEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#activeChanged
    """
    #  void QDeclarativeSatelliteSource::activeChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource13activeChangedEv',
    )

  def validityChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::validityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#validityChanged
    """
    #  void QDeclarativeSatelliteSource::validityChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource15validityChangedEv',
    )

  def updateIntervalChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::updateIntervalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html
    """
    #  void QDeclarativeSatelliteSource::updateIntervalChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource21updateIntervalChangedEv',
    )

  def sourceErrorChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::sourceErrorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html
    """
    #  void QDeclarativeSatelliteSource::sourceErrorChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource18sourceErrorChangedEv',
    )

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#nameChanged
    """
    #  void QDeclarativeSatelliteSource::nameChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource11nameChangedEv',
    )

  def satellitesInUseChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::satellitesInUseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html
    """
    #  void QDeclarativeSatelliteSource::satellitesInUseChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource22satellitesInUseChangedEv',
    )

  def satellitesInViewChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::satellitesInViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html
    """
    #  void QDeclarativeSatelliteSource::satellitesInViewChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource23satellitesInViewChangedEv',
    )

  def onParameterInitialized(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::onParameterInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html
    """
    #  void QDeclarativeSatelliteSource::onParameterInitialized()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource22onParameterInitializedEv',
    )

  @overload(QList[QGeoSatelliteInfo])
  def satellitesInViewUpdateReceived(
      self,
      satellites: QList[QGeoSatelliteInfo],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSatelliteSource::satellitesInViewUpdateReceived(const
    QList<QGeoSatelliteInfo> &satellites)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html

    Parameters
    ----------

    satellites : QList[QGeoSatelliteInfo]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeSatelliteSource::satellitesInViewUpdateReceived(const
    #      QList<QGeoSatelliteInfo> &satellites)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource30satellitesInViewUpdateRece'
        'ivedERK5QListI17QGeoSatelliteInfoE',
        self._valueOf(satellites),
    )

  @overload(QList[QGeoSatelliteInfo])
  def satellitesInUseUpdateReceived(
      self,
      satellites: QList[QGeoSatelliteInfo],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSatelliteSource::satellitesInUseUpdateReceived(const
    QList<QGeoSatelliteInfo> &satellites)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html

    Parameters
    ----------

    satellites : QList[QGeoSatelliteInfo]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeSatelliteSource::satellitesInUseUpdateReceived(const
    #      QList<QGeoSatelliteInfo> &satellites)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource29satellitesInUseUpdateRecei'
        'vedERK5QListI17QGeoSatelliteInfoE',
        self._valueOf(satellites),
    )

  @overload(str)
  def createSource(self, newName: str) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::createSource(const QString
    &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#createSource

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSatelliteSource::createSource(const QString &newName)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource12createSourceERK7QString',
        newName,
    )

  def handleSingleUpdateReceived(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSatelliteSource::handleSingleUpdateReceived()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html
    """
    #  void QDeclarativeSatelliteSource::handleSingleUpdateReceived()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource26handleSingleUpdateReceived'
        'Ev',
    )

  def executeStart(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::executeStart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html#executeStart
    """
    #  void QDeclarativeSatelliteSource::executeStart()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource12executeStartEv',
    )

  @overload(int)
  def executeSingleUpdate(self, timeout: int) -> None:
    """
    Calls Qt's 'void QDeclarativeSatelliteSource::executeSingleUpdate(int
    timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesatellitesource.html

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QDeclarativeSatelliteSource::executeSingleUpdate(int timeout)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSatelliteSource19executeSingleUpdateEi',
        timeout,
    )

  @staticmethod
  def parameter_append(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeSatelliteSource::parameter_append(PluginParameterProperty
    *prop, QDeclarativePluginParameter *parameter)': names
    'QDeclarativeSatelliteSource::PluginParameterProperty', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSatelliteSource.parameter_append' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeSatelliteSource::parameter_append(PluginParameterProper"
        "ty *prop, QDeclarativePluginParameter *parameter)': names "
        "'QDeclarativeSatelliteSource::PluginParameterProperty', which has "
        "no cute class yet.")

  @staticmethod
  def parameter_at(*__, **_) -> Never:
    """
    Qt's 'QDeclarativePluginParameter
    *QDeclarativeSatelliteSource::parameter_at(PluginParameterProperty *prop,
    qsizetype index)': names
    'QDeclarativeSatelliteSource::PluginParameterProperty', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSatelliteSource.parameter_at' has no cute function "
        "yet. Qt's 'QDeclarativePluginParameter "
        "*QDeclarativeSatelliteSource::parameter_at(PluginParameterProperty "
        "*prop, qsizetype index)': names "
        "'QDeclarativeSatelliteSource::PluginParameterProperty', which has "
        "no cute class yet.")

  @staticmethod
  def parameter_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeSatelliteSource::parameter_clear(PluginParameterProperty
    *prop)': names 'QDeclarativeSatelliteSource::PluginParameterProperty',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSatelliteSource.parameter_clear' has no cute function "
        "yet. Qt's 'void "
        "QDeclarativeSatelliteSource::parameter_clear(PluginParameterPropert"
        "y *prop)': names "
        "'QDeclarativeSatelliteSource::PluginParameterProperty', which has "
        "no cute class yet.")

  @staticmethod
  def parameter_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QDeclarativeSatelliteSource::parameter_count(PluginParameterProperty
    *prop)': names 'QDeclarativeSatelliteSource::PluginParameterProperty',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSatelliteSource.parameter_count' has no cute function "
        "yet. Qt's 'qsizetype "
        "QDeclarativeSatelliteSource::parameter_count(PluginParameterPropert"
        "y *prop)': names "
        "'QDeclarativeSatelliteSource::PluginParameterProperty', which has "
        "no cute class yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QDeclarativePluginParameter>
    QDeclarativeSatelliteSource::parameters()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSatelliteSource.parameters' has no cute function yet. "
        "Qt's 'QQmlListProperty<QDeclarativePluginParameter> "
        "QDeclarativeSatelliteSource::parameters()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def sourceErrorReceived(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeSatelliteSource::sourceErrorReceived(const
    QGeoSatelliteInfoSource::Error error)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSatelliteSource.sourceErrorReceived' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeSatelliteSource::sourceErrorReceived(const "
        "QGeoSatelliteInfoSource::Error error)': takes a type Python has no "
        "way to hand over yet.")
