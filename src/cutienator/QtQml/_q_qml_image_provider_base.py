"""
QQmlImageProviderBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlImageProviderBase(QObject):
  """
  The cute side of Qt's QQmlImageProviderBase: a plain Python object standing
  in front of one C++ QQmlImageProviderBase.

  It is built on the cute 'QObject', as Qt's QQmlImageProviderBase is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlImageProviderBase that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'imageType',
  'flags'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlImageProviderBase::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlImageProviderBase::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlImageProviderBase::~QQmlImageProviderBase()': the destructor:
    Python never removes a C++ QQmlImageProviderBase.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlImageProviderBase is created at the first use, not by
    'QQmlImageProviderBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlImageProviderBase.
  - Qt tells when it has removed the C++ QQmlImageProviderBase. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQmlImageProviderBase, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QQmlImageProviderBase::Flag' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QQmlImageProviderBase::Flags'.
    """

    ForceAsynchronousImageLoading = 0x1

  Flags = Flag

  class ImageType(CuteNum):
    """
    The enum 'QQmlImageProviderBase::ImageType' of Qt, with the 5 names Qt
    gives in it.
    """

    Invalid = Kee[int](0)
    Image = Kee[int](1)
    Pixmap = Kee[int](2)
    Texture = Kee[int](3)
    ImageResponse = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQmlImageProviderBase::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimageproviderbase.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlImageProviderBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQmlImageProviderBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlImageProviderBase'

  #  A C++ QQmlImageProviderBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlImageProviderBase'

  #  The functions Qt calls itself that QQmlImageProviderBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'imageType': (
          ('_ZNK21QQmlImageProviderBase9imageTypeEv',
           ('int', 'enum', 'QtQml:QQmlImageProviderBase.ImageType'),
           ()),
      ),
      'flags': (
          ('_ZNK21QQmlImageProviderBase5flagsEv',
           ('int', 'flags', 'QtQml:QQmlImageProviderBase.Flag'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlImageProviderBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimageproviderbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlImageProviderBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlImageProviderBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def imageType(self) -> ImageType:
    """
    Calls Qt's 'ImageType QQmlImageProviderBase::imageType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimageproviderbase.html#imageType

    Returns
    -------

    ImageType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ImageType(number)' gives.
    """
    #  ImageType QQmlImageProviderBase::imageType() const
    return QQmlImageProviderBase.ImageType(self.uglySide.call(
        'ritual_ZNK21QQmlImageProviderBase9imageTypeEv',
    ))

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QQmlImageProviderBase::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimageproviderbase.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QQmlImageProviderBase::flags() const
    return QQmlImageProviderBase.Flags(self.uglySide.call(
        'ritual_ZNK21QQmlImageProviderBase5flagsEv',
    ))

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
    'QQmlImageProviderBase::QQmlImageProviderBase()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimageproviderbase.html#QQmlImageProviderBase
    """
    #  QQmlImageProviderBase::QQmlImageProviderBase()
    self._noteCreation(QQmlImageProviderBase, lambda: Rituals.call(
        'ritual_ZN21QQmlImageProviderBaseC1Ev',
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
