"""
Qt3DAnimation::QMorphTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qmorphtarget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMorphTarget(QObject):
  """
  The cute side of Qt's Qt3DAnimation::QMorphTarget: a plain Python object
  standing in front of one C++ Qt3DAnimation::QMorphTarget.

  It is built on the cute 'QObject', as Qt's Qt3DAnimation::QMorphTarget is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QMorphTarget that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'attributeNames', 'addAttribute', 'removeAttribute', 'fromGeometry',
  'attributeNamesChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QMorphTarget::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DAnimation::QMorphTarget::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<Qt3DCore::QAttribute *>
    Qt3DAnimation::QMorphTarget::attributeList() const': gives a type Python
    has no way to take yet.
  - Qt's 'void Qt3DAnimation::QMorphTarget::setAttributes(const
    QList<Qt3DCore::QAttribute *> &attributes)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QMorphTargetPrivate *Qt3DAnimation::QMorphTarget::d_func()
    const': takes in Python what 'QMorphTargetPrivate
    *Qt3DAnimation::QMorphTarget::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QMorphTarget is created at the first use, not by
    'Qt3DAnimation::QMorphTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QMorphTarget.
  - Qt tells when it has removed the C++ Qt3DAnimation::QMorphTarget. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QMorphTarget that has no cute function
    yet, 'attributeList', 'setAttributes', holds a function that raises
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
    Calls Qt's 'QString Qt3DAnimation::QMorphTarget::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#tr

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
    #  QString Qt3DAnimation::QMorphTarget::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation12QMorphTarget2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(WAIT['Qt3DCore.QGeometry'], QStringList)
  @overload(NoneType, QStringList)
  def fromGeometry(
      geometry: Optional[Qt3DCore.QGeometry],
      attributes: QStringList,
  ) -> Optional[QMorphTarget]:
    """
    Calls Qt's 'QMorphTarget
    *Qt3DAnimation::QMorphTarget::fromGeometry(Qt3DCore::QGeometry *geometry,
    const QStringList &attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#fromGeometry

    Parameters
    ----------

    geometry : Optional[Qt3DCore.QGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attributes : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QMorphTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMorphTarget
    #      *Qt3DAnimation::QMorphTarget::fromGeometry(Qt3DCore::QGeometry
    #      *geometry, const QStringList &attributes)
    address = Rituals.call(
        'ritual_ZN13Qt3DAnimation12QMorphTarget12fromGeometryEPN8Qt3DCore9Q'
        'GeometryERK5QListI7QStringE',
        CuteMixin._addressOf(geometry), CuteMixin._valueOf(attributes),
    )
    return QMorphTarget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QMorphTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DAnimation::QMorphTarget::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QMorphTarget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation12QMorphTarget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def attributeNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DAnimation::QMorphTarget::attributeNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#attributeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DAnimation::QMorphTarget::attributeNames() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation12QMorphTarget14attributeNamesEv',
    )
    return QStringList._cuteOwning(address)

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
    'Qt3DAnimation::QMorphTarget::QMorphTarget(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#QMorphTarget

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QMorphTarget::QMorphTarget(QObject *parent)
    self._noteCreation(QMorphTarget, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation12QMorphTargetC1EP7QObject',
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

  @overload(WAIT['Qt3DCore.QAttribute'])
  @overload(NoneType)
  def addAttribute(self, attribute: Optional[Qt3DCore.QAttribute]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphTarget::addAttribute(Qt3DCore::QAttribute
    *attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#addAttribute

    Parameters
    ----------

    attribute : Optional[Qt3DCore.QAttribute]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QMorphTarget::addAttribute(Qt3DCore::QAttribute
    #      *attribute)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation12QMorphTarget12addAttributeEPN8Qt3DCore10'
        'QAttributeE',
        self._addressOf(attribute),
    )

  @overload(WAIT['Qt3DCore.QAttribute'])
  @overload(NoneType)
  def removeAttribute(
      self,
      attribute: Optional[Qt3DCore.QAttribute],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphTarget::removeAttribute(Qt3DCore::QAttribute
    *attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#removeAttribute

    Parameters
    ----------

    attribute : Optional[Qt3DCore.QAttribute]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QMorphTarget::removeAttribute(Qt3DCore::QAttribute
    #      *attribute)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation12QMorphTarget15removeAttributeEPN8Qt3DCor'
        'e10QAttributeE',
        self._addressOf(attribute),
    )

  @overload(QStringList)
  def attributeNamesChanged(self, attributeNames: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QMorphTarget::attributeNamesChanged(const
    QStringList &attributeNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html

    Parameters
    ----------

    attributeNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DAnimation::QMorphTarget::attributeNamesChanged(const
    #      QStringList &attributeNames)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation12QMorphTarget21attributeNamesChangedERK5Q'
        'ListI7QStringE',
        self._valueOf(attributeNames),
    )

  def d_func(self) -> Optional[Qt3DAnimation.QMorphTargetPrivate]:
    """
    Calls Qt's 'QMorphTargetPrivate *Qt3DAnimation::QMorphTarget::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtarget.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QMorphTargetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMorphTargetPrivate *Qt3DAnimation::QMorphTarget::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation12QMorphTarget6d_funcEv',
    )
    return Qt3DAnimation.QMorphTargetPrivate._cuteAt(address)

  @staticmethod
  def attributeList(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QAttribute *>
    Qt3DAnimation::QMorphTarget::attributeList() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphTarget.attributeList' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QAttribute *> "
        "Qt3DAnimation::QMorphTarget::attributeList() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setAttributes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QMorphTarget::setAttributes(const
    QList<Qt3DCore::QAttribute *> &attributes)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphTarget.setAttributes' has no cute function "
        "yet. Qt's 'void Qt3DAnimation::QMorphTarget::setAttributes(const "
        "QList<Qt3DCore::QAttribute *> &attributes)': takes a type Python "
        "has no way to hand over yet.")
