"""
Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/quick3dlevelofdetailloader_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl, QVariant
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Quick3DLevelOfDetailLoader(Qt3DCore.QEntity):
  """
  The cute side of Qt's
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader: a plain Python
  object standing in front of one C++
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader.

  It is built on the cute 'Qt3DCore::QEntity', as Qt's
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader is built on Qt's
  Qt3DCore::QEntity, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader that has a ritual and
  that Python can call so far, 24 names in all: 'metaObject', 'tr',
  'sources', 'setSources', 'camera', 'setCamera', 'currentIndex',
  'setCurrentIndex', 'thresholdType', 'setThresholdType', 'volumeOverride',
  'setVolumeOverride', 'createBoundingSphere', 'entity', 'source',
  'sourcesChanged', 'cameraChanged', 'currentIndexChanged',
  'thresholdTypeChanged', 'thresholdsChanged', 'volumeOverrideChanged',
  'entityChanged', 'sourceChanged', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QList<qreal>
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholds()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setThresholds(
    const QList<qreal> &thresholds)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const Quick3DLevelOfDetailLoaderPrivate
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::d_func() const':
    takes in Python what 'Quick3DLevelOfDetailLoaderPrivate
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader is created
    at the first use, not by
    'Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader.
  - Qt tells when it has removed the C++
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader
    that has no cute function yet, 'setThresholds', 'thresholds', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

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
    #      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::tr(const
    #      char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader2trE'
        'PKcS4_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader'

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
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader10m'
        'etaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sources(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::sources() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList
    #      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::sources()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader7so'
        'urcesEv',
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def camera(self) -> Optional[Qt3DRender.QCamera]:
    """
    Calls Qt's 'Qt3DRender::QCamera
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::camera() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    Optional[Qt3DRender.QCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QCamera
    #      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::camera()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6ca'
        'meraEv',
    )
    return Qt3DRender.QCamera._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::currentIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  int Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      currentIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader12c'
        'urrentIndexEv',
    )

  def thresholdType(self) -> Qt3DRender.QLevelOfDetail.ThresholdType:
    """
    Calls Qt's 'Qt3DRender::QLevelOfDetail::ThresholdType
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholdType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    Qt3DRender.QLevelOfDetail.ThresholdType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QLevelOfDetail.ThresholdType(number)' gives.
    """
    #  Qt3DRender::QLevelOfDetail::ThresholdType
    #      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      thresholdType() const
    return Qt3DRender.QLevelOfDetail.ThresholdType(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13t'
        'hresholdTypeEv',
    ))

  def volumeOverride(self) -> Qt3DRender.QLevelOfDetailBoundingSphere:
    """
    Calls Qt's 'Qt3DRender::QLevelOfDetailBoundingSphere
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::volumeOverride()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    Qt3DRender.QLevelOfDetailBoundingSphere
      A new cute Qt3DRender::QLevelOfDetailBoundingSphere around the copy Qt
      gave back. Python owns it.
    """
    #  Qt3DRender::QLevelOfDetailBoundingSphere
    #      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      volumeOverride() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader14v'
        'olumeOverrideEv',
    )
    return Qt3DRender.QLevelOfDetailBoundingSphere._cuteOwning(address)

  def entity(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::entity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject
    #      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::entity()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6en'
        'tityEv',
    )
    return QObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::source()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6so'
        'urceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QVariant])
  def setSources(self, sources: QList[QVariant]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setSources(const
    QVariantList &sources)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Parameters
    ----------

    sources : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void
    #      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setSources(
    #      const QVariantList &sources)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader10se'
        'tSourcesERK5QListI8QVariantE',
        self._valueOf(sources),
    )

  @overload(WAIT['Qt3DRender.QCamera'])
  @overload(NoneType)
  def setCamera(self, camera: Optional[Qt3DRender.QCamera]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setCamera(
    Qt3DRender::QCamera *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Parameters
    ----------

    camera : Optional[Qt3DRender.QCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setCamera(
    #      Qt3DRender::QCamera *camera)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader9set'
        'CameraEPN10Qt3DRender7QCameraE',
        self._addressOf(camera),
    )

  @overload(int)
  def setCurrentIndex(self, currentIndex: int) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setCurrentIndex(
    int currentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      setCurrentIndex(int currentIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader15se'
        'tCurrentIndexEi',
        currentIndex,
    )

  @overload(Qt3DRender.QLevelOfDetail.ThresholdType)
  def setThresholdType(
      self,
      thresholdType: Qt3DRender.QLevelOfDetail.ThresholdType,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setThresholdType(
    Qt3DRender::QLevelOfDetail::ThresholdType thresholdType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Parameters
    ----------

    thresholdType : Qt3DRender.QLevelOfDetail.ThresholdType
      Passed on as its number.
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      setThresholdType(Qt3DRender::QLevelOfDetail::ThresholdType
    #      thresholdType)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader16se'
        'tThresholdTypeEN10Qt3DRender14QLevelOfDetail13ThresholdTypeE',
        thresholdType.value,
    )

  @overload(WAIT['Qt3DRender.QLevelOfDetailBoundingSphere'])
  def setVolumeOverride(
      self,
      volumeOverride: Qt3DRender.QLevelOfDetailBoundingSphere,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setVolumeOverride(
    const Qt3DRender::QLevelOfDetailBoundingSphere &volumeOverride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Parameters
    ----------

    volumeOverride : Qt3DRender.QLevelOfDetailBoundingSphere
      Passed on as a value: Qt reads the C++
      Qt3DRender::QLevelOfDetailBoundingSphere, which stays Python's own.
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      setVolumeOverride(const Qt3DRender::QLevelOfDetailBoundingSphere
    #      &volumeOverride)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader17se'
        'tVolumeOverrideERKN10Qt3DRender28QLevelOfDetailBoundingSphereE',
        self._valueOf(volumeOverride),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    Quick3DLevelOfDetailLoader(QNode *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      Quick3DLevelOfDetailLoader(QNode *parent)
    self._noteCreation(Quick3DLevelOfDetailLoader, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoaderC1EP'
        'N8Qt3DCore5QNodeE',
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

  @overload(QVector3D, float)
  def createBoundingSphere(
      self,
      center: QVector3D,
      radius: float,
  ) -> Qt3DRender.QLevelOfDetailBoundingSphere:
    """
    Calls Qt's 'Qt3DRender::QLevelOfDetailBoundingSphere
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    createBoundingSphere(const QVector3D &center, float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Parameters
    ----------

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.

    Returns
    -------

    Qt3DRender.QLevelOfDetailBoundingSphere
      A new cute Qt3DRender::QLevelOfDetailBoundingSphere around the copy Qt
      gave back. Python owns it.
    """
    #  Qt3DRender::QLevelOfDetailBoundingSphere
    #      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      createBoundingSphere(const QVector3D &center, float radius)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader20cr'
        'eateBoundingSphereERK9QVector3Df',
        self._valueOf(center), radius,
    )
    return Qt3DRender.QLevelOfDetailBoundingSphere._cuteOwning(address)

  def sourcesChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::sourcesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      sourcesChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader14so'
        'urcesChangedEv',
    )

  def cameraChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::cameraChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      cameraChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13ca'
        'meraChangedEv',
    )

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      currentIndexChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader19cu'
        'rrentIndexChangedEv',
    )

  def thresholdTypeChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    thresholdTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      thresholdTypeChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader20th'
        'resholdTypeChangedEv',
    )

  def thresholdsChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholdsChanged(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      thresholdsChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader17th'
        'resholdsChangedEv',
    )

  def volumeOverrideChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    volumeOverrideChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      volumeOverrideChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader21vo'
        'lumeOverrideChangedEv',
    )

  def entityChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::entityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      entityChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13en'
        'tityChangedEv',
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html
    """
    #  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::
    #      sourceChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13so'
        'urceChangedEv',
    )

  def d_func(
      self,
  ) -> Optional[Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoaderPrivate]:
    """
    Calls Qt's 'Quick3DLevelOfDetailLoaderPrivate
    *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-extras-quick-quick3dlevelofdetailloader.html

    Returns
    -------

    Optional[Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Quick3DLevelOfDetailLoaderPrivate
    #      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6d_f'
        'uncEv',
    )
    return Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoaderPrivate._cuteAt(address)

  @staticmethod
  def setThresholds(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setThresholds(
    const QList<qreal> &thresholds)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoader.setThresholds' "
        "has no cute function yet. Qt's 'void "
        "Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setThreshold"
        "s(const QList<qreal> &thresholds)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def thresholds(*__, **_) -> Never:
    """
    Qt's 'QList<qreal>
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholds()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DExtras.Extras.Quick.Quick3DLevelOfDetailLoader.thresholds' "
        "has no cute function yet. Qt's 'QList<qreal> "
        "Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholds()"
        " const': gives a type Python has no way to take yet.")
