//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qndefnfcsmartposterrecord.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qndefnfcsmartposterrecord.h>
#include <QtNfc/qndefrecord.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtNfc/qndefnfctextrecord.h>
#include <QtCore/qurl.h>
#include <QtNfc/qndefnfcurirecord.h>
#include <QtCore/qlist.h>

//  QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord()
extern "C" Q_DECL_EXPORT
QNdefNfcSmartPosterRecord *ritual_ZN25QNdefNfcSmartPosterRecordC1Ev() {
  return new QNdefNfcSmartPosterRecord();
}

//  QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord(const QNdefRecord
//      &other)
extern "C" Q_DECL_EXPORT
QNdefNfcSmartPosterRecord *ritual_ZN25QNdefNfcSmartPosterRecordC1ERK11QNdefRecord(
    const QNdefRecord *other) {
  return new QNdefNfcSmartPosterRecord(*other);
}

//  QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord(const
//      QNdefNfcSmartPosterRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcSmartPosterRecord *ritual_ZN25QNdefNfcSmartPosterRecordC1ERKS_(
    const QNdefNfcSmartPosterRecord *other) {
  return new QNdefNfcSmartPosterRecord(*other);
}

//  QNdefNfcSmartPosterRecord &QNdefNfcSmartPosterRecord::operator=(const
//      QNdefNfcSmartPosterRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcSmartPosterRecord *ritual_ZN25QNdefNfcSmartPosterRecordaSERKS_(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcSmartPosterRecord *other) {
  return &(self->operator=(*other));
}

//  QNdefNfcSmartPosterRecord::~QNdefNfcSmartPosterRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecordD1Ev(
    QNdefNfcSmartPosterRecord *self) {
  delete self;
}

//  void QNdefNfcSmartPosterRecord::setPayload(const QByteArray &payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord10setPayloadERK10QByteArray(
    QNdefNfcSmartPosterRecord *self,
    const QByteArray *payload) {
  self->setPayload(*payload);
}

//  bool QNdefNfcSmartPosterRecord::hasTitle(const QString &locale) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QNdefNfcSmartPosterRecord8hasTitleERK7QString(
    const QNdefNfcSmartPosterRecord *self,
    const QString *locale) {
  return self->hasTitle(*locale);
}

//  bool QNdefNfcSmartPosterRecord::hasAction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QNdefNfcSmartPosterRecord9hasActionEv(
    const QNdefNfcSmartPosterRecord *self) {
  return self->hasAction();
}

//  bool QNdefNfcSmartPosterRecord::hasIcon(const QByteArray &mimetype) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QNdefNfcSmartPosterRecord7hasIconERK10QByteArray(
    const QNdefNfcSmartPosterRecord *self,
    const QByteArray *mimetype) {
  return self->hasIcon(*mimetype);
}

//  bool QNdefNfcSmartPosterRecord::hasSize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QNdefNfcSmartPosterRecord7hasSizeEv(
    const QNdefNfcSmartPosterRecord *self) {
  return self->hasSize();
}

//  bool QNdefNfcSmartPosterRecord::hasTypeInfo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QNdefNfcSmartPosterRecord11hasTypeInfoEv(
    const QNdefNfcSmartPosterRecord *self) {
  return self->hasTypeInfo();
}

//  qsizetype QNdefNfcSmartPosterRecord::titleCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK25QNdefNfcSmartPosterRecord10titleCountEv(
    const QNdefNfcSmartPosterRecord *self) {
  return self->titleCount();
}

//  QNdefNfcTextRecord QNdefNfcSmartPosterRecord::titleRecord(qsizetype
//      index) const
extern "C" Q_DECL_EXPORT
QNdefNfcTextRecord *ritual_ZNK25QNdefNfcSmartPosterRecord11titleRecordEx(
    const QNdefNfcSmartPosterRecord *self,
    qsizetype index) {
  return new QNdefNfcTextRecord(self->titleRecord(index));
}

//  QString QNdefNfcSmartPosterRecord::title(const QString &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QNdefNfcSmartPosterRecord5titleERK7QString(
    const QNdefNfcSmartPosterRecord *self,
    const QString *locale) {
  return new QString(self->title(*locale));
}

//  QList<QNdefNfcTextRecord> QNdefNfcSmartPosterRecord::titleRecords() const
extern "C" Q_DECL_EXPORT
QList<QNdefNfcTextRecord> *ritual_ZNK25QNdefNfcSmartPosterRecord12titleRecordsEv(
    const QNdefNfcSmartPosterRecord *self) {
  return new QList<QNdefNfcTextRecord>(self->titleRecords());
}

//  bool QNdefNfcSmartPosterRecord::addTitle(const QNdefNfcTextRecord &text)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNdefNfcSmartPosterRecord8addTitleERK18QNdefNfcTextRecord(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcTextRecord *text) {
  return self->addTitle(*text);
}

//  bool QNdefNfcSmartPosterRecord::addTitle(const QString &text, const
//      QString &locale, QNdefNfcTextRecord::Encoding encoding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNdefNfcSmartPosterRecord8addTitleERK7QStringS2_N18QNdefNfcTextRecord8EncodingE(
    QNdefNfcSmartPosterRecord *self,
    const QString *text,
    const QString *locale,
    QNdefNfcTextRecord::Encoding encoding) {
  return self->addTitle(*text, *locale, encoding);
}

//  bool QNdefNfcSmartPosterRecord::removeTitle(const QNdefNfcTextRecord
//      &text)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNdefNfcSmartPosterRecord11removeTitleERK18QNdefNfcTextRecord(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcTextRecord *text) {
  return self->removeTitle(*text);
}

//  bool QNdefNfcSmartPosterRecord::removeTitle(const QString &locale)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNdefNfcSmartPosterRecord11removeTitleERK7QString(
    QNdefNfcSmartPosterRecord *self,
    const QString *locale) {
  return self->removeTitle(*locale);
}

//  void QNdefNfcSmartPosterRecord::setTitles(const QList<QNdefNfcTextRecord>
//      &titles)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord9setTitlesERK5QListI18QNdefNfcTextRecordE(
    QNdefNfcSmartPosterRecord *self,
    const QList<QNdefNfcTextRecord> *titles) {
  self->setTitles(*titles);
}

//  QUrl QNdefNfcSmartPosterRecord::uri() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QNdefNfcSmartPosterRecord3uriEv(
    const QNdefNfcSmartPosterRecord *self) {
  return new QUrl(self->uri());
}

//  QNdefNfcUriRecord QNdefNfcSmartPosterRecord::uriRecord() const
extern "C" Q_DECL_EXPORT
QNdefNfcUriRecord *ritual_ZNK25QNdefNfcSmartPosterRecord9uriRecordEv(
    const QNdefNfcSmartPosterRecord *self) {
  return new QNdefNfcUriRecord(self->uriRecord());
}

//  void QNdefNfcSmartPosterRecord::setUri(const QNdefNfcUriRecord &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord6setUriERK17QNdefNfcUriRecord(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcUriRecord *url) {
  self->setUri(*url);
}

//  void QNdefNfcSmartPosterRecord::setUri(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord6setUriERK4QUrl(
    QNdefNfcSmartPosterRecord *self,
    const QUrl *url) {
  self->setUri(*url);
}

//  Action QNdefNfcSmartPosterRecord::action() const
extern "C" Q_DECL_EXPORT
QNdefNfcSmartPosterRecord::Action ritual_ZNK25QNdefNfcSmartPosterRecord6actionEv(
    const QNdefNfcSmartPosterRecord *self) {
  return self->action();
}

//  void QNdefNfcSmartPosterRecord::setAction(Action act)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord9setActionENS_6ActionE(
    QNdefNfcSmartPosterRecord *self,
    QNdefNfcSmartPosterRecord::Action act) {
  self->setAction(act);
}

//  qsizetype QNdefNfcSmartPosterRecord::iconCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK25QNdefNfcSmartPosterRecord9iconCountEv(
    const QNdefNfcSmartPosterRecord *self) {
  return self->iconCount();
}

//  QNdefNfcIconRecord QNdefNfcSmartPosterRecord::iconRecord(qsizetype index)
//      const
extern "C" Q_DECL_EXPORT
QNdefNfcIconRecord *ritual_ZNK25QNdefNfcSmartPosterRecord10iconRecordEx(
    const QNdefNfcSmartPosterRecord *self,
    qsizetype index) {
  return new QNdefNfcIconRecord(self->iconRecord(index));
}

//  QByteArray QNdefNfcSmartPosterRecord::icon(const QByteArray &mimetype)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QNdefNfcSmartPosterRecord4iconERK10QByteArray(
    const QNdefNfcSmartPosterRecord *self,
    const QByteArray *mimetype) {
  return new QByteArray(self->icon(*mimetype));
}

//  QList<QNdefNfcIconRecord> QNdefNfcSmartPosterRecord::iconRecords() const
extern "C" Q_DECL_EXPORT
QList<QNdefNfcIconRecord> *ritual_ZNK25QNdefNfcSmartPosterRecord11iconRecordsEv(
    const QNdefNfcSmartPosterRecord *self) {
  return new QList<QNdefNfcIconRecord>(self->iconRecords());
}

//  void QNdefNfcSmartPosterRecord::addIcon(const QNdefNfcIconRecord &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord7addIconERK18QNdefNfcIconRecord(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcIconRecord *icon) {
  self->addIcon(*icon);
}

//  void QNdefNfcSmartPosterRecord::addIcon(const QByteArray &type, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord7addIconERK10QByteArrayS2_(
    QNdefNfcSmartPosterRecord *self,
    const QByteArray *type,
    const QByteArray *data) {
  self->addIcon(*type, *data);
}

//  bool QNdefNfcSmartPosterRecord::removeIcon(const QNdefNfcIconRecord
//      &icon)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNdefNfcSmartPosterRecord10removeIconERK18QNdefNfcIconRecord(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcIconRecord *icon) {
  return self->removeIcon(*icon);
}

//  bool QNdefNfcSmartPosterRecord::removeIcon(const QByteArray &type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNdefNfcSmartPosterRecord10removeIconERK10QByteArray(
    QNdefNfcSmartPosterRecord *self,
    const QByteArray *type) {
  return self->removeIcon(*type);
}

//  void QNdefNfcSmartPosterRecord::setIcons(const QList<QNdefNfcIconRecord>
//      &icons)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord8setIconsERK5QListI18QNdefNfcIconRecordE(
    QNdefNfcSmartPosterRecord *self,
    const QList<QNdefNfcIconRecord> *icons) {
  self->setIcons(*icons);
}

//  quint32 QNdefNfcSmartPosterRecord::size() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK25QNdefNfcSmartPosterRecord4sizeEv(
    const QNdefNfcSmartPosterRecord *self) {
  return self->size();
}

//  void QNdefNfcSmartPosterRecord::setSize(quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord7setSizeEj(
    QNdefNfcSmartPosterRecord *self,
    quint32 size) {
  self->setSize(size);
}

//  QString QNdefNfcSmartPosterRecord::typeInfo() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QNdefNfcSmartPosterRecord8typeInfoEv(
    const QNdefNfcSmartPosterRecord *self) {
  return new QString(self->typeInfo());
}

//  void QNdefNfcSmartPosterRecord::setTypeInfo(const QString &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord11setTypeInfoERK7QString(
    QNdefNfcSmartPosterRecord *self,
    const QString *type) {
  self->setTypeInfo(*type);
}

//  void QNdefNfcSmartPosterRecord::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord7cleanupEv(
    QNdefNfcSmartPosterRecord *self) {
  self->cleanup();
}

//  void QNdefNfcSmartPosterRecord::convertToPayload()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord16convertToPayloadEv(
    QNdefNfcSmartPosterRecord *self) {
  self->convertToPayload();
}

//  bool QNdefNfcSmartPosterRecord::addTitleInternal(const QNdefNfcTextRecord
//      &text)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNdefNfcSmartPosterRecord16addTitleInternalERK18QNdefNfcTextRecord(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcTextRecord *text) {
  return self->addTitleInternal(*text);
}

//  void QNdefNfcSmartPosterRecord::addIconInternal(const QNdefNfcIconRecord
//      &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNdefNfcSmartPosterRecord15addIconInternalERK18QNdefNfcIconRecord(
    QNdefNfcSmartPosterRecord *self,
    const QNdefNfcIconRecord *icon) {
  self->addIconInternal(*icon);
}
