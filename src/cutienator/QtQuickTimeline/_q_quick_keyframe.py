"""
QQuickKeyframe binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquickkeyframe_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickKeyframe to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEasingCurve, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickKeyframe(QObject):
  """
  The cute side of Qt's QQuickKeyframe: a plain Python object standing in
  front of one C++ QQuickKeyframe.

  It is built on the cute 'QObject', as Qt's QQuickKeyframe is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickKeyframe that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'frame', 'setFrame',
  'reset', 'easing', 'setEasing', 'value', 'setValue', 'evaluate',
  'frameChanged', 'easingCurveChanged', 'valueChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickKeyframe::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickKeyframe::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickKeyframePrivate *QQuickKeyframe::d_func()': gives
    'QQuickKeyframePrivate', which has no cute class yet.
  - Qt's 'const QQuickKeyframePrivate *QQuickKeyframe::d_func() const': gives
    'QQuickKeyframePrivate', which has no cute class yet.
  - Qt's 'QQuickKeyframe::QQuickKeyframe(QQuickKeyframePrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickKeyframe is created at the first use, not by
    'QQuickKeyframe(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickKeyframe.
  - Qt tells when it has removed the C++ QQuickKeyframe. Every call on the
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
    Calls Qt's 'QString QQuickKeyframe::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#tr

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
    #  QString QQuickKeyframe::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickKeyframe2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickKeyframe'

  #  A C++ QQuickKeyframe Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickKeyframe'

  #  The functions Qt calls itself that QQuickKeyframe is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'evaluate': (
          ('_ZNK14QQuickKeyframe8evaluateEPS_di',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'address', 'QtQuickTimeline:QQuickKeyframe'),
               ('double', 'number', ''),
               ('int', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QQuickKeyframe::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickKeyframe::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickKeyframe10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def frame(self) -> float:
    """
    Calls Qt's 'qreal QQuickKeyframe::frame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#frame
    """
    #  qreal QQuickKeyframe::frame() const
    return self.uglySide.call('ritual_ZNK14QQuickKeyframe5frameEv')

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickKeyframe::easing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickKeyframe::easing() const
    address = self.uglySide.call('ritual_ZNK14QQuickKeyframe6easingEv')
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickKeyframe::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickKeyframe::value() const
    address = self.uglySide.call('ritual_ZNK14QQuickKeyframe5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(THIS, float, int)
  @overload(NoneType, float, int)
  def evaluate(
      self,
      pre: Optional[QQuickKeyframe],
      frame: float,
      userType: int,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickKeyframe::evaluate(QQuickKeyframe *pre, qreal
    frame, int userType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#evaluate

    Parameters
    ----------

    pre : Optional[QQuickKeyframe]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frame : float
      Passed on as it is.

    userType : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickKeyframe::evaluate(QQuickKeyframe *pre, qreal frame,
    #      int userType) const
    ritual = 'ritual_ZNK14QQuickKeyframe8evaluateEPS_di'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickKeyframe8evaluateEPS_di'
    address = self.uglySide.call(
        ritual, self._addressOf(pre), frame, userType,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrame(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickKeyframe::setFrame(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#setFrame

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickKeyframe::setFrame(qreal a0)
    self.uglySide.call('ritual_ZN14QQuickKeyframe8setFrameEd', a0)

  @overload(QEasingCurve)
  def setEasing(self, a0: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickKeyframe::setEasing(const QEasingCurve &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#setEasing

    Parameters
    ----------

    a0 : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickKeyframe::setEasing(const QEasingCurve &a0)
    self.uglySide.call(
        'ritual_ZN14QQuickKeyframe9setEasingERK12QEasingCurve',
        self._valueOf(a0),
    )

  @overload(QVariant)
  def setValue(self, v: QVariant) -> None:
    """
    Calls Qt's 'void QQuickKeyframe::setValue(const QVariant &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#setValue

    Parameters
    ----------

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickKeyframe::setValue(const QVariant &v)
    self.uglySide.call(
        'ritual_ZN14QQuickKeyframe8setValueERK8QVariant', self._valueOf(v),
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
    Notes what was given, for Qt's 'QQuickKeyframe::QQuickKeyframe(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#QQuickKeyframe

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickKeyframe::QQuickKeyframe(QObject *parent)
    self._noteCreation(QQuickKeyframe, lambda: Rituals.call(
        'ritual_ZN14QQuickKeyframeC1EP7QObject',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframe::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#reset
    """
    #  void QQuickKeyframe::reset()
    self.uglySide.call('ritual_ZN14QQuickKeyframe5resetEv')

  def frameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframe::frameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#frameChanged
    """
    #  void QQuickKeyframe::frameChanged()
    self.uglySide.call('ritual_ZN14QQuickKeyframe12frameChangedEv')

  def easingCurveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframe::easingCurveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeyframe.html#easingCurveChanged
    """
    #  void QQuickKeyframe::easingCurveChanged()
    self.uglySide.call('ritual_ZN14QQuickKeyframe18easingCurveChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyframe::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyframe.html#valueChanged
    """
    #  void QQuickKeyframe::valueChanged()
    self.uglySide.call('ritual_ZN14QQuickKeyframe12valueChangedEv')
