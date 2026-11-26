//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextselection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextselection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qurl.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktextselection_p.h>
#include <QtGui/QFont>
#include <QtGui/QTextOption>
#include <QtQuick/private/qquicktextcontrol_p.h>
#include <QtQuick/private/qquicktextcontrol_p_p.h>
#include <QtQuick/private/qquicktextedit_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicktextselection.cpp, line 415, as _ZN19QQuickTextSelection20updateFromCharFormatERK15QTextCharFormat
inline void QQuickTextSelection::updateFromCharFormat(const QTextCharFormat &fmt)
{
    if (fmt.font() != m_charFormat.font())
        emit fontChanged();
    if (fmt.foreground().color() != m_charFormat.foreground().color())
        emit colorChanged();

    m_charFormat = fmt;
}

//  from ../qtdeclarative/src/quick/util/qquicktextselection.cpp, line 425, as _ZN19QQuickTextSelection21updateFromBlockFormatEv
inline void QQuickTextSelection::updateFromBlockFormat()
{
    QTextBlockFormat fmt = cursor().blockFormat();

    if (fmt.alignment() != m_blockFormat.alignment())
        emit alignmentChanged();

    m_blockFormat = fmt;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickTextSelection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickTextSelection10metaObjectEv(
    const QQuickTextSelection *self) {
  return self->metaObject();
}

//  void *QQuickTextSelection::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickTextSelection11qt_metacastEPKc(
    QQuickTextSelection *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextSelection::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickTextSelection11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextSelection *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTextSelection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickTextSelection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextSelection::tr(s, c, n));
}

//  QQuickTextSelection::QQuickTextSelection(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTextSelection *ritual_ZN19QQuickTextSelectionC1EP7QObject(
    QObject *parent) {
  return new QQuickTextSelection(parent);
}

//  void QQuickTextSelection::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection10classBeginEv(
    QQuickTextSelection *self) {
  self->classBegin();
}

//  void QQuickTextSelection::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection17componentCompleteEv(
    QQuickTextSelection *self) {
  self->componentComplete();
}

//  QQuickTextDocument *QQuickTextSelection::document() const
extern "C" Q_DECL_EXPORT
QQuickTextDocument *ritual_ZNK19QQuickTextSelection8documentEv(
    const QQuickTextSelection *self) {
  return self->document();
}

//  void QQuickTextSelection::setDocument(QQuickTextDocument *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection11setDocumentEP18QQuickTextDocument(
    QQuickTextSelection *self,
    QQuickTextDocument *doc) {
  self->setDocument(doc);
}

//  int QQuickTextSelection::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickTextSelection14selectionStartEv(
    const QQuickTextSelection *self) {
  return self->selectionStart();
}

//  void QQuickTextSelection::setSelectionStart(int start)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection17setSelectionStartEi(
    QQuickTextSelection *self,
    int start) {
  self->setSelectionStart(start);
}

//  int QQuickTextSelection::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickTextSelection12selectionEndEv(
    const QQuickTextSelection *self) {
  return self->selectionEnd();
}

//  void QQuickTextSelection::setSelectionEnd(int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection15setSelectionEndEi(
    QQuickTextSelection *self,
    int end) {
  self->setSelectionEnd(end);
}

//  QString QQuickTextSelection::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickTextSelection4textEv(
    const QQuickTextSelection *self) {
  return new QString(self->text());
}

//  void QQuickTextSelection::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection7setTextERK7QString(
    QQuickTextSelection *self,
    const QString *text) {
  self->setText(*text);
}

//  QFont QQuickTextSelection::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickTextSelection4fontEv(
    const QQuickTextSelection *self) {
  return new QFont(self->font());
}

//  void QQuickTextSelection::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection7setFontERK5QFont(
    QQuickTextSelection *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QColor QQuickTextSelection::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickTextSelection5colorEv(
    const QQuickTextSelection *self) {
  return new QColor(self->color());
}

//  void QQuickTextSelection::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection8setColorE6QColor(
    QQuickTextSelection *self,
    const QColor *color) {
  self->setColor(*color);
}

//  Qt::Alignment QQuickTextSelection::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickTextSelection9alignmentEv(
    const QQuickTextSelection *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QQuickTextSelection::setAlignment(Qt::Alignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickTextSelection *self,
    int align) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(align));
}

//  bool QQuickTextSelection::moveSelectionStart(MoveOperation op, int n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickTextSelection18moveSelectionStartENS_13MoveOperationEi(
    QQuickTextSelection *self,
    QQuickTextSelection::MoveOperation op,
    int n) {
  return self->moveSelectionStart(op, n);
}

//  bool QQuickTextSelection::moveSelectionEnd(MoveOperation op, int n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickTextSelection16moveSelectionEndENS_13MoveOperationEi(
    QQuickTextSelection *self,
    QQuickTextSelection::MoveOperation op,
    int n) {
  return self->moveSelectionEnd(op, n);
}

//  void QQuickTextSelection::duplicate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection9duplicateEv(QQuickTextSelection *self) {
  self->duplicate();
}

//  void QQuickTextSelection::linkTo(const QUrl &destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection6linkToERK4QUrl(
    QQuickTextSelection *self,
    const QUrl *destination) {
  self->linkTo(*destination);
}

//  void QQuickTextSelection::documentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection15documentChangedEv(
    QQuickTextSelection *self) {
  self->documentChanged();
}

//  void QQuickTextSelection::selectionStartChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection21selectionStartChangedEv(
    QQuickTextSelection *self) {
  self->selectionStartChanged();
}

//  void QQuickTextSelection::selectionEndChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection19selectionEndChangedEv(
    QQuickTextSelection *self) {
  self->selectionEndChanged();
}

//  void QQuickTextSelection::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection11textChangedEv(
    QQuickTextSelection *self) {
  self->textChanged();
}

//  void QQuickTextSelection::fontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection11fontChangedEv(
    QQuickTextSelection *self) {
  self->fontChanged();
}

//  void QQuickTextSelection::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection12colorChangedEv(
    QQuickTextSelection *self) {
  self->colorChanged();
}

//  void QQuickTextSelection::alignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection16alignmentChangedEv(
    QQuickTextSelection *self) {
  self->alignmentChanged();
}

//  QTextCursor QQuickTextSelection::cursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK19QQuickTextSelection6cursorEv(
    const QQuickTextSelection *self) {
  return new QTextCursor(self->cursor());
}

//  void QQuickTextSelection::updateFromCharFormat(const QTextCharFormat
//      &fmt)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection20updateFromCharFormatERK15QTextCharFormat(
    QQuickTextSelection *self,
    const QTextCharFormat *fmt) {
  self->updateFromCharFormat(*fmt);
}

//  void QQuickTextSelection::updateFromBlockFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextSelection21updateFromBlockFormatEv(
    QQuickTextSelection *self) {
  self->updateFromBlockFormat();
}

//  QQuickTextSelection as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickTextSelection_QQmlParserStatus(
    QQuickTextSelection *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQuickTextSelection::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickTextSelection10classBeginEv(
    QQuickTextSelection *self) {
  self->QQuickTextSelection::classBegin();
}

//  void QQuickTextSelection::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickTextSelection17componentCompleteEv(
    QQuickTextSelection *self) {
  self->QQuickTextSelection::componentComplete();
}
