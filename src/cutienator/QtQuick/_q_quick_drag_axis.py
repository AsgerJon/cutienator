"""
QQuickDragAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdragaxis_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDragAxis to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickPointerHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPointerHandler = WAIT['QQuickPointerHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDragAxis(QObject):
  """
  The cute side of Qt's QQuickDragAxis: a plain Python object standing in
  front of one C++ QQuickDragAxis.

  It is built on the cute 'QObject', as Qt's QQuickDragAxis is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDragAxis that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'minimum', 'setMinimum',
  'maximum', 'setMaximum', 'enabled', 'setEnabled', 'activeValue',
  'persistentValue', 'onActiveChanged', 'updateValue', 'minimumChanged',
  'maximumChanged', 'enabledChanged', 'activeValueChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDragAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickDragAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDragAxis::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickDragAxis is created at the first use, not by
    'QQuickDragAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDragAxis.
  - Qt tells when it has removed the C++ QQuickDragAxis. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickDragAxis that has no cute function yet,
    'targetValue', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QQuickDragAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#tr

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
    #  QString QQuickDragAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickDragAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDragAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDragAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDragAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickDragAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimum(self) -> float:
    """
    Calls Qt's 'qreal QQuickDragAxis::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#minimum
    """
    #  qreal QQuickDragAxis::minimum() const
    return self.uglySide.call('ritual_ZNK14QQuickDragAxis7minimumEv')

  def maximum(self) -> float:
    """
    Calls Qt's 'qreal QQuickDragAxis::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#maximum
    """
    #  qreal QQuickDragAxis::maximum() const
    return self.uglySide.call('ritual_ZNK14QQuickDragAxis7maximumEv')

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragAxis::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#enabled
    """
    #  bool QQuickDragAxis::enabled() const
    return self.uglySide.call('ritual_ZNK14QQuickDragAxis7enabledEv')

  def activeValue(self) -> float:
    """
    Calls Qt's 'qreal QQuickDragAxis::activeValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#activeValue
    """
    #  qreal QQuickDragAxis::activeValue() const
    return self.uglySide.call('ritual_ZNK14QQuickDragAxis11activeValueEv')

  def persistentValue(self) -> float:
    """
    Calls Qt's 'qreal QQuickDragAxis::persistentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragaxis.html#persistentValue
    """
    #  qreal QQuickDragAxis::persistentValue() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickDragAxis15persistentValueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMinimum(self, minimum: float) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::setMinimum(qreal minimum)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#setMinimum

    Parameters
    ----------

    minimum : float
      Passed on as it is.
    """
    #  void QQuickDragAxis::setMinimum(qreal minimum)
    self.uglySide.call('ritual_ZN14QQuickDragAxis10setMinimumEd', minimum)

  @overload(float)
  def setMaximum(self, maximum: float) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::setMaximum(qreal maximum)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#setMaximum

    Parameters
    ----------

    maximum : float
      Passed on as it is.
    """
    #  void QQuickDragAxis::setMaximum(qreal maximum)
    self.uglySide.call('ritual_ZN14QQuickDragAxis10setMaximumEd', maximum)

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickDragAxis::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN14QQuickDragAxis10setEnabledEb', enabled)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPointerHandler, str)
  @overload(NoneType, str)
  @overload(QQuickPointerHandler, str, float)
  @overload(NoneType, str, float)
  def __init__(
      self,
      handler: Optional[QQuickPointerHandler],
      propertyName: str,
      initValue: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickDragAxis::QQuickDragAxis(QQuickPointerHandler *handler, const
    QString &propertyName, qreal initValue)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#QQuickDragAxis

    Parameters
    ----------

    handler : Optional[QQuickPointerHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    initValue : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QQuickDragAxis::QQuickDragAxis(QQuickPointerHandler *handler, const
    #      QString &propertyName, qreal initValue)
    self._noteCreation(QQuickDragAxis, lambda: Rituals.call(
        'ritual_ZN14QQuickDragAxisC1EP20QQuickPointerHandlerRK7QStringd',
        self._addressOf(handler), propertyName, initValue,
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

  @overload(bool, float)
  def onActiveChanged(self, active: bool, initActiveValue: float) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::onActiveChanged(bool active, qreal
    initActiveValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragaxis.html#onActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.

    initActiveValue : float
      Passed on as it is.
    """
    #  void QQuickDragAxis::onActiveChanged(bool active, qreal
    #      initActiveValue)
    self.uglySide.call(
        'ritual_ZN14QQuickDragAxis15onActiveChangedEbd',
        active, initActiveValue,
    )

  @overload(float, float)
  @overload(float, float, float)
  def updateValue(
      self,
      activeValue: float,
      accumulatedValue: float,
      delta: float = 0.0,
  ) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::updateValue(qreal activeValue, qreal
    accumulatedValue, qreal delta)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#updateValue

    Parameters
    ----------

    activeValue : float
      Passed on as it is.

    accumulatedValue : float
      Passed on as it is.

    delta : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QQuickDragAxis::updateValue(qreal activeValue, qreal
    #      accumulatedValue, qreal delta)
    self.uglySide.call(
        'ritual_ZN14QQuickDragAxis11updateValueEddd',
        activeValue, accumulatedValue, delta,
    )

  def minimumChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::minimumChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#minimumChanged
    """
    #  void QQuickDragAxis::minimumChanged()
    self.uglySide.call('ritual_ZN14QQuickDragAxis14minimumChangedEv')

  def maximumChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::maximumChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#maximumChanged
    """
    #  void QQuickDragAxis::maximumChanged()
    self.uglySide.call('ritual_ZN14QQuickDragAxis14maximumChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragaxis.html#enabledChanged
    """
    #  void QQuickDragAxis::enabledChanged()
    self.uglySide.call('ritual_ZN14QQuickDragAxis14enabledChangedEv')

  @overload(float)
  def activeValueChanged(self, delta: float) -> None:
    """
    Calls Qt's 'void QQuickDragAxis::activeValueChanged(qreal delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragaxis.html#activeValueChanged

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void QQuickDragAxis::activeValueChanged(qreal delta)
    self.uglySide.call(
        'ritual_ZN14QQuickDragAxis18activeValueChangedEd', delta,
    )

  @staticmethod
  def targetValue(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickDragAxis::targetValue()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickDragAxis.targetValue' has no cute function yet. Qt's 'qreal "
        "QQuickDragAxis::targetValue()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
