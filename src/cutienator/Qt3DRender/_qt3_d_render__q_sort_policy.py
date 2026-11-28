"""
Qt3DRender::QSortPolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qsortpolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSortPolicy(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QSortPolicy: a plain Python object
  standing in front of one C++ Qt3DRender::QSortPolicy.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QSortPolicy is built on Qt's Qt3DRender::QFrameGraphNode, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSortPolicy that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'tr', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QSortPolicy::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QSortPolicy::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QSortPolicy::~QSortPolicy()': the destructor: Python
    never removes a C++ Qt3DRender::QSortPolicy.
  - Qt's 'QList<SortType> Qt3DRender::QSortPolicy::sortTypes() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<int> Qt3DRender::QSortPolicy::sortTypesInt() const': gives a
    type Python has no way to take yet.
  - Qt's 'void Qt3DRender::QSortPolicy::setSortTypes(const QList<SortType>
    &sortTypes)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DRender::QSortPolicy::setSortTypes(const QList<int>
    &sortTypesInt)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DRender::QSortPolicy::sortTypesChanged(const
    QList<SortType> &sortTypes)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void Qt3DRender::QSortPolicy::sortTypesChanged(const QList<int>
    &sortTypes)': takes a type Python has no way to hand over yet.
  - Qt's 'Qt3DRender::QSortPolicy::QSortPolicy(QSortPolicyPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QSortPolicyPrivate *Qt3DRender::QSortPolicy::d_func() const':
    takes in Python what 'QSortPolicyPrivate
    *Qt3DRender::QSortPolicy::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QSortPolicy is created at the first use, not by
    'Qt3DRender::QSortPolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSortPolicy.
  - Qt tells when it has removed the C++ Qt3DRender::QSortPolicy. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QSortPolicy that has no cute function yet,
    'setSortTypes', 'sortTypes', 'sortTypesChanged', 'sortTypesInt', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QSortPolicy, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class SortType(CuteNum):
    """
    The enum 'Qt3DRender::QSortPolicy::SortType' of Qt, with the 6 names Qt
    gives in it.
    """

    StateChangeCost = Kee[int](1)
    BackToFront = Kee[int](2)
    Material = Kee[int](4)
    FrontToBack = Kee[int](8)
    Texture = Kee[int](16)
    Uniform = Kee[int](32)

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
    Calls Qt's 'QString Qt3DRender::QSortPolicy::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsortpolicy.html#tr

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
    #  QString Qt3DRender::QSortPolicy::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender11QSortPolicy2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSortPolicy'

  #  A C++ Qt3DRender::QSortPolicy Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSortPolicy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QSortPolicy::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsortpolicy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QSortPolicy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QSortPolicy10metaObjectEv',
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QSortPolicy::QSortPolicy(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsortpolicy.html#QSortPolicy

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QSortPolicy::QSortPolicy(Qt3DCore::QNode *parent)
    self._noteCreation(QSortPolicy, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender11QSortPolicyC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  def d_func(self) -> Optional[Qt3DRender.QSortPolicyPrivate]:
    """
    Calls Qt's 'QSortPolicyPrivate *Qt3DRender::QSortPolicy::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsortpolicy.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QSortPolicyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSortPolicyPrivate *Qt3DRender::QSortPolicy::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender11QSortPolicy6d_funcEv',
    )
    return Qt3DRender.QSortPolicyPrivate._cuteAt(address)

  @staticmethod
  def setSortTypes(*__, **_) -> Never:
    """
    - Qt's 'void Qt3DRender::QSortPolicy::setSortTypes(const QList<SortType>
      &sortTypes)': takes a type Python has no way to hand over yet.
    - Qt's 'void Qt3DRender::QSortPolicy::setSortTypes(const QList<int>
      &sortTypesInt)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QSortPolicy.setSortTypes' has no cute function yet. "
        "Qt's 'void Qt3DRender::QSortPolicy::setSortTypes(const "
        "QList<SortType> &sortTypes)': takes a type Python has no way to "
        "hand over yet. Qt's 'void "
        "Qt3DRender::QSortPolicy::setSortTypes(const QList<int> "
        "&sortTypesInt)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def sortTypes(*__, **_) -> Never:
    """
    Qt's 'QList<SortType> Qt3DRender::QSortPolicy::sortTypes() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QSortPolicy.sortTypes' has no cute function yet. Qt's "
        "'QList<SortType> Qt3DRender::QSortPolicy::sortTypes() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def sortTypesChanged(*__, **_) -> Never:
    """
    - Qt's 'void Qt3DRender::QSortPolicy::sortTypesChanged(const
      QList<SortType> &sortTypes)': takes a type Python has no way to hand
      over yet.
    - Qt's 'void Qt3DRender::QSortPolicy::sortTypesChanged(const QList<int>
      &sortTypes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QSortPolicy.sortTypesChanged' has no cute function "
        "yet. Qt's 'void Qt3DRender::QSortPolicy::sortTypesChanged(const "
        "QList<SortType> &sortTypes)': takes a type Python has no way to "
        "hand over yet. Qt's 'void "
        "Qt3DRender::QSortPolicy::sortTypesChanged(const QList<int> "
        "&sortTypes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def sortTypesInt(*__, **_) -> Never:
    """
    Qt's 'QList<int> Qt3DRender::QSortPolicy::sortTypesInt() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QSortPolicy.sortTypesInt' has no cute function yet. "
        "Qt's 'QList<int> Qt3DRender::QSortPolicy::sortTypesInt() const': "
        "gives a type Python has no way to take yet.")
