"""
QRhiComputePipeline binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteFlags, WAIT
from ..occult import Rituals
from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhiImplementation, QRhiShaderResourceBindings
  from . import QRhiShaderStage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QRhiShaderStage = WAIT['QRhiShaderStage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiComputePipeline(QRhiResource):
  """
  The cute side of Qt's QRhiComputePipeline: a plain Python object standing
  in front of one C++ QRhiComputePipeline.

  It is built on the cute 'QRhiResource', as Qt's QRhiComputePipeline is
  built on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiComputePipeline that has a ritual and that
  Python can call so far, 8 names in all: 'resourceType', 'create', 'flags',
  'setFlags', 'shaderStage', 'setShaderStage', 'shaderResourceBindings',
  'setShaderResourceBindings'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QRhiComputePipeline is created at the first use, not by
    'QRhiComputePipeline(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiComputePipeline.
  """

  #  The enums Qt writes inside QRhiComputePipeline, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QRhiComputePipeline::Flag' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QRhiComputePipeline::Flags'.
    """

    CompileShadersWithDebugInfo = 0x1

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiComputePipeline'

  #  A C++ QRhiComputePipeline Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiComputePipeline'

  #  The functions Qt calls itself that QRhiComputePipeline is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN19QRhiComputePipeline6createEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiComputePipeline::resourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicomputepipeline.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiComputePipeline::resourceType() const
    ritual = 'ritual_ZNK19QRhiComputePipeline12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QRhiComputePipeline12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QRhiComputePipeline::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicomputepipeline.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QRhiComputePipeline::flags() const
    return QRhiComputePipeline.Flags(self.uglySide.call(
        'ritual_ZNK19QRhiComputePipeline5flagsEv',
    ))

  def shaderStage(self) -> QRhiShaderStage:
    """
    Calls Qt's 'QRhiShaderStage QRhiComputePipeline::shaderStage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicomputepipeline.html#shaderStage

    Returns
    -------

    QRhiShaderStage
      A new cute QRhiShaderStage around the copy Qt gave back. Python owns
      it.
    """
    #  QRhiShaderStage QRhiComputePipeline::shaderStage() const
    address = self.uglySide.call(
        'ritual_ZNK19QRhiComputePipeline11shaderStageEv',
    )
    from . import QRhiShaderStage
    return QRhiShaderStage._cuteOwning(address)

  def shaderResourceBindings(self) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhiComputePipeline::shaderResourceBindings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicomputepipeline.html#shaderResourceBindings

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings
    #      *QRhiComputePipeline::shaderResourceBindings() const
    address = self.uglySide.call(
        'ritual_ZNK19QRhiComputePipeline22shaderResourceBindingsEv',
    )
    from . import QRhiShaderResourceBindings
    return QRhiShaderResourceBindings._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QRhiComputePipeline::setFlags(Flags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicomputepipeline.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as its number.
    """
    #  void QRhiComputePipeline::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN19QRhiComputePipeline8setFlagsE6QFlagsINS_4FlagEE',
        f.value,
    )

  @overload(QRhiShaderStage)
  def setShaderStage(self, stage: QRhiShaderStage) -> None:
    """
    Calls Qt's 'void QRhiComputePipeline::setShaderStage(const
    QRhiShaderStage &stage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicomputepipeline.html#setShaderStage

    Parameters
    ----------

    stage : QRhiShaderStage
      Passed on as a value: Qt reads the C++ QRhiShaderStage, which stays
      Python's own.
    """
    #  void QRhiComputePipeline::setShaderStage(const QRhiShaderStage &stage)
    self.uglySide.call(
        'ritual_ZN19QRhiComputePipeline14setShaderStageERK15QRhiShaderStage',
        self._valueOf(stage),
    )

  @overload(QRhiShaderResourceBindings)
  @overload(NoneType)
  def setShaderResourceBindings(
      self,
      srb: Optional[QRhiShaderResourceBindings],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiComputePipeline::setShaderResourceBindings(QRhiShaderResourceBindings
    *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicomputepipeline.html#setShaderResourceBindings

    Parameters
    ----------

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiComputePipeline::setShaderResourceBindings(
    #      QRhiShaderResourceBindings *srb)
    self.uglySide.call(
        'ritual_ZN19QRhiComputePipeline25setShaderResourceBindingsEP26QRhiS'
        'haderResourceBindings',
        self._addressOf(srb),
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

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiComputePipeline::QRhiComputePipeline(QRhiImplementation *rhi)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicomputepipeline.html#QRhiComputePipeline

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiComputePipeline::QRhiComputePipeline(QRhiImplementation *rhi)
    self._noteCreation(QRhiComputePipeline, lambda: Rituals.call(
        'ritual_ZN19QRhiComputePipelineC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QRhiComputePipeline::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicomputepipeline.html#create
    """
    #  bool QRhiComputePipeline::create()
    return self.uglySide.call('ritual_ZN19QRhiComputePipeline6createEv')
