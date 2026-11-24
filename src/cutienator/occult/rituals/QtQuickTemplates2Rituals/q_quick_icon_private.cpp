//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QQuickIconPrivate::isResolved(const QQuickIcon &icon, int
//      resolveMask)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickIconPrivate10isResolvedERK10QQuickIconi(
    const QQuickIcon *icon,
    int resolveMask) {
  return QQuickIconPrivate::isResolved(*icon, resolveMask);
}

//  QQuickIconPrivate::~QQuickIconPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickIconPrivateD1Ev(QQuickIconPrivate *self) {
  delete self;
}
