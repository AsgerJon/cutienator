"""
QSGGradientCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGGradientCache to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhi
  from . import QSGGradientCacheKey, QSGPlainTexture, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']
  QSGGradientCacheKey = WAIT['QSGGradientCacheKey']
  QSGPlainTexture = WAIT['QSGPlainTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGGradientCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGGradientCache: a plain Python object standing in
  front of one C++ QSGGradientCache.

  What exists
  -----------

  Every function of Qt's QSGGradientCache that has a ritual and that Python
  can call so far, 3 names in all: 'cacheForRhi', 'get', 'setTextureData'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGGradientCache::~QSGGradientCache()': the destructor: Python
    never removes a C++ QSGGradientCache.

  What to expect
  --------------

  - The C++ QSGGradientCache is created at the first use, not by
    'QSGGradientCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGGradientCache.
  """

  #  The classes Qt writes inside QSGGradientCache, each a class in here as
  #  in C++.

  class GradientDesc(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGGradientCache::GradientDesc: a plain Python
    object standing in front of one C++ QSGGradientCache::GradientDesc.

    C++ hands a QSGGradientCache::GradientDesc around as a copy, so every C++
    QSGGradientCache::GradientDesc behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSGGradientCache::GradientDesc that has a ritual
    and that Python can call so far, 1 name in all: 'compare'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGGradientCache::GradientDesc::~GradientDesc()': the destructor:
      Python removes its C++ QSGGradientCache::GradientDesc by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSGGradientCache::GradientDesc is created at the first use, not
      by 'QSGGradientCache::GradientDesc(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGGradientCache::GradientDesc back gives a copy
      the ritual made for Python, in a new cute
      QSGGradientCache::GradientDesc.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGGradientCache::GradientDesc'

    #  Qt's '~QSGGradientCache::GradientDesc()'. Naming it makes this a value
    #  class: Python owns every C++ QSGGradientCache::GradientDesc behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSGGradientCache12GradientDescD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def compare(self, other: QSGGradientCache.GradientDesc) -> int:
      """
      Calls Qt's 'int QSGGradientCache::GradientDesc::compare(const
      GradientDesc &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsggradientcache-gradientdesc.html#compare

      Parameters
      ----------

      other : QSGGradientCache.GradientDesc
        Passed on as a value: Qt reads the C++
        QSGGradientCache::GradientDesc, which stays Python's own.
      """
      #  int QSGGradientCache::GradientDesc::compare(const GradientDesc
      #      &other) const
      return self.uglySide.call(
          'ritual_ZNK16QSGGradientCache12GradientDesc7compareERKS0_',
          self._valueOf(other),
      )

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

  @staticmethod
  @overload(QRhi)
  @overload(NoneType)
  def cacheForRhi(rhi: Optional[QRhi]) -> Optional[QSGGradientCache]:
    """
    Calls Qt's 'QSGGradientCache *QSGGradientCache::cacheForRhi(QRhi *rhi)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggradientcache.html#cacheForRhi

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGGradientCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGradientCache *QSGGradientCache::cacheForRhi(QRhi *rhi)
    address = Rituals.call(
        'ritual_ZN16QSGGradientCache11cacheForRhiEP4QRhi',
        CuteMixin._addressOf(rhi),
    )
    return QSGGradientCache._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGGradientCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGPlainTexture, QSGGradientCacheKey)
  @overload(NoneType, QSGGradientCacheKey)
  def setTextureData(
      self,
      tx: Optional[QSGPlainTexture],
      grad: QSGGradientCacheKey,
  ) -> None:
    """
    Calls Qt's 'void QSGGradientCache::setTextureData(QSGPlainTexture *tx,
    const QSGGradientCacheKey &grad)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggradientcache.html#setTextureData

    Parameters
    ----------

    tx : Optional[QSGPlainTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    grad : QSGGradientCacheKey
      Passed on as a value: Qt reads the C++ QSGGradientCacheKey, which stays
      Python's own.
    """
    #  void QSGGradientCache::setTextureData(QSGPlainTexture *tx, const
    #      QSGGradientCacheKey &grad)
    self.uglySide.call(
        'ritual_ZN16QSGGradientCache14setTextureDataEP15QSGPlainTextureRK19'
        'QSGGradientCacheKey',
        self._addressOf(tx), self._valueOf(grad),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSGGradientCache::QSGGradientCache()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggradientcache.html#QSGGradientCache
    """
    #  QSGGradientCache::QSGGradientCache()
    self._noteCreation(QSGGradientCache, lambda: Rituals.call(
        'ritual_ZN16QSGGradientCacheC1Ev',
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

  @overload(QSGGradientCacheKey)
  def get(self, grad: QSGGradientCacheKey) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGGradientCache::get(const QSGGradientCacheKey
    &grad)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggradientcache.html#get

    Parameters
    ----------

    grad : QSGGradientCacheKey
      Passed on as a value: Qt reads the C++ QSGGradientCacheKey, which stays
      Python's own.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGGradientCache::get(const QSGGradientCacheKey &grad)
    address = self.uglySide.call(
        'ritual_ZN16QSGGradientCache3getERK19QSGGradientCacheKey',
        self._valueOf(grad),
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)
