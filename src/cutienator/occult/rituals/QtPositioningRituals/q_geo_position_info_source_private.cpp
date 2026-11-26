//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopositioninfosource_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/qgeopositioninfosource.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopositioninfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QMultiHash>
#include <QtCore/QString>
#include <QtCore/QCborMap>

//  QGeoPositionInfoSource *QGeoPositionInfoSourcePrivate::q_func()
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN29QGeoPositionInfoSourcePrivate6q_funcEv(
    QGeoPositionInfoSourcePrivate *self) {
  return self->q_func();
}

//  const QGeoPositionInfoSource *QGeoPositionInfoSourcePrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QGeoPositionInfoSource *ritual_ZNK29QGeoPositionInfoSourcePrivate6q_funcEv(
    const QGeoPositionInfoSourcePrivate *self) {
  return self->q_func();
}

//  QGeoPositionInfoSourcePrivate::~QGeoPositionInfoSourcePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoPositionInfoSourcePrivateD1Ev(
    QGeoPositionInfoSourcePrivate *self) {
  delete self;
}

//  void QGeoPositionInfoSourcePrivate::setPositioningMethods(QGeoPositionInf
//      oSource::PositioningMethods methods)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoPositionInfoSourcePrivate21setPositioningMethodsE6QFlagsIN22QGeoPositionInfoSource17PositioningMethodEE(
    QGeoPositionInfoSourcePrivate *self,
    int methods) {
  self->setPositioningMethods(
      QFlags<QGeoPositionInfoSource::PositioningMethod>::fromInt(methods));
}

//  size_t QGeoPositionInfoSourcePrivate::_qt_property_interval_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN29QGeoPositionInfoSourcePrivate28_qt_property_interval_offsetEv() {
  return QGeoPositionInfoSourcePrivate::_qt_property_interval_offset();
}

//  size_t QGeoPositionInfoSourcePrivate::_qt_property_methods_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN29QGeoPositionInfoSourcePrivate27_qt_property_methods_offsetEv() {
  return QGeoPositionInfoSourcePrivate::_qt_property_methods_offset();
}

//  a QMultiHash<QString, QCborMap> a ritual of QGeoPositionInfoSourcePrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoPositionInfoSourcePrivate__QMultiHash_QString_QCborMap(
    QMultiHash<QString, QCborMap> *self) {
  delete self;
}
