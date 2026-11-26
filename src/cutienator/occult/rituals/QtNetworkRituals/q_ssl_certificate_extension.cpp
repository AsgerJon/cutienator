//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslcertificateextension.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtNetwork/qsslcertificateextension.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QSslCertificateExtension::QSslCertificateExtension()
extern "C" Q_DECL_EXPORT
QSslCertificateExtension *ritual_ZN24QSslCertificateExtensionC1Ev() {
  return new QSslCertificateExtension();
}

//  QSslCertificateExtension::QSslCertificateExtension(const
//      QSslCertificateExtension &other)
extern "C" Q_DECL_EXPORT
QSslCertificateExtension *ritual_ZN24QSslCertificateExtensionC1ERKS_(
    const QSslCertificateExtension *other) {
  return new QSslCertificateExtension(*other);
}

//  QSslCertificateExtension
//      &QSslCertificateExtension::operator=(QSslCertificateExtension
//      &&other)
extern "C" Q_DECL_EXPORT
QSslCertificateExtension *ritual_ZN24QSslCertificateExtensionaSEOS_(
    QSslCertificateExtension *self,
    QSslCertificateExtension *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSslCertificateExtension &QSslCertificateExtension::operator=(const
//      QSslCertificateExtension &other)
extern "C" Q_DECL_EXPORT
QSslCertificateExtension *ritual_ZN24QSslCertificateExtensionaSERKS_(
    QSslCertificateExtension *self,
    const QSslCertificateExtension *other) {
  return &(self->operator=(*other));
}

//  QSslCertificateExtension::~QSslCertificateExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSslCertificateExtensionD1Ev(
    QSslCertificateExtension *self) {
  delete self;
}

//  void QSslCertificateExtension::swap(QSslCertificateExtension &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSslCertificateExtension4swapERS_(
    QSslCertificateExtension *self,
    QSslCertificateExtension *other) {
  self->swap(*other);
}

//  QString QSslCertificateExtension::oid() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QSslCertificateExtension3oidEv(
    const QSslCertificateExtension *self) {
  return new QString(self->oid());
}

//  QString QSslCertificateExtension::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QSslCertificateExtension4nameEv(
    const QSslCertificateExtension *self) {
  return new QString(self->name());
}

//  QVariant QSslCertificateExtension::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QSslCertificateExtension5valueEv(
    const QSslCertificateExtension *self) {
  return new QVariant(self->value());
}

//  bool QSslCertificateExtension::isCritical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSslCertificateExtension10isCriticalEv(
    const QSslCertificateExtension *self) {
  return self->isCritical();
}

//  bool QSslCertificateExtension::isSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSslCertificateExtension11isSupportedEv(
    const QSslCertificateExtension *self) {
  return self->isSupported();
}

//  QList<QSslCertificateExtension>::QList()
extern "C" Q_DECL_EXPORT
QList<QSslCertificateExtension> *ritual_list_make_QSslCertificateExtension() {
  return new QList<QSslCertificateExtension>();
}

//  void QList<QSslCertificateExtension>::append(const
//      QSslCertificateExtension &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSslCertificateExtension(
    QList<QSslCertificateExtension> *self,
    const QSslCertificateExtension *element) {
  self->append(*element);
}

//  qsizetype QList<QSslCertificateExtension>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSslCertificateExtension(
    const QList<QSslCertificateExtension> *self) {
  return self->size();
}

//  const QSslCertificateExtension
//      &QList<QSslCertificateExtension>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSslCertificateExtension *ritual_list_at_QSslCertificateExtension(
    const QList<QSslCertificateExtension> *self,
    long long index) {
  return new QSslCertificateExtension(self->at(index));
}

//  QList<QSslCertificateExtension>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSslCertificateExtension(
    QList<QSslCertificateExtension> *self) {
  delete self;
}
