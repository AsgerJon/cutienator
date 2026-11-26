//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickheaderviewdelegate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderviewdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QQuickHeaderViewDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickHeaderViewDelegate10metaObjectEv(
    const QQuickHeaderViewDelegate *self) {
  return self->metaObject();
}

//  void *QQuickHeaderViewDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickHeaderViewDelegate11qt_metacastEPKc(
    QQuickHeaderViewDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickHeaderViewDelegate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickHeaderViewDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickHeaderViewDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickHeaderViewDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickHeaderViewDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickHeaderViewDelegate::tr(s, c, n));
}

//  QQuickHeaderViewDelegate::QQuickHeaderViewDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickHeaderViewDelegate *ritual_ZN24QQuickHeaderViewDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickHeaderViewDelegate(parent);
}

//  QQuickHeaderViewBase *QQuickHeaderViewDelegate::headerView() const
extern "C" Q_DECL_EXPORT
QQuickHeaderViewBase *ritual_ZNK24QQuickHeaderViewDelegate10headerViewEv(
    const QQuickHeaderViewDelegate *self) {
  return self->headerView();
}

//  void QQuickHeaderViewDelegate::setHeaderView(QQuickHeaderViewBase
//      *headerView)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickHeaderViewDelegate13setHeaderViewEP20QQuickHeaderViewBase(
    QQuickHeaderViewDelegate *self,
    QQuickHeaderViewBase *headerView) {
  self->setHeaderView(headerView);
}

//  Qt::Orientation QQuickHeaderViewDelegate::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK24QQuickHeaderViewDelegate11orientationEv(
    const QQuickHeaderViewDelegate *self) {
  return self->orientation();
}

//  QVariant QQuickHeaderViewDelegate::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QQuickHeaderViewDelegate5modelEv(
    const QQuickHeaderViewDelegate *self) {
  return new QVariant(self->model());
}

//  void QQuickHeaderViewDelegate::setModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickHeaderViewDelegate8setModelERK8QVariant(
    QQuickHeaderViewDelegate *self,
    const QVariant *model) {
  self->setModel(*model);
}

//  void QQuickHeaderViewDelegate::headerViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickHeaderViewDelegate17headerViewChangedEv(
    QQuickHeaderViewDelegate *self) {
  self->headerViewChanged();
}

//  void QQuickHeaderViewDelegate::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickHeaderViewDelegate12modelChangedEv(
    QQuickHeaderViewDelegate *self) {
  self->modelChanged();
}

//  void QQuickHeaderViewDelegate::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickHeaderViewDelegate18orientationChangedEv(
    QQuickHeaderViewDelegate *self) {
  self->orientationChanged();
}

//  QQuickHeaderViewDelegatePrivate *QQuickHeaderViewDelegate::d_func()
extern "C" Q_DECL_EXPORT
QQuickHeaderViewDelegatePrivate *ritual_ZN24QQuickHeaderViewDelegate6d_funcEv(
    QQuickHeaderViewDelegate *self) {
  return self->d_func();
}

//  const QQuickHeaderViewDelegatePrivate *QQuickHeaderViewDelegate::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickHeaderViewDelegatePrivate *ritual_ZNK24QQuickHeaderViewDelegate6d_funcEv(
    const QQuickHeaderViewDelegate *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quick_tableview)
