//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontentitem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontentitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickContentItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickContentItem10metaObjectEv(
    const QQuickContentItem *self) {
  return self->metaObject();
}

//  QString QQuickContentItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickContentItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickContentItem::tr(s, c, n));
}

//  QQuickContentItem::QQuickContentItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickContentItem *ritual_ZN17QQuickContentItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickContentItem(parent);
}

//  QQuickContentItem::QQuickContentItem(const QObject *scope, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickContentItem *ritual_ZN17QQuickContentItemC1EPK7QObjectP10QQuickItem(
    const QObject *scope,
    QQuickItem *parent) {
  return new QQuickContentItem(scope, parent);
}
