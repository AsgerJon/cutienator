//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qaccessiblequicktextinput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qaccessiblequicktextinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QAccessibleQuickTextInput::QAccessibleQuickTextInput(QQuickTextInput
//      *textEdit)
extern "C" Q_DECL_EXPORT
QAccessibleQuickTextInput *ritual_ZN25QAccessibleQuickTextInputC1EP15QQuickTextInput(
    QQuickTextInput *textEdit) {
  return new QAccessibleQuickTextInput(textEdit);
}

//  void QAccessibleQuickTextInput::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleQuickTextInput15removeSelectionEi(
    QAccessibleQuickTextInput *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleQuickTextInput::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleQuickTextInput12setSelectionEiii(
    QAccessibleQuickTextInput *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  void QAccessibleQuickTextInput::deleteText(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleQuickTextInput10deleteTextEii(
    QAccessibleQuickTextInput *self,
    int startOffset,
    int endOffset) {
  self->deleteText(startOffset, endOffset);
}

//  void QAccessibleQuickTextInput::insertText(int offset, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleQuickTextInput10insertTextEiRK7QString(
    QAccessibleQuickTextInput *self,
    int offset,
    const QString *text) {
  self->insertText(offset, *text);
}

//  void QAccessibleQuickTextInput::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleQuickTextInput11replaceTextEiiRK7QString(
    QAccessibleQuickTextInput *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->replaceText(startOffset, endOffset, *text);
}

//  QQuickTextInput *QAccessibleQuickTextInput::textInput() const
extern "C" Q_DECL_EXPORT
QQuickTextInput *ritual_ZNK25QAccessibleQuickTextInput9textInputEv(
    const QAccessibleQuickTextInput *self) {
  return self->textInput();
}

//  QAccessibleQuickTextInput as the QAccessibleEditableTextInterface it is
//      built on
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_cast_QAccessibleQuickTextInput_QAccessibleEditableTextInterface(
    QAccessibleQuickTextInput *self) {
  return static_cast<QAccessibleEditableTextInterface *>(self);
}

//  void QAccessibleQuickTextInput::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleQuickTextInput15removeSelectionEi(
    QAccessibleQuickTextInput *self,
    int selectionIndex) {
  self->QAccessibleQuickTextInput::removeSelection(selectionIndex);
}

//  void QAccessibleQuickTextInput::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleQuickTextInput12setSelectionEiii(
    QAccessibleQuickTextInput *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->QAccessibleQuickTextInput::setSelection(
      selectionIndex,
      startOffset,
      endOffset);
}

//  void QAccessibleQuickTextInput::deleteText(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleQuickTextInput10deleteTextEii(
    QAccessibleQuickTextInput *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleQuickTextInput::deleteText(startOffset, endOffset);
}

//  void QAccessibleQuickTextInput::insertText(int offset, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleQuickTextInput10insertTextEiRK7QString(
    QAccessibleQuickTextInput *self,
    int offset,
    const QString *text) {
  self->QAccessibleQuickTextInput::insertText(offset, *text);
}

//  void QAccessibleQuickTextInput::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleQuickTextInput11replaceTextEiiRK7QString(
    QAccessibleQuickTextInput *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->QAccessibleQuickTextInput::replaceText(
      startOffset,
      endOffset,
      *text);
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
