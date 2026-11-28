"""
Qt3DRender::RayCasting::QCollisionQueryResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::RayCasting::QCollisionQueryResult to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QVector3D


class QCollisionQueryResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::RayCasting::QCollisionQueryResult: a
  plain Python object standing in front of one C++
  Qt3DRender::RayCasting::QCollisionQueryResult.

  C++ hands a Qt3DRender::RayCasting::QCollisionQueryResult around as a copy,
  so every C++ Qt3DRender::RayCasting::QCollisionQueryResult behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::RayCasting::QCollisionQueryResult that
  has a ritual and that Python can call so far, 2 names in all: 'handle',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::RayCasting::QCollisionQueryResult::~QCollisionQueryResult(
    )': the destructor: Python removes its C++
    Qt3DRender::RayCasting::QCollisionQueryResult by it, and has no other use
    for it.
  - Qt's 'QCollisionQueryResult
    &Qt3DRender::RayCasting::QCollisionQueryResult::operator=(const
    QCollisionQueryResult &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCollisionQueryResult
    &Qt3DRender::RayCasting::QCollisionQueryResult::operator=(
    QCollisionQueryResult &&other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'void
    Qt3DRender::RayCasting::QCollisionQueryResult::swap(QCollisionQueryResult
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'const std::vector<Hit>
    &Qt3DRender::RayCasting::QCollisionQueryResult::hits() const': gives a
    type Python has no way to take yet.
  - Qt's 'std::vector<Qt3DCore::QNodeId>
    Qt3DRender::RayCasting::QCollisionQueryResult::entitiesHit() const':
    gives a type Python has no way to take yet.
  - Qt's
    'Qt3DRender::RayCasting::QCollisionQueryResult::QCollisionQueryResult(
    QCollisionQueryResultPrivate &p)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QCollisionQueryResultPrivate
    *Qt3DRender::RayCasting::QCollisionQueryResult::d_func() const': takes in
    Python what 'QCollisionQueryResultPrivate
    *Qt3DRender::RayCasting::QCollisionQueryResult::d_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::QCollisionQueryResult is created at the
    first use, not by 'Qt3DRender::RayCasting::QCollisionQueryResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::RayCasting::QCollisionQueryResult back
    gives a copy the ritual made for Python, in a new cute
    Qt3DRender::RayCasting::QCollisionQueryResult.
  - Each name of Qt's Qt3DRender::RayCasting::QCollisionQueryResult that has
    no cute function yet, 'entitiesHit', 'hits', 'swap', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside
  #  Qt3DRender::RayCasting::QCollisionQueryResult, each a class in here as
  #  in C++.

  class Hit(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DRender::RayCasting::QCollisionQueryResult::Hit:
    a plain Python object standing in front of one C++
    Qt3DRender::RayCasting::QCollisionQueryResult::Hit.

    C++ hands a Qt3DRender::RayCasting::QCollisionQueryResult::Hit around as
    a copy, so every C++ Qt3DRender::RayCasting::QCollisionQueryResult::Hit
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DRender::RayCasting::QCollisionQueryResult::Hit
    yet. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DRender::RayCasting::QCollisionQueryResult::Hit::~Hit()': the
      destructor: Python removes its C++
      Qt3DRender::RayCasting::QCollisionQueryResult::Hit by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Qt3DRender::RayCasting::QCollisionQueryResult::Hit is created
      at the first use, not by
      'Qt3DRender::RayCasting::QCollisionQueryResult::Hit(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DRender::RayCasting::QCollisionQueryResult::Hit
      back gives a copy the ritual made for Python, in a new cute
      Qt3DRender::RayCasting::QCollisionQueryResult::Hit.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVector3D = WAIT['QVector3D']

    #  The enums Qt writes inside
    #  Qt3DRender::RayCasting::QCollisionQueryResult::Hit, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class HitType(CuteNum):
      """
      The enum 'Qt3DRender::RayCasting::QCollisionQueryResult::Hit::HitType'
      of Qt, with the 4 names Qt gives in it.
      """

      Entity = Kee[int](0)
      Point = Kee[int](1)
      Edge = Kee[int](2)
      Triangle = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::RayCasting::QCollisionQueryResult::Hit'

    #  Qt's '~Qt3DRender::RayCasting::QCollisionQueryResult::Hit()'. Naming
    #  it makes this a value class: Python owns every C++
    #  Qt3DRender::RayCasting::QCollisionQueryResult::Hit behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult3HitD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DRender::RayCasting::QCollisionQueryResult::Hit::Hit()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresult-hit.html
      """
      #  Qt3DRender::RayCasting::QCollisionQueryResult::Hit::Hit()
      self._noteCreation(QCollisionQueryResult.Hit, lambda: Rituals.call(
          'ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult3HitC1Ev',
      ))

    @overload(WAIT['Qt3DCore.QNodeId'], QVector3D, float, QVector3D)
    def __init__(
        self,
        entity: Qt3DCore.QNodeId,
        intersection: QVector3D,
        distance: float,
        uvw: QVector3D,
    ) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DRender::RayCasting::QCollisionQueryResult::Hit::Hit(Qt3DCore::
      QNodeId entity, const Vector3D &intersection, float distance, const
      Vector3D &uvw)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresult-hit.html

      Parameters
      ----------

      entity : Qt3DCore.QNodeId
        Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
        Python's own.

      intersection : QVector3D
        Passed on as a value: Qt reads the C++ QVector3D, which stays
        Python's own.

      distance : float
        Passed on as it is.

      uvw : QVector3D
        Passed on as a value: Qt reads the C++ QVector3D, which stays
        Python's own.
      """
      #  Qt3DRender::RayCasting::QCollisionQueryResult::Hit::Hit(
      #      Qt3DCore::QNodeId entity, const Vector3D &intersection, float
      #      distance, const Vector3D &uvw)
      self._noteCreation(QCollisionQueryResult.Hit, lambda: Rituals.call(
          'ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult3HitC1EN'
          '8Qt3DCore7QNodeIdERK9QVector3DfS7_',
          self._valueOf(entity), self._valueOf(intersection), distance,
          self._valueOf(uvw),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::QCollisionQueryResult'

  #  Qt's '~Qt3DRender::RayCasting::QCollisionQueryResult()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DRender::RayCasting::QCollisionQueryResult behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def handle(self) -> int:
    """
    Calls Qt's 'QQueryHandle
    Qt3DRender::RayCasting::QCollisionQueryResult::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresult.html
    """
    #  QQueryHandle Qt3DRender::RayCasting::QCollisionQueryResult::handle()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting21QCollisionQueryResult6handleEv',
    )

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::RayCasting::QCollisionQueryResult::QCollisionQueryResult()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresult.html
    """
    #  Qt3DRender::RayCasting::QCollisionQueryResult::QCollisionQueryResult()
    self._noteCreation(QCollisionQueryResult, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QCollisionQueryResult) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::RayCasting::QCollisionQueryResult::QCollisionQueryResult(
    const QCollisionQueryResult &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresult.html

    Parameters
    ----------

    a0 : QCollisionQueryResult
      Passed on as a value: Qt reads the C++
      Qt3DRender::RayCasting::QCollisionQueryResult, which stays Python's
      own.
    """
    #  Qt3DRender::RayCasting::QCollisionQueryResult::
    #      QCollisionQueryResult(const QCollisionQueryResult &a0)
    self._noteCreation(QCollisionQueryResult, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultC1ERKS1_',
        self._valueOf(a0),
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

  def d_func(
      self,
  ) -> Optional[Qt3DRender.RayCasting.QCollisionQueryResultPrivate]:
    """
    Calls Qt's 'QCollisionQueryResultPrivate
    *Qt3DRender::RayCasting::QCollisionQueryResult::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresult.html

    Returns
    -------

    Optional[Qt3DRender.RayCasting.QCollisionQueryResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCollisionQueryResultPrivate
    #      *Qt3DRender::RayCasting::QCollisionQueryResult::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult6d_funcEv',
    )
    return Qt3DRender.RayCasting.QCollisionQueryResultPrivate._cuteAt(address)

  @staticmethod
  def entitiesHit(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QNodeId>
    Qt3DRender::RayCasting::QCollisionQueryResult::entitiesHit() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QCollisionQueryResult.entitiesHit' has no "
        "cute function yet. Qt's 'std::vector<Qt3DCore::QNodeId> "
        "Qt3DRender::RayCasting::QCollisionQueryResult::entitiesHit() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def hits(*__, **_) -> Never:
    """
    Qt's 'const std::vector<Hit>
    &Qt3DRender::RayCasting::QCollisionQueryResult::hits() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QCollisionQueryResult.hits' has no cute "
        "function yet. Qt's 'const std::vector<Hit> "
        "&Qt3DRender::RayCasting::QCollisionQueryResult::hits() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::RayCasting::QCollisionQueryResult::swap(QCollisionQueryResult
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QCollisionQueryResult.swap' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::RayCasting::QCollisionQueryResult::swap(QCollisionQuery"
        "Result &other)': takes a type Python has no way to hand over yet.")
