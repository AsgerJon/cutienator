"""
QQmlBind binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlbind_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlBind to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus, QQmlPropertyValueSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProperty = WAIT['QQmlProperty']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlBind(QObject, QQmlPropertyValueSource, QQmlParserStatus):
  """
  The cute side of Qt's QQmlBind: a plain Python object standing in front of
  one C++ QQmlBind.

  It is built on the cute 'QObject', as Qt's QQmlBind is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlPropertyValueSource' as well, as Qt's QQmlBind is built on Qt's
  QQmlPropertyValueSource too, and has everything that class has. It is built
  on the cute 'QQmlParserStatus' as well, as Qt's QQmlBind is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlBind that has a ritual and that Python can call
  so far, 26 names in all: 'metaObject', 'tr', 'when', 'setWhen', 'object',
  'setObject', 'property', 'setProperty', 'value', 'setValue', 'delayed',
  'setDelayed', 'restoreMode', 'setRestoreMode', 'restoreModeChanged',
  'objectChanged', 'propertyChanged', 'valueChanged', 'whenChanged',
  'delayedChanged', 'setTarget', 'classBegin', 'componentComplete',
  'prepareEval', 'eval', 'targetValueChanged'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlBind::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QQmlBind::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlBindPrivate *QQmlBind::d_func()': gives 'QQmlBindPrivate',
    which has no cute class yet.
  - Qt's 'const QQmlBindPrivate *QQmlBind::d_func() const': gives
    'QQmlBindPrivate', which has no cute class yet.
  - Qt's 'QQmlBind::~QQmlBind()': the destructor: Python never removes a C++
    QQmlBind.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlBind is created at the first use, not by 'QQmlBind(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlBind.
  - Qt tells when it has removed the C++ QQmlBind. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQmlBind, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class RestorationMode(CuteNum):
    """
    The enum 'QQmlBind::RestorationMode' of Qt, with the 4 names Qt gives in
    it.
    """

    RestoreNone = Kee[int](0)
    RestoreBinding = Kee[int](1)
    RestoreValue = Kee[int](2)
    RestoreBindingOrValue = Kee[int](3)

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
    Calls Qt's 'QString QQmlBind::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#tr

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
    #  QString QQmlBind::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QQmlBind2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlBind'

  #  Qt's QQmlBind is built on more than one class. The part of a C++
  #  QQmlBind that belongs to a class after the first begins somewhere inside
  #  the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlPropertyValueSource':
          'ritual_cast_QQmlBind_QQmlPropertyValueSource',
      'QQmlParserStatus': 'ritual_cast_QQmlBind_QQmlParserStatus',
  }

  #  A C++ QQmlBind Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlBind'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlBind::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlBind::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QQmlBind10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def when(self) -> bool:
    """
    Calls Qt's 'bool QQmlBind::when() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#when
    """
    #  bool QQmlBind::when() const
    return self.uglySide.call('ritual_ZNK8QQmlBind4whenEv')

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlBind::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlBind::object() const
    address = self.uglySide.call('ritual_ZNK8QQmlBind6objectEv')
    return QObject._cuteAt(address)

  def property(self) -> str:
    """
    Calls Qt's 'QString QQmlBind::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#property

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlBind::property() const
    return self.uglySide.call('ritual_ZNK8QQmlBind8propertyEv')

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlBind::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlBind::value() const
    address = self.uglySide.call('ritual_ZNK8QQmlBind5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delayed(self) -> bool:
    """
    Calls Qt's 'bool QQmlBind::delayed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#delayed
    """
    #  bool QQmlBind::delayed() const
    return self.uglySide.call('ritual_ZNK8QQmlBind7delayedEv')

  def restoreMode(self) -> RestorationMode:
    """
    Calls Qt's 'RestorationMode QQmlBind::restoreMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#restoreMode

    Returns
    -------

    RestorationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RestorationMode(number)'
      gives.
    """
    #  RestorationMode QQmlBind::restoreMode() const
    return QQmlBind.RestorationMode(self.uglySide.call(
        'ritual_ZNK8QQmlBind11restoreModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setWhen(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQmlBind::setWhen(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#setWhen

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQmlBind::setWhen(bool a0)
    self.uglySide.call('ritual_ZN8QQmlBind7setWhenEb', a0)

  @overload(QObject)
  @overload(NoneType)
  def setObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlBind::setObject(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#setObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlBind::setObject(QObject *a0)
    self.uglySide.call(
        'ritual_ZN8QQmlBind9setObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(str)
  def setProperty(self, a0: str) -> None:
    """
    Calls Qt's 'void QQmlBind::setProperty(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#setProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlBind::setProperty(const QString &a0)
    self.uglySide.call('ritual_ZN8QQmlBind11setPropertyERK7QString', a0)

  @overload(QVariant)
  def setValue(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQmlBind::setValue(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#setValue

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlBind::setValue(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN8QQmlBind8setValueERK8QVariant', self._valueOf(a0),
    )

  @overload(bool)
  def setDelayed(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQmlBind::setDelayed(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#setDelayed

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQmlBind::setDelayed(bool a0)
    self.uglySide.call('ritual_ZN8QQmlBind10setDelayedEb', a0)

  @overload(RestorationMode)
  def setRestoreMode(self, a0: RestorationMode) -> None:
    """
    Calls Qt's 'void QQmlBind::setRestoreMode(RestorationMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#setRestoreMode

    Parameters
    ----------

    a0 : RestorationMode
      Passed on as its number.
    """
    #  void QQmlBind::setRestoreMode(RestorationMode a0)
    self.uglySide.call(
        'ritual_ZN8QQmlBind14setRestoreModeENS_15RestorationModeE', a0.value,
    )

  @overload(QQmlProperty)
  def setTarget(self, a0: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQmlBind::setTarget(const QQmlProperty &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#setTarget

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlBind::setTarget(const QQmlProperty &a0)
    ritual = 'ritual_ZN8QQmlBind9setTargetERK12QQmlProperty'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QQmlBind9setTargetERK12QQmlProperty'
    self.uglySide.call(ritual, self._valueOf(a0))

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
    Notes what was given, for Qt's 'QQmlBind::QQmlBind(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#QQmlBind

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlBind::QQmlBind(QObject *parent)
    self._noteCreation(QQmlBind, lambda: Rituals.call(
        'ritual_ZN8QQmlBindC1EP7QObject', self._addressOf(parent, 'QObject'),
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

  def restoreModeChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBind::restoreModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#restoreModeChanged
    """
    #  void QQmlBind::restoreModeChanged()
    self.uglySide.call('ritual_ZN8QQmlBind18restoreModeChangedEv')

  def objectChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBind::objectChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#objectChanged
    """
    #  void QQmlBind::objectChanged()
    self.uglySide.call('ritual_ZN8QQmlBind13objectChangedEv')

  def propertyChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBind::propertyChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#propertyChanged
    """
    #  void QQmlBind::propertyChanged()
    self.uglySide.call('ritual_ZN8QQmlBind15propertyChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBind::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#valueChanged
    """
    #  void QQmlBind::valueChanged()
    self.uglySide.call('ritual_ZN8QQmlBind12valueChangedEv')

  def whenChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBind::whenChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#whenChanged
    """
    #  void QQmlBind::whenChanged()
    self.uglySide.call('ritual_ZN8QQmlBind11whenChangedEv')

  def delayedChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBind::delayedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#delayedChanged
    """
    #  void QQmlBind::delayedChanged()
    self.uglySide.call('ritual_ZN8QQmlBind14delayedChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlBind::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#classBegin
    """
    #  void QQmlBind::classBegin()
    ritual = 'ritual_ZN8QQmlBind10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QQmlBind10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlBind::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#componentComplete
    """
    #  void QQmlBind::componentComplete()
    ritual = 'ritual_ZN8QQmlBind17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QQmlBind17componentCompleteEv'
    self.uglySide.call(ritual)

  def prepareEval(self) -> None:
    """
    Calls Qt's 'void QQmlBind::prepareEval()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#prepareEval
    """
    #  void QQmlBind::prepareEval()
    self.uglySide.call('ritual_ZN8QQmlBind11prepareEvalEv')

  def eval(self) -> None:
    """
    Calls Qt's 'void QQmlBind::eval()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#eval
    """
    #  void QQmlBind::eval()
    self.uglySide.call('ritual_ZN8QQmlBind4evalEv')

  def targetValueChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBind::targetValueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbind.html#targetValueChanged
    """
    #  void QQmlBind::targetValueChanged()
    self.uglySide.call('ritual_ZN8QQmlBind18targetValueChangedEv')
