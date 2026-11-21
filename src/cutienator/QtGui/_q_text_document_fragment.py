"""
QTextDocumentFragment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextdocumentfragment.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QTextDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QTextCursor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextCursor = WAIT['QTextCursor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextDocumentFragment(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextDocumentFragment: a plain Python object standing
  in front of one C++ QTextDocumentFragment.

  C++ hands a QTextDocumentFragment around as a copy, so every C++
  QTextDocumentFragment behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextDocumentFragment that has a ritual and that
  Python can call so far, 8 names in all: 'isEmpty', 'toPlainText',
  'toRawText', 'toHtml', 'toMarkdown', 'fromPlainText', 'fromHtml',
  'fromMarkdown'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextDocumentFragment::~QTextDocumentFragment()': the destructor:
    Python removes its C++ QTextDocumentFragment by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QTextDocumentFragment is created at the first use, not by
    'QTextDocumentFragment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextDocumentFragment back gives a copy the ritual
    made for Python, in a new cute QTextDocumentFragment.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromPlainText(plainText: str) -> QTextDocumentFragment:
    """
    Calls Qt's 'QTextDocumentFragment
    QTextDocumentFragment::fromPlainText(const QString &plainText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#fromPlainText

    Parameters
    ----------

    plainText : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTextDocumentFragment
      A new cute QTextDocumentFragment around the copy Qt gave back. Python
      owns it.
    """
    #  QTextDocumentFragment QTextDocumentFragment::fromPlainText(const
    #      QString &plainText)
    address = Rituals.call(
        'ritual_ZN21QTextDocumentFragment13fromPlainTextERK7QString',
        plainText,
    )
    return QTextDocumentFragment._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, QTextDocument)
  @overload(str, NoneType)
  def fromHtml(
      html: str,
      resourceProvider: Optional[QTextDocument] = None,
  ) -> QTextDocumentFragment:
    """
    Calls Qt's 'QTextDocumentFragment QTextDocumentFragment::fromHtml(const
    QString &html, const QTextDocument *resourceProvider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#fromHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    resourceProvider : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QTextDocumentFragment
      A new cute QTextDocumentFragment around the copy Qt gave back. Python
      owns it.
    """
    #  QTextDocumentFragment QTextDocumentFragment::fromHtml(const QString
    #      &html, const QTextDocument *resourceProvider)
    address = Rituals.call(
        'ritual_ZN21QTextDocumentFragment8fromHtmlERK7QStringPK13QTextDocum'
        'ent',
        html, CuteMixin._addressOf(resourceProvider),
    )
    return QTextDocumentFragment._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, QTextDocument.MarkdownFeatures)
  def fromMarkdown(
      markdown: str,
      features: QTextDocument.MarkdownFeatures = (
          QTextDocument.MarkdownFeatures.MarkdownDialectGitHub),
  ) -> QTextDocumentFragment:
    """
    Calls Qt's 'QTextDocumentFragment
    QTextDocumentFragment::fromMarkdown(const QString &markdown,
    QTextDocument::MarkdownFeatures features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#fromMarkdown

    Parameters
    ----------

    markdown : str
      Passed on as it is: a QString is made of it for the call.

    features : QTextDocument.MarkdownFeatures
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.MarkdownFeatures.MarkdownDialectGitHub.

    Returns
    -------

    QTextDocumentFragment
      A new cute QTextDocumentFragment around the copy Qt gave back. Python
      owns it.
    """
    #  QTextDocumentFragment QTextDocumentFragment::fromMarkdown(const
    #      QString &markdown, QTextDocument::MarkdownFeatures features)
    address = Rituals.call(
        'ritual_ZN21QTextDocumentFragment12fromMarkdownERK7QString6QFlagsIN'
        '13QTextDocument15MarkdownFeatureEE',
        markdown, features.value,
    )
    return QTextDocumentFragment._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextDocumentFragment'

  #  Qt's '~QTextDocumentFragment()'. Naming it makes this a value class:
  #  Python owns every C++ QTextDocumentFragment behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QTextDocumentFragmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentFragment::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentfragment.html#isEmpty
    """
    #  bool QTextDocumentFragment::isEmpty() const
    return self.uglySide.call('ritual_ZNK21QTextDocumentFragment7isEmptyEv')

  def toPlainText(self) -> str:
    """
    Calls Qt's 'QString QTextDocumentFragment::toPlainText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#toPlainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocumentFragment::toPlainText() const
    return self.uglySide.call(
        'ritual_ZNK21QTextDocumentFragment11toPlainTextEv',
    )

  def toRawText(self) -> str:
    """
    Calls Qt's 'QString QTextDocumentFragment::toRawText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#toRawText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocumentFragment::toRawText() const
    return self.uglySide.call(
        'ritual_ZNK21QTextDocumentFragment9toRawTextEv',
    )

  def toHtml(self) -> str:
    """
    Calls Qt's 'QString QTextDocumentFragment::toHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentfragment.html#toHtml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocumentFragment::toHtml() const
    return self.uglySide.call('ritual_ZNK21QTextDocumentFragment6toHtmlEv')

  @overload()
  @overload(QTextDocument.MarkdownFeatures)
  def toMarkdown(
      self,
      features: QTextDocument.MarkdownFeatures = (
          QTextDocument.MarkdownFeatures.MarkdownDialectGitHub),
  ) -> str:
    """
    Calls Qt's 'QString
    QTextDocumentFragment::toMarkdown(QTextDocument::MarkdownFeatures
    features) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#toMarkdown

    Parameters
    ----------

    features : QTextDocument.MarkdownFeatures
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.MarkdownFeatures.MarkdownDialectGitHub.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QTextDocumentFragment::toMarkdown(QTextDocument::MarkdownFeatures
    #      features) const
    return self.uglySide.call(
        'ritual_ZNK21QTextDocumentFragment10toMarkdownE6QFlagsIN13QTextDocu'
        'ment15MarkdownFeatureEE',
        features.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QTextDocumentFragment::QTextDocumentFragment()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#QTextDocumentFragment
    """
    #  QTextDocumentFragment::QTextDocumentFragment()
    self._noteCreation(QTextDocumentFragment, lambda: Rituals.call(
        'ritual_ZN21QTextDocumentFragmentC1Ev',
    ))

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, document: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's
    'QTextDocumentFragment::QTextDocumentFragment(const QTextDocument
    *document)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#QTextDocumentFragment

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextDocumentFragment::QTextDocumentFragment(const QTextDocument
    #      *document)
    self._noteCreation(QTextDocumentFragment, lambda: Rituals.call(
        'ritual_ZN21QTextDocumentFragmentC1EPK13QTextDocument',
        self._addressOf(document),
    ))

  @overload(QTextCursor)
  def __init__(self, range: QTextCursor) -> None:
    """
    Notes what was given, for Qt's
    'QTextDocumentFragment::QTextDocumentFragment(const QTextCursor &range)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#QTextDocumentFragment

    Parameters
    ----------

    range : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  QTextDocumentFragment::QTextDocumentFragment(const QTextCursor &range)
    self._noteCreation(QTextDocumentFragment, lambda: Rituals.call(
        'ritual_ZN21QTextDocumentFragmentC1ERK11QTextCursor',
        self._valueOf(range),
    ))

  @overload(THIS)
  def __init__(self, rhs: QTextDocumentFragment) -> None:
    """
    Notes what was given, for Qt's
    'QTextDocumentFragment::QTextDocumentFragment(const QTextDocumentFragment
    &rhs)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentfragment.html#QTextDocumentFragment

    Parameters
    ----------

    rhs : QTextDocumentFragment
      Passed on as a value: Qt reads the C++ QTextDocumentFragment, which
      stays Python's own.
    """
    #  QTextDocumentFragment::QTextDocumentFragment(const
    #      QTextDocumentFragment &rhs)
    self._noteCreation(QTextDocumentFragment, lambda: Rituals.call(
        'ritual_ZN21QTextDocumentFragmentC1ERKS_', self._valueOf(rhs),
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
