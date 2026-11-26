//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickTableViewAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickTableViewAttached10metaObjectEv(
    const QQuickTableViewAttached *self) {
  return self->metaObject();
}

//  void *QQuickTableViewAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickTableViewAttached11qt_metacastEPKc(
    QQuickTableViewAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTableViewAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickTableViewAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTableViewAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTableViewAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickTableViewAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTableViewAttached::tr(s, c, n));
}

//  QQuickTableViewAttached::QQuickTableViewAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTableViewAttached *ritual_ZN23QQuickTableViewAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickTableViewAttached(parent);
}

//  QQuickTableView *QQuickTableViewAttached::view() const
extern "C" Q_DECL_EXPORT
QQuickTableView *ritual_ZNK23QQuickTableViewAttached4viewEv(
    const QQuickTableViewAttached *self) {
  return self->view();
}

//  void QQuickTableViewAttached::setView(QQuickTableView *newTableView)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewAttached7setViewEP15QQuickTableView(
    QQuickTableViewAttached *self,
    QQuickTableView *newTableView) {
  self->setView(newTableView);
}

//  QQmlComponent *QQuickTableViewAttached::editDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK23QQuickTableViewAttached12editDelegateEv(
    const QQuickTableViewAttached *self) {
  return self->editDelegate();
}

//  void QQuickTableViewAttached::setEditDelegate(QQmlComponent
//      *newEditDelegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewAttached15setEditDelegateEP13QQmlComponent(
    QQuickTableViewAttached *self,
    QQmlComponent *newEditDelegate) {
  self->setEditDelegate(newEditDelegate);
}

//  void QQuickTableViewAttached::viewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewAttached11viewChangedEv(
    QQuickTableViewAttached *self) {
  self->viewChanged();
}

//  void QQuickTableViewAttached::pooled()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewAttached6pooledEv(
    QQuickTableViewAttached *self) {
  self->pooled();
}

//  void QQuickTableViewAttached::reused()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewAttached6reusedEv(
    QQuickTableViewAttached *self) {
  self->reused();
}

//  void QQuickTableViewAttached::editDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewAttached19editDelegateChangedEv(
    QQuickTableViewAttached *self) {
  self->editDelegateChanged();
}

//  void QQuickTableViewAttached::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTableViewAttached6commitEv(
    QQuickTableViewAttached *self) {
  self->commit();
}

#endif  // QT_CONFIG(quick_tableview)
#endif  // QT_CONFIG(quick_tableview)
