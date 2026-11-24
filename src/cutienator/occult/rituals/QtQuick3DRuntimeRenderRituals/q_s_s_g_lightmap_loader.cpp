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

//  QSSGLightmapLoader::~QSSGLightmapLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGLightmapLoaderD1Ev(QSSGLightmapLoader *self) {
  delete self;
}

//  QByteArray QSSGLightmapLoader::readF32Image(const QString &key,
//      QSSGLightmapIODataTag tag) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSSGLightmapLoader12readF32ImageERK7QString21QSSGLightmapIODataTag(
    const QSSGLightmapLoader *self,
    const QString *key,
    QSSGLightmapIODataTag tag) {
  return new QByteArray(self->readF32Image(*key, tag));
}

//  QByteArray QSSGLightmapLoader::readU32Image(const QString &key,
//      QSSGLightmapIODataTag tag) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSSGLightmapLoader12readU32ImageERK7QString21QSSGLightmapIODataTag(
    const QSSGLightmapLoader *self,
    const QString *key,
    QSSGLightmapIODataTag tag) {
  return new QByteArray(self->readU32Image(*key, tag));
}

//  QByteArray QSSGLightmapLoader::readData(const QString &key,
//      QSSGLightmapIODataTag tag) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSSGLightmapLoader8readDataERK7QString21QSSGLightmapIODataTag(
    const QSSGLightmapLoader *self,
    const QString *key,
    QSSGLightmapIODataTag tag) {
  return new QByteArray(self->readData(*key, tag));
}

//  QVariantMap QSSGLightmapLoader::readMap(const QString &key,
//      QSSGLightmapIODataTag tag) const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK18QSSGLightmapLoader7readMapERK7QString21QSSGLightmapIODataTag(
    const QSSGLightmapLoader *self,
    const QString *key,
    QSSGLightmapIODataTag tag) {
  return new QMap<QString, QVariant>(self->readMap(*key, tag));
}

//  QSSGLightmapLoader::QSSGLightmapLoader()
extern "C" Q_DECL_EXPORT
QSSGLightmapLoader *ritual_ZN18QSSGLightmapLoaderC1Ev() {
  return new QSSGLightmapLoader();
}
