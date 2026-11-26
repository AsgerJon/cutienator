//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqlresult_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/qsqlresult.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqlresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QSqlResultPrivate that Python can take functions over in. Every QSqlResultPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQSqlResultPrivateCall0)(const void *, qsizetype, int *);
class CuteQSqlResultPrivate : public QSqlResultPrivate {
public:
  using QSqlResultPrivate::QSqlResultPrivate;
  CuteQSqlResultPrivate(const QSqlResultPrivate & other) : QSqlResultPrivate(other) {}
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
      CuteQSqlResultPrivateCall0 call = reinterpret_cast<CuteQSqlResultPrivateCall0>(taken[0]);
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

//  QSqlResult *QSqlResultPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSqlResult *ritual_ZN17QSqlResultPrivate6q_funcEv(QSqlResultPrivate *self) {
  return self->q_func();
}

//  const QSqlResult *QSqlResultPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSqlResult *ritual_ZNK17QSqlResultPrivate6q_funcEv(
    const QSqlResultPrivate *self) {
  return self->q_func();
}

//  QSqlResultPrivate::QSqlResultPrivate(QSqlResult *q, const QSqlDriver
//      *drv)
extern "C" Q_DECL_EXPORT
QSqlResultPrivate *ritual_ZN17QSqlResultPrivateC1EP10QSqlResultPK10QSqlDriver(
    QSqlResult *q,
    const QSqlDriver *drv) {
  return new CuteQSqlResultPrivate(q, drv);
}

//  QSqlResultPrivate::~QSqlResultPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSqlResultPrivateD1Ev(QSqlResultPrivate *self) {
  delete self;
}

//  void QSqlResultPrivate::clearValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSqlResultPrivate11clearValuesEv(QSqlResultPrivate *self) {
  self->clearValues();
}

//  void QSqlResultPrivate::resetBindCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSqlResultPrivate14resetBindCountEv(
    QSqlResultPrivate *self) {
  self->resetBindCount();
}

//  void QSqlResultPrivate::clearIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSqlResultPrivate10clearIndexEv(QSqlResultPrivate *self) {
  self->clearIndex();
}

//  void QSqlResultPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSqlResultPrivate5clearEv(QSqlResultPrivate *self) {
  self->clear();
}

//  QString QSqlResultPrivate::fieldSerial(qsizetype a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSqlResultPrivate11fieldSerialEx(
    const QSqlResultPrivate *self,
    qsizetype a0) {
  return new QString(self->fieldSerial(a0));
}

//  QString QSqlResultPrivate::positionalToNamedBinding(const QString &query)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSqlResultPrivate24positionalToNamedBindingERK7QString(
    const QSqlResultPrivate *self,
    const QString *query) {
  return new QString(self->positionalToNamedBinding(*query));
}

//  QString QSqlResultPrivate::namedToPositionalBinding(const QString &query)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSqlResultPrivate24namedToPositionalBindingERK7QString(
    QSqlResultPrivate *self,
    const QString *query) {
  return new QString(self->namedToPositionalBinding(*query));
}

//  QString QSqlResultPrivate::holderAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSqlResultPrivate8holderAtEi(
    const QSqlResultPrivate *self,
    int index) {
  return new QString(self->holderAt(index));
}

//  bool QSqlResultPrivate::isVariantNull(const QVariant &variant)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSqlResultPrivate13isVariantNullERK8QVariant(
    const QVariant *variant) {
  return QSqlResultPrivate::isVariantNull(*variant);
}

//  a Python function taken by a CuteQSqlResultPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlResultPrivate(
    QSqlResultPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlResultPrivate *>(self)->take(key, call);
}

//  QString QSqlResultPrivate::fieldSerial(qsizetype a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK17QSqlResultPrivate11fieldSerialEx(
    const QSqlResultPrivate *self,
    qsizetype a0) {
  return new QString(self->QSqlResultPrivate::fieldSerial(a0));
}
