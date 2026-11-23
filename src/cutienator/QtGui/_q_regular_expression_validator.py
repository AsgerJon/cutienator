"""
QRegularExpressionValidator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QValidator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRegularExpression
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRegularExpression = WAIT['QRegularExpression']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRegularExpressionValidator(QValidator):
  """
  The cute side of Qt's QRegularExpressionValidator: a plain Python object
  standing in front of one C++ QRegularExpressionValidator.

  It is built on the cute 'QValidator', as Qt's QRegularExpressionValidator
  is built on Qt's QValidator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRegularExpressionValidator that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'regularExpression', 'setRegularExpression'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRegularExpressionValidator::~QRegularExpressionValidator()': the
    destructor: Python never removes a C++ QRegularExpressionValidator.

  What has no ritual
  ------------------

  10 of the 17 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QRegularExpressionValidator is created at the first use, not by
    'QRegularExpressionValidator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRegularExpressionValidator.
  - Qt tells when it has removed the C++ QRegularExpressionValidator. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QRegularExpressionValidator::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionvalidator.html#tr

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
    #  QString QRegularExpressionValidator::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QRegularExpressionValidator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRegularExpressionValidator'

  #  A C++ QRegularExpressionValidator Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRegularExpressionValidator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRegularExpressionValidator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionvalidator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRegularExpressionValidator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QRegularExpressionValidator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def regularExpression(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QRegularExpressionValidator::regularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionvalidator.html#regularExpression

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QRegularExpressionValidator::regularExpression()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QRegularExpressionValidator17regularExpressionEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRegularExpression)
  def setRegularExpression(self, re: QRegularExpression) -> None:
    """
    Calls Qt's 'void QRegularExpressionValidator::setRegularExpression(const
    QRegularExpression &re)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionvalidator.html

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QRegularExpressionValidator::setRegularExpression(const
    #      QRegularExpression &re)
    self.uglySide.call(
        'ritual_ZN27QRegularExpressionValidator20setRegularExpressionERK18Q'
        'RegularExpression',
        self._valueOf(re),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpressionValidator::QRegularExpressionValidator(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionvalidator.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRegularExpressionValidator::QRegularExpressionValidator(QObject
    #      *parent)
    self._noteCreation(QRegularExpressionValidator, lambda: Rituals.call(
        'ritual_ZN27QRegularExpressionValidatorC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QRegularExpression)
  @overload(QRegularExpression, QObject)
  @overload(QRegularExpression, NoneType)
  def __init__(
      self,
      re: QRegularExpression,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRegularExpressionValidator::QRegularExpressionValidator(const
    QRegularExpression &re, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qregularexpressionvalidator.html

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRegularExpressionValidator::QRegularExpressionValidator(const
    #      QRegularExpression &re, QObject *parent)
    self._noteCreation(QRegularExpressionValidator, lambda: Rituals.call(
        'ritual_ZN27QRegularExpressionValidatorC1ERK18QRegularExpressionP7Q'
        'Object',
        self._valueOf(re), self._addressOf(parent, 'QObject'),
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
