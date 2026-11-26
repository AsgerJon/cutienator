//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuax509distinguishedname.h, Qt 6.12.0.
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
#include <QtOpcUa/qopcuax509distinguishedname.h>
#include <QtCore/qstring.h>

//  QOpcUaX509DistinguishedName::QOpcUaX509DistinguishedName()
extern "C" Q_DECL_EXPORT
QOpcUaX509DistinguishedName *ritual_ZN27QOpcUaX509DistinguishedNameC1Ev() {
  return new QOpcUaX509DistinguishedName();
}

//  QOpcUaX509DistinguishedName::QOpcUaX509DistinguishedName(const
//      QOpcUaX509DistinguishedName &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509DistinguishedName *ritual_ZN27QOpcUaX509DistinguishedNameC1ERKS_(
    const QOpcUaX509DistinguishedName *a0) {
  return new QOpcUaX509DistinguishedName(*a0);
}

//  QOpcUaX509DistinguishedName &QOpcUaX509DistinguishedName::operator=(const
//      QOpcUaX509DistinguishedName &a0)
extern "C" Q_DECL_EXPORT
QOpcUaX509DistinguishedName *ritual_ZN27QOpcUaX509DistinguishedNameaSERKS_(
    QOpcUaX509DistinguishedName *self,
    const QOpcUaX509DistinguishedName *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaX509DistinguishedName::operator==(const
//      QOpcUaX509DistinguishedName &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpcUaX509DistinguishedNameeqERKS_(
    const QOpcUaX509DistinguishedName *self,
    const QOpcUaX509DistinguishedName *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaX509DistinguishedName::~QOpcUaX509DistinguishedName()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaX509DistinguishedNameD1Ev(
    QOpcUaX509DistinguishedName *self) {
  delete self;
}

//  void QOpcUaX509DistinguishedName::setEntry(Type type, const QString
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaX509DistinguishedName8setEntryENS_4TypeERK7QString(
    QOpcUaX509DistinguishedName *self,
    QOpcUaX509DistinguishedName::Type type,
    const QString *value) {
  self->setEntry(type, *value);
}

//  QString QOpcUaX509DistinguishedName::entry(Type type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QOpcUaX509DistinguishedName5entryENS_4TypeE(
    const QOpcUaX509DistinguishedName *self,
    QOpcUaX509DistinguishedName::Type type) {
  return new QString(self->entry(type));
}

//  QString QOpcUaX509DistinguishedName::typeToOid(Type type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QOpcUaX509DistinguishedName9typeToOidENS_4TypeE(
    QOpcUaX509DistinguishedName::Type type) {
  return new QString(QOpcUaX509DistinguishedName::typeToOid(type));
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
