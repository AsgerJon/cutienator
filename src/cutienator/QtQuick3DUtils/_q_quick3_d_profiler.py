"""
QQuick3DProfiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qquick3dprofiler_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DProfiler to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QElapsedTimer, QMetaObject
  from . import QQuick3DProfilerData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QElapsedTimer = WAIT['QElapsedTimer']
  QQuick3DProfilerData = WAIT['QQuick3DProfilerData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DProfiler(QObject):
  """
  The cute side of Qt's QQuick3DProfiler: a plain Python object standing in
  front of one C++ QQuick3DProfiler.

  It is built on the cute 'QObject', as Qt's QQuick3DProfiler is built on
  Qt's QObject, and has everything that class has. Qt's QQuick3DProfiler is
  built on Qt's QQmlProfilerDefinitions as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuick3DProfiler that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'timestamp',
  'initialize', 'registerObject', 'registerString', 'processMessage',
  'startProfilingImpl', 'stopProfilingImpl', 'reportDataImpl', 'setTimer'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DProfiler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DProfiler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DProfiler::~QQuick3DProfiler()': the destructor: Python
    never removes a C++ QQuick3DProfiler.
  - Qt's 'void QQuick3DProfiler::dataReady(const
    QVector<QQuick3DProfilerData> &data, const QHash<int, QByteArray>
    &eventData)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 24 functions Qt declares: 6 a template; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DProfiler is created at the first use, not by
    'QQuick3DProfiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DProfiler.
  - Qt tells when it has removed the C++ QQuick3DProfiler. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DProfiler that has no cute function yet,
    'dataReady', 'recordSceneGraphTimestamp', 'reportQuick3DFrame', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DProfiler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Quick3DStage(CuteNum):
    """
    The enum 'QQuick3DProfiler::Quick3DStage' of Qt, with the 2 names Qt
    gives in it.
    """

    Quick3DStageBegin = Kee[int](0)
    Quick3DStageEnd = Kee[int](1)

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
    Calls Qt's 'QString QQuick3DProfiler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dprofiler.html#tr

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
    #  QString QQuick3DProfiler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuick3DProfiler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def initialize(parent: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DProfiler::initialize(QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dprofiler.html#initialize

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DProfiler::initialize(QObject *parent)
    Rituals.call(
        'ritual_ZN16QQuick3DProfiler10initializeEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def registerObject(object: Optional[QObject]) -> int:
    """
    Calls Qt's 'int QQuick3DProfiler::registerObject(const QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofiler.html#registerObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuick3DProfiler::registerObject(const QObject *object)
    return Rituals.call(
        'ritual_ZN16QQuick3DProfiler14registerObjectEPK7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QByteArray)
  def registerString(string: QByteArray) -> int:
    """
    Calls Qt's 'int QQuick3DProfiler::registerString(const QByteArray
    &string)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofiler.html#registerString

    Parameters
    ----------

    string : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QQuick3DProfiler::registerString(const QByteArray &string)
    return Rituals.call(
        'ritual_ZN16QQuick3DProfiler14registerStringERK10QByteArray',
        CuteMixin._valueOf(string),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DProfiler'

  #  A C++ QQuick3DProfiler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DProfiler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DProfiler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dprofiler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DProfiler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DProfiler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QElapsedTimer)
  def setTimer(self, t: QElapsedTimer) -> None:
    """
    Calls Qt's 'void QQuick3DProfiler::setTimer(const QElapsedTimer &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dprofiler.html#setTimer

    Parameters
    ----------

    t : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  void QQuick3DProfiler::setTimer(const QElapsedTimer &t)
    self.uglySide.call(
        'ritual_ZN16QQuick3DProfiler8setTimerERK13QElapsedTimer',
        self._valueOf(t),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DProfiler::QQuick3DProfiler(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofiler.html#QQuick3DProfiler

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuick3DProfiler::QQuick3DProfiler(QObject *parent)
    self._noteCreation(QQuick3DProfiler, lambda: Rituals.call(
        'ritual_ZN16QQuick3DProfilerC1EP7QObject',
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

  def timestamp(self) -> int:
    """
    Calls Qt's 'qint64 QQuick3DProfiler::timestamp()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dprofiler.html#timestamp
    """
    #  qint64 QQuick3DProfiler::timestamp()
    return self.uglySide.call('ritual_ZN16QQuick3DProfiler9timestampEv')

  @overload(QQuick3DProfilerData)
  def processMessage(self, message: QQuick3DProfilerData) -> None:
    """
    Calls Qt's 'void QQuick3DProfiler::processMessage(const
    QQuick3DProfilerData &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofiler.html#processMessage

    Parameters
    ----------

    message : QQuick3DProfilerData
      Passed on as a value: Qt reads the C++ QQuick3DProfilerData, which
      stays Python's own.
    """
    #  void QQuick3DProfiler::processMessage(const QQuick3DProfilerData
    #      &message)
    self.uglySide.call(
        'ritual_ZN16QQuick3DProfiler14processMessageERK20QQuick3DProfilerDa'
        'ta',
        self._valueOf(message),
    )

  @overload(int)
  def startProfilingImpl(self, features: int) -> None:
    """
    Calls Qt's 'void QQuick3DProfiler::startProfilingImpl(quint64 features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofiler.html#startProfilingImpl

    Parameters
    ----------

    features : int
      Passed on as it is.
    """
    #  void QQuick3DProfiler::startProfilingImpl(quint64 features)
    self.uglySide.call(
        'ritual_ZN16QQuick3DProfiler18startProfilingImplEy', features,
    )

  def stopProfilingImpl(self) -> None:
    """
    Calls Qt's 'void QQuick3DProfiler::stopProfilingImpl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofiler.html#stopProfilingImpl
    """
    #  void QQuick3DProfiler::stopProfilingImpl()
    self.uglySide.call('ritual_ZN16QQuick3DProfiler17stopProfilingImplEv')

  def reportDataImpl(self) -> None:
    """
    Calls Qt's 'void QQuick3DProfiler::reportDataImpl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofiler.html#reportDataImpl
    """
    #  void QQuick3DProfiler::reportDataImpl()
    self.uglySide.call('ritual_ZN16QQuick3DProfiler14reportDataImplEv')

  @staticmethod
  def dataReady(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DProfiler::dataReady(const
    QVector<QQuick3DProfilerData> &data, const QHash<int, QByteArray>
    &eventData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DProfiler.dataReady' has no cute function yet. Qt's 'void "
        "QQuick3DProfiler::dataReady(const QVector<QQuick3DProfilerData> "
        "&data, const QHash<int, QByteArray> &eventData)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def recordSceneGraphTimestamp(*__, **_) -> Never:
    """
    Qt's 'QQuick3DProfiler::recordSceneGraphTimestamp': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQuick3DProfiler.recordSceneGraphTimestamp' has no cute function "
        "yet. Qt's 'QQuick3DProfiler::recordSceneGraphTimestamp': a "
        "template: a pattern and no single function.")

  @staticmethod
  def reportQuick3DFrame(*__, **_) -> Never:
    """
    Qt's 'QQuick3DProfiler::reportQuick3DFrame': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuick3DProfiler.reportQuick3DFrame' has no cute function yet. "
        "Qt's 'QQuick3DProfiler::reportQuick3DFrame': a template: a pattern "
        "and no single function.")
