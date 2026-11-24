//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qaccessiblequickitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qaccessiblequickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  QAccessibleQuickItem::QAccessibleQuickItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QAccessibleQuickItem *ritual_ZN20QAccessibleQuickItemC1EP10QQuickItem(
    QQuickItem *item) {
  return new QAccessibleQuickItem(item);
}

//  bool QAccessibleQuickItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAccessibleQuickItem7isValidEv(
    const QAccessibleQuickItem *self) {
  return self->isValid();
}

//  QWindow *QAccessibleQuickItem::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK20QAccessibleQuickItem6windowEv(
    const QAccessibleQuickItem *self) {
  return self->window();
}

//  QRect QAccessibleQuickItem::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QAccessibleQuickItem4rectEv(
    const QAccessibleQuickItem *self) {
  return new QRect(self->rect());
}

//  QRect QAccessibleQuickItem::viewRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QAccessibleQuickItem8viewRectEv(
    const QAccessibleQuickItem *self) {
  return new QRect(self->viewRect());
}

//  bool QAccessibleQuickItem::clipsChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAccessibleQuickItem13clipsChildrenEv(
    const QAccessibleQuickItem *self) {
  return self->clipsChildren();
}

//  QAccessibleInterface *QAccessibleQuickItem::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleQuickItem7childAtEii(
    const QAccessibleQuickItem *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QAccessibleInterface *QAccessibleQuickItem::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleQuickItem6parentEv(
    const QAccessibleQuickItem *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleQuickItem::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleQuickItem5childEi(
    const QAccessibleQuickItem *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleQuickItem::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleQuickItem10childCountEv(
    const QAccessibleQuickItem *self) {
  return self->childCount();
}

//  int QAccessibleQuickItem::indexOfChild(const QAccessibleInterface *iface)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleQuickItem12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickItem *self,
    const QAccessibleInterface *iface) {
  return self->indexOfChild(iface);
}

//  QList<QQuickItem *> QAccessibleQuickItem::childItems() const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK20QAccessibleQuickItem10childItemsEv(
    const QAccessibleQuickItem *self) {
  return new QList<QQuickItem *>(self->childItems());
}

//  QAccessible::State QAccessibleQuickItem::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK20QAccessibleQuickItem5stateEv(
    const QAccessibleQuickItem *self) {
  return new QAccessible::State(self->state());
}

//  QAccessible::Role QAccessibleQuickItem::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK20QAccessibleQuickItem4roleEv(
    const QAccessibleQuickItem *self) {
  return self->role();
}

//  QString QAccessibleQuickItem::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleQuickItem4textEN11QAccessible4TextE(
    const QAccessibleQuickItem *self,
    QAccessible::Text a0) {
  return new QString(self->text(a0));
}

//  void QAccessibleQuickItem::setText(QAccessible::Text a0, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem7setTextEN11QAccessible4TextERK7QString(
    QAccessibleQuickItem *self,
    QAccessible::Text a0,
    const QString *text) {
  self->setText(a0, *text);
}

//  bool QAccessibleQuickItem::isAccessible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAccessibleQuickItem12isAccessibleEv(
    const QAccessibleQuickItem *self) {
  return self->isAccessible();
}

//  QStringList QAccessibleQuickItem::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QAccessibleQuickItem11actionNamesEv(
    const QAccessibleQuickItem *self) {
  return new QList<QString>(self->actionNames());
}

//  void QAccessibleQuickItem::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem8doActionERK7QString(
    QAccessibleQuickItem *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleQuickItem::keyBindingsForAction(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QAccessibleQuickItem20keyBindingsForActionERK7QString(
    const QAccessibleQuickItem *self,
    const QString *actionName) {
  return new QList<QString>(self->keyBindingsForAction(*actionName));
}

//  QVariant QAccessibleQuickItem::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAccessibleQuickItem12currentValueEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->currentValue());
}

//  void QAccessibleQuickItem::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem15setCurrentValueERK8QVariant(
    QAccessibleQuickItem *self,
    const QVariant *value) {
  self->setCurrentValue(*value);
}

//  QVariant QAccessibleQuickItem::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAccessibleQuickItem12maximumValueEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->maximumValue());
}

//  QVariant QAccessibleQuickItem::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAccessibleQuickItem12minimumValueEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->minimumValue());
}

//  QVariant QAccessibleQuickItem::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAccessibleQuickItem15minimumStepSizeEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->minimumStepSize());
}

//  void QAccessibleQuickItem::selection(int selectionIndex, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QAccessibleQuickItem9selectionEiPiS0_(
    const QAccessibleQuickItem *self,
    int selectionIndex,
    int *startOffset,
    int *endOffset) {
  self->selection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleQuickItem::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleQuickItem14selectionCountEv(
    const QAccessibleQuickItem *self) {
  return self->selectionCount();
}

//  void QAccessibleQuickItem::addSelection(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem12addSelectionEii(
    QAccessibleQuickItem *self,
    int startOffset,
    int endOffset) {
  self->addSelection(startOffset, endOffset);
}

//  void QAccessibleQuickItem::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem15removeSelectionEi(
    QAccessibleQuickItem *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleQuickItem::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem12setSelectionEiii(
    QAccessibleQuickItem *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleQuickItem::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleQuickItem14cursorPositionEv(
    const QAccessibleQuickItem *self) {
  return self->cursorPosition();
}

//  void QAccessibleQuickItem::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem17setCursorPositionEi(
    QAccessibleQuickItem *self,
    int position) {
  self->setCursorPosition(position);
}

//  QString QAccessibleQuickItem::text(int startOffset, int endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleQuickItem4textEii(
    const QAccessibleQuickItem *self,
    int startOffset,
    int endOffset) {
  return new QString(self->text(startOffset, endOffset));
}

//  QString QAccessibleQuickItem::textBeforeOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleQuickItem16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleQuickItem *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textBeforeOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleQuickItem::textAfterOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleQuickItem15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleQuickItem *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAfterOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleQuickItem::textAtOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleQuickItem12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleQuickItem *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAtOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  int QAccessibleQuickItem::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleQuickItem14characterCountEv(
    const QAccessibleQuickItem *self) {
  return self->characterCount();
}

//  QRect QAccessibleQuickItem::characterRect(int a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QAccessibleQuickItem13characterRectEi(
    const QAccessibleQuickItem *self,
    int a0) {
  return new QRect(self->characterRect(a0));
}

//  int QAccessibleQuickItem::offsetAtPoint(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleQuickItem13offsetAtPointERK6QPoint(
    const QAccessibleQuickItem *self,
    const QPoint *a0) {
  return self->offsetAtPoint(*a0);
}

//  void QAccessibleQuickItem::scrollToSubstring(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleQuickItem17scrollToSubstringEii(
    QAccessibleQuickItem *self,
    int a0,
    int a1) {
  self->scrollToSubstring(a0, a1);
}

//  QString QAccessibleQuickItem::attributes(int a0, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleQuickItem10attributesEiPiS0_(
    const QAccessibleQuickItem *self,
    int a0,
    int *startOffset,
    int *endOffset) {
  return new QString(self->attributes(a0, startOffset, endOffset));
}

//  QTextDocument *QAccessibleQuickItem::textDocument() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK20QAccessibleQuickItem12textDocumentEv(
    const QAccessibleQuickItem *self) {
  return self->textDocument();
}

//  QVariant QAccessibleQuickItem::attributeValue(QAccessible::Attribute key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAccessibleQuickItem14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickItem *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  QQuickItem *QAccessibleQuickItem::item() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QAccessibleQuickItem4itemEv(
    const QAccessibleQuickItem *self) {
  return self->item();
}

//  QAccessibleQuickItem as the QAccessibleActionInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleActionInterface *ritual_cast_QAccessibleQuickItem_QAccessibleActionInterface(
    QAccessibleQuickItem *self) {
  return static_cast<QAccessibleActionInterface *>(self);
}

//  QAccessibleQuickItem as the QAccessibleValueInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleValueInterface *ritual_cast_QAccessibleQuickItem_QAccessibleValueInterface(
    QAccessibleQuickItem *self) {
  return static_cast<QAccessibleValueInterface *>(self);
}

//  QAccessibleQuickItem as the QAccessibleTextInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleTextInterface *ritual_cast_QAccessibleQuickItem_QAccessibleTextInterface(
    QAccessibleQuickItem *self) {
  return static_cast<QAccessibleTextInterface *>(self);
}

//  QAccessibleQuickItem as the QAccessibleAttributesInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleAttributesInterface *ritual_cast_QAccessibleQuickItem_QAccessibleAttributesInterface(
    QAccessibleQuickItem *self) {
  return static_cast<QAccessibleAttributesInterface *>(self);
}

//  bool QAccessibleQuickItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QAccessibleQuickItem7isValidEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::isValid();
}

//  QWindow *QAccessibleQuickItem::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZNK20QAccessibleQuickItem6windowEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::window();
}

//  QRect QAccessibleQuickItem::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK20QAccessibleQuickItem4rectEv(
    const QAccessibleQuickItem *self) {
  return new QRect(self->QAccessibleQuickItem::rect());
}

//  QAccessibleInterface *QAccessibleQuickItem::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleQuickItem7childAtEii(
    const QAccessibleQuickItem *self,
    int x,
    int y) {
  return self->QAccessibleQuickItem::childAt(x, y);
}

//  QAccessibleInterface *QAccessibleQuickItem::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleQuickItem6parentEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::parent();
}

//  QAccessibleInterface *QAccessibleQuickItem::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleQuickItem5childEi(
    const QAccessibleQuickItem *self,
    int index) {
  return self->QAccessibleQuickItem::child(index);
}

//  int QAccessibleQuickItem::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleQuickItem10childCountEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::childCount();
}

//  int QAccessibleQuickItem::indexOfChild(const QAccessibleInterface *iface)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleQuickItem12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickItem *self,
    const QAccessibleInterface *iface) {
  return self->QAccessibleQuickItem::indexOfChild(iface);
}

//  QAccessible::State QAccessibleQuickItem::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK20QAccessibleQuickItem5stateEv(
    const QAccessibleQuickItem *self) {
  return new QAccessible::State(self->QAccessibleQuickItem::state());
}

//  QAccessible::Role QAccessibleQuickItem::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK20QAccessibleQuickItem4roleEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::role();
}

//  QString QAccessibleQuickItem::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QAccessibleQuickItem4textEN11QAccessible4TextE(
    const QAccessibleQuickItem *self,
    QAccessible::Text a0) {
  return new QString(self->QAccessibleQuickItem::text(a0));
}

//  void QAccessibleQuickItem::setText(QAccessible::Text a0, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem7setTextEN11QAccessible4TextERK7QString(
    QAccessibleQuickItem *self,
    QAccessible::Text a0,
    const QString *text) {
  self->QAccessibleQuickItem::setText(a0, *text);
}

//  void QAccessibleQuickItem::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem8doActionERK7QString(
    QAccessibleQuickItem *self,
    const QString *actionName) {
  self->QAccessibleQuickItem::doAction(*actionName);
}

//  QVariant QAccessibleQuickItem::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QAccessibleQuickItem12currentValueEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->QAccessibleQuickItem::currentValue());
}

//  void QAccessibleQuickItem::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem15setCurrentValueERK8QVariant(
    QAccessibleQuickItem *self,
    const QVariant *value) {
  self->QAccessibleQuickItem::setCurrentValue(*value);
}

//  QVariant QAccessibleQuickItem::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QAccessibleQuickItem12maximumValueEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->QAccessibleQuickItem::maximumValue());
}

//  QVariant QAccessibleQuickItem::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QAccessibleQuickItem12minimumValueEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->QAccessibleQuickItem::minimumValue());
}

//  QVariant QAccessibleQuickItem::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QAccessibleQuickItem15minimumStepSizeEv(
    const QAccessibleQuickItem *self) {
  return new QVariant(self->QAccessibleQuickItem::minimumStepSize());
}

//  int QAccessibleQuickItem::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleQuickItem14selectionCountEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::selectionCount();
}

//  void QAccessibleQuickItem::addSelection(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem12addSelectionEii(
    QAccessibleQuickItem *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleQuickItem::addSelection(startOffset, endOffset);
}

//  void QAccessibleQuickItem::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem15removeSelectionEi(
    QAccessibleQuickItem *self,
    int selectionIndex) {
  self->QAccessibleQuickItem::removeSelection(selectionIndex);
}

//  void QAccessibleQuickItem::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem12setSelectionEiii(
    QAccessibleQuickItem *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->QAccessibleQuickItem::setSelection(
      selectionIndex,
      startOffset,
      endOffset);
}

//  int QAccessibleQuickItem::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleQuickItem14cursorPositionEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::cursorPosition();
}

//  void QAccessibleQuickItem::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem17setCursorPositionEi(
    QAccessibleQuickItem *self,
    int position) {
  self->QAccessibleQuickItem::setCursorPosition(position);
}

//  QString QAccessibleQuickItem::text(int startOffset, int endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QAccessibleQuickItem4textEii(
    const QAccessibleQuickItem *self,
    int startOffset,
    int endOffset) {
  return new QString(
      self->QAccessibleQuickItem::text(
          startOffset,
          endOffset));
}

//  int QAccessibleQuickItem::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleQuickItem14characterCountEv(
    const QAccessibleQuickItem *self) {
  return self->QAccessibleQuickItem::characterCount();
}

//  QRect QAccessibleQuickItem::characterRect(int a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK20QAccessibleQuickItem13characterRectEi(
    const QAccessibleQuickItem *self,
    int a0) {
  return new QRect(self->QAccessibleQuickItem::characterRect(a0));
}

//  int QAccessibleQuickItem::offsetAtPoint(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleQuickItem13offsetAtPointERK6QPoint(
    const QAccessibleQuickItem *self,
    const QPoint *a0) {
  return self->QAccessibleQuickItem::offsetAtPoint(*a0);
}

//  void QAccessibleQuickItem::scrollToSubstring(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleQuickItem17scrollToSubstringEii(
    QAccessibleQuickItem *self,
    int a0,
    int a1) {
  self->QAccessibleQuickItem::scrollToSubstring(a0, a1);
}

//  QVariant QAccessibleQuickItem::attributeValue(QAccessible::Attribute key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QAccessibleQuickItem14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickItem *self,
    QAccessible::Attribute key) {
  return new QVariant(self->QAccessibleQuickItem::attributeValue(key));
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
