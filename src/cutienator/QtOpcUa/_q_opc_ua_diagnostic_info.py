"""
QOpcUaDiagnosticInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuadiagnosticinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpcUaDiagnosticInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaDiagnosticInfo: a plain Python object standing
  in front of one C++ QOpcUaDiagnosticInfo.

  C++ hands a QOpcUaDiagnosticInfo around as a copy, so every C++
  QOpcUaDiagnosticInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaDiagnosticInfo that has a ritual and that
  Python can call so far, 30 names in all: 'symbolicId', 'setSymbolicId',
  'hasSymbolicId', 'setHasSymbolicId', 'namespaceUri', 'setNamespaceUri',
  'hasNamespaceUri', 'setHasNamespaceUri', 'locale', 'setLocale',
  'hasLocale', 'setHasLocale', 'localizedText', 'setLocalizedText',
  'hasLocalizedText', 'setHasLocalizedText', 'additionalInfo',
  'setAdditionalInfo', 'hasAdditionalInfo', 'setHasAdditionalInfo',
  'innerStatusCode', 'setInnerStatusCode', 'hasInnerStatusCode',
  'setHasInnerStatusCode', 'innerDiagnosticInfo', 'setInnerDiagnosticInfo',
  'hasInnerDiagnosticInfo', 'setHasInnerDiagnosticInfo', '__eq__', '__ne__'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaDiagnosticInfo::~QOpcUaDiagnosticInfo()': the destructor:
    Python removes its C++ QOpcUaDiagnosticInfo by it, and has no other use
    for it.
  - Qt's 'QOpcUaDiagnosticInfo::QOpcUaDiagnosticInfo(QOpcUaDiagnosticInfo
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaDiagnosticInfo &QOpcUaDiagnosticInfo::operator=(const
    QOpcUaDiagnosticInfo &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'void QOpcUaDiagnosticInfo::swap(QOpcUaDiagnosticInfo &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaDiagnosticInfo
    &QOpcUaDiagnosticInfo::operator=(QOpcUaDiagnosticInfo &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaDiagnosticInfo::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaDiagnosticInfo
    &QOpcUaDiagnosticInfo::innerDiagnosticInfoRef()': gives a type Python has
    no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaDiagnosticInfo is created at the first use, not by
    'QOpcUaDiagnosticInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaDiagnosticInfo back gives a copy the ritual
    made for Python, in a new cute QOpcUaDiagnosticInfo.
  - Each name of Qt's QOpcUaDiagnosticInfo that has no cute function yet,
    'innerDiagnosticInfoRef', 'swap', holds a function that raises
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
  __qt_class__ = 'QOpcUaDiagnosticInfo'

  #  Qt's '~QOpcUaDiagnosticInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaDiagnosticInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpcUaDiagnosticInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def symbolicId(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaDiagnosticInfo::symbolicId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#symbolicId
    """
    #  qint32 QOpcUaDiagnosticInfo::symbolicId() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo10symbolicIdEv',
    )

  def hasSymbolicId(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDiagnosticInfo::hasSymbolicId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#hasSymbolicId
    """
    #  bool QOpcUaDiagnosticInfo::hasSymbolicId() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo13hasSymbolicIdEv',
    )

  def namespaceUri(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaDiagnosticInfo::namespaceUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#namespaceUri
    """
    #  qint32 QOpcUaDiagnosticInfo::namespaceUri() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo12namespaceUriEv',
    )

  def hasNamespaceUri(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDiagnosticInfo::hasNamespaceUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#hasNamespaceUri
    """
    #  bool QOpcUaDiagnosticInfo::hasNamespaceUri() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo15hasNamespaceUriEv',
    )

  def locale(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaDiagnosticInfo::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#locale
    """
    #  qint32 QOpcUaDiagnosticInfo::locale() const
    return self.uglySide.call('ritual_ZNK20QOpcUaDiagnosticInfo6localeEv')

  def hasLocale(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDiagnosticInfo::hasLocale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#hasLocale
    """
    #  bool QOpcUaDiagnosticInfo::hasLocale() const
    return self.uglySide.call('ritual_ZNK20QOpcUaDiagnosticInfo9hasLocaleEv')

  def localizedText(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaDiagnosticInfo::localizedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#localizedText
    """
    #  qint32 QOpcUaDiagnosticInfo::localizedText() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo13localizedTextEv',
    )

  def hasLocalizedText(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDiagnosticInfo::hasLocalizedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#hasLocalizedText
    """
    #  bool QOpcUaDiagnosticInfo::hasLocalizedText() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo16hasLocalizedTextEv',
    )

  def additionalInfo(self) -> str:
    """
    Calls Qt's 'QString QOpcUaDiagnosticInfo::additionalInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#additionalInfo

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaDiagnosticInfo::additionalInfo() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo14additionalInfoEv',
    )

  def hasAdditionalInfo(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDiagnosticInfo::hasAdditionalInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#hasAdditionalInfo
    """
    #  bool QOpcUaDiagnosticInfo::hasAdditionalInfo() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo17hasAdditionalInfoEv',
    )

  def innerStatusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaDiagnosticInfo::innerStatusCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#innerStatusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaDiagnosticInfo::innerStatusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo15innerStatusCodeEv',
    ))

  def hasInnerStatusCode(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDiagnosticInfo::hasInnerStatusCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#hasInnerStatusCode
    """
    #  bool QOpcUaDiagnosticInfo::hasInnerStatusCode() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo18hasInnerStatusCodeEv',
    )

  def innerDiagnosticInfo(self) -> QOpcUaDiagnosticInfo:
    """
    Calls Qt's 'QOpcUaDiagnosticInfo
    QOpcUaDiagnosticInfo::innerDiagnosticInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#innerDiagnosticInfo

    Returns
    -------

    QOpcUaDiagnosticInfo
      A new cute QOpcUaDiagnosticInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaDiagnosticInfo QOpcUaDiagnosticInfo::innerDiagnosticInfo() const
    address = self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo19innerDiagnosticInfoEv',
    )
    return QOpcUaDiagnosticInfo._cuteOwning(address)

  def hasInnerDiagnosticInfo(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaDiagnosticInfo::hasInnerDiagnosticInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#hasInnerDiagnosticInfo
    """
    #  bool QOpcUaDiagnosticInfo::hasInnerDiagnosticInfo() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaDiagnosticInfo22hasInnerDiagnosticInfoEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSymbolicId(self, newSymbolicId: int) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setSymbolicId(qint32
    newSymbolicId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setSymbolicId

    Parameters
    ----------

    newSymbolicId : int
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setSymbolicId(qint32 newSymbolicId)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo13setSymbolicIdEi', newSymbolicId,
    )

  @overload(bool)
  def setHasSymbolicId(self, newHasSymbolicId: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setHasSymbolicId(bool
    newHasSymbolicId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setHasSymbolicId

    Parameters
    ----------

    newHasSymbolicId : bool
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setHasSymbolicId(bool newHasSymbolicId)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo16setHasSymbolicIdEb',
        newHasSymbolicId,
    )

  @overload(int)
  def setNamespaceUri(self, newNamespaceUri: int) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setNamespaceUri(qint32
    newNamespaceUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setNamespaceUri

    Parameters
    ----------

    newNamespaceUri : int
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setNamespaceUri(qint32 newNamespaceUri)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo15setNamespaceUriEi',
        newNamespaceUri,
    )

  @overload(bool)
  def setHasNamespaceUri(self, newHasNamespaceUri: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setHasNamespaceUri(bool
    newHasNamespaceUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setHasNamespaceUri

    Parameters
    ----------

    newHasNamespaceUri : bool
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setHasNamespaceUri(bool newHasNamespaceUri)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo18setHasNamespaceUriEb',
        newHasNamespaceUri,
    )

  @overload(int)
  def setLocale(self, newLocale: int) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setLocale(qint32 newLocale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setLocale

    Parameters
    ----------

    newLocale : int
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setLocale(qint32 newLocale)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo9setLocaleEi', newLocale,
    )

  @overload(bool)
  def setHasLocale(self, newHasLocale: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setHasLocale(bool newHasLocale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setHasLocale

    Parameters
    ----------

    newHasLocale : bool
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setHasLocale(bool newHasLocale)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo12setHasLocaleEb', newHasLocale,
    )

  @overload(int)
  def setLocalizedText(self, newLocalizedText: int) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setLocalizedText(qint32
    newLocalizedText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setLocalizedText

    Parameters
    ----------

    newLocalizedText : int
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setLocalizedText(qint32 newLocalizedText)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo16setLocalizedTextEi',
        newLocalizedText,
    )

  @overload(bool)
  def setHasLocalizedText(self, newHasLocalizedText: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setHasLocalizedText(bool
    newHasLocalizedText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setHasLocalizedText

    Parameters
    ----------

    newHasLocalizedText : bool
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setHasLocalizedText(bool
    #      newHasLocalizedText)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo19setHasLocalizedTextEb',
        newHasLocalizedText,
    )

  @overload(str)
  def setAdditionalInfo(self, newAdditionalInfo: str) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setAdditionalInfo(const QString
    &newAdditionalInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setAdditionalInfo

    Parameters
    ----------

    newAdditionalInfo : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaDiagnosticInfo::setAdditionalInfo(const QString
    #      &newAdditionalInfo)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo17setAdditionalInfoERK7QString',
        newAdditionalInfo,
    )

  @overload(bool)
  def setHasAdditionalInfo(self, newHasAdditionalInfo: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setHasAdditionalInfo(bool
    newHasAdditionalInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setHasAdditionalInfo

    Parameters
    ----------

    newHasAdditionalInfo : bool
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setHasAdditionalInfo(bool
    #      newHasAdditionalInfo)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo20setHasAdditionalInfoEb',
        newHasAdditionalInfo,
    )

  @overload(QOpcUa.UaStatusCode)
  def setInnerStatusCode(
      self,
      newInnerStatusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaDiagnosticInfo::setInnerStatusCode(QOpcUa::UaStatusCode
    newInnerStatusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setInnerStatusCode

    Parameters
    ----------

    newInnerStatusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaDiagnosticInfo::setInnerStatusCode(QOpcUa::UaStatusCode
    #      newInnerStatusCode)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo18setInnerStatusCodeEN6QOpcUa12UaSt'
        'atusCodeE',
        newInnerStatusCode.value,
    )

  @overload(bool)
  def setHasInnerStatusCode(self, newHasInnerStatusCode: bool) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setHasInnerStatusCode(bool
    newHasInnerStatusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setHasInnerStatusCode

    Parameters
    ----------

    newHasInnerStatusCode : bool
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setHasInnerStatusCode(bool
    #      newHasInnerStatusCode)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo21setHasInnerStatusCodeEb',
        newHasInnerStatusCode,
    )

  @overload(THIS)
  def setInnerDiagnosticInfo(
      self,
      newInnerDiagnosticInfo: QOpcUaDiagnosticInfo,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setInnerDiagnosticInfo(const
    QOpcUaDiagnosticInfo &newInnerDiagnosticInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#setInnerDiagnosticInfo

    Parameters
    ----------

    newInnerDiagnosticInfo : QOpcUaDiagnosticInfo
      Passed on as a value: Qt reads the C++ QOpcUaDiagnosticInfo, which
      stays Python's own.
    """
    #  void QOpcUaDiagnosticInfo::setInnerDiagnosticInfo(const
    #      QOpcUaDiagnosticInfo &newInnerDiagnosticInfo)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo22setInnerDiagnosticInfoERKS_',
        self._valueOf(newInnerDiagnosticInfo),
    )

  @overload(bool)
  def setHasInnerDiagnosticInfo(
      self,
      newHasInnerDiagnosticInfo: bool,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaDiagnosticInfo::setHasInnerDiagnosticInfo(bool
    newHasInnerDiagnosticInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html

    Parameters
    ----------

    newHasInnerDiagnosticInfo : bool
      Passed on as it is.
    """
    #  void QOpcUaDiagnosticInfo::setHasInnerDiagnosticInfo(bool
    #      newHasInnerDiagnosticInfo)
    self.uglySide.call(
        'ritual_ZN20QOpcUaDiagnosticInfo25setHasInnerDiagnosticInfoEb',
        newHasInnerDiagnosticInfo,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaDiagnosticInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaDiagnosticInfo &lhs, const
    QOpcUaDiagnosticInfo &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#operator==

    Parameters
    ----------

    rhs : QOpcUaDiagnosticInfo
      Passed on as a value: Qt reads the C++ QOpcUaDiagnosticInfo, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaDiagnosticInfo &lhs, const
    #      QOpcUaDiagnosticInfo &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QOpcUaDiagnosticInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QOpcUaDiagnosticInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaDiagnosticInfo &lhs, const
    QOpcUaDiagnosticInfo &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaDiagnosticInfo
      Passed on as a value: Qt reads the C++ QOpcUaDiagnosticInfo, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaDiagnosticInfo &lhs, const
    #      QOpcUaDiagnosticInfo &rhs)
    return Rituals.call(
        'ritual_ZneRK20QOpcUaDiagnosticInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaDiagnosticInfo::QOpcUaDiagnosticInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#QOpcUaDiagnosticInfo
    """
    #  QOpcUaDiagnosticInfo::QOpcUaDiagnosticInfo()
    self._noteCreation(QOpcUaDiagnosticInfo, lambda: Rituals.call(
        'ritual_ZN20QOpcUaDiagnosticInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaDiagnosticInfo) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaDiagnosticInfo::QOpcUaDiagnosticInfo(const QOpcUaDiagnosticInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadiagnosticinfo.html#QOpcUaDiagnosticInfo

    Parameters
    ----------

    other : QOpcUaDiagnosticInfo
      Passed on as a value: Qt reads the C++ QOpcUaDiagnosticInfo, which
      stays Python's own.
    """
    #  QOpcUaDiagnosticInfo::QOpcUaDiagnosticInfo(const QOpcUaDiagnosticInfo
    #      &other)
    self._noteCreation(QOpcUaDiagnosticInfo, lambda: Rituals.call(
        'ritual_ZN20QOpcUaDiagnosticInfoC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def innerDiagnosticInfoRef(*__, **_) -> Never:
    """
    Qt's 'QOpcUaDiagnosticInfo
    &QOpcUaDiagnosticInfo::innerDiagnosticInfoRef()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaDiagnosticInfo.innerDiagnosticInfoRef' has no cute function "
        "yet. Qt's 'QOpcUaDiagnosticInfo "
        "&QOpcUaDiagnosticInfo::innerDiagnosticInfoRef()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaDiagnosticInfo::swap(QOpcUaDiagnosticInfo &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaDiagnosticInfo.swap' has no cute function yet. Qt's 'void "
        "QOpcUaDiagnosticInfo::swap(QOpcUaDiagnosticInfo &other)': takes a "
        "type Python has no way to hand over yet.")
