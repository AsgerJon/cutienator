"""
QQmlSynchronizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsSynchronizer/6.12.0/QtLabsSynchronizer/private/qqmlsynchronizer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlSynchronizer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProperty = WAIT['QQmlProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlSynchronizer(QObject):
  """
  The cute side of Qt's QQmlSynchronizer: a plain Python object standing in
  front of one C++ QQmlSynchronizer.

  It is built on the cute 'QObject', as Qt's QQmlSynchronizer is built on
  Qt's QObject, and has everything that class has. Qt's QQmlSynchronizer is
  built on Qt's QQmlPropertyValueSource as well, which is not reflected. Qt's
  QQmlSynchronizer is built on Qt's QQmlFinalizerHook as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQmlSynchronizer that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'sourceObject',
  'setSourceObject', 'sourceProperty', 'setSourceProperty', 'targetObject',
  'setTargetObject', 'targetProperty', 'setTargetProperty',
  'sourceObjectChanged', 'sourcePropertyChanged', 'targetObjectChanged',
  'targetPropertyChanged', 'valueBounced', 'valueIgnored', 'setTarget',
  'componentFinalized'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlSynchronizer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlSynchronizer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlSynchronizerPrivate *QQmlSynchronizer::d_func()': gives
    'QQmlSynchronizerPrivate', which has no cute class yet.
  - Qt's 'const QQmlSynchronizerPrivate *QQmlSynchronizer::d_func() const':
    gives 'QQmlSynchronizerPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlSynchronizer is created at the first use, not by
    'QQmlSynchronizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSynchronizer.
  - Qt tells when it has removed the C++ QQmlSynchronizer. Every call on the
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
    Calls Qt's 'QString QQmlSynchronizer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsynchronizer.html#tr

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
    #  QString QQmlSynchronizer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlSynchronizer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSynchronizer'

  #  A C++ QQmlSynchronizer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSynchronizer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlSynchronizer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsynchronizer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlSynchronizer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlSynchronizer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlSynchronizer::sourceObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsynchronizer.html#sourceObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlSynchronizer::sourceObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlSynchronizer12sourceObjectEv',
    )
    return QObject._cuteAt(address)

  def sourceProperty(self) -> str:
    """
    Calls Qt's 'QString QQmlSynchronizer::sourceProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#sourceProperty

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSynchronizer::sourceProperty() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlSynchronizer14sourcePropertyEv',
    )

  def targetObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlSynchronizer::targetObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsynchronizer.html#targetObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlSynchronizer::targetObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlSynchronizer12targetObjectEv',
    )
    return QObject._cuteAt(address)

  def targetProperty(self) -> str:
    """
    Calls Qt's 'QString QQmlSynchronizer::targetProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#targetProperty

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSynchronizer::targetProperty() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlSynchronizer14targetPropertyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setSourceObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::setSourceObject(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#setSourceObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlSynchronizer::setSourceObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer15setSourceObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(str)
  def setSourceProperty(self, property: str) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::setSourceProperty(const QString
    &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#setSourceProperty

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSynchronizer::setSourceProperty(const QString &property)
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer17setSourcePropertyERK7QString',
        property,
    )

  @overload(QObject)
  @overload(NoneType)
  def setTargetObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::setTargetObject(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#setTargetObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlSynchronizer::setTargetObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer15setTargetObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(str)
  def setTargetProperty(self, property: str) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::setTargetProperty(const QString
    &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#setTargetProperty

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSynchronizer::setTargetProperty(const QString &property)
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer17setTargetPropertyERK7QString',
        property,
    )

  @overload(QQmlProperty)
  def setTarget(self, target: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::setTarget(const QQmlProperty
    &target)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsynchronizer.html#setTarget

    Parameters
    ----------

    target : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlSynchronizer::setTarget(const QQmlProperty &target)
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer9setTargetERK12QQmlProperty',
        self._valueOf(target),
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
    'QQmlSynchronizer::QQmlSynchronizer(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#QQmlSynchronizer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlSynchronizer::QQmlSynchronizer(QObject *parent)
    self._noteCreation(QQmlSynchronizer, lambda: Rituals.call(
        'ritual_ZN16QQmlSynchronizerC1EP7QObject',
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

  def sourceObjectChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::sourceObjectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#sourceObjectChanged
    """
    #  void QQmlSynchronizer::sourceObjectChanged()
    self.uglySide.call('ritual_ZN16QQmlSynchronizer19sourceObjectChangedEv')

  def sourcePropertyChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::sourcePropertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#sourcePropertyChanged
    """
    #  void QQmlSynchronizer::sourcePropertyChanged()
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer21sourcePropertyChangedEv',
    )

  def targetObjectChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::targetObjectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#targetObjectChanged
    """
    #  void QQmlSynchronizer::targetObjectChanged()
    self.uglySide.call('ritual_ZN16QQmlSynchronizer19targetObjectChangedEv')

  def targetPropertyChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::targetPropertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#targetPropertyChanged
    """
    #  void QQmlSynchronizer::targetPropertyChanged()
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer21targetPropertyChangedEv',
    )

  @overload(QObject, str)
  @overload(NoneType, str)
  def valueBounced(self, object: Optional[QObject], property: str) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::valueBounced(QObject *object, const
    QString &property)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsynchronizer.html#valueBounced

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSynchronizer::valueBounced(QObject *object, const QString
    #      &property)
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer12valueBouncedEP7QObjectRK7QString',
        self._addressOf(object, 'QObject'), property,
    )

  @overload(QObject, str)
  @overload(NoneType, str)
  def valueIgnored(self, object: Optional[QObject], property: str) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::valueIgnored(QObject *object, const
    QString &property)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsynchronizer.html#valueIgnored

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSynchronizer::valueIgnored(QObject *object, const QString
    #      &property)
    self.uglySide.call(
        'ritual_ZN16QQmlSynchronizer12valueIgnoredEP7QObjectRK7QString',
        self._addressOf(object, 'QObject'), property,
    )

  def componentFinalized(self) -> None:
    """
    Calls Qt's 'void QQmlSynchronizer::componentFinalized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsynchronizer.html#componentFinalized
    """
    #  void QQmlSynchronizer::componentFinalized()
    self.uglySide.call('ritual_ZN16QQmlSynchronizer18componentFinalizedEv')
