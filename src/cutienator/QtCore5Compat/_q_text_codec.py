"""
QTextCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qtextcodec.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringConverterBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QChar
  from . import QTextDecoder, QTextEncoder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextCodec(QStringConverterBase):
  """
  The cute side of Qt's QTextCodec: a plain Python object standing in front
  of one C++ QTextCodec.

  It is built on the cute 'QStringConverterBase', as Qt's QTextCodec is built
  on Qt's QStringConverterBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextCodec that has a ritual and that Python can
  call so far, 16 names in all: 'codecForName', 'codecForMib',
  'availableCodecs', 'codecForLocale', 'setCodecForLocale', 'codecForTr',
  'codecForHtml', 'codecForUtfText', 'canEncode', 'toUnicode', 'fromUnicode',
  'makeDecoder', 'makeEncoder', 'name', 'aliases', 'mibEnum'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> QTextCodec::availableMibs()': gives a type Python has no
    way to take yet.
  - Qt's 'bool QTextCodec::canEncode(QStringView a0) const': takes in Python
    what 'bool QTextCodec::canEncode(const QString &a0) const' takes.
  - Qt's 'QByteArray QTextCodec::fromUnicode(QStringView uc) const': takes in
    Python what 'QByteArray QTextCodec::fromUnicode(const QString &uc) const'
    takes.
  - Qt's 'QString QTextCodec::toUnicode(const char *in, int length,
    ConverterState *state) const': names 'QTextCodec::ConverterState', which
    has no cute class yet.
  - Qt's 'QByteArray QTextCodec::fromUnicode(const QChar *in, int length,
    ConverterState *state) const': names 'QTextCodec::ConverterState', which
    has no cute class yet.
  - Qt's 'QString QTextCodec::convertToUnicode(const char *in, int length,
    ConverterState *state) const': names 'QTextCodec::ConverterState', which
    has no cute class yet.
  - Qt's 'QByteArray QTextCodec::convertFromUnicode(const QChar *in, int
    length, ConverterState *state) const': names
    'QTextCodec::ConverterState', which has no cute class yet.
  - Qt's 'QTextCodec::~QTextCodec()': the destructor: Python never removes a
    C++ QTextCodec.

  What has no ritual
  ------------------

  3 of the 32 functions Qt declares: 2 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QTextCodec is created at the first use, not by 'QTextCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextCodec.
  - Each name of Qt's QTextCodec that has no cute function yet, '__init__',
    'availableMibs', 'convertFromUnicode', 'convertToUnicode', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray)
  def codecForName(name: QByteArray) -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForName(const QByteArray
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForName(const QByteArray &name)
    address = Rituals.call(
        'ritual_ZN10QTextCodec12codecForNameERK10QByteArray',
        CuteMixin._valueOf(name),
    )
    return QTextCodec._cuteAt(address)

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def codecForName(name: Optional[str]) -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForName(const char *name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForName

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForName(const char *name)
    address = Rituals.call(
        'ritual_ZN10QTextCodec12codecForNameEPKc', CuteMixin._bytesOf(name),
    )
    return QTextCodec._cuteAt(address)

  @staticmethod
  @overload(int)
  def codecForMib(mib: int) -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForMib(int mib)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForMib

    Parameters
    ----------

    mib : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForMib(int mib)
    address = Rituals.call('ritual_ZN10QTextCodec11codecForMibEi', mib)
    return QTextCodec._cuteAt(address)

  @staticmethod
  def availableCodecs() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QTextCodec::availableCodecs()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#availableCodecs

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QTextCodec::availableCodecs()
    address = Rituals.call('ritual_ZN10QTextCodec15availableCodecsEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def codecForLocale() -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForLocale()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForLocale

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForLocale()
    address = Rituals.call('ritual_ZN10QTextCodec14codecForLocaleEv')
    return QTextCodec._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def setCodecForLocale(c: Optional[QTextCodec]) -> None:
    """
    Calls Qt's 'void QTextCodec::setCodecForLocale(QTextCodec *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#setCodecForLocale

    Parameters
    ----------

    c : Optional[QTextCodec]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextCodec::setCodecForLocale(QTextCodec *c)
    Rituals.call(
        'ritual_ZN10QTextCodec17setCodecForLocaleEPS_',
        CuteMixin._addressOf(c),
    )

  @staticmethod
  def codecForTr() -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForTr()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForTr

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForTr()
    address = Rituals.call('ritual_ZN10QTextCodec10codecForTrEv')
    return QTextCodec._cuteAt(address)

  @staticmethod
  @overload(QByteArray)
  def codecForHtml(ba: QByteArray) -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForHtml(const QByteArray &ba)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForHtml

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForHtml(const QByteArray &ba)
    address = Rituals.call(
        'ritual_ZN10QTextCodec12codecForHtmlERK10QByteArray',
        CuteMixin._valueOf(ba),
    )
    return QTextCodec._cuteAt(address)

  @staticmethod
  @overload(QByteArray, THIS)
  @overload(QByteArray, NoneType)
  def codecForHtml(
      ba: QByteArray,
      defaultCodec: Optional[QTextCodec],
  ) -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForHtml(const QByteArray &ba,
    QTextCodec *defaultCodec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForHtml

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    defaultCodec : Optional[QTextCodec]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForHtml(const QByteArray &ba, QTextCodec
    #      *defaultCodec)
    address = Rituals.call(
        'ritual_ZN10QTextCodec12codecForHtmlERK10QByteArrayPS_',
        CuteMixin._valueOf(ba), CuteMixin._addressOf(defaultCodec),
    )
    return QTextCodec._cuteAt(address)

  @staticmethod
  @overload(QByteArray)
  def codecForUtfText(ba: QByteArray) -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForUtfText(const QByteArray
    &ba)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForUtfText

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForUtfText(const QByteArray &ba)
    address = Rituals.call(
        'ritual_ZN10QTextCodec15codecForUtfTextERK10QByteArray',
        CuteMixin._valueOf(ba),
    )
    return QTextCodec._cuteAt(address)

  @staticmethod
  @overload(QByteArray, THIS)
  @overload(QByteArray, NoneType)
  def codecForUtfText(
      ba: QByteArray,
      defaultCodec: Optional[QTextCodec],
  ) -> Optional[QTextCodec]:
    """
    Calls Qt's 'QTextCodec *QTextCodec::codecForUtfText(const QByteArray &ba,
    QTextCodec *defaultCodec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#codecForUtfText

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    defaultCodec : Optional[QTextCodec]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTextCodec]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCodec *QTextCodec::codecForUtfText(const QByteArray &ba,
    #      QTextCodec *defaultCodec)
    address = Rituals.call(
        'ritual_ZN10QTextCodec15codecForUtfTextERK10QByteArrayPS_',
        CuteMixin._valueOf(ba), CuteMixin._addressOf(defaultCodec),
    )
    return QTextCodec._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextCodec'

  #  A C++ QTextCodec Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextCodec'

  #  The functions Qt calls itself that QTextCodec is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'aliases': (
          'QList<QByteArray> QTextCodec::aliases() const',
      ),
      'convertToUnicode': (
          'QString QTextCodec::convertToUnicode(const char *, int, '
          'ConverterState *) const',
      ),
      'convertFromUnicode': (
          'QByteArray QTextCodec::convertFromUnicode(const QChar *, int, '
          'ConverterState *) const',
      ),
  }

  #  The functions Qt calls itself that QTextCodec is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK10QTextCodec4nameEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'mibEnum': (
          ('_ZNK10QTextCodec7mibEnumEv',
           ('int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QChar)
  def canEncode(self, a0: QChar) -> bool:
    """
    Calls Qt's 'bool QTextCodec::canEncode(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#canEncode

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QTextCodec::canEncode(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK10QTextCodec9canEncodeE5QChar', self._valueOf(a0),
    )

  @overload(str)
  def canEncode(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QTextCodec::canEncode(const QString &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#canEncode

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QTextCodec::canEncode(const QString &a0) const
    return self.uglySide.call(
        'ritual_ZNK10QTextCodec9canEncodeERK7QString', a0,
    )

  @overload(QByteArray)
  def toUnicode(self, a0: QByteArray) -> str:
    """
    Calls Qt's 'QString QTextCodec::toUnicode(const QByteArray &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#toUnicode

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextCodec::toUnicode(const QByteArray &a0) const
    return self.uglySide.call(
        'ritual_ZNK10QTextCodec9toUnicodeERK10QByteArray', self._valueOf(a0),
    )

  @overload(str)
  @overload(NoneType)
  def toUnicode(self, chars: Optional[str]) -> str:
    """
    Calls Qt's 'QString QTextCodec::toUnicode(const char *chars) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#toUnicode

    Parameters
    ----------

    chars : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextCodec::toUnicode(const char *chars) const
    return self.uglySide.call(
        'ritual_ZNK10QTextCodec9toUnicodeEPKc', self._bytesOf(chars),
    )

  @overload(str)
  def fromUnicode(self, uc: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextCodec::fromUnicode(const QString &uc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#fromUnicode

    Parameters
    ----------

    uc : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextCodec::fromUnicode(const QString &uc) const
    address = self.uglySide.call(
        'ritual_ZNK10QTextCodec11fromUnicodeERK7QString', uc,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QStringConverterBase.Flags)
  def makeDecoder(
      self,
      flags: QStringConverterBase.Flags,
  ) -> Optional[QTextDecoder]:
    """
    Calls Qt's 'QTextDecoder *QTextCodec::makeDecoder(ConversionFlags flags)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#makeDecoder

    Parameters
    ----------

    flags : QStringConverterBase.Flags
      Passed on as its number.

    Returns
    -------

    Optional[QTextDecoder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDecoder *QTextCodec::makeDecoder(ConversionFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNK10QTextCodec11makeDecoderE6QFlagsIN20QStringConverterBas'
        'e4FlagEE',
        flags.value,
    )
    from . import QTextDecoder
    return QTextDecoder._cuteAt(address)

  @overload(QStringConverterBase.Flags)
  def makeEncoder(
      self,
      flags: QStringConverterBase.Flags,
  ) -> Optional[QTextEncoder]:
    """
    Calls Qt's 'QTextEncoder *QTextCodec::makeEncoder(ConversionFlags flags)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#makeEncoder

    Parameters
    ----------

    flags : QStringConverterBase.Flags
      Passed on as its number.

    Returns
    -------

    Optional[QTextEncoder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextEncoder *QTextCodec::makeEncoder(ConversionFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNK10QTextCodec11makeEncoderE6QFlagsIN20QStringConverterBas'
        'e4FlagEE',
        flags.value,
    )
    from . import QTextEncoder
    return QTextEncoder._cuteAt(address)

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextCodec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextCodec::name() const
    address = self.uglySide.call('ritual_ZNK10QTextCodec4nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def aliases(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QTextCodec::aliases() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QTextCodec::aliases() const
    address = self.uglySide.call('ritual_ZNK10QTextCodec7aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QTextCodec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcodec.html#mibEnum
    """
    #  int QTextCodec::mibEnum() const
    return self.uglySide.call('ritual_ZNK10QTextCodec7mibEnumEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QTextCodec::QTextCodec()': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'QTextCodec.__init__' has no cute function yet. Qt's "
        "'QTextCodec::QTextCodec()': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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
  def availableMibs(*__, **_) -> Never:
    """
    Qt's 'QList<int> QTextCodec::availableMibs()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QTextCodec.availableMibs' has no cute function yet. Qt's "
        "'QList<int> QTextCodec::availableMibs()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def convertFromUnicode(*__, **_) -> Never:
    """
    Qt's 'QByteArray QTextCodec::convertFromUnicode(const QChar *in, int
    length, ConverterState *state) const': names
    'QTextCodec::ConverterState', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextCodec.convertFromUnicode' has no cute function yet. Qt's "
        "'QByteArray QTextCodec::convertFromUnicode(const QChar *in, int "
        "length, ConverterState *state) const': names "
        "'QTextCodec::ConverterState', which has no cute class yet.")

  @staticmethod
  def convertToUnicode(*__, **_) -> Never:
    """
    Qt's 'QString QTextCodec::convertToUnicode(const char *in, int length,
    ConverterState *state) const': names 'QTextCodec::ConverterState', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextCodec.convertToUnicode' has no cute function yet. Qt's "
        "'QString QTextCodec::convertToUnicode(const char *in, int length, "
        "ConverterState *state) const': names 'QTextCodec::ConverterState', "
        "which has no cute class yet.")
