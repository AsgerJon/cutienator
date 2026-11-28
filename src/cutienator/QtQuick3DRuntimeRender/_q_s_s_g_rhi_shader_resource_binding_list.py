"""
QSSGRhiShaderResourceBindingList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiShaderResourceBindingList to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QRhiShaderResourceBinding

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhiBuffer, QRhiSampler, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiBuffer = WAIT['QRhiBuffer']
  QRhiSampler = WAIT['QRhiSampler']
  QRhiTexture = WAIT['QRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiShaderResourceBindingList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiShaderResourceBindingList: a plain Python
  object standing in front of one C++ QSSGRhiShaderResourceBindingList.

  C++ hands a QSSGRhiShaderResourceBindingList around as a copy, so every C++
  QSSGRhiShaderResourceBindingList behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiShaderResourceBindingList that has a ritual
  and that Python can call so far, 7 names in all: 'clear',
  'addUniformBuffer', 'addTexture', 'addImageLoad', 'addImageStore',
  'addImageLoadStore', 'addStorageBuffer'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiShaderResourceBindingList
    &QSSGRhiShaderResourceBindingList::operator=(const
    QSSGRhiShaderResourceBindingList &other)': assignment: Python binds a
    name and has no operator for it.
  - Qt's
    'QSSGRhiShaderResourceBindingList::~QSSGRhiShaderResourceBindingList()':
    the destructor: Python removes its C++ QSSGRhiShaderResourceBindingList
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRhiShaderResourceBindingList is created at the first use, not
    by 'QSSGRhiShaderResourceBindingList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiShaderResourceBindingList back gives a copy
    the ritual made for Python, in a new cute
    QSSGRhiShaderResourceBindingList.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiShaderResourceBindingList'

  #  Qt's '~QSSGRhiShaderResourceBindingList()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGRhiShaderResourceBindingList behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QSSGRhiShaderResourceBindingListD1Ev'

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
    'QSSGRhiShaderResourceBindingList::QSSGRhiShaderResourceBindingList()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html
    """
    #  QSSGRhiShaderResourceBindingList::QSSGRhiShaderResourceBindingList()
    self._noteCreation(
        QSSGRhiShaderResourceBindingList, lambda: Rituals.call(
            'ritual_ZN32QSSGRhiShaderResourceBindingListC1Ev',
        ))

  @overload(THIS)
  def __init__(self, other: QSSGRhiShaderResourceBindingList) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRhiShaderResourceBindingList::QSSGRhiShaderResourceBindingList(const
    QSSGRhiShaderResourceBindingList &other)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html

    Parameters
    ----------

    other : QSSGRhiShaderResourceBindingList
      Passed on as a value: Qt reads the C++
      QSSGRhiShaderResourceBindingList, which stays Python's own.
    """
    #  QSSGRhiShaderResourceBindingList::
    #      QSSGRhiShaderResourceBindingList(const
    #      QSSGRhiShaderResourceBindingList &other)
    self._noteCreation(
        QSSGRhiShaderResourceBindingList, lambda: Rituals.call(
            'ritual_ZN32QSSGRhiShaderResourceBindingListC1ERKS_',
            self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderResourceBindingList::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html#clear
    """
    #  void QSSGRhiShaderResourceBindingList::clear()
    self.uglySide.call('ritual_ZN32QSSGRhiShaderResourceBindingList5clearEv')

  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType)
  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer, int, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, int, int)
  @overload(
      int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer, int, int, bool,
  )
  @overload(
      int, QRhiShaderResourceBinding.StageFlags, NoneType, int, int, bool,
  )
  def addUniformBuffer(
      self,
      binding: int,
      stage: QRhiShaderResourceBinding.StageFlags,
      buf: Optional[QRhiBuffer],
      offset: int = 0,
      size: int = 0,
      hasDynamicOffset: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderResourceBindingList::addUniformBuffer(int
    binding, QRhiShaderResourceBinding::StageFlags stage, QRhiBuffer *buf,
    int offset, int size, bool hasDynamicOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    size : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    hasDynamicOffset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSSGRhiShaderResourceBindingList::addUniformBuffer(int binding,
    #      QRhiShaderResourceBinding::StageFlags stage, QRhiBuffer *buf, int
    #      offset, int size, bool hasDynamicOffset)
    self.uglySide.call(
        'ritual_ZN32QSSGRhiShaderResourceBindingList16addUniformBufferEi6QF'
        'lagsIN25QRhiShaderResourceBinding9StageFlagEEP10QRhiBufferiib',
        binding, stage.value, self._addressOf(buf), offset, size,
        hasDynamicOffset,
    )

  @overload(
      int, QRhiShaderResourceBinding.StageFlags, QRhiTexture, QRhiSampler,
  )
  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiTexture, NoneType)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, QRhiSampler)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, NoneType)
  def addTexture(
      self,
      binding: int,
      stage: QRhiShaderResourceBinding.StageFlags,
      tex: Optional[QRhiTexture],
      sampler: Optional[QRhiSampler],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderResourceBindingList::addTexture(int
    binding, QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex,
    QRhiSampler *sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html#addTexture

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sampler : Optional[QRhiSampler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiShaderResourceBindingList::addTexture(int binding,
    #      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex,
    #      QRhiSampler *sampler)
    self.uglySide.call(
        'ritual_ZN32QSSGRhiShaderResourceBindingList10addTextureEi6QFlagsIN'
        '25QRhiShaderResourceBinding9StageFlagEEP11QRhiTextureP11QRhiSample'
        'r',
        binding, stage.value, self._addressOf(tex), self._addressOf(sampler),
    )

  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiTexture, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, int)
  def addImageLoad(
      self,
      binding: int,
      stage: QRhiShaderResourceBinding.StageFlags,
      tex: Optional[QRhiTexture],
      level: int,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderResourceBindingList::addImageLoad(int
    binding, QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex,
    int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html#addImageLoad

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : int
      Passed on as it is.
    """
    #  void QSSGRhiShaderResourceBindingList::addImageLoad(int binding,
    #      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex, int
    #      level)
    self.uglySide.call(
        'ritual_ZN32QSSGRhiShaderResourceBindingList12addImageLoadEi6QFlags'
        'IN25QRhiShaderResourceBinding9StageFlagEEP11QRhiTexturei',
        binding, stage.value, self._addressOf(tex), level,
    )

  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiTexture, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, int)
  def addImageStore(
      self,
      binding: int,
      stage: QRhiShaderResourceBinding.StageFlags,
      tex: Optional[QRhiTexture],
      level: int,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderResourceBindingList::addImageStore(int
    binding, QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex,
    int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : int
      Passed on as it is.
    """
    #  void QSSGRhiShaderResourceBindingList::addImageStore(int binding,
    #      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex, int
    #      level)
    self.uglySide.call(
        'ritual_ZN32QSSGRhiShaderResourceBindingList13addImageStoreEi6QFlag'
        'sIN25QRhiShaderResourceBinding9StageFlagEEP11QRhiTexturei',
        binding, stage.value, self._addressOf(tex), level,
    )

  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiTexture, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, int)
  def addImageLoadStore(
      self,
      binding: int,
      stage: QRhiShaderResourceBinding.StageFlags,
      tex: Optional[QRhiTexture],
      level: int,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderResourceBindingList::addImageLoadStore(int
    binding, QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex,
    int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : int
      Passed on as it is.
    """
    #  void QSSGRhiShaderResourceBindingList::addImageLoadStore(int binding,
    #      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex, int
    #      level)
    self.uglySide.call(
        'ritual_ZN32QSSGRhiShaderResourceBindingList17addImageLoadStoreEi6Q'
        'FlagsIN25QRhiShaderResourceBinding9StageFlagEEP11QRhiTexturei',
        binding, stage.value, self._addressOf(tex), level,
    )

  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType)
  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer, int, int)
  @overload(int, QRhiShaderResourceBinding.StageFlags, NoneType, int, int)
  @overload(
      int, QRhiShaderResourceBinding.StageFlags, QRhiBuffer, int, int, bool,
  )
  @overload(
      int, QRhiShaderResourceBinding.StageFlags, NoneType, int, int, bool,
  )
  def addStorageBuffer(
      self,
      binding: int,
      stage: QRhiShaderResourceBinding.StageFlags,
      buf: Optional[QRhiBuffer],
      offset: int = 0,
      size: int = 0,
      hasDynamicOffset: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiShaderResourceBindingList::addStorageBuffer(int
    binding, QRhiShaderResourceBinding::StageFlags stage, QRhiBuffer *buf,
    int offset, int size, bool hasDynamicOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhishaderresourcebindinglist.html

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    size : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    hasDynamicOffset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSSGRhiShaderResourceBindingList::addStorageBuffer(int binding,
    #      QRhiShaderResourceBinding::StageFlags stage, QRhiBuffer *buf, int
    #      offset, int size, bool hasDynamicOffset)
    self.uglySide.call(
        'ritual_ZN32QSSGRhiShaderResourceBindingList16addStorageBufferEi6QF'
        'lagsIN25QRhiShaderResourceBinding9StageFlagEEP10QRhiBufferiib',
        binding, stage.value, self._addressOf(buf), offset, size,
        hasDynamicOffset,
    )
