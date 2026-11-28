"""
QQmlJS::LoggerCategory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsloggingutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJS::LoggerCategory to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA, QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class LoggerCategory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::LoggerCategory: a plain Python object
  standing in front of one C++ QQmlJS::LoggerCategory.

  C++ hands a QQmlJS::LoggerCategory around as a copy, so every C++
  QQmlJS::LoggerCategory behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::LoggerCategory that has a ritual and that
  Python can call so far, 8 names in all: 'd_func', 'name', 'settingsName',
  'description', 'severity', 'isEssential', 'id', 'setSeverity'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const LoggerCategoryPrivate *QQmlJS::LoggerCategory::d_func()
    const': takes in Python what 'LoggerCategoryPrivate
    *QQmlJS::LoggerCategory::d_func()' takes.
  - Qt's 'QQmlJS::LoggerCategory::LoggerCategory(LoggerCategory &&a0)': takes
    a type Python has no way to hand over yet.
  - Qt's 'LoggerCategory &QQmlJS::LoggerCategory::operator=(const
    LoggerCategory &a0)': assignment: Python binds a name and has no operator
    for it.
  - Qt's 'LoggerCategory &QQmlJS::LoggerCategory::operator=(LoggerCategory
    &&a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlJS::LoggerCategory::~LoggerCategory()': the destructor: Python
    removes its C++ QQmlJS::LoggerCategory by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QQmlJS::LoggerCategory is created at the first use, not by
    'QQmlJS::LoggerCategory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::LoggerCategory back gives a copy the ritual
    made for Python, in a new cute QQmlJS::LoggerCategory.
  """

  #  The enums Qt writes inside QQmlJS::LoggerCategory, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Essentiality(CuteNum):
    """
    The enum 'QQmlJS::LoggerCategory::Essentiality' of Qt, with the 2 names
    Qt gives in it.
    """

    Essential = Kee[int](0)
    NonEssential = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::LoggerCategory'

  #  Qt's '~QQmlJS::LoggerCategory()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJS::LoggerCategory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS14LoggerCategoryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::LoggerCategory::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-loggercategory.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::LoggerCategory::name() const
    return self.uglySide.call('ritual_ZNK6QQmlJS14LoggerCategory4nameEv')

  def settingsName(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::LoggerCategory::settingsName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#settingsName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::LoggerCategory::settingsName() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS14LoggerCategory12settingsNameEv',
    )

  def description(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::LoggerCategory::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::LoggerCategory::description() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS14LoggerCategory11descriptionEv',
    )

  def severity(self) -> QQmlSA.WarningSeverity:
    """
    Calls Qt's 'WarningSeverity QQmlJS::LoggerCategory::severity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#severity

    Returns
    -------

    QQmlSA.WarningSeverity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.WarningSeverity(number)' gives.
    """
    #  WarningSeverity QQmlJS::LoggerCategory::severity() const
    return QQmlSA.WarningSeverity(self.uglySide.call(
        'ritual_ZNK6QQmlJS14LoggerCategory8severityEv',
    ))

  def isEssential(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::LoggerCategory::isEssential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#isEssential
    """
    #  bool QQmlJS::LoggerCategory::isEssential() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS14LoggerCategory11isEssentialEv',
    )

  def id(self) -> QQmlSA.LoggerWarningId:
    """
    Calls Qt's 'LoggerWarningId QQmlJS::LoggerCategory::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-loggercategory.html#id

    Returns
    -------

    QQmlSA.LoggerWarningId
      A new cute QQmlSA::LoggerWarningId around the copy Qt gave back. Python
      owns it.
    """
    #  LoggerWarningId QQmlJS::LoggerCategory::id() const
    address = self.uglySide.call('ritual_ZNK6QQmlJS14LoggerCategory2idEv')
    return QQmlSA.LoggerWarningId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlSA.WarningSeverity)
  def setSeverity(self, a0: QQmlSA.WarningSeverity) -> None:
    """
    Calls Qt's 'void QQmlJS::LoggerCategory::setSeverity(WarningSeverity
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#setSeverity

    Parameters
    ----------

    a0 : QQmlSA.WarningSeverity
      Passed on as its number.
    """
    #  void QQmlJS::LoggerCategory::setSeverity(WarningSeverity a0)
    self.uglySide.call(
        'ritual_ZN6QQmlJS14LoggerCategory11setSeverityEN6QQmlSA15WarningSev'
        'erityE',
        a0.value,
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
    'QQmlJS::LoggerCategory::LoggerCategory()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#LoggerCategory
    """
    #  QQmlJS::LoggerCategory::LoggerCategory()
    self._noteCreation(LoggerCategory, lambda: Rituals.call(
        'ritual_ZN6QQmlJS14LoggerCategoryC1Ev',
    ))

  @overload(str, str, str, QQmlSA.WarningSeverity)
  @overload(str, str, str, QQmlSA.WarningSeverity, Essentiality)
  def __init__(
      self,
      name: str,
      settingsName: str,
      description: str,
      severity: QQmlSA.WarningSeverity,
      essentiality: Essentiality = Essentiality.NonEssential,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::LoggerCategory::LoggerCategory(const QString &name, const
    QString &settingsName, const QString &description, WarningSeverity
    severity, Essentiality essentiality)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#LoggerCategory

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    settingsName : str
      Passed on as it is: a QString is made of it for the call.

    description : str
      Passed on as it is: a QString is made of it for the call.

    severity : QQmlSA.WarningSeverity
      Passed on as its number.

    essentiality : Essentiality
      Passed on as its number. May be left out, as in Qt: it is then
      Essentiality.NonEssential.
    """
    #  QQmlJS::LoggerCategory::LoggerCategory(const QString &name, const
    #      QString &settingsName, const QString &description, WarningSeverity
    #      severity, Essentiality essentiality)
    self._noteCreation(LoggerCategory, lambda: Rituals.call(
        'ritual_ZN6QQmlJS14LoggerCategoryC1ERK7QStringS3_S3_N6QQmlSA15Warni'
        'ngSeverityENS0_12EssentialityE',
        name, settingsName, description, severity.value, essentiality.value,
    ))

  @overload(THIS)
  def __init__(self, a0: LoggerCategory) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::LoggerCategory::LoggerCategory(const LoggerCategory &a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategory.html#LoggerCategory

    Parameters
    ----------

    a0 : LoggerCategory
      Passed on as a value: Qt reads the C++ QQmlJS::LoggerCategory, which
      stays Python's own.
    """
    #  QQmlJS::LoggerCategory::LoggerCategory(const LoggerCategory &a0)
    self._noteCreation(LoggerCategory, lambda: Rituals.call(
        'ritual_ZN6QQmlJS14LoggerCategoryC1ERKS0_', self._valueOf(a0),
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

  def d_func(self) -> Optional[QQmlJS.LoggerCategoryPrivate]:
    """
    Calls Qt's 'LoggerCategoryPrivate *QQmlJS::LoggerCategory::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-loggercategory.html#d_func

    Returns
    -------

    Optional[QQmlJS.LoggerCategoryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LoggerCategoryPrivate *QQmlJS::LoggerCategory::d_func()
    address = self.uglySide.call('ritual_ZN6QQmlJS14LoggerCategory6d_funcEv')
    return QQmlJS.LoggerCategoryPrivate._cuteAt(address)
