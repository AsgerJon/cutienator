//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qaccessiblewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qaccessiblewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>
#include <QtGui/qcolor.h>

//  QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r)
extern "C" Q_DECL_EXPORT
QAccessibleWidget *ritual_ZN17QAccessibleWidgetC1EP7QWidgetN11QAccessible4RoleE(
    QWidget *o,
    QAccessible::Role r) {
  return new QAccessibleWidget(o, r);
}

//  QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r,
//      const QString &name)
extern "C" Q_DECL_EXPORT
QAccessibleWidget *ritual_ZN17QAccessibleWidgetC1EP7QWidgetN11QAccessible4RoleERK7QString(
    QWidget *o,
    QAccessible::Role r,
    const QString *name) {
  return new QAccessibleWidget(o, r, *name);
}

//  bool QAccessibleWidget::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAccessibleWidget7isValidEv(const QAccessibleWidget *self) {
  return self->isValid();
}

//  QWindow *QAccessibleWidget::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK17QAccessibleWidget6windowEv(
    const QAccessibleWidget *self) {
  return self->window();
}

//  int QAccessibleWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAccessibleWidget10childCountEv(
    const QAccessibleWidget *self) {
  return self->childCount();
}

//  int QAccessibleWidget::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAccessibleWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleWidget *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleWidget::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleWidget10focusChildEv(
    const QAccessibleWidget *self) {
  return self->focusChild();
}

//  QRect QAccessibleWidget::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QAccessibleWidget4rectEv(const QAccessibleWidget *self) {
  return new QRect(self->rect());
}

//  QAccessibleInterface *QAccessibleWidget::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleWidget6parentEv(
    const QAccessibleWidget *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleWidget5childEi(
    const QAccessibleWidget *self,
    int index) {
  return self->child(index);
}

//  QString QAccessibleWidget::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAccessibleWidget4textEN11QAccessible4TextE(
    const QAccessibleWidget *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleWidget::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QAccessibleWidget4roleEv(
    const QAccessibleWidget *self) {
  return self->role();
}

//  QAccessible::State QAccessibleWidget::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK17QAccessibleWidget5stateEv(
    const QAccessibleWidget *self) {
  return new QAccessible::State(self->state());
}

//  QColor QAccessibleWidget::foregroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QAccessibleWidget15foregroundColorEv(
    const QAccessibleWidget *self) {
  return new QColor(self->foregroundColor());
}

//  QColor QAccessibleWidget::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QAccessibleWidget15backgroundColorEv(
    const QAccessibleWidget *self) {
  return new QColor(self->backgroundColor());
}

//  void QAccessibleWidget::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleWidget8doActionERK7QString(
    QAccessibleWidget *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QAccessibleWidget as the QAccessibleActionInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleActionInterface *ritual_cast_QAccessibleWidget_QAccessibleActionInterface(
    QAccessibleWidget *self) {
  return static_cast<QAccessibleActionInterface *>(self);
}
