"""
QQmlJS::Export binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscope_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJS::Export to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QTypeRevision


class Export(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::Export: a plain Python object standing in
  front of one C++ QQmlJS::Export.

  C++ hands a QQmlJS::Export around as a copy, so every C++ QQmlJS::Export
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::Export that has a ritual and that Python can
  call so far, 4 names in all: 'package', 'type', 'version', 'revision'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::Export::~Export()': the destructor: Python removes its C++
    QQmlJS::Export by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlJS::Export is created at the first use, not by
    'QQmlJS::Export(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::Export back gives a copy the ritual made for
    Python, in a new cute QQmlJS::Export.
  - Each name of Qt's QQmlJS::Export that has no cute function yet,
    'isValid', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::Export'

  #  Qt's '~QQmlJS::Export()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJS::Export behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS6ExportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def package(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::Export::package() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-export.html#package

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::Export::package() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Export7packageEv')

  def type(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::Export::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-export.html#type

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::Export::type() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Export4typeEv')

  def version(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlJS::Export::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-export.html#version

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlJS::Export::version() const
    address = self.uglySide.call('ritual_ZNK6QQmlJS6Export7versionEv')
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def revision(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlJS::Export::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-export.html#revision

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlJS::Export::revision() const
    address = self.uglySide.call('ritual_ZNK6QQmlJS6Export8revisionEv')
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

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
    Notes what was given, for Qt's 'QQmlJS::Export::Export()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-export.html#Export
    """
    #  QQmlJS::Export::Export()
    self._noteCreation(Export, lambda: Rituals.call(
        'ritual_ZN6QQmlJS6ExportC1Ev',
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
  def isValid(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJS::Export::isValid() const': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlJS.Export.isValid' has no cute function yet. Qt's 'bool "
        "QQmlJS::Export::isValid() const': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
