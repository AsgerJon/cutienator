"""
QQmlIncubator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlincubator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QVariant
  from . import QQmlError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlIncubator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlIncubator: a plain Python object standing in
  front of one C++ QQmlIncubator.

  What exists
  -----------

  Every function of Qt's QQmlIncubator that has a ritual and that Python can
  call so far, 13 names in all: 'clear', 'forceCompletion', 'isNull',
  'isReady', 'isError', 'isLoading', 'errors', 'incubationMode', 'status',
  'object', 'setInitialProperties', 'statusChanged', 'setInitialState'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlIncubator::~QQmlIncubator()': the destructor: Python never
    removes a C++ QQmlIncubator.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlIncubator is created at the first use, not by
    'QQmlIncubator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlIncubator.
  """

  #  The enums Qt writes inside QQmlIncubator, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class IncubationMode(CuteNum):
    """
    The enum 'QQmlIncubator::IncubationMode' of Qt, with the 3 names Qt gives
    in it.
    """

    Asynchronous = Kee[int](0)
    AsynchronousIfNested = Kee[int](1)
    Synchronous = Kee[int](2)

  class Status(CuteNum):
    """
    The enum 'QQmlIncubator::Status' of Qt, with the 4 names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlIncubator'

  #  A C++ QQmlIncubator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlIncubator'

  #  The functions Qt calls itself that QQmlIncubator is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'statusChanged': (
          ('_ZN13QQmlIncubator13statusChangedENS_6StatusE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQml:QQmlIncubator.Status'),
           )),
      ),
      'setInitialState': (
          ('_ZN13QQmlIncubator15setInitialStateEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
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

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlIncubator::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#isNull
    """
    #  bool QQmlIncubator::isNull() const
    return self.uglySide.call('ritual_ZNK13QQmlIncubator6isNullEv')

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QQmlIncubator::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#isReady
    """
    #  bool QQmlIncubator::isReady() const
    return self.uglySide.call('ritual_ZNK13QQmlIncubator7isReadyEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QQmlIncubator::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#isError
    """
    #  bool QQmlIncubator::isError() const
    return self.uglySide.call('ritual_ZNK13QQmlIncubator7isErrorEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQmlIncubator::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#isLoading
    """
    #  bool QQmlIncubator::isLoading() const
    return self.uglySide.call('ritual_ZNK13QQmlIncubator9isLoadingEv')

  def errors(self) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlIncubator::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#errors

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlIncubator::errors() const
    address = self.uglySide.call('ritual_ZNK13QQmlIncubator6errorsEv')
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  def incubationMode(self) -> IncubationMode:
    """
    Calls Qt's 'IncubationMode QQmlIncubator::incubationMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#incubationMode

    Returns
    -------

    IncubationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'IncubationMode(number)'
      gives.
    """
    #  IncubationMode QQmlIncubator::incubationMode() const
    return QQmlIncubator.IncubationMode(self.uglySide.call(
        'ritual_ZNK13QQmlIncubator14incubationModeEv',
    ))

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQmlIncubator::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQmlIncubator::status() const
    return QQmlIncubator.Status(self.uglySide.call(
        'ritual_ZNK13QQmlIncubator6statusEv',
    ))

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlIncubator::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlIncubator::object() const
    address = self.uglySide.call('ritual_ZNK13QQmlIncubator6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant])
  def setInitialProperties(
      self,
      initialProperties: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QQmlIncubator::setInitialProperties(const QVariantMap
    &initialProperties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubator.html#setInitialProperties

    Parameters
    ----------

    initialProperties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlIncubator::setInitialProperties(const QVariantMap
    #      &initialProperties)
    self.uglySide.call(
        'ritual_ZN13QQmlIncubator20setInitialPropertiesERK4QMapI7QString8QV'
        'ariantE',
        self._valueOf(initialProperties),
    )

  @overload(QObject)
  @overload(NoneType)
  def setInitialState(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlIncubator::setInitialState(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#setInitialState

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlIncubator::setInitialState(QObject *a0)
    ritual = 'ritual_ZN13QQmlIncubator15setInitialStateEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlIncubator15setInitialStateEP7QObject'
    self.uglySide.call(ritual, self._addressOf(a0, 'QObject'))

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
  @overload(IncubationMode)
  def __init__(
      self,
      a0: IncubationMode = IncubationMode.Asynchronous,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlIncubator::QQmlIncubator(IncubationMode a0)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#QQmlIncubator

    Parameters
    ----------

    a0 : IncubationMode
      Passed on as its number. May be left out, as in Qt: it is then
      IncubationMode.Asynchronous.
    """
    #  QQmlIncubator::QQmlIncubator(IncubationMode a0)
    self._noteCreation(QQmlIncubator, lambda: Rituals.call(
        'ritual_ZN13QQmlIncubatorC1ENS_14IncubationModeE', a0.value,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlIncubator::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#clear
    """
    #  void QQmlIncubator::clear()
    self.uglySide.call('ritual_ZN13QQmlIncubator5clearEv')

  def forceCompletion(self) -> None:
    """
    Calls Qt's 'void QQmlIncubator::forceCompletion()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#forceCompletion
    """
    #  void QQmlIncubator::forceCompletion()
    self.uglySide.call('ritual_ZN13QQmlIncubator15forceCompletionEv')

  @overload(Status)
  def statusChanged(self, a0: Status) -> None:
    """
    Calls Qt's 'void QQmlIncubator::statusChanged(Status a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubator.html#statusChanged

    Parameters
    ----------

    a0 : Status
      Passed on as its number.
    """
    #  void QQmlIncubator::statusChanged(Status a0)
    ritual = 'ritual_ZN13QQmlIncubator13statusChangedENS_6StatusE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlIncubator13statusChangedENS_6StatusE'
    self.uglySide.call(ritual, a0.value)
