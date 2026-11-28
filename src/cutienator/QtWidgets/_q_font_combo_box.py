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

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtGui import QFontDatabase
from . import QComboBox, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
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
  call so far, 16 names in all: 'metaObject', 'tr', 'setWritingSystem',
  'writingSystem', 'setFontFilters', 'fontFilters', 'currentFont',
  'sizeHint', 'setSampleTextForSystem', 'sampleTextForSystem',
  'setSampleTextForFont', 'sampleTextForFont', 'setDisplayFont',
  'setCurrentFont', 'currentFontChanged', 'event'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFontComboBox::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QFontComboBox::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QFontComboBox::~QFontComboBox()': the destructor: Python never
    removes a C++ QFontComboBox.
  - Qt's 'std::optional<QFont> QFontComboBox::displayFont(const QString
    &fontFamily) const': gives a type Python has no way to take yet.
  - Qt's 'QFontComboBoxPrivate *QFontComboBox::d_func()': gives
    'QFontComboBoxPrivate', which has no cute class yet.
  - Qt's 'const QFontComboBoxPrivate *QFontComboBox::d_func() const': gives
    'QFontComboBoxPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

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
  - Each name of Qt's QFontComboBox that has no cute function yet,
    'displayFont', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QFontComboBox, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FontFilter(CuteFlags):
    """
    The flags enum 'QFontComboBox::FontFilter' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QFontComboBox::FontFilters'.
    """

    AllFonts = 0x0
    ScalableFonts = 0x1
    NonScalableFonts = 0x2
    MonospacedFonts = 0x4
    ProportionalFonts = 0x8

  FontFilters = FontFilter

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

  #  A C++ QFontComboBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontComboBox'

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
    return QFontDatabase.WritingSystem(self.uglySide.call(
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
    ritual = 'ritual_ZNK13QFontComboBox8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFontComboBox8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QFontDatabase.WritingSystem)
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

  @overload(QFontDatabase.WritingSystem)
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

  @overload(QFontDatabase.WritingSystem, str)
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

  @overload(QFont)
  def currentFontChanged(self, f: QFont) -> None:
    """
    Calls Qt's 'void QFontComboBox::currentFontChanged(const QFont &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontcombobox.html#currentFontChanged

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QFontComboBox::currentFontChanged(const QFont &f)
    self.uglySide.call(
        'ritual_ZN13QFontComboBox18currentFontChangedERK5QFont',
        self._valueOf(f),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QFontComboBox::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcombobox.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFontComboBox::event(QEvent *e)
    ritual = 'ritual_ZN13QFontComboBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFontComboBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def displayFont(*__, **_) -> Never:
    """
    Qt's 'std::optional<QFont> QFontComboBox::displayFont(const QString
    &fontFamily) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFontComboBox.displayFont' has no cute function yet. Qt's "
        "'std::optional<QFont> QFontComboBox::displayFont(const QString "
        "&fontFamily) const': gives a type Python has no way to take yet.")
