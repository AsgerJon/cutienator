"""
QOpenGLTimeMonitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopengltimerquery.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLTimeMonitor(QObject):
  """
  The cute side of Qt's QOpenGLTimeMonitor: a plain Python object standing in
  front of one C++ QOpenGLTimeMonitor.

  It is built on the cute 'QObject', as Qt's QOpenGLTimeMonitor is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLTimeMonitor that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'setSampleCount',
  'sampleCount', 'create', 'destroy', 'isCreated', 'recordSample',
  'isResultAvailable', 'reset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLTimeMonitor::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QOpenGLTimeMonitor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLTimeMonitor::~QOpenGLTimeMonitor()': the destructor: Python
    never removes a C++ QOpenGLTimeMonitor.
  - Qt's 'QList<GLuint> QOpenGLTimeMonitor::objectIds() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<GLuint64> QOpenGLTimeMonitor::waitForSamples() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<GLuint64> QOpenGLTimeMonitor::waitForIntervals() const':
    gives a type Python has no way to take yet.
  - Qt's 'QOpenGLTimeMonitorPrivate *QOpenGLTimeMonitor::d_func()': gives
    'QOpenGLTimeMonitorPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLTimeMonitorPrivate *QOpenGLTimeMonitor::d_func()
    const': gives 'QOpenGLTimeMonitorPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLTimeMonitor is created at the first use, not by
    'QOpenGLTimeMonitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLTimeMonitor.
  - Qt tells when it has removed the C++ QOpenGLTimeMonitor. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpenGLTimeMonitor that has no cute function yet,
    'objectIds', 'waitForIntervals', 'waitForSamples', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QOpenGLTimeMonitor::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimemonitor.html#tr

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
    #  QString QOpenGLTimeMonitor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QOpenGLTimeMonitor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTimeMonitor'

  #  A C++ QOpenGLTimeMonitor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLTimeMonitor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLTimeMonitor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimemonitor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLTimeMonitor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QOpenGLTimeMonitor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QOpenGLTimeMonitor::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimemonitor.html#sampleCount
    """
    #  int QOpenGLTimeMonitor::sampleCount() const
    return self.uglySide.call(
        'ritual_ZNK18QOpenGLTimeMonitor11sampleCountEv',
    )

  def isCreated(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTimeMonitor::isCreated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimemonitor.html#isCreated
    """
    #  bool QOpenGLTimeMonitor::isCreated() const
    return self.uglySide.call('ritual_ZNK18QOpenGLTimeMonitor9isCreatedEv')

  def isResultAvailable(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTimeMonitor::isResultAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimemonitor.html#isResultAvailable
    """
    #  bool QOpenGLTimeMonitor::isResultAvailable() const
    return self.uglySide.call(
        'ritual_ZNK18QOpenGLTimeMonitor17isResultAvailableEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSampleCount(self, sampleCount: int) -> None:
    """
    Calls Qt's 'void QOpenGLTimeMonitor::setSampleCount(int sampleCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimemonitor.html#setSampleCount

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.
    """
    #  void QOpenGLTimeMonitor::setSampleCount(int sampleCount)
    self.uglySide.call(
        'ritual_ZN18QOpenGLTimeMonitor14setSampleCountEi', sampleCount,
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
    'QOpenGLTimeMonitor::QOpenGLTimeMonitor(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimemonitor.html#QOpenGLTimeMonitor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLTimeMonitor::QOpenGLTimeMonitor(QObject *parent)
    self._noteCreation(QOpenGLTimeMonitor, lambda: Rituals.call(
        'ritual_ZN18QOpenGLTimeMonitorC1EP7QObject',
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTimeMonitor::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimemonitor.html#create
    """
    #  bool QOpenGLTimeMonitor::create()
    return self.uglySide.call('ritual_ZN18QOpenGLTimeMonitor6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOpenGLTimeMonitor::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimemonitor.html#destroy
    """
    #  void QOpenGLTimeMonitor::destroy()
    self.uglySide.call('ritual_ZN18QOpenGLTimeMonitor7destroyEv')

  def recordSample(self) -> int:
    """
    Calls Qt's 'int QOpenGLTimeMonitor::recordSample()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimemonitor.html#recordSample
    """
    #  int QOpenGLTimeMonitor::recordSample()
    return self.uglySide.call(
        'ritual_ZN18QOpenGLTimeMonitor12recordSampleEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QOpenGLTimeMonitor::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimemonitor.html#reset
    """
    #  void QOpenGLTimeMonitor::reset()
    self.uglySide.call('ritual_ZN18QOpenGLTimeMonitor5resetEv')

  @staticmethod
  def objectIds(*__, **_) -> Never:
    """
    Qt's 'QList<GLuint> QOpenGLTimeMonitor::objectIds() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLTimeMonitor.objectIds' has no cute function yet. Qt's "
        "'QList<GLuint> QOpenGLTimeMonitor::objectIds() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def waitForIntervals(*__, **_) -> Never:
    """
    Qt's 'QList<GLuint64> QOpenGLTimeMonitor::waitForIntervals() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLTimeMonitor.waitForIntervals' has no cute function yet. "
        "Qt's 'QList<GLuint64> QOpenGLTimeMonitor::waitForIntervals() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def waitForSamples(*__, **_) -> Never:
    """
    Qt's 'QList<GLuint64> QOpenGLTimeMonitor::waitForSamples() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLTimeMonitor.waitForSamples' has no cute function yet. Qt's "
        "'QList<GLuint64> QOpenGLTimeMonitor::waitForSamples() const': "
        "gives a type Python has no way to take yet.")
