"""
QGesture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGesture(QObject):
  """
  The cute side of Qt's QGesture: a plain Python object standing in front of
  one C++ QGesture.

  It is built on the cute 'QObject', as Qt's QGesture is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGesture that has a ritual and that Python can call
  so far, 10 names in all: 'metaObject', 'tr', 'gestureType', 'state',
  'hotSpot', 'setHotSpot', 'hasHotSpot', 'unsetHotSpot',
  'setGestureCancelPolicy', 'gestureCancelPolicy'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGesture::~QGesture()': the destructor: Python never removes a C++
    QGesture.

  What has no ritual
  ------------------

  7 of the 19 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QGesture is created at the first use, not by 'QGesture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGesture.
  - Qt tells when it has removed the C++ QGesture. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QGesture, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class GestureCancelPolicy(CuteNum):
    """
    The enum 'QGesture::GestureCancelPolicy' of Qt, with the 2 names Qt gives
    in it.
    """

    CancelNone = Kee[int](0)
    CancelAllInContext = Kee[int](1)

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
    Calls Qt's 'QString QGesture::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#tr

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
    #  QString QGesture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QGesture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGesture'

  #  A C++ QGesture Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGesture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGesture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGesture::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QGesture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def gestureType(self) -> Qt.GestureType:
    """
    Calls Qt's 'Qt::GestureType QGesture::gestureType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#gestureType

    Returns
    -------

    Qt.GestureType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.GestureType(number)'
      gives.
    """
    #  Qt::GestureType QGesture::gestureType() const
    return Qt.GestureType(self.uglySide.call(
        'ritual_ZNK8QGesture11gestureTypeEv',
    ))

  def state(self) -> Qt.GestureState:
    """
    Calls Qt's 'Qt::GestureState QGesture::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#state

    Returns
    -------

    Qt.GestureState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.GestureState(number)'
      gives.
    """
    #  Qt::GestureState QGesture::state() const
    return Qt.GestureState(self.uglySide.call('ritual_ZNK8QGesture5stateEv'))

  def hotSpot(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGesture::hotSpot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#hotSpot

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGesture::hotSpot() const
    address = self.uglySide.call('ritual_ZNK8QGesture7hotSpotEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def hasHotSpot(self) -> bool:
    """
    Calls Qt's 'bool QGesture::hasHotSpot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#hasHotSpot
    """
    #  bool QGesture::hasHotSpot() const
    return self.uglySide.call('ritual_ZNK8QGesture10hasHotSpotEv')

  def gestureCancelPolicy(self) -> GestureCancelPolicy:
    """
    Calls Qt's 'GestureCancelPolicy QGesture::gestureCancelPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#gestureCancelPolicy

    Returns
    -------

    GestureCancelPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'GestureCancelPolicy(number)' gives.
    """
    #  GestureCancelPolicy QGesture::gestureCancelPolicy() const
    return QGesture.GestureCancelPolicy(self.uglySide.call(
        'ritual_ZNK8QGesture19gestureCancelPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setHotSpot(self, value: QPointF) -> None:
    """
    Calls Qt's 'void QGesture::setHotSpot(const QPointF &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#setHotSpot

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGesture::setHotSpot(const QPointF &value)
    self.uglySide.call(
        'ritual_ZN8QGesture10setHotSpotERK7QPointF', self._valueOf(value),
    )

  @overload(GestureCancelPolicy)
  def setGestureCancelPolicy(self, policy: GestureCancelPolicy) -> None:
    """
    Calls Qt's 'void QGesture::setGestureCancelPolicy(GestureCancelPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgesture.html#setGestureCancelPolicy

    Parameters
    ----------

    policy : GestureCancelPolicy
      Passed on as its number.
    """
    #  void QGesture::setGestureCancelPolicy(GestureCancelPolicy policy)
    self.uglySide.call(
        'ritual_ZN8QGesture22setGestureCancelPolicyENS_19GestureCancelPolic'
        'yE',
        policy.value,
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
    Notes what was given, for Qt's 'QGesture::QGesture(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#QGesture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGesture::QGesture(QObject *parent)
    self._noteCreation(QGesture, lambda: Rituals.call(
        'ritual_ZN8QGestureC1EP7QObject', self._addressOf(parent),
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

  def unsetHotSpot(self) -> None:
    """
    Calls Qt's 'void QGesture::unsetHotSpot()'.

    Qt's own words: https://doc.qt.io/qt-6/qgesture.html#unsetHotSpot
    """
    #  void QGesture::unsetHotSpot()
    self.uglySide.call('ritual_ZN8QGesture12unsetHotSpotEv')
