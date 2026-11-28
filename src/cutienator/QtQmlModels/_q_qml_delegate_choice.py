"""
QQmlDelegateChoice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatecomponent_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlDelegateChoice to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlComponent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateChoice(QObject):
  """
  The cute side of Qt's QQmlDelegateChoice: a plain Python object standing in
  front of one C++ QQmlDelegateChoice.

  It is built on the cute 'QObject', as Qt's QQmlDelegateChoice is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateChoice that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'roleValue',
  'setRoleValue', 'row', 'setRow', 'column', 'setColumn', 'delegate',
  'setDelegate', 'match', 'roleValueChanged', 'rowChanged', 'indexChanged',
  'columnChanged', 'delegateChanged', 'changed'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDelegateChoice::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlDelegateChoice::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlDelegateChoice is created at the first use, not by
    'QQmlDelegateChoice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateChoice.
  - Qt tells when it has removed the C++ QQmlDelegateChoice. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlDelegateChoice::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#tr

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
    #  QString QQmlDelegateChoice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQmlDelegateChoice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateChoice'

  #  The functions Qt calls itself that QQmlDelegateChoice is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'match': (
          ('_ZNK18QQmlDelegateChoice5matchEiiRK8QVariant',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
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
    Calls Qt's 'const QMetaObject *QQmlDelegateChoice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDelegateChoice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlDelegateChoice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def roleValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDelegateChoice::roleValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#roleValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDelegateChoice::roleValue() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlDelegateChoice9roleValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def row(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateChoice::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#row
    """
    #  int QQmlDelegateChoice::row() const
    return self.uglySide.call('ritual_ZNK18QQmlDelegateChoice3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateChoice::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#column
    """
    #  int QQmlDelegateChoice::column() const
    return self.uglySide.call('ritual_ZNK18QQmlDelegateChoice6columnEv')

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlDelegateChoice::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlDelegateChoice::delegate() const
    address = self.uglySide.call('ritual_ZNK18QQmlDelegateChoice8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  @overload(int, int, QVariant)
  def match(self, row: int, column: int, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateChoice::match(int row, int column, const
    QVariant &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#match

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQmlDelegateChoice::match(int row, int column, const QVariant
    #      &value) const
    ritual = 'ritual_ZNK18QQmlDelegateChoice5matchEiiRK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQmlDelegateChoice5matchEiiRK8QVariant'
    return self.uglySide.call(ritual, row, column, self._valueOf(value))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setRoleValue(self, roleValue: QVariant) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::setRoleValue(const QVariant
    &roleValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechoice.html#setRoleValue

    Parameters
    ----------

    roleValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlDelegateChoice::setRoleValue(const QVariant &roleValue)
    self.uglySide.call(
        'ritual_ZN18QQmlDelegateChoice12setRoleValueERK8QVariant',
        self._valueOf(roleValue),
    )

  @overload(int)
  def setRow(self, r: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::setRow(int r)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#setRow

    Parameters
    ----------

    r : int
      Passed on as it is.
    """
    #  void QQmlDelegateChoice::setRow(int r)
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice6setRowEi', r)

  @overload(int)
  def setColumn(self, c: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::setColumn(int c)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#setColumn

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QQmlDelegateChoice::setColumn(int c)
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice9setColumnEi', c)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechoice.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateChoice::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN18QQmlDelegateChoice11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
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

  def roleValueChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::roleValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechoice.html#roleValueChanged
    """
    #  void QQmlDelegateChoice::roleValueChanged()
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice16roleValueChangedEv')

  def rowChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::rowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#rowChanged
    """
    #  void QQmlDelegateChoice::rowChanged()
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice10rowChangedEv')

  def indexChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechoice.html#indexChanged
    """
    #  void QQmlDelegateChoice::indexChanged()
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice12indexChangedEv')

  def columnChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::columnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechoice.html#columnChanged
    """
    #  void QQmlDelegateChoice::columnChanged()
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice13columnChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechoice.html#delegateChanged
    """
    #  void QQmlDelegateChoice::delegateChanged()
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice15delegateChangedEv')

  def changed(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateChoice::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechoice.html#changed
    """
    #  void QQmlDelegateChoice::changed()
    self.uglySide.call('ritual_ZN18QQmlDelegateChoice7changedEv')
