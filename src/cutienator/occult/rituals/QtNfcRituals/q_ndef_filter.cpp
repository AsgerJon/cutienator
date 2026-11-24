//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qndeffilter.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qndeffilter.h>
#include <QtCore/qbytearray.h>
#include <QtNfc/qndefmessage.h>

//  QNdefFilter::QNdefFilter()
extern "C" Q_DECL_EXPORT
QNdefFilter *ritual_ZN11QNdefFilterC1Ev() {
  return new QNdefFilter();
}

//  QNdefFilter::QNdefFilter(const QNdefFilter &other)
extern "C" Q_DECL_EXPORT
QNdefFilter *ritual_ZN11QNdefFilterC1ERKS_(const QNdefFilter *other) {
  return new QNdefFilter(*other);
}

//  QNdefFilter::~QNdefFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefFilterD1Ev(QNdefFilter *self) {
  delete self;
}

//  void QNdefFilter::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefFilter5clearEv(QNdefFilter *self) {
  self->clear();
}

//  void QNdefFilter::setOrderMatch(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefFilter13setOrderMatchEb(QNdefFilter *self, bool on) {
  self->setOrderMatch(on);
}

//  bool QNdefFilter::orderMatch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QNdefFilter10orderMatchEv(const QNdefFilter *self) {
  return self->orderMatch();
}

//  bool QNdefFilter::appendRecord(QNdefRecord::TypeNameFormat
//      typeNameFormat, const QByteArray &type, unsigned int min, unsigned
//      int max)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QNdefFilter12appendRecordEN11QNdefRecord14TypeNameFormatERK10QByteArrayjj(
    QNdefFilter *self,
    QNdefRecord::TypeNameFormat typeNameFormat,
    const QByteArray *type,
    unsigned int min,
    unsigned int max) {
  return self->appendRecord(typeNameFormat, *type, min, max);
}

//  bool QNdefFilter::appendRecord(const Record &record)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QNdefFilter12appendRecordERKNS_6RecordE(
    QNdefFilter *self,
    const QNdefFilter::Record *record) {
  return self->appendRecord(*record);
}

//  qsizetype QNdefFilter::recordCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QNdefFilter11recordCountEv(const QNdefFilter *self) {
  return self->recordCount();
}

//  Record QNdefFilter::recordAt(qsizetype i) const
extern "C" Q_DECL_EXPORT
QNdefFilter::Record *ritual_ZNK11QNdefFilter8recordAtEx(
    const QNdefFilter *self,
    qsizetype i) {
  return new QNdefFilter::Record(self->recordAt(i));
}

//  bool QNdefFilter::match(const QNdefMessage &message) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QNdefFilter5matchERK12QNdefMessage(
    const QNdefFilter *self,
    const QNdefMessage *message) {
  return self->match(*message);
}
