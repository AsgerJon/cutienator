"""
QQmlTranslation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltranslation_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlTranslation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class QQmlTranslation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTranslation: a plain Python object standing in
  front of one C++ QQmlTranslation.

  C++ hands a QQmlTranslation around as a copy, so every C++ QQmlTranslation
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlTranslation that has a ritual and that Python
  can call so far, 2 names in all: 'translate', 'contextFromQmlFilename'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTranslation::QQmlTranslation(const Data &d)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlTranslation::~QQmlTranslation()': the destructor: Python
    removes its C++ QQmlTranslation by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlTranslation is created at the first use, not by
    'QQmlTranslation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTranslation back gives a copy the ritual made for
    Python, in a new cute QQmlTranslation.
  - Each name of Qt's QQmlTranslation that has no cute function yet, 'visit',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QQmlTranslation, each a class in here as in
  #  C++.

  class QsTrData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTranslation::QsTrData: a plain Python object
    standing in front of one C++ QQmlTranslation::QsTrData.

    C++ hands a QQmlTranslation::QsTrData around as a copy, so every C++
    QQmlTranslation::QsTrData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlTranslation::QsTrData that has a ritual and
    that Python can call so far, 5 names in all: 'translate', 'context',
    'text', 'comment', 'number'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTranslation::QsTrData::~QsTrData()': the destructor: Python
      removes its C++ QQmlTranslation::QsTrData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlTranslation::QsTrData is created at the first use, not by
      'QQmlTranslation::QsTrData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTranslation::QsTrData back gives a copy the
      ritual made for Python, in a new cute QQmlTranslation::QsTrData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTranslation::QsTrData'

    #  Qt's '~QQmlTranslation::QsTrData()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlTranslation::QsTrData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QQmlTranslation8QsTrDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def translate(self) -> str:
      """
      Calls Qt's 'QString QQmlTranslation::QsTrData::translate() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstrdata.html#translate

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QQmlTranslation::QsTrData::translate() const
      return self.uglySide.call(
          'ritual_ZNK15QQmlTranslation8QsTrData9translateEv',
      )

    def context(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QQmlTranslation::QsTrData::context() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstrdata.html#context

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QQmlTranslation::QsTrData::context() const
      address = self.uglySide.call(
          'ritual_ZNK15QQmlTranslation8QsTrData7contextEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

    def text(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QQmlTranslation::QsTrData::text() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstrdata.html#text

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QQmlTranslation::QsTrData::text() const
      address = self.uglySide.call(
          'ritual_ZNK15QQmlTranslation8QsTrData4textEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

    def comment(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QQmlTranslation::QsTrData::comment() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstrdata.html#comment

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QQmlTranslation::QsTrData::comment() const
      address = self.uglySide.call(
          'ritual_ZNK15QQmlTranslation8QsTrData7commentEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

    def number(self) -> int:
      """
      Calls Qt's 'int QQmlTranslation::QsTrData::number() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstrdata.html#number
      """
      #  int QQmlTranslation::QsTrData::number() const
      return self.uglySide.call(
          'ritual_ZNK15QQmlTranslation8QsTrData6numberEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str, str, str, int)
    def __init__(
        self,
        fileNameForContext: str,
        text: str,
        comment: str,
        number: int,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QQmlTranslation::QsTrData::QsTrData(const QString &fileNameForContext,
      const QString &text, const QString &comment, int number)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstrdata.html#QsTrData

      Parameters
      ----------

      fileNameForContext : str
        Passed on as it is: a QString is made of it for the call.

      text : str
        Passed on as it is: a QString is made of it for the call.

      comment : str
        Passed on as it is: a QString is made of it for the call.

      number : int
        Passed on as it is.
      """
      #  QQmlTranslation::QsTrData::QsTrData(const QString
      #      &fileNameForContext, const QString &text, const QString
      #      &comment, int number)
      self._noteCreation(QQmlTranslation.QsTrData, lambda: Rituals.call(
          'ritual_ZN15QQmlTranslation8QsTrDataC1ERK7QStringS3_S3_i',
          fileNameForContext, text, comment, number,
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class QsTrIdData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTranslation::QsTrIdData: a plain Python object
    standing in front of one C++ QQmlTranslation::QsTrIdData.

    C++ hands a QQmlTranslation::QsTrIdData around as a copy, so every C++
    QQmlTranslation::QsTrIdData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlTranslation::QsTrIdData that has a ritual and
    that Python can call so far, 3 names in all: 'translate', 'id', 'number'.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTranslation::QsTrIdData::~QsTrIdData()': the destructor:
      Python removes its C++ QQmlTranslation::QsTrIdData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlTranslation::QsTrIdData is created at the first use, not by
      'QQmlTranslation::QsTrIdData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTranslation::QsTrIdData back gives a copy the
      ritual made for Python, in a new cute QQmlTranslation::QsTrIdData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTranslation::QsTrIdData'

    #  Qt's '~QQmlTranslation::QsTrIdData()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlTranslation::QsTrIdData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QQmlTranslation10QsTrIdDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def translate(self) -> str:
      """
      Calls Qt's 'QString QQmlTranslation::QsTrIdData::translate() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstriddata.html#translate

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QQmlTranslation::QsTrIdData::translate() const
      return self.uglySide.call(
          'ritual_ZNK15QQmlTranslation10QsTrIdData9translateEv',
      )

    def id(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QQmlTranslation::QsTrIdData::id() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstriddata.html#id

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QQmlTranslation::QsTrIdData::id() const
      address = self.uglySide.call(
          'ritual_ZNK15QQmlTranslation10QsTrIdData2idEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

    def number(self) -> int:
      """
      Calls Qt's 'int QQmlTranslation::QsTrIdData::number() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstriddata.html#number
      """
      #  int QQmlTranslation::QsTrIdData::number() const
      return self.uglySide.call(
          'ritual_ZNK15QQmlTranslation10QsTrIdData6numberEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str, int)
    def __init__(self, id: str, number: int) -> None:
      """
      Notes what was given, for Qt's
      'QQmlTranslation::QsTrIdData::QsTrIdData(const QString &id, int
      number)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltranslation-qstriddata.html#QsTrIdData

      Parameters
      ----------

      id : str
        Passed on as it is: a QString is made of it for the call.

      number : int
        Passed on as it is.
      """
      #  QQmlTranslation::QsTrIdData::QsTrIdData(const QString &id, int
      #      number)
      self._noteCreation(QQmlTranslation.QsTrIdData, lambda: Rituals.call(
          'ritual_ZN15QQmlTranslation10QsTrIdDataC1ERK7QStringi', id, number,
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def contextFromQmlFilename(qmlFilename: str) -> str:
    """
    Calls Qt's 'QString QQmlTranslation::contextFromQmlFilename(const QString
    &qmlFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltranslation.html#contextFromQmlFilename

    Parameters
    ----------

    qmlFilename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTranslation::contextFromQmlFilename(const QString
    #      &qmlFilename)
    return Rituals.call(
        'ritual_ZN15QQmlTranslation22contextFromQmlFilenameERK7QString',
        qmlFilename,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTranslation'

  #  Qt's '~QQmlTranslation()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlTranslation behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QQmlTranslationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def translate(self) -> str:
    """
    Calls Qt's 'QString QQmlTranslation::translate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltranslation.html#translate

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTranslation::translate() const
    return self.uglySide.call('ritual_ZNK15QQmlTranslation9translateEv')

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
    Notes what was given, for Qt's 'QQmlTranslation::QQmlTranslation()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltranslation.html#QQmlTranslation
    """
    #  QQmlTranslation::QQmlTranslation()
    self._noteCreation(QQmlTranslation, lambda: Rituals.call(
        'ritual_ZN15QQmlTranslationC1Ev',
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

  @staticmethod
  def visit(*__, **_) -> Never:
    """
    Qt's 'QQmlTranslation::visit': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTranslation.visit' has no cute function yet. Qt's "
        "'QQmlTranslation::visit': a template: a pattern and no single "
        "function.")
