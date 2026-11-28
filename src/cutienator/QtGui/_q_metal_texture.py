"""
QMetalTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMetalTexture to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMetalTexture(QRhiTexture):
  """
  The cute side of Qt's QMetalTexture: a plain Python object standing in
  front of one C++ QMetalTexture.

  It is built on the cute 'QRhiTexture', as Qt's QMetalTexture is built on
  Qt's QRhiTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMetalTexture that has a ritual and that Python can
  call so far, 4 names in all: 'destroy', 'create', 'createFrom',
  'nativeTexture'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QMetalTexture is created at the first use, not by
    'QMetalTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetalTexture.
  - Each name of Qt's QMetalTexture that has no cute function yet,
    '__init__', 'prepareCreate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetalTexture'

  #  A C++ QMetalTexture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMetalTexture'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QMetalTexture::QMetalTexture(QRhiImplementation *rhi, Format
    format, const QSize &pixelSize, int depth, int arraySize, int
    sampleCount, Flags flags)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QMetalTexture.__init__' has no cute function yet. Qt's "
        "'QMetalTexture::QMetalTexture(QRhiImplementation *rhi, Format "
        "format, const QSize &pixelSize, int depth, int arraySize, int "
        "sampleCount, Flags flags)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

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
    Calls Qt's 'void QMetalTexture::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaltexture.html#destroy
    """
    #  void QMetalTexture::destroy()
    self.uglySide.call('ritual_ZN13QMetalTexture7destroyEv')

  def create(self) -> bool:
    """
    Calls Qt's 'bool QMetalTexture::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaltexture.html#create
    """
    #  bool QMetalTexture::create()
    return self.uglySide.call('ritual_ZN13QMetalTexture6createEv')

  @overload(QRhiTexture.NativeTexture)
  def createFrom(self, src: QRhiTexture.NativeTexture) -> bool:
    """
    Calls Qt's 'bool QMetalTexture::createFrom(NativeTexture src)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaltexture.html#createFrom

    Parameters
    ----------

    src : QRhiTexture.NativeTexture
      Passed on as a value: Qt reads the C++ QRhiTexture::NativeTexture,
      which stays Python's own.
    """
    #  bool QMetalTexture::createFrom(NativeTexture src)
    return self.uglySide.call(
        'ritual_ZN13QMetalTexture10createFromEN11QRhiTexture13NativeTexture'
        'E',
        self._valueOf(src),
    )

  def nativeTexture(self) -> QRhiTexture.NativeTexture:
    """
    Calls Qt's 'NativeTexture QMetalTexture::nativeTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaltexture.html#nativeTexture

    Returns
    -------

    QRhiTexture.NativeTexture
      A new cute QRhiTexture::NativeTexture around the copy Qt gave back.
      Python owns it.
    """
    #  NativeTexture QMetalTexture::nativeTexture()
    address = self.uglySide.call('ritual_ZN13QMetalTexture13nativeTextureEv')
    return QRhiTexture.NativeTexture._cuteOwning(address)

  @staticmethod
  def prepareCreate(*__, **_) -> Never:
    """
    Qt's 'bool QMetalTexture::prepareCreate(QSize *adjustedSize)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QMetalTexture.prepareCreate' has no cute function yet. Qt's 'bool "
        "QMetalTexture::prepareCreate(QSize *adjustedSize)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
