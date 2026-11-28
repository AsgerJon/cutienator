"""
QQuickRenderTargetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrendertarget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRenderTargetPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhi
  from . import QQuickRenderTarget, QQuickWindowRenderTarget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickRenderTarget = WAIT['QQuickRenderTarget']
  QQuickWindowRenderTarget = WAIT['QQuickWindowRenderTarget']
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRenderTargetPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRenderTargetPrivate: a plain Python object
  standing in front of one C++ QQuickRenderTargetPrivate.

  C++ hands a QQuickRenderTargetPrivate around as a copy, so every C++
  QQuickRenderTargetPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickRenderTargetPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'get', 'resolve'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickRenderTargetPrivate
    *QQuickRenderTargetPrivate::get(const QQuickRenderTarget *rt)': takes in
    Python what 'QQuickRenderTargetPrivate
    *QQuickRenderTargetPrivate::get(QQuickRenderTarget *rt)' takes.
  - Qt's 'QQuickRenderTargetPrivate::~QQuickRenderTargetPrivate()': the
    destructor: Python removes its C++ QQuickRenderTargetPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickRenderTargetPrivate is created at the first use, not by
    'QQuickRenderTargetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickRenderTargetPrivate back gives a copy the
    ritual made for Python, in a new cute QQuickRenderTargetPrivate.
  """

  #  The enums Qt writes inside QQuickRenderTargetPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QQuickRenderTargetPrivate::Type' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Null = Kee[int](0)
    NativeTexture = Kee[int](1)
    NativeTextureArray = Kee[int](2)
    NativeRenderbuffer = Kee[int](3)
    RhiRenderTarget = Kee[int](4)
    PaintDevice = Kee[int](5)

  #  The classes Qt writes inside QQuickRenderTargetPrivate, each a class in
  #  here as in C++.

  class NativeTexture(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickRenderTargetPrivate::NativeTexture: a plain
    Python object standing in front of one C++
    QQuickRenderTargetPrivate::NativeTexture.

    C++ hands a QQuickRenderTargetPrivate::NativeTexture around as a copy, so
    every C++ QQuickRenderTargetPrivate::NativeTexture behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickRenderTargetPrivate::NativeTexture yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickRenderTargetPrivate::NativeTexture::~NativeTexture()': the
      destructor: Python removes its C++
      QQuickRenderTargetPrivate::NativeTexture by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuickRenderTargetPrivate::NativeTexture is created at the
      first use, not by 'QQuickRenderTargetPrivate::NativeTexture(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickRenderTargetPrivate::NativeTexture back gives
      a copy the ritual made for Python, in a new cute
      QQuickRenderTargetPrivate::NativeTexture.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickRenderTargetPrivate::NativeTexture'

    #  Qt's '~QQuickRenderTargetPrivate::NativeTexture()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQuickRenderTargetPrivate::NativeTexture behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QQuickRenderTargetPrivate13NativeTextureD1Ev')

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

  class NativeTextureArray(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickRenderTargetPrivate::NativeTextureArray: a
    plain Python object standing in front of one C++
    QQuickRenderTargetPrivate::NativeTextureArray.

    C++ hands a QQuickRenderTargetPrivate::NativeTextureArray around as a
    copy, so every C++ QQuickRenderTargetPrivate::NativeTextureArray behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickRenderTargetPrivate::NativeTextureArray yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQuickRenderTargetPrivate::NativeTextureArray::~NativeTextureArray()':
      the destructor: Python removes its C++
      QQuickRenderTargetPrivate::NativeTextureArray by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QQuickRenderTargetPrivate::NativeTextureArray is created at the
      first use, not by 'QQuickRenderTargetPrivate::NativeTextureArray(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickRenderTargetPrivate::NativeTextureArray back
      gives a copy the ritual made for Python, in a new cute
      QQuickRenderTargetPrivate::NativeTextureArray.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickRenderTargetPrivate::NativeTextureArray'

    #  Qt's '~QQuickRenderTargetPrivate::NativeTextureArray()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QQuickRenderTargetPrivate::NativeTextureArray behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QQuickRenderTargetPrivate18NativeTextureArrayD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickRenderTarget)
  @overload(NoneType)
  def get(
      rt: Optional[QQuickRenderTarget],
  ) -> Optional[QQuickRenderTargetPrivate]:
    """
    Calls Qt's 'QQuickRenderTargetPrivate
    *QQuickRenderTargetPrivate::get(QQuickRenderTarget *rt)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendertargetprivate.html#get

    Parameters
    ----------

    rt : Optional[QQuickRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickRenderTargetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRenderTargetPrivate
    #      *QQuickRenderTargetPrivate::get(QQuickRenderTarget *rt)
    address = Rituals.call(
        'ritual_ZN25QQuickRenderTargetPrivate3getEP18QQuickRenderTarget',
        CuteMixin._addressOf(rt),
    )
    return QQuickRenderTargetPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRenderTargetPrivate'

  #  Qt's '~QQuickRenderTargetPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickRenderTargetPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QQuickRenderTargetPrivateD1Ev'

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
    'QQuickRenderTargetPrivate::QQuickRenderTargetPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertargetprivate.html
    """
    #  QQuickRenderTargetPrivate::QQuickRenderTargetPrivate()
    self._noteCreation(QQuickRenderTargetPrivate, lambda: Rituals.call(
        'ritual_ZN25QQuickRenderTargetPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QQuickRenderTargetPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRenderTargetPrivate::QQuickRenderTargetPrivate(const
    QQuickRenderTargetPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertargetprivate.html

    Parameters
    ----------

    other : QQuickRenderTargetPrivate
      Passed on as a value: Qt reads the C++ QQuickRenderTargetPrivate, which
      stays Python's own.
    """
    #  QQuickRenderTargetPrivate::QQuickRenderTargetPrivate(const
    #      QQuickRenderTargetPrivate &other)
    self._noteCreation(QQuickRenderTargetPrivate, lambda: Rituals.call(
        'ritual_ZN25QQuickRenderTargetPrivateC1ERKS_', self._valueOf(other),
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

  @overload(QRhi, QQuickWindowRenderTarget)
  @overload(QRhi, NoneType)
  @overload(NoneType, QQuickWindowRenderTarget)
  @overload(NoneType, NoneType)
  def resolve(
      self,
      rhi: Optional[QRhi],
      dst: Optional[QQuickWindowRenderTarget],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickRenderTargetPrivate::resolve(QRhi *rhi,
    QQuickWindowRenderTarget *dst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertargetprivate.html#resolve

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dst : Optional[QQuickWindowRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickRenderTargetPrivate::resolve(QRhi *rhi,
    #      QQuickWindowRenderTarget *dst)
    return self.uglySide.call(
        'ritual_ZN25QQuickRenderTargetPrivate7resolveEP4QRhiP24QQuickWindow'
        'RenderTarget',
        self._addressOf(rhi), self._addressOf(dst),
    )
