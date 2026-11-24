//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickmenuseparator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenuseparator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickMenuSeparator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMenuSeparator : QQuickMenuSeparator {
  using QQuickMenuSeparator::defaultFont;
  using QQuickMenuSeparator::accessibleRole;
};

//  const QMetaObject *QQuickMenuSeparator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickMenuSeparator10metaObjectEv(
    const QQuickMenuSeparator *self) {
  return self->metaObject();
}

//  QString QQuickMenuSeparator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickMenuSeparator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMenuSeparator::tr(s, c, n));
}

//  QQuickMenuSeparator::QQuickMenuSeparator(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMenuSeparator *ritual_ZN19QQuickMenuSeparatorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickMenuSeparator(parent);
}

//  QFont QQuickMenuSeparator::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickMenuSeparator11defaultFontEv(
    const QQuickMenuSeparator *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuSeparator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickMenuSeparator14accessibleRoleEv(
    const QQuickMenuSeparator *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QFont QQuickMenuSeparator::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK19QQuickMenuSeparator11defaultFontEv(
    const QQuickMenuSeparator *self) {
  return new QFont(
      static_cast<const OwnQQuickMenuSeparator *>(self)->OwnQQuickMenuSeparator::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuSeparator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickMenuSeparator14accessibleRoleEv(
    const QQuickMenuSeparator *self) {
  return static_cast<const OwnQQuickMenuSeparator *>(self)->OwnQQuickMenuSeparator::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
