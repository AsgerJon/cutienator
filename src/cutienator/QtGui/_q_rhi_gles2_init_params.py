"""
QRhiGles2InitParams binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi_platform.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QRhiInitParams

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOffscreenSurface, QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSurfaceFormat = WAIT['QSurfaceFormat']


class QRhiGles2InitParams(QRhiInitParams):
  """
  The cute side of Qt's QRhiGles2InitParams: a plain Python object standing
  in front of one C++ QRhiGles2InitParams.

  It is built on the cute 'QRhiInitParams', as Qt's QRhiGles2InitParams is
  built on Qt's QRhiInitParams, and has everything that class has.

  C++ hands a QRhiGles2InitParams around as a copy, so every C++
  QRhiGles2InitParams behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiGles2InitParams that has a ritual and that
  Python can call so far, 1 name in all: 'newFallbackSurface'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiGles2InitParams::~QRhiGles2InitParams()': the destructor:
    Python removes its C++ QRhiGles2InitParams by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QRhiGles2InitParams is created at the first use, not by
    'QRhiGles2InitParams(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiGles2InitParams back gives a copy the ritual made
    for Python, in a new cute QRhiGles2InitParams.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSurfaceFormat)
  def newFallbackSurface(
      format: QSurfaceFormat,
  ) -> Optional[QOffscreenSurface]:
    """
    Calls Qt's 'QOffscreenSurface
    *QRhiGles2InitParams::newFallbackSurface(const QSurfaceFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2initparams.html#newFallbackSurface

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.

    Returns
    -------

    Optional[QOffscreenSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOffscreenSurface *QRhiGles2InitParams::newFallbackSurface(const
    #      QSurfaceFormat &format)
    address = Rituals.call(
        'ritual_ZN19QRhiGles2InitParams18newFallbackSurfaceERK14QSurfaceFor'
        'mat',
        CuteMixin._valueOf(format),
    )
    from . import QOffscreenSurface
    return QOffscreenSurface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiGles2InitParams'

  #  Qt's '~QRhiGles2InitParams()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiGles2InitParams behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QRhiGles2InitParamsD1Ev'

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
    'QRhiGles2InitParams::QRhiGles2InitParams()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2initparams.html#QRhiGles2InitParams
    """
    #  QRhiGles2InitParams::QRhiGles2InitParams()
    self._noteCreation(QRhiGles2InitParams, lambda: Rituals.call(
        'ritual_ZN19QRhiGles2InitParamsC1Ev',
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
