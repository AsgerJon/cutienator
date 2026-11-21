//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibleobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessibleobject.h>
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>

//  QAccessibleApplication::QAccessibleApplication()
extern "C" Q_DECL_EXPORT
QAccessibleApplication *ritual_ZN22QAccessibleApplicationC1Ev() {
  return new QAccessibleApplication();
}

//  QWindow *QAccessibleApplication::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK22QAccessibleApplication6windowEv(
    const QAccessibleApplication *self) {
  return self->window();
}

//  int QAccessibleApplication::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleApplication10childCountEv(
    const QAccessibleApplication *self) {
  return self->childCount();
}

//  int QAccessibleApplication::indexOfChild(const QAccessibleInterface *a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleApplication12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleApplication *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QAccessibleInterface *QAccessibleApplication::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleApplication10focusChildEv(
    const QAccessibleApplication *self) {
  return self->focusChild();
}

//  QAccessibleInterface *QAccessibleApplication::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleApplication6parentEv(
    const QAccessibleApplication *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleApplication::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleApplication5childEi(
    const QAccessibleApplication *self,
    int index) {
  return self->child(index);
}

//  QString QAccessibleApplication::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QAccessibleApplication4textEN11QAccessible4TextE(
    const QAccessibleApplication *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleApplication::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK22QAccessibleApplication4roleEv(
    const QAccessibleApplication *self) {
  return self->role();
}

//  QAccessible::State QAccessibleApplication::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK22QAccessibleApplication5stateEv(
    const QAccessibleApplication *self) {
  return new QAccessible::State(self->state());
}
