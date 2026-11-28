"""
Qt3DRender::RayCasting::QAbstractCollisionQueryService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qabstractcollisionqueryservice_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::RayCasting::QAbstractCollisionQueryService to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
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


class QAbstractCollisionQueryService(Qt3DCore.QAbstractServiceProvider):
  """
  The cute side of Qt's
  Qt3DRender::RayCasting::QAbstractCollisionQueryService: a plain Python
  object standing in front of one C++
  Qt3DRender::RayCasting::QAbstractCollisionQueryService.

  It is built on the cute 'Qt3DCore::QAbstractServiceProvider', as Qt's
  Qt3DRender::RayCasting::QAbstractCollisionQueryService is built on Qt's
  Qt3DCore::QAbstractServiceProvider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  Qt3DRender::RayCasting::QAbstractCollisionQueryService that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'query', 'fetchResult', 'd_func'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *Qt3DRender::RayCasting::QAbstractCollisionQueryService::qt_metacast(
    const char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QList<QCollisionQueryResult>
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::fetchAllResults()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::setResultHandle(
    QCollisionQueryResult &result, const QQueryHandle &handle)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::addEntityHit(
    QCollisionQueryResult &result, Qt3DCore::QNodeId entity, const Vector3D
    &intersection, float distance, const Vector3D &uvw)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QAbstractCollisionQueryServicePrivate
    *Qt3DRender::RayCasting::QAbstractCollisionQueryService::d_func() const':
    takes in Python what 'QAbstractCollisionQueryServicePrivate
    *Qt3DRender::RayCasting::QAbstractCollisionQueryService::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::QAbstractCollisionQueryService is created
    at the first use, not by
    'Qt3DRender::RayCasting::QAbstractCollisionQueryService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::RayCasting::QAbstractCollisionQueryService.
  - Qt tells when it has removed the C++
    Qt3DRender::RayCasting::QAbstractCollisionQueryService. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::RayCasting::QAbstractCollisionQueryService
    that has no cute function yet, '__init__', 'addEntityHit',
    'fetchAllResults', 'setResultHandle', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside
  #  Qt3DRender::RayCasting::QAbstractCollisionQueryService, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class QueryMode(CuteNum):
    """
    The enum
    'Qt3DRender::RayCasting::QAbstractCollisionQueryService::QueryMode' of
    Qt, with the 2 names Qt gives in it.
    """

    FirstHit = Kee[int](0)
    AllHits = Kee[int](1)

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
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qabstractcollisionqueryservice.html

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
    #  QString
    #      Qt3DRender::RayCasting::QAbstractCollisionQueryService::tr(const
    #      char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService2'
        'trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::QAbstractCollisionQueryService'

  #  The functions Qt calls itself that
  #  Qt3DRender::RayCasting::QAbstractCollisionQueryService is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'fetchAllResults': (
          'QList<QCollisionQueryResult> '
          'Qt3DRender::RayCasting::QAbstractCollisionQueryService::fetchAll'
          'Results() const',
      ),
  }

  #  The functions Qt calls itself that
  #  Qt3DRender::RayCasting::QAbstractCollisionQueryService is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'query': (
          ('_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService5que'
           'ryERKNS0_6QRay3DENS1_9QueryModeEPNS0_23QBoundingVolumeProviderE',
           ('int', 'number', ''),
           (
               ('address', 'value',
                'Qt3DRender:Qt3DRender.RayCasting.QRay3D'),
               ('int', 'enum',
                'Qt3DRender:Qt3DRender.RayCasting.QAbstractCollisionQueryService.QueryMode'),
               ('address', 'address',
                'Qt3DRender:Qt3DRender.RayCasting.QBoundingVolumeProvider'),
           )),
          ('_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService5que'
           'ryERKNS0_6QRay3DEPKNS0_15QBoundingVolumeE',
           ('address', 'value',
            'Qt3DRender:Qt3DRender.RayCasting.QCollisionQueryResult.Hit'),
           (
               ('address', 'value',
                'Qt3DRender:Qt3DRender.RayCasting.QRay3D'),
               ('address', 'address',
                'Qt3DRender:Qt3DRender.RayCasting.QBoundingVolume'),
           )),
      ),
      'fetchResult': (
          ('_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService11fe'
           'tchResultERKi',
           ('address', 'value',
            'Qt3DRender:Qt3DRender.RayCasting.QCollisionQueryResult'),
           (
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
    Calls Qt's 'const QMetaObject
    *Qt3DRender::RayCasting::QAbstractCollisionQueryService::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qabstractcollisionqueryservice.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DRender::RayCasting::QAbstractCollisionQueryService::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting30QAbstractCollisionQueryService'
        '10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'Qt3DRender::RayCasting::QAbstractCollisionQueryService::
      QAbstractCollisionQueryService(const QString &description)': the class
      is abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    - Qt's 'Qt3DRender::RayCasting::QAbstractCollisionQueryService::
      QAbstractCollisionQueryService(QAbstractCollisionQueryServicePrivate
      &dd)': the class is abstract, so C++ cannot make one, and the C++ class
      of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QAbstractCollisionQueryService.__init__' "
        "has no cute function yet. Qt's "
        "'Qt3DRender::RayCasting::QAbstractCollisionQueryService::QAbstractC"
        "ollisionQueryService(const QString &description)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open. Qt's "
        "'Qt3DRender::RayCasting::QAbstractCollisionQueryService::QAbstractC"
        "ollisionQueryService(QAbstractCollisionQueryServicePrivate &dd)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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

  @overload(
      WAIT['Qt3DRender.RayCasting.QRay3D'], QueryMode,
      WAIT['Qt3DRender.RayCasting.QBoundingVolumeProvider'],
  )
  @overload(WAIT['Qt3DRender.RayCasting.QRay3D'], QueryMode, NoneType)
  def query(
      self,
      ray: Qt3DRender.RayCasting.QRay3D,
      mode: QueryMode,
      provider: Optional[Qt3DRender.RayCasting.QBoundingVolumeProvider],
  ) -> int:
    """
    Calls Qt's 'QQueryHandle
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::query(const
    QRay3D &ray, QueryMode mode, QBoundingVolumeProvider *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qabstractcollisionqueryservice.html

    Parameters
    ----------

    ray : Qt3DRender.RayCasting.QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.

    mode : QueryMode
      Passed on as its number.

    provider : Optional[Qt3DRender.RayCasting.QBoundingVolumeProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQueryHandle
    #      Qt3DRender::RayCasting::QAbstractCollisionQueryService::query(
    #      const QRay3D &ray, QueryMode mode, QBoundingVolumeProvider
    #      *provider)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService5'
        'queryERKNS0_6QRay3DENS1_9QueryModeEPNS0_23QBoundingVolumeProviderE',
        self._valueOf(ray), mode.value, self._addressOf(provider),
    )

  @overload(
      WAIT['Qt3DRender.RayCasting.QRay3D'],
      WAIT['Qt3DRender.RayCasting.QBoundingVolume'],
  )
  @overload(WAIT['Qt3DRender.RayCasting.QRay3D'], NoneType)
  def query(
      self,
      ray: Qt3DRender.RayCasting.QRay3D,
      volume: Optional[Qt3DRender.RayCasting.QBoundingVolume],
  ) -> Qt3DRender.RayCasting.QCollisionQueryResult.Hit:
    """
    Calls Qt's 'QCollisionQueryResult::Hit
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::query(const
    QRay3D &ray, const QBoundingVolume *volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qabstractcollisionqueryservice.html

    Parameters
    ----------

    ray : Qt3DRender.RayCasting.QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.

    volume : Optional[Qt3DRender.RayCasting.QBoundingVolume]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt3DRender.RayCasting.QCollisionQueryResult.Hit
      A new cute Qt3DRender::RayCasting::QCollisionQueryResult::Hit around
      the copy Qt gave back. Python owns it.
    """
    #  QCollisionQueryResult::Hit
    #      Qt3DRender::RayCasting::QAbstractCollisionQueryService::query(
    #      const QRay3D &ray, const QBoundingVolume *volume)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService5'
        'queryERKNS0_6QRay3DEPKNS0_15QBoundingVolumeE',
        self._valueOf(ray), self._addressOf(volume),
    )
    return Qt3DRender.RayCasting.QCollisionQueryResult.Hit._cuteOwning(address)

  @overload(int)
  def fetchResult(
      self,
      handle: int,
  ) -> Qt3DRender.RayCasting.QCollisionQueryResult:
    """
    Calls Qt's 'QCollisionQueryResult
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::fetchResult(const
    QQueryHandle &handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qabstractcollisionqueryservice.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    Returns
    -------

    Qt3DRender.RayCasting.QCollisionQueryResult
      A new cute Qt3DRender::RayCasting::QCollisionQueryResult around the
      copy Qt gave back. Python owns it.
    """
    #  QCollisionQueryResult
    #      Qt3DRender::RayCasting::QAbstractCollisionQueryService::
    #      fetchResult(const QQueryHandle &handle)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService1'
        '1fetchResultERKi',
        handle,
    )
    return Qt3DRender.RayCasting.QCollisionQueryResult._cuteOwning(address)

  def d_func(
      self,
  ) -> Optional[Qt3DRender.RayCasting.QAbstractCollisionQueryServicePrivate]:
    """
    Calls Qt's 'QAbstractCollisionQueryServicePrivate
    *Qt3DRender::RayCasting::QAbstractCollisionQueryService::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qabstractcollisionqueryservice.html

    Returns
    -------

    Optional[Qt3DRender.RayCasting.QAbstractCollisionQueryServicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractCollisionQueryServicePrivate
    #      *Qt3DRender::RayCasting::QAbstractCollisionQueryService::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService6'
        'd_funcEv',
    )
    return Qt3DRender.RayCasting.QAbstractCollisionQueryServicePrivate._cuteAt(address)

  @staticmethod
  def addEntityHit(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::addEntityHit(
    QCollisionQueryResult &result, Qt3DCore::QNodeId entity, const Vector3D
    &intersection, float distance, const Vector3D &uvw)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QAbstractCollisionQueryService.addEntityHit'"
        " has no cute function yet. Qt's 'void "
        "Qt3DRender::RayCasting::QAbstractCollisionQueryService::addEntityHi"
        "t(QCollisionQueryResult &result, Qt3DCore::QNodeId entity, const "
        "Vector3D &intersection, float distance, const Vector3D &uvw)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def fetchAllResults(*__, **_) -> Never:
    """
    Qt's 'QList<QCollisionQueryResult>
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::fetchAllResults()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QAbstractCollisionQueryService.fetchAllResul"
        "ts' has no cute function yet. Qt's 'QList<QCollisionQueryResult> "
        "Qt3DRender::RayCasting::QAbstractCollisionQueryService::fetchAllRes"
        "ults() const': gives a type Python has no way to take yet.")

  @staticmethod
  def setResultHandle(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::setResultHandle(
    QCollisionQueryResult &result, const QQueryHandle &handle)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QAbstractCollisionQueryService.setResultHand"
        "le' has no cute function yet. Qt's 'void "
        "Qt3DRender::RayCasting::QAbstractCollisionQueryService::setResultHa"
        "ndle(QCollisionQueryResult &result, const QQueryHandle &handle)': "
        "takes a type Python has no way to hand over yet.")
