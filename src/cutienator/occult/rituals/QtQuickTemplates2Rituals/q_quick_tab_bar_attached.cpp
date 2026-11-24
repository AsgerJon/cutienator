//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbar_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickTabBarAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickTabBarAttached10metaObjectEv(
    const QQuickTabBarAttached *self) {
  return self->metaObject();
}

//  QString QQuickTabBarAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickTabBarAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTabBarAttached::tr(s, c, n));
}

//  QQuickTabBarAttached::QQuickTabBarAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTabBarAttached *ritual_ZN20QQuickTabBarAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickTabBarAttached(parent);
}

//  int QQuickTabBarAttached::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickTabBarAttached5indexEv(
    const QQuickTabBarAttached *self) {
  return self->index();
}

//  QQuickTabBar *QQuickTabBarAttached::tabBar() const
extern "C" Q_DECL_EXPORT
QQuickTabBar *ritual_ZNK20QQuickTabBarAttached6tabBarEv(
    const QQuickTabBarAttached *self) {
  return self->tabBar();
}

//  QQuickTabBar::Position QQuickTabBarAttached::position() const
extern "C" Q_DECL_EXPORT
QQuickTabBar::Position ritual_ZNK20QQuickTabBarAttached8positionEv(
    const QQuickTabBarAttached *self) {
  return self->position();
}

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
