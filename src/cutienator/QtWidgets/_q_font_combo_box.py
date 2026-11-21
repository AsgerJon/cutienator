"""
QFontComboBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qfontcombobox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QFontDatabaseWritingSystem
from . import QComboBox, QFontComboBoxFontFilter, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QFont, QFontDatabase
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontComboBox(QComboBox):
  """
  The cute side of Qt's QFontComboBox: a plain Python object standing in
  front of one C++ QFontComboBox.

  It is built on the cute 'QComboBox', as Qt's QFontComboBox is built on Qt's
  QComboBox, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFontComboBox that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'setWritingSystem',
  'writingSystem', 'setFontFilters', 'fontFilters', 'currentFont',
  'sizeHint', 'setSampleTextForSystem', 'sampleTextForSystem',
  'setSampleTextForFont', 'sampleTextForFont', 'setDisplayFont',
  'setCurrentFont'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontComboBox::~QFontComboBox()': the destructor: Python never
    removes a C++ QFontComboBox.

  What has no ritual
  ------------------

  11 of the 27 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template; 1 a signal; 1 protected.

  What to expect
  --------------

  - The C++ QFontComboBox is created at the first use, not by
    'QFontComboBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontComboBox.
  - Qt tells when it has removed the C++ QFontComboBox. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QFontComboBox, and the names Qt has for the
  #  combinations of its flags enums.
  FontFilter = QFontComboBoxFontFilter
  FontFilters = QFontComboBoxFontFilter

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
    Calls Qt's 'QString QFontComboBox::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#tr

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
    #  QString QFontComboBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QFontComboBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontComboBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFontComboBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFontComboBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QFontComboBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def writingSystem(self) -> QFontDatabase.WritingSystem:
    """
    Calls Qt's 'QFontDatabase::WritingSystem QFontComboBox::writingSystem()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#writingSystem

    Returns
    -------

    QFontDatabase.WritingSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFontDatabase.WritingSystem(number)' gives.
    """
    #  QFontDatabase::WritingSystem QFontComboBox::writingSystem() const
    return QFontDatabaseWritingSystem(self.uglySide.call(
        'ritual_ZNK13QFontComboBox13writingSystemEv',
    ))

  def fontFilters(self) -> FontFilters:
    """
    Calls Qt's 'FontFilters QFontComboBox::fontFilters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#fontFilters

    Returns
    -------

    FontFilters
      The value standing for the combination Qt gave back.
    """
    #  FontFilters QFontComboBox::fontFilters() const
    return QFontComboBox.FontFilters(self.uglySide.call(
        'ritual_ZNK13QFontComboBox11fontFiltersEv',
    ))

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QFontComboBox::currentFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFontComboBox::currentFont() const
    address = self.uglySide.call('ritual_ZNK13QFontComboBox11currentFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QFontComboBox::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QFontComboBox::sizeHint() const
    address = self.uglySide.call('ritual_ZNK13QFontComboBox8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QFontDatabaseWritingSystem)
  def sampleTextForSystem(
      self,
      writingSystem: QFontDatabase.WritingSystem,
  ) -> str:
    """
    Calls Qt's 'QString
    QFontComboBox::sampleTextForSystem(QFontDatabase::WritingSystem
    writingSystem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontcombobox.html#sampleTextForSystem

    Parameters
    ----------

    writingSystem : QFontDatabase.WritingSystem
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QFontComboBox::sampleTextForSystem(QFontDatabase::WritingSystem
    #      writingSystem) const
    return self.uglySide.call(
        'ritual_ZNK13QFontComboBox19sampleTextForSystemEN13QFontDatabase13W'
        'ritingSystemE',
        writingSystem.value,
    )

  @overload(str)
  def sampleTextForFont(self, fontFamily: str) -> str:
    """
    Calls Qt's 'QString QFontComboBox::sampleTextForFont(const QString
    &fontFamily) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontcombobox.html#sampleTextForFont

    Parameters
    ----------

    fontFamily : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontComboBox::sampleTextForFont(const QString &fontFamily)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QFontComboBox17sampleTextForFontERK7QString',
        fontFamily,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFontDatabaseWritingSystem)
  def setWritingSystem(self, a0: QFontDatabase.WritingSystem) -> None:
    """
    Calls Qt's 'void
    QFontComboBox::setWritingSystem(QFontDatabase::WritingSystem a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontcombobox.html#setWritingSystem

    Parameters
    ----------

    a0 : QFontDatabase.WritingSystem
      Passed on as its number.
    """
    #  void QFontComboBox::setWritingSystem(QFontDatabase::WritingSystem a0)
    self.uglySide.call(
        'ritual_ZN13QFontComboBox16setWritingSystemEN13QFontDatabase13Writi'
        'ngSystemE',
        a0.value,
    )

  @overload(FontFilters)
  def setFontFilters(self, filters: FontFilters) -> None:
    """
    Calls Qt's 'void QFontComboBox::setFontFilters(FontFilters filters)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#setFontFilters

    Parameters
    ----------

    filters : FontFilters
      Passed on as its number.
    """
    #  void QFontComboBox::setFontFilters(FontFilters filters)
    self.uglySide.call(
        'ritual_ZN13QFontComboBox14setFontFiltersE6QFlagsINS_10FontFilterEE',
        filters.value,
    )

  @overload(QFontDatabaseWritingSystem, str)
  def setSampleTextForSystem(
      self,
      writingSystem: QFontDatabase.WritingSystem,
      sampleText: str,
  ) -> None:
    """
    Calls Qt's 'void
    QFontComboBox::setSampleTextForSystem(QFontDatabase::WritingSystem
    writingSystem, const QString &sampleText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontcombobox.html#setSampleTextForSystem

    Parameters
    ----------

    writingSystem : QFontDatabase.WritingSystem
      Passed on as its number.

    sampleText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      QFontComboBox::setSampleTextForSystem(QFontDatabase::WritingSystem
    #      writingSystem, const QString &sampleText)
    self.uglySide.call(
        'ritual_ZN13QFontComboBox22setSampleTextForSystemEN13QFontDatabase1'
        '3WritingSystemERK7QString',
        writingSystem.value, sampleText,
    )

  @overload(str, str)
  def setSampleTextForFont(self, fontFamily: str, sampleText: str) -> None:
    """
    Calls Qt's 'void QFontComboBox::setSampleTextForFont(const QString
    &fontFamily, const QString &sampleText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontcombobox.html#setSampleTextForFont

    Parameters
    ----------

    fontFamily : str
      Passed on as it is: a QString is made of it for the call.

    sampleText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFontComboBox::setSampleTextForFont(const QString &fontFamily,
    #      const QString &sampleText)
    self.uglySide.call(
        'ritual_ZN13QFontComboBox20setSampleTextForFontERK7QStringS2_',
        fontFamily, sampleText,
    )

  @overload(str, QFont)
  def setDisplayFont(self, fontFamily: str, font: QFont) -> None:
    """
    Calls Qt's 'void QFontComboBox::setDisplayFont(const QString &fontFamily,
    const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#setDisplayFont

    Parameters
    ----------

    fontFamily : str
      Passed on as it is: a QString is made of it for the call.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QFontComboBox::setDisplayFont(const QString &fontFamily, const
    #      QFont &font)
    self.uglySide.call(
        'ritual_ZN13QFontComboBox14setDisplayFontERK7QStringRK5QFont',
        fontFamily, self._valueOf(font),
    )

  @overload(QFont)
  def setCurrentFont(self, f: QFont) -> None:
    """
    Calls Qt's 'void QFontComboBox::setCurrentFont(const QFont &f)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#setCurrentFont

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QFontComboBox::setCurrentFont(const QFont &f)
    self.uglySide.call(
        'ritual_ZN13QFontComboBox14setCurrentFontERK5QFont',
        self._valueOf(f),
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QFontComboBox::QFontComboBox(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#QFontComboBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFontComboBox::QFontComboBox(QWidget *parent)
    self._noteCreation(QFontComboBox, lambda: Rituals.call(
        'ritual_ZN13QFontComboBoxC1EP7QWidget', self._addressOf(parent),
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
