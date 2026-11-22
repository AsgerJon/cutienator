//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

//  QAccessibleEditableTextInterface::~QAccessibleEditableTextInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterfaceD1Ev(
    QAccessibleEditableTextInterface *self) {
  delete self;
}

//  void QAccessibleEditableTextInterface::deleteText(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterface10deleteTextEii(
    QAccessibleEditableTextInterface *self,
    int startOffset,
    int endOffset) {
  self->deleteText(startOffset, endOffset);
}

//  void QAccessibleEditableTextInterface::insertText(int offset, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString(
    QAccessibleEditableTextInterface *self,
    int offset,
    const QString *text) {
  self->insertText(offset, *text);
}

//  void QAccessibleEditableTextInterface::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString(
    QAccessibleEditableTextInterface *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->replaceText(startOffset, endOffset, *text);
}
