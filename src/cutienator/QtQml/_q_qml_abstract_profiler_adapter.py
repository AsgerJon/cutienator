"""
QQmlAbstractProfilerAdapter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlabstractprofileradapter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlAbstractProfilerAdapter to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlProfilerDefinitions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QElapsedTimer, QMetaObject
  from . import QQmlProfilerService
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QElapsedTimer = WAIT['QElapsedTimer']
  QQmlProfilerService = WAIT['QQmlProfilerService']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAbstractProfilerAdapter(QObject, QQmlProfilerDefinitions):
  """
  The cute side of Qt's QQmlAbstractProfilerAdapter: a plain Python object
  standing in front of one C++ QQmlAbstractProfilerAdapter.

  It is built on the cute 'QObject', as Qt's QQmlAbstractProfilerAdapter is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlProfilerDefinitions' as well, as Qt's
  QQmlAbstractProfilerAdapter is built on Qt's QQmlProfilerDefinitions too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlAbstractProfilerAdapter that has a ritual and
  that Python can call so far, 17 names in all: 'metaObject', 'tr',
  'setService', 'startProfiling', 'stopProfiling', 'reportData',
  'stopWaiting', 'startWaiting', 'isRunning', 'features', 'synchronize',
  'profilingEnabled', 'profilingEnabledWhileWaiting', 'profilingDisabled',
  'profilingDisabledWhileWaiting', 'dataRequested', 'referenceTimeKnown'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlAbstractProfilerAdapter::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQmlAbstractProfilerAdapter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlAbstractProfilerAdapter::~QQmlAbstractProfilerAdapter()': the
    destructor: Python never removes a C++ QQmlAbstractProfilerAdapter.
  - Qt's 'qint64 QQmlAbstractProfilerAdapter::sendMessages(qint64 until,
    QList<QByteArray> &messages)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  3 of the 24 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QQmlAbstractProfilerAdapter is created at the first use, not by
    'QQmlAbstractProfilerAdapter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAbstractProfilerAdapter.
  - Qt tells when it has removed the C++ QQmlAbstractProfilerAdapter. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlAbstractProfilerAdapter that has no cute function
    yet, '__init__', 'sendMessages', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlAbstractProfilerAdapter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#tr

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
    #  QString QQmlAbstractProfilerAdapter::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAbstractProfilerAdapter'

  #  Qt's QQmlAbstractProfilerAdapter is built on more than one class. The
  #  part of a C++ QQmlAbstractProfilerAdapter that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlProfilerDefinitions':
          'ritual_cast_QQmlAbstractProfilerAdapter_QQmlProfilerDefinitions',
  }

  #  A C++ QQmlAbstractProfilerAdapter Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlAbstractProfilerAdapter'

  #  The functions Qt calls itself that QQmlAbstractProfilerAdapter is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'sendMessages': (
          'qint64 QQmlAbstractProfilerAdapter::sendMessages(qint64, '
          'QList<QByteArray> &)',
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
    Calls Qt's 'const QMetaObject *QQmlAbstractProfilerAdapter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlAbstractProfilerAdapter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQmlAbstractProfilerAdapter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractProfilerAdapter::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#isRunning
    """
    #  bool QQmlAbstractProfilerAdapter::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlAbstractProfilerAdapter9isRunningEv',
    )

  def features(self) -> int:
    """
    Calls Qt's 'quint64 QQmlAbstractProfilerAdapter::features() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#features
    """
    #  quint64 QQmlAbstractProfilerAdapter::features() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlAbstractProfilerAdapter8featuresEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlProfilerService)
  @overload(NoneType)
  def setService(self, new_service: Optional[QQmlProfilerService]) -> None:
    """
    Calls Qt's 'void
    QQmlAbstractProfilerAdapter::setService(QQmlProfilerService
    *new_service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#setService

    Parameters
    ----------

    new_service : Optional[QQmlProfilerService]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlAbstractProfilerAdapter::setService(QQmlProfilerService
    #      *new_service)
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter10setServiceEP19QQmlProfiler'
        'Service',
        self._addressOf(new_service),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlAbstractProfilerAdapter::QQmlAbstractProfilerAdapter(QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlAbstractProfilerAdapter.__init__' has no cute function yet. "
        "Qt's "
        "'QQmlAbstractProfilerAdapter::QQmlAbstractProfilerAdapter(QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  @overload(int)
  def startProfiling(self, features: int) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::startProfiling(quint64
    features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#startProfiling

    Parameters
    ----------

    features : int
      Passed on as it is.
    """
    #  void QQmlAbstractProfilerAdapter::startProfiling(quint64 features)
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter14startProfilingEy', features,
    )

  def stopProfiling(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::stopProfiling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#stopProfiling
    """
    #  void QQmlAbstractProfilerAdapter::stopProfiling()
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter13stopProfilingEv',
    )

  def reportData(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::reportData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#reportData
    """
    #  void QQmlAbstractProfilerAdapter::reportData()
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter10reportDataEv',
    )

  def stopWaiting(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::stopWaiting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#stopWaiting
    """
    #  void QQmlAbstractProfilerAdapter::stopWaiting()
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter11stopWaitingEv',
    )

  def startWaiting(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::startWaiting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#startWaiting
    """
    #  void QQmlAbstractProfilerAdapter::startWaiting()
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter12startWaitingEv',
    )

  @overload(QElapsedTimer)
  def synchronize(self, t: QElapsedTimer) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::synchronize(const
    QElapsedTimer &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#synchronize

    Parameters
    ----------

    t : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  void QQmlAbstractProfilerAdapter::synchronize(const QElapsedTimer &t)
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter11synchronizeERK13QElapsedTi'
        'mer',
        self._valueOf(t),
    )

  @overload(int)
  def profilingEnabled(self, features: int) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::profilingEnabled(quint64
    features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#profilingEnabled

    Parameters
    ----------

    features : int
      Passed on as it is.
    """
    #  void QQmlAbstractProfilerAdapter::profilingEnabled(quint64 features)
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter16profilingEnabledEy',
        features,
    )

  @overload(int)
  def profilingEnabledWhileWaiting(self, features: int) -> None:
    """
    Calls Qt's 'void
    QQmlAbstractProfilerAdapter::profilingEnabledWhileWaiting(quint64
    features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html

    Parameters
    ----------

    features : int
      Passed on as it is.
    """
    #  void QQmlAbstractProfilerAdapter::profilingEnabledWhileWaiting(quint64
    #      features)
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter28profilingEnabledWhileWaiti'
        'ngEy',
        features,
    )

  def profilingDisabled(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::profilingDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#profilingDisabled
    """
    #  void QQmlAbstractProfilerAdapter::profilingDisabled()
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter17profilingDisabledEv',
    )

  def profilingDisabledWhileWaiting(self) -> None:
    """
    Calls Qt's 'void
    QQmlAbstractProfilerAdapter::profilingDisabledWhileWaiting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html
    """
    #  void QQmlAbstractProfilerAdapter::profilingDisabledWhileWaiting()
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter29profilingDisabledWhileWait'
        'ingEv',
    )

  def dataRequested(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::dataRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html#dataRequested
    """
    #  void QQmlAbstractProfilerAdapter::dataRequested()
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter13dataRequestedEv',
    )

  @overload(QElapsedTimer)
  def referenceTimeKnown(self, timer: QElapsedTimer) -> None:
    """
    Calls Qt's 'void QQmlAbstractProfilerAdapter::referenceTimeKnown(const
    QElapsedTimer &timer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractprofileradapter.html

    Parameters
    ----------

    timer : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  void QQmlAbstractProfilerAdapter::referenceTimeKnown(const
    #      QElapsedTimer &timer)
    self.uglySide.call(
        'ritual_ZN27QQmlAbstractProfilerAdapter18referenceTimeKnownERK13QEl'
        'apsedTimer',
        self._valueOf(timer),
    )

  @staticmethod
  def sendMessages(*__, **_) -> Never:
    """
    Qt's 'qint64 QQmlAbstractProfilerAdapter::sendMessages(qint64 until,
    QList<QByteArray> &messages)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractProfilerAdapter.sendMessages' has no cute function "
        "yet. Qt's 'qint64 QQmlAbstractProfilerAdapter::sendMessages(qint64 "
        "until, QList<QByteArray> &messages)': takes a type Python has no "
        "way to hand over yet.")
