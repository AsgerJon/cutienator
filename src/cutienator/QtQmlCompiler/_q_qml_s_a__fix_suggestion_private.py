"""
QQmlSA::FixSuggestionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::FixSuggestionPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSFixSuggestion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSFixSuggestion = WAIT['QQmlJSFixSuggestion']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FixSuggestionPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::FixSuggestionPrivate: a plain Python object
  standing in front of one C++ QQmlSA::FixSuggestionPrivate.

  C++ hands a QQmlSA::FixSuggestionPrivate around as a copy, so every C++
  QQmlSA::FixSuggestionPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::FixSuggestionPrivate that has a ritual and
  that Python can call so far, 9 names in all: 'q_func', 'location',
  'description', 'addDocumentEdit', 'setFileName', 'fileName',
  'setAutoApplicable', 'isAutoApplicable', 'createQQmlSAFixSuggestion'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const FixSuggestion *QQmlSA::FixSuggestionPrivate::q_func() const':
    takes in Python what 'FixSuggestion
    *QQmlSA::FixSuggestionPrivate::q_func()' takes.
  - Qt's 'QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion
    *a0, const QString &description, const SourceLocation &location, const
    QList<DocumentEdit> &documentEdits)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion
    *a0, FixSuggestionPrivate &&a1)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlSA::FixSuggestionPrivate::~FixSuggestionPrivate()': the
    destructor: Python removes its C++ QQmlSA::FixSuggestionPrivate by it,
    and has no other use for it.
  - Qt's 'QList<DocumentEdit> QQmlSA::FixSuggestionPrivate::documentEdits()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSFixSuggestion
    &QQmlSA::FixSuggestionPrivate::fixSuggestion(QQmlSA::FixSuggestion &a0)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 18 functions Qt declares: 1 leans on 'QQmlSA.

  What to expect
  --------------

  - The C++ QQmlSA::FixSuggestionPrivate is created at the first use, not by
    'QQmlSA::FixSuggestionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::FixSuggestionPrivate back gives a copy the
    ritual made for Python, in a new cute QQmlSA::FixSuggestionPrivate.
  - Each name of Qt's QQmlSA::FixSuggestionPrivate that has no cute function
    yet, 'documentEdits', 'fixSuggestion', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlJSFixSuggestion)
  def createQQmlSAFixSuggestion(
      a0: QQmlJSFixSuggestion,
  ) -> QQmlSA.FixSuggestion:
    """
    Calls Qt's 'FixSuggestion
    QQmlSA::FixSuggestionPrivate::createQQmlSAFixSuggestion(const
    QQmlJSFixSuggestion &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html

    Parameters
    ----------

    a0 : QQmlJSFixSuggestion
      Passed on as a value: Qt reads the C++ QQmlJSFixSuggestion, which stays
      Python's own.

    Returns
    -------

    QQmlSA.FixSuggestion
      A new cute QQmlSA::FixSuggestion around the copy Qt gave back. Python
      owns it.
    """
    #  FixSuggestion
    #      QQmlSA::FixSuggestionPrivate::createQQmlSAFixSuggestion(const
    #      QQmlJSFixSuggestion &a0)
    address = Rituals.call(
        'ritual_ZN6QQmlSA20FixSuggestionPrivate25createQQmlSAFixSuggestionE'
        'RK19QQmlJSFixSuggestion',
        CuteMixin._valueOf(a0),
    )
    return QQmlSA.FixSuggestion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::FixSuggestionPrivate'

  #  Qt's '~QQmlSA::FixSuggestionPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlSA::FixSuggestionPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA20FixSuggestionPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def location(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlSA::FixSuggestionPrivate::location()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#location

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlSA::FixSuggestionPrivate::location() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA20FixSuggestionPrivate8locationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def description(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::FixSuggestionPrivate::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::FixSuggestionPrivate::description() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA20FixSuggestionPrivate11descriptionEv',
    )

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::FixSuggestionPrivate::fileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::FixSuggestionPrivate::fileName() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA20FixSuggestionPrivate8fileNameEv',
    )

  def isAutoApplicable(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::FixSuggestionPrivate::isAutoApplicable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#isAutoApplicable
    """
    #  bool QQmlSA::FixSuggestionPrivate::isAutoApplicable() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA20FixSuggestionPrivate16isAutoApplicableEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, a0: str) -> None:
    """
    Calls Qt's 'void QQmlSA::FixSuggestionPrivate::setFileName(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#setFileName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSA::FixSuggestionPrivate::setFileName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN6QQmlSA20FixSuggestionPrivate11setFileNameERK7QString', a0,
    )

  @overload()
  @overload(bool)
  def setAutoApplicable(self, autoApplicable: bool = True) -> None:
    """
    Calls Qt's 'void QQmlSA::FixSuggestionPrivate::setAutoApplicable(bool
    autoApplicable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#setAutoApplicable

    Parameters
    ----------

    autoApplicable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlSA::FixSuggestionPrivate::setAutoApplicable(bool
    #      autoApplicable)
    self.uglySide.call(
        'ritual_ZN6QQmlSA20FixSuggestionPrivate17setAutoApplicableEb',
        autoApplicable,
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

  @overload(WAIT['QQmlSA.FixSuggestion'])
  @overload(NoneType)
  def __init__(self, a0: Optional[QQmlSA.FixSuggestion]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html

    Parameters
    ----------

    a0 : Optional[QQmlSA.FixSuggestion]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0)
    self._noteCreation(FixSuggestionPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionE',
        self._addressOf(a0),
    ))

  @overload(WAIT['QQmlSA.FixSuggestion'], THIS)
  @overload(NoneType, THIS)
  def __init__(
      self,
      a0: Optional[QQmlSA.FixSuggestion],
      a1: FixSuggestionPrivate,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0,
    const FixSuggestionPrivate &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html

    Parameters
    ----------

    a0 : Optional[QQmlSA.FixSuggestion]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : FixSuggestionPrivate
      Passed on as a value: Qt reads the C++ QQmlSA::FixSuggestionPrivate,
      which stays Python's own.
    """
    #  QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0,
    #      const FixSuggestionPrivate &a1)
    self._noteCreation(FixSuggestionPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionERKS0_',
        self._addressOf(a0), self._valueOf(a1),
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

  def q_func(self) -> Optional[QQmlSA.FixSuggestion]:
    """
    Calls Qt's 'FixSuggestion *QQmlSA::FixSuggestionPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#q_func

    Returns
    -------

    Optional[QQmlSA.FixSuggestion]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FixSuggestion *QQmlSA::FixSuggestionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA20FixSuggestionPrivate6q_funcEv',
    )
    return QQmlSA.FixSuggestion._cuteAt(address)

  @overload(WAIT['QQmlSA.DocumentEdit'])
  def addDocumentEdit(self, a0: QQmlSA.DocumentEdit) -> None:
    """
    Calls Qt's 'void QQmlSA::FixSuggestionPrivate::addDocumentEdit(const
    DocumentEdit &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-fixsuggestionprivate.html#addDocumentEdit

    Parameters
    ----------

    a0 : QQmlSA.DocumentEdit
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEdit, which
      stays Python's own.
    """
    #  void QQmlSA::FixSuggestionPrivate::addDocumentEdit(const DocumentEdit
    #      &a0)
    self.uglySide.call(
        'ritual_ZN6QQmlSA20FixSuggestionPrivate15addDocumentEditERKNS_12Doc'
        'umentEditE',
        self._valueOf(a0),
    )

  @staticmethod
  def documentEdits(*__, **_) -> Never:
    """
    Qt's 'QList<DocumentEdit> QQmlSA::FixSuggestionPrivate::documentEdits()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.FixSuggestionPrivate.documentEdits' has no cute function "
        "yet. Qt's 'QList<DocumentEdit> "
        "QQmlSA::FixSuggestionPrivate::documentEdits() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def fixSuggestion(*__, **_) -> Never:
    """
    - Qt's 'QQmlJSFixSuggestion
      &QQmlSA::FixSuggestionPrivate::fixSuggestion(QQmlSA::FixSuggestion
      &a0)': takes a type Python has no way to hand over yet.
    - Qt's 'const QQmlJSFixSuggestion
      &QQmlSA::FixSuggestionPrivate::fixSuggestion(const
      QQmlSA::FixSuggestion &a0)': leans on
      'QQmlSA::FixSuggestionPrivate::fixSuggestion(QQmlSA::FixSuggestion
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlSA.FixSuggestionPrivate.fixSuggestion' has no cute function "
        "yet. Qt's 'QQmlJSFixSuggestion "
        "&QQmlSA::FixSuggestionPrivate::fixSuggestion(QQmlSA::FixSuggestion "
        "&a0)': takes a type Python has no way to hand over yet. Qt's "
        "'const QQmlJSFixSuggestion "
        "&QQmlSA::FixSuggestionPrivate::fixSuggestion(const "
        "QQmlSA::FixSuggestion &a0)': leans on "
        "'QQmlSA::FixSuggestionPrivate::fixSuggestion(QQmlSA::FixSuggestion "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
