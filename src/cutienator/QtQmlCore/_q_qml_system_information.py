"""
QQmlSystemInformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCore/6.12.0/QtQmlCore/private/qqmlsysteminformation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlSystemInformation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlSystemInformation(QObject):
  """
  The cute side of Qt's QQmlSystemInformation: a plain Python object standing
  in front of one C++ QQmlSystemInformation.

  It is built on the cute 'QObject', as Qt's QQmlSystemInformation is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlSystemInformation that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'wordSize',
  'byteOrder', 'buildCpuArchitecture', 'currentCpuArchitecture', 'buildAbi',
  'kernelType', 'kernelVersion', 'productType', 'productVersion',
  'prettyProductName', 'machineHostName', 'machineUniqueId', 'bootUniqueId'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlSystemInformation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlSystemInformation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlSystemInformation::qt_qmlMarker_singleton()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlSystemInformation is created at the first use, not by
    'QQmlSystemInformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSystemInformation.
  - Qt tells when it has removed the C++ QQmlSystemInformation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQmlSystemInformation, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Endian(CuteNum, scoped=True):
    """
    The enum 'QQmlSystemInformation::Endian' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Big = Kee[int](0)
    Little = Kee[int](1)

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
    Calls Qt's 'QString QQmlSystemInformation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsysteminformation.html#tr

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
    #  QString QQmlSystemInformation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQmlSystemInformation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSystemInformation'

  #  A C++ QQmlSystemInformation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSystemInformation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlSystemInformation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlSystemInformation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def wordSize(self) -> int:
    """
    Calls Qt's 'int QQmlSystemInformation::wordSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#wordSize
    """
    #  int QQmlSystemInformation::wordSize() const
    return self.uglySide.call('ritual_ZNK21QQmlSystemInformation8wordSizeEv')

  def byteOrder(self) -> Endian:
    """
    Calls Qt's 'Endian QQmlSystemInformation::byteOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#byteOrder

    Returns
    -------

    Endian
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Endian(number)' gives.
    """
    #  Endian QQmlSystemInformation::byteOrder() const
    return QQmlSystemInformation.Endian(self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation9byteOrderEv',
    ))

  def buildCpuArchitecture(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::buildCpuArchitecture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#buildCpuArchitecture

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::buildCpuArchitecture() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation20buildCpuArchitectureEv',
    )

  def currentCpuArchitecture(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::currentCpuArchitecture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#currentCpuArchitecture

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::currentCpuArchitecture() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation22currentCpuArchitectureEv',
    )

  def buildAbi(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::buildAbi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#buildAbi

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::buildAbi() const
    return self.uglySide.call('ritual_ZNK21QQmlSystemInformation8buildAbiEv')

  def kernelType(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::kernelType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#kernelType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::kernelType() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation10kernelTypeEv',
    )

  def kernelVersion(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::kernelVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#kernelVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::kernelVersion() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation13kernelVersionEv',
    )

  def productType(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::productType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#productType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::productType() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation11productTypeEv',
    )

  def productVersion(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::productVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#productVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::productVersion() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation14productVersionEv',
    )

  def prettyProductName(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::prettyProductName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#prettyProductName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::prettyProductName() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation17prettyProductNameEv',
    )

  def machineHostName(self) -> str:
    """
    Calls Qt's 'QString QQmlSystemInformation::machineHostName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#machineHostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSystemInformation::machineHostName() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation15machineHostNameEv',
    )

  def machineUniqueId(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlSystemInformation::machineUniqueId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#machineUniqueId

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlSystemInformation::machineUniqueId() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation15machineUniqueIdEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def bootUniqueId(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlSystemInformation::bootUniqueId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#bootUniqueId

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlSystemInformation::bootUniqueId() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlSystemInformation12bootUniqueIdEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSystemInformation::QQmlSystemInformation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsysteminformation.html#QQmlSystemInformation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlSystemInformation::QQmlSystemInformation(QObject *parent)
    self._noteCreation(QQmlSystemInformation, lambda: Rituals.call(
        'ritual_ZN21QQmlSystemInformationC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
