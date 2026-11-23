"""
QPropertyAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpropertyanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractAnimation, QObject, QVariantAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QEvent, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyAnimation(QVariantAnimation):
  """
  The cute side of Qt's QPropertyAnimation: a plain Python object standing in
  front of one C++ QPropertyAnimation.

  It is built on the cute 'QVariantAnimation', as Qt's QPropertyAnimation is
  built on Qt's QVariantAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPropertyAnimation that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'targetObject',
  'setTargetObject', 'propertyName', 'setPropertyName', 'event',
  'updateCurrentValue', 'updateState'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPropertyAnimation::~QPropertyAnimation()': the destructor: Python
    never removes a C++ QPropertyAnimation.

  What has no ritual
  ------------------

  10 of the 22 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QPropertyAnimation is created at the first use, not by
    'QPropertyAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPropertyAnimation.
  - Qt tells when it has removed the C++ QPropertyAnimation. Every call on
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
    Calls Qt's 'QString QPropertyAnimation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpropertyanimation.html#tr

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
    #  QString QPropertyAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QPropertyAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyAnimation'

  #  A C++ QPropertyAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPropertyAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPropertyAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpropertyanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPropertyAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QPropertyAnimation10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def targetObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QPropertyAnimation::targetObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#targetObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QPropertyAnimation::targetObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QPropertyAnimation12targetObjectEv',
    )
    return QObject._cuteAt(address)

  def propertyName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QPropertyAnimation::propertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#propertyName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QPropertyAnimation::propertyName() const
    address = self.uglySide.call(
        'ritual_ZNK18QPropertyAnimation12propertyNameEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setTargetObject(self, target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QPropertyAnimation::setTargetObject(QObject *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#setTargetObject

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyAnimation::setTargetObject(QObject *target)
    self.uglySide.call(
        'ritual_ZN18QPropertyAnimation15setTargetObjectEP7QObject',
        self._addressOf(target, 'QObject'),
    )

  @overload(QByteArray)
  def setPropertyName(self, propertyName: QByteArray) -> None:
    """
    Calls Qt's 'void QPropertyAnimation::setPropertyName(const QByteArray
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#setPropertyName

    Parameters
    ----------

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QPropertyAnimation::setPropertyName(const QByteArray
    #      &propertyName)
    self.uglySide.call(
        'ritual_ZN18QPropertyAnimation15setPropertyNameERK10QByteArray',
        self._valueOf(propertyName),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyAnimation::QPropertyAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#QPropertyAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPropertyAnimation::QPropertyAnimation(QObject *parent)
    self._noteCreation(QPropertyAnimation, lambda: Rituals.call(
        'ritual_ZN18QPropertyAnimationC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QObject, QByteArray)
  @overload(NoneType, QByteArray)
  @overload(QObject, QByteArray, QObject)
  @overload(QObject, QByteArray, NoneType)
  @overload(NoneType, QByteArray, QObject)
  @overload(NoneType, QByteArray, NoneType)
  def __init__(
      self,
      target: Optional[QObject],
      propertyName: QByteArray,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyAnimation::QPropertyAnimation(QObject *target, const QByteArray
    &propertyName, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#QPropertyAnimation

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPropertyAnimation::QPropertyAnimation(QObject *target, const
    #      QByteArray &propertyName, QObject *parent)
    self._noteCreation(QPropertyAnimation, lambda: Rituals.call(
        'ritual_ZN18QPropertyAnimationC1EP7QObjectRK10QByteArrayS1_',
        self._addressOf(target, 'QObject'), self._valueOf(propertyName),
        self._addressOf(parent, 'QObject'),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QPropertyAnimation::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpropertyanimation.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPropertyAnimation::event(QEvent *event)
    ritual = 'ritual_ZN18QPropertyAnimation5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPropertyAnimation5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QVariant)
  def updateCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QPropertyAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPropertyAnimation::updateCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN18QPropertyAnimation18updateCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPropertyAnimation18updateCurrentValueERK8QVarian'
          't')
    self.uglySide.call(ritual, self._valueOf(value))

  @overload(QAbstractAnimation.State, QAbstractAnimation.State)
  def updateState(
      self,
      newState: QAbstractAnimation.State,
      oldState: QAbstractAnimation.State,
  ) -> None:
    """
    Calls Qt's 'void
    QPropertyAnimation::updateState(QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertyanimation.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimation.State
      Passed on as its number.

    oldState : QAbstractAnimation.State
      Passed on as its number.
    """
    #  void QPropertyAnimation::updateState(QAbstractAnimation::State
    #      newState, QAbstractAnimation::State oldState)
    ritual = (
        'ritual_ZN18QPropertyAnimation11updateStateEN18QAbstractAnimation5S'
        'tateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPropertyAnimation11updateStateEN18QAbstractAnima'
          'tion5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)
