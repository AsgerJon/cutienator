//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbutton_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickButton : QQuickButton {
  using QQuickButton::defaultFont;
};

//  const QMetaObject *QQuickButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickButton10metaObjectEv(
    const QQuickButton *self) {
  return self->metaObject();
}

//  QString QQuickButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickButton::tr(s, c, n));
}

//  QQuickButton::QQuickButton(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickButton *ritual_ZN12QQuickButtonC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickButton(parent);
}

//  bool QQuickButton::isHighlighted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickButton13isHighlightedEv(const QQuickButton *self) {
  return self->isHighlighted();
}

//  void QQuickButton::setHighlighted(bool highlighted)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickButton14setHighlightedEb(
    QQuickButton *self,
    bool highlighted) {
  self->setHighlighted(highlighted);
}

//  bool QQuickButton::isFlat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickButton6isFlatEv(const QQuickButton *self) {
  return self->isFlat();
}

//  void QQuickButton::setFlat(bool flat)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickButton7setFlatEb(QQuickButton *self, bool flat) {
  self->setFlat(flat);
}

//  QFont QQuickButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QQuickButton11defaultFontEv(const QQuickButton *self) {
  return new QFont(self->defaultFont());
}

//  QQuickButtonPrivate *QQuickButton::d_func()
extern "C" Q_DECL_EXPORT
QQuickButtonPrivate *ritual_ZN12QQuickButton6d_funcEv(QQuickButton *self) {
  return self->d_func();
}

//  const QQuickButtonPrivate *QQuickButton::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickButtonPrivate *ritual_ZNK12QQuickButton6d_funcEv(
    const QQuickButton *self) {
  return self->d_func();
}

//  QFont QQuickButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK12QQuickButton11defaultFontEv(
    const QQuickButton *self) {
  return new QFont(
      static_cast<const OwnQQuickButton *>(self)->OwnQQuickButton::defaultFont());
}
