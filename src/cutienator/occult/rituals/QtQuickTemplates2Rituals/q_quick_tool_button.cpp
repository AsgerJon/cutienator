//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktoolbutton_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktoolbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickToolButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickToolButton : QQuickToolButton {
  using QQuickToolButton::defaultFont;
};

//  const QMetaObject *QQuickToolButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickToolButton10metaObjectEv(
    const QQuickToolButton *self) {
  return self->metaObject();
}

//  QString QQuickToolButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickToolButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickToolButton::tr(s, c, n));
}

//  QQuickToolButton::QQuickToolButton(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickToolButton *ritual_ZN16QQuickToolButtonC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickToolButton(parent);
}

//  QFont QQuickToolButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16QQuickToolButton11defaultFontEv(
    const QQuickToolButton *self) {
  return new QFont(self->defaultFont());
}

//  QFont QQuickToolButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK16QQuickToolButton11defaultFontEv(
    const QQuickToolButton *self) {
  return new QFont(
      static_cast<const OwnQQuickToolButton *>(self)->OwnQQuickToolButton::defaultFont());
}
