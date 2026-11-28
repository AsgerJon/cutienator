"""
QGeoAreaMonitorSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeoareamonitorsource.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QGeoAreaMonitorInfo, QGeoPositionInfo, QGeoPositionInfoSource
  from . import QGeoShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoAreaMonitorInfo = WAIT['QGeoAreaMonitorInfo']
  QGeoPositionInfo = WAIT['QGeoPositionInfo']
  QGeoPositionInfoSource = WAIT['QGeoPositionInfoSource']
  QGeoShape = WAIT['QGeoShape']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoAreaMonitorSource(QObject):
  """
  The cute side of Qt's QGeoAreaMonitorSource: a plain Python object standing
  in front of one C++ QGeoAreaMonitorSource.

  It is built on the cute 'QObject', as Qt's QGeoAreaMonitorSource is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoAreaMonitorSource that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr',
  'createDefaultSource', 'createSource', 'availableSources',
  'setPositionInfoSource', 'positionInfoSource', 'sourceName', 'error',
  'supportedAreaMonitorFeatures', 'startMonitoring', 'stopMonitoring',
  'requestUpdate', 'activeMonitors', 'setBackendProperty', 'backendProperty',
  'areaEntered', 'areaExited', 'monitorExpired', 'errorOccurred'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoAreaMonitorSource::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGeoAreaMonitorSource::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoAreaMonitorSource::~QGeoAreaMonitorSource()': the destructor:
    Python never removes a C++ QGeoAreaMonitorSource.
  - Qt's 'QGeoAreaMonitorSourcePrivate *QGeoAreaMonitorSource::d_func()':
    gives 'QGeoAreaMonitorSourcePrivate', which has no cute class yet.
  - Qt's 'const QGeoAreaMonitorSourcePrivate *QGeoAreaMonitorSource::d_func()
    const': gives 'QGeoAreaMonitorSourcePrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  5 of the 31 functions Qt declares: 2 not a gap; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QGeoAreaMonitorSource is created at the first use, not by
    'QGeoAreaMonitorSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoAreaMonitorSource.
  - Qt tells when it has removed the C++ QGeoAreaMonitorSource. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoAreaMonitorSource that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QGeoAreaMonitorSource, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AreaMonitorFeature(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QGeoAreaMonitorSource::AreaMonitorFeature' of Qt, with
    the 2 names Qt gives in it. Qt names the type of its combinations
    'QGeoAreaMonitorSource::AreaMonitorFeatures'.
    """

    PersistentAreaMonitorFeature = 0x1
    AnyAreaMonitorFeature = 0xffffffff

  AreaMonitorFeatures = AreaMonitorFeature

  class Error(CuteNum):
    """
    The enum 'QGeoAreaMonitorSource::Error' of Qt, with the 4 names Qt gives
    in it.
    """

    AccessError = Kee[int](0)
    InsufficientPositionInfo = Kee[int](1)
    UnknownSourceError = Kee[int](2)
    NoError = Kee[int](3)

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
    Calls Qt's 'QString QGeoAreaMonitorSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorsource.html#tr

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
    #  QString QGeoAreaMonitorSource::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QGeoAreaMonitorSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def createDefaultSource(
      parent: Optional[QObject],
  ) -> Optional[QGeoAreaMonitorSource]:
    """
    Calls Qt's 'QGeoAreaMonitorSource
    *QGeoAreaMonitorSource::createDefaultSource(QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#createDefaultSource

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoAreaMonitorSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoAreaMonitorSource
    #      *QGeoAreaMonitorSource::createDefaultSource(QObject *parent)
    address = Rituals.call(
        'ritual_ZN21QGeoAreaMonitorSource19createDefaultSourceEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoAreaMonitorSource._cuteAt(address)

  @staticmethod
  @overload(str, QObject)
  @overload(str, NoneType)
  def createSource(
      sourceName: str,
      parent: Optional[QObject],
  ) -> Optional[QGeoAreaMonitorSource]:
    """
    Calls Qt's 'QGeoAreaMonitorSource
    *QGeoAreaMonitorSource::createSource(const QString &sourceName, QObject
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#createSource

    Parameters
    ----------

    sourceName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoAreaMonitorSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoAreaMonitorSource *QGeoAreaMonitorSource::createSource(const
    #      QString &sourceName, QObject *parent)
    address = Rituals.call(
        'ritual_ZN21QGeoAreaMonitorSource12createSourceERK7QStringP7QObject',
        sourceName, CuteMixin._addressOf(parent, 'QObject'),
    )
    return QGeoAreaMonitorSource._cuteAt(address)

  @staticmethod
  def availableSources() -> QStringList:
    """
    Calls Qt's 'QStringList QGeoAreaMonitorSource::availableSources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#availableSources

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGeoAreaMonitorSource::availableSources()
    address = Rituals.call(
        'ritual_ZN21QGeoAreaMonitorSource16availableSourcesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoAreaMonitorSource'

  #  A C++ QGeoAreaMonitorSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoAreaMonitorSource'

  #  The functions Qt calls itself that QGeoAreaMonitorSource is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'requestUpdate': (
          'bool QGeoAreaMonitorSource::requestUpdate(const '
          'QGeoAreaMonitorInfo &, const char *)',
      ),
      'activeMonitors': (
          'QList<QGeoAreaMonitorInfo> '
          'QGeoAreaMonitorSource::activeMonitors() const',
          'QList<QGeoAreaMonitorInfo> '
          'QGeoAreaMonitorSource::activeMonitors(const QGeoShape &) const',
      ),
  }

  #  The functions Qt calls itself that QGeoAreaMonitorSource is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setPositionInfoSource': (
          ('_ZN21QGeoAreaMonitorSource21setPositionInfoSourceEP22QGeoPositi'
           'onInfoSource',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtPositioning:QGeoPositionInfoSource'),
           )),
      ),
      'positionInfoSource': (
          ('_ZNK21QGeoAreaMonitorSource18positionInfoSourceEv',
           ('address', 'address', 'QtPositioning:QGeoPositionInfoSource'),
           ()),
      ),
      'error': (
          ('_ZNK21QGeoAreaMonitorSource5errorEv',
           ('int', 'enum', 'QtPositioning:QGeoAreaMonitorSource.Error'),
           ()),
      ),
      'supportedAreaMonitorFeatures': (
          ('_ZNK21QGeoAreaMonitorSource28supportedAreaMonitorFeaturesEv',
           ('int', 'flags',
            'QtPositioning:QGeoAreaMonitorSource.AreaMonitorFeature'),
           ()),
      ),
      'startMonitoring': (
          ('_ZN21QGeoAreaMonitorSource15startMonitoringERK19QGeoAreaMonitor'
           'Info',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoAreaMonitorInfo'),
           )),
      ),
      'stopMonitoring': (
          ('_ZN21QGeoAreaMonitorSource14stopMonitoringERK19QGeoAreaMonitorI'
           'nfo',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoAreaMonitorInfo'),
           )),
      ),
      'setBackendProperty': (
          ('_ZN21QGeoAreaMonitorSource18setBackendPropertyERK7QStringRK8QVa'
           'riant',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'backendProperty': (
          ('_ZNK21QGeoAreaMonitorSource15backendPropertyERK7QString',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
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
    Calls Qt's 'const QMetaObject *QGeoAreaMonitorSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoAreaMonitorSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QGeoAreaMonitorSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def positionInfoSource(self) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QGeoAreaMonitorSource::positionInfoSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#positionInfoSource

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource *QGeoAreaMonitorSource::positionInfoSource()
    #      const
    ritual = 'ritual_ZNK21QGeoAreaMonitorSource18positionInfoSourceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QGeoAreaMonitorSource18positionInfoSourceEv'
    address = self.uglySide.call(ritual)
    from . import QGeoPositionInfoSource
    return QGeoPositionInfoSource._cuteAt(address)

  def sourceName(self) -> str:
    """
    Calls Qt's 'QString QGeoAreaMonitorSource::sourceName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#sourceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAreaMonitorSource::sourceName() const
    return self.uglySide.call(
        'ritual_ZNK21QGeoAreaMonitorSource10sourceNameEv',
    )

  def error(self) -> Error:
    """
    Calls Qt's 'Error QGeoAreaMonitorSource::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorsource.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoAreaMonitorSource::error() const
    return QGeoAreaMonitorSource.Error(self.uglySide.call(
        'ritual_ZNK21QGeoAreaMonitorSource5errorEv',
    ))

  def supportedAreaMonitorFeatures(self) -> AreaMonitorFeatures:
    """
    Calls Qt's 'AreaMonitorFeatures
    QGeoAreaMonitorSource::supportedAreaMonitorFeatures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html

    Returns
    -------

    AreaMonitorFeatures
      The value standing for the combination Qt gave back.
    """
    #  AreaMonitorFeatures
    #      QGeoAreaMonitorSource::supportedAreaMonitorFeatures() const
    return QGeoAreaMonitorSource.AreaMonitorFeatures(self.uglySide.call(
        'ritual_ZNK21QGeoAreaMonitorSource28supportedAreaMonitorFeaturesEv',
    ))

  @overload()
  def activeMonitors(self) -> QList[QGeoAreaMonitorInfo]:
    """
    Calls Qt's 'QList<QGeoAreaMonitorInfo>
    QGeoAreaMonitorSource::activeMonitors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#activeMonitors

    Returns
    -------

    QList[QGeoAreaMonitorInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoAreaMonitorInfo> QGeoAreaMonitorSource::activeMonitors()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QGeoAreaMonitorSource14activeMonitorsEv',
    )
    from . import QGeoAreaMonitorInfo
    return QList[QGeoAreaMonitorInfo]._cuteOwning(address)

  @overload(QGeoShape)
  def activeMonitors(
      self,
      lookupArea: QGeoShape,
  ) -> QList[QGeoAreaMonitorInfo]:
    """
    Calls Qt's 'QList<QGeoAreaMonitorInfo>
    QGeoAreaMonitorSource::activeMonitors(const QGeoShape &lookupArea)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#activeMonitors

    Parameters
    ----------

    lookupArea : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    QList[QGeoAreaMonitorInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoAreaMonitorInfo> QGeoAreaMonitorSource::activeMonitors(const
    #      QGeoShape &lookupArea) const
    address = self.uglySide.call(
        'ritual_ZNK21QGeoAreaMonitorSource14activeMonitorsERK9QGeoShape',
        self._valueOf(lookupArea),
    )
    from . import QGeoAreaMonitorInfo
    return QList[QGeoAreaMonitorInfo]._cuteOwning(address)

  @overload(str)
  def backendProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QGeoAreaMonitorSource::backendProperty(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#backendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGeoAreaMonitorSource::backendProperty(const QString &name)
    #      const
    ritual = 'ritual_ZNK21QGeoAreaMonitorSource15backendPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QGeoAreaMonitorSource15backendPropertyERK7QStrin'
          'g')
    address = self.uglySide.call(ritual, name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoPositionInfoSource)
  @overload(NoneType)
  def setPositionInfoSource(
      self,
      source: Optional[QGeoPositionInfoSource],
  ) -> None:
    """
    Calls Qt's 'void
    QGeoAreaMonitorSource::setPositionInfoSource(QGeoPositionInfoSource
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#setPositionInfoSource

    Parameters
    ----------

    source : Optional[QGeoPositionInfoSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoAreaMonitorSource::setPositionInfoSource(
    #      QGeoPositionInfoSource *source)
    ritual = (
        'ritual_ZN21QGeoAreaMonitorSource21setPositionInfoSourceEP22QGeoPos'
        'itionInfoSource')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QGeoAreaMonitorSource21setPositionInfoSourceEP22Q'
          'GeoPositionInfoSource')
    self.uglySide.call(ritual, self._addressOf(source))

  @overload(str, QVariant)
  def setBackendProperty(self, name: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QGeoAreaMonitorSource::setBackendProperty(const QString
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#setBackendProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QGeoAreaMonitorSource::setBackendProperty(const QString &name,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN21QGeoAreaMonitorSource18setBackendPropertyERK7QStringRK8'
        'QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QGeoAreaMonitorSource18setBackendPropertyERK7QStr'
          'ingRK8QVariant')
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGeoAreaMonitorSource::QGeoAreaMonitorSource(QObject *parent)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QGeoAreaMonitorSource.__init__' has no cute function yet. Qt's "
        "'QGeoAreaMonitorSource::QGeoAreaMonitorSource(QObject *parent)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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

  @overload(QGeoAreaMonitorInfo)
  def startMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool:
    """
    Calls Qt's 'bool QGeoAreaMonitorSource::startMonitoring(const
    QGeoAreaMonitorInfo &monitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#startMonitoring

    Parameters
    ----------

    monitor : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.
    """
    #  bool QGeoAreaMonitorSource::startMonitoring(const QGeoAreaMonitorInfo
    #      &monitor)
    return self.uglySide.call(
        'ritual_ZN21QGeoAreaMonitorSource15startMonitoringERK19QGeoAreaMoni'
        'torInfo',
        self._valueOf(monitor),
    )

  @overload(QGeoAreaMonitorInfo)
  def stopMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool:
    """
    Calls Qt's 'bool QGeoAreaMonitorSource::stopMonitoring(const
    QGeoAreaMonitorInfo &monitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#stopMonitoring

    Parameters
    ----------

    monitor : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.
    """
    #  bool QGeoAreaMonitorSource::stopMonitoring(const QGeoAreaMonitorInfo
    #      &monitor)
    return self.uglySide.call(
        'ritual_ZN21QGeoAreaMonitorSource14stopMonitoringERK19QGeoAreaMonit'
        'orInfo',
        self._valueOf(monitor),
    )

  @overload(QGeoAreaMonitorInfo, str)
  @overload(QGeoAreaMonitorInfo, NoneType)
  def requestUpdate(
      self,
      monitor: QGeoAreaMonitorInfo,
      signal: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QGeoAreaMonitorSource::requestUpdate(const
    QGeoAreaMonitorInfo &monitor, const char *signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#requestUpdate

    Parameters
    ----------

    monitor : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QGeoAreaMonitorSource::requestUpdate(const QGeoAreaMonitorInfo
    #      &monitor, const char *signal)
    return self.uglySide.call(
        'ritual_ZN21QGeoAreaMonitorSource13requestUpdateERK19QGeoAreaMonito'
        'rInfoPKc',
        self._valueOf(monitor), self._bytesOf(signal),
    )

  @overload(QGeoAreaMonitorInfo, QGeoPositionInfo)
  def areaEntered(
      self,
      monitor: QGeoAreaMonitorInfo,
      update: QGeoPositionInfo,
  ) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorSource::areaEntered(const
    QGeoAreaMonitorInfo &monitor, const QGeoPositionInfo &update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#areaEntered

    Parameters
    ----------

    monitor : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.

    update : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  void QGeoAreaMonitorSource::areaEntered(const QGeoAreaMonitorInfo
    #      &monitor, const QGeoPositionInfo &update)
    self.uglySide.call(
        'ritual_ZN21QGeoAreaMonitorSource11areaEnteredERK19QGeoAreaMonitorI'
        'nfoRK16QGeoPositionInfo',
        self._valueOf(monitor), self._valueOf(update),
    )

  @overload(QGeoAreaMonitorInfo, QGeoPositionInfo)
  def areaExited(
      self,
      monitor: QGeoAreaMonitorInfo,
      update: QGeoPositionInfo,
  ) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorSource::areaExited(const
    QGeoAreaMonitorInfo &monitor, const QGeoPositionInfo &update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#areaExited

    Parameters
    ----------

    monitor : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.

    update : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  void QGeoAreaMonitorSource::areaExited(const QGeoAreaMonitorInfo
    #      &monitor, const QGeoPositionInfo &update)
    self.uglySide.call(
        'ritual_ZN21QGeoAreaMonitorSource10areaExitedERK19QGeoAreaMonitorIn'
        'foRK16QGeoPositionInfo',
        self._valueOf(monitor), self._valueOf(update),
    )

  @overload(QGeoAreaMonitorInfo)
  def monitorExpired(self, monitor: QGeoAreaMonitorInfo) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorSource::monitorExpired(const
    QGeoAreaMonitorInfo &monitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#monitorExpired

    Parameters
    ----------

    monitor : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.
    """
    #  void QGeoAreaMonitorSource::monitorExpired(const QGeoAreaMonitorInfo
    #      &monitor)
    self.uglySide.call(
        'ritual_ZN21QGeoAreaMonitorSource14monitorExpiredERK19QGeoAreaMonit'
        'orInfo',
        self._valueOf(monitor),
    )

  @overload(Error)
  def errorOccurred(self, error: Error) -> None:
    """
    Calls Qt's 'void
    QGeoAreaMonitorSource::errorOccurred(QGeoAreaMonitorSource::Error
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorsource.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QGeoAreaMonitorSource::errorOccurred(QGeoAreaMonitorSource::Error
    #      error)
    self.uglySide.call(
        'ritual_ZN21QGeoAreaMonitorSource13errorOccurredENS_5ErrorE',
        error.value,
    )
