"""
QMqttTopicFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqtttopicfilter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QLatin1String
  from . import QMqttTopicName
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']
  QMqttTopicName = WAIT['QMqttTopicName']


class QMqttTopicFilter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttTopicFilter: a plain Python object standing in
  front of one C++ QMqttTopicFilter.

  C++ hands a QMqttTopicFilter around as a copy, so every C++
  QMqttTopicFilter behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttTopicFilter that has a ritual and that Python
  can call so far, 8 names in all: 'filter', 'setFilter',
  'sharedSubscriptionName', 'isValid', 'match', '__eq__', '__ne__', '__lt__'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttTopicFilter::~QMqttTopicFilter()': the destructor: Python
    removes its C++ QMqttTopicFilter by it, and has no other use for it.
  - Qt's 'QMqttTopicFilter &QMqttTopicFilter::operator=(const
    QMqttTopicFilter &filter)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QMqttTopicFilter &QMqttTopicFilter::operator=(QMqttTopicFilter
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QMqttTopicFilter::swap(QMqttTopicFilter &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QMqttTopicFilter is created at the first use, not by
    'QMqttTopicFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttTopicFilter back gives a copy the ritual made
    for Python, in a new cute QMqttTopicFilter.
  - Each name of Qt's QMqttTopicFilter that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QMqttTopicFilter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class MatchOption(CuteFlags):
    """
    The flags enum 'QMqttTopicFilter::MatchOption' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QMqttTopicFilter::MatchOptions'.
    """

    NoMatchOption = 0x0
    WildcardsDontMatchDollarTopicMatchOption = 0x1

  MatchOptions = MatchOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttTopicFilter'

  #  Qt's '~QMqttTopicFilter()'. Naming it makes this a value class: Python
  #  owns every C++ QMqttTopicFilter behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QMqttTopicFilterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def filter(self) -> str:
    """
    Calls Qt's 'QString QMqttTopicFilter::filter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicfilter.html#filter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttTopicFilter::filter() const
    return self.uglySide.call('ritual_ZNK16QMqttTopicFilter6filterEv')

  def sharedSubscriptionName(self) -> str:
    """
    Calls Qt's 'QString QMqttTopicFilter::sharedSubscriptionName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqtttopicfilter.html#sharedSubscriptionName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttTopicFilter::sharedSubscriptionName() const
    return self.uglySide.call(
        'ritual_ZNK16QMqttTopicFilter22sharedSubscriptionNameEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMqttTopicFilter::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicfilter.html#isValid
    """
    #  bool QMqttTopicFilter::isValid() const
    return self.uglySide.call('ritual_ZNK16QMqttTopicFilter7isValidEv')

  @overload(QMqttTopicName)
  @overload(QMqttTopicName, MatchOptions)
  def match(
      self,
      name: QMqttTopicName,
      matchOptions: MatchOptions = MatchOptions.NoMatchOption,
  ) -> bool:
    """
    Calls Qt's 'bool QMqttTopicFilter::match(const QMqttTopicName &name,
    MatchOptions matchOptions) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicfilter.html#match

    Parameters
    ----------

    name : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.

    matchOptions : MatchOptions
      Passed on as its number. May be left out, as in Qt: it is then
      MatchOptions.NoMatchOption.
    """
    #  bool QMqttTopicFilter::match(const QMqttTopicName &name, MatchOptions
    #      matchOptions) const
    return self.uglySide.call(
        'ritual_ZNK16QMqttTopicFilter5matchERK14QMqttTopicName6QFlagsINS_11'
        'MatchOptionEE',
        self._valueOf(name), matchOptions.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QMqttTopicFilter::setFilter(const QString &filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicfilter.html#setFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttTopicFilter::setFilter(const QString &filter)
    self.uglySide.call(
        'ritual_ZN16QMqttTopicFilter9setFilterERK7QString', filter,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QMqttTopicFilter) -> bool:
    """
    Calls Qt's 'bool operator==(const QMqttTopicFilter &lhs, const
    QMqttTopicFilter &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicfilter.html#operator==

    Parameters
    ----------

    rhs : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.
    """
    #  bool operator==(const QMqttTopicFilter &lhs, const QMqttTopicFilter
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QMqttTopicFilterS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QMqttTopicFilter) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMqttTopicFilter &lhs, const
    QMqttTopicFilter &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicfilter.html#operator!=

    Parameters
    ----------

    rhs : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.
    """
    #  bool operator!=(const QMqttTopicFilter &lhs, const QMqttTopicFilter
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QMqttTopicFilterS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: QMqttTopicFilter) -> bool:
    """
    Calls Qt's 'bool operator<(const QMqttTopicFilter &lhs, const
    QMqttTopicFilter &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicfilter.html#operator<

    Parameters
    ----------

    rhs : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.
    """
    #  bool operator<(const QMqttTopicFilter &lhs, const QMqttTopicFilter
    #      &rhs)
    return Rituals.call(
        'ritual_ZltRK16QMqttTopicFilterS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  def __init__(self, filter: str = '') -> None:
    """
    Notes what was given, for Qt's 'QMqttTopicFilter::QMqttTopicFilter(const
    QString &filter)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqtttopicfilter.html#QMqttTopicFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QMqttTopicFilter::QMqttTopicFilter(const QString &filter)
    self._noteCreation(QMqttTopicFilter, lambda: Rituals.call(
        'ritual_ZN16QMqttTopicFilterC1ERK7QString', filter,
    ))

  @overload(QLatin1String)
  def __init__(self, filter: QLatin1String) -> None:
    """
    Notes what was given, for Qt's 'QMqttTopicFilter::QMqttTopicFilter(const
    QLatin1String &filter)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqtttopicfilter.html#QMqttTopicFilter

    Parameters
    ----------

    filter : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QMqttTopicFilter::QMqttTopicFilter(const QLatin1String &filter)
    self._noteCreation(QMqttTopicFilter, lambda: Rituals.call(
        'ritual_ZN16QMqttTopicFilterC1ERK13QLatin1String',
        self._valueOf(filter),
    ))

  @overload(THIS)
  def __init__(self, filter: QMqttTopicFilter) -> None:
    """
    Notes what was given, for Qt's 'QMqttTopicFilter::QMqttTopicFilter(const
    QMqttTopicFilter &filter)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqtttopicfilter.html#QMqttTopicFilter

    Parameters
    ----------

    filter : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.
    """
    #  QMqttTopicFilter::QMqttTopicFilter(const QMqttTopicFilter &filter)
    self._noteCreation(QMqttTopicFilter, lambda: Rituals.call(
        'ritual_ZN16QMqttTopicFilterC1ERKS_', self._valueOf(filter),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMqttTopicFilter::swap(QMqttTopicFilter &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMqttTopicFilter.swap' has no cute function yet. Qt's 'void "
        "QMqttTopicFilter::swap(QMqttTopicFilter &other)': takes a type "
        "Python has no way to hand over yet.")
