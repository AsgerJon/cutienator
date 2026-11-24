//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqlquerymodel_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSql/qtsqlglobal.h>
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#if QT_CONFIG(sqlmodel)
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/qsqlquerymodel.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqlquerymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsqlquerymodel.h"
#include "qsqlquerymodel_p.h"
#include <qdebug.h>
#include <qsqldriver.h>
#include <qsqlfield.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/sql/models/qsqlquerymodel.cpp, line 53, as _ZN21QSqlQueryModelPrivateD1Ev
inline QSqlQueryModelPrivate::~QSqlQueryModelPrivate()
{
}

//  from src/sql/models/qsqlquerymodel.cpp, line 18, as _ZN21QSqlQueryModelPrivate8prefetchEi
inline void QSqlQueryModelPrivate::prefetch(int limit)
{
    Q_Q(QSqlQueryModel);

    if (atEnd || limit <= bottom.row() || bottom.column() == -1)
        return;

    QModelIndex newBottom;
    const int oldBottomRow = qMax(bottom.row(), 0);

    // try to seek directly
    if (query.seek(limit)) {
        newBottom = q->createIndex(limit, bottom.column());
    } else {
        // have to seek back to our old position for MS Access
        int i = oldBottomRow;
        if (query.seek(i)) {
            while (query.next())
                ++i;
            newBottom = q->createIndex(i, bottom.column());
        } else {
            // empty or invalid query
            newBottom = q->createIndex(-1, bottom.column());
        }
        atEnd = true; // this is the end.
    }
    if (newBottom.row() >= 0 && newBottom.row() > bottom.row()) {
        q->beginInsertRows(QModelIndex(), bottom.row() + 1, newBottom.row());
        bottom = newBottom;
        q->endInsertRows();
    } else {
        bottom = newBottom;
    }
}

//  from src/sql/models/qsqlquerymodel.cpp, line 57, as _ZN21QSqlQueryModelPrivate14initColOffsetsEi
inline void QSqlQueryModelPrivate::initColOffsets(int size)
{
    colOffsets.resize(size);
    memset(colOffsets.data(), 0, colOffsets.size() * sizeof(int));
}

//  from src/sql/models/qsqlquerymodel.cpp, line 63, as _ZNK21QSqlQueryModelPrivate13columnInQueryEi
inline int QSqlQueryModelPrivate::columnInQuery(int modelColumn) const
{
    if (modelColumn < 0 || modelColumn >= rec.count() || !rec.isGenerated(modelColumn) || modelColumn >= colOffsets.size())
        return -1;
    return modelColumn - colOffsets[modelColumn];
}
//  -----------------------------------------------------------------------

//  A QSqlQueryModelPrivate that Python can take functions over in. Every QSqlQueryModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlQueryModelPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
class CuteQSqlQueryModelPrivate : public QSqlQueryModelPrivate {
public:
  using QSqlQueryModelPrivate::QSqlQueryModelPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    return false;
  }

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModelPrivate::executePendingOperations() const
  void executePendingOperations() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlQueryModelPrivateCall0 call = reinterpret_cast<CuteQSqlQueryModelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)
};

//  QSqlQueryModel *QSqlQueryModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSqlQueryModel *ritual_ZN21QSqlQueryModelPrivate6q_funcEv(
    QSqlQueryModelPrivate *self) {
  return self->q_func();
}

//  const QSqlQueryModel *QSqlQueryModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSqlQueryModel *ritual_ZNK21QSqlQueryModelPrivate6q_funcEv(
    const QSqlQueryModelPrivate *self) {
  return self->q_func();
}

//  QSqlQueryModelPrivate::QSqlQueryModelPrivate()
extern "C" Q_DECL_EXPORT
QSqlQueryModelPrivate *ritual_ZN21QSqlQueryModelPrivateC1Ev() {
  return new CuteQSqlQueryModelPrivate();
}

//  QSqlQueryModelPrivate::~QSqlQueryModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlQueryModelPrivateD1Ev(QSqlQueryModelPrivate *self) {
  delete self;
}

//  void QSqlQueryModelPrivate::prefetch(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlQueryModelPrivate8prefetchEi(
    QSqlQueryModelPrivate *self,
    int a0) {
  self->prefetch(a0);
}

//  void QSqlQueryModelPrivate::initColOffsets(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlQueryModelPrivate14initColOffsetsEi(
    QSqlQueryModelPrivate *self,
    int size) {
  self->initColOffsets(size);
}

//  int QSqlQueryModelPrivate::columnInQuery(int modelColumn) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSqlQueryModelPrivate13columnInQueryEi(
    const QSqlQueryModelPrivate *self,
    int modelColumn) {
  return self->columnInQuery(modelColumn);
}

//  a Python function taken by a CuteQSqlQueryModelPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlQueryModelPrivate(
    QSqlQueryModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlQueryModelPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(sqlmodel)
