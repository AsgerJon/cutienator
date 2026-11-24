//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qaccessiblequickview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qaccessiblequickview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qlist.h>

//  QAccessibleQuickWindow::QAccessibleQuickWindow(QQuickWindow *object)
extern "C" Q_DECL_EXPORT
QAccessibleQuickWindow *ritual_ZN22QAccessibleQuickWindowC1EP12QQuickWindow(
    QQuickWindow *object) {
  return new QAccessibleQuickWindow(object);
}

//  QAccessibleInterface *QAccessibleQuickWindow::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleQuickWindow6parentEv(
    const QAccessibleQuickWindow *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleQuickWindow::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleQuickWindow5childEi(
    const QAccessibleQuickWindow *self,
    int index) {
  return self->child(index);
}

//  QAccessibleInterface *QAccessibleQuickWindow::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleQuickWindow10focusChildEv(
    const QAccessibleQuickWindow *self) {
  return self->focusChild();
}

//  QAccessible::Role QAccessibleQuickWindow::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK22QAccessibleQuickWindow4roleEv(
    const QAccessibleQuickWindow *self) {
  return self->role();
}

//  QAccessible::State QAccessibleQuickWindow::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK22QAccessibleQuickWindow5stateEv(
    const QAccessibleQuickWindow *self) {
  return new QAccessible::State(self->state());
}

//  QRect QAccessibleQuickWindow::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK22QAccessibleQuickWindow4rectEv(
    const QAccessibleQuickWindow *self) {
  return new QRect(self->rect());
}

//  int QAccessibleQuickWindow::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleQuickWindow10childCountEv(
    const QAccessibleQuickWindow *self) {
  return self->childCount();
}

//  int QAccessibleQuickWindow::indexOfChild(const QAccessibleInterface
//      *iface) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleQuickWindow12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickWindow *self,
    const QAccessibleInterface *iface) {
  return self->indexOfChild(iface);
}

//  QString QAccessibleQuickWindow::text(QAccessible::Text text) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QAccessibleQuickWindow4textEN11QAccessible4TextE(
    const QAccessibleQuickWindow *self,
    QAccessible::Text text) {
  return new QString(self->text(text));
}

//  QAccessibleInterface *QAccessibleQuickWindow::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleQuickWindow7childAtEii(
    const QAccessibleQuickWindow *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QQuickWindow *QAccessibleQuickWindow::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK22QAccessibleQuickWindow6windowEv(
    const QAccessibleQuickWindow *self) {
  return self->window();
}

//  QList<QQuickItem *> QAccessibleQuickWindow::rootItems() const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK22QAccessibleQuickWindow9rootItemsEv(
    const QAccessibleQuickWindow *self) {
  return new QList<QQuickItem *>(self->rootItems());
}

//  QAccessibleInterface *QAccessibleQuickWindow::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleQuickWindow6parentEv(
    const QAccessibleQuickWindow *self) {
  return self->QAccessibleQuickWindow::parent();
}

//  QAccessibleInterface *QAccessibleQuickWindow::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleQuickWindow5childEi(
    const QAccessibleQuickWindow *self,
    int index) {
  return self->QAccessibleQuickWindow::child(index);
}

//  QAccessibleInterface *QAccessibleQuickWindow::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleQuickWindow10focusChildEv(
    const QAccessibleQuickWindow *self) {
  return self->QAccessibleQuickWindow::focusChild();
}

//  QAccessible::Role QAccessibleQuickWindow::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK22QAccessibleQuickWindow4roleEv(
    const QAccessibleQuickWindow *self) {
  return self->QAccessibleQuickWindow::role();
}

//  QAccessible::State QAccessibleQuickWindow::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK22QAccessibleQuickWindow5stateEv(
    const QAccessibleQuickWindow *self) {
  return new QAccessible::State(self->QAccessibleQuickWindow::state());
}

//  QRect QAccessibleQuickWindow::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK22QAccessibleQuickWindow4rectEv(
    const QAccessibleQuickWindow *self) {
  return new QRect(self->QAccessibleQuickWindow::rect());
}

//  int QAccessibleQuickWindow::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAccessibleQuickWindow10childCountEv(
    const QAccessibleQuickWindow *self) {
  return self->QAccessibleQuickWindow::childCount();
}

//  int QAccessibleQuickWindow::indexOfChild(const QAccessibleInterface
//      *iface) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAccessibleQuickWindow12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickWindow *self,
    const QAccessibleInterface *iface) {
  return self->QAccessibleQuickWindow::indexOfChild(iface);
}

//  QString QAccessibleQuickWindow::text(QAccessible::Text text) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QAccessibleQuickWindow4textEN11QAccessible4TextE(
    const QAccessibleQuickWindow *self,
    QAccessible::Text text) {
  return new QString(self->QAccessibleQuickWindow::text(text));
}

//  QAccessibleInterface *QAccessibleQuickWindow::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleQuickWindow7childAtEii(
    const QAccessibleQuickWindow *self,
    int x,
    int y) {
  return self->QAccessibleQuickWindow::childAt(x, y);
}

//  QQuickWindow *QAccessibleQuickWindow::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_own_ZNK22QAccessibleQuickWindow6windowEv(
    const QAccessibleQuickWindow *self) {
  return self->QAccessibleQuickWindow::window();
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
