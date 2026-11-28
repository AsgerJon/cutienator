"""
Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/quick3dvertexblendanimation_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DAnimation import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DVertexBlendAnimation(QObject):
  """
  The cute side of Qt's Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation: a
  plain Python object standing in front of one C++
  Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation.

  It is built on the cute 'QObject', as Qt's
  Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation
  that has a ritual and that Python can call so far, 3 names in all:
  'metaObject', 'tr', 'parentVertexBlendAnimation'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QQmlListProperty<Qt3DAnimation::QMorphTarget>
    Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::morphTargets()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation is created at
    the first use, not by
    'Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation.
  - Qt tells when it has removed the C++
    Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation that
    has no cute function yet, 'morphTargets', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString
    Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-quick-qquick3dvertexblendanimation.html

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
    #  QString Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::tr(const
    #      char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation5Quick28QQuick3DVertexBlendAnimation2trEPK'
        'cS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation'

  #  A C++ Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation Python makes is
  #  of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_Quick_QQuick3DVertexBlendAnimation'

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
    *Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-quick-qquick3dvertexblendanimation.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation5Quick28QQuick3DVertexBlendAnimation10met'
        'aObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def parentVertexBlendAnimation(
      self,
  ) -> Optional[Qt3DAnimation.QVertexBlendAnimation]:
    """
    Calls Qt's 'QVertexBlendAnimation
    *Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::
    parentVertexBlendAnimation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-quick-qquick3dvertexblendanimation.html

    Returns
    -------

    Optional[Qt3DAnimation.QVertexBlendAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVertexBlendAnimation
    #      *Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::
    #      parentVertexBlendAnimation() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation5Quick28QQuick3DVertexBlendAnimation26par'
        'entVertexBlendAnimationEv',
    )
    return Qt3DAnimation.QVertexBlendAnimation._cuteAt(address)

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
    'Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::
    QQuick3DVertexBlendAnimation(QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-quick-qquick3dvertexblendanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::
    #      QQuick3DVertexBlendAnimation(QObject *parent)
    self._noteCreation(QQuick3DVertexBlendAnimation, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation5Quick28QQuick3DVertexBlendAnimationC1EP7Q'
        'Object',
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

  @staticmethod
  def morphTargets(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<Qt3DAnimation::QMorphTarget>
    Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::morphTargets()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Quick.QQuick3DVertexBlendAnimation.morphTargets' "
        "has no cute function yet. Qt's "
        "'QQmlListProperty<Qt3DAnimation::QMorphTarget> "
        "Qt3DAnimation::Quick::QQuick3DVertexBlendAnimation::morphTargets()'"
        ": gives a type Python has no way to take yet.")
