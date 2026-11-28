"""
QCheckBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcheckbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractButton, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QSize
  from ..QtGui import QMouseEvent, QPaintEvent
  from . import QStyleOptionButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QStyleOptionButton = WAIT['QStyleOptionButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCheckBox(QAbstractButton):
  """
  The cute side of Qt's QCheckBox: a plain Python object standing in front of
  one C++ QCheckBox.

  It is built on the cute 'QAbstractButton', as Qt's QCheckBox is built on
  Qt's QAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCheckBox that has a ritual and that Python can call
  so far, 17 names in all: 'metaObject', 'tr', 'sizeHint', 'minimumSizeHint',
  'setTristate', 'isTristate', 'checkState', 'setCheckState', 'stateChanged',
  'checkStateChanged', 'event', 'hitButton', 'checkStateSet',
  'nextCheckState', 'paintEvent', 'mouseMoveEvent', 'initStyleOption'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCheckBox::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCheckBox::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCheckBox::~QCheckBox()': the destructor: Python never removes a
    C++ QCheckBox.
  - Qt's 'QCheckBoxPrivate *QCheckBox::d_func()': gives 'QCheckBoxPrivate',
    which has no cute class yet.
  - Qt's 'const QCheckBoxPrivate *QCheckBox::d_func() const': gives
    'QCheckBoxPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCheckBox is created at the first use, not by 'QCheckBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCheckBox.
  - Qt tells when it has removed the C++ QCheckBox. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QCheckBox::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#tr

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
    #  QString QCheckBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QCheckBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCheckBox'

  #  A C++ QCheckBox Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCheckBox'

  #  The functions Qt calls itself that QCheckBox is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK9QCheckBox15initStyleOptionEP18QStyleOptionButton',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionButton'),
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
    Calls Qt's 'const QMetaObject *QCheckBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCheckBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QCheckBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QCheckBox::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCheckBox::sizeHint() const
    ritual = 'ritual_ZNK9QCheckBox8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QCheckBox8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QCheckBox::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCheckBox::minimumSizeHint() const
    ritual = 'ritual_ZNK9QCheckBox15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QCheckBox15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isTristate(self) -> bool:
    """
    Calls Qt's 'bool QCheckBox::isTristate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#isTristate
    """
    #  bool QCheckBox::isTristate() const
    return self.uglySide.call('ritual_ZNK9QCheckBox10isTristateEv')

  def checkState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QCheckBox::checkState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#checkState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QCheckBox::checkState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK9QCheckBox10checkStateEv',
    ))

  @overload(QPoint)
  def hitButton(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QCheckBox::hitButton(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#hitButton

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QCheckBox::hitButton(const QPoint &pos) const
    ritual = 'ritual_ZNK9QCheckBox9hitButtonERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QCheckBox9hitButtonERK6QPoint'
    return self.uglySide.call(ritual, self._valueOf(pos))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  def setTristate(self, y: bool = True) -> None:
    """
    Calls Qt's 'void QCheckBox::setTristate(bool y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#setTristate

    Parameters
    ----------

    y : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QCheckBox::setTristate(bool y)
    self.uglySide.call('ritual_ZN9QCheckBox11setTristateEb', y)

  @overload(Qt.CheckState)
  def setCheckState(self, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QCheckBox::setCheckState(Qt::CheckState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#setCheckState

    Parameters
    ----------

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QCheckBox::setCheckState(Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN9QCheckBox13setCheckStateEN2Qt10CheckStateE', state.value,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QCheckBox::QCheckBox(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#QCheckBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCheckBox::QCheckBox(QWidget *parent)
    self._noteCreation(QCheckBox, lambda: Rituals.call(
        'ritual_ZN9QCheckBoxC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QCheckBox::QCheckBox(const QString &text,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#QCheckBox

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCheckBox::QCheckBox(const QString &text, QWidget *parent)
    self._noteCreation(QCheckBox, lambda: Rituals.call(
        'ritual_ZN9QCheckBoxC1ERK7QStringP7QWidget',
        text, self._addressOf(parent),
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

  @overload(int)
  def stateChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QCheckBox::stateChanged(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#stateChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QCheckBox::stateChanged(int a0)
    self.uglySide.call('ritual_ZN9QCheckBox12stateChangedEi', a0)

  @overload(Qt.CheckState)
  def checkStateChanged(self, a0: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QCheckBox::checkStateChanged(Qt::CheckState a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#checkStateChanged

    Parameters
    ----------

    a0 : Qt.CheckState
      Passed on as its number.
    """
    #  void QCheckBox::checkStateChanged(Qt::CheckState a0)
    self.uglySide.call(
        'ritual_ZN9QCheckBox17checkStateChangedEN2Qt10CheckStateE', a0.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCheckBox::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCheckBox::event(QEvent *e)
    ritual = 'ritual_ZN9QCheckBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QCheckBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def checkStateSet(self) -> None:
    """
    Calls Qt's 'void QCheckBox::checkStateSet()'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#checkStateSet
    """
    #  void QCheckBox::checkStateSet()
    ritual = 'ritual_ZN9QCheckBox13checkStateSetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QCheckBox13checkStateSetEv'
    self.uglySide.call(ritual)

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QCheckBox::nextCheckState()'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#nextCheckState
    """
    #  void QCheckBox::nextCheckState()
    ritual = 'ritual_ZN9QCheckBox14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QCheckBox14nextCheckStateEv'
    self.uglySide.call(ritual)

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QCheckBox::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCheckBox::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN9QCheckBox10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QCheckBox10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QCheckBox::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCheckBox::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN9QCheckBox14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QCheckBox14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QStyleOptionButton)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionButton]) -> None:
    """
    Calls Qt's 'void QCheckBox::initStyleOption(QStyleOptionButton *option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcheckbox.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCheckBox::initStyleOption(QStyleOptionButton *option) const
    ritual = 'ritual_ZNK9QCheckBox15initStyleOptionEP18QStyleOptionButton'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9QCheckBox15initStyleOptionEP18QStyleOptionButton')
    self.uglySide.call(ritual, self._addressOf(option))
