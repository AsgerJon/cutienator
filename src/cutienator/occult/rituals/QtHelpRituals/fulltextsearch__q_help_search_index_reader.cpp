//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/6.12.0/QtHelp/private/qhelpsearchindexreader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHelp/QtHelp>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHelp/6.12.0/QtHelp/private/qhelpsearchindexreader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtHelp/qhelpsearchresult.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHelp/private/qhelpsearchindexreader_p.h>
#include <QtHelp/qhelpenginecore.h>
#include <QtHelp/qhelpfilterengine.h>
#include <QtCore/qmap.h>
#include <QtCore/qset.h>
#include <QtSql/qsqldatabase.h>
#include <QtSql/qsqlquery.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/assistant/help/qhelpsearchindexreader.cpp, line 20, as local:qhelpsearchindexreader.cpp:Reader
namespace fulltextsearch {
using namespace Qt::StringLiterals;
class Reader
{
public:
    void setIndexPath(const QString &path)
    {
        m_indexPath = path;
        m_namespaceAttributes.clear();
        m_filterEngineNamespaceList.clear();
        m_useFilterEngine = false;
    }
    void addNamespaceAttributes(const QString &namespaceName, const QStringList &attributes)
    {
        m_namespaceAttributes.insert(namespaceName, attributes);
    }
    void setFilterEngineNamespaceList(const QStringList &namespaceList)
    {
        m_useFilterEngine = true;
        m_filterEngineNamespaceList = namespaceList;
    }

    void searchInDB(const QString &term);
    QList<QHelpSearchResult> searchResults() const { return m_searchResults; }

private:
    QList<QHelpSearchResult> queryTable(const QSqlDatabase &db, const QString &tableName,
                                        const QString &searchInput) const;

    QMultiMap<QString, QStringList> m_namespaceAttributes;
    QStringList m_filterEngineNamespaceList;
    QList<QHelpSearchResult> m_searchResults;
    QString m_indexPath;
    bool m_useFilterEngine = false;
};
}  // namespace fulltextsearch

//  from ../qttools/src/assistant/help/qhelpsearchindexreader.cpp, line 54, as local:qhelpsearchindexreader.cpp:namespacePlaceholders
namespace fulltextsearch {
using namespace Qt::StringLiterals;
static QString namespacePlaceholders(const QMultiMap<QString, QStringList> &namespaces)
{
    QString placeholders;
    const auto &namespaceList = namespaces.uniqueKeys();
    bool firstNS = true;
    for (const QString &ns : namespaceList) {
        if (firstNS)
            firstNS = false;
        else
            placeholders += " OR "_L1;
        placeholders += "(namespace = ?"_L1;

        const QList<QStringList> &attributeSets = namespaces.values(ns);
        bool firstAS = true;
        for (const QStringList &attributeSet : attributeSets) {
            if (!attributeSet.isEmpty()) {
                if (firstAS) {
                    firstAS = false;
                    placeholders += " AND ("_L1;
                } else {
                    placeholders += " OR "_L1;
                }
                placeholders += "attributes = ?"_L1;
            }
        }
        if (!firstAS)
            placeholders += u')'; // close "AND ("
        placeholders += u')';
    }
    return placeholders;
}
}  // namespace fulltextsearch

//  from ../qttools/src/assistant/help/qhelpsearchindexreader.cpp, line 150, as local:qhelpsearchindexreader.cpp:Reader::searchInDB
namespace fulltextsearch {
using namespace Qt::StringLiterals;
inline void Reader::searchInDB(const QString &searchInput)
{
    const QString &uniqueId = QHelpGlobal::uniquifyConnectionName("QHelpReader"_L1, this);
    {
        QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE"_L1, uniqueId);
        db.setConnectOptions("QSQLITE_OPEN_READONLY"_L1);
        db.setDatabaseName(m_indexPath + "/fts"_L1);

        if (db.open()) {
            const QList<QHelpSearchResult> titleResults = queryTable(db, "titles"_L1, searchInput);
            const QList<QHelpSearchResult> contentResults =
                    queryTable(db, "contents"_L1, searchInput);

            // merge results form title and contents searches
            m_searchResults.clear();
            QSet<QUrl> urls;
            for (const QHelpSearchResult &result : titleResults) {
                const auto size = urls.size();
                urls.insert(result.url());
                if (size != urls.size()) // insertion took place
                    m_searchResults.append(result);
            }
            for (const QHelpSearchResult &result : contentResults) {
                const auto size = urls.size();
                urls.insert(result.url());
                if (size != urls.size()) // insertion took place
                    m_searchResults.append(result);
            }
        }
    }
    QSqlDatabase::removeDatabase(uniqueId);
}
}  // namespace fulltextsearch

//  from ../qttools/src/assistant/help/qhelpsearchindexreader.cpp, line 198, as _ZN14fulltextsearch22QHelpSearchIndexReader15cancelSearchingEv
namespace fulltextsearch {
using namespace Qt::StringLiterals;
inline void QHelpSearchIndexReader::cancelSearching()
{
    QMutexLocker lock(&m_mutex);
    m_cancel = true;
}
}  // namespace fulltextsearch

//  from ../qttools/src/assistant/help/qhelpsearchindexreader.cpp, line 204, as _ZN14fulltextsearch22QHelpSearchIndexReader6searchERK7QStringS3_S3_b
namespace fulltextsearch {
using namespace Qt::StringLiterals;
inline void QHelpSearchIndexReader::search(const QString &collectionFile, const QString &indexFilesFolder,
                                    const QString &searchInput, bool usesFilterEngine)
{
    wait();

    m_searchResults.clear();
    m_cancel = false;
    m_searchInput = searchInput;
    m_collectionFile = collectionFile;
    m_indexFilesFolder = indexFilesFolder;
    m_usesFilterEngine = usesFilterEngine;

    start(QThread::NormalPriority);
}
}  // namespace fulltextsearch

//  from ../qttools/src/assistant/help/qhelpsearchindexreader.cpp, line 219, as _ZNK14fulltextsearch22QHelpSearchIndexReader17searchResultCountEv
namespace fulltextsearch {
using namespace Qt::StringLiterals;
inline int QHelpSearchIndexReader::searchResultCount() const
{
    QMutexLocker lock(&m_mutex);
    return m_searchResults.size();
}
}  // namespace fulltextsearch

//  from ../qttools/src/assistant/help/qhelpsearchindexreader.cpp, line 225, as _ZNK14fulltextsearch22QHelpSearchIndexReader13searchResultsEii
namespace fulltextsearch {
using namespace Qt::StringLiterals;
inline QList<QHelpSearchResult> QHelpSearchIndexReader::searchResults(int start, int end) const
{
    QMutexLocker lock(&m_mutex);
    return m_searchResults.mid(start, end - start);
}
}  // namespace fulltextsearch
//  -----------------------------------------------------------------------

//  A fulltextsearch::QHelpSearchIndexReader that Python can take functions over in. Every fulltextsearch::QHelpSearchIndexReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cutefulltextsearch_QHelpSearchIndexReaderCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cutefulltextsearch_QHelpSearchIndexReaderCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cutefulltextsearch_QHelpSearchIndexReader : public fulltextsearch::QHelpSearchIndexReader {
public:
  using fulltextsearch::QHelpSearchIndexReader::QHelpSearchIndexReader;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void fulltextsearch::QHelpSearchIndexReader::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall0 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    fulltextsearch::QHelpSearchIndexReader::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall1 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall2 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall3 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall4 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall5 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall6 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall7 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *fulltextsearch::QHelpSearchIndexReader::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14fulltextsearch22QHelpSearchIndexReader10metaObjectEv(
    const fulltextsearch::QHelpSearchIndexReader *self) {
  return self->metaObject();
}

//  void *fulltextsearch::QHelpSearchIndexReader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14fulltextsearch22QHelpSearchIndexReader11qt_metacastEPKc(
    fulltextsearch::QHelpSearchIndexReader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int fulltextsearch::QHelpSearchIndexReader::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14fulltextsearch22QHelpSearchIndexReader11qt_metacallEN11QMetaObject4CallEiPPv(
    fulltextsearch::QHelpSearchIndexReader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  fulltextsearch::QHelpSearchIndexReader::~QHelpSearchIndexReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14fulltextsearch22QHelpSearchIndexReaderD1Ev(
    fulltextsearch::QHelpSearchIndexReader *self) {
  delete self;
}

//  void fulltextsearch::QHelpSearchIndexReader::cancelSearching()
extern "C" Q_DECL_EXPORT
void ritual_ZN14fulltextsearch22QHelpSearchIndexReader15cancelSearchingEv(
    fulltextsearch::QHelpSearchIndexReader *self) {
  self->cancelSearching();
}

//  void fulltextsearch::QHelpSearchIndexReader::search(const QString
//      &collectionFile, const QString &indexFilesFolder, const QString
//      &searchInput, bool usesFilterEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN14fulltextsearch22QHelpSearchIndexReader6searchERK7QStringS3_S3_b(
    fulltextsearch::QHelpSearchIndexReader *self,
    const QString *collectionFile,
    const QString *indexFilesFolder,
    const QString *searchInput,
    bool usesFilterEngine) {
  self->search(
      *collectionFile,
      *indexFilesFolder,
      *searchInput,
      usesFilterEngine);
}

//  int fulltextsearch::QHelpSearchIndexReader::searchResultCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14fulltextsearch22QHelpSearchIndexReader17searchResultCountEv(
    const fulltextsearch::QHelpSearchIndexReader *self) {
  return self->searchResultCount();
}

//  QList<QHelpSearchResult>
//      fulltextsearch::QHelpSearchIndexReader::searchResults(int start, int
//      end) const
extern "C" Q_DECL_EXPORT
QList<QHelpSearchResult> *ritual_ZNK14fulltextsearch22QHelpSearchIndexReader13searchResultsEii(
    const fulltextsearch::QHelpSearchIndexReader *self,
    int start,
    int end) {
  return new QList<QHelpSearchResult>(self->searchResults(start, end));
}

//  void fulltextsearch::QHelpSearchIndexReader::searchingStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN14fulltextsearch22QHelpSearchIndexReader16searchingStartedEv(
    fulltextsearch::QHelpSearchIndexReader *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "fulltextsearch::QHelpSearchIndexReader")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "searchingStarted()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "searchingStarted()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void fulltextsearch::QHelpSearchIndexReader::searchingFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN14fulltextsearch22QHelpSearchIndexReader17searchingFinishedEv(
    fulltextsearch::QHelpSearchIndexReader *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "fulltextsearch::QHelpSearchIndexReader")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "searchingFinished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "searchingFinished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void fulltextsearch::QHelpSearchIndexReader::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN14fulltextsearch22QHelpSearchIndexReader3runEv(
    fulltextsearch::QHelpSearchIndexReader *self) {
  self->run();
}

//  a Python function taken by a Cutefulltextsearch_QHelpSearchIndexReader,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_fulltextsearch_QHelpSearchIndexReader(
    fulltextsearch::QHelpSearchIndexReader *self,
    const char *key,
    void *call) {
  return static_cast<Cutefulltextsearch_QHelpSearchIndexReader *>(self)->take(key, call);
}
