//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qocspresponse.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
#include <QtNetwork/qocspresponse.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qlist.h>

//  QOcspResponse::QOcspResponse()
extern "C" Q_DECL_EXPORT
QOcspResponse *ritual_ZN13QOcspResponseC1Ev() {
  return new QOcspResponse();
}

//  QOcspResponse::QOcspResponse(const QOcspResponse &other)
extern "C" Q_DECL_EXPORT
QOcspResponse *ritual_ZN13QOcspResponseC1ERKS_(const QOcspResponse *other) {
  return new QOcspResponse(*other);
}

//  QOcspResponse::~QOcspResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOcspResponseD1Ev(QOcspResponse *self) {
  delete self;
}

//  QOcspCertificateStatus QOcspResponse::certificateStatus() const
extern "C" Q_DECL_EXPORT
QOcspCertificateStatus ritual_ZNK13QOcspResponse17certificateStatusEv(
    const QOcspResponse *self) {
  return self->certificateStatus();
}

//  QOcspRevocationReason QOcspResponse::revocationReason() const
extern "C" Q_DECL_EXPORT
QOcspRevocationReason ritual_ZNK13QOcspResponse16revocationReasonEv(
    const QOcspResponse *self) {
  return self->revocationReason();
}

//  QSslCertificate QOcspResponse::subject() const
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZNK13QOcspResponse7subjectEv(
    const QOcspResponse *self) {
  return new QSslCertificate(self->subject());
}

//  bool QOcspResponse::isEqual(const QOcspResponse &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOcspResponse7isEqualERKS_(
    const QOcspResponse *self,
    const QOcspResponse *other) {
  return self->isEqual(*other);
}

//  bool operator==(const QOcspResponse &lhs, const QOcspResponse &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QOcspResponseS1_(
    const QOcspResponse *lhs,
    const QOcspResponse *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOcspResponse &lhs, const QOcspResponse &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QOcspResponseS1_(
    const QOcspResponse *lhs,
    const QOcspResponse *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOcspResponse>::QList()
extern "C" Q_DECL_EXPORT
QList<QOcspResponse> *ritual_list_make_QOcspResponse() {
  return new QList<QOcspResponse>();
}

//  void QList<QOcspResponse>::append(const QOcspResponse &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOcspResponse(
    QList<QOcspResponse> *self,
    const QOcspResponse *element) {
  self->append(*element);
}

//  qsizetype QList<QOcspResponse>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOcspResponse(const QList<QOcspResponse> *self) {
  return self->size();
}

//  const QOcspResponse &QList<QOcspResponse>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOcspResponse *ritual_list_at_QOcspResponse(
    const QList<QOcspResponse> *self,
    long long index) {
  return new QOcspResponse(self->at(index));
}

//  QList<QOcspResponse>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOcspResponse(QList<QOcspResponse> *self) {
  delete self;
}

#endif  // QT_CONFIG(ssl)
#endif  // QT_CONFIG(ssl)
