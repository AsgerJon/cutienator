"""
QOpcUaLocalizedText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcualocalizedtext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QOpcUaLocalizedText(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaLocalizedText: a plain Python object standing
  in front of one C++ QOpcUaLocalizedText.

  C++ hands a QOpcUaLocalizedText around as a copy, so every C++
  QOpcUaLocalizedText behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaLocalizedText that has a ritual and that
  Python can call so far, 6 names in all: '__eq__', 'locale', 'setLocale',
  'text', 'setText', '__rlshift__'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaLocalizedText &QOpcUaLocalizedText::operator=(const
    QOpcUaLocalizedText &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaLocalizedText::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaLocalizedText::~QOpcUaLocalizedText()': the destructor:
    Python removes its C++ QOpcUaLocalizedText by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaLocalizedText is created at the first use, not by
    'QOpcUaLocalizedText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaLocalizedText back gives a copy the ritual made
    for Python, in a new cute QOpcUaLocalizedText.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaLocalizedText'

  #  Qt's '~QOpcUaLocalizedText()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaLocalizedText behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QOpcUaLocalizedTextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def locale(self) -> str:
    """
    Calls Qt's 'QString QOpcUaLocalizedText::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualocalizedtext.html#locale

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaLocalizedText::locale() const
    return self.uglySide.call('ritual_ZNK19QOpcUaLocalizedText6localeEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QOpcUaLocalizedText::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualocalizedtext.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaLocalizedText::text() const
    return self.uglySide.call('ritual_ZNK19QOpcUaLocalizedText4textEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLocale(self, locale: str) -> None:
    """
    Calls Qt's 'void QOpcUaLocalizedText::setLocale(const QString &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualocalizedtext.html#setLocale

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaLocalizedText::setLocale(const QString &locale)
    self.uglySide.call(
        'ritual_ZN19QOpcUaLocalizedText9setLocaleERK7QString', locale,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QOpcUaLocalizedText::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcualocalizedtext.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaLocalizedText::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN19QOpcUaLocalizedText7setTextERK7QString', text,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaLocalizedText) -> bool:
    """
    Calls Qt's 'bool QOpcUaLocalizedText::operator==(const
    QOpcUaLocalizedText &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualocalizedtext.html#operator==

    Parameters
    ----------

    rhs : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  bool QOpcUaLocalizedText::operator==(const QOpcUaLocalizedText &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaLocalizedTexteqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QOpcUaLocalizedText
    &lt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualocalizedtext.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QOpcUaLocalizedText &lt)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QOpcUaLocalizedText',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaLocalizedText::QOpcUaLocalizedText()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualocalizedtext.html#QOpcUaLocalizedText
    """
    #  QOpcUaLocalizedText::QOpcUaLocalizedText()
    self._noteCreation(QOpcUaLocalizedText, lambda: Rituals.call(
        'ritual_ZN19QOpcUaLocalizedTextC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaLocalizedText) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaLocalizedText::QOpcUaLocalizedText(const QOpcUaLocalizedText
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualocalizedtext.html#QOpcUaLocalizedText

    Parameters
    ----------

    a0 : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  QOpcUaLocalizedText::QOpcUaLocalizedText(const QOpcUaLocalizedText
    #      &a0)
    self._noteCreation(QOpcUaLocalizedText, lambda: Rituals.call(
        'ritual_ZN19QOpcUaLocalizedTextC1ERKS_', self._valueOf(a0),
    ))

  @overload(str, str)
  def __init__(self, locale: str, text: str) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaLocalizedText::QOpcUaLocalizedText(const QString &locale, const
    QString &text)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcualocalizedtext.html#QOpcUaLocalizedText

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QOpcUaLocalizedText::QOpcUaLocalizedText(const QString &locale, const
    #      QString &text)
    self._noteCreation(QOpcUaLocalizedText, lambda: Rituals.call(
        'ritual_ZN19QOpcUaLocalizedTextC1ERK7QStringS2_', locale, text,
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


#  Qt's 'QList<QOpcUaLocalizedText>': the list of QOpcUaLocalizedText, which
#  'QList[QOpcUaLocalizedText]' gives. It is made here, so that there is one
#  as soon as there can be a QOpcUaLocalizedText.
QList.createKind(
    QOpcUaLocalizedText, 'value',
    make='ritual_list_make_QOpcUaLocalizedText',
    add='ritual_list_add_QOpcUaLocalizedText',
    size='ritual_list_size_QOpcUaLocalizedText',
    at='ritual_list_at_QOpcUaLocalizedText',
    drop='ritual_list_drop_QOpcUaLocalizedText',
)
