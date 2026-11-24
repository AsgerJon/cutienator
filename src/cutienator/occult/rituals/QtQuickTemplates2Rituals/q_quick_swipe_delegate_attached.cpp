//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickSwipeDelegateAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickSwipeDelegateAttached10metaObjectEv(
    const QQuickSwipeDelegateAttached *self) {
  return self->metaObject();
}

//  QString QQuickSwipeDelegateAttached::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuickSwipeDelegateAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSwipeDelegateAttached::tr(s, c, n));
}

//  QQuickSwipeDelegateAttached::QQuickSwipeDelegateAttached(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickSwipeDelegateAttached *ritual_ZN27QQuickSwipeDelegateAttachedC1EP7QObject(
    QObject *object) {
  return new QQuickSwipeDelegateAttached(object);
}

//  bool QQuickSwipeDelegateAttached::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickSwipeDelegateAttached9isPressedEv(
    const QQuickSwipeDelegateAttached *self) {
  return self->isPressed();
}

//  void QQuickSwipeDelegateAttached::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickSwipeDelegateAttached10setPressedEb(
    QQuickSwipeDelegateAttached *self,
    bool pressed) {
  self->setPressed(pressed);
}
