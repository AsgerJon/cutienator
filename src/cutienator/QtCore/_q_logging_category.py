"""
QLoggingCategory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qloggingcategory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QLoggingCategory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLoggingCategory: a plain Python object standing in
  front of one C++ QLoggingCategory.

  What exists
  -----------

  Every function of Qt's QLoggingCategory that has a ritual and that Python
  can call so far, 7 names in all: 'isDebugEnabled', 'isInfoEnabled',
  'isWarningEnabled', 'isCriticalEnabled', 'categoryName', 'defaultCategory',
  'setFilterRules'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLoggingCategory::QLoggingCategory(const char *category, QtMsgType
    severityLevel)': names the enum 'QtMsgType', whose class cannot be named
    here.
  - Qt's 'QLoggingCategory::~QLoggingCategory()': the destructor: Python
    never removes a C++ QLoggingCategory.
  - Qt's 'bool QLoggingCategory::isEnabled(QtMsgType type) const': names the
    enum 'QtMsgType', whose class cannot be named here.
  - Qt's 'void QLoggingCategory::setEnabled(QtMsgType type, bool enable)':
    names the enum 'QtMsgType', whose class cannot be named here.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QLoggingCategory is created at the first use, not by
    'QLoggingCategory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLoggingCategory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultCategory() -> Optional[QLoggingCategory]:
    """
    Calls Qt's 'QLoggingCategory *QLoggingCategory::defaultCategory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategory.html#defaultCategory

    Returns
    -------

    Optional[QLoggingCategory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLoggingCategory *QLoggingCategory::defaultCategory()
    address = Rituals.call('ritual_ZN16QLoggingCategory15defaultCategoryEv')
    return QLoggingCategory._cuteAt(address)

  @staticmethod
  @overload(str)
  def setFilterRules(rules: str) -> None:
    """
    Calls Qt's 'void QLoggingCategory::setFilterRules(const QString &rules)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategory.html#setFilterRules

    Parameters
    ----------

    rules : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLoggingCategory::setFilterRules(const QString &rules)
    Rituals.call(
        'ritual_ZN16QLoggingCategory14setFilterRulesERK7QString', rules,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLoggingCategory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isDebugEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLoggingCategory::isDebugEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategory.html#isDebugEnabled
    """
    #  bool QLoggingCategory::isDebugEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QLoggingCategory14isDebugEnabledEv',
    )

  def isInfoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLoggingCategory::isInfoEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategory.html#isInfoEnabled
    """
    #  bool QLoggingCategory::isInfoEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QLoggingCategory13isInfoEnabledEv',
    )

  def isWarningEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLoggingCategory::isWarningEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategory.html#isWarningEnabled
    """
    #  bool QLoggingCategory::isWarningEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QLoggingCategory16isWarningEnabledEv',
    )

  def isCriticalEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLoggingCategory::isCriticalEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingcategory.html#isCriticalEnabled
    """
    #  bool QLoggingCategory::isCriticalEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QLoggingCategory17isCriticalEnabledEv',
    )

  def categoryName(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QLoggingCategory::categoryName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qloggingcategory.html#categoryName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QLoggingCategory::categoryName() const
    chars = self.uglySide.call(
        'ritual_ZNK16QLoggingCategory12categoryNameEv',
    )
    return None if chars is None else chars.decode()

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
