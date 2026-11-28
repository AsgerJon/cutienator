"""
QQuickCheckBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcheckbox_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickCheckBox to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickItem
from . import QQuickAbstractButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickCheckBox(QQuickAbstractButton):
  """
  The cute side of Qt's QQuickCheckBox: a plain Python object standing in
  front of one C++ QQuickCheckBox.

  It is built on the cute 'QQuickAbstractButton', as Qt's QQuickCheckBox is
  built on Qt's QQuickAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickCheckBox that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'isTristate',
  'setTristate', 'checkState', 'setCheckState', 'getNextCheckState',
  'setNextCheckState', 'tristateChanged', 'checkStateChanged',
  'nextCheckStateChanged', 'defaultFont', 'nextCheckState'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickCheckBox::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickCheckBox::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickCheckBox::buttonChange(ButtonChange change)': names the
    enum 'QQuickAbstractButton::ButtonChange', whose class cannot be named
    here.
  - Qt's 'QQuickCheckBoxPrivate *QQuickCheckBox::d_func()': gives
    'QQuickCheckBoxPrivate', which has no cute class yet.
  - Qt's 'const QQuickCheckBoxPrivate *QQuickCheckBox::d_func() const': gives
    'QQuickCheckBoxPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickCheckBox is created at the first use, not by
    'QQuickCheckBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCheckBox.
  - Qt tells when it has removed the C++ QQuickCheckBox. Every call on the
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
    Calls Qt's 'QString QQuickCheckBox::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#tr

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
    #  QString QQuickCheckBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickCheckBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCheckBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickCheckBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickCheckBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickCheckBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isTristate(self) -> bool:
    """
    Calls Qt's 'bool QQuickCheckBox::isTristate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#isTristate
    """
    #  bool QQuickCheckBox::isTristate() const
    return self.uglySide.call('ritual_ZNK14QQuickCheckBox10isTristateEv')

  def checkState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QQuickCheckBox::checkState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#checkState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QQuickCheckBox::checkState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK14QQuickCheckBox10checkStateEv',
    ))

  def getNextCheckState(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickCheckBox::getNextCheckState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckbox.html#getNextCheckState

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickCheckBox::getNextCheckState() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickCheckBox17getNextCheckStateEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickCheckBox::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickCheckBox::defaultFont() const
    ritual = 'ritual_ZNK14QQuickCheckBox11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickCheckBox11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTristate(self, tristate: bool) -> None:
    """
    Calls Qt's 'void QQuickCheckBox::setTristate(bool tristate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#setTristate

    Parameters
    ----------

    tristate : bool
      Passed on as it is.
    """
    #  void QQuickCheckBox::setTristate(bool tristate)
    self.uglySide.call('ritual_ZN14QQuickCheckBox11setTristateEb', tristate)

  @overload(Qt.CheckState)
  def setCheckState(self, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QQuickCheckBox::setCheckState(Qt::CheckState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#setCheckState

    Parameters
    ----------

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QQuickCheckBox::setCheckState(Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN14QQuickCheckBox13setCheckStateEN2Qt10CheckStateE',
        state.value,
    )

  @overload(QJSValue)
  def setNextCheckState(self, callback: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickCheckBox::setNextCheckState(const QJSValue
    &callback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckbox.html#setNextCheckState

    Parameters
    ----------

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickCheckBox::setNextCheckState(const QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN14QQuickCheckBox17setNextCheckStateERK8QJSValue',
        self._valueOf(callback),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickCheckBox::QQuickCheckBox(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#QQuickCheckBox

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickCheckBox::QQuickCheckBox(QQuickItem *parent)
    self._noteCreation(QQuickCheckBox, lambda: Rituals.call(
        'ritual_ZN14QQuickCheckBoxC1EP10QQuickItem', self._addressOf(parent),
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

  def tristateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCheckBox::tristateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckbox.html#tristateChanged
    """
    #  void QQuickCheckBox::tristateChanged()
    self.uglySide.call('ritual_ZN14QQuickCheckBox15tristateChangedEv')

  def checkStateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCheckBox::checkStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckbox.html#checkStateChanged
    """
    #  void QQuickCheckBox::checkStateChanged()
    self.uglySide.call('ritual_ZN14QQuickCheckBox17checkStateChangedEv')

  def nextCheckStateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCheckBox::nextCheckStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckbox.html#nextCheckStateChanged
    """
    #  void QQuickCheckBox::nextCheckStateChanged()
    self.uglySide.call('ritual_ZN14QQuickCheckBox21nextCheckStateChangedEv')

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QQuickCheckBox::nextCheckState()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckbox.html#nextCheckState
    """
    #  void QQuickCheckBox::nextCheckState()
    ritual = 'ritual_ZN14QQuickCheckBox14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickCheckBox14nextCheckStateEv'
    self.uglySide.call(ritual)
