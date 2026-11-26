//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderlibraryman
//  ager_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderlibrarymanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QString QSSGShaderLibraryManager::getShaderCodeLibraryDirectory()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QSSGShaderLibraryManager29getShaderCodeLibraryDirectoryEv() {
  return new QString(
      QSSGShaderLibraryManager::getShaderCodeLibraryDirectory());
}

//  QSSGShaderLibraryManager::QSSGShaderLibraryManager()
extern "C" Q_DECL_EXPORT
QSSGShaderLibraryManager *ritual_ZN24QSSGShaderLibraryManagerC1Ev() {
  return new QSSGShaderLibraryManager();
}

//  QSSGShaderLibraryManager::~QSSGShaderLibraryManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGShaderLibraryManagerD1Ev(
    QSSGShaderLibraryManager *self) {
  delete self;
}

//  QQsbCollection::EntryMap
//      QSSGShaderLibraryManager::getParticleShaderEntries() const
extern "C" Q_DECL_EXPORT
QQsbCollection::EntryMap *ritual_ZNK24QSSGShaderLibraryManager24getParticleShaderEntriesEv(
    const QSSGShaderLibraryManager *self) {
  return new QQsbCollection::EntryMap(self->getParticleShaderEntries());
}

//  void QSSGShaderLibraryManager::setShaderSource(const QByteArray
//      &inShaderPathKey, QSSGShaderCache::ShaderType type, const QByteArray
//      &inSource, const QSSGCustomShaderMetaData &meta)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGShaderLibraryManager15setShaderSourceERK10QByteArrayN15QSSGShaderCache10ShaderTypeES2_RK24QSSGCustomShaderMetaData(
    QSSGShaderLibraryManager *self,
    const QByteArray *inShaderPathKey,
    QSSGShaderCache::ShaderType type,
    const QByteArray *inSource,
    const QSSGCustomShaderMetaData *meta) {
  self->setShaderSource(*inShaderPathKey, type, *inSource, *meta);
}

//  void QSSGShaderLibraryManager::loadPregeneratedShaderInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGShaderLibraryManager26loadPregeneratedShaderInfoEv(
    QSSGShaderLibraryManager *self) {
  self->loadPregeneratedShaderInfo();
}

//  void QSSGShaderLibraryManager::resolveIncludeFiles(QByteArray
//      &theReadBuffer, const QByteArray &inMaterialInfoString)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGShaderLibraryManager19resolveIncludeFilesER10QByteArrayRKS0_(
    QSSGShaderLibraryManager *self,
    QByteArray *theReadBuffer,
    const QByteArray *inMaterialInfoString) {
  self->resolveIncludeFiles(*theReadBuffer, *inMaterialInfoString);
}

//  QByteArray QSSGShaderLibraryManager::getIncludeContents(const QByteArray
//      &inShaderPathKey)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN24QSSGShaderLibraryManager18getIncludeContentsERK10QByteArray(
    QSSGShaderLibraryManager *self,
    const QByteArray *inShaderPathKey) {
  return new QByteArray(self->getIncludeContents(*inShaderPathKey));
}

//  QByteArray QSSGShaderLibraryManager::getShaderSource(const QByteArray
//      &inShaderPathKey, QSSGShaderCache::ShaderType type)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN24QSSGShaderLibraryManager15getShaderSourceERK10QByteArrayN15QSSGShaderCache10ShaderTypeE(
    QSSGShaderLibraryManager *self,
    const QByteArray *inShaderPathKey,
    QSSGShaderCache::ShaderType type) {
  return new QByteArray(self->getShaderSource(*inShaderPathKey, type));
}

//  QSSGCustomShaderMetaData
//      QSSGShaderLibraryManager::getShaderMetaData(const QByteArray
//      &inShaderPathKey, QSSGShaderCache::ShaderType type)
extern "C" Q_DECL_EXPORT
QSSGCustomShaderMetaData *ritual_ZN24QSSGShaderLibraryManager17getShaderMetaDataERK10QByteArrayN15QSSGShaderCache10ShaderTypeE(
    QSSGShaderLibraryManager *self,
    const QByteArray *inShaderPathKey,
    QSSGShaderCache::ShaderType type) {
  return new QSSGCustomShaderMetaData(
      self->getShaderMetaData(
          *inShaderPathKey,
          type));
}

//  bool QSSGShaderLibraryManager::compare(const QSSGShaderDefaultMaterialKey
//      &key1, const QSSGShaderDefaultMaterialKey &key2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSSGShaderLibraryManager7compareERK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EES4_(
    const QSSGShaderDefaultMaterialKey *key1,
    const QSSGShaderDefaultMaterialKey *key2) {
  return QSSGShaderLibraryManager::compare(*key1, *key2);
}

//  a QQsbCollection::EntryMap a ritual of QSSGShaderLibraryManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGShaderLibraryManager__QQsbCollection_EntryMap(
    QQsbCollection::EntryMap *self) {
  delete self;
}
