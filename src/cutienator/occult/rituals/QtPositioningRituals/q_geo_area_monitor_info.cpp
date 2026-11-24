//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeoareamonitorinfo.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtPositioning/qgeoareamonitorinfo.h>
#include <QtCore/qstring.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QGeoAreaMonitorInfo::QGeoAreaMonitorInfo(const QString &name)
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorInfo *ritual_ZN19QGeoAreaMonitorInfoC1ERK7QString(
    const QString *name) {
  return new QGeoAreaMonitorInfo(*name);
}

//  QGeoAreaMonitorInfo::QGeoAreaMonitorInfo(const QGeoAreaMonitorInfo
//      &other)
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorInfo *ritual_ZN19QGeoAreaMonitorInfoC1ERKS_(
    const QGeoAreaMonitorInfo *other) {
  return new QGeoAreaMonitorInfo(*other);
}

//  QGeoAreaMonitorInfo::~QGeoAreaMonitorInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoAreaMonitorInfoD1Ev(QGeoAreaMonitorInfo *self) {
  delete self;
}

//  bool operator==(const QGeoAreaMonitorInfo &lhs, const QGeoAreaMonitorInfo
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QGeoAreaMonitorInfoS1_(
    const QGeoAreaMonitorInfo *lhs,
    const QGeoAreaMonitorInfo *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoAreaMonitorInfo &lhs, const QGeoAreaMonitorInfo
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QGeoAreaMonitorInfoS1_(
    const QGeoAreaMonitorInfo *lhs,
    const QGeoAreaMonitorInfo *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QGeoAreaMonitorInfo::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoAreaMonitorInfo4nameEv(
    const QGeoAreaMonitorInfo *self) {
  return new QString(self->name());
}

//  void QGeoAreaMonitorInfo::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoAreaMonitorInfo7setNameERK7QString(
    QGeoAreaMonitorInfo *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QGeoAreaMonitorInfo::identifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoAreaMonitorInfo10identifierEv(
    const QGeoAreaMonitorInfo *self) {
  return new QString(self->identifier());
}

//  bool QGeoAreaMonitorInfo::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoAreaMonitorInfo7isValidEv(
    const QGeoAreaMonitorInfo *self) {
  return self->isValid();
}

//  QGeoShape QGeoAreaMonitorInfo::area() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK19QGeoAreaMonitorInfo4areaEv(
    const QGeoAreaMonitorInfo *self) {
  return new QGeoShape(self->area());
}

//  void QGeoAreaMonitorInfo::setArea(const QGeoShape &newShape)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoAreaMonitorInfo7setAreaERK9QGeoShape(
    QGeoAreaMonitorInfo *self,
    const QGeoShape *newShape) {
  self->setArea(*newShape);
}

//  QDateTime QGeoAreaMonitorInfo::expiration() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QGeoAreaMonitorInfo10expirationEv(
    const QGeoAreaMonitorInfo *self) {
  return new QDateTime(self->expiration());
}

//  void QGeoAreaMonitorInfo::setExpiration(const QDateTime &expiry)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoAreaMonitorInfo13setExpirationERK9QDateTime(
    QGeoAreaMonitorInfo *self,
    const QDateTime *expiry) {
  self->setExpiration(*expiry);
}

//  bool QGeoAreaMonitorInfo::isPersistent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoAreaMonitorInfo12isPersistentEv(
    const QGeoAreaMonitorInfo *self) {
  return self->isPersistent();
}

//  void QGeoAreaMonitorInfo::setPersistent(bool isPersistent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoAreaMonitorInfo13setPersistentEb(
    QGeoAreaMonitorInfo *self,
    bool isPersistent) {
  self->setPersistent(isPersistent);
}

//  QVariantMap QGeoAreaMonitorInfo::notificationParameters() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK19QGeoAreaMonitorInfo22notificationParametersEv(
    const QGeoAreaMonitorInfo *self) {
  return new QMap<QString, QVariant>(self->notificationParameters());
}

//  void QGeoAreaMonitorInfo::setNotificationParameters(const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoAreaMonitorInfo25setNotificationParametersERK4QMapI7QString8QVariantE(
    QGeoAreaMonitorInfo *self,
    const QMap<QString, QVariant> *parameters) {
  self->setNotificationParameters(*parameters);
}

//  void QGeoAreaMonitorInfo::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoAreaMonitorInfo6detachEv(QGeoAreaMonitorInfo *self) {
  self->detach();
}

//  bool QGeoAreaMonitorInfo::equals(const QGeoAreaMonitorInfo &lhs, const
//      QGeoAreaMonitorInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QGeoAreaMonitorInfo6equalsERKS_S1_(
    const QGeoAreaMonitorInfo *lhs,
    const QGeoAreaMonitorInfo *rhs) {
  return QGeoAreaMonitorInfo::equals(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QGeoAreaMonitorInfo &monitor)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QGeoAreaMonitorInfo(
    const QDebug *dbg,
    const QGeoAreaMonitorInfo *monitor) {
  return new QDebug(operator<<(*dbg, *monitor));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QGeoAreaMonitorInfo::debugStreaming(QDebug dbg, const
//      QGeoAreaMonitorInfo &monitor)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN19QGeoAreaMonitorInfo14debugStreamingE6QDebugRKS_(
    const QDebug *dbg,
    const QGeoAreaMonitorInfo *monitor) {
  return new QDebug(QGeoAreaMonitorInfo::debugStreaming(*dbg, *monitor));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QGeoAreaMonitorInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoAreaMonitorInfo> *ritual_list_make_QGeoAreaMonitorInfo() {
  return new QList<QGeoAreaMonitorInfo>();
}

//  void QList<QGeoAreaMonitorInfo>::append(const QGeoAreaMonitorInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoAreaMonitorInfo(
    QList<QGeoAreaMonitorInfo> *self,
    const QGeoAreaMonitorInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoAreaMonitorInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoAreaMonitorInfo(
    const QList<QGeoAreaMonitorInfo> *self) {
  return self->size();
}

//  const QGeoAreaMonitorInfo &QList<QGeoAreaMonitorInfo>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorInfo *ritual_list_at_QGeoAreaMonitorInfo(
    const QList<QGeoAreaMonitorInfo> *self,
    long long index) {
  return new QGeoAreaMonitorInfo(self->at(index));
}

//  QList<QGeoAreaMonitorInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoAreaMonitorInfo(QList<QGeoAreaMonitorInfo> *self) {
  delete self;
}
