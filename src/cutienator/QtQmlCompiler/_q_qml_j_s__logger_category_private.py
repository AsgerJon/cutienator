"""
QQmlJS::LoggerCategoryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsloggingutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJS::LoggerCategoryPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA, QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LoggerCategoryPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::LoggerCategoryPrivate: a plain Python object
  standing in front of one C++ QQmlJS::LoggerCategoryPrivate.

  C++ hands a QQmlJS::LoggerCategoryPrivate around as a copy, so every C++
  QQmlJS::LoggerCategoryPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::LoggerCategoryPrivate that has a ritual and
  that Python can call so far, 11 names in all: 'id', 'name', 'settingsName',
  'description', 'isEssential', 'severity', 'setSeverity', 'hasChanged',
  'get', '__eq__', '__ne__'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::LoggerCategoryPrivate::~LoggerCategoryPrivate()': the
    destructor: Python removes its C++ QQmlJS::LoggerCategoryPrivate by it,
    and has no other use for it.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QQmlJS::LoggerCategoryPrivate is created at the first use, not by
    'QQmlJS::LoggerCategoryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::LoggerCategoryPrivate back gives a copy the
    ritual made for Python, in a new cute QQmlJS::LoggerCategoryPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QQmlJS.LoggerCategory'])
  @overload(NoneType)
  def get(
      a0: Optional[QQmlJS.LoggerCategory],
  ) -> Optional[LoggerCategoryPrivate]:
    """
    Calls Qt's 'LoggerCategoryPrivate
    *QQmlJS::LoggerCategoryPrivate::get(LoggerCategory *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#get

    Parameters
    ----------

    a0 : Optional[QQmlJS.LoggerCategory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[LoggerCategoryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LoggerCategoryPrivate
    #      *QQmlJS::LoggerCategoryPrivate::get(LoggerCategory *a0)
    address = Rituals.call(
        'ritual_ZN6QQmlJS21LoggerCategoryPrivate3getEPNS_14LoggerCategoryE',
        CuteMixin._addressOf(a0),
    )
    return LoggerCategoryPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::LoggerCategoryPrivate'

  #  Qt's '~QQmlJS::LoggerCategoryPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlJS::LoggerCategoryPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS21LoggerCategoryPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> QQmlSA.LoggerWarningId:
    """
    Calls Qt's 'LoggerWarningId QQmlJS::LoggerCategoryPrivate::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#id

    Returns
    -------

    QQmlSA.LoggerWarningId
      A new cute QQmlSA::LoggerWarningId around the copy Qt gave back. Python
      owns it.
    """
    #  LoggerWarningId QQmlJS::LoggerCategoryPrivate::id() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivate2idEv',
    )
    return QQmlSA.LoggerWarningId._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::LoggerCategoryPrivate::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::LoggerCategoryPrivate::name() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivate4nameEv',
    )

  def settingsName(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::LoggerCategoryPrivate::settingsName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#settingsName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::LoggerCategoryPrivate::settingsName() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivate12settingsNameEv',
    )

  def description(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::LoggerCategoryPrivate::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::LoggerCategoryPrivate::description() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivate11descriptionEv',
    )

  def isEssential(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::LoggerCategoryPrivate::isEssential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#isEssential
    """
    #  bool QQmlJS::LoggerCategoryPrivate::isEssential() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivate11isEssentialEv',
    )

  def severity(self) -> QQmlSA.WarningSeverity:
    """
    Calls Qt's 'WarningSeverity QQmlJS::LoggerCategoryPrivate::severity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#severity

    Returns
    -------

    QQmlSA.WarningSeverity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.WarningSeverity(number)' gives.
    """
    #  WarningSeverity QQmlJS::LoggerCategoryPrivate::severity() const
    return QQmlSA.WarningSeverity(self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivate8severityEv',
    ))

  def hasChanged(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::LoggerCategoryPrivate::hasChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#hasChanged
    """
    #  bool QQmlJS::LoggerCategoryPrivate::hasChanged() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivate10hasChangedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlSA.WarningSeverity)
  def setSeverity(self, a0: QQmlSA.WarningSeverity) -> None:
    """
    Calls Qt's 'void
    QQmlJS::LoggerCategoryPrivate::setSeverity(WarningSeverity a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#setSeverity

    Parameters
    ----------

    a0 : QQmlSA.WarningSeverity
      Passed on as its number.
    """
    #  void QQmlJS::LoggerCategoryPrivate::setSeverity(WarningSeverity a0)
    self.uglySide.call(
        'ritual_ZN6QQmlJS21LoggerCategoryPrivate11setSeverityEN6QQmlSA15War'
        'ningSeverityE',
        a0.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: LoggerCategoryPrivate) -> bool:
    """
    Calls Qt's 'bool operator==(const LoggerCategoryPrivate &lhs, const
    LoggerCategoryPrivate &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#operator==

    Parameters
    ----------

    rhs : LoggerCategoryPrivate
      Passed on as a value: Qt reads the C++ QQmlJS::LoggerCategoryPrivate,
      which stays Python's own.
    """
    #  bool operator==(const LoggerCategoryPrivate &lhs, const
    #      LoggerCategoryPrivate &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlJSeqERKNS_21LoggerCategoryPrivateES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(WAIT['QQmlSA.LoggerWarningId'])
  def __eq__(self, warningId: QQmlSA.LoggerWarningId) -> bool:
    """
    Calls Qt's 'bool QQmlJS::LoggerCategoryPrivate::operator==(const
    LoggerWarningId warningId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#operator==

    Parameters
    ----------

    warningId : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.
    """
    #  bool QQmlJS::LoggerCategoryPrivate::operator==(const LoggerWarningId
    #      warningId) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS21LoggerCategoryPrivateeqEN6QQmlSA15LoggerWarning'
        'IdE',
        self._valueOf(warningId),
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
  def __ne__(self, rhs: LoggerCategoryPrivate) -> bool:
    """
    Calls Qt's 'bool operator!=(const LoggerCategoryPrivate &lhs, const
    LoggerCategoryPrivate &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html#operator!=

    Parameters
    ----------

    rhs : LoggerCategoryPrivate
      Passed on as a value: Qt reads the C++ QQmlJS::LoggerCategoryPrivate,
      which stays Python's own.
    """
    #  bool operator!=(const LoggerCategoryPrivate &lhs, const
    #      LoggerCategoryPrivate &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlJSneERKNS_21LoggerCategoryPrivateES2_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::LoggerCategoryPrivate::LoggerCategoryPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html
    """
    #  QQmlJS::LoggerCategoryPrivate::LoggerCategoryPrivate()
    self._noteCreation(LoggerCategoryPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlJS21LoggerCategoryPrivateC1Ev',
    ))

  @overload(
      str, str, str, QQmlSA.WarningSeverity,
      QQmlJS.LoggerCategory.Essentiality,
  )
  def __init__(
      self,
      name: str,
      settingsName: str,
      description: str,
      severity: QQmlSA.WarningSeverity,
      essentiality: QQmlJS.LoggerCategory.Essentiality,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::LoggerCategoryPrivate::LoggerCategoryPrivate(const QString
    &name, const QString &settingsName, const QString &description,
    WarningSeverity severity, LoggerCategory::Essentiality essentiality)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-loggercategoryprivate.html

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

    essentiality : QQmlJS.LoggerCategory.Essentiality
      Passed on as its number.
    """
    #  QQmlJS::LoggerCategoryPrivate::LoggerCategoryPrivate(const QString
    #      &name, const QString &settingsName, const QString &description,
    #      WarningSeverity severity, LoggerCategory::Essentiality
    #      essentiality)
    self._noteCreation(LoggerCategoryPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlJS21LoggerCategoryPrivateC1ERK7QStringS3_S3_N6QQmlSA'
        '15WarningSeverityENS_14LoggerCategory12EssentialityE',
        name, settingsName, description, severity.value, essentiality.value,
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
