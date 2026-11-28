"""
QFontPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QFontPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QFont

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFontEngine

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontPrivate: a plain Python object standing in front
  of one C++ QFontPrivate.

  C++ hands a QFontPrivate around as a copy, so every C++ QFontPrivate behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontPrivate that has a ritual and that Python can
  call so far, 12 names in all: 'engineForScript', 'engineForCharacter',
  'smallCapsFont', 'smallCapsFontPrivate', 'get', 'resolve',
  'detachButKeepEngineData', 'setFeature', 'unsetFeature', 'setVariableAxis',
  'unsetVariableAxis', 'hasVariableAxis'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontPrivate::~QFontPrivate()': the destructor: Python removes its
    C++ QFontPrivate by it, and has no other use for it.
  - Qt's 'void QFontPrivate::alterCharForCapitalization(QChar &c) const':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QFontPrivate is created at the first use, not by
    'QFontPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontPrivate back gives a copy the ritual made for
    Python, in a new cute QFontPrivate.
  - Each name of Qt's QFontPrivate that has no cute function yet,
    'alterCharForCapitalization', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFontPrivate, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class EngineQueryOption(CuteFlags, scoped=True):
    """
    The flags enum 'QFontPrivate::EngineQueryOption' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QFontPrivate::EngineQueryOptions'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Default = 0x0
    IgnoreSmallCapsEngine = 0x1

  EngineQueryOptions = EngineQueryOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QFont)
  def get(font: QFont) -> Optional[QFontPrivate]:
    """
    Calls Qt's 'QFontPrivate *QFontPrivate::get(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#get

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    Returns
    -------

    Optional[QFontPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontPrivate *QFontPrivate::get(const QFont &font)
    address = Rituals.call(
        'ritual_ZN12QFontPrivate3getERK5QFont', CuteMixin._valueOf(font),
    )
    return QFontPrivate._cuteAt(address)

  @staticmethod
  @overload(QFont)
  @overload(NoneType)
  def detachButKeepEngineData(font: Optional[QFont]) -> None:
    """
    Calls Qt's 'void QFontPrivate::detachButKeepEngineData(QFont *font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontprivate.html#detachButKeepEngineData

    Parameters
    ----------

    font : Optional[QFont]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFontPrivate::detachButKeepEngineData(QFont *font)
    Rituals.call(
        'ritual_ZN12QFontPrivate23detachButKeepEngineDataEP5QFont',
        CuteMixin._addressOf(font),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontPrivate'

  #  Qt's '~QFontPrivate()'. Naming it makes this a value class: Python owns
  #  every C++ QFontPrivate behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QFontPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def engineForScript(self, script: int) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontPrivate::engineForScript(int script)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#engineForScript

    Parameters
    ----------

    script : int
      Passed on as it is.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontPrivate::engineForScript(int script) const
    address = self.uglySide.call(
        'ritual_ZNK12QFontPrivate15engineForScriptEi', script,
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  @overload(int)
  @overload(int, EngineQueryOptions)
  def engineForCharacter(
      self,
      c: int,
      opt: EngineQueryOptions = EngineQueryOptions(),
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontPrivate::engineForCharacter(char32_t c,
    EngineQueryOptions opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontprivate.html#engineForCharacter

    Parameters
    ----------

    c : int
      Passed on as it is.

    opt : EngineQueryOptions
      Passed on as its number. May be left out, as in Qt: it is then
      EngineQueryOptions().

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontPrivate::engineForCharacter(char32_t c,
    #      EngineQueryOptions opt) const
    address = self.uglySide.call(
        'ritual_ZNK12QFontPrivate18engineForCharacterEDi6QFlagsINS_17Engine'
        'QueryOptionEE',
        c, opt.value,
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  def smallCapsFont(self) -> QFont:
    """
    Calls Qt's 'QFont QFontPrivate::smallCapsFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#smallCapsFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFontPrivate::smallCapsFont() const
    address = self.uglySide.call('ritual_ZNK12QFontPrivate13smallCapsFontEv')
    return QFont._cuteOwning(address)

  def smallCapsFontPrivate(self) -> Optional[QFontPrivate]:
    """
    Calls Qt's 'QFontPrivate *QFontPrivate::smallCapsFontPrivate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontprivate.html#smallCapsFontPrivate

    Returns
    -------

    Optional[QFontPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontPrivate *QFontPrivate::smallCapsFontPrivate() const
    address = self.uglySide.call(
        'ritual_ZNK12QFontPrivate20smallCapsFontPrivateEv',
    )
    return QFontPrivate._cuteAt(address)

  @overload(QFont.Tag, float)
  def hasVariableAxis(self, tag: QFont.Tag, value: float) -> bool:
    """
    Calls Qt's 'bool QFontPrivate::hasVariableAxis(QFont::Tag tag, float
    value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#hasVariableAxis

    Parameters
    ----------

    tag : QFont.Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.

    value : float
      Passed on as it is.
    """
    #  bool QFontPrivate::hasVariableAxis(QFont::Tag tag, float value) const
    return self.uglySide.call(
        'ritual_ZNK12QFontPrivate15hasVariableAxisEN5QFont3TagEf',
        self._valueOf(tag), value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont.Tag, int)
  def setFeature(self, tag: QFont.Tag, value: int) -> None:
    """
    Calls Qt's 'void QFontPrivate::setFeature(QFont::Tag tag, quint32
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#setFeature

    Parameters
    ----------

    tag : QFont.Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.

    value : int
      Passed on as it is.
    """
    #  void QFontPrivate::setFeature(QFont::Tag tag, quint32 value)
    self.uglySide.call(
        'ritual_ZN12QFontPrivate10setFeatureEN5QFont3TagEj',
        self._valueOf(tag), value,
    )

  @overload(QFont.Tag, float)
  def setVariableAxis(self, tag: QFont.Tag, value: float) -> None:
    """
    Calls Qt's 'void QFontPrivate::setVariableAxis(QFont::Tag tag, float
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#setVariableAxis

    Parameters
    ----------

    tag : QFont.Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.

    value : float
      Passed on as it is.
    """
    #  void QFontPrivate::setVariableAxis(QFont::Tag tag, float value)
    self.uglySide.call(
        'ritual_ZN12QFontPrivate15setVariableAxisEN5QFont3TagEf',
        self._valueOf(tag), value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFontPrivate::QFontPrivate()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#QFontPrivate
    """
    #  QFontPrivate::QFontPrivate()
    self._noteCreation(QFontPrivate, lambda: Rituals.call(
        'ritual_ZN12QFontPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QFontPrivate) -> None:
    """
    Notes what was given, for Qt's 'QFontPrivate::QFontPrivate(const
    QFontPrivate &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#QFontPrivate

    Parameters
    ----------

    other : QFontPrivate
      Passed on as a value: Qt reads the C++ QFontPrivate, which stays
      Python's own.
    """
    #  QFontPrivate::QFontPrivate(const QFontPrivate &other)
    self._noteCreation(QFontPrivate, lambda: Rituals.call(
        'ritual_ZN12QFontPrivateC1ERKS_', self._valueOf(other),
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

  @overload(int, THIS)
  @overload(int, NoneType)
  def resolve(self, mask: int, other: Optional[QFontPrivate]) -> None:
    """
    Calls Qt's 'void QFontPrivate::resolve(uint mask, const QFontPrivate
    *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#resolve

    Parameters
    ----------

    mask : int
      Passed on as it is.

    other : Optional[QFontPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFontPrivate::resolve(uint mask, const QFontPrivate *other)
    self.uglySide.call(
        'ritual_ZN12QFontPrivate7resolveEjPKS_',
        mask, self._addressOf(other),
    )

  @overload(QFont.Tag)
  def unsetFeature(self, tag: QFont.Tag) -> None:
    """
    Calls Qt's 'void QFontPrivate::unsetFeature(QFont::Tag tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontprivate.html#unsetFeature

    Parameters
    ----------

    tag : QFont.Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  void QFontPrivate::unsetFeature(QFont::Tag tag)
    self.uglySide.call(
        'ritual_ZN12QFontPrivate12unsetFeatureEN5QFont3TagE',
        self._valueOf(tag),
    )

  @overload(QFont.Tag)
  def unsetVariableAxis(self, tag: QFont.Tag) -> None:
    """
    Calls Qt's 'void QFontPrivate::unsetVariableAxis(QFont::Tag tag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontprivate.html#unsetVariableAxis

    Parameters
    ----------

    tag : QFont.Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  void QFontPrivate::unsetVariableAxis(QFont::Tag tag)
    self.uglySide.call(
        'ritual_ZN12QFontPrivate17unsetVariableAxisEN5QFont3TagE',
        self._valueOf(tag),
    )

  @staticmethod
  def alterCharForCapitalization(*__, **_) -> Never:
    """
    Qt's 'void QFontPrivate::alterCharForCapitalization(QChar &c) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFontPrivate.alterCharForCapitalization' has no cute function "
        "yet. Qt's 'void QFontPrivate::alterCharForCapitalization(QChar &c) "
        "const': takes a type Python has no way to hand over yet.")
