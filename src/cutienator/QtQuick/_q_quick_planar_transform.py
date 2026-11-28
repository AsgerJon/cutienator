"""
QQuickPlanarTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPlanarTransform to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPlanarTransform(QObject):
  """
  The cute side of Qt's QQuickPlanarTransform: a plain Python object standing
  in front of one C++ QQuickPlanarTransform.

  It is built on the cute 'QObject', as Qt's QQuickPlanarTransform is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPlanarTransform that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'identity',
  'fromAffineMatrix', 'fromTranslate', 'fromScale', 'fromRotate',
  'fromShear'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPlanarTransform::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPlanarTransform::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPlanarTransform::qt_qmlMarker_singleton()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPlanarTransform is created at the first use, not by
    'QQuickPlanarTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPlanarTransform.
  - Qt tells when it has removed the C++ QQuickPlanarTransform. Every call on
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
    Calls Qt's 'QString QQuickPlanarTransform::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickplanartransform.html#tr

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
    #  QString QQuickPlanarTransform::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickPlanarTransform2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def identity() -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuickPlanarTransform::identity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#identity

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuickPlanarTransform::identity()
    address = Rituals.call('ritual_ZN21QQuickPlanarTransform8identityEv')
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  @overload(float, float, float, float, float, float)
  def fromAffineMatrix(
      scaleX: float,
      shearY: float,
      shearX: float,
      scaleY: float,
      translateX: float,
      translateY: float,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuickPlanarTransform::fromAffineMatrix(float
    scaleX, float shearY, float shearX, float scaleY, float translateX, float
    translateY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#fromAffineMatrix

    Parameters
    ----------

    scaleX : float
      Passed on as it is.

    shearY : float
      Passed on as it is.

    shearX : float
      Passed on as it is.

    scaleY : float
      Passed on as it is.

    translateX : float
      Passed on as it is.

    translateY : float
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuickPlanarTransform::fromAffineMatrix(float scaleX, float
    #      shearY, float shearX, float scaleY, float translateX, float
    #      translateY)
    address = Rituals.call(
        'ritual_ZN21QQuickPlanarTransform16fromAffineMatrixEffffff',
        scaleX, shearY, shearX, scaleY, translateX, translateY,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  @overload(float, float)
  def fromTranslate(translateX: float, translateY: float) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuickPlanarTransform::fromTranslate(float
    translateX, float translateY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#fromTranslate

    Parameters
    ----------

    translateX : float
      Passed on as it is.

    translateY : float
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuickPlanarTransform::fromTranslate(float translateX,
    #      float translateY)
    address = Rituals.call(
        'ritual_ZN21QQuickPlanarTransform13fromTranslateEff',
        translateX, translateY,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  @overload(float, float)
  @overload(float, float, float)
  @overload(float, float, float, float)
  def fromScale(
      scaleX: float,
      scaleY: float,
      originX: float = 0.0,
      originY: float = 0.0,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuickPlanarTransform::fromScale(float scaleX,
    float scaleY, float originX, float originY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#fromScale

    Parameters
    ----------

    scaleX : float
      Passed on as it is.

    scaleY : float
      Passed on as it is.

    originX : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    originY : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuickPlanarTransform::fromScale(float scaleX, float
    #      scaleY, float originX, float originY)
    address = Rituals.call(
        'ritual_ZN21QQuickPlanarTransform9fromScaleEffff',
        scaleX, scaleY, originX, originY,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  @overload(float)
  @overload(float, float)
  @overload(float, float, float)
  def fromRotate(
      angle: float,
      originX: float = 0.0,
      originY: float = 0.0,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuickPlanarTransform::fromRotate(float angle,
    float originX, float originY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#fromRotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    originX : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    originY : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuickPlanarTransform::fromRotate(float angle, float
    #      originX, float originY)
    address = Rituals.call(
        'ritual_ZN21QQuickPlanarTransform10fromRotateEfff',
        angle, originX, originY,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  @overload(float, float)
  @overload(float, float, float)
  @overload(float, float, float, float)
  def fromShear(
      shearX: float,
      shearY: float,
      originX: float = 0.0,
      originY: float = 0.0,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuickPlanarTransform::fromShear(float shearX,
    float shearY, float originX, float originY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#fromShear

    Parameters
    ----------

    shearX : float
      Passed on as it is.

    shearY : float
      Passed on as it is.

    originX : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    originY : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuickPlanarTransform::fromShear(float shearX, float
    #      shearY, float originX, float originY)
    address = Rituals.call(
        'ritual_ZN21QQuickPlanarTransform9fromShearEffff',
        shearX, shearY, originX, originY,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPlanarTransform'

  #  A C++ QQuickPlanarTransform Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPlanarTransform'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPlanarTransform::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPlanarTransform::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickPlanarTransform10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickPlanarTransform::QQuickPlanarTransform(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplanartransform.html#QQuickPlanarTransform

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPlanarTransform::QQuickPlanarTransform(QObject *parent)
    self._noteCreation(QQuickPlanarTransform, lambda: Rituals.call(
        'ritual_ZN21QQuickPlanarTransformC1EP7QObject',
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
