//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickApplicationWindowAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickApplicationWindowAttached10metaObjectEv(
    const QQuickApplicationWindowAttached *self) {
  return self->metaObject();
}

//  QString QQuickApplicationWindowAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickApplicationWindowAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickApplicationWindowAttached::tr(s, c, n));
}

//  QQuickApplicationWindowAttached::QQuickApplicationWindowAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickApplicationWindowAttached *ritual_ZN31QQuickApplicationWindowAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickApplicationWindowAttached(parent);
}

//  QQuickApplicationWindow *QQuickApplicationWindowAttached::window() const
extern "C" Q_DECL_EXPORT
QQuickApplicationWindow *ritual_ZNK31QQuickApplicationWindowAttached6windowEv(
    const QQuickApplicationWindowAttached *self) {
  return self->window();
}

//  QQuickItem *QQuickApplicationWindowAttached::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK31QQuickApplicationWindowAttached11contentItemEv(
    const QQuickApplicationWindowAttached *self) {
  return self->contentItem();
}

//  QQuickItem *QQuickApplicationWindowAttached::activeFocusControl() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK31QQuickApplicationWindowAttached18activeFocusControlEv(
    const QQuickApplicationWindowAttached *self) {
  return self->activeFocusControl();
}

//  QQuickItem *QQuickApplicationWindowAttached::header() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK31QQuickApplicationWindowAttached6headerEv(
    const QQuickApplicationWindowAttached *self) {
  return self->header();
}

//  QQuickItem *QQuickApplicationWindowAttached::footer() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK31QQuickApplicationWindowAttached6footerEv(
    const QQuickApplicationWindowAttached *self) {
  return self->footer();
}

//  QQuickItem *QQuickApplicationWindowAttached::menuBar() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK31QQuickApplicationWindowAttached7menuBarEv(
    const QQuickApplicationWindowAttached *self) {
  return self->menuBar();
}
