"""
QQuickBehavior binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickbehavior_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickBehavior to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlFinalizerHook, QQmlPropertyValueInterceptor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUntypedBindable, QVariant
  from ..QtQml import QQmlProperty
  from . import QQuickAbstractAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProperty = WAIT['QQmlProperty']
  QQuickAbstractAnimation = WAIT['QQuickAbstractAnimation']
  QUntypedBindable = WAIT['QUntypedBindable']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBehavior(QObject, QQmlPropertyValueInterceptor, QQmlFinalizerHook):
  """
  The cute side of Qt's QQuickBehavior: a plain Python object standing in
  front of one C++ QQuickBehavior.

  It is built on the cute 'QObject', as Qt's QQuickBehavior is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlPropertyValueInterceptor' as well, as Qt's QQuickBehavior is built on
  Qt's QQmlPropertyValueInterceptor too, and has everything that class has.
  It is built on the cute 'QQmlFinalizerHook' as well, as Qt's QQuickBehavior
  is built on Qt's QQmlFinalizerHook too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickBehavior that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'setTarget', 'write',
  'bindable', 'animation', 'setAnimation', 'enabled', 'setEnabled',
  'targetValue', 'targetProperty', 'componentFinalized', 'enabledChanged',
  'targetValueChanged', 'targetPropertyChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBehavior::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickBehavior::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickBehaviorPrivate *QQuickBehavior::d_func()': gives
    'QQuickBehaviorPrivate', which has no cute class yet.
  - Qt's 'const QQuickBehaviorPrivate *QQuickBehavior::d_func() const': gives
    'QQuickBehaviorPrivate', which has no cute class yet.
  - Qt's 'QQuickBehavior::~QQuickBehavior()': the destructor: Python never
    removes a C++ QQuickBehavior.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickBehavior is created at the first use, not by
    'QQuickBehavior(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBehavior.
  - Qt tells when it has removed the C++ QQuickBehavior. Every call on the
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
    Calls Qt's 'QString QQuickBehavior::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#tr

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
    #  QString QQuickBehavior::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickBehavior2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBehavior'

  #  Qt's QQuickBehavior is built on more than one class. The part of a C++
  #  QQuickBehavior that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlPropertyValueInterceptor':
          'ritual_cast_QQuickBehavior_QQmlPropertyValueInterceptor',
      'QQmlFinalizerHook': 'ritual_cast_QQuickBehavior_QQmlFinalizerHook',
  }

  #  A C++ QQuickBehavior Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickBehavior'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBehavior::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBehavior::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickBehavior10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickBehavior::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#enabled
    """
    #  bool QQuickBehavior::enabled() const
    return self.uglySide.call('ritual_ZNK14QQuickBehavior7enabledEv')

  def targetValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickBehavior::targetValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#targetValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickBehavior::targetValue() const
    address = self.uglySide.call('ritual_ZNK14QQuickBehavior11targetValueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def targetProperty(self) -> QQmlProperty:
    """
    Calls Qt's 'QQmlProperty QQuickBehavior::targetProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#targetProperty

    Returns
    -------

    QQmlProperty
      A new cute QQmlProperty around the copy Qt gave back. Python owns it.
    """
    #  QQmlProperty QQuickBehavior::targetProperty() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickBehavior14targetPropertyEv',
    )
    from ..QtQml import QQmlProperty
    return QQmlProperty._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlProperty)
  def setTarget(self, a0: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQuickBehavior::setTarget(const QQmlProperty &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#setTarget

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQuickBehavior::setTarget(const QQmlProperty &a0)
    ritual = 'ritual_ZN14QQuickBehavior9setTargetERK12QQmlProperty'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickBehavior9setTargetERK12QQmlProperty'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QQuickAbstractAnimation)
  @overload(NoneType)
  def setAnimation(self, a0: Optional[QQuickAbstractAnimation]) -> None:
    """
    Calls Qt's 'void QQuickBehavior::setAnimation(QQuickAbstractAnimation
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#setAnimation

    Parameters
    ----------

    a0 : Optional[QQuickAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBehavior::setAnimation(QQuickAbstractAnimation *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickBehavior12setAnimationEP23QQuickAbstractAnimation',
        self._addressOf(a0),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickBehavior::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickBehavior::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN14QQuickBehavior10setEnabledEb', enabled)

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
    Notes what was given, for Qt's 'QQuickBehavior::QQuickBehavior(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#QQuickBehavior

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickBehavior::QQuickBehavior(QObject *parent)
    self._noteCreation(QQuickBehavior, lambda: Rituals.call(
        'ritual_ZN14QQuickBehaviorC1EP7QObject',
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

  @overload(QVariant)
  def write(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQuickBehavior::write(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#write

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickBehavior::write(const QVariant &value)
    ritual = 'ritual_ZN14QQuickBehavior5writeERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickBehavior5writeERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(value))

  @overload(QUntypedBindable, QUntypedBindable)
  @overload(NoneType, QUntypedBindable)
  def bindable(
      self,
      untypedBindable: Optional[QUntypedBindable],
      target: QUntypedBindable,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickBehavior::bindable(QUntypedBindable
    *untypedBindable, QUntypedBindable target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#bindable

    Parameters
    ----------

    untypedBindable : Optional[QUntypedBindable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : QUntypedBindable
      Passed on as a value: Qt reads the C++ QUntypedBindable, which stays
      Python's own.
    """
    #  bool QQuickBehavior::bindable(QUntypedBindable *untypedBindable,
    #      QUntypedBindable target)
    ritual = 'ritual_ZN14QQuickBehavior8bindableEP16QUntypedBindableS0_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickBehavior8bindableEP16QUntypedBindableS0_')
    return self.uglySide.call(
        ritual, self._addressOf(untypedBindable), self._valueOf(target),
    )

  def animation(self) -> Optional[QQuickAbstractAnimation]:
    """
    Calls Qt's 'QQuickAbstractAnimation *QQuickBehavior::animation()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#animation

    Returns
    -------

    Optional[QQuickAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractAnimation *QQuickBehavior::animation()
    address = self.uglySide.call('ritual_ZN14QQuickBehavior9animationEv')
    from . import QQuickAbstractAnimation
    return QQuickAbstractAnimation._cuteAt(address)

  def componentFinalized(self) -> None:
    """
    Calls Qt's 'void QQuickBehavior::componentFinalized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbehavior.html#componentFinalized
    """
    #  void QQuickBehavior::componentFinalized()
    ritual = 'ritual_ZN14QQuickBehavior18componentFinalizedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickBehavior18componentFinalizedEv'
    self.uglySide.call(ritual)

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBehavior::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbehavior.html#enabledChanged
    """
    #  void QQuickBehavior::enabledChanged()
    self.uglySide.call('ritual_ZN14QQuickBehavior14enabledChangedEv')

  def targetValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBehavior::targetValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbehavior.html#targetValueChanged
    """
    #  void QQuickBehavior::targetValueChanged()
    self.uglySide.call('ritual_ZN14QQuickBehavior18targetValueChangedEv')

  def targetPropertyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBehavior::targetPropertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbehavior.html#targetPropertyChanged
    """
    #  void QQuickBehavior::targetPropertyChanged()
    self.uglySide.call('ritual_ZN14QQuickBehavior21targetPropertyChangedEv')
