"""
QMimeMagicRuleMatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimemagicrulematcher_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMimeMagicRuleMatcher to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArray, QMimeMagicRule
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMimeMagicRule = WAIT['QMimeMagicRule']


class QMimeMagicRuleMatcher(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeMagicRuleMatcher: a plain Python object standing
  in front of one C++ QMimeMagicRuleMatcher.

  C++ hands a QMimeMagicRuleMatcher around as a copy, so every C++
  QMimeMagicRuleMatcher behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMimeMagicRuleMatcher that has a ritual and that
  Python can call so far, 7 names in all: '__eq__', 'addRule', 'addRules',
  'magicRules', 'matches', 'priority', 'mimetype'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMimeMagicRuleMatcher::swap(QMimeMagicRuleMatcher &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMimeMagicRuleMatcher::~QMimeMagicRuleMatcher()': the destructor:
    Python removes its C++ QMimeMagicRuleMatcher by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QMimeMagicRuleMatcher is created at the first use, not by
    'QMimeMagicRuleMatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMimeMagicRuleMatcher back gives a copy the ritual
    made for Python, in a new cute QMimeMagicRuleMatcher.
  - Each name of Qt's QMimeMagicRuleMatcher that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeMagicRuleMatcher'

  #  Qt's '~QMimeMagicRuleMatcher()'. Naming it makes this a value class:
  #  Python owns every C++ QMimeMagicRuleMatcher behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QMimeMagicRuleMatcherD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def magicRules(self) -> QList[QMimeMagicRule]:
    """
    Calls Qt's 'QList<QMimeMagicRule> QMimeMagicRuleMatcher::magicRules()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimemagicrulematcher.html#magicRules

    Returns
    -------

    QList[QMimeMagicRule]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMimeMagicRule> QMimeMagicRuleMatcher::magicRules() const
    address = self.uglySide.call(
        'ritual_ZNK21QMimeMagicRuleMatcher10magicRulesEv',
    )
    from . import QMimeMagicRule
    return QList[QMimeMagicRule]._cuteOwning(address)

  @overload(QByteArray)
  def matches(self, data: QByteArray) -> bool:
    """
    Calls Qt's 'bool QMimeMagicRuleMatcher::matches(const QByteArray &data)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrulematcher.html#matches

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QMimeMagicRuleMatcher::matches(const QByteArray &data) const
    return self.uglySide.call(
        'ritual_ZNK21QMimeMagicRuleMatcher7matchesERK10QByteArray',
        self._valueOf(data),
    )

  def priority(self) -> int:
    """
    Calls Qt's 'unsigned int QMimeMagicRuleMatcher::priority() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimemagicrulematcher.html#priority
    """
    #  unsigned int QMimeMagicRuleMatcher::priority() const
    return self.uglySide.call('ritual_ZNK21QMimeMagicRuleMatcher8priorityEv')

  def mimetype(self) -> str:
    """
    Calls Qt's 'QString QMimeMagicRuleMatcher::mimetype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimemagicrulematcher.html#mimetype

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeMagicRuleMatcher::mimetype() const
    return self.uglySide.call('ritual_ZNK21QMimeMagicRuleMatcher8mimetypeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QMimeMagicRuleMatcher) -> bool:
    """
    Calls Qt's 'bool QMimeMagicRuleMatcher::operator==(const
    QMimeMagicRuleMatcher &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimemagicrulematcher.html#operator==

    Parameters
    ----------

    other : QMimeMagicRuleMatcher
      Passed on as a value: Qt reads the C++ QMimeMagicRuleMatcher, which
      stays Python's own.
    """
    #  bool QMimeMagicRuleMatcher::operator==(const QMimeMagicRuleMatcher
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK21QMimeMagicRuleMatchereqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, int)
  def __init__(self, mime: str, priority: int = 65535) -> None:
    """
    Notes what was given, for Qt's
    'QMimeMagicRuleMatcher::QMimeMagicRuleMatcher(const QString &mime,
    unsigned int priority)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimemagicrulematcher.html#QMimeMagicRuleMatcher

    Parameters
    ----------

    mime : str
      Passed on as it is: a QString is made of it for the call.

    priority : int
      Passed on as it is. May be left out, as in Qt: it is then 65535.
    """
    #  QMimeMagicRuleMatcher::QMimeMagicRuleMatcher(const QString &mime,
    #      unsigned int priority)
    self._noteCreation(QMimeMagicRuleMatcher, lambda: Rituals.call(
        'ritual_ZN21QMimeMagicRuleMatcherC1ERK7QStringj', mime, priority,
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

  @overload(QMimeMagicRule)
  def addRule(self, rule: QMimeMagicRule) -> None:
    """
    Calls Qt's 'void QMimeMagicRuleMatcher::addRule(const QMimeMagicRule
    &rule)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrulematcher.html#addRule

    Parameters
    ----------

    rule : QMimeMagicRule
      Passed on as a value: Qt reads the C++ QMimeMagicRule, which stays
      Python's own.
    """
    #  void QMimeMagicRuleMatcher::addRule(const QMimeMagicRule &rule)
    self.uglySide.call(
        'ritual_ZN21QMimeMagicRuleMatcher7addRuleERK14QMimeMagicRule',
        self._valueOf(rule),
    )

  @overload(QList[QMimeMagicRule])
  def addRules(self, rules: QList[QMimeMagicRule]) -> None:
    """
    Calls Qt's 'void QMimeMagicRuleMatcher::addRules(const
    QList<QMimeMagicRule> &rules)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimemagicrulematcher.html#addRules

    Parameters
    ----------

    rules : QList[QMimeMagicRule]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QMimeMagicRuleMatcher::addRules(const QList<QMimeMagicRule>
    #      &rules)
    self.uglySide.call(
        'ritual_ZN21QMimeMagicRuleMatcher8addRulesERK5QListI14QMimeMagicRul'
        'eE',
        self._valueOf(rules),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMimeMagicRuleMatcher::swap(QMimeMagicRuleMatcher &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeMagicRuleMatcher.swap' has no cute function yet. Qt's 'void "
        "QMimeMagicRuleMatcher::swap(QMimeMagicRuleMatcher &other)': takes "
        "a type Python has no way to hand over yet.")
