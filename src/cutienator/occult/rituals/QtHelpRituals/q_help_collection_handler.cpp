//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/6.12.0/QtHelp/private/qhelpcollectionhandler_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QHelpCollectionHandler'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 16 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHelp/QtHelp>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHelp/6.12.0/QtHelp/private/qhelpcollectionhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>
#include <QtHelp/qhelpfilterdata.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QList>
#include <QtCore/QStringList>
#include <QtCore/QString>
#include <QtCore/QMap>
#include <QtCore/QMultiMap>
#include <QtCore/QUrl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtHelp/private/qhelpdbreader_p.h>
#include <QtHelp/qhelp_global.h>
#include <QtCore/qfile.h>
#include <QtCore/qmap.h>
#include <QtCore/qvariant.h>
#include <QtCore/qversionnumber.h>
#include <QtSql/qsqldatabase.h>
#include <QtSql/qsqlerror.h>
#include <QtSql/qsqlquery.h>
#include <QtHelp/private/qhelpcollectionhandler_p.h>
#include <QtHelp/qhelp_global.h>
#include <QtHelp/private/qhelpdbreader_p.h>
#include <QtHelp/qhelpfilterdata.h>
#include <QtHelp/qhelplink.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdir.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qset.h>
#include <QtCore/qtimer.h>
#include <QtCore/qversionnumber.h>
#include <QtSql/qsqldriver.h>
#include <QtSql/qsqlerror.h>
#include <QtSql/qsqlquery.h>
#include <algorithm>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 29, as local:qhelpcollectionhandler.cpp:Transaction
class Transaction
{
public:
    Q_DISABLE_COPY_MOVE(Transaction);

    Transaction(const QString &connectionName)
        : m_db(QSqlDatabase::database(connectionName)),
          m_inTransaction(m_db.driver()->hasFeature(QSqlDriver::Transactions))
    {
        if (m_inTransaction)
            m_inTransaction = m_db.transaction();
    }

    ~Transaction()
    {
        if (m_inTransaction)
            m_db.rollback();
    }

    void commit()
    {
        if (!m_inTransaction)
            return;

        m_db.commit();
        m_inTransaction = false;
    }

private:
    QSqlDatabase m_db;
    bool m_inTransaction;
};

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 929, as local:qhelpcollectionhandler.cpp:extractFileInfo
static QHelpCollectionHandler::FileInfo extractFileInfo(const QUrl &url)
{
    QHelpCollectionHandler::FileInfo fileInfo;

    if (!url.isValid() || url.toString().count(u'/') < 4
        || url.scheme() != "qthelp"_L1) {
        return fileInfo;
    }

    fileInfo.namespaceName = url.authority();
    fileInfo.fileName = url.path();
    if (fileInfo.fileName.startsWith(u'/'))
        fileInfo.fileName = fileInfo.fileName.mid(1);
    fileInfo.folderName = fileInfo.fileName.mid(0, fileInfo.fileName.indexOf(u'/', 1));
    fileInfo.fileName.remove(0, fileInfo.folderName.size() + 1);

    return fileInfo;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 978, as local:qhelpcollectionhandler.cpp:prepareFilterQuery
static QString prepareFilterQuery(const QString &filterName)
{
    if (filterName.isEmpty())
        return {};

    return " AND EXISTS(SELECT * FROM Filter WHERE Filter.Name = ?) "
        "AND ("
        "(NOT EXISTS(" // 1. filter by component
        "SELECT * FROM "
            "ComponentFilter, "
            "Filter "
        "WHERE ComponentFilter.FilterId = Filter.FilterId "
            "AND Filter.Name = ?) "
        "OR NamespaceTable.Id IN ("
        "SELECT "
            "NamespaceTable.Id "
        "FROM "
            "NamespaceTable, "
            "ComponentTable, "
            "ComponentMapping, "
            "ComponentFilter, "
            "Filter "
        "WHERE ComponentMapping.NamespaceId = NamespaceTable.Id "
            "AND ComponentTable.ComponentId = ComponentMapping.ComponentId "
            "AND ((ComponentTable.Name = ComponentFilter.ComponentName) "
                "OR (ComponentTable.Name IS NULL AND ComponentFilter.ComponentName IS NULL)) "
            "AND ComponentFilter.FilterId = Filter.FilterId "
            "AND Filter.Name = ?))"
        " AND "
        "(NOT EXISTS(" // 2. filter by version
        "SELECT * FROM "
            "VersionFilter, "
            "Filter "
        "WHERE VersionFilter.FilterId = Filter.FilterId "
            "AND Filter.Name = ?) "
        "OR NamespaceTable.Id IN ("
        "SELECT "
            "NamespaceTable.Id "
        "FROM "
            "NamespaceTable, "
            "VersionFilter, "
            "VersionTable, "
            "Filter "
        "WHERE VersionFilter.FilterId = Filter.FilterId "
            "AND ((VersionFilter.Version = VersionTable.Version) "
                "OR (VersionFilter.Version IS NULL AND VersionTable.Version IS NULL)) "
            "AND VersionTable.NamespaceId = NamespaceTable.Id "
            "AND Filter.Name = ?))"
        ")"_L1;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1029, as local:qhelpcollectionhandler.cpp:bindFilterQuery
static void bindFilterQuery(QSqlQuery *query, int bindStart, const QString &filterName)
{
    if (filterName.isEmpty())
        return;

    query->bindValue(bindStart, filterName);
    query->bindValue(bindStart + 1, filterName);
    query->bindValue(bindStart + 2, filterName);
    query->bindValue(bindStart + 3, filterName);
    query->bindValue(bindStart + 4, filterName);
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 170, as local:qhelpdbreader.cpp:isAttributeUsed
static bool isAttributeUsed(QSqlQuery *query, const QString &tableName, int attributeId)
{
    query->prepare(QString::fromLatin1("SELECT FilterAttributeId "
                                       "FROM %1 "
                                       "WHERE FilterAttributeId = ? "
                                       "LIMIT 1").arg(tableName));
    query->bindValue(0, attributeId);
    query->exec();
    return query->next(); // if we got a result it means it was used
}

//  from QtHelp__QHelpCollectionHandler.cpp, line 1, as moc:QHelpCollectionHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QHelpCollectionHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto QHelpCollectionHandler::qt_create_metaobjectdata<qt_meta_tag_ZN22QHelpCollectionHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QHelpCollectionHandler",
        "error",
        "",
        "msg"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'error'
        QtMocHelpers::SignalData<void(const QString &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 3 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QHelpCollectionHandler, qt_meta_tag_ZN22QHelpCollectionHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QHelpCollectionHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QHelpCollectionHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QHelpCollectionHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QHelpCollectionHandlerE_t>.metaTypes,
    nullptr
} };

void QHelpCollectionHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QHelpCollectionHandler *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->error((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QHelpCollectionHandler::*)(const QString & )>(_a, &QHelpCollectionHandler::error, 0))
            return;
    }
}

const QMetaObject *QHelpCollectionHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QHelpCollectionHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QHelpCollectionHandlerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QHelpCollectionHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QHelpCollectionHandler::error(const QString & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 37, as _ZN13QHelpDBReader4initEv
inline bool QHelpDBReader::init()
{
    if (m_initDone)
        return true;

    if (!QFile::exists(m_dbName))
        return false;

    if (!initDB()) {
        QSqlDatabase::removeDatabase(m_uniqueId);
        return false;
    }

    m_initDone = true;
    m_query.reset(new QSqlQuery(QSqlDatabase::database(m_uniqueId)));
    return true;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 25, as _ZN13QHelpDBReaderC1ERK7QStringS2_P7QObject
inline QHelpDBReader::QHelpDBReader(const QString &dbName, const QString &uniqueId, QObject *parent)
    : QObject(parent)
    , m_dbName(dbName)
    , m_uniqueId(uniqueId)
{}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 31, as _ZN13QHelpDBReaderD1Ev
inline QHelpDBReader::~QHelpDBReader()
{
    if (m_initDone)
        QSqlDatabase::removeDatabase(m_uniqueId);
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1914, as _ZN22QHelpCollectionHandler18registerIndexTableERKN13QHelpDBReader10IndexTableEiiRK7QString
inline bool QHelpCollectionHandler::registerIndexTable(const QHelpDBReader::IndexTable &indexTable,
                                                int nsId, int vfId, const QString &fileName)
{
    Transaction transaction(m_connectionName);

    QMap<QString, QVariantList> filterAttributeToNewFileId;

    QVariantList fileFolderIds;
    QVariantList fileNames;
    QVariantList fileTitles;
    const int fileSize = indexTable.fileItems.size();
    fileFolderIds.reserve(fileSize);
    fileNames.reserve(fileSize);
    fileTitles.reserve(fileSize);

    if (!m_query->exec("SELECT MAX(FileId) FROM FileNameTable"_L1) || !m_query->next())
        return false;

    const int maxFileId = m_query->value(0).toInt();

    int newFileId = 0;
    for (const QHelpDBReader::FileItem &item : indexTable.fileItems) {
        fileFolderIds.append(vfId);
        fileNames.append(item.name);
        fileTitles.append(item.title);

        for (const QString &filterAttribute : item.filterAttributes)
            filterAttributeToNewFileId[filterAttribute].append(maxFileId + newFileId + 1);
        ++newFileId;
    }

    m_query->prepare("INSERT INTO FileNameTable VALUES(?, ?, NULL, ?)"_L1);
    m_query->addBindValue(fileFolderIds);
    m_query->addBindValue(fileNames);
    m_query->addBindValue(fileTitles);
    if (!m_query->execBatch())
        return false;

    for (auto it = filterAttributeToNewFileId.cbegin(),
         end = filterAttributeToNewFileId.cend(); it != end; ++it) {
        const QString filterAttribute = it.key();
        m_query->prepare("SELECT Id From FilterAttributeTable WHERE Name = ?"_L1);
        m_query->bindValue(0, filterAttribute);
        if (!m_query->exec() || !m_query->next())
            return false;

        const int attributeId = m_query->value(0).toInt();

        QVariantList attributeIds;
        for (int i = 0; i < it.value().size(); i++)
            attributeIds.append(attributeId);

        m_query->prepare("INSERT INTO FileFilterTable VALUES(?, ?)"_L1);
        m_query->addBindValue(attributeIds);
        m_query->addBindValue(it.value());
        if (!m_query->execBatch())
            return false;
    }

    QMap<QString, QVariantList> filterAttributeToNewIndexId;

    if (!m_query->exec("SELECT MAX(Id) FROM IndexTable"_L1) || !m_query->next())
        return false;

    const int maxIndexId = m_query->value(0).toInt();
    int newIndexId = 0;

    QVariantList indexNames;
    QVariantList indexIdentifiers;
    QVariantList indexNamespaceIds;
    QVariantList indexFileIds;
    QVariantList indexAnchors;
    const int indexSize = indexTable.indexItems.size();
    indexNames.reserve(indexSize);
    indexIdentifiers.reserve(indexSize);
    indexNamespaceIds.reserve(indexSize);
    indexFileIds.reserve(indexSize);
    indexAnchors.reserve(indexSize);

    for (const QHelpDBReader::IndexItem &item : indexTable.indexItems) {
        indexNames.append(item.name);
        indexIdentifiers.append(item.identifier);
        indexNamespaceIds.append(nsId);
        indexFileIds.append(maxFileId + item.fileId + 1);
        indexAnchors.append(item.anchor);

        for (const QString &filterAttribute : item.filterAttributes)
            filterAttributeToNewIndexId[filterAttribute].append(maxIndexId + newIndexId + 1);
        ++newIndexId;
    }

    m_query->prepare("INSERT INTO IndexTable VALUES(NULL, ?, ?, ?, ?, ?)"_L1);
    m_query->addBindValue(indexNames);
    m_query->addBindValue(indexIdentifiers);
    m_query->addBindValue(indexNamespaceIds);
    m_query->addBindValue(indexFileIds);
    m_query->addBindValue(indexAnchors);
    if (!m_query->execBatch())
        return false;

    for (auto it = filterAttributeToNewIndexId.cbegin(),
         end = filterAttributeToNewIndexId.cend(); it != end; ++it) {
        const QString filterAttribute = it.key();
        m_query->prepare("SELECT Id From FilterAttributeTable WHERE Name = ?"_L1);
        m_query->bindValue(0, filterAttribute);
        if (!m_query->exec() || !m_query->next())
            return false;

        const int attributeId = m_query->value(0).toInt();

        QVariantList attributeIds;
        for (int i = 0; i < it.value().size(); i++)
            attributeIds.append(attributeId);

        m_query->prepare("INSERT INTO IndexFilterTable VALUES(?, ?)"_L1);
        m_query->addBindValue(attributeIds);
        m_query->addBindValue(it.value());
        if (!m_query->execBatch())
            return false;
    }

    QMap<QString, QVariantList> filterAttributeToNewContentsId;

    QVariantList contentsNsIds;
    QVariantList contentsData;
    const int contentsSize = indexTable.contentsItems.size();
    contentsNsIds.reserve(contentsSize);
    contentsData.reserve(contentsSize);

    if (!m_query->exec("SELECT MAX(Id) FROM ContentsTable"_L1) || !m_query->next())
        return false;

    const int maxContentsId = m_query->value(0).toInt();

    int newContentsId = 0;
    for (const QHelpDBReader::ContentsItem &item : indexTable.contentsItems) {
        contentsNsIds.append(nsId);
        contentsData.append(item.data);

        for (const QString &filterAttribute : item.filterAttributes) {
            filterAttributeToNewContentsId[filterAttribute]
                    .append(maxContentsId + newContentsId + 1);
        }
        ++newContentsId;
    }

    m_query->prepare("INSERT INTO ContentsTable VALUES(NULL, ?, ?)"_L1);
    m_query->addBindValue(contentsNsIds);
    m_query->addBindValue(contentsData);
    if (!m_query->execBatch())
        return false;

    for (auto it = filterAttributeToNewContentsId.cbegin(),
         end = filterAttributeToNewContentsId.cend(); it != end; ++it) {
        const QString filterAttribute = it.key();
        m_query->prepare("SELECT Id From FilterAttributeTable WHERE Name = ?"_L1);
        m_query->bindValue(0, filterAttribute);
        if (!m_query->exec() || !m_query->next())
            return false;

        const int attributeId = m_query->value(0).toInt();

        QVariantList attributeIds;
        for (int i = 0; i < it.value().size(); i++)
            attributeIds.append(attributeId);

        m_query->prepare("INSERT INTO ContentsFilterTable VALUES(?, ?)"_L1);
        m_query->addBindValue(attributeIds);
        m_query->addBindValue(it.value());
        if (!m_query->execBatch())
            return false;
    }

    QVariantList filterNsIds;
    QVariantList filterAttributeIds;
    for (const QString &filterAttribute : indexTable.usedFilterAttributes) {
        filterNsIds.append(nsId);

        m_query->prepare("SELECT Id From FilterAttributeTable WHERE Name = ?"_L1);
        m_query->bindValue(0, filterAttribute);
        if (!m_query->exec() || !m_query->next())
            return false;

        filterAttributeIds.append(m_query->value(0).toInt());
    }

    m_query->prepare("INSERT INTO OptimizedFilterTable "
                     "(NamespaceId, FilterAttributeId) VALUES(?, ?)"_L1);
    m_query->addBindValue(filterNsIds);
    m_query->addBindValue(filterAttributeIds);
    if (!m_query->execBatch())
        return false;

    m_query->prepare("INSERT INTO TimeStampTable "
                     "(NamespaceId, FolderId, FilePath, Size, TimeStamp) "
                     "VALUES(?, ?, ?, ?, ?)"_L1);
    m_query->addBindValue(nsId);
    m_query->addBindValue(vfId);
    m_query->addBindValue(fileName);
    const QFileInfo fi(absoluteDocPath(fileName));
    m_query->addBindValue(fi.size());
    QDateTime lastModified = fi.lastModified(QTimeZone::UTC);
    if (qEnvironmentVariableIsSet("SOURCE_DATE_EPOCH")) {
        const QString sourceDateEpochStr = qEnvironmentVariable("SOURCE_DATE_EPOCH");
        bool ok;
        const qlonglong sourceDateEpoch = sourceDateEpochStr.toLongLong(&ok);
        if (ok && sourceDateEpoch < lastModified.toSecsSinceEpoch())
            lastModified.setSecsSinceEpoch(sourceDateEpoch);
    }
    m_query->addBindValue(lastModified);
    if (!m_query->exec())
        return false;

    transaction.commit();
    return true;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 415, as _ZNK13QHelpDBReader13customFiltersEv
inline QStringList QHelpDBReader::customFilters() const
{
    QStringList lst;
    if (m_query) {
        m_query->exec("SELECT Name FROM FilterNameTable"_L1);
        while (m_query->next())
            lst.append(m_query->value(0).toString());
    }
    return lst;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 70, as _ZNK13QHelpDBReader13namespaceNameEv
inline QString QHelpDBReader::namespaceName() const
{
    if (!m_namespace.isEmpty())
        return m_namespace;
    if (m_query) {
        m_query->exec("SELECT Name FROM NamespaceTable"_L1);
        if (m_query->next())
            m_namespace = m_query->value(0).toString();
    }
    return m_namespace;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 82, as _ZNK13QHelpDBReader13virtualFolderEv
inline QString QHelpDBReader::virtualFolder() const
{
    if (m_query) {
        m_query->exec("SELECT Name FROM FolderTable WHERE Id=1"_L1);
        if (m_query->next())
            return m_query->value(0).toString();
    }
    return {};
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 426, as _ZNK13QHelpDBReader16filterAttributesERK7QString
inline QStringList QHelpDBReader::filterAttributes(const QString &filterName) const
{
    QStringList lst;
    if (m_query) {
        if (filterName.isEmpty()) {
            m_query->prepare("SELECT Name FROM FilterAttributeTable"_L1);
        } else {
            m_query->prepare(
                 "SELECT "
                     "FilterAttributeTable.Name "
                 "FROM "
                     "FilterAttributeTable, "
                     "FilterTable, "
                     "FilterNameTable "
                 "WHERE FilterNameTable.Name = ? "
                "AND FilterNameTable.Id = FilterTable.NameId "
                "AND FilterTable.FilterAttributeId = FilterAttributeTable.Id"_L1);
            m_query->bindValue(0, filterName);
        }
        m_query->exec();
        while (m_query->next())
            lst.append(m_query->value(0).toString());
    }
    return lst;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 357, as _ZNK13QHelpDBReader19filterAttributeSetsEv
inline QList<QStringList> QHelpDBReader::filterAttributeSets() const
{
    QList<QStringList> result;
    if (m_query) {
        m_query->exec(
            "SELECT "
                "FileAttributeSetTable.Id, "
                "FilterAttributeTable.Name "
            "FROM "
                "FileAttributeSetTable, "
                "FilterAttributeTable "
            "WHERE FileAttributeSetTable.FilterAttributeId = FilterAttributeTable.Id "
            "ORDER BY FileAttributeSetTable.Id"_L1);
        int oldId = -1;
        while (m_query->next()) {
            const int id = m_query->value(0).toInt();
            if (id != oldId) {
                result.append(QStringList());
                oldId = id;
            }
            result.last().append(m_query->value(1).toString());
        }
    }
    return result;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 92, as _ZNK13QHelpDBReader7versionEv
inline QString QHelpDBReader::version() const
{
    const QString versionString = metaData("version"_L1).toString();
    if (versionString.isEmpty())
        return qtVersionHeuristic();
    return versionString;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 55, as _ZN13QHelpDBReader6initDBEv
inline bool QHelpDBReader::initDB()
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE"_L1, m_uniqueId);
    db.setConnectOptions("QSQLITE_OPEN_READONLY"_L1);
    db.setDatabaseName(m_dbName);
    if (!db.open()) {
        /*: The placeholders are: %1 - The name of the database which cannot be opened
                                  %2 - The unique id for the connection
                                  %3 - The actual error string */
        m_error = tr("Cannot open database \"%1\" \"%2\": %3").arg(m_dbName, m_uniqueId, db.lastError().text());
        return false;
    }
    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 62, as _ZN22QHelpCollectionHandlerC1ERK7QStringP7QObject
inline QHelpCollectionHandler::QHelpCollectionHandler(const QString &collectionFile, QObject *parent)
    : QObject(parent)
    , m_collectionFile(collectionFile)
{
    const QFileInfo fi(m_collectionFile);
    if (!fi.isAbsolute())
        m_collectionFile = fi.absoluteFilePath();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 71, as _ZN22QHelpCollectionHandlerD1Ev
inline QHelpCollectionHandler::~QHelpCollectionHandler()
{
    closeDB();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 300, as _ZN22QHelpCollectionHandler18copyCollectionFileERK7QString
inline bool QHelpCollectionHandler::copyCollectionFile(const QString &fileName)
{
    if (!m_query)
        return false;

    const QFileInfo fi(fileName);
    if (fi.exists()) {
        emit error(tr("The collection file \"%1\" already exists.").arg(fileName));
        return false;
    }

    if (!fi.absoluteDir().exists() && !QDir().mkpath(fi.absolutePath())) {
        emit error(tr("Cannot create directory: %1").arg(fi.absolutePath()));
        return false;
    }

    const QString &colFile = fi.absoluteFilePath();
    const QString &connectionName =
            QHelpGlobal::uniquifyConnectionName("QHelpCollectionHandlerCopy"_L1, this);
    QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE"_L1, connectionName);
    db.setDatabaseName(colFile);
    if (!db.open()) {
        emit error(tr("Cannot open collection file: %1").arg(colFile));
        return false;
    }

    QSqlQuery copyQuery(db);
    copyQuery.exec("PRAGMA synchronous=OFF"_L1);
    copyQuery.exec("PRAGMA cache_size=3000"_L1);

    if (!createTables(&copyQuery) || !recreateIndexAndNamespaceFilterTables(&copyQuery)) {
        emit error(tr("Cannot copy collection file: %1").arg(colFile));
        return false;
    }

    const QString &oldBaseDir = QFileInfo(collectionFile()).absolutePath();
    const QFileInfo newColFi(colFile);
    m_query->exec("SELECT Name, FilePath FROM NamespaceTable"_L1);
    while (m_query->next()) {
        copyQuery.prepare("INSERT INTO NamespaceTable VALUES(NULL, ?, ?)"_L1);
        copyQuery.bindValue(0, m_query->value(0).toString());
        QString oldFilePath = m_query->value(1).toString();
        if (!QDir::isAbsolutePath(oldFilePath))
            oldFilePath = oldBaseDir + u'/' + oldFilePath;
        copyQuery.bindValue(1, newColFi.absoluteDir().relativeFilePath(oldFilePath));
        copyQuery.exec();
    }

    m_query->exec("SELECT NamespaceId, Name FROM FolderTable"_L1);
    while (m_query->next()) {
        copyQuery.prepare("INSERT INTO FolderTable VALUES(NULL, ?, ?)"_L1);
        copyQuery.bindValue(0, m_query->value(0).toString());
        copyQuery.bindValue(1, m_query->value(1).toString());
        copyQuery.exec();
    }

    m_query->exec("SELECT Name FROM FilterAttributeTable"_L1);
    while (m_query->next()) {
        copyQuery.prepare("INSERT INTO FilterAttributeTable VALUES(NULL, ?)"_L1);
        copyQuery.bindValue(0, m_query->value(0).toString());
        copyQuery.exec();
    }

    m_query->exec("SELECT Name FROM FilterNameTable"_L1);
    while (m_query->next()) {
        copyQuery.prepare("INSERT INTO FilterNameTable VALUES(NULL, ?)"_L1);
        copyQuery.bindValue(0, m_query->value(0).toString());
        copyQuery.exec();
    }

    m_query->exec("SELECT NameId, FilterAttributeId FROM FilterTable"_L1);
    while (m_query->next()) {
        copyQuery.prepare("INSERT INTO FilterTable VALUES(?, ?)"_L1);
        copyQuery.bindValue(0, m_query->value(0).toInt());
        copyQuery.bindValue(1, m_query->value(1).toInt());
        copyQuery.exec();
    }

    m_query->exec("SELECT Key, Value FROM SettingsTable"_L1);
    while (m_query->next()) {
        if (m_query->value(0).toString() == "FTS5IndexedNamespaces"_L1)
            continue;
        copyQuery.prepare("INSERT INTO SettingsTable VALUES(?, ?)"_L1);
        copyQuery.bindValue(0, m_query->value(0).toString());
        copyQuery.bindValue(1, m_query->value(1));
        copyQuery.exec();
    }

    copyQuery.clear();
    QSqlDatabase::removeDatabase(connectionName);
    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 508, as _ZNK22QHelpCollectionHandler13customFiltersEv
inline QStringList QHelpCollectionHandler::customFilters() const
{
    QStringList list;
    if (m_query) {
        m_query->exec("SELECT Name FROM FilterNameTable"_L1);
        while (m_query->next())
            list.append(m_query->value(0).toString());
    }
    return list;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 699, as _ZN22QHelpCollectionHandler18removeCustomFilterERK7QString
inline bool QHelpCollectionHandler::removeCustomFilter(const QString &filterName)
{
    if (!isDBOpened() || filterName.isEmpty())
        return false;

    int filterNameId = -1;
    m_query->prepare("SELECT Id FROM FilterNameTable WHERE Name=?"_L1);
    m_query->bindValue(0, filterName);
    m_query->exec();
    if (m_query->next())
        filterNameId = m_query->value(0).toInt();

    if (filterNameId < 0) {
        emit error(tr("Unknown filter \"%1\".").arg(filterName));
        return false;
    }

    m_query->prepare("DELETE FROM FilterTable WHERE NameId=?"_L1);
    m_query->bindValue(0, filterNameId);
    m_query->exec();

    m_query->prepare("DELETE FROM FilterNameTable WHERE Id=?"_L1);
    m_query->bindValue(0, filterNameId);
    m_query->exec();

    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 727, as _ZN22QHelpCollectionHandler15addCustomFilterERK7QStringRK5QListIS0_E
inline bool QHelpCollectionHandler::addCustomFilter(const QString &filterName,
                                             const QStringList &attributes)
{
    if (!isDBOpened() || filterName.isEmpty())
        return false;

    int nameId = -1;
    m_query->prepare("SELECT Id FROM FilterNameTable WHERE Name=?"_L1);
    m_query->bindValue(0, filterName);
    m_query->exec();
    if (m_query->next())
        nameId = m_query->value(0).toInt();

    m_query->exec("SELECT Id, Name FROM FilterAttributeTable"_L1);
    QStringList idsToInsert = attributes;
    QMap<QString, int> attributeMap;
    while (m_query->next()) {
        // all old attributes
        const QString attributeName = m_query->value(1).toString();
        attributeMap.insert(attributeName, m_query->value(0).toInt());
        idsToInsert.removeAll(attributeName);
    }

    for (const QString &id : std::as_const(idsToInsert)) {
        m_query->prepare("INSERT INTO FilterAttributeTable VALUES(NULL, ?)"_L1);
        m_query->bindValue(0, id);
        m_query->exec();
        attributeMap.insert(id, m_query->lastInsertId().toInt());
    }

    if (nameId < 0) {
        m_query->prepare("INSERT INTO FilterNameTable VALUES(NULL, ?)"_L1);
        m_query->bindValue(0, filterName);
        if (m_query->exec())
            nameId = m_query->lastInsertId().toInt();
    }

    if (nameId < 0) {
        emit error(tr("Cannot register filter %1.").arg(filterName));
        return false;
    }

    m_query->prepare("DELETE FROM FilterTable WHERE NameId=?"_L1);
    m_query->bindValue(0, nameId);
    m_query->exec();

    for (const QString &att : attributes) {
        m_query->prepare("INSERT INTO FilterTable VALUES(?, ?)"_L1);
        m_query->bindValue(0, nameId);
        m_query->bindValue(1, attributeMap[att]);
        if (!m_query->exec())
            return false;
    }
    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1667, as _ZNK22QHelpCollectionHandler16filterAttributesEv
inline QStringList QHelpCollectionHandler::filterAttributes() const
{
    QStringList list;
    if (m_query) {
        m_query->exec("SELECT Name FROM FilterAttributeTable"_L1);
        while (m_query->next())
            list.append(m_query->value(0).toString());
    }
    return list;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1678, as _ZNK22QHelpCollectionHandler16filterAttributesERK7QString
inline QStringList QHelpCollectionHandler::filterAttributes(const QString &filterName) const
{
    QStringList list;
    if (m_query) {
        m_query->prepare(
            "SELECT "
                "FilterAttributeTable.Name "
            "FROM "
                "FilterAttributeTable, "
                "FilterTable, "
                "FilterNameTable "
            "WHERE FilterAttributeTable.Id = FilterTable.FilterAttributeId "
            "AND FilterTable.NameId = FilterNameTable.Id "
            "AND FilterNameTable.Name=?"_L1);
        m_query->bindValue(0, filterName);
        m_query->exec();
        while (m_query->next())
            list.append(m_query->value(0).toString());
    }
    return list;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1700, as _ZNK22QHelpCollectionHandler19filterAttributeSetsERK7QString
inline QList<QStringList> QHelpCollectionHandler::filterAttributeSets(const QString &namespaceName) const
{
    if (!isDBOpened())
        return {};

    m_query->prepare(
        "SELECT "
            "FileAttributeSetTable.FilterAttributeSetId, "
            "FilterAttributeTable.Name "
        "FROM "
            "FileAttributeSetTable, "
            "FilterAttributeTable, "
            "NamespaceTable "
        "WHERE FileAttributeSetTable.FilterAttributeId = FilterAttributeTable.Id "
        "AND FileAttributeSetTable.NamespaceId = NamespaceTable.Id "
        "AND NamespaceTable.Name = ? "
        "ORDER BY FileAttributeSetTable.FilterAttributeSetId"_L1);
    m_query->bindValue(0, namespaceName);
    m_query->exec();
    int oldId = -1;
    QList<QStringList> result;
    while (m_query->next()) {
        const int id = m_query->value(0).toInt();
        if (id != oldId) {
            result.append(QStringList());
            oldId = id;
        }
        result.last().append(m_query->value(1).toString());
    }

    if (result.isEmpty())
        result.append(QStringList());
    return result;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 519, as _ZNK22QHelpCollectionHandler7filtersEv
inline QStringList QHelpCollectionHandler::filters() const
{
    QStringList list;
    if (m_query) {
        m_query->exec("SELECT Name FROM Filter ORDER BY Name"_L1);
        while (m_query->next())
            list.append(m_query->value(0).toString());
    }
    return list;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 530, as _ZNK22QHelpCollectionHandler19availableComponentsEv
inline QStringList QHelpCollectionHandler::availableComponents() const
{
    QStringList list;
    if (m_query) {
        m_query->exec("SELECT DISTINCT Name FROM ComponentTable ORDER BY Name"_L1);
        while (m_query->next())
            list.append(m_query->value(0).toString());
    }
    return list;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 541, as _ZNK22QHelpCollectionHandler17availableVersionsEv
inline QList<QVersionNumber> QHelpCollectionHandler::availableVersions() const
{
    QList<QVersionNumber> list;
    if (m_query) {
        m_query->exec("SELECT DISTINCT Version FROM VersionTable ORDER BY Version"_L1);
        while (m_query->next())
            list.append(QVersionNumber::fromString(m_query->value(0).toString()));
    }
    return list;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 552, as _ZNK22QHelpCollectionHandler20namespaceToComponentEv
inline QMap<QString, QString> QHelpCollectionHandler::namespaceToComponent() const
{
    QMap<QString, QString> result;
    if (m_query) {
        m_query->exec(
            "SELECT "
                "NamespaceTable.Name, "
                "ComponentTable.Name "
            "FROM NamespaceTable, "
                "ComponentTable, "
                "ComponentMapping "
            "WHERE NamespaceTable.Id = ComponentMapping.NamespaceId "
            "AND ComponentMapping.ComponentId = ComponentTable.ComponentId"_L1);
        while (m_query->next())
            result.insert(m_query->value(0).toString(), m_query->value(1).toString());
    }
    return result;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 571, as _ZNK22QHelpCollectionHandler18namespaceToVersionEv
inline QMap<QString, QVersionNumber> QHelpCollectionHandler::namespaceToVersion() const
{
    QMap<QString, QVersionNumber> result;
    if (m_query) {
        m_query->exec(
            "SELECT "
                "NamespaceTable.Name, "
                "VersionTable.Version "
            "FROM NamespaceTable, "
                "VersionTable "
            "WHERE NamespaceTable.Id = VersionTable.NamespaceId"_L1);
        while (m_query->next()) {
            result.insert(m_query->value(0).toString(),
                QVersionNumber::fromString(m_query->value(1).toString()));
        }
    }
    return result;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 590, as _ZNK22QHelpCollectionHandler10filterDataERK7QString
inline QHelpFilterData QHelpCollectionHandler::filterData(const QString &filterName) const
{
    QStringList components;
    QList<QVersionNumber> versions;
    if (m_query) {
        m_query->prepare(
            "SELECT ComponentFilter.ComponentName "
            "FROM ComponentFilter, Filter "
            "WHERE ComponentFilter.FilterId = Filter.FilterId "
            "AND Filter.Name = ? "
            "ORDER BY ComponentFilter.ComponentName"_L1);
        m_query->bindValue(0, filterName);
        m_query->exec();
        while (m_query->next())
            components.append(m_query->value(0).toString());

        m_query->prepare(
            "SELECT VersionFilter.Version "
            "FROM VersionFilter, Filter "
            "WHERE VersionFilter.FilterId = Filter.FilterId "
            "AND Filter.Name = ? "
            "ORDER BY VersionFilter.Version"_L1);
        m_query->bindValue(0, filterName);
        m_query->exec();
        while (m_query->next())
            versions.append(QVersionNumber::fromString(m_query->value(0).toString()));

    }
    QHelpFilterData data;
    data.setComponents(components);
    data.setVersions(versions);
    return data;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 624, as _ZN22QHelpCollectionHandler13setFilterDataERK7QStringRK15QHelpFilterData
inline bool QHelpCollectionHandler::setFilterData(const QString &filterName,
                                           const QHelpFilterData &filterData)
{
    if (!removeFilter(filterName))
        return false;

    m_query->prepare("INSERT INTO Filter VALUES (NULL, ?)"_L1);
    m_query->bindValue(0, filterName);
    if (!m_query->exec())
        return false;

    const int filterId = m_query->lastInsertId().toInt();

    QVariantList componentList;
    QVariantList versionList;
    QVariantList filterIdList;

    const auto &components = filterData.components();
    for (const QString &component : components) {
        componentList.append(component);
        filterIdList.append(filterId);
    }

    m_query->prepare("INSERT INTO ComponentFilter VALUES (?, ?)"_L1);
    m_query->addBindValue(componentList);
    m_query->addBindValue(filterIdList);
    if (!m_query->execBatch())
        return false;

    filterIdList.clear();
    const auto &versions = filterData.versions();
    for (const QVersionNumber &version : versions) {
        versionList.append(version.isNull() ? QString() : version.toString());
        filterIdList.append(filterId);
    }

    m_query->prepare("INSERT INTO VersionFilter VALUES (?, ?)"_L1);
    m_query->addBindValue(versionList);
    m_query->addBindValue(filterIdList);
    if (!m_query->execBatch())
        return false;

    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 669, as _ZN22QHelpCollectionHandler12removeFilterERK7QString
inline bool QHelpCollectionHandler::removeFilter(const QString &filterName)
{
    m_query->prepare("SELECT FilterId FROM Filter WHERE Name = ?"_L1);
    m_query->bindValue(0, filterName);
    if (!m_query->exec())
        return false;

    if (!m_query->next())
        return true; // no filter in DB

    const int filterId = m_query->value(0).toInt();

    m_query->prepare("DELETE FROM Filter WHERE Filter.Name = ?"_L1);
    m_query->bindValue(0, filterName);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM ComponentFilter WHERE ComponentFilter.FilterId = ?"_L1);
    m_query->bindValue(0, filterId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM VersionFilter WHERE VersionFilter.FilterId = ?"_L1);
    m_query->bindValue(0, filterId);
    if (!m_query->exec())
        return false;

    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 783, as _ZNK22QHelpCollectionHandler23registeredDocumentationERK7QString
inline QHelpCollectionHandler::FileInfo QHelpCollectionHandler::registeredDocumentation(
        const QString &namespaceName) const
{
    FileInfo fileInfo;

    if (!m_query)
        return fileInfo;

    m_query->prepare(
        "SELECT "
            "NamespaceTable.Name, "
            "NamespaceTable.FilePath, "
            "FolderTable.Name "
        "FROM "
            "NamespaceTable, "
            "FolderTable "
        "WHERE NamespaceTable.Id = FolderTable.NamespaceId "
        "AND NamespaceTable.Name = ? LIMIT 1"_L1);
    m_query->bindValue(0, namespaceName);
    if (!m_query->exec() || !m_query->next())
        return fileInfo;

    fileInfo.namespaceName = m_query->value(0).toString();
    fileInfo.fileName = m_query->value(1).toString();
    fileInfo.folderName = m_query->value(2).toString();

    m_query->clear();

    return fileInfo;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 814, as _ZNK22QHelpCollectionHandler24registeredDocumentationsEv
inline QHelpCollectionHandler::FileInfoList QHelpCollectionHandler::registeredDocumentations() const
{
    FileInfoList list;
    if (!m_query)
        return list;

    m_query->exec(
        "SELECT "
            "NamespaceTable.Name, "
            "NamespaceTable.FilePath, "
            "FolderTable.Name "
        "FROM "
            "NamespaceTable, "
            "FolderTable "
        "WHERE NamespaceTable.Id = FolderTable.NamespaceId"_L1);

    while (m_query->next()) {
        FileInfo fileInfo;
        fileInfo.namespaceName = m_query->value(0).toString();
        fileInfo.fileName = m_query->value(1).toString();
        fileInfo.folderName = m_query->value(2).toString();
        list.append(fileInfo);
    }

    return list;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 879, as _ZN22QHelpCollectionHandler23unregisterDocumentationERK7QString
inline bool QHelpCollectionHandler::unregisterDocumentation(const QString &namespaceName)
{
    if (!isDBOpened())
        return false;

    m_query->prepare("SELECT Id FROM NamespaceTable WHERE Name = ?"_L1);
    m_query->bindValue(0, namespaceName);
    m_query->exec();

    if (!m_query->next()) {
        emit error(tr("The namespace %1 was not registered.").arg(namespaceName));
        return false;
    }

    const int nsId = m_query->value(0).toInt();

    m_query->prepare("DELETE FROM NamespaceTable WHERE Id = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("SELECT Id FROM FolderTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    m_query->exec();

    if (!m_query->next()) {
        emit error(tr("The namespace %1 was not registered.").arg(namespaceName));
        return false;
    }

    const int vfId = m_query->value(0).toInt();

    m_query->prepare("DELETE FROM NamespaceTable WHERE Id = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM FolderTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    if (!unregisterIndexTable(nsId, vfId))
        return false;

    scheduleVacuum();

    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1544, as _ZN22QHelpCollectionHandler17removeCustomValueERK7QString
inline bool QHelpCollectionHandler::removeCustomValue(const QString &key)
{
    if (!isDBOpened())
        return false;

    m_query->prepare("DELETE FROM SettingsTable WHERE Key=?"_L1);
    m_query->bindValue(0, key);
    return m_query->exec();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1554, as _ZNK22QHelpCollectionHandler11customValueERK7QStringRK8QVariant
inline QVariant QHelpCollectionHandler::customValue(const QString &key,
                                             const QVariant &defaultValue) const
{
    if (!m_query)
        return defaultValue;

    m_query->prepare("SELECT COUNT(Key) FROM SettingsTable WHERE Key=?"_L1);
    m_query->bindValue(0, key);
    if (!m_query->exec() || !m_query->next() || !m_query->value(0).toInt()) {
        m_query->clear();
        return defaultValue;
    }

    m_query->clear();
    m_query->prepare("SELECT Value FROM SettingsTable WHERE Key=?"_L1);
    m_query->bindValue(0, key);
    if (m_query->exec() && m_query->next()) {
        const QVariant &value = m_query->value(0);
        m_query->clear();
        return value;
    }
    return defaultValue;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1578, as _ZN22QHelpCollectionHandler14setCustomValueERK7QStringRK8QVariant
inline bool QHelpCollectionHandler::setCustomValue(const QString &key,
                                            const QVariant &value)
{
    if (!isDBOpened())
        return false;

    m_query->prepare("SELECT Value FROM SettingsTable WHERE Key=?"_L1);
    m_query->bindValue(0, key);
    m_query->exec();
    if (m_query->next()) {
        m_query->prepare("UPDATE SettingsTable SET Value=? where Key=?"_L1);
        m_query->bindValue(0, value);
        m_query->bindValue(1, key);
    } else {
        m_query->prepare("INSERT INTO SettingsTable VALUES(?, ?)"_L1);
        m_query->bindValue(0, key);
        m_query->bindValue(1, value);
    }
    return m_query->exec();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1757, as _ZN22QHelpCollectionHandler17registerNamespaceERK7QStringS2_
inline int QHelpCollectionHandler::registerNamespace(const QString &nspace, const QString &fileName)
{
    const int errorValue = -1;
    if (!m_query)
        return errorValue;

    m_query->prepare("SELECT COUNT(Id) FROM NamespaceTable WHERE Name=?"_L1);
    m_query->bindValue(0, nspace);
    m_query->exec();
    while (m_query->next()) {
        if (m_query->value(0).toInt() > 0) {
            emit error(tr("Namespace %1 already exists.").arg(nspace));
            return errorValue;
        }
    }

    QFileInfo fi(m_collectionFile);
    m_query->prepare("INSERT INTO NamespaceTable VALUES(NULL, ?, ?)"_L1);
    m_query->bindValue(0, nspace);
    m_query->bindValue(1, fi.absoluteDir().relativeFilePath(fileName));
    int namespaceId = errorValue;
    if (m_query->exec()) {
        namespaceId = m_query->lastInsertId().toInt();
        m_query->clear();
    }
    if (namespaceId < 1) {
        emit error(tr("Cannot register namespace \"%1\".").arg(nspace));
        return errorValue;
    }
    return namespaceId;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1789, as _ZN22QHelpCollectionHandler21registerVirtualFolderERK7QStringi
inline int QHelpCollectionHandler::registerVirtualFolder(const QString &folderName, int namespaceId)
{
    if (!m_query)
        return false;

    m_query->prepare("INSERT INTO FolderTable VALUES(NULL, ?, ?)"_L1);
    m_query->bindValue(0, namespaceId);
    m_query->bindValue(1, folderName);

    int virtualId = -1;
    if (m_query->exec()) {
        virtualId = m_query->lastInsertId().toInt();
        m_query->clear();
    }
    if (virtualId < 1) {
        emit error(tr("Cannot register virtual folder '%1'.").arg(folderName));
        return -1;
    }
    if (registerComponent(folderName, namespaceId) < 0)
        return -1;
    return virtualId;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1812, as _ZN22QHelpCollectionHandler17registerComponentERK7QStringi
inline int QHelpCollectionHandler::registerComponent(const QString &componentName, int namespaceId)
{
    m_query->prepare("SELECT ComponentId FROM ComponentTable WHERE Name = ?"_L1);
    m_query->bindValue(0, componentName);
    if (!m_query->exec())
        return -1;

    if (!m_query->next()) {
        m_query->prepare("INSERT INTO ComponentTable VALUES(NULL, ?)"_L1);
        m_query->bindValue(0, componentName);
        if (!m_query->exec())
            return -1;

        m_query->prepare("SELECT ComponentId FROM ComponentTable WHERE Name = ?"_L1);
        m_query->bindValue(0, componentName);
        if (!m_query->exec() || !m_query->next())
            return -1;
    }

    const int componentId = m_query->value(0).toInt();

    m_query->prepare("INSERT INTO ComponentMapping VALUES(?, ?)"_L1);
    m_query->bindValue(0, componentId);
    m_query->bindValue(1, namespaceId);
    if (!m_query->exec())
        return -1;

    return componentId;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1842, as _ZN22QHelpCollectionHandler15registerVersionERK7QStringi
inline bool QHelpCollectionHandler::registerVersion(const QString &version, int namespaceId)
{
    if (!m_query)
        return false;

    m_query->prepare("INSERT INTO VersionTable (NamespaceId, Version) VALUES(?, ?)"_L1);
    m_query->addBindValue(namespaceId);
    m_query->addBindValue(version);
    return m_query->exec();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 2216, as _ZN22QHelpCollectionHandler9buildQUrlERK7QStringS2_S2_S2_
inline QUrl QHelpCollectionHandler::buildQUrl(const QString &ns, const QString &folder,
                                       const QString &relFileName, const QString &anchor)
{
    QUrl url;
    url.setScheme("qthelp"_L1);
    url.setAuthority(ns);
    url.setPath(u'/' + folder + u'/' + relFileName);
    url.setFragment(anchor);
    return url;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1735, as _ZNK22QHelpCollectionHandler16namespaceVersionERK7QString
inline QString QHelpCollectionHandler::namespaceVersion(const QString &namespaceName) const
{
    if (!m_query)
        return {};

    m_query->prepare(
        "SELECT "
            "VersionTable.Version "
        "FROM "
            "NamespaceTable, "
            "VersionTable "
        "WHERE NamespaceTable.Name = ? "
        "AND NamespaceTable.Id = VersionTable.NamespaceId"_L1);
    m_query->bindValue(0, namespaceName);
    if (!m_query->exec() || !m_query->next())
        return {};

    const QString ret = m_query->value(0).toString();
    m_query->clear();
    return ret;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 76, as _ZNK22QHelpCollectionHandler10isDBOpenedEv
inline bool QHelpCollectionHandler::isDBOpened() const
{
    if (m_query)
        return true;
    auto *that = const_cast<QHelpCollectionHandler *>(this);
    emit that->error(tr("The collection file \"%1\" is not set up yet.").arg(m_collectionFile));
    return false;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 393, as _ZN22QHelpCollectionHandler12createTablesEP9QSqlQuery
inline bool QHelpCollectionHandler::createTables(QSqlQuery *query)
{
    const QStringList tables = {
        "CREATE TABLE NamespaceTable ("
            "Id INTEGER PRIMARY KEY, "
            "Name TEXT, "
            "FilePath TEXT )"_L1,
        "CREATE TABLE FolderTable ("
            "Id INTEGER PRIMARY KEY, "
            "NamespaceId INTEGER, "
            "Name TEXT )"_L1,
        "CREATE TABLE FilterAttributeTable ("
            "Id INTEGER PRIMARY KEY, "
            "Name TEXT )"_L1,
        "CREATE TABLE FilterNameTable ("
            "Id INTEGER PRIMARY KEY, "
            "Name TEXT )"_L1,
        "CREATE TABLE FilterTable ("
            "NameId INTEGER, "
            "FilterAttributeId INTEGER )"_L1,
        "CREATE TABLE SettingsTable ("
            "Key TEXT PRIMARY KEY, "
            "Value BLOB )"_L1
    };

    for (const QString &q : tables) {
        if (!query->exec(q))
            return false;
    }
    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 85, as _ZN22QHelpCollectionHandler7closeDBEv
inline void QHelpCollectionHandler::closeDB()
{
    if (!m_query)
        return;

    m_query.reset();
    QSqlDatabase::removeDatabase(m_connectionName);
    m_connectionName.clear();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 425, as _ZN22QHelpCollectionHandler37recreateIndexAndNamespaceFilterTablesEP9QSqlQuery
inline bool QHelpCollectionHandler::recreateIndexAndNamespaceFilterTables(QSqlQuery *query)
{
    const QStringList tables = {
        "DROP TABLE IF EXISTS FileNameTable"_L1,
        "DROP TABLE IF EXISTS IndexTable"_L1,
        "DROP TABLE IF EXISTS ContentsTable"_L1,
        "DROP TABLE IF EXISTS FileFilterTable"_L1, // legacy
        "DROP TABLE IF EXISTS IndexFilterTable"_L1, // legacy
        "DROP TABLE IF EXISTS ContentsFilterTable"_L1, // legacy
        "DROP TABLE IF EXISTS FileAttributeSetTable"_L1, // legacy
        "DROP TABLE IF EXISTS OptimizedFilterTable"_L1, // legacy
        "DROP TABLE IF EXISTS TimeStampTable"_L1,
        "DROP TABLE IF EXISTS VersionTable"_L1,
        "DROP TABLE IF EXISTS Filter"_L1,
        "DROP TABLE IF EXISTS ComponentTable"_L1,
        "DROP TABLE IF EXISTS ComponentMapping"_L1,
        "DROP TABLE IF EXISTS ComponentFilter"_L1,
        "DROP TABLE IF EXISTS VersionFilter"_L1,
        "CREATE TABLE FileNameTable ("
            "FolderId INTEGER, "
            "Name TEXT, "
            "FileId INTEGER PRIMARY KEY, "
            "Title TEXT)"_L1,
        "CREATE TABLE IndexTable ("
            "Id INTEGER PRIMARY KEY, "
            "Name TEXT, "
            "Identifier TEXT, "
            "NamespaceId INTEGER, "
            "FileId INTEGER, "
            "Anchor TEXT)"_L1,
        "CREATE TABLE ContentsTable ("
            "Id INTEGER PRIMARY KEY, "
            "NamespaceId INTEGER, "
            "Data BLOB)"_L1,
        "CREATE TABLE FileFilterTable ("
            "FilterAttributeId INTEGER, "
            "FileId INTEGER)"_L1,
        "CREATE TABLE IndexFilterTable ("
            "FilterAttributeId INTEGER, "
            "IndexId INTEGER)"_L1,
        "CREATE TABLE ContentsFilterTable ("
            "FilterAttributeId INTEGER, "
            "ContentsId INTEGER )"_L1,
        "CREATE TABLE FileAttributeSetTable ("
            "NamespaceId INTEGER, "
            "FilterAttributeSetId INTEGER, "
            "FilterAttributeId INTEGER)"_L1,
        "CREATE TABLE OptimizedFilterTable ("
            "NamespaceId INTEGER, "
            "FilterAttributeId INTEGER)"_L1,
        "CREATE TABLE TimeStampTable ("
            "NamespaceId INTEGER, "
            "FolderId INTEGER, "
            "FilePath TEXT, "
            "Size INTEGER, "
            "TimeStamp TEXT)"_L1,
        "CREATE TABLE VersionTable ("
            "NamespaceId INTEGER, "
            "Version TEXT)"_L1,
        "CREATE TABLE Filter ("
            "FilterId INTEGER PRIMARY KEY, "
            "Name TEXT)"_L1,
        "CREATE TABLE ComponentTable ("
            "ComponentId INTEGER PRIMARY KEY, "
            "Name TEXT)"_L1,
        "CREATE TABLE ComponentMapping ("
            "ComponentId INTEGER, "
            "NamespaceId INTEGER)"_L1,
        "CREATE TABLE ComponentFilter ("
            "ComponentName TEXT, "
            "FilterId INTEGER)"_L1,
        "CREATE TABLE VersionFilter ("
            "Version TEXT, "
            "FilterId INTEGER)"_L1
    };

    for (const QString &q : tables) {
        if (!query->exec(q))
            return false;
    }
    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1896, as _ZN22QHelpCollectionHandler19createVersionFilterERK7QString
inline void QHelpCollectionHandler::createVersionFilter(const QString &version)
{
    if (version.isEmpty())
        return;

    const QVersionNumber versionNumber = QVersionNumber::fromString(version);
    if (versionNumber.isNull())
        return;

    const QString filterName = tr("Version %1").arg(version);
    if (filters().contains(filterName))
        return;

    QHelpFilterData filterData;
    filterData.setVersions({versionNumber});
    setFilterData(filterName, filterData);
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1599, as _ZN22QHelpCollectionHandler24registerFilterAttributesERK5QListIS0_I7QStringEEi
inline bool QHelpCollectionHandler::registerFilterAttributes(const QList<QStringList> &attributeSets,
                                                      int nsId)
{
    if (!isDBOpened())
        return false;

    m_query->exec("SELECT Name FROM FilterAttributeTable"_L1);
    QSet<QString> atts;
    while (m_query->next())
        atts.insert(m_query->value(0).toString());

    for (const QStringList &attributeSet : attributeSets) {
        for (const QString &attribute : attributeSet) {
            if (!atts.contains(attribute)) {
                m_query->prepare("INSERT INTO FilterAttributeTable VALUES(NULL, ?)"_L1);
                m_query->bindValue(0, attribute);
                m_query->exec();
            }
        }
    }
    return registerFileAttributeSets(attributeSets, nsId);
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 1622, as _ZN22QHelpCollectionHandler25registerFileAttributeSetsERK5QListIS0_I7QStringEEi
inline bool QHelpCollectionHandler::registerFileAttributeSets(const QList<QStringList> &attributeSets,
                                                       int nsId)
{
    if (!isDBOpened())
        return false;

    if (attributeSets.isEmpty())
        return true;

    QVariantList nsIds;
    QVariantList attributeSetIds;
    QVariantList filterAttributeIds;

    if (!m_query->exec("SELECT MAX(FilterAttributeSetId) FROM FileAttributeSetTable"_L1)
        || !m_query->next()) {
        return false;
    }

    int attributeSetId = m_query->value(0).toInt();

    for (const QStringList &attributeSet : attributeSets) {
        ++attributeSetId;

        for (const QString &attribute : attributeSet) {
            m_query->prepare("SELECT Id FROM FilterAttributeTable WHERE Name=?"_L1);
            m_query->bindValue(0, attribute);

            if (!m_query->exec() || !m_query->next())
                return false;

            nsIds.append(nsId);
            attributeSetIds.append(attributeSetId);
            filterAttributeIds.append(m_query->value(0).toInt());
        }
    }

    m_query->prepare("INSERT INTO FileAttributeSetTable "
                     "(NamespaceId, FilterAttributeSetId, FilterAttributeId) "
                     "VALUES(?, ?, ?)"_L1);
    m_query->addBindValue(nsIds);
    m_query->addBindValue(attributeSetIds);
    m_query->addBindValue(filterAttributeIds);
    return m_query->execBatch();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 2131, as _ZN22QHelpCollectionHandler20unregisterIndexTableEii
inline bool QHelpCollectionHandler::unregisterIndexTable(int nsId, int vfId)
{
    m_query->prepare("DELETE FROM IndexFilterTable WHERE IndexId IN "
                         "(SELECT Id FROM IndexTable WHERE NamespaceId = ?)"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM IndexTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM FileFilterTable WHERE FileId IN "
                         "(SELECT FileId FROM FileNameTable WHERE FolderId = ?)"_L1);
    m_query->bindValue(0, vfId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM FileNameTable WHERE FolderId = ?"_L1);
    m_query->bindValue(0, vfId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM ContentsFilterTable WHERE ContentsId IN "
                         "(SELECT Id FROM ContentsTable WHERE NamespaceId = ?)"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM ContentsTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM FileAttributeSetTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM OptimizedFilterTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM TimeStampTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("DELETE FROM VersionTable WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("SELECT ComponentId FROM ComponentMapping WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    if (!m_query->next())
        return false;

    const int componentId = m_query->value(0).toInt();

    m_query->prepare("DELETE FROM ComponentMapping WHERE NamespaceId = ?"_L1);
    m_query->bindValue(0, nsId);
    if (!m_query->exec())
        return false;

    m_query->prepare("SELECT ComponentId FROM ComponentMapping WHERE ComponentId = ?"_L1);
    m_query->bindValue(0, componentId);
    if (!m_query->exec())
        return false;

    if (!m_query->next()) { // no more namespaces refer to the componentId
        m_query->prepare("DELETE FROM ComponentTable WHERE ComponentId = ?"_L1);
        m_query->bindValue(0, componentId);
        if (!m_query->exec())
            return false;
    }

    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 227, as _ZNK22QHelpCollectionHandler15absoluteDocPathERK7QString
inline QString QHelpCollectionHandler::absoluteDocPath(const QString &fileName) const
{
    const QFileInfo fi(collectionFile());
    return QDir::isAbsolutePath(fileName)
            ? fileName
            : QFileInfo(fi.absolutePath() + u'/' + fileName).absoluteFilePath();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 235, as _ZNK22QHelpCollectionHandler18isTimeStampCorrectERKNS_9TimeStampE
inline bool QHelpCollectionHandler::isTimeStampCorrect(const TimeStamp &timeStamp) const
{
    const QFileInfo fi(absoluteDocPath(timeStamp.fileName));

    if (!fi.exists())
        return false;

    if (fi.size() != timeStamp.size)
        return false;

    if (fi.lastModified(QTimeZone::UTC) != timeStamp.timeStamp)
        return false;

    m_query->prepare("SELECT FilePath FROM NamespaceTable WHERE Id = ?"_L1);
    m_query->bindValue(0, timeStamp.namespaceId);
    if (!m_query->exec() || !m_query->next())
        return false;

    const QString oldFileName = m_query->value(0).toString();
    m_query->clear();
    if (oldFileName != timeStamp.fileName)
        return false;

    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 261, as _ZNK22QHelpCollectionHandler16hasTimeStampInfoERK7QString
inline bool QHelpCollectionHandler::hasTimeStampInfo(const QString &nameSpace) const
{
    m_query->prepare(
        "SELECT "
            "TimeStampTable.NamespaceId "
        "FROM "
            "NamespaceTable, "
            "TimeStampTable "
        "WHERE NamespaceTable.Id = TimeStampTable.NamespaceId "
        "AND NamespaceTable.Name = ? LIMIT 1"_L1);
    m_query->bindValue(0, nameSpace);
    if (!m_query->exec())
        return false;

    if (!m_query->next())
        return false;

    m_query->clear();
    return true;
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 282, as _ZN22QHelpCollectionHandler14scheduleVacuumEv
inline void QHelpCollectionHandler::scheduleVacuum()
{
    if (m_vacuumScheduled)
        return;

    m_vacuumScheduled = true;
    QTimer::singleShot(0, this, &QHelpCollectionHandler::execVacuum);
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 291, as _ZN22QHelpCollectionHandler10execVacuumEv
inline void QHelpCollectionHandler::execVacuum()
{
    if (!m_query)
        return;

    m_query->exec("VACUUM"_L1);
    m_vacuumScheduled = false;
}
//  -----------------------------------------------------------------------

//  A QHelpCollectionHandler that Python can take functions over in. Every QHelpCollectionHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpCollectionHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpCollectionHandlerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpCollectionHandler : public QHelpCollectionHandler {
public:
  using QHelpCollectionHandler::QHelpCollectionHandler;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall0 call = reinterpret_cast<CuteQHelpCollectionHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall1 call = reinterpret_cast<CuteQHelpCollectionHandlerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall2 call = reinterpret_cast<CuteQHelpCollectionHandlerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall3 call = reinterpret_cast<CuteQHelpCollectionHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall4 call = reinterpret_cast<CuteQHelpCollectionHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall5 call = reinterpret_cast<CuteQHelpCollectionHandlerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall6 call = reinterpret_cast<CuteQHelpCollectionHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpCollectionHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QHelpCollectionHandler10metaObjectEv(
    const QHelpCollectionHandler *self) {
  return self->metaObject();
}

//  void *QHelpCollectionHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QHelpCollectionHandler11qt_metacastEPKc(
    QHelpCollectionHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHelpCollectionHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QHelpCollectionHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QHelpCollectionHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHelpCollectionHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QHelpCollectionHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpCollectionHandler::tr(s, c, n));
}

//  QHelpCollectionHandler::QHelpCollectionHandler(const QString
//      &collectionFile, QObject *parent)
extern "C" Q_DECL_EXPORT
QHelpCollectionHandler *ritual_ZN22QHelpCollectionHandlerC1ERK7QStringP7QObject(
    const QString *collectionFile,
    QObject *parent) {
  return new CuteQHelpCollectionHandler(*collectionFile, parent);
}

//  QHelpCollectionHandler::~QHelpCollectionHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandlerD1Ev(QHelpCollectionHandler *self) {
  delete self;
}

//  QString QHelpCollectionHandler::collectionFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHelpCollectionHandler14collectionFileEv(
    const QHelpCollectionHandler *self) {
  return new QString(self->collectionFile());
}

//  bool QHelpCollectionHandler::copyCollectionFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler18copyCollectionFileERK7QString(
    QHelpCollectionHandler *self,
    const QString *fileName) {
  return self->copyCollectionFile(*fileName);
}

//  QStringList QHelpCollectionHandler::customFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QHelpCollectionHandler13customFiltersEv(
    const QHelpCollectionHandler *self) {
  return new QList<QString>(self->customFilters());
}

//  bool QHelpCollectionHandler::removeCustomFilter(const QString
//      &filterName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler18removeCustomFilterERK7QString(
    QHelpCollectionHandler *self,
    const QString *filterName) {
  return self->removeCustomFilter(*filterName);
}

//  bool QHelpCollectionHandler::addCustomFilter(const QString &filterName,
//      const QStringList &attributes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler15addCustomFilterERK7QStringRK5QListIS0_E(
    QHelpCollectionHandler *self,
    const QString *filterName,
    const QList<QString> *attributes) {
  return self->addCustomFilter(*filterName, *attributes);
}

//  QStringList QHelpCollectionHandler::filterAttributes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QHelpCollectionHandler16filterAttributesEv(
    const QHelpCollectionHandler *self) {
  return new QList<QString>(self->filterAttributes());
}

//  QStringList QHelpCollectionHandler::filterAttributes(const QString
//      &filterName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QHelpCollectionHandler16filterAttributesERK7QString(
    const QHelpCollectionHandler *self,
    const QString *filterName) {
  return new QList<QString>(self->filterAttributes(*filterName));
}

//  QList<QStringList> QHelpCollectionHandler::filterAttributeSets(const
//      QString &namespaceName) const
extern "C" Q_DECL_EXPORT
QList<QStringList> *ritual_ZNK22QHelpCollectionHandler19filterAttributeSetsERK7QString(
    const QHelpCollectionHandler *self,
    const QString *namespaceName) {
  return new QList<QStringList>(self->filterAttributeSets(*namespaceName));
}

//  QStringList QHelpCollectionHandler::filters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QHelpCollectionHandler7filtersEv(
    const QHelpCollectionHandler *self) {
  return new QList<QString>(self->filters());
}

//  QStringList QHelpCollectionHandler::availableComponents() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QHelpCollectionHandler19availableComponentsEv(
    const QHelpCollectionHandler *self) {
  return new QList<QString>(self->availableComponents());
}

//  QList<QVersionNumber> QHelpCollectionHandler::availableVersions() const
extern "C" Q_DECL_EXPORT
QList<QVersionNumber> *ritual_ZNK22QHelpCollectionHandler17availableVersionsEv(
    const QHelpCollectionHandler *self) {
  return new QList<QVersionNumber>(self->availableVersions());
}

//  QMap<QString, QString> QHelpCollectionHandler::namespaceToComponent()
//      const
extern "C" Q_DECL_EXPORT
QMap<QString, QString> *ritual_ZNK22QHelpCollectionHandler20namespaceToComponentEv(
    const QHelpCollectionHandler *self) {
  return new QMap<QString, QString>(self->namespaceToComponent());
}

//  QMap<QString, QVersionNumber>
//      QHelpCollectionHandler::namespaceToVersion() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVersionNumber> *ritual_ZNK22QHelpCollectionHandler18namespaceToVersionEv(
    const QHelpCollectionHandler *self) {
  return new QMap<QString, QVersionNumber>(self->namespaceToVersion());
}

//  QHelpFilterData QHelpCollectionHandler::filterData(const QString
//      &filterName) const
extern "C" Q_DECL_EXPORT
QHelpFilterData *ritual_ZNK22QHelpCollectionHandler10filterDataERK7QString(
    const QHelpCollectionHandler *self,
    const QString *filterName) {
  return new QHelpFilterData(self->filterData(*filterName));
}

//  bool QHelpCollectionHandler::setFilterData(const QString &filterName,
//      const QHelpFilterData &filterData)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler13setFilterDataERK7QStringRK15QHelpFilterData(
    QHelpCollectionHandler *self,
    const QString *filterName,
    const QHelpFilterData *filterData) {
  return self->setFilterData(*filterName, *filterData);
}

//  bool QHelpCollectionHandler::removeFilter(const QString &filterName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler12removeFilterERK7QString(
    QHelpCollectionHandler *self,
    const QString *filterName) {
  return self->removeFilter(*filterName);
}

//  FileInfo QHelpCollectionHandler::registeredDocumentation(const QString
//      &namespaceName) const
extern "C" Q_DECL_EXPORT
QHelpCollectionHandler::FileInfo *ritual_ZNK22QHelpCollectionHandler23registeredDocumentationERK7QString(
    const QHelpCollectionHandler *self,
    const QString *namespaceName) {
  return new QHelpCollectionHandler::FileInfo(
      self->registeredDocumentation(
          *namespaceName));
}

//  FileInfoList QHelpCollectionHandler::registeredDocumentations() const
extern "C" Q_DECL_EXPORT
QHelpCollectionHandler::FileInfoList *ritual_ZNK22QHelpCollectionHandler24registeredDocumentationsEv(
    const QHelpCollectionHandler *self) {
  return new QHelpCollectionHandler::FileInfoList(
      self->registeredDocumentations());
}

//  bool QHelpCollectionHandler::unregisterDocumentation(const QString
//      &namespaceName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler23unregisterDocumentationERK7QString(
    QHelpCollectionHandler *self,
    const QString *namespaceName) {
  return self->unregisterDocumentation(*namespaceName);
}

//  bool QHelpCollectionHandler::removeCustomValue(const QString &key)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler17removeCustomValueERK7QString(
    QHelpCollectionHandler *self,
    const QString *key) {
  return self->removeCustomValue(*key);
}

//  QVariant QHelpCollectionHandler::customValue(const QString &key, const
//      QVariant &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QHelpCollectionHandler11customValueERK7QStringRK8QVariant(
    const QHelpCollectionHandler *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->customValue(*key, *defaultValue));
}

//  bool QHelpCollectionHandler::setCustomValue(const QString &key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler14setCustomValueERK7QStringRK8QVariant(
    QHelpCollectionHandler *self,
    const QString *key,
    const QVariant *value) {
  return self->setCustomValue(*key, *value);
}

//  int QHelpCollectionHandler::registerNamespace(const QString &nspace,
//      const QString &fileName)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QHelpCollectionHandler17registerNamespaceERK7QStringS2_(
    QHelpCollectionHandler *self,
    const QString *nspace,
    const QString *fileName) {
  return self->registerNamespace(*nspace, *fileName);
}

//  int QHelpCollectionHandler::registerVirtualFolder(const QString
//      &folderName, int namespaceId)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QHelpCollectionHandler21registerVirtualFolderERK7QStringi(
    QHelpCollectionHandler *self,
    const QString *folderName,
    int namespaceId) {
  return self->registerVirtualFolder(*folderName, namespaceId);
}

//  int QHelpCollectionHandler::registerComponent(const QString
//      &componentName, int namespaceId)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QHelpCollectionHandler17registerComponentERK7QStringi(
    QHelpCollectionHandler *self,
    const QString *componentName,
    int namespaceId) {
  return self->registerComponent(*componentName, namespaceId);
}

//  bool QHelpCollectionHandler::registerVersion(const QString &version, int
//      namespaceId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler15registerVersionERK7QStringi(
    QHelpCollectionHandler *self,
    const QString *version,
    int namespaceId) {
  return self->registerVersion(*version, namespaceId);
}

//  void QHelpCollectionHandler::setReadOnly(bool readOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler11setReadOnlyEb(
    QHelpCollectionHandler *self,
    bool readOnly) {
  self->setReadOnly(readOnly);
}

//  QUrl QHelpCollectionHandler::buildQUrl(const QString &ns, const QString
//      &folder, const QString &relFileName, const QString &anchor)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN22QHelpCollectionHandler9buildQUrlERK7QStringS2_S2_S2_(
    const QString *ns,
    const QString *folder,
    const QString *relFileName,
    const QString *anchor) {
  return new QUrl(
      QHelpCollectionHandler::buildQUrl(
          *ns,
          *folder,
          *relFileName,
          *anchor));
}

//  void QHelpCollectionHandler::error(const QString &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler5errorERK7QString(
    QHelpCollectionHandler *self,
    const QString *msg) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHelpCollectionHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "error(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "error(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(msg)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QString QHelpCollectionHandler::namespaceVersion(const QString
//      &namespaceName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHelpCollectionHandler16namespaceVersionERK7QString(
    const QHelpCollectionHandler *self,
    const QString *namespaceName) {
  return new QString(self->namespaceVersion(*namespaceName));
}

//  bool QHelpCollectionHandler::isDBOpened() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QHelpCollectionHandler10isDBOpenedEv(
    const QHelpCollectionHandler *self) {
  return self->isDBOpened();
}

//  bool QHelpCollectionHandler::createTables(QSqlQuery *query)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler12createTablesEP9QSqlQuery(
    QHelpCollectionHandler *self,
    QSqlQuery *query) {
  return self->createTables(query);
}

//  void QHelpCollectionHandler::closeDB()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler7closeDBEv(
    QHelpCollectionHandler *self) {
  self->closeDB();
}

//  bool
//      QHelpCollectionHandler::recreateIndexAndNamespaceFilterTables(QSqlQue
//      ry *query)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler37recreateIndexAndNamespaceFilterTablesEP9QSqlQuery(
    QHelpCollectionHandler *self,
    QSqlQuery *query) {
  return self->recreateIndexAndNamespaceFilterTables(query);
}

//  void QHelpCollectionHandler::createVersionFilter(const QString &version)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler19createVersionFilterERK7QString(
    QHelpCollectionHandler *self,
    const QString *version) {
  self->createVersionFilter(*version);
}

//  bool QHelpCollectionHandler::registerFilterAttributes(const
//      QList<QStringList> &attributeSets, int nsId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler24registerFilterAttributesERK5QListIS0_I7QStringEEi(
    QHelpCollectionHandler *self,
    const QList<QStringList> *attributeSets,
    int nsId) {
  return self->registerFilterAttributes(*attributeSets, nsId);
}

//  bool QHelpCollectionHandler::registerFileAttributeSets(const
//      QList<QStringList> &attributeSets, int nsId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler25registerFileAttributeSetsERK5QListIS0_I7QStringEEi(
    QHelpCollectionHandler *self,
    const QList<QStringList> *attributeSets,
    int nsId) {
  return self->registerFileAttributeSets(*attributeSets, nsId);
}

//  bool QHelpCollectionHandler::unregisterIndexTable(int nsId, int vfId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHelpCollectionHandler20unregisterIndexTableEii(
    QHelpCollectionHandler *self,
    int nsId,
    int vfId) {
  return self->unregisterIndexTable(nsId, vfId);
}

//  QString QHelpCollectionHandler::absoluteDocPath(const QString &fileName)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHelpCollectionHandler15absoluteDocPathERK7QString(
    const QHelpCollectionHandler *self,
    const QString *fileName) {
  return new QString(self->absoluteDocPath(*fileName));
}

//  bool QHelpCollectionHandler::isTimeStampCorrect(const TimeStamp
//      &timeStamp) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QHelpCollectionHandler18isTimeStampCorrectERKNS_9TimeStampE(
    const QHelpCollectionHandler *self,
    const QHelpCollectionHandler::TimeStamp *timeStamp) {
  return self->isTimeStampCorrect(*timeStamp);
}

//  bool QHelpCollectionHandler::hasTimeStampInfo(const QString &nameSpace)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QHelpCollectionHandler16hasTimeStampInfoERK7QString(
    const QHelpCollectionHandler *self,
    const QString *nameSpace) {
  return self->hasTimeStampInfo(*nameSpace);
}

//  void QHelpCollectionHandler::scheduleVacuum()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler14scheduleVacuumEv(
    QHelpCollectionHandler *self) {
  self->scheduleVacuum();
}

//  void QHelpCollectionHandler::execVacuum()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler10execVacuumEv(
    QHelpCollectionHandler *self) {
  self->execVacuum();
}

//  a Python function taken by a CuteQHelpCollectionHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpCollectionHandler(
    QHelpCollectionHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpCollectionHandler *>(self)->take(key, call);
}

//  a QList<QHelpCollectionHandler::ContentsData> a ritual of
//      QHelpCollectionHandler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpCollectionHandler__QList_QHelpCollectionHandler_ContentsData(
    QList<QHelpCollectionHandler::ContentsData> *self) {
  delete self;
}

//  a QList<QStringList> a ritual of QHelpCollectionHandler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpCollectionHandler__QList_QStringList(
    QList<QStringList> *self) {
  delete self;
}

//  a QMap<QString, QString> a ritual of QHelpCollectionHandler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpCollectionHandler__QMap_QString_QString(
    QMap<QString, QString> *self) {
  delete self;
}

//  a QHelpCollectionHandler::FileInfoList a ritual of QHelpCollectionHandler
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpCollectionHandler__QHelpCollectionHandler_FileInfoList(
    QHelpCollectionHandler::FileInfoList *self) {
  delete self;
}

//  a QMultiMap<QString, QUrl> a ritual of QHelpCollectionHandler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpCollectionHandler__QMultiMap_QString_QUrl(
    QMultiMap<QString, QUrl> *self) {
  delete self;
}
