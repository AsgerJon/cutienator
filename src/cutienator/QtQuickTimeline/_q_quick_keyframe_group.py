"""
QQuickKeyframeGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquickkeyframe_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickKeyframeGroup to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickKeyframeGroup(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickKeyframeGroup: a plain Python object standing
  in front of one C++ QQuickKeyframeGroup.

  It is built on the cute 'QObject', as Qt's QQuickKeyframeGroup is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickKeyframeGroup is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickKeyframeGroup that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'target',
  'setTargetObject', 'property', 'setProperty', 'keyframeSource',
  'setKeyframeSource', 'keyframeData', 'setKeyframeData', 'evaluate', 'init',
  'resetDefaultValue', 'reset', 'setupKeyframes', 'classBegin',
  'componentComplete', 'targetChanged', 'propertyChanged',
  'keyframeSourceChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickKeyframeGroup::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickKeyframeGroup::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickKeyframeGroupPrivate *QQuickKeyframeGroup::d_func()': gives
    'QQuickKeyframeGroupPrivate', which has no cute class yet.
  - Qt's 'const QQuickKeyframeGroupPrivate *QQuickKeyframeGroup::d_func()
    const': gives 'QQuickKeyframeGroupPrivate', which has no cute class yet.
  - Qt's 'QQmlListProperty<QQuickKeyframe> QQuickKeyframeGroup::keyframes()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickKeyframeGroup is created at the first use, not by
    'QQuickKeyframeGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickKeyframeGroup.
  - Qt tells when it has removed the C++ QQuickKeyframeGroup. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickKeyframeGroup that has no cute function yet,
    'keyframes', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuickKeyframeGroup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframegroup.html#tr

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
    #  QString QQuickKeyframeGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickKeyframeGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickKeyframeGroup'

  #  Qt's QQuickKeyframeGroup is built on more than one class. The part of a
  #  C++ QQuickKeyframeGroup that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickKeyframeGroup_QQmlParserStatus',
  }

  #  A C++ QQuickKeyframeGroup Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickKeyframeGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickKeyframeGroup::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickKeyframeGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickKeyframeGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickKeyframeGroup::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframegroup.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickKeyframeGroup::target() const
    address = self.uglySide.call('ritual_ZNK19QQuickKeyframeGroup6targetEv')
    return QObject._cuteAt(address)

  def property(self) -> str:
    """
    Calls Qt's 'QString QQuickKeyframeGroup::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframegroup.html#property

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickKeyframeGroup::property() const
    return self.uglySide.call('ritual_ZNK19QQuickKeyframeGroup8propertyEv')

  def keyframeSource(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickKeyframeGroup::keyframeSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#keyframeSource

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickKeyframeGroup::keyframeSource() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickKeyframeGroup14keyframeSourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def keyframeData(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray QQuickKeyframeGroup::keyframeData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#keyframeData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray QQuickKeyframeGroup::keyframeData() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickKeyframeGroup12keyframeDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(float)
  def evaluate(self, frame: float) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickKeyframeGroup::evaluate(qreal frame) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframegroup.html#evaluate

    Parameters
    ----------

    frame : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickKeyframeGroup::evaluate(qreal frame) const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickKeyframeGroup8evaluateEd', frame,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setTargetObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::setTargetObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#setTargetObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeyframeGroup::setTargetObject(QObject *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickKeyframeGroup15setTargetObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(str)
  def setProperty(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::setProperty(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#setProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickKeyframeGroup::setProperty(const QString &a0)
    self.uglySide.call(
        'ritual_ZN19QQuickKeyframeGroup11setPropertyERK7QString', a0,
    )

  @overload(float)
  def setProperty(self, frame: float) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::setProperty(qreal frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#setProperty

    Parameters
    ----------

    frame : float
      Passed on as it is.
    """
    #  void QQuickKeyframeGroup::setProperty(qreal frame)
    self.uglySide.call(
        'ritual_ZN19QQuickKeyframeGroup11setPropertyEd', frame,
    )

  @overload(QUrl)
  def setKeyframeSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::setKeyframeSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#setKeyframeSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickKeyframeGroup::setKeyframeSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN19QQuickKeyframeGroup17setKeyframeSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(QByteArray)
  def setKeyframeData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::setKeyframeData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#setKeyframeData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickKeyframeGroup::setKeyframeData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN19QQuickKeyframeGroup15setKeyframeDataERK10QByteArray',
        self._valueOf(data),
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
    'QQuickKeyframeGroup::QQuickKeyframeGroup(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#QQuickKeyframeGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickKeyframeGroup::QQuickKeyframeGroup(QObject *parent)
    self._noteCreation(QQuickKeyframeGroup, lambda: Rituals.call(
        'ritual_ZN19QQuickKeyframeGroupC1EP7QObject',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframegroup.html#init
    """
    #  void QQuickKeyframeGroup::init()
    self.uglySide.call('ritual_ZN19QQuickKeyframeGroup4initEv')

  def resetDefaultValue(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::resetDefaultValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#resetDefaultValue
    """
    #  void QQuickKeyframeGroup::resetDefaultValue()
    self.uglySide.call('ritual_ZN19QQuickKeyframeGroup17resetDefaultValueEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframegroup.html#reset
    """
    #  void QQuickKeyframeGroup::reset()
    self.uglySide.call('ritual_ZN19QQuickKeyframeGroup5resetEv')

  def setupKeyframes(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::setupKeyframes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#setupKeyframes
    """
    #  void QQuickKeyframeGroup::setupKeyframes()
    self.uglySide.call('ritual_ZN19QQuickKeyframeGroup14setupKeyframesEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#classBegin
    """
    #  void QQuickKeyframeGroup::classBegin()
    ritual = 'ritual_ZN19QQuickKeyframeGroup10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickKeyframeGroup10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#componentComplete
    """
    #  void QQuickKeyframeGroup::componentComplete()
    ritual = 'ritual_ZN19QQuickKeyframeGroup17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickKeyframeGroup17componentCompleteEv'
    self.uglySide.call(ritual)

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#targetChanged
    """
    #  void QQuickKeyframeGroup::targetChanged()
    self.uglySide.call('ritual_ZN19QQuickKeyframeGroup13targetChangedEv')

  def propertyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::propertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#propertyChanged
    """
    #  void QQuickKeyframeGroup::propertyChanged()
    self.uglySide.call('ritual_ZN19QQuickKeyframeGroup15propertyChangedEv')

  def keyframeSourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframeGroup::keyframeSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframegroup.html#keyframeSourceChanged
    """
    #  void QQuickKeyframeGroup::keyframeSourceChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickKeyframeGroup21keyframeSourceChangedEv',
    )

  @staticmethod
  def keyframes(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickKeyframe> QQuickKeyframeGroup::keyframes()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickKeyframeGroup.keyframes' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickKeyframe> "
        "QQuickKeyframeGroup::keyframes()': gives a type Python has no way "
        "to take yet.")
