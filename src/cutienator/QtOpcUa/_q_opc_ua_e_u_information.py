"""
QOpcUaEUInformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaeuinformation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QOpcUaLocalizedText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']


class QOpcUaEUInformation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaEUInformation: a plain Python object standing
  in front of one C++ QOpcUaEUInformation.

  C++ hands a QOpcUaEUInformation around as a copy, so every C++
  QOpcUaEUInformation behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaEUInformation that has a ritual and that
  Python can call so far, 9 names in all: '__eq__', 'namespaceUri',
  'setNamespaceUri', 'unitId', 'setUnitId', 'displayName', 'setDisplayName',
  'description', 'setDescription'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaEUInformation &QOpcUaEUInformation::operator=(const
    QOpcUaEUInformation &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaEUInformation::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaEUInformation::~QOpcUaEUInformation()': the destructor:
    Python removes its C++ QOpcUaEUInformation by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaEUInformation is created at the first use, not by
    'QOpcUaEUInformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaEUInformation back gives a copy the ritual made
    for Python, in a new cute QOpcUaEUInformation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaEUInformation'

  #  Qt's '~QOpcUaEUInformation()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaEUInformation behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QOpcUaEUInformationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def namespaceUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaEUInformation::namespaceUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#namespaceUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaEUInformation::namespaceUri() const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaEUInformation12namespaceUriEv',
    )

  def unitId(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaEUInformation::unitId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaeuinformation.html#unitId
    """
    #  qint32 QOpcUaEUInformation::unitId() const
    return self.uglySide.call('ritual_ZNK19QOpcUaEUInformation6unitIdEv')

  def displayName(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaEUInformation::displayName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#displayName

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaEUInformation::displayName() const
    address = self.uglySide.call(
        'ritual_ZNK19QOpcUaEUInformation11displayNameEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def description(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaEUInformation::description()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#description

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaEUInformation::description() const
    address = self.uglySide.call(
        'ritual_ZNK19QOpcUaEUInformation11descriptionEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNamespaceUri(self, namespaceUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaEUInformation::setNamespaceUri(const QString
    &namespaceUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#setNamespaceUri

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaEUInformation::setNamespaceUri(const QString &namespaceUri)
    self.uglySide.call(
        'ritual_ZN19QOpcUaEUInformation15setNamespaceUriERK7QString',
        namespaceUri,
    )

  @overload(int)
  def setUnitId(self, unitId: int) -> None:
    """
    Calls Qt's 'void QOpcUaEUInformation::setUnitId(qint32 unitId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaeuinformation.html#setUnitId

    Parameters
    ----------

    unitId : int
      Passed on as it is.
    """
    #  void QOpcUaEUInformation::setUnitId(qint32 unitId)
    self.uglySide.call('ritual_ZN19QOpcUaEUInformation9setUnitIdEi', unitId)

  @overload(QOpcUaLocalizedText)
  def setDisplayName(self, displayName: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaEUInformation::setDisplayName(const
    QOpcUaLocalizedText &displayName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#setDisplayName

    Parameters
    ----------

    displayName : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaEUInformation::setDisplayName(const QOpcUaLocalizedText
    #      &displayName)
    self.uglySide.call(
        'ritual_ZN19QOpcUaEUInformation14setDisplayNameERK19QOpcUaLocalized'
        'Text',
        self._valueOf(displayName),
    )

  @overload(QOpcUaLocalizedText)
  def setDescription(self, description: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaEUInformation::setDescription(const
    QOpcUaLocalizedText &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#setDescription

    Parameters
    ----------

    description : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaEUInformation::setDescription(const QOpcUaLocalizedText
    #      &description)
    self.uglySide.call(
        'ritual_ZN19QOpcUaEUInformation14setDescriptionERK19QOpcUaLocalized'
        'Text',
        self._valueOf(description),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaEUInformation) -> bool:
    """
    Calls Qt's 'bool QOpcUaEUInformation::operator==(const
    QOpcUaEUInformation &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#operator==

    Parameters
    ----------

    rhs : QOpcUaEUInformation
      Passed on as a value: Qt reads the C++ QOpcUaEUInformation, which stays
      Python's own.
    """
    #  bool QOpcUaEUInformation::operator==(const QOpcUaEUInformation &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaEUInformationeqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    'QOpcUaEUInformation::QOpcUaEUInformation()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#QOpcUaEUInformation
    """
    #  QOpcUaEUInformation::QOpcUaEUInformation()
    self._noteCreation(QOpcUaEUInformation, lambda: Rituals.call(
        'ritual_ZN19QOpcUaEUInformationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaEUInformation) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaEUInformation::QOpcUaEUInformation(const QOpcUaEUInformation
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#QOpcUaEUInformation

    Parameters
    ----------

    a0 : QOpcUaEUInformation
      Passed on as a value: Qt reads the C++ QOpcUaEUInformation, which stays
      Python's own.
    """
    #  QOpcUaEUInformation::QOpcUaEUInformation(const QOpcUaEUInformation
    #      &a0)
    self._noteCreation(QOpcUaEUInformation, lambda: Rituals.call(
        'ritual_ZN19QOpcUaEUInformationC1ERKS_', self._valueOf(a0),
    ))

  @overload(str, int, QOpcUaLocalizedText, QOpcUaLocalizedText)
  def __init__(
      self,
      namespaceUri: str,
      unitId: int,
      displayName: QOpcUaLocalizedText,
      description: QOpcUaLocalizedText,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaEUInformation::QOpcUaEUInformation(const QString &namespaceUri,
    qint32 unitId, const QOpcUaLocalizedText &displayName, const
    QOpcUaLocalizedText &description)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaeuinformation.html#QOpcUaEUInformation

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    unitId : int
      Passed on as it is.

    displayName : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.

    description : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  QOpcUaEUInformation::QOpcUaEUInformation(const QString &namespaceUri,
    #      qint32 unitId, const QOpcUaLocalizedText &displayName, const
    #      QOpcUaLocalizedText &description)
    self._noteCreation(QOpcUaEUInformation, lambda: Rituals.call(
        'ritual_ZN19QOpcUaEUInformationC1ERK7QStringiRK19QOpcUaLocalizedTex'
        'tS5_',
        namespaceUri, unitId, self._valueOf(displayName),
        self._valueOf(description),
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
