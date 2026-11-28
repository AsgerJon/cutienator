"""
qdesigner_internal::HtmlHighlighter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/htmlhighlighter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::HtmlHighlighter to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtGui import QSyntaxHighlighter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QTextCharFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextCharFormat = WAIT['QTextCharFormat']


class HtmlHighlighter(QSyntaxHighlighter):
  """
  The cute side of Qt's qdesigner_internal::HtmlHighlighter: a plain Python
  object standing in front of one C++ qdesigner_internal::HtmlHighlighter.

  It is built on the cute 'QSyntaxHighlighter', as Qt's
  qdesigner_internal::HtmlHighlighter is built on Qt's QSyntaxHighlighter,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::HtmlHighlighter that has a
  ritual and that Python can call so far, 4 names in all: 'metaObject',
  'setFormatFor', 'formatFor', 'highlightBlock'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::HtmlHighlighter::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::HtmlHighlighter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 not a gap; 1 leans on
  'qdesigner_internal; 1 leans on 'vtable for qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::HtmlHighlighter is created at the first use,
    not by 'qdesigner_internal::HtmlHighlighter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::HtmlHighlighter.
  - Qt tells when it has removed the C++ qdesigner_internal::HtmlHighlighter.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::HtmlHighlighter that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::HtmlHighlighter, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Construct(CuteNum):
    """
    The enum 'qdesigner_internal::HtmlHighlighter::Construct' of Qt, with the
    6 names Qt gives in it.
    """

    Entity = Kee[int](0)
    Tag = Kee[int](1)
    Comment = Kee[int](2)
    Attribute = Kee[int](3)
    Value = Kee[int](4)
    LastConstruct = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::HtmlHighlighter'

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
    *qdesigner_internal::HtmlHighlighter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-htmlhighlighter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::HtmlHighlighter::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal15HtmlHighlighter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Construct)
  def formatFor(self, construct: Construct) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat
    qdesigner_internal::HtmlHighlighter::formatFor(Construct construct)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-htmlhighlighter.html#formatFor

    Parameters
    ----------

    construct : Construct
      Passed on as its number.

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat
    #      qdesigner_internal::HtmlHighlighter::formatFor(Construct
    #      construct) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal15HtmlHighlighter9formatForENS0_9Con'
        'structE',
        construct.value,
    )
    from ..QtGui import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Construct, QTextCharFormat)
  def setFormatFor(
      self,
      construct: Construct,
      format: QTextCharFormat,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::HtmlHighlighter::setFormatFor(Construct construct,
    const QTextCharFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-htmlhighlighter.html

    Parameters
    ----------

    construct : Construct
      Passed on as its number.

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void qdesigner_internal::HtmlHighlighter::setFormatFor(Construct
    #      construct, const QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15HtmlHighlighter12setFormatForENS0_9'
        'ConstructERK15QTextCharFormat',
        construct.value, self._valueOf(format),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::HtmlHighlighter::HtmlHighlighter(QTextEdit
    *textEdit)': leans on 'vtable for qdesigner_internal::HtmlHighlighter',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.HtmlHighlighter.__init__' has no cute function "
        "yet. Qt's "
        "'qdesigner_internal::HtmlHighlighter::HtmlHighlighter(QTextEdit "
        "*textEdit)': leans on 'vtable for "
        "qdesigner_internal::HtmlHighlighter', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def highlightBlock(self, text: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::HtmlHighlighter::highlightBlock(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-htmlhighlighter.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::HtmlHighlighter::highlightBlock(const QString
    #      &text)
    ritual = (
        'ritual_ZN18qdesigner_internal15HtmlHighlighter14highlightBlockERK7'
        'QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal15HtmlHighlighter14highlightBlo'
          'ckERK7QString')
    self.uglySide.call(ritual, text)
