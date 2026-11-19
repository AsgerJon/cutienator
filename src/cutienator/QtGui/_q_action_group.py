"""
QActionGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qactiongroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ._q_action import QAction
from ._q_icon import QIcon
from ..QtCore import QMetaObject
from ..QtCore import QObject
from ._q_action_group_exclusion_policy import ExclusionPolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QActionGroup(QObject):
  """
  The cute side of Qt's QActionGroup: a plain Python object standing in front
  of one C++ QActionGroup.

  It is built on the cute 'QObject', as Qt's QActionGroup is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QActionGroup that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'addAction',
  'removeAction', 'checkedAction', 'isExclusive', 'isEnabled', 'isVisible',
  'exclusionPolicy', 'setEnabled', 'setDisabled', 'setVisible',
  'setExclusive', 'setExclusionPolicy'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QActionGroup::~QActionGroup()': the destructor: Python never
    removes a C++ QActionGroup.

  What has no ritual
  ------------------

  15 of the 33 functions Qt declares: 6 private; 3 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QActionGroup is created at the first use, not by
    'QActionGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QActionGroup.
  - Qt tells when it has removed the C++ QActionGroup. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QActionGroup, and the names Qt has for the
  #  combinations of its flags enums.
  ExclusionPolicy = ExclusionPolicy

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
    Calls Qt's 'QString QActionGroup::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#tr

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
    #  QString QActionGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QActionGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QActionGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QActionGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QActionGroup::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QActionGroup10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def checkedAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QActionGroup::checkedAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#checkedAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QActionGroup::checkedAction() const
    address = self.uglySide.call('ritual_ZNK12QActionGroup13checkedActionEv')
    return QAction._cuteAt(address)

  def isExclusive(self) -> bool:
    """
    Calls Qt's 'bool QActionGroup::isExclusive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#isExclusive
    """
    #  bool QActionGroup::isExclusive() const
    return self.uglySide.call('ritual_ZNK12QActionGroup11isExclusiveEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QActionGroup::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#isEnabled
    """
    #  bool QActionGroup::isEnabled() const
    return self.uglySide.call('ritual_ZNK12QActionGroup9isEnabledEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QActionGroup::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#isVisible
    """
    #  bool QActionGroup::isVisible() const
    return self.uglySide.call('ritual_ZNK12QActionGroup9isVisibleEv')

  def exclusionPolicy(self) -> ExclusionPolicy:
    """
    Calls Qt's 'ExclusionPolicy QActionGroup::exclusionPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#exclusionPolicy

    Returns
    -------

    ExclusionPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ExclusionPolicy(number)'
      gives.
    """
    #  ExclusionPolicy QActionGroup::exclusionPolicy() const
    return ExclusionPolicy(self.uglySide.call(
        'ritual_ZNK12QActionGroup15exclusionPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QActionGroup::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QActionGroup::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN12QActionGroup10setEnabledEb', a0)

  @overload(bool)
  def setDisabled(self, b: bool) -> None:
    """
    Calls Qt's 'void QActionGroup::setDisabled(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#setDisabled

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QActionGroup::setDisabled(bool b)
    self.uglySide.call('ritual_ZN12QActionGroup11setDisabledEb', b)

  @overload(bool)
  def setVisible(self, a0: bool) -> None:
    """
    Calls Qt's 'void QActionGroup::setVisible(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#setVisible

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QActionGroup::setVisible(bool a0)
    self.uglySide.call('ritual_ZN12QActionGroup10setVisibleEb', a0)

  @overload(bool)
  def setExclusive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QActionGroup::setExclusive(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#setExclusive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QActionGroup::setExclusive(bool a0)
    self.uglySide.call('ritual_ZN12QActionGroup12setExclusiveEb', a0)

  @overload(ExclusionPolicy)
  def setExclusionPolicy(self, policy: ExclusionPolicy) -> None:
    """
    Calls Qt's 'void QActionGroup::setExclusionPolicy(ExclusionPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qactiongroup.html#setExclusionPolicy

    Parameters
    ----------

    policy : ExclusionPolicy
      Passed on as its number.
    """
    #  void QActionGroup::setExclusionPolicy(ExclusionPolicy policy)
    self.uglySide.call(
        'ritual_ZN12QActionGroup18setExclusionPolicyENS_15ExclusionPolicyE',
        policy.value,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QActionGroup::QActionGroup(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#QActionGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QActionGroup::QActionGroup(QObject *parent)
    self._noteCreation(QActionGroup, lambda: Rituals.call(
        'ritual_ZN12QActionGroupC1EP7QObject', self._addressOf(parent),
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

  @overload(QAction)
  @overload(NoneType)
  def addAction(self, a: Optional[QAction]) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QActionGroup::addAction(QAction *a)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#addAction

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QActionGroup::addAction(QAction *a)
    address = self.uglySide.call(
        'ritual_ZN12QActionGroup9addActionEP7QAction', self._addressOf(a),
    )
    return QAction._cuteAt(address)

  @overload(str)
  def addAction(self, text: str) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QActionGroup::addAction(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#addAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QActionGroup::addAction(const QString &text)
    address = self.uglySide.call(
        'ritual_ZN12QActionGroup9addActionERK7QString', text,
    )
    return QAction._cuteAt(address)

  @overload(QIcon, str)
  def addAction(self, icon: QIcon, text: str) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QActionGroup::addAction(const QIcon &icon, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#addAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QActionGroup::addAction(const QIcon &icon, const QString
    #      &text)
    address = self.uglySide.call(
        'ritual_ZN12QActionGroup9addActionERK5QIconRK7QString',
        self._valueOf(icon), text,
    )
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def removeAction(self, a: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QActionGroup::removeAction(QAction *a)'.

    Qt's own words: https://doc.qt.io/qt-6/qactiongroup.html#removeAction

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QActionGroup::removeAction(QAction *a)
    self.uglySide.call(
        'ritual_ZN12QActionGroup12removeActionEP7QAction',
        self._addressOf(a),
    )
