"""
QQmlJSFixSuggestion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSFixSuggestion to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQml import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QQmlJSDocumentEdit
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSDocumentEdit = WAIT['QQmlJSDocumentEdit']


class QQmlJSFixSuggestion(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSFixSuggestion: a plain Python object standing
  in front of one C++ QQmlJSFixSuggestion.

  C++ hands a QQmlJSFixSuggestion around as a copy, so every C++
  QQmlJSFixSuggestion behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSFixSuggestion that has a ritual and that
  Python can call so far, 11 names in all: 'description', 'location',
  'addDocumentEdit', 'setDocumentEdits', 'documentEdits', 'setFilename',
  'filename', 'setAutoApplicable', 'isAutoApplicable', '__eq__', '__ne__'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSFixSuggestion::~QQmlJSFixSuggestion()': the destructor:
    Python removes its C++ QQmlJSFixSuggestion by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlJSFixSuggestion is created at the first use, not by
    'QQmlJSFixSuggestion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSFixSuggestion back gives a copy the ritual made
    for Python, in a new cute QQmlJSFixSuggestion.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSFixSuggestion'

  #  Qt's '~QQmlJSFixSuggestion()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJSFixSuggestion behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlJSFixSuggestionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def description(self) -> str:
    """
    Calls Qt's 'QString QQmlJSFixSuggestion::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSFixSuggestion::description() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSFixSuggestion11descriptionEv',
    )

  def location(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation QQmlJSFixSuggestion::location()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#location

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSFixSuggestion::location() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSFixSuggestion8locationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def documentEdits(self) -> QList[QQmlJSDocumentEdit]:
    """
    Calls Qt's 'QList<QQmlJSDocumentEdit>
    QQmlJSFixSuggestion::documentEdits() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#documentEdits

    Returns
    -------

    QList[QQmlJSDocumentEdit]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSDocumentEdit> QQmlJSFixSuggestion::documentEdits() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSFixSuggestion13documentEditsEv',
    )
    from . import QQmlJSDocumentEdit
    return QList[QQmlJSDocumentEdit]._cuteOwning(address)

  def filename(self) -> str:
    """
    Calls Qt's 'QString QQmlJSFixSuggestion::filename() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#filename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSFixSuggestion::filename() const
    return self.uglySide.call('ritual_ZNK19QQmlJSFixSuggestion8filenameEv')

  def isAutoApplicable(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSFixSuggestion::isAutoApplicable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#isAutoApplicable
    """
    #  bool QQmlJSFixSuggestion::isAutoApplicable() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSFixSuggestion16isAutoApplicableEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QQmlJSDocumentEdit])
  def setDocumentEdits(
      self,
      documentEdits: QList[QQmlJSDocumentEdit],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSFixSuggestion::setDocumentEdits(const
    QList<QQmlJSDocumentEdit> &documentEdits)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#setDocumentEdits

    Parameters
    ----------

    documentEdits : QList[QQmlJSDocumentEdit]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSFixSuggestion::setDocumentEdits(const
    #      QList<QQmlJSDocumentEdit> &documentEdits)
    self.uglySide.call(
        'ritual_ZN19QQmlJSFixSuggestion16setDocumentEditsERK5QListI18QQmlJS'
        'DocumentEditE',
        self._valueOf(documentEdits),
    )

  @overload(str)
  def setFilename(self, filename: str) -> None:
    """
    Calls Qt's 'void QQmlJSFixSuggestion::setFilename(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#setFilename

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSFixSuggestion::setFilename(const QString &filename)
    self.uglySide.call(
        'ritual_ZN19QQmlJSFixSuggestion11setFilenameERK7QString', filename,
    )

  @overload()
  @overload(bool)
  def setAutoApplicable(self, autoApply: bool = True) -> None:
    """
    Calls Qt's 'void QQmlJSFixSuggestion::setAutoApplicable(bool autoApply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#setAutoApplicable

    Parameters
    ----------

    autoApply : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlJSFixSuggestion::setAutoApplicable(bool autoApply)
    self.uglySide.call(
        'ritual_ZN19QQmlJSFixSuggestion17setAutoApplicableEb', autoApply,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QQmlJSFixSuggestion) -> bool:
    """
    Calls Qt's 'bool QQmlJSFixSuggestion::operator==(const
    QQmlJSFixSuggestion &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#operator==

    Parameters
    ----------

    a0 : QQmlJSFixSuggestion
      Passed on as a value: Qt reads the C++ QQmlJSFixSuggestion, which stays
      Python's own.
    """
    #  bool QQmlJSFixSuggestion::operator==(const QQmlJSFixSuggestion &a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSFixSuggestioneqERKS_', self._valueOf(a0),
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
  def __ne__(self, a0: QQmlJSFixSuggestion) -> bool:
    """
    Calls Qt's 'bool QQmlJSFixSuggestion::operator!=(const
    QQmlJSFixSuggestion &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#operator!=

    Parameters
    ----------

    a0 : QQmlJSFixSuggestion
      Passed on as a value: Qt reads the C++ QQmlJSFixSuggestion, which stays
      Python's own.
    """
    #  bool QQmlJSFixSuggestion::operator!=(const QQmlJSFixSuggestion &a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSFixSuggestionneERKS_', self._valueOf(a0),
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
    'QQmlJSFixSuggestion::QQmlJSFixSuggestion()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#QQmlJSFixSuggestion
    """
    #  QQmlJSFixSuggestion::QQmlJSFixSuggestion()
    self._noteCreation(QQmlJSFixSuggestion, lambda: Rituals.call(
        'ritual_ZN19QQmlJSFixSuggestionC1Ev',
    ))

  @overload(str, WAIT['QQmlJS.SourceLocation'], QQmlJSDocumentEdit)
  def __init__(
      self,
      description: str,
      location: QQmlJS.SourceLocation,
      a2: QQmlJSDocumentEdit,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSFixSuggestion::QQmlJSFixSuggestion(const QString &description,
    const QQmlJS::SourceLocation &location, const QQmlJSDocumentEdit &a2)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#QQmlJSFixSuggestion

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    a2 : QQmlJSDocumentEdit
      Passed on as a value: Qt reads the C++ QQmlJSDocumentEdit, which stays
      Python's own.
    """
    #  QQmlJSFixSuggestion::QQmlJSFixSuggestion(const QString &description,
    #      const QQmlJS::SourceLocation &location, const QQmlJSDocumentEdit
    #      &a2)
    self._noteCreation(QQmlJSFixSuggestion, lambda: Rituals.call(
        'ritual_ZN19QQmlJSFixSuggestionC1ERK7QStringRKN6QQmlJS14SourceLocat'
        'ionERK18QQmlJSDocumentEdit',
        description, self._valueOf(location), self._valueOf(a2),
    ))

  @overload(str, WAIT['QQmlJS.SourceLocation'], QList[QQmlJSDocumentEdit])
  def __init__(
      self,
      description: str,
      location: QQmlJS.SourceLocation,
      a2: QList[QQmlJSDocumentEdit],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSFixSuggestion::QQmlJSFixSuggestion(const QString &description,
    const QQmlJS::SourceLocation &location, const QList<QQmlJSDocumentEdit>
    &a2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#QQmlJSFixSuggestion

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    a2 : QList[QQmlJSDocumentEdit]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QQmlJSFixSuggestion::QQmlJSFixSuggestion(const QString &description,
    #      const QQmlJS::SourceLocation &location, const
    #      QList<QQmlJSDocumentEdit> &a2)
    self._noteCreation(QQmlJSFixSuggestion, lambda: Rituals.call(
        'ritual_ZN19QQmlJSFixSuggestionC1ERK7QStringRKN6QQmlJS14SourceLocat'
        'ionERK5QListI18QQmlJSDocumentEditE',
        description, self._valueOf(location), self._valueOf(a2),
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

  @overload(QQmlJSDocumentEdit)
  def addDocumentEdit(self, documentEdit: QQmlJSDocumentEdit) -> None:
    """
    Calls Qt's 'void QQmlJSFixSuggestion::addDocumentEdit(const
    QQmlJSDocumentEdit &documentEdit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfixsuggestion.html#addDocumentEdit

    Parameters
    ----------

    documentEdit : QQmlJSDocumentEdit
      Passed on as a value: Qt reads the C++ QQmlJSDocumentEdit, which stays
      Python's own.
    """
    #  void QQmlJSFixSuggestion::addDocumentEdit(const QQmlJSDocumentEdit
    #      &documentEdit)
    self.uglySide.call(
        'ritual_ZN19QQmlJSFixSuggestion15addDocumentEditERK18QQmlJSDocument'
        'Edit',
        self._valueOf(documentEdit),
    )
