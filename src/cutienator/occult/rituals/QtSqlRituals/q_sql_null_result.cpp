//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqlnulldriver_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqlnulldriver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqlerror.h>
#include <QtSql/qsqlrecord.h>
#include <cstring>

//  Only a class built on QSqlNullResult may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlNullResult : QSqlNullResult {
  using QSqlNullResult::data;
  using QSqlNullResult::reset;
  using QSqlNullResult::fetch;
  using QSqlNullResult::fetchFirst;
  using QSqlNullResult::fetchLast;
  using QSqlNullResult::isNull;
  using QSqlNullResult::size;
  using QSqlNullResult::numRowsAffected;
  using QSqlNullResult::setAt;
  using QSqlNullResult::setActive;
  using QSqlNullResult::setLastError;
  using QSqlNullResult::setQuery;
  using QSqlNullResult::setSelect;
  using QSqlNullResult::setForwardOnly;
  using QSqlNullResult::exec;
  using QSqlNullResult::prepare;
  using QSqlNullResult::savePrepare;
  using QSqlNullResult::bindValue;
};

//  A QSqlNullResult that Python can take functions over in. Every QSqlNullResult
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQSqlNullResultCall0)(const void *, int, int *);
typedef bool (*CuteQSqlNullResultCall1)(const void *, const QString *, int *);
typedef bool (*CuteQSqlNullResultCall2)(const void *, int, int *);
typedef bool (*CuteQSqlNullResultCall3)(const void *, int *);
typedef bool (*CuteQSqlNullResultCall4)(const void *, int *);
typedef bool (*CuteQSqlNullResultCall5)(const void *, int, int *);
typedef int (*CuteQSqlNullResultCall6)(const void *, int *);
typedef int (*CuteQSqlNullResultCall7)(const void *, int *);
typedef void (*CuteQSqlNullResultCall8)(const void *, int, int *);
typedef void (*CuteQSqlNullResultCall9)(const void *, bool, int *);
typedef void (*CuteQSqlNullResultCall10)(const void *, const QSqlError *, int *);
typedef void (*CuteQSqlNullResultCall11)(const void *, const QString *, int *);
typedef void (*CuteQSqlNullResultCall12)(const void *, bool, int *);
typedef void (*CuteQSqlNullResultCall13)(const void *, bool, int *);
typedef bool (*CuteQSqlNullResultCall14)(const void *, int *);
typedef bool (*CuteQSqlNullResultCall15)(const void *, const QString *, int *);
typedef bool (*CuteQSqlNullResultCall16)(const void *, const QString *, int *);
typedef void (*CuteQSqlNullResultCall17)(const void *, int, const QVariant *, int, int *);
typedef void (*CuteQSqlNullResultCall18)(const void *, const QString *, const QVariant *, int, int *);
typedef const QVariant * (*CuteQSqlNullResultCall19)(const void *, int *);
typedef bool (*CuteQSqlNullResultCall20)(const void *, int *);
typedef bool (*CuteQSqlNullResultCall21)(const void *, int *);
typedef const QSqlRecord * (*CuteQSqlNullResultCall22)(const void *, int *);
typedef const QVariant * (*CuteQSqlNullResultCall23)(const void *, int *);
typedef void (*CuteQSqlNullResultCall24)(const void *, int, void *, int *);
typedef bool (*CuteQSqlNullResultCall25)(const void *, bool, int *);
typedef void (*CuteQSqlNullResultCall26)(const void *, int *);
typedef void (*CuteQSqlNullResultCall27)(const void *, int, int *);
typedef bool (*CuteQSqlNullResultCall28)(const void *, int *);
class CuteQSqlNullResult : public QSqlNullResult {
public:
  using QSqlNullResult::QSqlNullResult;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QSqlResult4dataEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult5resetERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult5fetchEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult10fetchFirstEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9fetchLastEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult6isNullEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult4sizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult15numRowsAffectedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult5setAtEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9setActiveEb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult12setLastErrorERK9QSqlError")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult8setQueryERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9setSelectEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult14setForwardOnlyEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult4execEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult7prepareERK7QString")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult11savePrepareERK7QString")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlResult6handleEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult9fetchNextEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlResult13fetchPreviousEv")) {
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

  //  QVariant QSqlNullResult::data(int a0)
  QVariant data(int a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlNullResultCall0 call = reinterpret_cast<CuteQSqlNullResultCall0>(taken[0]);
      const QVariant * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QSqlNullResult::data(a0);
  }

  //  bool QSqlNullResult::reset(const QString &a0)
  bool reset(const QString &a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlNullResultCall1 call = reinterpret_cast<CuteQSqlNullResultCall1>(taken[1]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::reset(a0);
  }

  //  bool QSqlNullResult::fetch(int a0)
  bool fetch(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlNullResultCall2 call = reinterpret_cast<CuteQSqlNullResultCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::fetch(a0);
  }

  //  bool QSqlNullResult::fetchFirst()
  bool fetchFirst() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlNullResultCall3 call = reinterpret_cast<CuteQSqlNullResultCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::fetchFirst();
  }

  //  bool QSqlNullResult::fetchLast()
  bool fetchLast() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSqlNullResultCall4 call = reinterpret_cast<CuteQSqlNullResultCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::fetchLast();
  }

  //  bool QSqlNullResult::isNull(int a0)
  bool isNull(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSqlNullResultCall5 call = reinterpret_cast<CuteQSqlNullResultCall5>(taken[5]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::isNull(a0);
  }

  //  int QSqlNullResult::size()
  int size() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSqlNullResultCall6 call = reinterpret_cast<CuteQSqlNullResultCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::size();
  }

  //  int QSqlNullResult::numRowsAffected()
  int numRowsAffected() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSqlNullResultCall7 call = reinterpret_cast<CuteQSqlNullResultCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::numRowsAffected();
  }

  //  void QSqlNullResult::setAt(int a0)
  void setAt(int a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSqlNullResultCall8 call = reinterpret_cast<CuteQSqlNullResultCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSqlNullResult::setAt(a0);
  }

  //  void QSqlNullResult::setActive(bool a0)
  void setActive(bool a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSqlNullResultCall9 call = reinterpret_cast<CuteQSqlNullResultCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSqlNullResult::setActive(a0);
  }

  //  void QSqlNullResult::setLastError(const QSqlError &a0)
  void setLastError(const QSqlError &a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSqlNullResultCall10 call = reinterpret_cast<CuteQSqlNullResultCall10>(taken[10]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSqlNullResult::setLastError(a0);
  }

  //  void QSqlNullResult::setQuery(const QString &a0)
  void setQuery(const QString &a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSqlNullResultCall11 call = reinterpret_cast<CuteQSqlNullResultCall11>(taken[11]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSqlNullResult::setQuery(a0);
  }

  //  void QSqlNullResult::setSelect(bool a0)
  void setSelect(bool a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSqlNullResultCall12 call = reinterpret_cast<CuteQSqlNullResultCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSqlNullResult::setSelect(a0);
  }

  //  void QSqlNullResult::setForwardOnly(bool a0)
  void setForwardOnly(bool a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSqlNullResultCall13 call = reinterpret_cast<CuteQSqlNullResultCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSqlNullResult::setForwardOnly(a0);
  }

  //  bool QSqlNullResult::exec()
  bool exec() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSqlNullResultCall14 call = reinterpret_cast<CuteQSqlNullResultCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::exec();
  }

  //  bool QSqlNullResult::prepare(const QString &a0)
  bool prepare(const QString &a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSqlNullResultCall15 call = reinterpret_cast<CuteQSqlNullResultCall15>(taken[15]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::prepare(a0);
  }

  //  bool QSqlNullResult::savePrepare(const QString &a0)
  bool savePrepare(const QString &a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSqlNullResultCall16 call = reinterpret_cast<CuteQSqlNullResultCall16>(taken[16]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QSqlNullResult::savePrepare(a0);
  }

  //  void QSqlNullResult::bindValue(int a0, const QVariant &a1,
  //      QSql::ParamType a2)
  void bindValue(int a0, const QVariant &a1, QSql::ParamType a2) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSqlNullResultCall17 call = reinterpret_cast<CuteQSqlNullResultCall17>(taken[17]);
      call(this, a0, &a1, static_cast<int>(a2.toInt()), &handled);
      if (handled) return;
    }
    QSqlNullResult::bindValue(a0, a1, a2);
  }

  //  void QSqlNullResult::bindValue(const QString &a0, const QVariant &a1,
  //      QSql::ParamType a2)
  void bindValue(
      const QString &a0,
      const QVariant &a1,
      QSql::ParamType a2) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSqlNullResultCall18 call = reinterpret_cast<CuteQSqlNullResultCall18>(taken[18]);
      call(this, &a0, &a1, static_cast<int>(a2.toInt()), &handled);
      if (handled) return;
    }
    QSqlNullResult::bindValue(a0, a1, a2);
  }

  //  QVariant QSqlResult::handle() const
  QVariant handle() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSqlNullResultCall19 call = reinterpret_cast<CuteQSqlNullResultCall19>(taken[19]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlResult::handle();
  }

  //  bool QSqlResult::fetchNext()
  bool fetchNext() override {
    if (taken[20]) {
      int handled = 0;
      CuteQSqlNullResultCall20 call = reinterpret_cast<CuteQSqlNullResultCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlResult::fetchNext();
  }

  //  bool QSqlResult::fetchPrevious()
  bool fetchPrevious() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSqlNullResultCall21 call = reinterpret_cast<CuteQSqlNullResultCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlResult::fetchPrevious();
  }

  //  QSqlRecord QSqlResult::record() const
  QSqlRecord record() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSqlNullResultCall22 call = reinterpret_cast<CuteQSqlNullResultCall22>(taken[22]);
      const QSqlRecord * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlResult::record();
  }

  //  QVariant QSqlResult::lastInsertId() const
  QVariant lastInsertId() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSqlNullResultCall23 call = reinterpret_cast<CuteQSqlNullResultCall23>(taken[23]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlResult::lastInsertId();
  }

  //  void QSqlResult::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSqlNullResultCall24 call = reinterpret_cast<CuteQSqlNullResultCall24>(taken[24]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QSqlResult::virtual_hook(id, data);
  }

  //  bool QSqlResult::execBatch(bool arrayBind)
  bool execBatch(bool arrayBind) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSqlNullResultCall25 call = reinterpret_cast<CuteQSqlNullResultCall25>(taken[25]);
      bool given = call(this, arrayBind, &handled);
      if (handled) return given;
    }
    return QSqlResult::execBatch(arrayBind);
  }

  //  void QSqlResult::detachFromResultSet()
  void detachFromResultSet() override {
    if (taken[26]) {
      int handled = 0;
      CuteQSqlNullResultCall26 call = reinterpret_cast<CuteQSqlNullResultCall26>(taken[26]);
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
      CuteQSqlNullResultCall27 call = reinterpret_cast<CuteQSqlNullResultCall27>(taken[27]);
      call(this, static_cast<int>(policy), &handled);
      if (handled) return;
    }
    QSqlResult::setNumericalPrecisionPolicy(policy);
  }

  //  bool QSqlResult::nextResult()
  bool nextResult() override {
    if (taken[28]) {
      int handled = 0;
      CuteQSqlNullResultCall28 call = reinterpret_cast<CuteQSqlNullResultCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlResult::nextResult();
  }
};

//  QSqlNullResult::QSqlNullResult(const QSqlDriver *d)
extern "C" Q_DECL_EXPORT
QSqlNullResult *ritual_ZN14QSqlNullResultC1EPK10QSqlDriver(
    const QSqlDriver *d) {
  return new CuteQSqlNullResult(d);
}

//  QVariant QSqlNullResult::data(int a0)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QSqlNullResult4dataEi(QSqlNullResult *self, int a0) {
  return new QVariant(self->data(a0));
}

//  bool QSqlNullResult::reset(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult5resetERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  return self->reset(*a0);
}

//  bool QSqlNullResult::fetch(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult5fetchEi(QSqlNullResult *self, int a0) {
  return self->fetch(a0);
}

//  bool QSqlNullResult::fetchFirst()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult10fetchFirstEv(QSqlNullResult *self) {
  return self->fetchFirst();
}

//  bool QSqlNullResult::fetchLast()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult9fetchLastEv(QSqlNullResult *self) {
  return self->fetchLast();
}

//  bool QSqlNullResult::isNull(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult6isNullEi(QSqlNullResult *self, int a0) {
  return self->isNull(a0);
}

//  int QSqlNullResult::size()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QSqlNullResult4sizeEv(QSqlNullResult *self) {
  return self->size();
}

//  int QSqlNullResult::numRowsAffected()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QSqlNullResult15numRowsAffectedEv(QSqlNullResult *self) {
  return self->numRowsAffected();
}

//  void QSqlNullResult::setAt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult5setAtEi(QSqlNullResult *self, int a0) {
  self->setAt(a0);
}

//  void QSqlNullResult::setActive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult9setActiveEb(QSqlNullResult *self, bool a0) {
  self->setActive(a0);
}

//  void QSqlNullResult::setLastError(const QSqlError &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult12setLastErrorERK9QSqlError(
    QSqlNullResult *self,
    const QSqlError *a0) {
  self->setLastError(*a0);
}

//  void QSqlNullResult::setQuery(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult8setQueryERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  self->setQuery(*a0);
}

//  void QSqlNullResult::setSelect(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult9setSelectEb(QSqlNullResult *self, bool a0) {
  self->setSelect(a0);
}

//  void QSqlNullResult::setForwardOnly(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult14setForwardOnlyEb(
    QSqlNullResult *self,
    bool a0) {
  self->setForwardOnly(a0);
}

//  bool QSqlNullResult::exec()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult4execEv(QSqlNullResult *self) {
  return self->exec();
}

//  bool QSqlNullResult::prepare(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult7prepareERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  return self->prepare(*a0);
}

//  bool QSqlNullResult::savePrepare(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullResult11savePrepareERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  return self->savePrepare(*a0);
}

//  void QSqlNullResult::bindValue(int a0, const QVariant &a1,
//      QSql::ParamType a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlNullResult *self,
    int a0,
    const QVariant *a1,
    int a2) {
  self->bindValue(a0, *a1, QFlags<QSql::ParamTypeFlag>::fromInt(a2));
}

//  void QSqlNullResult::bindValue(const QString &a0, const QVariant &a1,
//      QSql::ParamType a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlNullResult *self,
    const QString *a0,
    const QVariant *a1,
    int a2) {
  self->bindValue(*a0, *a1, QFlags<QSql::ParamTypeFlag>::fromInt(a2));
}

//  a Python function taken by a CuteQSqlNullResult, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlNullResult(
    QSqlNullResult *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlNullResult *>(self)->take(key, call);
}

//  QVariant QSqlNullResult::data(int a0)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN14QSqlNullResult4dataEi(
    QSqlNullResult *self,
    int a0) {
  return new QVariant(
      static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::data(
          a0));
}

//  bool QSqlNullResult::reset(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult5resetERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::reset(
      *a0);
}

//  bool QSqlNullResult::fetch(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult5fetchEi(QSqlNullResult *self, int a0) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::fetch(
      a0);
}

//  bool QSqlNullResult::fetchFirst()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult10fetchFirstEv(QSqlNullResult *self) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::fetchFirst();
}

//  bool QSqlNullResult::fetchLast()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult9fetchLastEv(QSqlNullResult *self) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::fetchLast();
}

//  bool QSqlNullResult::isNull(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult6isNullEi(QSqlNullResult *self, int a0) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::isNull(
      a0);
}

//  int QSqlNullResult::size()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN14QSqlNullResult4sizeEv(QSqlNullResult *self) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::size();
}

//  int QSqlNullResult::numRowsAffected()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN14QSqlNullResult15numRowsAffectedEv(QSqlNullResult *self) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::numRowsAffected();
}

//  void QSqlNullResult::setAt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult5setAtEi(QSqlNullResult *self, int a0) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::setAt(a0);
}

//  void QSqlNullResult::setActive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult9setActiveEb(
    QSqlNullResult *self,
    bool a0) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::setActive(a0);
}

//  void QSqlNullResult::setLastError(const QSqlError &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult12setLastErrorERK9QSqlError(
    QSqlNullResult *self,
    const QSqlError *a0) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::setLastError(
      *a0);
}

//  void QSqlNullResult::setQuery(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult8setQueryERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::setQuery(*a0);
}

//  void QSqlNullResult::setSelect(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult9setSelectEb(
    QSqlNullResult *self,
    bool a0) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::setSelect(a0);
}

//  void QSqlNullResult::setForwardOnly(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult14setForwardOnlyEb(
    QSqlNullResult *self,
    bool a0) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::setForwardOnly(
      a0);
}

//  bool QSqlNullResult::exec()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult4execEv(QSqlNullResult *self) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::exec();
}

//  bool QSqlNullResult::prepare(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult7prepareERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::prepare(
      *a0);
}

//  bool QSqlNullResult::savePrepare(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullResult11savePrepareERK7QString(
    QSqlNullResult *self,
    const QString *a0) {
  return static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::savePrepare(
      *a0);
}

//  void QSqlNullResult::bindValue(int a0, const QVariant &a1,
//      QSql::ParamType a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlNullResult *self,
    int a0,
    const QVariant *a1,
    int a2) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::bindValue(
      a0,
      *a1,
      QFlags<QSql::ParamTypeFlag>::fromInt(a2));
}

//  void QSqlNullResult::bindValue(const QString &a0, const QVariant &a1,
//      QSql::ParamType a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlNullResult *self,
    const QString *a0,
    const QVariant *a1,
    int a2) {
  static_cast<OwnQSqlNullResult *>(self)->OwnQSqlNullResult::bindValue(
      *a0,
      *a1,
      QFlags<QSql::ParamTypeFlag>::fromInt(a2));
}
