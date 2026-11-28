"""
QRawFontPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrawfont_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRawFontPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QFont

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QFontEngine, QRawFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QFontEngine = WAIT['QFontEngine']
  QRawFont = WAIT['QRawFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRawFontPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRawFontPrivate: a plain Python object standing in
  front of one C++ QRawFontPrivate.

  C++ hands a QRawFontPrivate around as a copy, so every C++ QRawFontPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRawFontPrivate that has a ritual and that Python
  can call so far, 5 names in all: 'cleanUp', 'isValid', 'setFontEngine',
  'loadFromData', 'get'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRawFontPrivate::~QRawFontPrivate()': the destructor: Python
    removes its C++ QRawFontPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRawFontPrivate is created at the first use, not by
    'QRawFontPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRawFontPrivate back gives a copy the ritual made for
    Python, in a new cute QRawFontPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRawFont)
  def get(font: QRawFont) -> Optional[QRawFontPrivate]:
    """
    Calls Qt's 'QRawFontPrivate *QRawFontPrivate::get(const QRawFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfontprivate.html#get

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    Returns
    -------

    Optional[QRawFontPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRawFontPrivate *QRawFontPrivate::get(const QRawFont &font)
    address = Rituals.call(
        'ritual_ZN15QRawFontPrivate3getERK8QRawFont',
        CuteMixin._valueOf(font),
    )
    return QRawFontPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRawFontPrivate'

  #  Qt's '~QRawFontPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QRawFontPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QRawFontPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRawFontPrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfontprivate.html#isValid
    """
    #  bool QRawFontPrivate::isValid() const
    return self.uglySide.call('ritual_ZNK15QRawFontPrivate7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFontEngine)
  @overload(NoneType)
  def setFontEngine(self, engine: Optional[QFontEngine]) -> None:
    """
    Calls Qt's 'void QRawFontPrivate::setFontEngine(QFontEngine *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfontprivate.html#setFontEngine

    Parameters
    ----------

    engine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRawFontPrivate::setFontEngine(QFontEngine *engine)
    self.uglySide.call(
        'ritual_ZN15QRawFontPrivate13setFontEngineEP11QFontEngine',
        self._addressOf(engine),
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
    Notes what was given, for Qt's 'QRawFontPrivate::QRawFontPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrawfontprivate.html#QRawFontPrivate
    """
    #  QRawFontPrivate::QRawFontPrivate()
    self._noteCreation(QRawFontPrivate, lambda: Rituals.call(
        'ritual_ZN15QRawFontPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QRawFontPrivate) -> None:
    """
    Notes what was given, for Qt's 'QRawFontPrivate::QRawFontPrivate(const
    QRawFontPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrawfontprivate.html#QRawFontPrivate

    Parameters
    ----------

    other : QRawFontPrivate
      Passed on as a value: Qt reads the C++ QRawFontPrivate, which stays
      Python's own.
    """
    #  QRawFontPrivate::QRawFontPrivate(const QRawFontPrivate &other)
    self._noteCreation(QRawFontPrivate, lambda: Rituals.call(
        'ritual_ZN15QRawFontPrivateC1ERKS_', self._valueOf(other),
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

  def cleanUp(self) -> None:
    """
    Calls Qt's 'void QRawFontPrivate::cleanUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfontprivate.html#cleanUp
    """
    #  void QRawFontPrivate::cleanUp()
    self.uglySide.call('ritual_ZN15QRawFontPrivate7cleanUpEv')

  @overload(QByteArray, float, QFont.HintingPreference)
  def loadFromData(
      self,
      fontData: QByteArray,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference,
  ) -> None:
    """
    Calls Qt's 'void QRawFontPrivate::loadFromData(const QByteArray
    &fontData, qreal pixelSize, QFont::HintingPreference hintingPreference)'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfontprivate.html#loadFromData

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    pixelSize : float
      Passed on as it is.

    hintingPreference : QFont.HintingPreference
      Passed on as its number.
    """
    #  void QRawFontPrivate::loadFromData(const QByteArray &fontData, qreal
    #      pixelSize, QFont::HintingPreference hintingPreference)
    self.uglySide.call(
        'ritual_ZN15QRawFontPrivate12loadFromDataERK10QByteArraydN5QFont17H'
        'intingPreferenceE',
        self._valueOf(fontData), pixelSize, hintingPreference.value,
    )
