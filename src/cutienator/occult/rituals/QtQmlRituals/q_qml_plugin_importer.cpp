//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpluginimporter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpluginimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpluginimporter_p.h>
#include <QtQml/private/qqmlimport_p.h>
#include <QtQml/private/qqmlextensionplugin_p.h>
#include <QtQml/private/qqmltypeloader_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtCore/qobject.h>
#include <QtCore/qpluginloader.h>
#include <QtCore/qdir.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qjsonarray.h>
#include <unordered_map>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 22, as local:qqmlpluginimporter.cpp:QmlPlugin
struct QmlPlugin
{
    using Loader = std::unique_ptr<QPluginLoader>;
    QPluginLoader *loader() const
    {
        if (auto loader = std::get_if<Loader>(&data))
            return loader->get();
        return nullptr;
    }

    bool hasInstanceOrLoader() const
    {
        if (auto instance = std::get_if<QQmlExtensionPlugin *>(&data))
            return *instance;
        return bool(std::get<Loader>(data));
    }

    QString unloadOrErrorMessage() const
    {
        if (auto instance = std::get_if<QQmlExtensionPlugin *>(&data)) {
            if (*instance)
                (*instance)->unregisterTypes();
            return {};
        }
        const Loader &loader = std::get<Loader>(data);
        if (!loader)
            return {};

#if QT_CONFIG(library)
        if (auto extensionPlugin = qobject_cast<QQmlExtensionPlugin *>(loader->instance()))
            extensionPlugin->unregisterTypes();
        if (!loader->unload())
            return loader->errorString();
#endif
        return {};
    }
    std::variant<Loader, QQmlExtensionPlugin *> data;
};

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 61, as local:qqmlpluginimporter.cpp:PluginMap
class PluginMap
{
    Q_DISABLE_COPY_MOVE(PluginMap)
public:
    PluginMap() = default;
    ~PluginMap() = default;

    // This is a std::unordered_map because QHash cannot handle move-only types.
    using Container = std::unordered_map<QString, QmlPlugin>;

private:
    QBasicMutex mutex;
    Container plugins;
    friend class PluginMapPtr;
};

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 97, as local:qqmlpluginimporter.cpp:StaticPluginMapping
struct StaticPluginMapping
{
    QStaticPlugin plugin;
    QString metadataURI;
};

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 116, as local:qqmlpluginimporter.cpp:tryExtractQmlPluginURIs
static QJsonArray tryExtractQmlPluginURIs(const QStaticPlugin &plugin)
{
    const auto isQmlPlugin = [](const QStaticPlugin &plugin, auto &&pluginMetadata) -> bool {
        const QString iid = pluginMetadata.value(QLatin1String("IID")).toString();
        const bool isQmlExtensionIID = iid == QLatin1String(QQmlEngineExtensionInterface_iid)
                || iid == QLatin1String(QQmlExtensionInterface_iid)
                || iid == QLatin1String(QQmlExtensionInterface_iid_old);
        if (Q_UNLIKELY(iid == QLatin1String(QQmlExtensionInterface_iid_old))) {
            qWarning() << QQmlImports::tr(
                    "Found plugin with old IID, this will be unsupported in upcoming Qt "
                    "releases:")
                       << pluginMetadata;
        }
        if (!isQmlExtensionIID) {
            return false;
        }

        // plugin.instance must not be called earlier to avoid instantiating
        // non-QML plugins, potentially from an unexpected thread(typeloader vs
        // main thread)
        const auto *pluginInstance = plugin.instance();
        return qobject_cast<const QQmlEngineExtensionPlugin *>(pluginInstance)
                || qobject_cast<const QQmlExtensionPlugin *>(pluginInstance);
    };

    const auto &pluginMetadata = plugin.metaData();
    if (!isQmlPlugin(plugin, pluginMetadata)) {
        return {};
    }

    const QJsonArray metadataUriList = pluginMetadata.value(QStringLiteral("uri")).toArray();
    if (metadataUriList.isEmpty()) {
        qWarning() << QQmlImports::tr("qml static plugin with name \"%2\" has no metadata URI")
                              .arg(plugin.instance()->metaObject()->className())
                   << pluginMetadata;
        return {};
    }
    return metadataUriList;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 156, as local:qqmlpluginimporter.cpp:staticQmlPlugins
static QList<StaticPluginMapping> staticQmlPlugins()
{
    QList<StaticPluginMapping> qmlPlugins;
    const auto staticPlugins = QPluginLoader::staticPlugins();
    qmlPlugins.reserve(staticPlugins.size());

    for (const auto &plugin : staticPlugins) {
        // Filter out static plugins which are not Qml plugins
        const QJsonArray pluginURIs = tryExtractQmlPluginURIs(plugin);
        for (const QJsonValueConstRef &pluginURI : pluginURIs)
            qmlPlugins.append({ plugin, pluginURI.toString() });
    }
    return qmlPlugins;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 229, as local:qqmlpluginimporter.cpp:lockModule
static QTypeRevision lockModule(const QString &uri, const QString &typeNamespace,
                                             QTypeRevision version, QList<QQmlError> *errors)
{
    if (!version.hasMajorVersion()) {
        version = QQmlMetaType::latestModuleVersion(uri);
        if (!version.isValid())
            errors->prepend(QQmlImports::moduleNotFoundError(uri, version));
    }
    if (version.hasMajorVersion() && !typeNamespace.isEmpty()
        && !QQmlMetaType::protectModule(uri, version, true)) {
        // Not being able to protect the module means there are not types registered for it,
        // means the plugin we loaded didn't provide any, means we didn't find the module.
        // We output the generic error message as depending on the load order of imports we may
        // hit this path or another one that only figures "plugin is already loaded but module
        // unavailable" and doesn't try to protect it anymore.
        errors->prepend(QQmlImports::moduleNotFoundError(uri, version));
        return QTypeRevision();
    }

    return version;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 285, as _ZN18QQmlPluginImporter19truncateToDirectoryERK7QString
inline QString QQmlPluginImporter::truncateToDirectory(const QString &qmldirFilePath)
{
    const int slash = qmldirFilePath.lastIndexOf(u'/');
    return slash > 0 ? qmldirFilePath.left(slash) : qmldirFilePath;
}
//  -----------------------------------------------------------------------

//  QQmlPluginImporter::QQmlPluginImporter(const QString &uri, QTypeRevision
//      version, const QQmlTypeLoaderQmldirContent *qmldir, QQmlTypeLoader
//      *typeLoader, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
QQmlPluginImporter *ritual_ZN18QQmlPluginImporterC1ERK7QString13QTypeRevisionPK27QQmlTypeLoaderQmldirContentP14QQmlTypeLoaderP5QListI9QQmlErrorE(
    const QString *uri,
    const QTypeRevision *version,
    const QQmlTypeLoaderQmldirContent *qmldir,
    QQmlTypeLoader *typeLoader,
    QList<QQmlError> *errors) {
  return new QQmlPluginImporter(*uri, *version, qmldir, typeLoader, errors);
}

//  QQmlPluginImporter::~QQmlPluginImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPluginImporterD1Ev(QQmlPluginImporter *self) {
  delete self;
}

//  QString QQmlPluginImporter::truncateToDirectory(const QString
//      &qmldirFilePath)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlPluginImporter19truncateToDirectoryERK7QString(
    const QString *qmldirFilePath) {
  return new QString(
      QQmlPluginImporter::truncateToDirectory(
          *qmldirFilePath));
}
