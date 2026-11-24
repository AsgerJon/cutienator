//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickradiodelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickradiodelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickRadioDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRadioDelegate : QQuickRadioDelegate {
  using QQuickRadioDelegate::defaultFont;
  using QQuickRadioDelegate::accessibleRole;
};

//  const QMetaObject *QQuickRadioDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickRadioDelegate10metaObjectEv(
    const QQuickRadioDelegate *self) {
  return self->metaObject();
}

//  QString QQuickRadioDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickRadioDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRadioDelegate::tr(s, c, n));
}

//  QQuickRadioDelegate::QQuickRadioDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRadioDelegate *ritual_ZN19QQuickRadioDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickRadioDelegate(parent);
}

//  QFont QQuickRadioDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickRadioDelegate11defaultFontEv(
    const QQuickRadioDelegate *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickRadioDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickRadioDelegate14accessibleRoleEv(
    const QQuickRadioDelegate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QFont QQuickRadioDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK19QQuickRadioDelegate11defaultFontEv(
    const QQuickRadioDelegate *self) {
  return new QFont(
      static_cast<const OwnQQuickRadioDelegate *>(self)->OwnQQuickRadioDelegate::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickRadioDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickRadioDelegate14accessibleRoleEv(
    const QQuickRadioDelegate *self) {
  return static_cast<const OwnQQuickRadioDelegate *>(self)->OwnQQuickRadioDelegate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
