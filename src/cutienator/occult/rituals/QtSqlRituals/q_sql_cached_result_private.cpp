//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqlcachedresult_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqlcachedresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/private/qsqlcachedresult_p.h>
#include <QtCore/qvariant.h>
#include <QtSql/private/qsqldriver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/sql/kernel/qsqlcachedresult.cpp, line 74, as _ZNK23QSqlCachedResultPrivate10cacheCountEv
inline int QSqlCachedResultPrivate::cacheCount() const
{
    Q_ASSERT(!forwardOnly);
    Q_ASSERT(colCount);
    return rowCacheEnd / colCount;
}
//  -----------------------------------------------------------------------

//  A QSqlCachedResultPrivate that Python can take functions over in. Every QSqlCachedResultPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQSqlCachedResultPrivateCall0)(const void *, qsizetype, int *);
class CuteQSqlCachedResultPrivate : public QSqlCachedResultPrivate {
public:
  using QSqlCachedResultPrivate::QSqlCachedResultPrivate;
  CuteQSqlCachedResultPrivate(const QSqlCachedResultPrivate &other) : QSqlCachedResultPrivate(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QSqlResultPrivate11fieldSerialEx")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QString QSqlResultPrivate::fieldSerial(qsizetype a0) const
  QString fieldSerial(qsizetype a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlCachedResultPrivateCall0 call = reinterpret_cast<CuteQSqlCachedResultPrivateCall0>(taken[0]);
      QString * given = call(this, a0, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlResultPrivate::fieldSerial(a0);
  }
};

//  QSqlCachedResult *QSqlCachedResultPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSqlCachedResult *ritual_ZN23QSqlCachedResultPrivate6q_funcEv(
    QSqlCachedResultPrivate *self) {
  return self->q_func();
}

//  const QSqlCachedResult *QSqlCachedResultPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSqlCachedResult *ritual_ZNK23QSqlCachedResultPrivate6q_funcEv(
    const QSqlCachedResultPrivate *self) {
  return self->q_func();
}

//  bool QSqlCachedResultPrivate::canSeek(int i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSqlCachedResultPrivate7canSeekEi(
    const QSqlCachedResultPrivate *self,
    int i) {
  return self->canSeek(i);
}

//  int QSqlCachedResultPrivate::cacheCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSqlCachedResultPrivate10cacheCountEv(
    const QSqlCachedResultPrivate *self) {
  return self->cacheCount();
}

//  void QSqlCachedResultPrivate::init(int count, bool fo)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSqlCachedResultPrivate4initEib(
    QSqlCachedResultPrivate *self,
    int count,
    bool fo) {
  self->init(count, fo);
}

//  void QSqlCachedResultPrivate::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSqlCachedResultPrivate7cleanupEv(
    QSqlCachedResultPrivate *self) {
  self->cleanup();
}

//  int QSqlCachedResultPrivate::nextIndex()
extern "C" Q_DECL_EXPORT
int ritual_ZN23QSqlCachedResultPrivate9nextIndexEv(
    QSqlCachedResultPrivate *self) {
  return self->nextIndex();
}

//  void QSqlCachedResultPrivate::revertLast()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSqlCachedResultPrivate10revertLastEv(
    QSqlCachedResultPrivate *self) {
  self->revertLast();
}

//  QSqlCachedResultPrivate::~QSqlCachedResultPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSqlCachedResultPrivateD1Ev(QSqlCachedResultPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQSqlCachedResultPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlCachedResultPrivate(
    QSqlCachedResultPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlCachedResultPrivate *>(self)->take(key, call);
}
