"""
QRhiRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QRhiImplementation, QRhiRenderPassDescriptor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiRenderTarget(QRhiResource):
  """
  The cute side of Qt's QRhiRenderTarget: a plain Python object standing in
  front of one C++ QRhiRenderTarget.

  It is built on the cute 'QRhiResource', as Qt's QRhiRenderTarget is built
  on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiRenderTarget that has a ritual and that Python
  can call so far, 5 names in all: 'pixelSize', 'devicePixelRatio',
  'sampleCount', 'renderPassDescriptor', 'setRenderPassDescriptor'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiRenderTarget is created at the first use, not by
    'QRhiRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiRenderTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiRenderTarget'

  #  A C++ QRhiRenderTarget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiRenderTarget'

  #  The functions Qt calls itself that QRhiRenderTarget is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'pixelSize': (
          ('_ZNK16QRhiRenderTarget9pixelSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'devicePixelRatio': (
          ('_ZNK16QRhiRenderTarget16devicePixelRatioEv',
           ('float', 'number', ''),
           ()),
      ),
      'sampleCount': (
          ('_ZNK16QRhiRenderTarget11sampleCountEv',
           ('int', 'number', ''),
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

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiRenderTarget::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirendertarget.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiRenderTarget::pixelSize() const
    address = self.uglySide.call('ritual_ZNK16QRhiRenderTarget9pixelSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float QRhiRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirendertarget.html#devicePixelRatio
    """
    #  float QRhiRenderTarget::devicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK16QRhiRenderTarget16devicePixelRatioEv',
    )

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QRhiRenderTarget::sampleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirendertarget.html#sampleCount
    """
    #  int QRhiRenderTarget::sampleCount() const
    return self.uglySide.call('ritual_ZNK16QRhiRenderTarget11sampleCountEv')

  def renderPassDescriptor(self) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QRhiRenderTarget::renderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirendertarget.html#renderPassDescriptor

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor *QRhiRenderTarget::renderPassDescriptor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QRhiRenderTarget20renderPassDescriptorEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiRenderPassDescriptor)
  @overload(NoneType)
  def setRenderPassDescriptor(
      self,
      desc: Optional[QRhiRenderPassDescriptor],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiRenderTarget::setRenderPassDescriptor(QRhiRenderPassDescriptor
    *desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirendertarget.html#setRenderPassDescriptor

    Parameters
    ----------

    desc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QRhiRenderTarget::setRenderPassDescriptor(QRhiRenderPassDescriptor
    #      *desc)
    self.uglySide.call(
        'ritual_ZN16QRhiRenderTarget23setRenderPassDescriptorEP24QRhiRender'
        'PassDescriptor',
        self._addressOf(desc),
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
    'QRhiRenderTarget::QRhiRenderTarget(QRhiImplementation *rhi)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirendertarget.html#QRhiRenderTarget

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiRenderTarget::QRhiRenderTarget(QRhiImplementation *rhi)
    self._noteCreation(QRhiRenderTarget, lambda: Rituals.call(
        'ritual_ZN16QRhiRenderTargetC1EP18QRhiImplementation',
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
