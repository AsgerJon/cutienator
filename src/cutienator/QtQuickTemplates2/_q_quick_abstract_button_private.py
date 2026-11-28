"""
QQuickAbstractButtonPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickabstractbutton_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAbstractButtonPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from ..QtQml import QQml
from . import QQuickControlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from ..QtQuick import QQuickItem
  from . import QQuickAbstractButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractButtonPrivate(QQuickControlPrivate):
  """
  The cute side of Qt's QQuickAbstractButtonPrivate: a plain Python object
  standing in front of one C++ QQuickAbstractButtonPrivate.

  It is built on the cute 'QQuickControlPrivate', as Qt's
  QQuickAbstractButtonPrivate is built on Qt's QQuickControlPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAbstractButtonPrivate that has a ritual and
  that Python can call so far, 35 names in all: 'q_func', 'get',
  'centerPressPoint', 'setPressPoint', 'setMovePoint', 'handlePress',
  'handleMove', 'handleRelease', 'handleUngrab', 'acceptKeyClick',
  'accessiblePressAction', 'accessibleToggleAction',
  'isPressAndHoldConnected', 'isDoubleClickConnected', 'startPressAndHold',
  'stopPressAndHold', 'startRepeatDelay', 'startPressRepeat',
  'stopPressRepeat', 'grabShortcut', 'ungrabShortcut', 'findCheckedButton',
  'findExclusiveButtons', 'actionTextChange', 'setText', 'init',
  'updateEffectiveIcon', 'click', 'trigger', 'toggle', 'cancelIndicator',
  'executeIndicator', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'itemDestroyed'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAbstractButton *QQuickAbstractButtonPrivate::q_func()
    const': takes in Python what 'QQuickAbstractButton
    *QQuickAbstractButtonPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickAbstractButtonPrivate is created at the first use, not by
    'QQuickAbstractButtonPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractButtonPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def get(
      button: Optional[QQuickAbstractButton],
  ) -> Optional[QQuickAbstractButtonPrivate]:
    """
    Calls Qt's 'QQuickAbstractButtonPrivate
    *QQuickAbstractButtonPrivate::get(QQuickAbstractButton *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#get

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickAbstractButtonPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButtonPrivate
    #      *QQuickAbstractButtonPrivate::get(QQuickAbstractButton *button)
    address = Rituals.call(
        'ritual_ZN27QQuickAbstractButtonPrivate3getEP20QQuickAbstractButton',
        CuteMixin._addressOf(button),
    )
    return QQuickAbstractButtonPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractButtonPrivate'

  #  A C++ QQuickAbstractButtonPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractButtonPrivate'

  #  The functions Qt calls itself that QQuickAbstractButtonPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'acceptKeyClick': (
          ('_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Key'),
           )),
      ),
      'accessiblePressAction': (
          ('_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'accessibleToggleAction': (
          ('_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def centerPressPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickAbstractButtonPrivate::centerPressPoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#centerPressPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickAbstractButtonPrivate::centerPressPoint() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickAbstractButtonPrivate16centerPressPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(Qt.Key)
  def acceptKeyClick(self, key: Qt.Key) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#acceptKeyClick

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.
    """
    #  bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key) const
    ritual = (
        'ritual_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt'
          '3KeyE')
    return self.uglySide.call(ritual, key.value)

  def findCheckedButton(self) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton
    *QQuickAbstractButtonPrivate::findCheckedButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#findCheckedButton

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton *QQuickAbstractButtonPrivate::findCheckedButton()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickAbstractButtonPrivate17findCheckedButtonEv',
    )
    from . import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def findExclusiveButtons(self) -> QList[QQuickAbstractButton]:
    """
    Calls Qt's 'QList<QQuickAbstractButton *>
    QQuickAbstractButtonPrivate::findExclusiveButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html

    Returns
    -------

    QList[QQuickAbstractButton]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickAbstractButton *>
    #      QQuickAbstractButtonPrivate::findExclusiveButtons() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickAbstractButtonPrivate20findExclusiveButtonsEv',
    )
    from . import QQuickAbstractButton
    return QList[QQuickAbstractButton]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPressPoint(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::setPressPoint(const QPointF
    &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#setPressPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickAbstractButtonPrivate::setPressPoint(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate13setPressPointERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def setMovePoint(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::setMovePoint(const QPointF
    &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#setMovePoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickAbstractButtonPrivate::setMovePoint(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate12setMovePointERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(str, QQml.PropertyUtils.State)
  def setText(
      self,
      text: str,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::setText(const QString
    &text, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickAbstractButtonPrivate::setText(const QString &text,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate7setTextERK7QStringN4QQml13P'
        'ropertyUtils5StateE',
        text, propertyState.value,
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

  def q_func(self) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton *QQuickAbstractButtonPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#q_func

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton *QQuickAbstractButtonPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate6q_funcEv',
    )
    from . import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  @overload(QPointF, int)
  def handlePress(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButtonPrivate::handlePress(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#handlePress

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickAbstractButtonPrivate::handlePress(const QPointF &point,
    #      ulong timestamp)
    ritual = (
        'ritual_ZN27QQuickAbstractButtonPrivate11handlePressERK7QPointFm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate11handlePressERK7QPoin'
          'tFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleMove(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButtonPrivate::handleMove(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#handleMove

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point,
    #      ulong timestamp)
    ritual = 'ritual_ZN27QQuickAbstractButtonPrivate10handleMoveERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate10handleMoveERK7QPoint'
          'Fm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleRelease(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButtonPrivate::handleRelease(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#handleRelease

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickAbstractButtonPrivate::handleRelease(const QPointF &point,
    #      ulong timestamp)
    ritual = (
        'ritual_ZN27QQuickAbstractButtonPrivate13handleReleaseERK7QPointFm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate13handleReleaseERK7QPo'
          'intFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  def handleUngrab(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::handleUngrab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#handleUngrab
    """
    #  void QQuickAbstractButtonPrivate::handleUngrab()
    ritual = 'ritual_ZN27QQuickAbstractButtonPrivate12handleUngrabEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickAbstractButtonPrivate12handleUngrabEv'
    self.uglySide.call(ritual)

  def accessiblePressAction(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::accessiblePressAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html
    """
    #  void QQuickAbstractButtonPrivate::accessiblePressAction()
    ritual = (
        'ritual_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate21accessiblePressActio'
          'nEv')
    self.uglySide.call(ritual)

  def accessibleToggleAction(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::accessibleToggleAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html
    """
    #  void QQuickAbstractButtonPrivate::accessibleToggleAction()
    ritual = (
        'ritual_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate22accessibleToggleActi'
          'onEv')
    self.uglySide.call(ritual)

  def isPressAndHoldConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButtonPrivate::isPressAndHoldConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html
    """
    #  bool QQuickAbstractButtonPrivate::isPressAndHoldConnected()
    return self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate23isPressAndHoldConnectedEv',
    )

  def isDoubleClickConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButtonPrivate::isDoubleClickConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html
    """
    #  bool QQuickAbstractButtonPrivate::isDoubleClickConnected()
    return self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate22isDoubleClickConnectedEv',
    )

  def startPressAndHold(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::startPressAndHold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#startPressAndHold
    """
    #  void QQuickAbstractButtonPrivate::startPressAndHold()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate17startPressAndHoldEv',
    )

  def stopPressAndHold(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::stopPressAndHold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#stopPressAndHold
    """
    #  void QQuickAbstractButtonPrivate::stopPressAndHold()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate16stopPressAndHoldEv',
    )

  def startRepeatDelay(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::startRepeatDelay()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#startRepeatDelay
    """
    #  void QQuickAbstractButtonPrivate::startRepeatDelay()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate16startRepeatDelayEv',
    )

  def startPressRepeat(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::startPressRepeat()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#startPressRepeat
    """
    #  void QQuickAbstractButtonPrivate::startPressRepeat()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate16startPressRepeatEv',
    )

  def stopPressRepeat(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::stopPressRepeat()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#stopPressRepeat
    """
    #  void QQuickAbstractButtonPrivate::stopPressRepeat()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate15stopPressRepeatEv',
    )

  def grabShortcut(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::grabShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#grabShortcut
    """
    #  void QQuickAbstractButtonPrivate::grabShortcut()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate12grabShortcutEv',
    )

  def ungrabShortcut(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::ungrabShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#ungrabShortcut
    """
    #  void QQuickAbstractButtonPrivate::ungrabShortcut()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate14ungrabShortcutEv',
    )

  def actionTextChange(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::actionTextChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#actionTextChange
    """
    #  void QQuickAbstractButtonPrivate::actionTextChange()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate16actionTextChangeEv',
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#init
    """
    #  void QQuickAbstractButtonPrivate::init()
    self.uglySide.call('ritual_ZN27QQuickAbstractButtonPrivate4initEv')

  def updateEffectiveIcon(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::updateEffectiveIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html
    """
    #  void QQuickAbstractButtonPrivate::updateEffectiveIcon()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate19updateEffectiveIconEv',
    )

  def click(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::click()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#click
    """
    #  void QQuickAbstractButtonPrivate::click()
    self.uglySide.call('ritual_ZN27QQuickAbstractButtonPrivate5clickEv')

  @overload()
  @overload(bool)
  def trigger(self, doubleClick: bool = False) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::trigger(bool doubleClick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#trigger

    Parameters
    ----------

    doubleClick : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickAbstractButtonPrivate::trigger(bool doubleClick)
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate7triggerEb', doubleClick,
    )

  @overload(bool)
  def toggle(self, value: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::toggle(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#toggle

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButtonPrivate::toggle(bool value)
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate6toggleEb', value,
    )

  def cancelIndicator(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::cancelIndicator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#cancelIndicator
    """
    #  void QQuickAbstractButtonPrivate::cancelIndicator()
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate15cancelIndicatorEv',
    )

  @overload()
  @overload(bool)
  def executeIndicator(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::executeIndicator(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#executeIndicator

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickAbstractButtonPrivate::executeIndicator(bool complete)
    self.uglySide.call(
        'ritual_ZN27QQuickAbstractButtonPrivate16executeIndicatorEb',
        complete,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN27QQuickAbstractButtonPrivate24itemImplicitWidthChangedEP'
        '10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate24itemImplicitWidthCha'
          'ngedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN27QQuickAbstractButtonPrivate25itemImplicitHeightChangedE'
        'P10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate25itemImplicitHeightCh'
          'angedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbuttonprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
    ritual = (
        'ritual_ZN27QQuickAbstractButtonPrivate13itemDestroyedEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAbstractButtonPrivate13itemDestroyedEP10QQu'
          'ickItem')
    self.uglySide.call(ritual, self._addressOf(item))
