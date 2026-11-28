"""
QQmlSA::DocumentEdit binding of the Qt C++
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
  from typing import Optional


class DocumentEdit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::DocumentEdit: a plain Python object standing
  in front of one C++ QQmlSA::DocumentEdit.

  C++ hands a QQmlSA::DocumentEdit around as a copy, so every C++
  QQmlSA::DocumentEdit behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::DocumentEdit that has a ritual and that
  Python can call so far, 6 names in all: 'd_func', '__eq__', '__ne__',
  'filename', 'location', 'replacement'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const DocumentEditPrivate *QQmlSA::DocumentEdit::d_func() const':
    takes in Python what 'DocumentEditPrivate
    *QQmlSA::DocumentEdit::d_func()' takes.
  - Qt's 'QQmlSA::DocumentEdit::DocumentEdit(DocumentEdit &&a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'DocumentEdit &QQmlSA::DocumentEdit::operator=(const DocumentEdit
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'DocumentEdit &QQmlSA::DocumentEdit::operator=(DocumentEdit &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlSA::DocumentEdit::~DocumentEdit()': the destructor: Python
    removes its C++ QQmlSA::DocumentEdit by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlSA::DocumentEdit is created at the first use, not by
    'QQmlSA::DocumentEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::DocumentEdit back gives a copy the ritual
    made for Python, in a new cute QQmlSA::DocumentEdit.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::DocumentEdit'

  #  Qt's '~QQmlSA::DocumentEdit()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::DocumentEdit behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA12DocumentEditD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def filename(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::DocumentEdit::filename() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-documentedit.html#filename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::DocumentEdit::filename() const
    return self.uglySide.call('ritual_ZNK6QQmlSA12DocumentEdit8filenameEv')

  def location(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlSA::DocumentEdit::location() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-documentedit.html#location

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlSA::DocumentEdit::location() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA12DocumentEdit8locationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def replacement(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::DocumentEdit::replacement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documentedit.html#replacement

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::DocumentEdit::replacement() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA12DocumentEdit11replacementEv',
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

  @overload(THIS)
  def __eq__(self, rhs: DocumentEdit) -> bool:
    """
    Calls Qt's 'bool operator==(const DocumentEdit &lhs, const DocumentEdit
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documentedit.html#operator==

    Parameters
    ----------

    rhs : DocumentEdit
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEdit, which
      stays Python's own.
    """
    #  bool operator==(const DocumentEdit &lhs, const DocumentEdit &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_12DocumentEditES2_',
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
  def __ne__(self, rhs: DocumentEdit) -> bool:
    """
    Calls Qt's 'bool operator!=(const DocumentEdit &lhs, const DocumentEdit
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documentedit.html#operator!=

    Parameters
    ----------

    rhs : DocumentEdit
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEdit, which
      stays Python's own.
    """
    #  bool operator!=(const DocumentEdit &lhs, const DocumentEdit &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_12DocumentEditES2_',
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

  @overload(str, WAIT['QQmlSA.SourceLocation'], str)
  def __init__(
      self,
      filename: str,
      location: QQmlSA.SourceLocation,
      replacement: str,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::DocumentEdit::DocumentEdit(const
    QString &filename, const SourceLocation &location, const QString
    &replacement)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documentedit.html#DocumentEdit

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.

    replacement : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlSA::DocumentEdit::DocumentEdit(const QString &filename, const
    #      SourceLocation &location, const QString &replacement)
    self._noteCreation(DocumentEdit, lambda: Rituals.call(
        'ritual_ZN6QQmlSA12DocumentEditC1ERK7QStringRKNS_14SourceLocationES'
        '3_',
        filename, self._valueOf(location), replacement,
    ))

  @overload(THIS)
  def __init__(self, a0: DocumentEdit) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::DocumentEdit::DocumentEdit(const
    DocumentEdit &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-documentedit.html#DocumentEdit

    Parameters
    ----------

    a0 : DocumentEdit
      Passed on as a value: Qt reads the C++ QQmlSA::DocumentEdit, which
      stays Python's own.
    """
    #  QQmlSA::DocumentEdit::DocumentEdit(const DocumentEdit &a0)
    self._noteCreation(DocumentEdit, lambda: Rituals.call(
        'ritual_ZN6QQmlSA12DocumentEditC1ERKS0_', self._valueOf(a0),
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

  def d_func(self) -> Optional[QQmlSA.DocumentEditPrivate]:
    """
    Calls Qt's 'DocumentEditPrivate *QQmlSA::DocumentEdit::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-documentedit.html#d_func

    Returns
    -------

    Optional[QQmlSA.DocumentEditPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DocumentEditPrivate *QQmlSA::DocumentEdit::d_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA12DocumentEdit6d_funcEv')
    return QQmlSA.DocumentEditPrivate._cuteAt(address)
