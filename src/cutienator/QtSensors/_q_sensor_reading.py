"""
QSensorReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qsensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QSensorReadingPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSensorReadingPrivate = WAIT['QSensorReadingPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSensorReading(QObject):
  """
  The cute side of Qt's QSensorReading: a plain Python object standing in
  front of one C++ QSensorReading.

  It is built on the cute 'QObject', as Qt's QSensorReading is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSensorReading that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'timestamp',
  'setTimestamp', 'valueCount', 'value', 'copyValuesFrom'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSensorReading::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSensorReading::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSensorReading::~QSensorReading()': the destructor: Python never
    removes a C++ QSensorReading.
  - Qt's 'QScopedPointer<QSensorReadingPrivate> *QSensorReading::d_ptr()':
    gives 'QScopedPointer<QSensorReadingPrivate>', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSensorReading is created at the first use, not by
    'QSensorReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSensorReading.
  - Qt tells when it has removed the C++ QSensorReading. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QSensorReading::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#tr

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
    #  QString QSensorReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QSensorReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSensorReading'

  #  A C++ QSensorReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSensorReading'

  #  The functions Qt calls itself that QSensorReading is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'copyValuesFrom': (
          ('_ZN14QSensorReading14copyValuesFromEPS_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSensors:QSensorReading'),
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
    Calls Qt's 'const QMetaObject *QSensorReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSensorReading::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QSensorReading10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def timestamp(self) -> int:
    """
    Calls Qt's 'quint64 QSensorReading::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#timestamp
    """
    #  quint64 QSensorReading::timestamp() const
    return self.uglySide.call('ritual_ZNK14QSensorReading9timestampEv')

  def valueCount(self) -> int:
    """
    Calls Qt's 'int QSensorReading::valueCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#valueCount
    """
    #  int QSensorReading::valueCount() const
    return self.uglySide.call('ritual_ZNK14QSensorReading10valueCountEv')

  @overload(int)
  def value(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSensorReading::value(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSensorReading::value(int index) const
    address = self.uglySide.call('ritual_ZNK14QSensorReading5valueEi', index)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimestamp(self, timestamp: int) -> None:
    """
    Calls Qt's 'void QSensorReading::setTimestamp(quint64 timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#setTimestamp

    Parameters
    ----------

    timestamp : int
      Passed on as it is.
    """
    #  void QSensorReading::setTimestamp(quint64 timestamp)
    self.uglySide.call(
        'ritual_ZN14QSensorReading12setTimestampEy', timestamp,
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

  @overload(QObject, QSensorReadingPrivate)
  @overload(QObject, NoneType)
  @overload(NoneType, QSensorReadingPrivate)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      parent: Optional[QObject],
      d: Optional[QSensorReadingPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's 'QSensorReading::QSensorReading(QObject
    *parent, QSensorReadingPrivate *d)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#QSensorReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : Optional[QSensorReadingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSensorReading::QSensorReading(QObject *parent, QSensorReadingPrivate
    #      *d)
    self._noteCreation(QSensorReading, lambda: Rituals.call(
        'ritual_ZN14QSensorReadingC1EP7QObjectP21QSensorReadingPrivate',
        self._addressOf(parent, 'QObject'), self._addressOf(d),
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

  @overload(THIS)
  @overload(NoneType)
  def copyValuesFrom(self, other: Optional[QSensorReading]) -> None:
    """
    Calls Qt's 'void QSensorReading::copyValuesFrom(QSensorReading *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorreading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSensorReading::copyValuesFrom(QSensorReading *other)
    ritual = 'ritual_ZN14QSensorReading14copyValuesFromEPS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSensorReading14copyValuesFromEPS_'
    self.uglySide.call(ritual, self._addressOf(other))
