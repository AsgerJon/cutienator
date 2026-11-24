//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QGeoMapType::QGeoMapType()
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_ZN11QGeoMapTypeC1Ev() {
  return new QGeoMapType();
}

//  QGeoMapType::QGeoMapType(const QGeoMapType &other)
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_ZN11QGeoMapTypeC1ERKS_(const QGeoMapType *other) {
  return new QGeoMapType(*other);
}

//  QGeoMapType::QGeoMapType(MapStyle style, const QString &name, const
//      QString &description, bool mobile, bool night, int mapId, const
//      QByteArray &pluginName, const QGeoCameraCapabilities
//      &cameraCapabilities, const QVariantMap &metadata)
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_ZN11QGeoMapTypeC1ENS_8MapStyleERK7QStringS3_bbiRK10QByteArrayRK22QGeoCameraCapabilitiesRK4QMapIS1_8QVariantE(
    QGeoMapType::MapStyle style,
    const QString *name,
    const QString *description,
    bool mobile,
    bool night,
    int mapId,
    const QByteArray *pluginName,
    const QGeoCameraCapabilities *cameraCapabilities,
    const QMap<QString, QVariant> *metadata) {
  return new QGeoMapType(
      style,
      *name,
      *description,
      mobile,
      night,
      mapId,
      *pluginName,
      *cameraCapabilities,
      *metadata);
}

//  QGeoMapType::~QGeoMapType()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoMapTypeD1Ev(QGeoMapType *self) {
  delete self;
}

//  bool operator==(const QGeoMapType &lhs, const QGeoMapType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QGeoMapTypeS1_(
    const QGeoMapType *lhs,
    const QGeoMapType *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoMapType &lhs, const QGeoMapType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QGeoMapTypeS1_(
    const QGeoMapType *lhs,
    const QGeoMapType *rhs) {
  return operator!=(*lhs, *rhs);
}

//  MapStyle QGeoMapType::style() const
extern "C" Q_DECL_EXPORT
QGeoMapType::MapStyle ritual_ZNK11QGeoMapType5styleEv(
    const QGeoMapType *self) {
  return self->style();
}

//  QString QGeoMapType::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoMapType4nameEv(const QGeoMapType *self) {
  return new QString(self->name());
}

//  QString QGeoMapType::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoMapType11descriptionEv(const QGeoMapType *self) {
  return new QString(self->description());
}

//  bool QGeoMapType::mobile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGeoMapType6mobileEv(const QGeoMapType *self) {
  return self->mobile();
}

//  bool QGeoMapType::night() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGeoMapType5nightEv(const QGeoMapType *self) {
  return self->night();
}

//  int QGeoMapType::mapId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGeoMapType5mapIdEv(const QGeoMapType *self) {
  return self->mapId();
}

//  QByteArray QGeoMapType::pluginName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QGeoMapType10pluginNameEv(const QGeoMapType *self) {
  return new QByteArray(self->pluginName());
}

//  QGeoCameraCapabilities QGeoMapType::cameraCapabilities() const
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZNK11QGeoMapType18cameraCapabilitiesEv(
    const QGeoMapType *self) {
  return new QGeoCameraCapabilities(self->cameraCapabilities());
}

//  QVariantMap QGeoMapType::metadata() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK11QGeoMapType8metadataEv(
    const QGeoMapType *self) {
  return new QMap<QString, QVariant>(self->metadata());
}

//  bool QGeoMapType::isEqual(const QGeoMapType &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGeoMapType7isEqualERKS_(
    const QGeoMapType *self,
    const QGeoMapType *other) {
  return self->isEqual(*other);
}

//  QList<QGeoMapType>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoMapType> *ritual_list_make_QGeoMapType() {
  return new QList<QGeoMapType>();
}

//  void QList<QGeoMapType>::append(const QGeoMapType &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoMapType(
    QList<QGeoMapType> *self,
    const QGeoMapType *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoMapType>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoMapType(const QList<QGeoMapType> *self) {
  return self->size();
}

//  const QGeoMapType &QList<QGeoMapType>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_list_at_QGeoMapType(
    const QList<QGeoMapType> *self,
    long long index) {
  return new QGeoMapType(self->at(index));
}

//  QList<QGeoMapType>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoMapType(QList<QGeoMapType> *self) {
  delete self;
}
