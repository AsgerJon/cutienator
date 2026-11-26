//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuax509extensionbasicconstraints.h, Qt 6.12.0.
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
#include <QtOpcUa/qopcuax509extensionbasicconstraints.h>

//  QOpcUaX509ExtensionBasicConstraints::QOpcUaX509ExtensionBasicConstraints(
//      )
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionBasicConstraints *ritual_ZN35QOpcUaX509ExtensionBasicConstraintsC1Ev() {
  return new QOpcUaX509ExtensionBasicConstraints();
}

//  QOpcUaX509ExtensionBasicConstraints::QOpcUaX509ExtensionBasicConstraints(
//      const QOpcUaX509ExtensionBasicConstraints &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionBasicConstraints *ritual_ZN35QOpcUaX509ExtensionBasicConstraintsC1ERKS_(
    const QOpcUaX509ExtensionBasicConstraints *a0) {
  return new QOpcUaX509ExtensionBasicConstraints(*a0);
}

//  QOpcUaX509ExtensionBasicConstraints
//      &QOpcUaX509ExtensionBasicConstraints::operator=(const
//      QOpcUaX509ExtensionBasicConstraints &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509ExtensionBasicConstraints *ritual_ZN35QOpcUaX509ExtensionBasicConstraintsaSERKS_(
    QOpcUaX509ExtensionBasicConstraints *self,
    const QOpcUaX509ExtensionBasicConstraints *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaX509ExtensionBasicConstraints::operator==(const
//      QOpcUaX509ExtensionBasicConstraints &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QOpcUaX509ExtensionBasicConstraintseqERKS_(
    const QOpcUaX509ExtensionBasicConstraints *self,
    const QOpcUaX509ExtensionBasicConstraints *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaX509ExtensionBasicConstraints::~QOpcUaX509ExtensionBasicConstraints
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509ExtensionBasicConstraintsD1Ev(
    QOpcUaX509ExtensionBasicConstraints *self) {
  delete self;
}

//  void QOpcUaX509ExtensionBasicConstraints::setCa(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509ExtensionBasicConstraints5setCaEb(
    QOpcUaX509ExtensionBasicConstraints *self,
    bool value) {
  self->setCa(value);
}

//  bool QOpcUaX509ExtensionBasicConstraints::ca() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QOpcUaX509ExtensionBasicConstraints2caEv(
    const QOpcUaX509ExtensionBasicConstraints *self) {
  return self->ca();
}

//  void QOpcUaX509ExtensionBasicConstraints::setPathLength(int length)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaX509ExtensionBasicConstraints13setPathLengthEi(
    QOpcUaX509ExtensionBasicConstraints *self,
    int length) {
  self->setPathLength(length);
}

//  int QOpcUaX509ExtensionBasicConstraints::pathLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK35QOpcUaX509ExtensionBasicConstraints10pathLengthEv(
    const QOpcUaX509ExtensionBasicConstraints *self) {
  return self->pathLength();
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
