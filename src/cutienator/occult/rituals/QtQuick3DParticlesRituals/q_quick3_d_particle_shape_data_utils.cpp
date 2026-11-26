//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticleshapedatautils_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleshapedatautils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  QVariant QQuick3DParticleShapeDataUtils::readValue(QCborStreamReader
//      &reader, QMetaType::Type type)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN30QQuick3DParticleShapeDataUtils9readValueER17QCborStreamReaderN9QMetaType4TypeE(
    QCborStreamReader *reader,
    QMetaType::Type type) {
  return new QVariant(
      QQuick3DParticleShapeDataUtils::readValue(
          *reader,
          type));
}

//  QString QQuick3DParticleShapeDataUtils::readString(QCborStreamReader
//      &reader)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuick3DParticleShapeDataUtils10readStringER17QCborStreamReader(
    QCborStreamReader *reader) {
  return new QString(QQuick3DParticleShapeDataUtils::readString(*reader));
}

//  double QQuick3DParticleShapeDataUtils::readReal(QCborStreamReader
//      &reader)
extern "C" Q_DECL_EXPORT
double ritual_ZN30QQuick3DParticleShapeDataUtils8readRealER17QCborStreamReader(
    QCborStreamReader *reader) {
  return QQuick3DParticleShapeDataUtils::readReal(*reader);
}

//  int QQuick3DParticleShapeDataUtils::readShapeHeader(QCborStreamReader
//      &reader)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QQuick3DParticleShapeDataUtils15readShapeHeaderER17QCborStreamReader(
    QCborStreamReader *reader) {
  return QQuick3DParticleShapeDataUtils::readShapeHeader(*reader);
}

#if QT_CONFIG(cborstreamwriter)
//  void QQuick3DParticleShapeDataUtils::writeShapeHeader(QCborStreamWriter
//      &writer, int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleShapeDataUtils16writeShapeHeaderER17QCborStreamWriteri(
    QCborStreamWriter *writer,
    int version) {
  QQuick3DParticleShapeDataUtils::writeShapeHeader(*writer, version);
}
#endif  // QT_CONFIG(cborstreamwriter)

#if QT_CONFIG(cborstreamwriter)
//  void QQuick3DParticleShapeDataUtils::writeValue(QCborStreamWriter
//      &writer, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleShapeDataUtils10writeValueER17QCborStreamWriterRK8QVariant(
    QCborStreamWriter *writer,
    const QVariant *value) {
  QQuick3DParticleShapeDataUtils::writeValue(*writer, *value);
}
#endif  // QT_CONFIG(cborstreamwriter)

//  QQuick3DParticleShapeDataUtils::~QQuick3DParticleShapeDataUtils()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleShapeDataUtilsD1Ev(
    QQuick3DParticleShapeDataUtils *self) {
  delete self;
}
