"""
QmlSensorReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QmlSensorReading to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QSensorReading

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlSensorReading(QObject):
  """
  The cute side of Qt's QmlSensorReading: a plain Python object standing in
  front of one C++ QmlSensorReading.

  It is built on the cute 'QObject', as Qt's QmlSensorReading is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlSensorReading that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'timestamp', 'update',
  'timestampChanged', 'reading', 'readingUpdate',
  '_qt_property_m_timestamp_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlSensorReading::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QmlSensorReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlSensorReading::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QmlSensorReading::~QmlSensorReading()': the destructor: Python
    never removes a C++ QmlSensorReading.
  - Qt's 'QBindable<quint64> QmlSensorReading::bindableTimestamp() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlSensorReading is created at the first use, not by
    'QmlSensorReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlSensorReading.
  - Qt tells when it has removed the C++ QmlSensorReading. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlSensorReading that has no cute function yet,
    'bindableTimestamp', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QmlSensorReading::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorreading.html#tr

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
    #  QString QmlSensorReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QmlSensorReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_timestamp_offset() -> int:
    """
    Calls Qt's 'size_t QmlSensorReading::_qt_property_m_timestamp_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensorreading.html
    """
    #  size_t QmlSensorReading::_qt_property_m_timestamp_offset()
    return Rituals.call(
        'ritual_ZN16QmlSensorReading31_qt_property_m_timestamp_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlSensorReading'

  #  A C++ QmlSensorReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlSensorReading'

  #  The functions Qt calls itself that QmlSensorReading is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'reading': (
          ('_ZNK16QmlSensorReading7readingEv',
           ('address', 'address', 'QtSensors:QSensorReading'),
           ()),
      ),
      'readingUpdate': (
          ('_ZN16QmlSensorReading13readingUpdateEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *QmlSensorReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlSensorReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QmlSensorReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def timestamp(self) -> int:
    """
    Calls Qt's 'quint64 QmlSensorReading::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorreading.html#timestamp
    """
    #  quint64 QmlSensorReading::timestamp() const
    return self.uglySide.call('ritual_ZNK16QmlSensorReading9timestampEv')

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlSensorReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlSensorReading::reading() const
    address = self.uglySide.call('ritual_ZNK16QmlSensorReading7readingEv')
    from ..QtSensors import QSensorReading
    return QSensorReading._cuteAt(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QmlSensorReading::QmlSensorReading()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensorreading.html#QmlSensorReading
    """
    #  QmlSensorReading::QmlSensorReading()
    self._noteCreation(QmlSensorReading, lambda: Rituals.call(
        'ritual_ZN16QmlSensorReadingC1Ev',
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

  def update(self) -> None:
    """
    Calls Qt's 'void QmlSensorReading::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorreading.html#update
    """
    #  void QmlSensorReading::update()
    self.uglySide.call('ritual_ZN16QmlSensorReading6updateEv')

  def timestampChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensorReading::timestampChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensorreading.html#timestampChanged
    """
    #  void QmlSensorReading::timestampChanged()
    self.uglySide.call('ritual_ZN16QmlSensorReading16timestampChangedEv')

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlSensorReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensorreading.html#readingUpdate
    """
    #  void QmlSensorReading::readingUpdate()
    self.uglySide.call('ritual_ZN16QmlSensorReading13readingUpdateEv')

  @staticmethod
  def bindableTimestamp(*__, **_) -> Never:
    """
    Qt's 'QBindable<quint64> QmlSensorReading::bindableTimestamp() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlSensorReading.bindableTimestamp' has no cute function yet. "
        "Qt's 'QBindable<quint64> QmlSensorReading::bindableTimestamp() "
        "const': gives a type Python has no way to take yet.")
