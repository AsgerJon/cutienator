//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuax509extensionkeyusage.h, Qt 6.12.0.
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
#include <QtOpcUa/qopcuax509extensionkeyusage.h>

//  QOpcUaX509ExtensionKeyUsage::QOpcUaX509ExtensionKeyUsage()
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionKeyUsage *ritual_ZN27QOpcUaX509ExtensionKeyUsageC1Ev() {
  return new QOpcUaX509ExtensionKeyUsage();
}

//  QOpcUaX509ExtensionKeyUsage::QOpcUaX509ExtensionKeyUsage(const
//      QOpcUaX509ExtensionKeyUsage &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionKeyUsage *ritual_ZN27QOpcUaX509ExtensionKeyUsageC1ERKS_(
    const QOpcUaX509ExtensionKeyUsage *a0) {
  return new QOpcUaX509ExtensionKeyUsage(*a0);
}

//  QOpcUaX509ExtensionKeyUsage &QOpcUaX509ExtensionKeyUsage::operator=(const
//      QOpcUaX509ExtensionKeyUsage &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionKeyUsage *ritual_ZN27QOpcUaX509ExtensionKeyUsageaSERKS_(
    QOpcUaX509ExtensionKeyUsage *self,
    const QOpcUaX509ExtensionKeyUsage *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaX509ExtensionKeyUsage::operator==(const
//      QOpcUaX509ExtensionKeyUsage &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpcUaX509ExtensionKeyUsageeqERKS_(
    const QOpcUaX509ExtensionKeyUsage *self,
    const QOpcUaX509ExtensionKeyUsage *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaX509ExtensionKeyUsage::~QOpcUaX509ExtensionKeyUsage()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaX509ExtensionKeyUsageD1Ev(
    QOpcUaX509ExtensionKeyUsage *self) {
  delete self;
}

//  void QOpcUaX509ExtensionKeyUsage::setKeyUsage(KeyUsage keyUsage, bool
//      enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaX509ExtensionKeyUsage11setKeyUsageENS_8KeyUsageEb(
    QOpcUaX509ExtensionKeyUsage *self,
    QOpcUaX509ExtensionKeyUsage::KeyUsage keyUsage,
    bool enable) {
  self->setKeyUsage(keyUsage, enable);
}

//  bool QOpcUaX509ExtensionKeyUsage::keyUsage(KeyUsage a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpcUaX509ExtensionKeyUsage8keyUsageENS_8KeyUsageE(
    const QOpcUaX509ExtensionKeyUsage *self,
    QOpcUaX509ExtensionKeyUsage::KeyUsage a0) {
  return self->keyUsage(a0);
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
