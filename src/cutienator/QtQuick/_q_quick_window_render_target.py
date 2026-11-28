"""
QQuickWindowRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickWindowRenderTarget to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhi
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWindowRenderTarget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickWindowRenderTarget: a plain Python object
  standing in front of one C++ QQuickWindowRenderTarget.

  C++ hands a QQuickWindowRenderTarget around as a copy, so every C++
  QQuickWindowRenderTarget behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickWindowRenderTarget that has a ritual and that
  Python can call so far, 1 name in all: 'reset'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickWindowRenderTarget::~QQuickWindowRenderTarget()': the
    destructor: Python removes its C++ QQuickWindowRenderTarget by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickWindowRenderTarget is created at the first use, not by
    'QQuickWindowRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickWindowRenderTarget back gives a copy the ritual
    made for Python, in a new cute QQuickWindowRenderTarget.
  """

  #  The enums Qt writes inside QQuickWindowRenderTarget, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ResetFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QQuickWindowRenderTarget::ResetFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QQuickWindowRenderTarget::ResetFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    KeepImplicitBuffers = 0x1

  ResetFlags = ResetFlag

  #  The classes Qt writes inside QQuickWindowRenderTarget, each a class in
  #  here as in C++.

  class ImplicitBuffers(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickWindowRenderTarget::ImplicitBuffers: a plain
    Python object standing in front of one C++
    QQuickWindowRenderTarget::ImplicitBuffers.

    C++ hands a QQuickWindowRenderTarget::ImplicitBuffers around as a copy,
    so every C++ QQuickWindowRenderTarget::ImplicitBuffers behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuickWindowRenderTarget::ImplicitBuffers that has
    a ritual and that Python can call so far, 1 name in all: 'reset'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickWindowRenderTarget::ImplicitBuffers::~ImplicitBuffers()':
      the destructor: Python removes its C++
      QQuickWindowRenderTarget::ImplicitBuffers by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuickWindowRenderTarget::ImplicitBuffers is created at the
      first use, not by 'QQuickWindowRenderTarget::ImplicitBuffers(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickWindowRenderTarget::ImplicitBuffers back
      gives a copy the ritual made for Python, in a new cute
      QQuickWindowRenderTarget::ImplicitBuffers.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRhi = WAIT['QRhi']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickWindowRenderTarget::ImplicitBuffers'

    #  Qt's '~QQuickWindowRenderTarget::ImplicitBuffers()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQuickWindowRenderTarget::ImplicitBuffers behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN24QQuickWindowRenderTarget15ImplicitBuffersD1Ev')

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

    @overload(QRhi)
    @overload(NoneType)
    def reset(self, rhi: Optional[QRhi]) -> None:
      """
      Calls Qt's 'void QQuickWindowRenderTarget::ImplicitBuffers::reset(QRhi
      *rhi)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickwindowrendertarget-implicitbuffers.html

      Parameters
      ----------

      rhi : Optional[QRhi]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QQuickWindowRenderTarget::ImplicitBuffers::reset(QRhi *rhi)
      self.uglySide.call(
          'ritual_ZN24QQuickWindowRenderTarget15ImplicitBuffers5resetEP4QRh'
          'i',
          self._addressOf(rhi),
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWindowRenderTarget'

  #  Qt's '~QQuickWindowRenderTarget()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickWindowRenderTarget behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQuickWindowRenderTargetD1Ev'

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

  @overload(QRhi)
  @overload(NoneType)
  @overload(QRhi, ResetFlags)
  @overload(NoneType, ResetFlags)
  def reset(
      self,
      rhi: Optional[QRhi],
      flags: ResetFlags = ResetFlags(),
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowRenderTarget::reset(QRhi *rhi, ResetFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowrendertarget.html#reset

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : ResetFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ResetFlags().
    """
    #  void QQuickWindowRenderTarget::reset(QRhi *rhi, ResetFlags flags)
    self.uglySide.call(
        'ritual_ZN24QQuickWindowRenderTarget5resetEP4QRhi6QFlagsINS_9ResetF'
        'lagEE',
        self._addressOf(rhi), flags.value,
    )
