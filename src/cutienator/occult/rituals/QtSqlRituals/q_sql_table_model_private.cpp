//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqltablemodel_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtSql/qtsqlglobal.h>
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#if QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/qsqltablemodel.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqltablemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtSql/qsqlrecord.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/qsqlquerymodel.h>
#include <QtSql/private/qsqlquerymodel_p.h>
#include <QtCore/qdebug.h>
#include <QtSql/qsqldriver.h>
#include <QtSql/qsqlfield.h>
#include <QtSql/qsqltablemodel.h>
#include <QtSql/qsqldriver.h>
#include <QtSql/qsqlerror.h>
#include <QtSql/qsqlfield.h>
#include <QtSql/qsqlindex.h>
#include <QtSql/qsqlquery.h>
#include <QtSql/qsqlrecord.h>
#include <QtSql/qsqlresult.h>
#include <QtSql/private/qsqltablemodel_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/sql/models/qsqlquerymodel.cpp, line 53, as _ZN21QSqlQueryModelPrivateD2Ev
inline QSqlQueryModelPrivate::~QSqlQueryModelPrivate()
{
}

//  from src/sql/models/qsqltablemodel.cpp, line 80, as _ZN21QSqlTableModelPrivate10clearCacheEv
inline void QSqlTableModelPrivate::clearCache()
{
    cache.clear();
}

//  from src/sql/models/qsqltablemodel.cpp, line 85, as _ZN21QSqlTableModelPrivate15revertCachedRowEi
inline void QSqlTableModelPrivate::revertCachedRow(int row)
{
    Q_Q(QSqlTableModel);
    ModifiedRow r = cache.value(row);

    switch (r.op()) {
    case QSqlTableModelPrivate::None:
        Q_ASSERT_X(false, "QSqlTableModelPrivate::revertCachedRow()", "Invalid entry in cache map");
        return;
    case QSqlTableModelPrivate::Update:
    case QSqlTableModelPrivate::Delete:
        if (!r.submitted()) {
            cache[row].revert();
            emit q->dataChanged(q->createIndex(row, 0),
                                q->createIndex(row, q->columnCount() - 1));
        }
        break;
    case QSqlTableModelPrivate::Insert: {
            QMap<int, QSqlTableModelPrivate::ModifiedRow>::Iterator it = cache.find(row);
            if (it == cache.end())
                return;
            q->beginRemoveRows(QModelIndex(), row, row);
            it = cache.erase(it);
            while (it != cache.end()) {
                int oldKey = it.key();
                const QSqlTableModelPrivate::ModifiedRow oldValue = it.value();
                cache.erase(it);
                it = cache.insert(oldKey - 1, oldValue);
                ++it;
            }
            q->endRemoveRows();
        break; }
    }
}

//  from src/sql/models/qsqltablemodel.cpp, line 36, as _ZNK21QSqlTableModelPrivate11nameToIndexERK7QString
inline int QSqlTableModelPrivate::nameToIndex(const QString &name) const
{
    return rec.indexOf(strippedFieldName(name));
}

//  from src/sql/models/qsqlquerymodel.cpp, line 57, as _ZN21QSqlQueryModelPrivate14initColOffsetsEi
inline void QSqlQueryModelPrivate::initColOffsets(int size)
{
    colOffsets.resize(size);
    memset(colOffsets.data(), 0, colOffsets.size() * sizeof(int));
}

//  from src/sql/models/qsqltablemodel.cpp, line 68, as _ZN21QSqlTableModelPrivate5clearEv
inline void QSqlTableModelPrivate::clear()
{
    sortColumn = -1;
    sortOrder = Qt::AscendingOrder;
    tableName.clear();
    editQuery.clear();
    cache.clear();
    primaryIndex.clear();
    rec.clear();
    filter.clear();
}

//  from src/sql/models/qsqltablemodel.cpp, line 28, as _ZNK21QSqlTableModelPrivate6recordERK5QListI8QVariantE
inline QSqlRecord QSqlTableModelPrivate::record(const QList<QVariant> &values) const
{
    QSqlRecord r = rec;
    for (int i = 0; i < r.count() && i < values.size(); ++i)
        r.setValue(i, values.at(i));
    return r;
}

//  from src/sql/models/qsqltablemodel.cpp, line 120, as _ZN21QSqlTableModelPrivate4execERK7QStringbRK10QSqlRecordS5_
inline bool QSqlTableModelPrivate::exec(const QString &stmt, bool prepStatement,
                                 const QSqlRecord &rec, const QSqlRecord &whereValues)
{
    if (stmt.isEmpty())
        return false;

    // lazy initialization of editQuery
    if (editQuery.driver() != db.driver())
        editQuery = QSqlQuery(db);

    // workaround for In-Process databases - remove all read locks
    // from the table to make sure the editQuery succeeds
    if (db.driver()->hasFeature(QSqlDriver::SimpleLocking))
        const_cast<QSqlResult *>(query.result())->detachFromResultSet();

    if (prepStatement) {
        if (editQuery.lastQuery() != stmt) {
            if (!editQuery.prepare(stmt)) {
                error = editQuery.lastError();
                return false;
            }
        }
        for (int i = 0; i < rec.count(); ++i)
            if (rec.isGenerated(i))
                editQuery.addBindValue(rec.value(i));
        for (int i = 0; i < whereValues.count(); ++i)
            if (whereValues.isGenerated(i) && !whereValues.isNull(i))
                editQuery.addBindValue(whereValues.value(i));

        if (!editQuery.exec()) {
            error = editQuery.lastError();
            return false;
        }
    } else {
        if (!editQuery.exec(stmt)) {
            error = editQuery.lastError();
            return false;
        }
    }
    return true;
}

//  from src/sql/models/qsqltablemodel.cpp, line 41, as _ZNK21QSqlTableModelPrivate17strippedFieldNameERK7QString
inline QString QSqlTableModelPrivate::strippedFieldName(const QString &name) const
{
    QString fieldname = name;
    if (db.driver()->isIdentifierEscaped(fieldname, QSqlDriver::FieldName))
        fieldname = db.driver()->stripDelimiters(fieldname, QSqlDriver::FieldName);
    return fieldname;
}

//  from src/sql/models/qsqltablemodel.cpp, line 49, as _ZNK21QSqlTableModelPrivate11insertCountEi
inline int QSqlTableModelPrivate::insertCount(int maxRow) const
{
    int cnt = 0;
    CacheMap::ConstIterator i = cache.constBegin();
    const CacheMap::ConstIterator e = cache.constEnd();
    for ( ; i != e && (maxRow < 0 || i.key() <= maxRow); ++i)
        if (i.value().insert())
            ++cnt;

    return cnt;
}

//  from src/sql/models/qsqltablemodel.cpp, line 61, as _ZN21QSqlTableModelPrivate25initRecordAndPrimaryIndexEv
inline void QSqlTableModelPrivate::initRecordAndPrimaryIndex()
{
    rec = db.record(tableName);
    primaryIndex = db.primaryIndex(tableName);
    initColOffsets(rec.count());
}
//  -----------------------------------------------------------------------

//  A QSqlTableModelPrivate that Python can take functions over in. Every QSqlTableModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelPrivateCall1)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlTableModelPrivateCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlTableModelPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
class CuteQSqlTableModelPrivate : public QSqlTableModelPrivate {
public:
  using QSqlTableModelPrivate::QSqlTableModelPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN21QSqlTableModelPrivate10clearCacheEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN21QSqlTableModelPrivate15revertCachedRowEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK21QSqlTableModelPrivate11nameToIndexERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    return false;
  }

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModelPrivate::clearCache()
  void clearCache() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlTableModelPrivateCall0 call = reinterpret_cast<CuteQSqlTableModelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlTableModelPrivate::clearCache();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModelPrivate::revertCachedRow(int row)
  void revertCachedRow(int row) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlTableModelPrivateCall1 call = reinterpret_cast<CuteQSqlTableModelPrivateCall1>(taken[1]);
      call(this, row, &handled);
      if (handled) return;
    }
    QSqlTableModelPrivate::revertCachedRow(row);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  int QSqlTableModelPrivate::nameToIndex(const QString &name) const
  int nameToIndex(const QString &name) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlTableModelPrivateCall2 call = reinterpret_cast<CuteQSqlTableModelPrivateCall2>(taken[2]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QSqlTableModelPrivate::nameToIndex(name);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModelPrivate::executePendingOperations() const
  void executePendingOperations() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlTableModelPrivateCall3 call = reinterpret_cast<CuteQSqlTableModelPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)
};

//  QSqlTableModel *QSqlTableModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSqlTableModel *ritual_ZN21QSqlTableModelPrivate6q_funcEv(
    QSqlTableModelPrivate *self) {
  return self->q_func();
}

//  const QSqlTableModel *QSqlTableModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSqlTableModel *ritual_ZNK21QSqlTableModelPrivate6q_funcEv(
    const QSqlTableModelPrivate *self) {
  return self->q_func();
}

//  QSqlTableModelPrivate::QSqlTableModelPrivate()
extern "C" Q_DECL_EXPORT
QSqlTableModelPrivate *ritual_ZN21QSqlTableModelPrivateC1Ev() {
  return new CuteQSqlTableModelPrivate();
}

//  void QSqlTableModelPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate5clearEv(QSqlTableModelPrivate *self) {
  self->clear();
}

//  void QSqlTableModelPrivate::clearCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate10clearCacheEv(
    QSqlTableModelPrivate *self) {
  self->clearCache();
}

//  QSqlRecord QSqlTableModelPrivate::record(const QList<QVariant> &values)
//      const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK21QSqlTableModelPrivate6recordERK5QListI8QVariantE(
    const QSqlTableModelPrivate *self,
    const QList<QVariant> *values) {
  return new QSqlRecord(self->record(*values));
}

//  bool QSqlTableModelPrivate::exec(const QString &stmt, bool prepStatement,
//      const QSqlRecord &rec, const QSqlRecord &whereValues)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSqlTableModelPrivate4execERK7QStringbRK10QSqlRecordS5_(
    QSqlTableModelPrivate *self,
    const QString *stmt,
    bool prepStatement,
    const QSqlRecord *rec,
    const QSqlRecord *whereValues) {
  return self->exec(*stmt, prepStatement, *rec, *whereValues);
}

//  void QSqlTableModelPrivate::revertCachedRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate15revertCachedRowEi(
    QSqlTableModelPrivate *self,
    int row) {
  self->revertCachedRow(row);
}

//  int QSqlTableModelPrivate::nameToIndex(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSqlTableModelPrivate11nameToIndexERK7QString(
    const QSqlTableModelPrivate *self,
    const QString *name) {
  return self->nameToIndex(*name);
}

//  QString QSqlTableModelPrivate::strippedFieldName(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QSqlTableModelPrivate17strippedFieldNameERK7QString(
    const QSqlTableModelPrivate *self,
    const QString *name) {
  return new QString(self->strippedFieldName(*name));
}

//  int QSqlTableModelPrivate::insertCount(int maxRow) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSqlTableModelPrivate11insertCountEi(
    const QSqlTableModelPrivate *self,
    int maxRow) {
  return self->insertCount(maxRow);
}

//  void QSqlTableModelPrivate::initRecordAndPrimaryIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate25initRecordAndPrimaryIndexEv(
    QSqlTableModelPrivate *self) {
  self->initRecordAndPrimaryIndex();
}

//  a Python function taken by a CuteQSqlTableModelPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlTableModelPrivate(
    QSqlTableModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlTableModelPrivate *>(self)->take(key, call);
}

//  void QSqlTableModelPrivate::clearCache()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSqlTableModelPrivate10clearCacheEv(
    QSqlTableModelPrivate *self) {
  self->QSqlTableModelPrivate::clearCache();
}

//  void QSqlTableModelPrivate::revertCachedRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSqlTableModelPrivate15revertCachedRowEi(
    QSqlTableModelPrivate *self,
    int row) {
  self->QSqlTableModelPrivate::revertCachedRow(row);
}

//  int QSqlTableModelPrivate::nameToIndex(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QSqlTableModelPrivate11nameToIndexERK7QString(
    const QSqlTableModelPrivate *self,
    const QString *name) {
  return self->QSqlTableModelPrivate::nameToIndex(*name);
}

#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(sqlmodel)
