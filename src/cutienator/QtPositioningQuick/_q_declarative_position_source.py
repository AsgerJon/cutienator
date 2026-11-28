"""
QDeclarativePositionSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativepositionsource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePositionSource to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtPositioning import QGeoPositionInfo, QGeoPositionInfoSource
  from . import QDeclarativePosition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoPositionInfo = WAIT['QGeoPositionInfo']
  QGeoPositionInfoSource = WAIT['QGeoPositionInfoSource']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativePositionSource(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativePositionSource: a plain Python object
  standing in front of one C++ QDeclarativePositionSource.

  It is built on the cute 'QObject', as Qt's QDeclarativePositionSource is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QDeclarativePositionSource is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePositionSource that has a ritual and
  that Python can call so far, 47 names in all: 'metaObject', 'tr',
  'setUpdateInterval', 'setActive', 'setPreferredPositioningMethods', 'name',
  'setName', 'updateInterval', 'isActive', 'isValid', 'position',
  'supportedPositioningMethods', 'preferredPositioningMethods',
  'sourceError', 'positionSource', 'parameterMap', 'classBegin',
  'componentComplete', 'setBackendProperty', 'backendProperty', 'update',
  'start', 'stop', 'positionChanged', 'activeChanged',
  'updateIntervalChanged', 'supportedPositioningMethodsChanged',
  'preferredPositioningMethodsChanged', 'sourceErrorChanged', 'nameChanged',
  'validityChanged', 'positionUpdateReceived', 'onParameterInitialized',
  'notifySupportedPositioningMethodsChanged', 'setPosition', 'setSource',
  'parametersReady', 'tryAttach', 'isValidActualComputation',
  'supportedMethodsActualComputation', 'executeStart',
  '_qt_property_m_sourceName_offset', '_qt_property_m_active_offset',
  '_qt_property_m_position_offset', '_qt_property_m_sourceError_offset',
  '_qt_property_m_supportedPositioningMethods_offset',
  '_qt_property_m_isValid_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativePositionSource::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativePositionSource::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativePositionSource::~QDeclarativePositionSource()': the
    destructor: Python never removes a C++ QDeclarativePositionSource.
  - Qt's 'QQmlListProperty<QDeclarativePluginParameter>
    QDeclarativePositionSource::parameters()': gives a type Python has no way
    to take yet.
  - Qt's 'QBindable<PositioningMethods>
    QDeclarativePositionSource::bindableSupportedPositioningMethods() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<SourceError>
    QDeclarativePositionSource::bindableSourceError() const': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<bool> QDeclarativePositionSource::bindableIsValid()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<QString> QDeclarativePositionSource::bindableName()':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<QDeclarativePosition *>
    QDeclarativePositionSource::bindablePosition() const': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<bool> QDeclarativePositionSource::bindableActive()':
    gives a type Python has no way to take yet.
  - Qt's 'void QDeclarativePositionSource::sourceErrorReceived(const
    QGeoPositionInfoSource::Error error)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QDeclarativePositionSource::parameter_append(
    QQmlListProperty<QDeclarativePluginParameter> *prop,
    QDeclarativePluginParameter *mapObject)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
  - Qt's 'qsizetype QDeclarativePositionSource::parameter_count(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
  - Qt's 'QDeclarativePluginParameter
    *QDeclarativePositionSource::parameter_at(
    QQmlListProperty<QDeclarativePluginParameter> *prop, qsizetype index)':
    names 'QQmlListProperty<QDeclarativePluginParameter>', which has no cute
    class yet.
  - Qt's 'void QDeclarativePositionSource::parameter_clear(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 65 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativePositionSource is created at the first use, not by
    'QDeclarativePositionSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePositionSource.
  - Qt tells when it has removed the C++ QDeclarativePositionSource. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativePositionSource that has no cute function
    yet, 'bindableActive', 'bindableIsValid', 'bindableName',
    'bindablePosition', 'bindableSourceError',
    'bindableSupportedPositioningMethods', 'parameter_append',
    'parameter_at', 'parameter_clear', 'parameter_count', 'parameters',
    'sourceErrorReceived', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativePositionSource, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class PositioningMethod(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QDeclarativePositionSource::PositioningMethod' of Qt,
    with the 4 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativePositionSource::PositioningMethods'.
    """

    NoPositioningMethods = 0x0
    SatellitePositioningMethods = 0xff
    NonSatellitePositioningMethods = 0xffffff00
    AllPositioningMethods = 0xffffffff

  PositioningMethods = PositioningMethod

  class SourceError(CuteNum):
    """
    The enum 'QDeclarativePositionSource::SourceError' of Qt, with the 5
    names Qt gives in it.
    """

    AccessError = Kee[int](0)
    ClosedError = Kee[int](1)
    UnknownSourceError = Kee[int](2)
    NoError = Kee[int](3)
    UpdateTimeoutError = Kee[int](4)

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
    Calls Qt's 'QString QDeclarativePositionSource::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativepositionsource.html#tr

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
    #  QString QDeclarativePositionSource::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QDeclarativePositionSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_sourceName_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePositionSource::_qt_property_m_sourceName_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  size_t QDeclarativePositionSource::_qt_property_m_sourceName_offset()
    return Rituals.call(
        'ritual_ZN26QDeclarativePositionSource32_qt_property_m_sourceName_o'
        'ffsetEv',
    )

  @staticmethod
  def _qt_property_m_active_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePositionSource::_qt_property_m_active_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  size_t QDeclarativePositionSource::_qt_property_m_active_offset()
    return Rituals.call(
        'ritual_ZN26QDeclarativePositionSource28_qt_property_m_active_offse'
        'tEv',
    )

  @staticmethod
  def _qt_property_m_position_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePositionSource::_qt_property_m_position_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  size_t QDeclarativePositionSource::_qt_property_m_position_offset()
    return Rituals.call(
        'ritual_ZN26QDeclarativePositionSource30_qt_property_m_position_off'
        'setEv',
    )

  @staticmethod
  def _qt_property_m_sourceError_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePositionSource::_qt_property_m_sourceError_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  size_t QDeclarativePositionSource::_qt_property_m_sourceError_offset()
    return Rituals.call(
        'ritual_ZN26QDeclarativePositionSource33_qt_property_m_sourceError_'
        'offsetEv',
    )

  @staticmethod
  def _qt_property_m_supportedPositioningMethods_offset() -> int:
    """
    Calls Qt's 'size_t QDeclarativePositionSource::
    _qt_property_m_supportedPositioningMethods_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  size_t QDeclarativePositionSource::
    #      _qt_property_m_supportedPositioningMethods_offset()
    return Rituals.call(
        'ritual_ZN26QDeclarativePositionSource49_qt_property_m_supportedPos'
        'itioningMethods_offsetEv',
    )

  @staticmethod
  def _qt_property_m_isValid_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePositionSource::_qt_property_m_isValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  size_t QDeclarativePositionSource::_qt_property_m_isValid_offset()
    return Rituals.call(
        'ritual_ZN26QDeclarativePositionSource29_qt_property_m_isValid_offs'
        'etEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativePositionSource'

  #  Qt's QDeclarativePositionSource is built on more than one class. The
  #  part of a C++ QDeclarativePositionSource that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativePositionSource_QQmlParserStatus',
  }

  #  A C++ QDeclarativePositionSource Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePositionSource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativePositionSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativePositionSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePositionSource::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePositionSource::name() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource4nameEv',
    )

  def updateInterval(self) -> int:
    """
    Calls Qt's 'int QDeclarativePositionSource::updateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#updateInterval
    """
    #  int QDeclarativePositionSource::updateInterval() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource14updateIntervalEv',
    )

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePositionSource::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#isActive
    """
    #  bool QDeclarativePositionSource::isActive() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource8isActiveEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePositionSource::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#isValid
    """
    #  bool QDeclarativePositionSource::isValid() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource7isValidEv',
    )

  def supportedPositioningMethods(self) -> PositioningMethods:
    """
    Calls Qt's 'PositioningMethods
    QDeclarativePositionSource::supportedPositioningMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html

    Returns
    -------

    PositioningMethods
      The value standing for the combination Qt gave back.
    """
    #  PositioningMethods
    #      QDeclarativePositionSource::supportedPositioningMethods() const
    return QDeclarativePositionSource.PositioningMethods(self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource27supportedPositioningMethod'
        'sEv',
    ))

  def preferredPositioningMethods(self) -> PositioningMethods:
    """
    Calls Qt's 'PositioningMethods
    QDeclarativePositionSource::preferredPositioningMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html

    Returns
    -------

    PositioningMethods
      The value standing for the combination Qt gave back.
    """
    #  PositioningMethods
    #      QDeclarativePositionSource::preferredPositioningMethods() const
    return QDeclarativePositionSource.PositioningMethods(self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource27preferredPositioningMethod'
        'sEv',
    ))

  def sourceError(self) -> SourceError:
    """
    Calls Qt's 'SourceError QDeclarativePositionSource::sourceError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#sourceError

    Returns
    -------

    SourceError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SourceError(number)'
      gives.
    """
    #  SourceError QDeclarativePositionSource::sourceError() const
    return QDeclarativePositionSource.SourceError(self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource11sourceErrorEv',
    ))

  def positionSource(self) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QDeclarativePositionSource::positionSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#positionSource

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource *QDeclarativePositionSource::positionSource()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource14positionSourceEv',
    )
    from ..QtPositioning import QGeoPositionInfoSource
    return QGeoPositionInfoSource._cuteAt(address)

  def parameterMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QDeclarativePositionSource::parameterMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#parameterMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QDeclarativePositionSource::parameterMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource12parameterMapEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(str)
  def backendProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativePositionSource::backendProperty(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#backendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativePositionSource::backendProperty(const QString
    #      &name) const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource15backendPropertyERK7QString',
        name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isValidActualComputation(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePositionSource::isValidActualComputation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  bool QDeclarativePositionSource::isValidActualComputation() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource24isValidActualComputationEv',
    )

  def supportedMethodsActualComputation(self) -> PositioningMethods:
    """
    Calls Qt's 'PositioningMethods
    QDeclarativePositionSource::supportedMethodsActualComputation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html

    Returns
    -------

    PositioningMethods
      The value standing for the combination Qt gave back.
    """
    #  PositioningMethods
    #      QDeclarativePositionSource::supportedMethodsActualComputation()
    #      const
    return QDeclarativePositionSource.PositioningMethods(self.uglySide.call(
        'ritual_ZNK26QDeclarativePositionSource33supportedMethodsActualComp'
        'utationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setUpdateInterval(self, updateInterval: int) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::setUpdateInterval(int
    updateInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#setUpdateInterval

    Parameters
    ----------

    updateInterval : int
      Passed on as it is.
    """
    #  void QDeclarativePositionSource::setUpdateInterval(int updateInterval)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource17setUpdateIntervalEi',
        updateInterval,
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QDeclarativePositionSource::setActive(bool active)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource9setActiveEb', active,
    )

  @overload(PositioningMethods)
  def setPreferredPositioningMethods(
      self,
      methods: PositioningMethods,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativePositionSource::setPreferredPositioningMethods(
    PositioningMethods methods)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html

    Parameters
    ----------

    methods : PositioningMethods
      Passed on as its number.
    """
    #  void QDeclarativePositionSource::setPreferredPositioningMethods(
    #      PositioningMethods methods)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource30setPreferredPositioningMeth'
        'odsE6QFlagsINS_17PositioningMethodEE',
        methods.value,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativePositionSource::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource7setNameERK7QString', name,
    )

  @overload(str, QVariant)
  def setBackendProperty(self, name: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QDeclarativePositionSource::setBackendProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#setBackendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QDeclarativePositionSource::setBackendProperty(const QString
    #      &name, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource18setBackendPropertyERK7QStri'
        'ngRK8QVariant',
        name, self._valueOf(value),
    )

  @overload(QGeoPositionInfo)
  def setPosition(self, pi: QGeoPositionInfo) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::setPosition(const
    QGeoPositionInfo &pi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#setPosition

    Parameters
    ----------

    pi : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  void QDeclarativePositionSource::setPosition(const QGeoPositionInfo
    #      &pi)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource11setPositionERK16QGeoPositio'
        'nInfo',
        self._valueOf(pi),
    )

  @overload(QGeoPositionInfoSource)
  @overload(NoneType)
  def setSource(self, source: Optional[QGeoPositionInfoSource]) -> None:
    """
    Calls Qt's 'void
    QDeclarativePositionSource::setSource(QGeoPositionInfoSource *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#setSource

    Parameters
    ----------

    source : Optional[QGeoPositionInfoSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePositionSource::setSource(QGeoPositionInfoSource
    #      *source)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource9setSourceEP22QGeoPositionInf'
        'oSource',
        self._addressOf(source),
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
    'QDeclarativePositionSource::QDeclarativePositionSource()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  QDeclarativePositionSource::QDeclarativePositionSource()
    self._noteCreation(QDeclarativePositionSource, lambda: Rituals.call(
        'ritual_ZN26QDeclarativePositionSourceC1Ev',
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

  def position(self) -> Optional[QDeclarativePosition]:
    """
    Calls Qt's 'QDeclarativePosition
    *QDeclarativePositionSource::position()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#position

    Returns
    -------

    Optional[QDeclarativePosition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativePosition *QDeclarativePositionSource::position()
    address = self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource8positionEv',
    )
    from . import QDeclarativePosition
    return QDeclarativePosition._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#classBegin
    """
    #  void QDeclarativePositionSource::classBegin()
    ritual = 'ritual_ZN26QDeclarativePositionSource10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QDeclarativePositionSource10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#componentComplete
    """
    #  void QDeclarativePositionSource::componentComplete()
    ritual = 'ritual_ZN26QDeclarativePositionSource17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativePositionSource17componentCompleteEv')
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def update(self, timeout: int = 0) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::update(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#update

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QDeclarativePositionSource::update(int timeout)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource6updateEi', timeout,
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#start
    """
    #  void QDeclarativePositionSource::start()
    self.uglySide.call('ritual_ZN26QDeclarativePositionSource5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#stop
    """
    #  void QDeclarativePositionSource::stop()
    self.uglySide.call('ritual_ZN26QDeclarativePositionSource4stopEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#positionChanged
    """
    #  void QDeclarativePositionSource::positionChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource15positionChangedEv',
    )

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#activeChanged
    """
    #  void QDeclarativePositionSource::activeChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource13activeChangedEv',
    )

  def updateIntervalChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::updateIntervalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  void QDeclarativePositionSource::updateIntervalChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource21updateIntervalChangedEv',
    )

  def supportedPositioningMethodsChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePositionSource::supportedPositioningMethodsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  void QDeclarativePositionSource::supportedPositioningMethodsChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource34supportedPositioningMethods'
        'ChangedEv',
    )

  def preferredPositioningMethodsChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePositionSource::preferredPositioningMethodsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  void QDeclarativePositionSource::preferredPositioningMethodsChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource34preferredPositioningMethods'
        'ChangedEv',
    )

  def sourceErrorChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::sourceErrorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#sourceErrorChanged
    """
    #  void QDeclarativePositionSource::sourceErrorChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource18sourceErrorChangedEv',
    )

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#nameChanged
    """
    #  void QDeclarativePositionSource::nameChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource11nameChangedEv',
    )

  def validityChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::validityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#validityChanged
    """
    #  void QDeclarativePositionSource::validityChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource15validityChangedEv',
    )

  @overload(QGeoPositionInfo)
  def positionUpdateReceived(self, update: QGeoPositionInfo) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::positionUpdateReceived(const
    QGeoPositionInfo &update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html

    Parameters
    ----------

    update : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  void QDeclarativePositionSource::positionUpdateReceived(const
    #      QGeoPositionInfo &update)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource22positionUpdateReceivedERK16'
        'QGeoPositionInfo',
        self._valueOf(update),
    )

  def onParameterInitialized(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::onParameterInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  void QDeclarativePositionSource::onParameterInitialized()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource22onParameterInitializedEv',
    )

  def notifySupportedPositioningMethodsChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePositionSource::notifySupportedPositioningMethodsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html
    """
    #  void QDeclarativePositionSource::
    #      notifySupportedPositioningMethodsChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource40notifySupportedPositioningM'
        'ethodsChangedEv',
    )

  def parametersReady(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePositionSource::parametersReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#parametersReady
    """
    #  bool QDeclarativePositionSource::parametersReady()
    return self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource15parametersReadyEv',
    )

  @overload(str)
  @overload(str, bool)
  def tryAttach(self, name: str, useFallback: bool = True) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::tryAttach(const QString
    &name, bool useFallback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#tryAttach

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    useFallback : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativePositionSource::tryAttach(const QString &name, bool
    #      useFallback)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource9tryAttachERK7QStringb',
        name, useFallback,
    )

  def executeStart(self) -> None:
    """
    Calls Qt's 'void QDeclarativePositionSource::executeStart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepositionsource.html#executeStart
    """
    #  void QDeclarativePositionSource::executeStart()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePositionSource12executeStartEv',
    )

  @staticmethod
  def bindableActive(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePositionSource::bindableActive()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.bindableActive' has no cute function "
        "yet. Qt's 'QBindable<bool> "
        "QDeclarativePositionSource::bindableActive()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableIsValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePositionSource::bindableIsValid()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.bindableIsValid' has no cute function "
        "yet. Qt's 'QBindable<bool> "
        "QDeclarativePositionSource::bindableIsValid() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableName(*__, **_) -> Never:
    """
    Qt's 'QBindable<QString> QDeclarativePositionSource::bindableName()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.bindableName' has no cute function "
        "yet. Qt's 'QBindable<QString> "
        "QDeclarativePositionSource::bindableName()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindablePosition(*__, **_) -> Never:
    """
    Qt's 'QBindable<QDeclarativePosition *>
    QDeclarativePositionSource::bindablePosition() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.bindablePosition' has no cute function "
        "yet. Qt's 'QBindable<QDeclarativePosition *> "
        "QDeclarativePositionSource::bindablePosition() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableSourceError(*__, **_) -> Never:
    """
    Qt's 'QBindable<SourceError>
    QDeclarativePositionSource::bindableSourceError() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.bindableSourceError' has no cute "
        "function yet. Qt's 'QBindable<SourceError> "
        "QDeclarativePositionSource::bindableSourceError() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableSupportedPositioningMethods(*__, **_) -> Never:
    """
    Qt's 'QBindable<PositioningMethods>
    QDeclarativePositionSource::bindableSupportedPositioningMethods() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.bindableSupportedPositioningMethods' "
        "has no cute function yet. Qt's 'QBindable<PositioningMethods> "
        "QDeclarativePositionSource::bindableSupportedPositioningMethods() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def parameter_append(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativePositionSource::parameter_append(
    QQmlListProperty<QDeclarativePluginParameter> *prop,
    QDeclarativePluginParameter *mapObject)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.parameter_append' has no cute function "
        "yet. Qt's 'void "
        "QDeclarativePositionSource::parameter_append(QQmlListProperty<QDecl"
        "arativePluginParameter> *prop, QDeclarativePluginParameter "
        "*mapObject)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameter_at(*__, **_) -> Never:
    """
    Qt's 'QDeclarativePluginParameter
    *QDeclarativePositionSource::parameter_at(
    QQmlListProperty<QDeclarativePluginParameter> *prop, qsizetype index)':
    names 'QQmlListProperty<QDeclarativePluginParameter>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.parameter_at' has no cute function "
        "yet. Qt's 'QDeclarativePluginParameter "
        "*QDeclarativePositionSource::parameter_at(QQmlListProperty<QDeclara"
        "tivePluginParameter> *prop, qsizetype index)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameter_clear(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativePositionSource::parameter_clear(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.parameter_clear' has no cute function "
        "yet. Qt's 'void "
        "QDeclarativePositionSource::parameter_clear(QQmlListProperty<QDecla"
        "rativePluginParameter> *prop)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameter_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDeclarativePositionSource::parameter_count(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.parameter_count' has no cute function "
        "yet. Qt's 'qsizetype "
        "QDeclarativePositionSource::parameter_count(QQmlListProperty<QDecla"
        "rativePluginParameter> *prop)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QDeclarativePluginParameter>
    QDeclarativePositionSource::parameters()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.parameters' has no cute function yet. "
        "Qt's 'QQmlListProperty<QDeclarativePluginParameter> "
        "QDeclarativePositionSource::parameters()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def sourceErrorReceived(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativePositionSource::sourceErrorReceived(const
    QGeoPositionInfoSource::Error error)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativePositionSource.sourceErrorReceived' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativePositionSource::sourceErrorReceived(const "
        "QGeoPositionInfoSource::Error error)': takes a type Python has no "
        "way to hand over yet.")
