//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqlresult.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqlerror.h>
#include <QtCore/qnamespace.h>
#include <QtSql/qsqlrecord.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QSqlResult may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlResult : QSqlResult {
  using QSqlResult::setAt;
  using QSqlResult::setActive;
  using QSqlResult::setLastError;
  using QSqlResult::setQuery;
  using QSqlResult::setSelect;
  using QSqlResult::setForwardOnly;
  using QSqlResult::exec;
  using QSqlResult::prepare;
  using QSqlResult::savePrepare;
  using QSqlResult::bindValue;
  using QSqlResult::fetchNext;
  using QSqlResult::fetchPrevious;
  using QSqlResult::record;
  using QSqlResult::lastInsertId;
  using QSqlResult::virtual_hook;
  using QSqlResult::execBatch;
  using QSqlResult::detachFromResultSet;
  using QSqlResult::setNumericalPrecisionPolicy;
  using QSqlResult::nextResult;
};

//  A QSqlResult that Python can take functions over in. Every QSqlResult
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQSqlResultCall0)(const void *, int *);
typedef void (*CuteQSqlResultCall1)(const void *, int, int *);
typedef void (*CuteQSqlResultCall2)(const void *, bool, int *);
typedef void (*CuteQSqlResultCall3)(const void *, const QSqlError *, int *);
typedef void (*CuteQSqlResultCall4)(const void *, const QString *, int *);
typedef void (*CuteQSqlResultCall5)(const void *, bool, int *);
typedef void (*CuteQSqlResultCall6)(const void *, bool, int *);
typedef bool (*CuteQSqlResultCall7)(const void *, int *);
typedef bool (*CuteQSqlResultCall8)(const void *, const QString *, int *);
typedef bool (*CuteQSqlResultCall9)(const void *, const QString *, int *);
typedef void (*CuteQSqlResultCall10)(const void *, int, const QVariant *, int, int *);
typedef void (*CuteQSqlResultCall11)(const void *, const QString *, const QVariant *, int, int *);
typedef const QVariant * (*CuteQSqlResultCall12)(const void *, int, int *);
typedef bool (*CuteQSqlResultCall13)(const void *, int, int *);
typedef bool (*CuteQSqlResultCall14)(const void *, const QString *, int *);
typedef bool (*CuteQSqlResultCall15)(const void *, int, int *);
typedef bool (*CuteQSqlResultCall16)(const void *, int *);
typedef bool (*CuteQSqlResultCall17)(const void *, int *);
typedef bool (*CuteQSqlResultCall18)(const void *, int *);
typedef bool (*CuteQSqlResultCall19)(const void *, int *);
typedef int (*CuteQSqlResultCall20)(const void *, int *);
typedef int (*CuteQSqlResultCall21)(const void *, int *);
typedef const QSqlRecord * (*CuteQSqlResultCall22)(const void *, int *);
typedef const QVariant * (*CuteQSqlResultCall23)(const void *, int *);
typedef void (*CuteQSqlResultCall24)(const void *, int, void *, int *);
typedef bool (*CuteQSqlResultCall25)(const void *, bool, int *);
typedef void (*CuteQSqlResultCall26)(const void *, int *);
typedef void (*CuteQSqlResultCall27)(const void *, int, int *);
typedef bool (*CuteQSqlResultCall28)(const void *, int *);
class CuteQSqlResult : public QSqlResult {
public:
  using QSqlResult::QSqlResult;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSqlResult6handleEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult5setAtEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9setActiveEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult12setLastErrorERK9QSqlError")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult8setQueryERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9setSelectEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult14setForwardOnlyEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult4execEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult7prepareERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult11savePrepareERK7QString")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult4dataEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult6isNullEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult5resetERK7QString")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult5fetchEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9fetchNextEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult13fetchPreviousEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult10fetchFirstEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9fetchLastEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult4sizeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult15numRowsAffectedEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlResult6recordEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlResult12lastInsertIdEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult12virtual_hookEiPv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9execBatchEb")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult19detachFromResultSetEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult10nextResultEv")) {
      taken[28] = call;
      return true;
    }
    return false;
  }

  //  QVariant QSqlResult::handle() const
  QVariant handle() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlResultCall0 call = reinterpret_cast<CuteQSqlResultCall0>(taken[0]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlResult::handle();
  }

  //  void QSqlResult::setAt(int at)
  void setAt(int at) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlResultCall1 call = reinterpret_cast<CuteQSqlResultCall1>(taken[1]);
      call(this, at, &handled);
      if (handled) return;
    }
    QSqlResult::setAt(at);
  }

  //  void QSqlResult::setActive(bool a)
  void setActive(bool a) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlResultCall2 call = reinterpret_cast<CuteQSqlResultCall2>(taken[2]);
      call(this, a, &handled);
      if (handled) return;
    }
    QSqlResult::setActive(a);
  }

  //  void QSqlResult::setLastError(const QSqlError &e)
  void setLastError(const QSqlError &e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlResultCall3 call = reinterpret_cast<CuteQSqlResultCall3>(taken[3]);
      call(this, &e, &handled);
      if (handled) return;
    }
    QSqlResult::setLastError(e);
  }

  //  void QSqlResult::setQuery(const QString &query)
  void setQuery(const QString &query) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSqlResultCall4 call = reinterpret_cast<CuteQSqlResultCall4>(taken[4]);
      call(this, &query, &handled);
      if (handled) return;
    }
    QSqlResult::setQuery(query);
  }

  //  void QSqlResult::setSelect(bool s)
  void setSelect(bool s) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSqlResultCall5 call = reinterpret_cast<CuteQSqlResultCall5>(taken[5]);
      call(this, s, &handled);
      if (handled) return;
    }
    QSqlResult::setSelect(s);
  }

  //  void QSqlResult::setForwardOnly(bool forward)
  void setForwardOnly(bool forward) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSqlResultCall6 call = reinterpret_cast<CuteQSqlResultCall6>(taken[6]);
      call(this, forward, &handled);
      if (handled) return;
    }
    QSqlResult::setForwardOnly(forward);
  }

  //  bool QSqlResult::exec()
  bool exec() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSqlResultCall7 call = reinterpret_cast<CuteQSqlResultCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlResult::exec();
  }

  //  bool QSqlResult::prepare(const QString &query)
  bool prepare(const QString &query) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSqlResultCall8 call = reinterpret_cast<CuteQSqlResultCall8>(taken[8]);
      bool given = call(this, &query, &handled);
      if (handled) return given;
    }
    return QSqlResult::prepare(query);
  }

  //  bool QSqlResult::savePrepare(const QString &sqlquery)
  bool savePrepare(const QString &sqlquery) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSqlResultCall9 call = reinterpret_cast<CuteQSqlResultCall9>(taken[9]);
      bool given = call(this, &sqlquery, &handled);
      if (handled) return given;
    }
    return QSqlResult::savePrepare(sqlquery);
  }

  //  void QSqlResult::bindValue(int pos, const QVariant &val,
  //      QSql::ParamType type)
  void bindValue(
      int pos,
      const QVariant &val,
      QSql::ParamType type) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSqlResultCall10 call = reinterpret_cast<CuteQSqlResultCall10>(taken[10]);
      call(this, pos, &val, static_cast<int>(type.toInt()), &handled);
      if (handled) return;
    }
    QSqlResult::bindValue(pos, val, type);
  }

  //  void QSqlResult::bindValue(const QString &placeholder, const QVariant
  //      &val, QSql::ParamType type)
  void bindValue(
      const QString &placeholder,
      const QVariant &val,
      QSql::ParamType type) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSqlResultCall11 call = reinterpret_cast<CuteQSqlResultCall11>(taken[11]);
      call(this, &placeholder, &val, static_cast<int>(type.toInt()), &handled);
      if (handled) return;
    }
    QSqlResult::bindValue(placeholder, val, type);
  }

  //  QVariant QSqlResult::data(int i)
  QVariant data(int i) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSqlResultCall12 call = reinterpret_cast<CuteQSqlResultCall12>(taken[12]);
      const QVariant * given = call(this, i, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSqlResult::isNull(int i)
  bool isNull(int i) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSqlResultCall13 call = reinterpret_cast<CuteQSqlResultCall13>(taken[13]);
      bool given = call(this, i, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSqlResult::reset(const QString &sqlquery)
  bool reset(const QString &sqlquery) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSqlResultCall14 call = reinterpret_cast<CuteQSqlResultCall14>(taken[14]);
      bool given = call(this, &sqlquery, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSqlResult::fetch(int i)
  bool fetch(int i) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSqlResultCall15 call = reinterpret_cast<CuteQSqlResultCall15>(taken[15]);
      bool given = call(this, i, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSqlResult::fetchNext()
  bool fetchNext() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSqlResultCall16 call = reinterpret_cast<CuteQSqlResultCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlResult::fetchNext();
  }

  //  bool QSqlResult::fetchPrevious()
  bool fetchPrevious() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSqlResultCall17 call = reinterpret_cast<CuteQSqlResultCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlResult::fetchPrevious();
  }

  //  bool QSqlResult::fetchFirst()
  bool fetchFirst() override {
    if (taken[18]) {
      int handled = 0;
      CuteQSqlResultCall18 call = reinterpret_cast<CuteQSqlResultCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSqlResult::fetchLast()
  bool fetchLast() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSqlResultCall19 call = reinterpret_cast<CuteQSqlResultCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QSqlResult::size()
  int size() override {
    if (taken[20]) {
      int handled = 0;
      CuteQSqlResultCall20 call = reinterpret_cast<CuteQSqlResultCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QSqlResult::numRowsAffected()
  int numRowsAffected() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSqlResultCall21 call = reinterpret_cast<CuteQSqlResultCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QSqlRecord QSqlResult::record() const
  QSqlRecord record() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSqlResultCall22 call = reinterpret_cast<CuteQSqlResultCall22>(taken[22]);
      const QSqlRecord * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlResult::record();
  }

  //  QVariant QSqlResult::lastInsertId() const
  QVariant lastInsertId() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSqlResultCall23 call = reinterpret_cast<CuteQSqlResultCall23>(taken[23]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlResult::lastInsertId();
  }

  //  void QSqlResult::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSqlResultCall24 call = reinterpret_cast<CuteQSqlResultCall24>(taken[24]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QSqlResult::virtual_hook(id, data);
  }

  //  bool QSqlResult::execBatch(bool arrayBind)
  bool execBatch(bool arrayBind) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSqlResultCall25 call = reinterpret_cast<CuteQSqlResultCall25>(taken[25]);
      bool given = call(this, arrayBind, &handled);
      if (handled) return given;
    }
    return QSqlResult::execBatch(arrayBind);
  }

  //  void QSqlResult::detachFromResultSet()
  void detachFromResultSet() override {
    if (taken[26]) {
      int handled = 0;
      CuteQSqlResultCall26 call = reinterpret_cast<CuteQSqlResultCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlResult::detachFromResultSet();
  }

  //  void QSqlResult::setNumericalPrecisionPolicy(QSql::NumericalPrecision
  //      Policy policy)
  void setNumericalPrecisionPolicy(
      QSql::NumericalPrecisionPolicy policy) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSqlResultCall27 call = reinterpret_cast<CuteQSqlResultCall27>(taken[27]);
      call(this, static_cast<int>(policy), &handled);
      if (handled) return;
    }
    QSqlResult::setNumericalPrecisionPolicy(policy);
  }

  //  bool QSqlResult::nextResult()
  bool nextResult() override {
    if (taken[28]) {
      int handled = 0;
      CuteQSqlResultCall28 call = reinterpret_cast<CuteQSqlResultCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlResult::nextResult();
  }
};

//  QSqlResultPrivate *QSqlResult::d_func()
extern "C" Q_DECL_EXPORT
QSqlResultPrivate *ritual_ZN10QSqlResult6d_funcEv(QSqlResult *self) {
  return self->d_func();
}

//  const QSqlResultPrivate *QSqlResult::d_func() const
extern "C" Q_DECL_EXPORT
const QSqlResultPrivate *ritual_ZNK10QSqlResult6d_funcEv(
    const QSqlResult *self) {
  return self->d_func();
}

//  QSqlResult::~QSqlResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResultD1Ev(QSqlResult *self) {
  delete self;
}

//  QVariant QSqlResult::handle() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QSqlResult6handleEv(const QSqlResult *self) {
  return new QVariant(self->handle());
}

//  QSqlResult::QSqlResult(const QSqlDriver *db)
extern "C" Q_DECL_EXPORT
QSqlResult *ritual_ZN10QSqlResultC1EPK10QSqlDriver(const QSqlDriver *db) {
  return new CuteQSqlResult(db);
}

//  QSqlResult::QSqlResult(QSqlResultPrivate &dd)
extern "C" Q_DECL_EXPORT
QSqlResult *ritual_ZN10QSqlResultC1ER17QSqlResultPrivate(
    QSqlResultPrivate *dd) {
  return new CuteQSqlResult(*dd);
}

//  int QSqlResult::at() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSqlResult2atEv(const QSqlResult *self) {
  return self->at();
}

//  QString QSqlResult::lastQuery() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlResult9lastQueryEv(const QSqlResult *self) {
  return new QString(self->lastQuery());
}

//  QSqlError QSqlResult::lastError() const
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZNK10QSqlResult9lastErrorEv(const QSqlResult *self) {
  return new QSqlError(self->lastError());
}

//  bool QSqlResult::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlResult7isValidEv(const QSqlResult *self) {
  return self->isValid();
}

//  bool QSqlResult::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlResult8isActiveEv(const QSqlResult *self) {
  return self->isActive();
}

//  bool QSqlResult::isSelect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlResult8isSelectEv(const QSqlResult *self) {
  return self->isSelect();
}

//  bool QSqlResult::isForwardOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlResult13isForwardOnlyEv(const QSqlResult *self) {
  return self->isForwardOnly();
}

//  const QSqlDriver *QSqlResult::driver() const
extern "C" Q_DECL_EXPORT
const QSqlDriver *ritual_ZNK10QSqlResult6driverEv(const QSqlResult *self) {
  return self->driver();
}

//  void QSqlResult::setAt(int at)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult5setAtEi(QSqlResult *self, int at) {
  self->setAt(at);
}

//  void QSqlResult::setActive(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult9setActiveEb(QSqlResult *self, bool a) {
  self->setActive(a);
}

//  void QSqlResult::setLastError(const QSqlError &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult12setLastErrorERK9QSqlError(
    QSqlResult *self,
    const QSqlError *e) {
  self->setLastError(*e);
}

//  void QSqlResult::setQuery(const QString &query)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult8setQueryERK7QString(
    QSqlResult *self,
    const QString *query) {
  self->setQuery(*query);
}

//  void QSqlResult::setSelect(bool s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult9setSelectEb(QSqlResult *self, bool s) {
  self->setSelect(s);
}

//  void QSqlResult::setForwardOnly(bool forward)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult14setForwardOnlyEb(
    QSqlResult *self,
    bool forward) {
  self->setForwardOnly(forward);
}

//  bool QSqlResult::exec()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult4execEv(QSqlResult *self) {
  return self->exec();
}

//  bool QSqlResult::prepare(const QString &query)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult7prepareERK7QString(
    QSqlResult *self,
    const QString *query) {
  return self->prepare(*query);
}

//  bool QSqlResult::savePrepare(const QString &sqlquery)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult11savePrepareERK7QString(
    QSqlResult *self,
    const QString *sqlquery) {
  return self->savePrepare(*sqlquery);
}

//  void QSqlResult::bindValue(int pos, const QVariant &val, QSql::ParamType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlResult *self,
    int pos,
    const QVariant *val,
    int type) {
  self->bindValue(pos, *val, QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  void QSqlResult::bindValue(const QString &placeholder, const QVariant
//      &val, QSql::ParamType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlResult *self,
    const QString *placeholder,
    const QVariant *val,
    int type) {
  self->bindValue(
      *placeholder,
      *val,
      QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  void QSqlResult::addBindValue(const QVariant &val, QSql::ParamType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult12addBindValueERK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlResult *self,
    const QVariant *val,
    int type) {
  self->addBindValue(*val, QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  QVariant QSqlResult::boundValue(const QString &placeholder) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QSqlResult10boundValueERK7QString(
    const QSqlResult *self,
    const QString *placeholder) {
  return new QVariant(self->boundValue(*placeholder));
}

//  QVariant QSqlResult::boundValue(int pos) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QSqlResult10boundValueEi(
    const QSqlResult *self,
    int pos) {
  return new QVariant(self->boundValue(pos));
}

//  QSql::ParamType QSqlResult::bindValueType(const QString &placeholder)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSqlResult13bindValueTypeERK7QString(
    const QSqlResult *self,
    const QString *placeholder) {
  return static_cast<int>(self->bindValueType(*placeholder).toInt());
}

//  QSql::ParamType QSqlResult::bindValueType(int pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSqlResult13bindValueTypeEi(
    const QSqlResult *self,
    int pos) {
  return static_cast<int>(self->bindValueType(pos).toInt());
}

//  int QSqlResult::boundValueCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSqlResult15boundValueCountEv(const QSqlResult *self) {
  return self->boundValueCount();
}

//  QVariantList &QSqlResult::boundValues(Qt::Disambiguated_t a0)
extern "C" Q_DECL_EXPORT
QVariantList *ritual_ZN10QSqlResult11boundValuesEN2Qt15Disambiguated_tE(
    QSqlResult *self,
    const Qt::Disambiguated_t *a0) {
  return &(self->boundValues(*a0));
}

//  QVariantList QSqlResult::boundValues(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK10QSqlResult11boundValuesEN2Qt15Disambiguated_tE(
    const QSqlResult *self,
    const Qt::Disambiguated_t *a0) {
  return new QList<QVariant>(self->boundValues(*a0));
}

//  QString QSqlResult::executedQuery() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlResult13executedQueryEv(const QSqlResult *self) {
  return new QString(self->executedQuery());
}

//  QStringList QSqlResult::boundValueNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QSqlResult15boundValueNamesEv(
    const QSqlResult *self) {
  return new QList<QString>(self->boundValueNames());
}

//  QString QSqlResult::boundValueName(int pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlResult14boundValueNameEi(
    const QSqlResult *self,
    int pos) {
  return new QString(self->boundValueName(pos));
}

//  void QSqlResult::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult5clearEv(QSqlResult *self) {
  self->clear();
}

//  bool QSqlResult::hasOutValues() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlResult12hasOutValuesEv(const QSqlResult *self) {
  return self->hasOutValues();
}

//  BindingSyntax QSqlResult::bindingSyntax() const
extern "C" Q_DECL_EXPORT
QSqlResult::BindingSyntax ritual_ZNK10QSqlResult13bindingSyntaxEv(
    const QSqlResult *self) {
  return self->bindingSyntax();
}

//  QVariant QSqlResult::data(int i)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN10QSqlResult4dataEi(QSqlResult *self, int i) {
  return new QVariant(self->data(i));
}

//  bool QSqlResult::isNull(int i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult6isNullEi(QSqlResult *self, int i) {
  return self->isNull(i);
}

//  bool QSqlResult::reset(const QString &sqlquery)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult5resetERK7QString(
    QSqlResult *self,
    const QString *sqlquery) {
  return self->reset(*sqlquery);
}

//  bool QSqlResult::fetch(int i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult5fetchEi(QSqlResult *self, int i) {
  return self->fetch(i);
}

//  bool QSqlResult::fetchNext()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult9fetchNextEv(QSqlResult *self) {
  return self->fetchNext();
}

//  bool QSqlResult::fetchPrevious()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult13fetchPreviousEv(QSqlResult *self) {
  return self->fetchPrevious();
}

//  bool QSqlResult::fetchFirst()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult10fetchFirstEv(QSqlResult *self) {
  return self->fetchFirst();
}

//  bool QSqlResult::fetchLast()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult9fetchLastEv(QSqlResult *self) {
  return self->fetchLast();
}

//  int QSqlResult::size()
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSqlResult4sizeEv(QSqlResult *self) {
  return self->size();
}

//  int QSqlResult::numRowsAffected()
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSqlResult15numRowsAffectedEv(QSqlResult *self) {
  return self->numRowsAffected();
}

//  QSqlRecord QSqlResult::record() const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK10QSqlResult6recordEv(const QSqlResult *self) {
  return new QSqlRecord(self->record());
}

//  QVariant QSqlResult::lastInsertId() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QSqlResult12lastInsertIdEv(const QSqlResult *self) {
  return new QVariant(self->lastInsertId());
}

//  void QSqlResult::virtual_hook(int id, void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult12virtual_hookEiPv(
    QSqlResult *self,
    int id,
    void *data) {
  self->virtual_hook(id, data);
}

//  bool QSqlResult::execBatch(bool arrayBind)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult9execBatchEb(QSqlResult *self, bool arrayBind) {
  return self->execBatch(arrayBind);
}

//  void QSqlResult::detachFromResultSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult19detachFromResultSetEv(QSqlResult *self) {
  self->detachFromResultSet();
}

//  void
//      QSqlResult::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolic
//      y policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE(
    QSqlResult *self,
    QSql::NumericalPrecisionPolicy policy) {
  self->setNumericalPrecisionPolicy(policy);
}

//  QSql::NumericalPrecisionPolicy QSqlResult::numericalPrecisionPolicy()
//      const
extern "C" Q_DECL_EXPORT
QSql::NumericalPrecisionPolicy ritual_ZNK10QSqlResult24numericalPrecisionPolicyEv(
    const QSqlResult *self) {
  return self->numericalPrecisionPolicy();
}

//  void QSqlResult::setPositionalBindingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult27setPositionalBindingEnabledEb(
    QSqlResult *self,
    bool enable) {
  self->setPositionalBindingEnabled(enable);
}

//  bool QSqlResult::isPositionalBindingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlResult26isPositionalBindingEnabledEv(
    const QSqlResult *self) {
  return self->isPositionalBindingEnabled();
}

//  bool QSqlResult::nextResult()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlResult10nextResultEv(QSqlResult *self) {
  return self->nextResult();
}

//  void QSqlResult::resetBindCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlResult14resetBindCountEv(QSqlResult *self) {
  self->resetBindCount();
}

//  a Python function taken by a CuteQSqlResult, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlResult(QSqlResult *self, const char *key, void *call) {
  return static_cast<CuteQSqlResult *>(self)->take(key, call);
}

//  QVariant QSqlResult::handle() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK10QSqlResult6handleEv(const QSqlResult *self) {
  return new QVariant(self->QSqlResult::handle());
}

//  void QSqlResult::setAt(int at)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult5setAtEi(QSqlResult *self, int at) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::setAt(at);
}

//  void QSqlResult::setActive(bool a)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult9setActiveEb(QSqlResult *self, bool a) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::setActive(a);
}

//  void QSqlResult::setLastError(const QSqlError &e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult12setLastErrorERK9QSqlError(
    QSqlResult *self,
    const QSqlError *e) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::setLastError(*e);
}

//  void QSqlResult::setQuery(const QString &query)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult8setQueryERK7QString(
    QSqlResult *self,
    const QString *query) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::setQuery(*query);
}

//  void QSqlResult::setSelect(bool s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult9setSelectEb(QSqlResult *self, bool s) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::setSelect(s);
}

//  void QSqlResult::setForwardOnly(bool forward)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult14setForwardOnlyEb(
    QSqlResult *self,
    bool forward) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::setForwardOnly(forward);
}

//  bool QSqlResult::exec()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlResult4execEv(QSqlResult *self) {
  return static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::exec();
}

//  bool QSqlResult::prepare(const QString &query)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlResult7prepareERK7QString(
    QSqlResult *self,
    const QString *query) {
  return static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::prepare(*query);
}

//  bool QSqlResult::savePrepare(const QString &sqlquery)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlResult11savePrepareERK7QString(
    QSqlResult *self,
    const QString *sqlquery) {
  return static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::savePrepare(
      *sqlquery);
}

//  void QSqlResult::bindValue(int pos, const QVariant &val, QSql::ParamType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlResult *self,
    int pos,
    const QVariant *val,
    int type) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::bindValue(
      pos,
      *val,
      QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  void QSqlResult::bindValue(const QString &placeholder, const QVariant
//      &val, QSql::ParamType type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlResult *self,
    const QString *placeholder,
    const QVariant *val,
    int type) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::bindValue(
      *placeholder,
      *val,
      QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  bool QSqlResult::fetchNext()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlResult9fetchNextEv(QSqlResult *self) {
  return static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::fetchNext();
}

//  bool QSqlResult::fetchPrevious()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlResult13fetchPreviousEv(QSqlResult *self) {
  return static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::fetchPrevious();
}

//  QSqlRecord QSqlResult::record() const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_own_ZNK10QSqlResult6recordEv(const QSqlResult *self) {
  return new QSqlRecord(
      static_cast<const OwnQSqlResult *>(self)->OwnQSqlResult::record());
}

//  QVariant QSqlResult::lastInsertId() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK10QSqlResult12lastInsertIdEv(
    const QSqlResult *self) {
  return new QVariant(
      static_cast<const OwnQSqlResult *>(self)->OwnQSqlResult::lastInsertId());
}

//  void QSqlResult::virtual_hook(int id, void *data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult12virtual_hookEiPv(
    QSqlResult *self,
    int id,
    void *data) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::virtual_hook(id, data);
}

//  bool QSqlResult::execBatch(bool arrayBind)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlResult9execBatchEb(
    QSqlResult *self,
    bool arrayBind) {
  return static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::execBatch(
      arrayBind);
}

//  void QSqlResult::detachFromResultSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult19detachFromResultSetEv(QSqlResult *self) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::detachFromResultSet();
}

//  void
//      QSqlResult::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolic
//      y policy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlResult27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE(
    QSqlResult *self,
    QSql::NumericalPrecisionPolicy policy) {
  static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::setNumericalPrecisionPolicy(
      policy);
}

//  bool QSqlResult::nextResult()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlResult10nextResultEv(QSqlResult *self) {
  return static_cast<OwnQSqlResult *>(self)->OwnQSqlResult::nextResult();
}
