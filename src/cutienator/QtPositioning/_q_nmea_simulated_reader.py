"""
QNmeaSimulatedReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QNmeaSimulatedReader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QNmeaReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNmeaSimulatedReader(QObject, QNmeaReader):
  """
  The cute side of Qt's QNmeaSimulatedReader: a plain Python object standing
  in front of one C++ QNmeaSimulatedReader.

  It is built on the cute 'QObject', as Qt's QNmeaSimulatedReader is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QNmeaReader' as well, as Qt's QNmeaSimulatedReader is built on Qt's
  QNmeaReader too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNmeaSimulatedReader that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'readAvailableData',
  'timerEvent', 'simulatePendingUpdate'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNmeaSimulatedReader::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNmeaSimulatedReader::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QNmeaSimulatedReader::~QNmeaSimulatedReader()': the destructor:
    Python never removes a C++ QNmeaSimulatedReader.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QNmeaSimulatedReader.

  What to expect
  --------------

  - The C++ QNmeaSimulatedReader is created at the first use, not by
    'QNmeaSimulatedReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNmeaSimulatedReader.
  - Qt tells when it has removed the C++ QNmeaSimulatedReader. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNmeaSimulatedReader that has no cute function yet,
    '__init__', 'processNextSentence', 'setFirstDateTime', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaSimulatedReader'

  #  Qt's QNmeaSimulatedReader is built on more than one class. The part of a
  #  C++ QNmeaSimulatedReader that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QNmeaReader': 'ritual_cast_QNmeaSimulatedReader_QNmeaReader',
  }

  #  A C++ QNmeaSimulatedReader Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNmeaSimulatedReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNmeaSimulatedReader::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasimulatedreader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNmeaSimulatedReader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QNmeaSimulatedReader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNmeaSimulatedReader::QNmeaSimulatedReader(
    QNmeaPositionInfoSourcePrivate *sourcePrivate)': leans on
    'QNmeaSimulatedReader::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaSimulatedReader.__init__' has no cute function yet. Qt's "
        "'QNmeaSimulatedReader::QNmeaSimulatedReader(QNmeaPositionInfoSource"
        "Private *sourcePrivate)': leans on "
        "'QNmeaSimulatedReader::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def readAvailableData(self) -> None:
    """
    Calls Qt's 'void QNmeaSimulatedReader::readAvailableData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasimulatedreader.html#readAvailableData
    """
    #  void QNmeaSimulatedReader::readAvailableData()
    self.uglySide.call(
        'ritual_ZN20QNmeaSimulatedReader17readAvailableDataEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QNmeaSimulatedReader::timerEvent(QTimerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasimulatedreader.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNmeaSimulatedReader::timerEvent(QTimerEvent *event)
    self.uglySide.call(
        'ritual_ZN20QNmeaSimulatedReader10timerEventEP11QTimerEvent',
        self._addressOf(event),
    )

  def simulatePendingUpdate(self) -> None:
    """
    Calls Qt's 'void QNmeaSimulatedReader::simulatePendingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasimulatedreader.html#simulatePendingUpdate
    """
    #  void QNmeaSimulatedReader::simulatePendingUpdate()
    self.uglySide.call(
        'ritual_ZN20QNmeaSimulatedReader21simulatePendingUpdateEv',
    )

  @staticmethod
  def processNextSentence(*__, **_) -> Never:
    """
    Qt's 'void QNmeaSimulatedReader::processNextSentence()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'QGeoPositionInfoPrivateNmea'; did you mean
    'QGeoPositionInfoPrivate'?.
    """
    raise NotImplementedError(
        "'QNmeaSimulatedReader.processNextSentence' has no cute function "
        "yet. Qt's 'void QNmeaSimulatedReader::processNextSentence()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name "
        "'QGeoPositionInfoPrivateNmea'; did you mean "
        "'QGeoPositionInfoPrivate'?.")

  @staticmethod
  def setFirstDateTime(*__, **_) -> Never:
    """
    Qt's 'bool QNmeaSimulatedReader::setFirstDateTime()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'QGeoPositionInfoPrivateNmea'; did you mean
    'QGeoPositionInfoPrivate'?.
    """
    raise NotImplementedError(
        "'QNmeaSimulatedReader.setFirstDateTime' has no cute function yet. "
        "Qt's 'bool QNmeaSimulatedReader::setFirstDateTime()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name "
        "'QGeoPositionInfoPrivateNmea'; did you mean "
        "'QGeoPositionInfoPrivate'?.")
