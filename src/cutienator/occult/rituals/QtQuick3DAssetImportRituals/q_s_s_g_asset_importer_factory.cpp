//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DAsset
//  Import/6.12.0/QtQuick3DAssetImport/private/qssgassetimporterfactory_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qtquick3dassetimportglobal_p.h>
#include <QtQuick3DAssetImport/QtQuick3DAssetImport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qssgassetimporterfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QSSGAssetImporterFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN24QSSGAssetImporterFactory4keysEv() {
  return new QList<QString>(QSSGAssetImporterFactory::keys());
}

//  QSSGAssetImporter *QSSGAssetImporterFactory::create(const QString &name,
//      const QStringList &args)
extern "C" Q_DECL_EXPORT
QSSGAssetImporter *ritual_ZN24QSSGAssetImporterFactory6createERK7QStringRK5QListIS0_E(
    const QString *name,
    const QList<QString> *args) {
  return QSSGAssetImporterFactory::create(*name, *args);
}

//  QSSGAssetImporterFactory::~QSSGAssetImporterFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGAssetImporterFactoryD1Ev(
    QSSGAssetImporterFactory *self) {
  delete self;
}
