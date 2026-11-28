"""
Qt3DCore::Quick::QQuaternionAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/qquaternionanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::QQuaternionAnimation to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickPropertyAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QQuaternion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuaternionAnimation(QQuickPropertyAnimation):
  """
  The cute side of Qt's Qt3DCore::Quick::QQuaternionAnimation: a plain Python
  object standing in front of one C++ Qt3DCore::Quick::QQuaternionAnimation.

  It is built on the cute 'QQuickPropertyAnimation', as Qt's
  Qt3DCore::Quick::QQuaternionAnimation is built on Qt's
  QQuickPropertyAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::QQuaternionAnimation that has a
  ritual and that Python can call so far, 27 names in all: 'metaObject',
  'tr', 'from_', 'setFrom', 'to', 'setTo', 'type', 'setType',
  'fromXRotation', 'setFromXRotation', 'fromYRotation', 'setFromYRotation',
  'fromZRotation', 'setFromZRotation', 'toXRotation', 'setToXRotation',
  'toYRotation', 'setToYRotation', 'toZRotation', 'setToZRotation',
  'typeChanged', 'fromXRotationChanged', 'fromYRotationChanged',
  'fromZRotationChanged', 'toXRotationChanged', 'toYRotationChanged',
  'toZRotationChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Quick::QQuaternionAnimation::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::Quick::QQuaternionAnimation::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::QQuaternionAnimation is created at the first
    use, not by 'Qt3DCore::Quick::QQuaternionAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::QQuaternionAnimation.
  - Qt tells when it has removed the C++
    Qt3DCore::Quick::QQuaternionAnimation. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The enums Qt writes inside Qt3DCore::Quick::QQuaternionAnimation, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Type(CuteNum):
    """
    The enum 'Qt3DCore::Quick::QQuaternionAnimation::Type' of Qt, with the 2
    names Qt gives in it.
    """

    Slerp = Kee[int](0)
    Nlerp = Kee[int](1)

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
    Calls Qt's 'QString Qt3DCore::Quick::QQuaternionAnimation::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html#tr

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
    #  QString Qt3DCore::Quick::QQuaternionAnimation::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::QQuaternionAnimation'

  #  A C++ Qt3DCore::Quick::QQuaternionAnimation Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_Quick_QQuaternionAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::Quick::QQuaternionAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::Quick::QQuaternionAnimation::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::Quick::QQuaternionAnimation::from()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html#from

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::Quick::QQuaternionAnimation::from() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation4fromEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def to(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::Quick::QQuaternionAnimation::to()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html#to

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::Quick::QQuaternionAnimation::to() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation2toEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type Qt3DCore::Quick::QQuaternionAnimation::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type Qt3DCore::Quick::QQuaternionAnimation::type() const
    return QQuaternionAnimation.Type(self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation4typeEv',
    ))

  def fromXRotation(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::Quick::QQuaternionAnimation::fromXRotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html
    """
    #  float Qt3DCore::Quick::QQuaternionAnimation::fromXRotation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation13fromXRotationEv',
    )

  def fromYRotation(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::Quick::QQuaternionAnimation::fromYRotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html
    """
    #  float Qt3DCore::Quick::QQuaternionAnimation::fromYRotation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation13fromYRotationEv',
    )

  def fromZRotation(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::Quick::QQuaternionAnimation::fromZRotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html
    """
    #  float Qt3DCore::Quick::QQuaternionAnimation::fromZRotation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation13fromZRotationEv',
    )

  def toXRotation(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::Quick::QQuaternionAnimation::toXRotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html
    """
    #  float Qt3DCore::Quick::QQuaternionAnimation::toXRotation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation11toXRotationEv',
    )

  def toYRotation(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::Quick::QQuaternionAnimation::toYRotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html
    """
    #  float Qt3DCore::Quick::QQuaternionAnimation::toYRotation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation11toYRotationEv',
    )

  def toZRotation(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::Quick::QQuaternionAnimation::toZRotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html
    """
    #  float Qt3DCore::Quick::QQuaternionAnimation::toZRotation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation11toZRotationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuaternion)
  def setFrom(self, f: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuaternionAnimation::setFrom(const
    QQuaternion &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html#setFrom

    Parameters
    ----------

    f : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setFrom(const QQuaternion
    #      &f)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation7setFromERK11QQuater'
        'nion',
        self._valueOf(f),
    )

  @overload(QQuaternion)
  def setTo(self, t: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuaternionAnimation::setTo(const
    QQuaternion &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html#setTo

    Parameters
    ----------

    t : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setTo(const QQuaternion
    #      &t)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation5setToERK11QQuaterni'
        'on',
        self._valueOf(t),
    )

  @overload(Type)
  def setType(self, type: Type) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuaternionAnimation::setType(Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html#setType

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setType(Type type)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation7setTypeENS1_4TypeE',
        type.value,
    )

  @overload(float)
  def setFromXRotation(self, f: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::setFromXRotation(float f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setFromXRotation(float f)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation16setFromXRotationEf',
        f,
    )

  @overload(float)
  def setFromYRotation(self, f: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::setFromYRotation(float f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setFromYRotation(float f)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation16setFromYRotationEf',
        f,
    )

  @overload(float)
  def setFromZRotation(self, f: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::setFromZRotation(float f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setFromZRotation(float f)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation16setFromZRotationEf',
        f,
    )

  @overload(float)
  def setToXRotation(self, f: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::setToXRotation(float f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setToXRotation(float f)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation14setToXRotationEf',
        f,
    )

  @overload(float)
  def setToYRotation(self, f: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::setToYRotation(float f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setToYRotation(float f)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation14setToYRotationEf',
        f,
    )

  @overload(float)
  def setToZRotation(self, f: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::setToZRotation(float f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::setToZRotation(float f)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation14setToZRotationEf',
        f,
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
    'Qt3DCore::Quick::QQuaternionAnimation::QQuaternionAnimation(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Quick::QQuaternionAnimation::QQuaternionAnimation(QObject
    #      *parent)
    self._noteCreation(QQuaternionAnimation, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimationC1EP7QObject',
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

  @overload(Type)
  def typeChanged(self, type: Type) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuaternionAnimation::typeChanged(Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::typeChanged(Type type)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation11typeChangedENS1_4T'
        'ypeE',
        type.value,
    )

  @overload(float)
  def fromXRotationChanged(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::fromXRotationChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::fromXRotationChanged(float
    #      value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation20fromXRotationChang'
        'edEf',
        value,
    )

  @overload(float)
  def fromYRotationChanged(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::fromYRotationChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::fromYRotationChanged(float
    #      value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation20fromYRotationChang'
        'edEf',
        value,
    )

  @overload(float)
  def fromZRotationChanged(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::fromZRotationChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::fromZRotationChanged(float
    #      value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation20fromZRotationChang'
        'edEf',
        value,
    )

  @overload(float)
  def toXRotationChanged(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::toXRotationChanged(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::toXRotationChanged(float
    #      value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation18toXRotationChanged'
        'Ef',
        value,
    )

  @overload(float)
  def toYRotationChanged(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::toYRotationChanged(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::toYRotationChanged(float
    #      value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation18toYRotationChanged'
        'Ef',
        value,
    )

  @overload(float)
  def toZRotationChanged(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuaternionAnimation::toZRotationChanged(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquaternionanimation.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuaternionAnimation::toZRotationChanged(float
    #      value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation18toZRotationChanged'
        'Ef',
        value,
    )
