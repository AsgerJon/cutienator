"""
QPdfOutputIntent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpdfoutputintent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
  from . import QColorSpace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorSpace = WAIT['QColorSpace']
  QUrl = WAIT['QUrl']


class QPdfOutputIntent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdfOutputIntent: a plain Python object standing in
  front of one C++ QPdfOutputIntent.

  C++ hands a QPdfOutputIntent around as a copy, so every C++
  QPdfOutputIntent behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPdfOutputIntent that has a ritual and that Python
  can call so far, 8 names in all: 'outputConditionIdentifier',
  'setOutputConditionIdentifier', 'outputCondition', 'setOutputCondition',
  'registryName', 'setRegistryName', 'outputProfile', 'setOutputProfile'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdfOutputIntent::~QPdfOutputIntent()': the destructor: Python
    removes its C++ QPdfOutputIntent by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPdfOutputIntent is created at the first use, not by
    'QPdfOutputIntent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdfOutputIntent back gives a copy the ritual made
    for Python, in a new cute QPdfOutputIntent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfOutputIntent'

  #  Qt's '~QPdfOutputIntent()'. Naming it makes this a value class: Python
  #  owns every C++ QPdfOutputIntent behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QPdfOutputIntentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def outputConditionIdentifier(self) -> str:
    """
    Calls Qt's 'QString QPdfOutputIntent::outputConditionIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#outputConditionIdentifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfOutputIntent::outputConditionIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK16QPdfOutputIntent25outputConditionIdentifierEv',
    )

  def outputCondition(self) -> str:
    """
    Calls Qt's 'QString QPdfOutputIntent::outputCondition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#outputCondition

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfOutputIntent::outputCondition() const
    return self.uglySide.call(
        'ritual_ZNK16QPdfOutputIntent15outputConditionEv',
    )

  def registryName(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPdfOutputIntent::registryName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfoutputintent.html#registryName

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPdfOutputIntent::registryName() const
    address = self.uglySide.call(
        'ritual_ZNK16QPdfOutputIntent12registryNameEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def outputProfile(self) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QPdfOutputIntent::outputProfile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#outputProfile

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QPdfOutputIntent::outputProfile() const
    address = self.uglySide.call(
        'ritual_ZNK16QPdfOutputIntent13outputProfileEv',
    )
    from . import QColorSpace
    return QColorSpace._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setOutputConditionIdentifier(self, identifier: str) -> None:
    """
    Calls Qt's 'void QPdfOutputIntent::setOutputConditionIdentifier(const
    QString &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#setOutputConditionIdentifier

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfOutputIntent::setOutputConditionIdentifier(const QString
    #      &identifier)
    self.uglySide.call(
        'ritual_ZN16QPdfOutputIntent28setOutputConditionIdentifierERK7QStri'
        'ng',
        identifier,
    )

  @overload(str)
  def setOutputCondition(self, condition: str) -> None:
    """
    Calls Qt's 'void QPdfOutputIntent::setOutputCondition(const QString
    &condition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#setOutputCondition

    Parameters
    ----------

    condition : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfOutputIntent::setOutputCondition(const QString &condition)
    self.uglySide.call(
        'ritual_ZN16QPdfOutputIntent18setOutputConditionERK7QString',
        condition,
    )

  @overload(QUrl)
  def setRegistryName(self, name: QUrl) -> None:
    """
    Calls Qt's 'void QPdfOutputIntent::setRegistryName(const QUrl &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#setRegistryName

    Parameters
    ----------

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPdfOutputIntent::setRegistryName(const QUrl &name)
    self.uglySide.call(
        'ritual_ZN16QPdfOutputIntent15setRegistryNameERK4QUrl',
        self._valueOf(name),
    )

  @overload(QColorSpace)
  def setOutputProfile(self, profile: QColorSpace) -> None:
    """
    Calls Qt's 'void QPdfOutputIntent::setOutputProfile(const QColorSpace
    &profile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#setOutputProfile

    Parameters
    ----------

    profile : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  void QPdfOutputIntent::setOutputProfile(const QColorSpace &profile)
    self.uglySide.call(
        'ritual_ZN16QPdfOutputIntent16setOutputProfileERK11QColorSpace',
        self._valueOf(profile),
    )

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
    Notes what was given, for Qt's 'QPdfOutputIntent::QPdfOutputIntent()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#QPdfOutputIntent
    """
    #  QPdfOutputIntent::QPdfOutputIntent()
    self._noteCreation(QPdfOutputIntent, lambda: Rituals.call(
        'ritual_ZN16QPdfOutputIntentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPdfOutputIntent) -> None:
    """
    Notes what was given, for Qt's 'QPdfOutputIntent::QPdfOutputIntent(const
    QPdfOutputIntent &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfoutputintent.html#QPdfOutputIntent

    Parameters
    ----------

    other : QPdfOutputIntent
      Passed on as a value: Qt reads the C++ QPdfOutputIntent, which stays
      Python's own.
    """
    #  QPdfOutputIntent::QPdfOutputIntent(const QPdfOutputIntent &other)
    self._noteCreation(QPdfOutputIntent, lambda: Rituals.call(
        'ritual_ZN16QPdfOutputIntentC1ERKS_', self._valueOf(other),
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
