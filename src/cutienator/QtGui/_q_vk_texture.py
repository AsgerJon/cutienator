"""
QVkTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVkTexture to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QVkTexture(QRhiTexture):
  """
  The cute side of Qt's QVkTexture: a plain Python object standing in front
  of one C++ QVkTexture.

  It is built on the cute 'QRhiTexture', as Qt's QVkTexture is built on Qt's
  QRhiTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVkTexture that has a ritual and that Python can
  call so far, 5 names in all: 'destroy', 'create', 'createFrom',
  'nativeTexture', 'setNativeLayout'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVkTexture::~QVkTexture()': the destructor: Python never removes a
    C++ QVkTexture.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QVkTexture.

  What to expect
  --------------

  - The C++ QVkTexture is created at the first use, not by 'QVkTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVkTexture.
  - Each name of Qt's QVkTexture that has no cute function yet, '__init__',
    'finishCreate', 'perLevelImageViewForLoadStore', 'prepareCreate', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QVkTexture, each a class in here as in C++.

  class UsageState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVkTexture::UsageState: a plain Python object
    standing in front of one C++ QVkTexture::UsageState.

    C++ hands a QVkTexture::UsageState around as a copy, so every C++
    QVkTexture::UsageState behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QVkTexture::UsageState yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVkTexture::UsageState::~UsageState()': the destructor: Python
      removes its C++ QVkTexture::UsageState by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QVkTexture::UsageState is created at the first use, not by
      'QVkTexture::UsageState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVkTexture::UsageState back gives a copy the ritual
      made for Python, in a new cute QVkTexture::UsageState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVkTexture::UsageState'

    #  Qt's '~QVkTexture::UsageState()'. Naming it makes this a value class:
    #  Python owns every C++ QVkTexture::UsageState behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QVkTexture10UsageStateD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVkTexture'

  #  A C++ QVkTexture Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVkTexture'

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

  @overload(int)
  def setNativeLayout(self, layout: int) -> None:
    """
    Calls Qt's 'void QVkTexture::setNativeLayout(int layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qvktexture.html#setNativeLayout

    Parameters
    ----------

    layout : int
      Passed on as it is.
    """
    #  void QVkTexture::setNativeLayout(int layout)
    ritual = 'ritual_ZN10QVkTexture15setNativeLayoutEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QVkTexture15setNativeLayoutEi'
    self.uglySide.call(ritual, layout)

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
    Qt's 'QVkTexture::QVkTexture(QRhiImplementation *rhi, Format format,
    const QSize &pixelSize, int depth, int arraySize, int sampleCount, Flags
    flags)': leans on 'QVkTexture::create()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QVkTexture.__init__' has no cute function yet. Qt's "
        "'QVkTexture::QVkTexture(QRhiImplementation *rhi, Format format, "
        "const QSize &pixelSize, int depth, int arraySize, int sampleCount, "
        "Flags flags)': leans on 'QVkTexture::create()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'void QVkTexture::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qvktexture.html#destroy
    """
    #  void QVkTexture::destroy()
    ritual = 'ritual_ZN10QVkTexture7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QVkTexture7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QVkTexture::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qvktexture.html#create
    """
    #  bool QVkTexture::create()
    return self.uglySide.call('ritual_ZN10QVkTexture6createEv')

  @overload(QRhiTexture.NativeTexture)
  def createFrom(self, src: QRhiTexture.NativeTexture) -> bool:
    """
    Calls Qt's 'bool QVkTexture::createFrom(NativeTexture src)'.

    Qt's own words: https://doc.qt.io/qt-6/qvktexture.html#createFrom

    Parameters
    ----------

    src : QRhiTexture.NativeTexture
      Passed on as a value: Qt reads the C++ QRhiTexture::NativeTexture,
      which stays Python's own.
    """
    #  bool QVkTexture::createFrom(NativeTexture src)
    return self.uglySide.call(
        'ritual_ZN10QVkTexture10createFromEN11QRhiTexture13NativeTextureE',
        self._valueOf(src),
    )

  def nativeTexture(self) -> QRhiTexture.NativeTexture:
    """
    Calls Qt's 'NativeTexture QVkTexture::nativeTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qvktexture.html#nativeTexture

    Returns
    -------

    QRhiTexture.NativeTexture
      A new cute QRhiTexture::NativeTexture around the copy Qt gave back.
      Python owns it.
    """
    #  NativeTexture QVkTexture::nativeTexture()
    ritual = 'ritual_ZN10QVkTexture13nativeTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QVkTexture13nativeTextureEv'
    address = self.uglySide.call(ritual)
    return QRhiTexture.NativeTexture._cuteOwning(address)

  @staticmethod
  def finishCreate(*__, **_) -> Never:
    """
    Qt's 'bool QVkTexture::finishCreate()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QVkTexture.finishCreate' has no cute function yet. Qt's 'bool "
        "QVkTexture::finishCreate()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def perLevelImageViewForLoadStore(*__, **_) -> Never:
    """
    Qt's 'VkImageView QVkTexture::perLevelImageViewForLoadStore(int level)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'aspectMaskForTextureFormat'.
    """
    raise NotImplementedError(
        "'QVkTexture.perLevelImageViewForLoadStore' has no cute function "
        "yet. Qt's 'VkImageView "
        "QVkTexture::perLevelImageViewForLoadStore(int level)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'aspectMaskForTextureFormat'.")

  @staticmethod
  def prepareCreate(*__, **_) -> Never:
    """
    Qt's 'bool QVkTexture::prepareCreate(QSize *adjustedSize)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'toVkTextureFormat'.
    """
    raise NotImplementedError(
        "'QVkTexture.prepareCreate' has no cute function yet. Qt's 'bool "
        "QVkTexture::prepareCreate(QSize *adjustedSize)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'toVkTextureFormat'.")
