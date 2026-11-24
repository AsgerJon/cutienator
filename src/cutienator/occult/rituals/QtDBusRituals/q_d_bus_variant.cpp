//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusextratypes.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>

//  QDBusVariant::QDBusVariant()
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_ZN12QDBusVariantC1Ev() {
  return new QDBusVariant();
}

//  QDBusVariant::QDBusVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_ZN12QDBusVariantC1ERK8QVariant(
    const QVariant *variant) {
  return new QDBusVariant(*variant);
}

//  void QDBusVariant::setVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusVariant10setVariantERK8QVariant(
    QDBusVariant *self,
    const QVariant *variant) {
  self->setVariant(*variant);
}

//  QVariant QDBusVariant::variant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QDBusVariant7variantEv(const QDBusVariant *self) {
  return new QVariant(self->variant());
}

//  QDBusVariant::~QDBusVariant()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusVariantD1Ev(QDBusVariant *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
