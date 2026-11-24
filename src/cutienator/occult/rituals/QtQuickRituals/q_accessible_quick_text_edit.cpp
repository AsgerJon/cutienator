//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qaccessiblequicktextedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qaccessiblequicktextedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QAccessibleQuickTextEdit::QAccessibleQuickTextEdit(QQuickTextEdit
//      *textEdit)
extern "C" Q_DECL_EXPORT
QAccessibleQuickTextEdit *ritual_ZN24QAccessibleQuickTextEditC1EP14QQuickTextEdit(
    QQuickTextEdit *textEdit) {
  return new QAccessibleQuickTextEdit(textEdit);
}

//  void QAccessibleQuickTextEdit::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleQuickTextEdit15removeSelectionEi(
    QAccessibleQuickTextEdit *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleQuickTextEdit::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleQuickTextEdit12setSelectionEiii(
    QAccessibleQuickTextEdit *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  void QAccessibleQuickTextEdit::deleteText(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleQuickTextEdit10deleteTextEii(
    QAccessibleQuickTextEdit *self,
    int startOffset,
    int endOffset) {
  self->deleteText(startOffset, endOffset);
}

//  void QAccessibleQuickTextEdit::insertText(int offset, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleQuickTextEdit10insertTextEiRK7QString(
    QAccessibleQuickTextEdit *self,
    int offset,
    const QString *text) {
  self->insertText(offset, *text);
}

//  void QAccessibleQuickTextEdit::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleQuickTextEdit11replaceTextEiiRK7QString(
    QAccessibleQuickTextEdit *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->replaceText(startOffset, endOffset, *text);
}

//  QQuickTextEdit *QAccessibleQuickTextEdit::textEdit() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit *ritual_ZNK24QAccessibleQuickTextEdit8textEditEv(
    const QAccessibleQuickTextEdit *self) {
  return self->textEdit();
}

//  QAccessibleQuickTextEdit as the QAccessibleEditableTextInterface it is
//      built on
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_cast_QAccessibleQuickTextEdit_QAccessibleEditableTextInterface(
    QAccessibleQuickTextEdit *self) {
  return static_cast<QAccessibleEditableTextInterface *>(self);
}

//  void QAccessibleQuickTextEdit::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessibleQuickTextEdit15removeSelectionEi(
    QAccessibleQuickTextEdit *self,
    int selectionIndex) {
  self->QAccessibleQuickTextEdit::removeSelection(selectionIndex);
}

//  void QAccessibleQuickTextEdit::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessibleQuickTextEdit12setSelectionEiii(
    QAccessibleQuickTextEdit *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->QAccessibleQuickTextEdit::setSelection(
      selectionIndex,
      startOffset,
      endOffset);
}

//  void QAccessibleQuickTextEdit::deleteText(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessibleQuickTextEdit10deleteTextEii(
    QAccessibleQuickTextEdit *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleQuickTextEdit::deleteText(startOffset, endOffset);
}

//  void QAccessibleQuickTextEdit::insertText(int offset, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessibleQuickTextEdit10insertTextEiRK7QString(
    QAccessibleQuickTextEdit *self,
    int offset,
    const QString *text) {
  self->QAccessibleQuickTextEdit::insertText(offset, *text);
}

//  void QAccessibleQuickTextEdit::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessibleQuickTextEdit11replaceTextEiiRK7QString(
    QAccessibleQuickTextEdit *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->QAccessibleQuickTextEdit::replaceText(startOffset, endOffset, *text);
}

#endif  // QT_CONFIG(accessibility)
