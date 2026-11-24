//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickshortcutcontext_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickshortcutcontext_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QQuickShortcutContext::matcher(QObject *object, Qt::ShortcutContext
//      context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickShortcutContext7matcherEP7QObjectN2Qt15ShortcutContextE(
    QObject *object,
    Qt::ShortcutContext context) {
  return QQuickShortcutContext::matcher(object, context);
}

//  QQuickShortcutContext::~QQuickShortcutContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickShortcutContextD1Ev(QQuickShortcutContext *self) {
  delete self;
}
