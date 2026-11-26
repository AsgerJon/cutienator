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
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QSharedPointer>
#include <QtCore/QString>
#include <QtCore/QList>
#include <utility>
#include <QtCore/QIODevice>

//  QSSGLightmapLoader::~QSSGLightmapLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGLightmapLoaderD1Ev(QSSGLightmapLoader *self) {
  delete self;
}

//  QSharedPointer<QSSGLightmapLoader> QSSGLightmapLoader::open(const
//      QSharedPointer<QIODevice> &stream)
extern "C" Q_DECL_EXPORT
QSharedPointer<QSSGLightmapLoader> *ritual_ZN18QSSGLightmapLoader4openERK14QSharedPointerI9QIODeviceE(
    const QSharedPointer<QIODevice> *stream) {
  return new QSharedPointer<QSSGLightmapLoader>(
      QSSGLightmapLoader::open(
          *stream));
}

//  QSharedPointer<QSSGLightmapLoader> QSSGLightmapLoader::open(const QString
//      &path)
extern "C" Q_DECL_EXPORT
QSharedPointer<QSSGLightmapLoader> *ritual_ZN18QSSGLightmapLoader4openERK7QString(
    const QString *path) {
  return new QSharedPointer<QSSGLightmapLoader>(
      QSSGLightmapLoader::open(
          *path));
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

//  QList<std::pair<QString, QSSGLightmapIODataTag>>
//      QSSGLightmapLoader::getKeys() const
extern "C" Q_DECL_EXPORT
QList<std::pair<QString, QSSGLightmapIODataTag>> *ritual_ZNK18QSSGLightmapLoader7getKeysEv(
    const QSSGLightmapLoader *self) {
  return new QList<std::pair<QString, QSSGLightmapIODataTag>>(
      self->getKeys());
}

//  QSSGLoadedTexture
//      *QSSGLightmapLoader::createTexture(QSharedPointer<QIODevice> stream,
//      const QSSGRenderTextureFormat &format, const QString &key)
extern "C" Q_DECL_EXPORT
QSSGLoadedTexture *ritual_ZN18QSSGLightmapLoader13createTextureE14QSharedPointerI9QIODeviceERK23QSSGRenderTextureFormatRK7QString(
    const QSharedPointer<QIODevice> *stream,
    const QSSGRenderTextureFormat *format,
    const QString *key) {
  return QSSGLightmapLoader::createTexture(*stream, *format, *key);
}

//  QSSGLightmapLoader::QSSGLightmapLoader()
extern "C" Q_DECL_EXPORT
QSSGLightmapLoader *ritual_ZN18QSSGLightmapLoaderC1Ev() {
  return new QSSGLightmapLoader();
}

//  a QSharedPointer<QSSGLightmapLoader> a ritual of QSSGLightmapLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGLightmapLoader__QSharedPointer_QSSGLightmapLoader(
    QSharedPointer<QSSGLightmapLoader> *self) {
  delete self;
}

//  a QList<std::pair<QString, QSSGLightmapIODataTag>> a ritual of
//      QSSGLightmapLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGLightmapLoader__QList_std_pair_QString_QSSGLightmapIODataTag(
    QList<std::pair<QString, QSSGLightmapIODataTag>> *self) {
  delete self;
}
