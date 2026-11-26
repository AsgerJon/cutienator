//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuax509extensionextendedkeyusage.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtOpcUa/qtopcua-config.h> before the #if, as it defines
//  QT_CONFIG(gds); the long #if line split in two.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuaglobal.h>
#include <QtOpcUa/qtopcua-config.h>
#if QT_CONFIG(gds) && QT_CONFIG(openssl) \
    && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
#include <QtOpcUa/QtOpcUa>
#include <QtOpcUa/qopcuax509extensionextendedkeyusage.h>

//  QOpcUaX509ExtensionExtendedKeyUsage::QOpcUaX509ExtensionExtendedKeyUsage(
//      )
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionExtendedKeyUsage *ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsageC1Ev() {
  return new QOpcUaX509ExtensionExtendedKeyUsage();
}

//  QOpcUaX509ExtensionExtendedKeyUsage::QOpcUaX509ExtensionExtendedKeyUsage(
//      const QOpcUaX509ExtensionExtendedKeyUsage &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionExtendedKeyUsage *ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsageC1ERKS_(
    const QOpcUaX509ExtensionExtendedKeyUsage *a0) {
  return new QOpcUaX509ExtensionExtendedKeyUsage(*a0);
}

//  QOpcUaX509ExtensionExtendedKeyUsage
//      &QOpcUaX509ExtensionExtendedKeyUsage::operator=(const
//      QOpcUaX509ExtensionExtendedKeyUsage &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionExtendedKeyUsage *ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsageaSERKS_(
    QOpcUaX509ExtensionExtendedKeyUsage *self,
    const QOpcUaX509ExtensionExtendedKeyUsage *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaX509ExtensionExtendedKeyUsage::operator==(const
//      QOpcUaX509ExtensionExtendedKeyUsage &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QOpcUaX509ExtensionExtendedKeyUsageeqERKS_(
    const QOpcUaX509ExtensionExtendedKeyUsage *self,
    const QOpcUaX509ExtensionExtendedKeyUsage *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaX509ExtensionExtendedKeyUsage::~QOpcUaX509ExtensionExtendedKeyUsage
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsageD1Ev(
    QOpcUaX509ExtensionExtendedKeyUsage *self) {
  delete self;
}

//  void QOpcUaX509ExtensionExtendedKeyUsage::setKeyUsage(KeyUsage keyUsage,
//      bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsage11setKeyUsageENS_8KeyUsageEb(
    QOpcUaX509ExtensionExtendedKeyUsage *self,
    QOpcUaX509ExtensionExtendedKeyUsage::KeyUsage keyUsage,
    bool enable) {
  self->setKeyUsage(keyUsage, enable);
}

//  bool QOpcUaX509ExtensionExtendedKeyUsage::keyUsage(KeyUsage a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QOpcUaX509ExtensionExtendedKeyUsage8keyUsageENS_8KeyUsageE(
    const QOpcUaX509ExtensionExtendedKeyUsage *self,
    QOpcUaX509ExtensionExtendedKeyUsage::KeyUsage a0) {
  return self->keyUsage(a0);
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
