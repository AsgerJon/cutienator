//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DAsset
//  Import/6.12.0/QtQuick3DAssetImport/private/qssgassetimportmanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qtquick3dassetimportglobal_p.h>
#include <QtQuick3DAssetImport/QtQuick3DAssetImport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qssgassetimportmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QSSGAssetImporterPluginInfo::~QSSGAssetImporterPluginInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGAssetImporterPluginInfoD1Ev(
    QSSGAssetImporterPluginInfo *self) {
  delete self;
}

//  QList<QSSGAssetImporterPluginInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QSSGAssetImporterPluginInfo> *ritual_list_make_QSSGAssetImporterPluginInfo() {
  return new QList<QSSGAssetImporterPluginInfo>();
}

//  void QList<QSSGAssetImporterPluginInfo>::append(const
//      QSSGAssetImporterPluginInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSSGAssetImporterPluginInfo(
    QList<QSSGAssetImporterPluginInfo> *self,
    const QSSGAssetImporterPluginInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QSSGAssetImporterPluginInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSSGAssetImporterPluginInfo(
    const QList<QSSGAssetImporterPluginInfo> *self) {
  return self->size();
}

//  const QSSGAssetImporterPluginInfo
//      &QList<QSSGAssetImporterPluginInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSSGAssetImporterPluginInfo *ritual_list_at_QSSGAssetImporterPluginInfo(
    const QList<QSSGAssetImporterPluginInfo> *self,
    long long index) {
  return new QSSGAssetImporterPluginInfo(self->at(index));
}

//  QList<QSSGAssetImporterPluginInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSSGAssetImporterPluginInfo(
    QList<QSSGAssetImporterPluginInfo> *self) {
  delete self;
}
