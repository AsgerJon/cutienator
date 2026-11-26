//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuax509extension.h, Qt 6.12.0.
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
#include <QtOpcUa/qopcuax509extension.h>

//  QOpcUaX509Extension::QOpcUaX509Extension()
extern "C" Q_DECL_EXPORT
QOpcUaX509Extension *ritual_ZN19QOpcUaX509ExtensionC1Ev() {
  return new QOpcUaX509Extension();
}

//  QOpcUaX509Extension::QOpcUaX509Extension(const QOpcUaX509Extension &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509Extension *ritual_ZN19QOpcUaX509ExtensionC1ERKS_(
    const QOpcUaX509Extension *a0) {
  return new QOpcUaX509Extension(*a0);
}

//  QOpcUaX509Extension &QOpcUaX509Extension::operator=(const
//      QOpcUaX509Extension &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509Extension *ritual_ZN19QOpcUaX509ExtensionaSERKS_(
    QOpcUaX509Extension *self,
    const QOpcUaX509Extension *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaX509Extension::operator==(const QOpcUaX509Extension &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpcUaX509ExtensioneqERKS_(
    const QOpcUaX509Extension *self,
    const QOpcUaX509Extension *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaX509Extension::~QOpcUaX509Extension()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaX509ExtensionD1Ev(QOpcUaX509Extension *self) {
  delete self;
}

//  void QOpcUaX509Extension::setCritical(bool critical)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaX509Extension11setCriticalEb(
    QOpcUaX509Extension *self,
    bool critical) {
  self->setCritical(critical);
}

//  bool QOpcUaX509Extension::critical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpcUaX509Extension8criticalEv(
    const QOpcUaX509Extension *self) {
  return self->critical();
}

//  QOpcUaX509Extension::QOpcUaX509Extension(QOpcUaX509ExtensionData *a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509Extension *ritual_ZN19QOpcUaX509ExtensionC1EP23QOpcUaX509ExtensionData(
    QOpcUaX509ExtensionData *a0) {
  return new QOpcUaX509Extension(a0);
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
