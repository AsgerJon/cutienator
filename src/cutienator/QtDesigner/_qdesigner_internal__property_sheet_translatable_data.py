"""
qdesigner_internal::PropertySheetTranslatableData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertySheetTranslatableData to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class PropertySheetTranslatableData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::PropertySheetTranslatableData: a
  plain Python object standing in front of one C++
  qdesigner_internal::PropertySheetTranslatableData.

  C++ hands a qdesigner_internal::PropertySheetTranslatableData around as a
  copy, so every C++ qdesigner_internal::PropertySheetTranslatableData behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PropertySheetTranslatableData
  that has a ritual and that Python can call so far, 10 names in all:
  'translatable', 'setTranslatable', 'disambiguation', 'setDisambiguation',
  'comment', 'setComment', 'id', 'setId', '__eq__', '__ne__'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::PropertySheetTranslatableData::
    ~PropertySheetTranslatableData()': the destructor: Python removes its C++
    qdesigner_internal::PropertySheetTranslatableData by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertySheetTranslatableData is created at
    the first use, not by
    'qdesigner_internal::PropertySheetTranslatableData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PropertySheetTranslatableData
    back gives a copy the ritual made for Python, in a new cute
    qdesigner_internal::PropertySheetTranslatableData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PropertySheetTranslatableData'

  #  Qt's '~qdesigner_internal::PropertySheetTranslatableData()'. Naming it
  #  makes this a value class: Python owns every C++
  #  qdesigner_internal::PropertySheetTranslatableData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal29PropertySheetTranslatableDataD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def translatable(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::PropertySheetTranslatableData::translatable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html
    """
    #  bool qdesigner_internal::PropertySheetTranslatableData::translatable()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData12tra'
        'nslatableEv',
    )

  def disambiguation(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::PropertySheetTranslatableData::disambiguation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      qdesigner_internal::PropertySheetTranslatableData::disambiguation(
    #      ) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData14dis'
        'ambiguationEv',
    )

  def comment(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::PropertySheetTranslatableData::comment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PropertySheetTranslatableData::comment()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData7comm'
        'entEv',
    )

  def id(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::PropertySheetTranslatableData::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PropertySheetTranslatableData::id() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData2idEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTranslatable(self, translatable: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetTranslatableData::setTranslatable(bool
    translatable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Parameters
    ----------

    translatable : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::PropertySheetTranslatableData::
    #      setTranslatable(bool translatable)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal29PropertySheetTranslatableData15setT'
        'ranslatableEb',
        translatable,
    )

  @overload(str)
  def setDisambiguation(self, d: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetTranslatableData::setDisambiguation(
    const QString &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Parameters
    ----------

    d : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PropertySheetTranslatableData::
    #      setDisambiguation(const QString &d)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal29PropertySheetTranslatableData17setD'
        'isambiguationERK7QString',
        d,
    )

  @overload(str)
  def setComment(self, comment: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetTranslatableData::setComment(const
    QString &comment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Parameters
    ----------

    comment : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PropertySheetTranslatableData::setComment(
    #      const QString &comment)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal29PropertySheetTranslatableData10setC'
        'ommentERK7QString',
        comment,
    )

  @overload(str)
  def setId(self, id: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetTranslatableData::setId(const QString
    &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PropertySheetTranslatableData::setId(const
    #      QString &id)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal29PropertySheetTranslatableData5setId'
        'ERK7QString',
        id,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: PropertySheetTranslatableData) -> bool:
    """
    Calls Qt's 'bool operator==(const PropertySheetTranslatableData &lhs,
    const PropertySheetTranslatableData &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Parameters
    ----------

    rhs : PropertySheetTranslatableData
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetTranslatableData, which stays Python's
      own.
    """
    #  bool operator==(const PropertySheetTranslatableData &lhs, const
    #      PropertySheetTranslatableData &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_29PropertySheetTranslatableDa'
        'taES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: PropertySheetTranslatableData) -> bool:
    """
    Calls Qt's 'bool operator!=(const PropertySheetTranslatableData &lhs,
    const PropertySheetTranslatableData &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Parameters
    ----------

    rhs : PropertySheetTranslatableData
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetTranslatableData, which stays Python's
      own.
    """
    #  bool operator!=(const PropertySheetTranslatableData &lhs, const
    #      PropertySheetTranslatableData &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_29PropertySheetTranslatableDa'
        'taES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
  @overload(bool)
  @overload(bool, str)
  @overload(bool, str, str)
  def __init__(
      self,
      translatable: bool = True,
      disambiguation: str = '',
      comment: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetTranslatableData::
    PropertySheetTranslatableData(bool translatable, const QString
    &disambiguation, const QString &comment)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheettranslatabledata.html

    Parameters
    ----------

    translatable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    disambiguation : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    comment : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  qdesigner_internal::PropertySheetTranslatableData::
    #      PropertySheetTranslatableData(bool translatable, const QString
    #      &disambiguation, const QString &comment)
    self._noteCreation(PropertySheetTranslatableData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal29PropertySheetTranslatableDataC1EbRK'
        '7QStringS3_',
        translatable, disambiguation, comment,
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
