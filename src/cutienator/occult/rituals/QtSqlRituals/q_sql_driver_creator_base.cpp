//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqldatabase.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqldatabase.h>
#include <cstring>

//  A QSqlDriverCreatorBase that Python can take functions over in. Every QSqlDriverCreatorBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSqlDriverCreatorBaseCall0)(const void *, int *);
class CuteQSqlDriverCreatorBase : public QSqlDriverCreatorBase {
public:
  using QSqlDriverCreatorBase::QSqlDriverCreatorBase;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QSqlDriverCreatorBase12createObjectEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QSqlDriver *QSqlDriverCreatorBase::createObject() const
  QSqlDriver *createObject() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlDriverCreatorBaseCall0 call = reinterpret_cast<CuteQSqlDriverCreatorBaseCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSqlDriver *>(given);
    }
    return {};
  }
};

//  QSqlDriverCreatorBase::~QSqlDriverCreatorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlDriverCreatorBaseD1Ev(QSqlDriverCreatorBase *self) {
  delete self;
}

//  QSqlDriver *QSqlDriverCreatorBase::createObject() const
extern "C" Q_DECL_EXPORT
QSqlDriver *ritual_ZNK21QSqlDriverCreatorBase12createObjectEv(
    const QSqlDriverCreatorBase *self) {
  return self->createObject();
}

//  a Python function taken by a CuteQSqlDriverCreatorBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlDriverCreatorBase(
    QSqlDriverCreatorBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlDriverCreatorBase *>(self)->take(key, call);
}
