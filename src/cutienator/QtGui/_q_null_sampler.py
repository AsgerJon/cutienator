"""
QNullSampler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullSampler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiSampler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNullSampler(QRhiSampler):
  """
  The cute side of Qt's QNullSampler: a plain Python object standing in front
  of one C++ QNullSampler.

  It is built on the cute 'QRhiSampler', as Qt's QNullSampler is built on
  Qt's QRhiSampler, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNullSampler that has a ritual and that Python can
  call so far, 2 names in all: 'destroy', 'create'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullSampler::~QNullSampler()': the destructor: Python never
    removes a C++ QNullSampler.

  What to expect
  --------------

  - The C++ QNullSampler is created at the first use, not by
    'QNullSampler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullSampler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullSampler'

  #  A C++ QNullSampler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullSampler'

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

  @overload(
      QRhiImplementation, QRhiSampler.Filter, QRhiSampler.Filter,
      QRhiSampler.Filter, QRhiSampler.AddressMode, QRhiSampler.AddressMode,
      QRhiSampler.AddressMode,
  )
  @overload(
      NoneType, QRhiSampler.Filter, QRhiSampler.Filter, QRhiSampler.Filter,
      QRhiSampler.AddressMode, QRhiSampler.AddressMode,
      QRhiSampler.AddressMode,
  )
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      magFilter: QRhiSampler.Filter,
      minFilter: QRhiSampler.Filter,
      mipmapMode: QRhiSampler.Filter,
      u: QRhiSampler.AddressMode,
      v: QRhiSampler.AddressMode,
      w: QRhiSampler.AddressMode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNullSampler::QNullSampler(QRhiImplementation *rhi, Filter magFilter,
    Filter minFilter, Filter mipmapMode, AddressMode u, AddressMode v,
    AddressMode w)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnullsampler.html#QNullSampler

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    magFilter : QRhiSampler.Filter
      Passed on as its number.

    minFilter : QRhiSampler.Filter
      Passed on as its number.

    mipmapMode : QRhiSampler.Filter
      Passed on as its number.

    u : QRhiSampler.AddressMode
      Passed on as its number.

    v : QRhiSampler.AddressMode
      Passed on as its number.

    w : QRhiSampler.AddressMode
      Passed on as its number.
    """
    #  QNullSampler::QNullSampler(QRhiImplementation *rhi, Filter magFilter,
    #      Filter minFilter, Filter mipmapMode, AddressMode u, AddressMode v,
    #      AddressMode w)
    self._noteCreation(QNullSampler, lambda: Rituals.call(
        'ritual_ZN12QNullSamplerC1EP18QRhiImplementationN11QRhiSampler6Filt'
        'erES3_S3_NS2_11AddressModeES4_S4_',
        self._addressOf(rhi), magFilter.value, minFilter.value,
        mipmapMode.value, u.value, v.value, w.value,
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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QNullSampler::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qnullsampler.html#destroy
    """
    #  void QNullSampler::destroy()
    ritual = 'ritual_ZN12QNullSampler7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QNullSampler7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QNullSampler::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qnullsampler.html#create
    """
    #  bool QNullSampler::create()
    ritual = 'ritual_ZN12QNullSampler6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QNullSampler6createEv'
    return self.uglySide.call(ritual)
