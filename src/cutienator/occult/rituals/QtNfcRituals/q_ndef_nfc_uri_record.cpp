//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qndefnfcurirecord.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qndefnfcurirecord.h>
#include <QtNfc/qndefrecord.h>
#include <QtCore/qurl.h>

#if !defined(Q_QDOC)
//  QNdefNfcUriRecord::QNdefNfcUriRecord()
extern "C" Q_DECL_EXPORT
QNdefNfcUriRecord *ritual_ZN17QNdefNfcUriRecordC1Ev() {
  return new QNdefNfcUriRecord();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QNdefNfcUriRecord::QNdefNfcUriRecord(const QNdefRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcUriRecord *ritual_ZN17QNdefNfcUriRecordC1ERK11QNdefRecord(
    const QNdefRecord *other) {
  return new QNdefNfcUriRecord(*other);
}
#endif  // !defined(Q_QDOC)

//  QUrl QNdefNfcUriRecord::uri() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QNdefNfcUriRecord3uriEv(const QNdefNfcUriRecord *self) {
  return new QUrl(self->uri());
}

//  void QNdefNfcUriRecord::setUri(const QUrl &uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNdefNfcUriRecord6setUriERK4QUrl(
    QNdefNfcUriRecord *self,
    const QUrl *uri) {
  self->setUri(*uri);
}

//  QNdefNfcUriRecord::~QNdefNfcUriRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNdefNfcUriRecordD1Ev(QNdefNfcUriRecord *self) {
  delete self;
}
