"""
QQmlSA::FixSuggestion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class FixSuggestion(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::FixSuggestion: a plain Python object standing
  in front of one C++ QQmlSA::FixSuggestion.

  C++ hands a QQmlSA::FixSuggestion around as a copy, so every C++
  QQmlSA::FixSuggestion behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::FixSuggestion that has a ritual and that
  Python can call so far, 10 names in all: 'd_func', 'description',
  'location', 'addDocumentEdit', 'setFileName', 'fileName',
  'setAutoApplicable', 'isAutoApplicable', '__eq__', '__ne__'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const FixSuggestionPrivate *QQmlSA::FixSuggestion::d_func() const':
    takes in Python what 'FixSuggestionPrivate
    *QQmlSA::FixSuggestion::d_func()' takes.
  - Qt's 'QQmlSA::FixSuggestion::FixSuggestion(const QString &description,
    const QQmlSA::SourceLocation &location, const QList<DocumentEdit>
    &documentEdits)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlSA::FixSuggestion::FixSuggestion(FixSuggestion &&a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'FixSuggestion &QQmlSA::FixSuggestion::operator=(const FixSuggestion
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'FixSuggestion &QQmlSA::FixSuggestion::operator=(FixSuggestion
    &&a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlSA::FixSuggestion::~FixSuggestion()': the destructor: Python
    removes its C++ QQmlSA::FixSuggestion by it, and has no other use for it.
  - Qt's 'QList<DocumentEdit> QQmlSA::FixSuggestion::documentEdits() const':
    gives a type Python has no way to take yet.
  - Qt's 'bool QQmlSA::FixSuggestion::operatorEqualsImpl(const FixSuggestion
    &a0, const FixSuggestion &a1)': an operator Python has no name for.

  What to expect
  --------------

  - The C++ QQmlSA::FixSuggestion is created at the first use, not by
    'QQmlSA::FixSuggestion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::FixSuggestion back gives a copy the ritual
    made for Python, in a new cute QQmlSA::FixSuggestion.
  - Each name of Qt's QQmlSA::FixSuggestion that has no cute function yet,
    'documentEdits', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::FixSuggestion'

  #  Qt's '~QQmlSA::FixSuggestion()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::FixSuggestion behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA13FixSuggestionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def description(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::FixSuggestion::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::FixSuggestion::description() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA13FixSuggestion11descriptionEv',
    )

  def location(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'QQmlSA::SourceLocation QQmlSA::FixSuggestion::location()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#location

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSA::SourceLocation QQmlSA::FixSuggestion::location() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA13FixSuggestion8locationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::FixSuggestion::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::FixSuggestion::fileName() const
    return self.uglySide.call('ritual_ZNK6QQmlSA13FixSuggestion8fileNameEv')

  def isAutoApplicable(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::FixSuggestion::isAutoApplicable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#isAutoApplicable
    """
    #  bool QQmlSA::FixSuggestion::isAutoApplicable() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA13FixSuggestion16isAutoApplicableEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, a0: str) -> None:
    """
    Calls Qt's 'void QQmlSA::FixSuggestion::setFileName(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#setFileName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSA::FixSuggestion::setFileName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN6QQmlSA13FixSuggestion11setFileNameERK7QString', a0,
    )

  @overload()
  @overload(bool)
  def setAutoApplicable(self, autoApplicable: bool = True) -> None:
    """
    Calls Qt's 'void QQmlSA::FixSuggestion::setAutoApplicable(bool
    autoApplicable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#setAutoApplicable

    Parameters
    ----------

    autoApplicable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlSA::FixSuggestion::setAutoApplicable(bool autoApplicable)
    self.uglySide.call(
        'ritual_ZN6QQmlSA13FixSuggestion17setAutoApplicableEb',
        autoApplicable,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: FixSuggestion) -> bool:
    """
    Calls Qt's 'bool operator==(const FixSuggestion &lhs, const FixSuggestion
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#operator==

    Parameters
    ----------

    rhs : FixSuggestion
      Passed on as a value: Qt reads the C++ QQmlSA::FixSuggestion, which
      stays Python's own.
    """
    #  bool operator==(const FixSuggestion &lhs, const FixSuggestion &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_13FixSuggestionES2_',
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
  def __ne__(self, rhs: FixSuggestion) -> bool:
    """
    Calls Qt's 'bool operator!=(const FixSuggestion &lhs, const FixSuggestion
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#operator!=

    Parameters
    ----------

    rhs : FixSuggestion
      Passed on as a value: Qt reads the C++ QQmlSA::FixSuggestion, which
      stays Python's own.
    """
    #  bool operator!=(const FixSuggestion &lhs, const FixSuggestion &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_13FixSuggestionES2_',
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

  @overload(str, WAIT['QQmlSA.SourceLocation'], WAIT['QQmlSA.DocumentEdit'])
  def __init__(
      self,
      description: str,
      location: QQmlSA.SourceLocation,
      documentEdit: QQmlSA.DocumentEdit,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::FixSuggestion::FixSuggestion(const QString &description, const
    QQmlSA::SourceLocation &location, const DocumentEdit &documentEdit)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#FixSuggestion

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.

    documentEdit : QQmlSA.DocumentEdit
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEdit, which
      stays Python's own.
    """
    #  QQmlSA::FixSuggestion::FixSuggestion(const QString &description, const
    #      QQmlSA::SourceLocation &location, const DocumentEdit
    #      &documentEdit)
    self._noteCreation(FixSuggestion, lambda: Rituals.call(
        'ritual_ZN6QQmlSA13FixSuggestionC1ERK7QStringRKNS_14SourceLocationE'
        'RKNS_12DocumentEditE',
        description, self._valueOf(location), self._valueOf(documentEdit),
    ))

  @overload(THIS)
  def __init__(self, a0: FixSuggestion) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::FixSuggestion::FixSuggestion(const FixSuggestion &a0)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#FixSuggestion

    Parameters
    ----------

    a0 : FixSuggestion
      Passed on as a value: Qt reads the C++ QQmlSA::FixSuggestion, which
      stays Python's own.
    """
    #  QQmlSA::FixSuggestion::FixSuggestion(const FixSuggestion &a0)
    self._noteCreation(FixSuggestion, lambda: Rituals.call(
        'ritual_ZN6QQmlSA13FixSuggestionC1ERKS0_', self._valueOf(a0),
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

  def d_func(self) -> Optional[QQmlSA.FixSuggestionPrivate]:
    """
    Calls Qt's 'FixSuggestionPrivate *QQmlSA::FixSuggestion::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#d_func

    Returns
    -------

    Optional[QQmlSA.FixSuggestionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FixSuggestionPrivate *QQmlSA::FixSuggestion::d_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA13FixSuggestion6d_funcEv')
    return QQmlSA.FixSuggestionPrivate._cuteAt(address)

  @overload(WAIT['QQmlSA.DocumentEdit'])
  def addDocumentEdit(self, a0: QQmlSA.DocumentEdit) -> None:
    """
    Calls Qt's 'void QQmlSA::FixSuggestion::addDocumentEdit(const
    DocumentEdit &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestion.html#addDocumentEdit

    Parameters
    ----------

    a0 : QQmlSA.DocumentEdit
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEdit, which
      stays Python's own.
    """
    #  void QQmlSA::FixSuggestion::addDocumentEdit(const DocumentEdit &a0)
    self.uglySide.call(
        'ritual_ZN6QQmlSA13FixSuggestion15addDocumentEditERKNS_12DocumentEd'
        'itE',
        self._valueOf(a0),
    )

  @staticmethod
  def documentEdits(*__, **_) -> Never:
    """
    Qt's 'QList<DocumentEdit> QQmlSA::FixSuggestion::documentEdits() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.FixSuggestion.documentEdits' has no cute function yet. "
        "Qt's 'QList<DocumentEdit> QQmlSA::FixSuggestion::documentEdits() "
        "const': gives a type Python has no way to take yet.")
