//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/6.12.0/QtHelp/private/qhelpdbreader_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QHelpDBReader' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 5 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHelp/QtHelp>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHelp/6.12.0/QtHelp/private/qhelpdbreader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <QtCore/QStringList>
#include <QtCore/QMultiMap>
#include <QtCore/QString>
#include <QtCore/QByteArray>
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

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 100, as local:qhelpdbreader.cpp:VersionData
struct VersionData
{
    QString tail;
    int major = -1;
    int minor = -1;
    int patch = -1;
};

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 108, as local:qhelpdbreader.cpp:getVersionData
static VersionData getVersionData(const QString &nameSpace)
{
    VersionData result;
    if (!nameSpace.startsWith("org.qt-project."_L1))
        return result;

    // We take the namespace tail, starting from the last letter in namespace name.
    // We drop any non digit characters.
    const QChar dot(u'.');
    QString &tail = result.tail;
    for (int i = nameSpace.size(); i > 0; --i) {
        const QChar c = nameSpace.at(i - 1);
        if (c.isDigit() || c == dot)
            tail.prepend(c);

        if (c.isLetter())
            break;
    }

    if (!tail.startsWith(dot) && tail.count(dot) == 1) {
        // The org.qt-project.qtquickcontrols2.5120 case,
        // tail = 2.5120 here. We need to cut "2." here.
        const int dotIndex = tail.indexOf(dot);
        if (dotIndex > 0)
            tail = tail.mid(dotIndex);
    }

    // Drop beginning dots
    while (tail.startsWith(dot))
        tail = tail.mid(1);

    // Drop ending dots
    while (tail.endsWith(dot))
        tail.chop(1);

    if (tail.size() >= 3 && tail.size() <= 5 && tail.count(dot) == 0) {
        // When we have 3 digits, we split it like: ABC -> A.B.C
        // When we have 4 digits, we split it like: ABCD -> A.BC.D
        // When we have 5 digits, we split it like: ABCDE -> A.BC.DE
        QStringView tail{result.tail};
        result.major = tail.left(1).toInt();
        result.minor = tail.size() == 3 ? tail.mid(1, 1).toInt() : tail.mid(1, 2).toInt();
        result.patch = tail.size() == 5 ? tail.right(2).toInt() : tail.right(1).toInt();
    }
    return result;
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

//  from QtHelp__QHelpDBReader.cpp, line 1, as moc:QHelpDBReader
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN13QHelpDBReaderE_t {};
} // unnamed namespace

template <> constexpr inline auto QHelpDBReader::qt_create_metaobjectdata<qt_meta_tag_ZN13QHelpDBReaderE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QHelpDBReader"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QHelpDBReader, qt_meta_tag_ZN13QHelpDBReaderE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QHelpDBReader::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13QHelpDBReaderE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13QHelpDBReaderE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN13QHelpDBReaderE_t>.metaTypes,
    nullptr
} };

void QHelpDBReader::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QHelpDBReader *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QHelpDBReader::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QHelpDBReader::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13QHelpDBReaderE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QHelpDBReader::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 155, as _ZNK13QHelpDBReader18qtVersionHeuristicEv
inline QString QHelpDBReader::qtVersionHeuristic() const
{
    VersionData version = getVersionData(namespaceName());
    return version.major >= 0
            ? QString::number(version.major) + u'.' + QString::number(version.minor) + u'.' + QString::number(version.patch)
            : version.tail;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 20, as _ZN13QHelpDBReaderC1ERK7QString
inline QHelpDBReader::QHelpDBReader(const QString &dbName)
    : m_dbName(dbName)
    , m_uniqueId(QHelpGlobal::uniquifyConnectionName("QHelpDBReader"_L1, this))
{}

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

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 92, as _ZNK13QHelpDBReader7versionEv
inline QString QHelpDBReader::version() const
{
    const QString versionString = metaData("version"_L1).toString();
    if (versionString.isEmpty())
        return qtVersionHeuristic();
    return versionString;
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

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 452, as _ZNK13QHelpDBReader9filesDataERK5QListI7QStringERKS1_
inline QMultiMap<QString, QByteArray> QHelpDBReader::filesData(const QStringList &filterAttributes,
                                                        const QString &extensionFilter) const
{
    if (!m_query)
        return {};

    QString query;
    QString extension;
    if (!extensionFilter.isEmpty())
        extension = "AND FileNameTable.Name LIKE \'%.%1\'"_L1.arg(extensionFilter);

    if (filterAttributes.isEmpty()) {
        query =
            "SELECT "
                "FileNameTable.Name, "
                "FileDataTable.Data "
            "FROM "
                "FolderTable, "
                "FileNameTable, "
                "FileDataTable "
            "WHERE FileDataTable.Id = FileNameTable.FileId "
            "AND FileNameTable.FolderId = FolderTable.Id %1"_L1.arg(extension);
    } else {
        for (int i = 0; i < filterAttributes.size(); ++i) {
            if (i > 0)
                query.append(" INTERSECT "_L1);
            query.append(
                "SELECT "
                    "FileNameTable.Name, "
                    "FileDataTable.Data "
                "FROM "
                    "FolderTable, "
                    "FileNameTable, "
                    "FileDataTable, "
                    "FileFilterTable, "
                    "FilterAttributeTable "
                "WHERE FileDataTable.Id = FileNameTable.FileId "
                "AND FileNameTable.FolderId = FolderTable.Id "
                "AND FileNameTable.FileId = FileFilterTable.FileId "
                "AND FileFilterTable.FilterAttributeId = FilterAttributeTable.Id "
                "AND FilterAttributeTable.Name = \'%1\' %2"_L1
                            .arg(quote(filterAttributes.at(i)), extension));
        }
    }
    m_query->exec(query);
    QMultiMap<QString, QByteArray> result;
    while (m_query->next())
        result.insert(m_query->value(0).toString(), qUncompress(m_query->value(1).toByteArray()));
    return result;
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 383, as _ZNK13QHelpDBReader8fileDataERK7QStringS2_
inline QByteArray QHelpDBReader::fileData(const QString &virtualFolder,
                                   const QString &filePath) const
{
    QByteArray ba;
    if (virtualFolder.isEmpty() || filePath.isEmpty() || !m_query)
        return ba;

    namespaceName();
    m_query->prepare(
        "SELECT "
            "FileDataTable.Data "
        "FROM "
            "FileDataTable, "
            "FileNameTable, "
            "FolderTable, "
            "NamespaceTable "
        "WHERE FileDataTable.Id = FileNameTable.FileId "
        "AND (FileNameTable.Name = ? OR FileNameTable.Name = ?) "
        "AND FileNameTable.FolderId = FolderTable.Id "
        "AND FolderTable.Name = ? "
        "AND FolderTable.NamespaceId = NamespaceTable.Id "
        "AND NamespaceTable.Name = ?"_L1);
    m_query->bindValue(0, filePath);
    m_query->bindValue(1, QString("./"_L1 + filePath));
    m_query->bindValue(2, virtualFolder);
    m_query->bindValue(3, m_namespace);
    m_query->exec();
    if (m_query->next() && m_query->isValid())
        ba = qUncompress(m_query->value(0).toByteArray());
    return ba;
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

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 503, as _ZNK13QHelpDBReader8metaDataERK7QString
inline QVariant QHelpDBReader::metaData(const QString &name) const
{
    if (!m_query)
        return {};

    m_query->prepare("SELECT COUNT(Value), Value FROM MetaDataTable WHERE Name=?"_L1);
    m_query->bindValue(0, name);
    if (m_query->exec() && m_query->next() && m_query->value(0).toInt() == 1)
        return m_query->value(1);
    return {};
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 163, as _ZN13QHelpDBReader16versionHeuristicERK7QString
inline QVersionNumber QHelpDBReader::versionHeuristic(const QString &namespaceName)
{
    VersionData version = getVersionData(namespaceName);
    return version.major >= 0 ? QVersionNumber{version.major, version.minor, version.patch}
                              : QVersionNumber::fromString(version.tail);
}

//  from ../qttools/src/assistant/help/qhelpdbreader.cpp, line 515, as _ZNK13QHelpDBReader5quoteERK7QString
inline QString QHelpDBReader::quote(const QString &string) const
{
    QString s = string;
    s.replace(u'\'', "\'\'"_L1);
    return s;
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
//  -----------------------------------------------------------------------

//  A QHelpDBReader that Python can take functions over in. Every QHelpDBReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpDBReaderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpDBReaderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpDBReaderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpDBReaderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpDBReaderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpDBReaderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpDBReaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpDBReader : public QHelpDBReader {
public:
  using QHelpDBReader::QHelpDBReader;
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
      CuteQHelpDBReaderCall0 call = reinterpret_cast<CuteQHelpDBReaderCall0>(taken[0]);
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
      CuteQHelpDBReaderCall1 call = reinterpret_cast<CuteQHelpDBReaderCall1>(taken[1]);
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
      CuteQHelpDBReaderCall2 call = reinterpret_cast<CuteQHelpDBReaderCall2>(taken[2]);
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
      CuteQHelpDBReaderCall3 call = reinterpret_cast<CuteQHelpDBReaderCall3>(taken[3]);
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
      CuteQHelpDBReaderCall4 call = reinterpret_cast<CuteQHelpDBReaderCall4>(taken[4]);
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
      CuteQHelpDBReaderCall5 call = reinterpret_cast<CuteQHelpDBReaderCall5>(taken[5]);
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
      CuteQHelpDBReaderCall6 call = reinterpret_cast<CuteQHelpDBReaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpDBReader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QHelpDBReader10metaObjectEv(
    const QHelpDBReader *self) {
  return self->metaObject();
}

//  void *QHelpDBReader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QHelpDBReader11qt_metacastEPKc(
    QHelpDBReader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHelpDBReader::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QHelpDBReader11qt_metacallEN11QMetaObject4CallEiPPv(
    QHelpDBReader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHelpDBReader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QHelpDBReader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpDBReader::tr(s, c, n));
}

//  QHelpDBReader::QHelpDBReader(const QString &dbName)
extern "C" Q_DECL_EXPORT
QHelpDBReader *ritual_ZN13QHelpDBReaderC1ERK7QString(const QString *dbName) {
  return new CuteQHelpDBReader(*dbName);
}

//  QHelpDBReader::QHelpDBReader(const QString &dbName, const QString
//      &uniqueId, QObject *parent)
extern "C" Q_DECL_EXPORT
QHelpDBReader *ritual_ZN13QHelpDBReaderC1ERK7QStringS2_P7QObject(
    const QString *dbName,
    const QString *uniqueId,
    QObject *parent) {
  return new CuteQHelpDBReader(*dbName, *uniqueId, parent);
}

//  QHelpDBReader::~QHelpDBReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHelpDBReaderD1Ev(QHelpDBReader *self) {
  delete self;
}

//  bool QHelpDBReader::init()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QHelpDBReader4initEv(QHelpDBReader *self) {
  return self->init();
}

//  QString QHelpDBReader::namespaceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QHelpDBReader13namespaceNameEv(
    const QHelpDBReader *self) {
  return new QString(self->namespaceName());
}

//  QString QHelpDBReader::virtualFolder() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QHelpDBReader13virtualFolderEv(
    const QHelpDBReader *self) {
  return new QString(self->virtualFolder());
}

//  QString QHelpDBReader::version() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QHelpDBReader7versionEv(const QHelpDBReader *self) {
  return new QString(self->version());
}

//  QList<QStringList> QHelpDBReader::filterAttributeSets() const
extern "C" Q_DECL_EXPORT
QList<QStringList> *ritual_ZNK13QHelpDBReader19filterAttributeSetsEv(
    const QHelpDBReader *self) {
  return new QList<QStringList>(self->filterAttributeSets());
}

//  QMultiMap<QString, QByteArray> QHelpDBReader::filesData(const QStringList
//      &filterAttributes, const QString &extensionFilter) const
extern "C" Q_DECL_EXPORT
QMultiMap<QString, QByteArray> *ritual_ZNK13QHelpDBReader9filesDataERK5QListI7QStringERKS1_(
    const QHelpDBReader *self,
    const QList<QString> *filterAttributes,
    const QString *extensionFilter) {
  return new QMultiMap<QString, QByteArray>(
      self->filesData(
          *filterAttributes,
          *extensionFilter));
}

//  QByteArray QHelpDBReader::fileData(const QString &virtualFolder, const
//      QString &filePath) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QHelpDBReader8fileDataERK7QStringS2_(
    const QHelpDBReader *self,
    const QString *virtualFolder,
    const QString *filePath) {
  return new QByteArray(self->fileData(*virtualFolder, *filePath));
}

//  QStringList QHelpDBReader::customFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QHelpDBReader13customFiltersEv(
    const QHelpDBReader *self) {
  return new QList<QString>(self->customFilters());
}

//  QStringList QHelpDBReader::filterAttributes(const QString &filterName)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QHelpDBReader16filterAttributesERK7QString(
    const QHelpDBReader *self,
    const QString *filterName) {
  return new QList<QString>(self->filterAttributes(*filterName));
}

//  QVariant QHelpDBReader::metaData(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QHelpDBReader8metaDataERK7QString(
    const QHelpDBReader *self,
    const QString *name) {
  return new QVariant(self->metaData(*name));
}

//  QVersionNumber QHelpDBReader::versionHeuristic(const QString
//      &namespaceName)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN13QHelpDBReader16versionHeuristicERK7QString(
    const QString *namespaceName) {
  return new QVersionNumber(QHelpDBReader::versionHeuristic(*namespaceName));
}

//  QString QHelpDBReader::quote(const QString &string) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QHelpDBReader5quoteERK7QString(
    const QHelpDBReader *self,
    const QString *string) {
  return new QString(self->quote(*string));
}

//  bool QHelpDBReader::initDB()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QHelpDBReader6initDBEv(QHelpDBReader *self) {
  return self->initDB();
}

//  a Python function taken by a CuteQHelpDBReader, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpDBReader(
    QHelpDBReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpDBReader *>(self)->take(key, call);
}

//  a QList<QStringList> a ritual of QHelpDBReader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpDBReader__QList_QStringList(QList<QStringList> *self) {
  delete self;
}

//  a QMultiMap<QString, QByteArray> a ritual of QHelpDBReader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpDBReader__QMultiMap_QString_QByteArray(
    QMultiMap<QString, QByteArray> *self) {
  delete self;
}
