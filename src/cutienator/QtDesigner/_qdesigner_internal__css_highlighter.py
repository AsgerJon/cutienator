"""
qdesigner_internal::CssHighlighter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/csshighlighter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::CssHighlighter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QSyntaxHighlighter
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QTextDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocument = WAIT['QTextDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CssHighlighter(QSyntaxHighlighter):
  """
  The cute side of Qt's qdesigner_internal::CssHighlighter: a plain Python
  object standing in front of one C++ qdesigner_internal::CssHighlighter.

  It is built on the cute 'QSyntaxHighlighter', as Qt's
  qdesigner_internal::CssHighlighter is built on Qt's QSyntaxHighlighter, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::CssHighlighter that has a ritual
  and that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'highlightBlock', 'highlight'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::CssHighlighter::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::CssHighlighter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::CssHighlighter is created at the first use,
    not by 'qdesigner_internal::CssHighlighter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::CssHighlighter.
  - Qt tells when it has removed the C++ qdesigner_internal::CssHighlighter.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString qdesigner_internal::CssHighlighter::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-csshighlighter.html#tr

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
    #  QString qdesigner_internal::CssHighlighter::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14CssHighlighter2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::CssHighlighter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::CssHighlighter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-csshighlighter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::CssHighlighter::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14CssHighlighter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(WAIT['qdesigner_internal.CssHighlightColors'], QTextDocument)
  @overload(WAIT['qdesigner_internal.CssHighlightColors'], NoneType)
  def __init__(
      self,
      colors: qdesigner_internal.CssHighlightColors,
      document: Optional[QTextDocument],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::CssHighlighter::CssHighlighter(const
    CssHighlightColors &colors, QTextDocument *document)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-csshighlighter.html

    Parameters
    ----------

    colors : qdesigner_internal.CssHighlightColors
      Passed on as a value: Qt reads the C++
      qdesigner_internal::CssHighlightColors, which stays Python's own.

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::CssHighlighter::CssHighlighter(const
    #      CssHighlightColors &colors, QTextDocument *document)
    self._noteCreation(CssHighlighter, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal14CssHighlighterC1ERKNS_18CssHighligh'
        'tColorsEP13QTextDocument',
        self._valueOf(colors), self._addressOf(document),
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

  @overload(str)
  def highlightBlock(self, a0: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CssHighlighter::highlightBlock(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-csshighlighter.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::CssHighlighter::highlightBlock(const QString
    #      &a0)
    ritual = (
        'ritual_ZN18qdesigner_internal14CssHighlighter14highlightBlockERK7Q'
        'String')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14CssHighlighter14highlightBloc'
          'kERK7QString')
    self.uglySide.call(ritual, a0)

  @overload(str, int, int, int)
  def highlight(self, a0: str, a1: int, a2: int, a3: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CssHighlighter::highlight(const
    QString &a0, int a1, int a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-csshighlighter.html#highlight

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.
    """
    #  void qdesigner_internal::CssHighlighter::highlight(const QString &a0,
    #      int a1, int a2, int a3)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14CssHighlighter9highlightERK7QString'
        'iii',
        a0, a1, a2, a3,
    )
