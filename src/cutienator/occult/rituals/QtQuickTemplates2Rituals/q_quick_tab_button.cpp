//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbutton_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickTabButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTabButton : QQuickTabButton {
  using QQuickTabButton::defaultFont;
  using QQuickTabButton::accessibleRole;
};

//  const QMetaObject *QQuickTabButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickTabButton10metaObjectEv(
    const QQuickTabButton *self) {
  return self->metaObject();
}

//  QString QQuickTabButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickTabButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTabButton::tr(s, c, n));
}

//  QQuickTabButton::QQuickTabButton(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTabButton *ritual_ZN15QQuickTabButtonC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickTabButton(parent);
}

//  QFont QQuickTabButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QQuickTabButton11defaultFontEv(
    const QQuickTabButton *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTabButton::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QQuickTabButton14accessibleRoleEv(
    const QQuickTabButton *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QFont QQuickTabButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK15QQuickTabButton11defaultFontEv(
    const QQuickTabButton *self) {
  return new QFont(
      static_cast<const OwnQQuickTabButton *>(self)->OwnQQuickTabButton::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTabButton::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QQuickTabButton14accessibleRoleEv(
    const QQuickTabButton *self) {
  return static_cast<const OwnQQuickTabButton *>(self)->OwnQQuickTabButton::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
