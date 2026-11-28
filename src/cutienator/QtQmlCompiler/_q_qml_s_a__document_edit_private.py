"""
QQmlSA::DocumentEditPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::DocumentEditPrivate to be private: it declares the class
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

  from . import QQmlJSDocumentEdit
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSDocumentEdit = WAIT['QQmlJSDocumentEdit']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DocumentEditPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::DocumentEditPrivate: a plain Python object
  standing in front of one C++ QQmlSA::DocumentEditPrivate.

  C++ hands a QQmlSA::DocumentEditPrivate around as a copy, so every C++
  QQmlSA::DocumentEditPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::DocumentEditPrivate that has a ritual and
  that Python can call so far, 6 names in all: 'q_func', 'filename',
  'location', 'replacement', 'documentEdit', 'createQQmlSADocumentEdit'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const DocumentEdit *QQmlSA::DocumentEditPrivate::q_func() const':
    takes in Python what 'DocumentEdit
    *QQmlSA::DocumentEditPrivate::q_func()' takes.
  - Qt's 'QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0,
    DocumentEditPrivate &&a1)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlSA::DocumentEditPrivate::~DocumentEditPrivate()': the
    destructor: Python removes its C++ QQmlSA::DocumentEditPrivate by it, and
    has no other use for it.
  - Qt's 'QList<QQmlJSDocumentEdit>
    QQmlSA::DocumentEditPrivate::documentEdits(const QList<DocumentEdit>
    &edits)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlSA::DocumentEditPrivate is created at the first use, not by
    'QQmlSA::DocumentEditPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::DocumentEditPrivate back gives a copy the
    ritual made for Python, in a new cute QQmlSA::DocumentEditPrivate.
  - Each name of Qt's QQmlSA::DocumentEditPrivate that has no cute function
    yet, 'documentEdits', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QQmlSA.DocumentEdit'])
  def documentEdit(edit: QQmlSA.DocumentEdit) -> QQmlJSDocumentEdit:
    """
    Calls Qt's 'QQmlJSDocumentEdit
    QQmlSA::DocumentEditPrivate::documentEdit(const DocumentEdit &edit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html#documentEdit

    Parameters
    ----------

    edit : QQmlSA.DocumentEdit
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEdit, which
      stays Python's own.

    Returns
    -------

    QQmlJSDocumentEdit
      A new cute QQmlJSDocumentEdit around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSDocumentEdit QQmlSA::DocumentEditPrivate::documentEdit(const
    #      DocumentEdit &edit)
    address = Rituals.call(
        'ritual_ZN6QQmlSA19DocumentEditPrivate12documentEditERKNS_12Documen'
        'tEditE',
        CuteMixin._valueOf(edit),
    )
    from . import QQmlJSDocumentEdit
    return QQmlJSDocumentEdit._cuteOwning(address)

  @staticmethod
  @overload(QQmlJSDocumentEdit)
  def createQQmlSADocumentEdit(
      edit: QQmlJSDocumentEdit,
  ) -> QQmlSA.DocumentEdit:
    """
    Calls Qt's 'DocumentEdit
    QQmlSA::DocumentEditPrivate::createQQmlSADocumentEdit(const
    QQmlJSDocumentEdit &edit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html

    Parameters
    ----------

    edit : QQmlJSDocumentEdit
      Passed on as a value: Qt reads the C++ QQmlJSDocumentEdit, which stays
      Python's own.

    Returns
    -------

    QQmlSA.DocumentEdit
      A new cute QQmlSA::DocumentEdit around the copy Qt gave back. Python
      owns it.
    """
    #  DocumentEdit
    #      QQmlSA::DocumentEditPrivate::createQQmlSADocumentEdit(const
    #      QQmlJSDocumentEdit &edit)
    address = Rituals.call(
        'ritual_ZN6QQmlSA19DocumentEditPrivate24createQQmlSADocumentEditERK'
        '18QQmlJSDocumentEdit',
        CuteMixin._valueOf(edit),
    )
    return QQmlSA.DocumentEdit._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::DocumentEditPrivate'

  #  Qt's '~QQmlSA::DocumentEditPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlSA::DocumentEditPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA19DocumentEditPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def filename(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::DocumentEditPrivate::filename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html#filename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::DocumentEditPrivate::filename() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA19DocumentEditPrivate8filenameEv',
    )

  def location(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlSA::DocumentEditPrivate::location()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html#location

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlSA::DocumentEditPrivate::location() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA19DocumentEditPrivate8locationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def replacement(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::DocumentEditPrivate::replacement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html#replacement

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::DocumentEditPrivate::replacement() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA19DocumentEditPrivate11replacementEv',
    )

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

  @overload(
      WAIT['QQmlSA.DocumentEdit'], str, WAIT['QQmlSA.SourceLocation'], str,
  )
  @overload(NoneType, str, WAIT['QQmlSA.SourceLocation'], str)
  def __init__(
      self,
      a0: Optional[QQmlSA.DocumentEdit],
      filename: str,
      location: QQmlSA.SourceLocation,
      replacement: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0, const
    QString &filename, const SourceLocation &location, const QString
    &replacement)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html

    Parameters
    ----------

    a0 : Optional[QQmlSA.DocumentEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filename : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.

    replacement : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0,
    #      const QString &filename, const SourceLocation &location, const
    #      QString &replacement)
    self._noteCreation(DocumentEditPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditERK7QStr'
        'ingRKNS_14SourceLocationES5_',
        self._addressOf(a0), filename, self._valueOf(location), replacement,
    ))

  @overload(WAIT['QQmlSA.DocumentEdit'], THIS)
  @overload(NoneType, THIS)
  def __init__(
      self,
      a0: Optional[QQmlSA.DocumentEdit],
      a1: DocumentEditPrivate,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0, const
    DocumentEditPrivate &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html

    Parameters
    ----------

    a0 : Optional[QQmlSA.DocumentEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : DocumentEditPrivate
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEditPrivate,
      which stays Python's own.
    """
    #  QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0,
    #      const DocumentEditPrivate &a1)
    self._noteCreation(DocumentEditPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditERKS0_',
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

  def q_func(self) -> Optional[QQmlSA.DocumentEdit]:
    """
    Calls Qt's 'DocumentEdit *QQmlSA::DocumentEditPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documenteditprivate.html#q_func

    Returns
    -------

    Optional[QQmlSA.DocumentEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DocumentEdit *QQmlSA::DocumentEditPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA19DocumentEditPrivate6q_funcEv',
    )
    return QQmlSA.DocumentEdit._cuteAt(address)

  @staticmethod
  def documentEdits(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJSDocumentEdit>
    QQmlSA::DocumentEditPrivate::documentEdits(const QList<DocumentEdit>
    &edits)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.DocumentEditPrivate.documentEdits' has no cute function "
        "yet. Qt's 'QList<QQmlJSDocumentEdit> "
        "QQmlSA::DocumentEditPrivate::documentEdits(const "
        "QList<DocumentEdit> &edits)': takes a type Python has no way to "
        "hand over yet.")
