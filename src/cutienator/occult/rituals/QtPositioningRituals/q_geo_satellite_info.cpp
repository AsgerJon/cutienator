//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeosatelliteinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/qgeosatelliteinfo.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QGeoSatelliteInfo::QGeoSatelliteInfo()
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfo *ritual_ZN17QGeoSatelliteInfoC1Ev() {
  return new QGeoSatelliteInfo();
}

//  QGeoSatelliteInfo::QGeoSatelliteInfo(const QGeoSatelliteInfo &other)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfo *ritual_ZN17QGeoSatelliteInfoC1ERKS_(
    const QGeoSatelliteInfo *other) {
  return new QGeoSatelliteInfo(*other);
}

//  QGeoSatelliteInfo::~QGeoSatelliteInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoSatelliteInfoD1Ev(QGeoSatelliteInfo *self) {
  delete self;
}

//  bool operator==(const QGeoSatelliteInfo &lhs, const QGeoSatelliteInfo
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK17QGeoSatelliteInfoS1_(
    const QGeoSatelliteInfo *lhs,
    const QGeoSatelliteInfo *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoSatelliteInfo &lhs, const QGeoSatelliteInfo
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK17QGeoSatelliteInfoS1_(
    const QGeoSatelliteInfo *lhs,
    const QGeoSatelliteInfo *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QGeoSatelliteInfo::setSatelliteSystem(SatelliteSystem system)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoSatelliteInfo18setSatelliteSystemENS_15SatelliteSystemE(
    QGeoSatelliteInfo *self,
    QGeoSatelliteInfo::SatelliteSystem system) {
  self->setSatelliteSystem(system);
}

//  SatelliteSystem QGeoSatelliteInfo::satelliteSystem() const
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfo::SatelliteSystem ritual_ZNK17QGeoSatelliteInfo15satelliteSystemEv(
    const QGeoSatelliteInfo *self) {
  return self->satelliteSystem();
}

//  void QGeoSatelliteInfo::setSatelliteIdentifier(int satId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoSatelliteInfo22setSatelliteIdentifierEi(
    QGeoSatelliteInfo *self,
    int satId) {
  self->setSatelliteIdentifier(satId);
}

//  int QGeoSatelliteInfo::satelliteIdentifier() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoSatelliteInfo19satelliteIdentifierEv(
    const QGeoSatelliteInfo *self) {
  return self->satelliteIdentifier();
}

//  void QGeoSatelliteInfo::setSignalStrength(int signalStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoSatelliteInfo17setSignalStrengthEi(
    QGeoSatelliteInfo *self,
    int signalStrength) {
  self->setSignalStrength(signalStrength);
}

//  int QGeoSatelliteInfo::signalStrength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoSatelliteInfo14signalStrengthEv(
    const QGeoSatelliteInfo *self) {
  return self->signalStrength();
}

//  void QGeoSatelliteInfo::setAttribute(Attribute attribute, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoSatelliteInfo12setAttributeENS_9AttributeEd(
    QGeoSatelliteInfo *self,
    QGeoSatelliteInfo::Attribute attribute,
    qreal value) {
  self->setAttribute(attribute, value);
}

//  qreal QGeoSatelliteInfo::attribute(Attribute attribute) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGeoSatelliteInfo9attributeENS_9AttributeE(
    const QGeoSatelliteInfo *self,
    QGeoSatelliteInfo::Attribute attribute) {
  return self->attribute(attribute);
}

//  void QGeoSatelliteInfo::removeAttribute(Attribute attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoSatelliteInfo15removeAttributeENS_9AttributeE(
    QGeoSatelliteInfo *self,
    QGeoSatelliteInfo::Attribute attribute) {
  self->removeAttribute(attribute);
}

//  bool QGeoSatelliteInfo::hasAttribute(Attribute attribute) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoSatelliteInfo12hasAttributeENS_9AttributeE(
    const QGeoSatelliteInfo *self,
    QGeoSatelliteInfo::Attribute attribute) {
  return self->hasAttribute(attribute);
}

//  void QGeoSatelliteInfo::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoSatelliteInfo6detachEv(QGeoSatelliteInfo *self) {
  self->detach();
}

//  bool QGeoSatelliteInfo::equals(const QGeoSatelliteInfo &lhs, const
//      QGeoSatelliteInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGeoSatelliteInfo6equalsERKS_S1_(
    const QGeoSatelliteInfo *lhs,
    const QGeoSatelliteInfo *rhs) {
  return QGeoSatelliteInfo::equals(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QGeoSatelliteInfo &info)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK17QGeoSatelliteInfo(
    const QDebug *dbg,
    const QGeoSatelliteInfo *info) {
  return new QDebug(operator<<(*dbg, *info));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QGeoSatelliteInfo::debugStreaming(QDebug dbg, const
//      QGeoSatelliteInfo &info)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN17QGeoSatelliteInfo14debugStreamingE6QDebugRKS_(
    const QDebug *dbg,
    const QGeoSatelliteInfo *info) {
  return new QDebug(QGeoSatelliteInfo::debugStreaming(*dbg, *info));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QGeoSatelliteInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoSatelliteInfo> *ritual_list_make_QGeoSatelliteInfo() {
  return new QList<QGeoSatelliteInfo>();
}

//  void QList<QGeoSatelliteInfo>::append(const QGeoSatelliteInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoSatelliteInfo(
    QList<QGeoSatelliteInfo> *self,
    const QGeoSatelliteInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoSatelliteInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoSatelliteInfo(
    const QList<QGeoSatelliteInfo> *self) {
  return self->size();
}

//  const QGeoSatelliteInfo &QList<QGeoSatelliteInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfo *ritual_list_at_QGeoSatelliteInfo(
    const QList<QGeoSatelliteInfo> *self,
    long long index) {
  return new QGeoSatelliteInfo(self->at(index));
}

//  QList<QGeoSatelliteInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoSatelliteInfo(QList<QGeoSatelliteInfo> *self) {
  delete self;
}
