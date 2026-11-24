//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssglightmapio_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglightmapio_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QSSGLightmapWriter::~QSSGLightmapWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGLightmapWriterD1Ev(QSSGLightmapWriter *self) {
  delete self;
}

//  bool QSSGLightmapWriter::writeF32Image(const QString &key,
//      QSSGLightmapIODataTag tag, const QByteArray &imageFP32)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSSGLightmapWriter13writeF32ImageERK7QString21QSSGLightmapIODataTagRK10QByteArray(
    QSSGLightmapWriter *self,
    const QString *key,
    QSSGLightmapIODataTag tag,
    const QByteArray *imageFP32) {
  return self->writeF32Image(*key, tag, *imageFP32);
}

//  bool QSSGLightmapWriter::writeU32Image(const QString &key,
//      QSSGLightmapIODataTag tag, const QByteArray &imageU32)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSSGLightmapWriter13writeU32ImageERK7QString21QSSGLightmapIODataTagRK10QByteArray(
    QSSGLightmapWriter *self,
    const QString *key,
    QSSGLightmapIODataTag tag,
    const QByteArray *imageU32) {
  return self->writeU32Image(*key, tag, *imageU32);
}

//  bool QSSGLightmapWriter::writeData(const QString &key,
//      QSSGLightmapIODataTag tag, const QByteArray &buffer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSSGLightmapWriter9writeDataERK7QString21QSSGLightmapIODataTagRK10QByteArray(
    QSSGLightmapWriter *self,
    const QString *key,
    QSSGLightmapIODataTag tag,
    const QByteArray *buffer) {
  return self->writeData(*key, tag, *buffer);
}

//  bool QSSGLightmapWriter::writeMap(const QString &key,
//      QSSGLightmapIODataTag tag, const QVariantMap &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSSGLightmapWriter8writeMapERK7QString21QSSGLightmapIODataTagRK4QMapIS0_8QVariantE(
    QSSGLightmapWriter *self,
    const QString *key,
    QSSGLightmapIODataTag tag,
    const QMap<QString, QVariant> *data) {
  return self->writeMap(*key, tag, *data);
}

//  bool QSSGLightmapWriter::close() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSSGLightmapWriter5closeEv(const QSSGLightmapWriter *self) {
  return self->close();
}

//  QSSGLightmapWriter::QSSGLightmapWriter()
extern "C" Q_DECL_EXPORT
QSSGLightmapWriter *ritual_ZN18QSSGLightmapWriterC1Ev() {
  return new QSSGLightmapWriter();
}
