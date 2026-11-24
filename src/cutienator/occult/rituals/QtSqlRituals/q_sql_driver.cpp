//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqldriver.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqldriver.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqlindex.h>
#include <QtSql/qsqlrecord.h>
#include <QtSql/qsqlfield.h>
#include <QtSql/qsqlerror.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QSqlDriver may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlDriver : QSqlDriver {
  using QSqlDriver::setOpen;
  using QSqlDriver::setOpenError;
  using QSqlDriver::setLastError;
};

//  A QSqlDriver that Python can take functions over in. Every QSqlDriver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSqlDriverCall0)(const void *, int *);
typedef bool (*CuteQSqlDriverCall1)(const void *, int *);
typedef bool (*CuteQSqlDriverCall2)(const void *, int *);
typedef bool (*CuteQSqlDriverCall3)(const void *, int *);
typedef const QSqlIndex * (*CuteQSqlDriverCall4)(const void *, const QString *, int *);
typedef const QSqlRecord * (*CuteQSqlDriverCall5)(const void *, const QString *, int *);
typedef QString * (*CuteQSqlDriverCall6)(const void *, const QSqlField *, bool, int *);
typedef QString * (*CuteQSqlDriverCall7)(const void *, const QString *, int, int *);
typedef QString * (*CuteQSqlDriverCall8)(const void *, int, const QString *, const QSqlRecord *, bool, int *);
typedef const QVariant * (*CuteQSqlDriverCall9)(const void *, int *);
typedef bool (*CuteQSqlDriverCall10)(const void *, int, int *);
typedef void (*CuteQSqlDriverCall11)(const void *, int *);
typedef void * (*CuteQSqlDriverCall12)(const void *, int *);
typedef bool (*CuteQSqlDriverCall13)(const void *, const QString *, const QString *, const QString *, const QString *, int, const QString *, int *);
typedef bool (*CuteQSqlDriverCall14)(const void *, const QString *, int *);
typedef bool (*CuteQSqlDriverCall15)(const void *, const QString *, int *);
typedef bool (*CuteQSqlDriverCall16)(const void *, const QString *, int, int *);
typedef QString * (*CuteQSqlDriverCall17)(const void *, const QString *, int, int *);
typedef int (*CuteQSqlDriverCall18)(const void *, int, int *);
typedef bool (*CuteQSqlDriverCall19)(const void *, int *);
typedef void (*CuteQSqlDriverCall20)(const void *, bool, int *);
typedef void (*CuteQSqlDriverCall21)(const void *, bool, int *);
typedef void (*CuteQSqlDriverCall22)(const void *, const QSqlError *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlDriverCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlDriverCall24)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlDriverCall25)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlDriverCall26)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlDriverCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlDriverCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlDriverCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSqlDriver : public QSqlDriver {
public:
  using QSqlDriver::QSqlDriver;
  void *taken[30] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSqlDriver6isOpenEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver16beginTransactionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver17commitTransactionEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver19rollbackTransactionEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver12primaryIndexERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver6recordERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver11formatValueERK9QSqlFieldb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver16escapeIdentifierERK7QStringNS_14IdentifierTypeE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver12sqlStatementENS_13StatementTypeERK7QStringRK10QSqlRecordb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver6handleEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver10hasFeatureENS_13DriverFeatureE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver5closeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver12createResultEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver4openERK7QStringS2_S2_S2_iS2_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver23subscribeToNotificationERK7QString")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver27unsubscribeFromNotificationERK7QString")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver19isIdentifierEscapedERK7QStringNS_14IdentifierTypeE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver15stripDelimitersERK7QStringNS_14IdentifierTypeE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver23maximumIdentifierLengthENS_14IdentifierTypeE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver11cancelQueryEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver7setOpenEb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver12setOpenErrorEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver12setLastErrorERK9QSqlError")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QSqlDriver::isOpen() const
  bool isOpen() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlDriverCall0 call = reinterpret_cast<CuteQSqlDriverCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::isOpen();
  }

  //  bool QSqlDriver::beginTransaction()
  bool beginTransaction() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlDriverCall1 call = reinterpret_cast<CuteQSqlDriverCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::beginTransaction();
  }

  //  bool QSqlDriver::commitTransaction()
  bool commitTransaction() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlDriverCall2 call = reinterpret_cast<CuteQSqlDriverCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::commitTransaction();
  }

  //  bool QSqlDriver::rollbackTransaction()
  bool rollbackTransaction() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlDriverCall3 call = reinterpret_cast<CuteQSqlDriverCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::rollbackTransaction();
  }

  //  QSqlIndex QSqlDriver::primaryIndex(const QString &tableName) const
  QSqlIndex primaryIndex(const QString &tableName) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSqlDriverCall4 call = reinterpret_cast<CuteQSqlDriverCall4>(taken[4]);
      const QSqlIndex * given = call(this, &tableName, &handled);
      if (handled && given) return *given;
    }
    return QSqlDriver::primaryIndex(tableName);
  }

  //  QSqlRecord QSqlDriver::record(const QString &tableName) const
  QSqlRecord record(const QString &tableName) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSqlDriverCall5 call = reinterpret_cast<CuteQSqlDriverCall5>(taken[5]);
      const QSqlRecord * given = call(this, &tableName, &handled);
      if (handled && given) return *given;
    }
    return QSqlDriver::record(tableName);
  }

  //  QString QSqlDriver::formatValue(const QSqlField &field, bool
  //      trimStrings) const
  QString formatValue(
      const QSqlField &field,
      bool trimStrings) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSqlDriverCall6 call = reinterpret_cast<CuteQSqlDriverCall6>(taken[6]);
      QString * given = call(this, &field, trimStrings, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlDriver::formatValue(field, trimStrings);
  }

  //  QString QSqlDriver::escapeIdentifier(const QString &identifier,
  //      IdentifierType type) const
  QString escapeIdentifier(
      const QString &identifier,
      QSqlDriver::IdentifierType type) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSqlDriverCall7 call = reinterpret_cast<CuteQSqlDriverCall7>(taken[7]);
      QString * given = call(this, &identifier, static_cast<int>(type), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlDriver::escapeIdentifier(identifier, type);
  }

  //  QString QSqlDriver::sqlStatement(StatementType type, const QString
  //      &tableName, const QSqlRecord &rec, bool preparedStatement) const
  QString sqlStatement(
      QSqlDriver::StatementType type,
      const QString &tableName,
      const QSqlRecord &rec,
      bool preparedStatement) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSqlDriverCall8 call = reinterpret_cast<CuteQSqlDriverCall8>(taken[8]);
      QString * given = call(this, static_cast<int>(type), &tableName, &rec, preparedStatement, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlDriver::sqlStatement(type, tableName, rec, preparedStatement);
  }

  //  QVariant QSqlDriver::handle() const
  QVariant handle() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSqlDriverCall9 call = reinterpret_cast<CuteQSqlDriverCall9>(taken[9]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlDriver::handle();
  }

  //  bool QSqlDriver::hasFeature(DriverFeature f) const
  bool hasFeature(QSqlDriver::DriverFeature f) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSqlDriverCall10 call = reinterpret_cast<CuteQSqlDriverCall10>(taken[10]);
      bool given = call(this, static_cast<int>(f), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSqlDriver::close()
  void close() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSqlDriverCall11 call = reinterpret_cast<CuteQSqlDriverCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QSqlResult *QSqlDriver::createResult() const
  QSqlResult *createResult() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSqlDriverCall12 call = reinterpret_cast<CuteQSqlDriverCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSqlResult *>(given);
    }
    return {};
  }

  //  bool QSqlDriver::open(const QString &db, const QString &user, const
  //      QString &password, const QString &host, int port, const QString
  //      &connOpts)
  bool open(
      const QString &db,
      const QString &user,
      const QString &password,
      const QString &host,
      int port,
      const QString &connOpts) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSqlDriverCall13 call = reinterpret_cast<CuteQSqlDriverCall13>(taken[13]);
      bool given = call(this, &db, &user, &password, &host, port, &connOpts, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSqlDriver::subscribeToNotification(const QString &name)
  bool subscribeToNotification(const QString &name) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSqlDriverCall14 call = reinterpret_cast<CuteQSqlDriverCall14>(taken[14]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QSqlDriver::subscribeToNotification(name);
  }

  //  bool QSqlDriver::unsubscribeFromNotification(const QString &name)
  bool unsubscribeFromNotification(const QString &name) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSqlDriverCall15 call = reinterpret_cast<CuteQSqlDriverCall15>(taken[15]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QSqlDriver::unsubscribeFromNotification(name);
  }

  //  bool QSqlDriver::isIdentifierEscaped(const QString &identifier,
  //      IdentifierType type) const
  bool isIdentifierEscaped(
      const QString &identifier,
      QSqlDriver::IdentifierType type) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSqlDriverCall16 call = reinterpret_cast<CuteQSqlDriverCall16>(taken[16]);
      bool given = call(this, &identifier, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return QSqlDriver::isIdentifierEscaped(identifier, type);
  }

  //  QString QSqlDriver::stripDelimiters(const QString &identifier,
  //      IdentifierType type) const
  QString stripDelimiters(
      const QString &identifier,
      QSqlDriver::IdentifierType type) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSqlDriverCall17 call = reinterpret_cast<CuteQSqlDriverCall17>(taken[17]);
      QString * given = call(this, &identifier, static_cast<int>(type), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlDriver::stripDelimiters(identifier, type);
  }

  //  int QSqlDriver::maximumIdentifierLength(IdentifierType type) const
  int maximumIdentifierLength(
      QSqlDriver::IdentifierType type) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSqlDriverCall18 call = reinterpret_cast<CuteQSqlDriverCall18>(taken[18]);
      int given = call(this, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return QSqlDriver::maximumIdentifierLength(type);
  }

  //  bool QSqlDriver::cancelQuery()
  bool cancelQuery() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSqlDriverCall19 call = reinterpret_cast<CuteQSqlDriverCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::cancelQuery();
  }

  //  void QSqlDriver::setOpen(bool o)
  void setOpen(bool o) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSqlDriverCall20 call = reinterpret_cast<CuteQSqlDriverCall20>(taken[20]);
      call(this, o, &handled);
      if (handled) return;
    }
    QSqlDriver::setOpen(o);
  }

  //  void QSqlDriver::setOpenError(bool e)
  void setOpenError(bool e) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSqlDriverCall21 call = reinterpret_cast<CuteQSqlDriverCall21>(taken[21]);
      call(this, e, &handled);
      if (handled) return;
    }
    QSqlDriver::setOpenError(e);
  }

  //  void QSqlDriver::setLastError(const QSqlError &e)
  void setLastError(const QSqlError &e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSqlDriverCall22 call = reinterpret_cast<CuteQSqlDriverCall22>(taken[22]);
      call(this, &e, &handled);
      if (handled) return;
    }
    QSqlDriver::setLastError(e);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSqlDriverCall23 call = reinterpret_cast<CuteQSqlDriverCall23>(taken[23]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSqlDriverCall24 call = reinterpret_cast<CuteQSqlDriverCall24>(taken[24]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSqlDriverCall25 call = reinterpret_cast<CuteQSqlDriverCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSqlDriverCall26 call = reinterpret_cast<CuteQSqlDriverCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSqlDriverCall27 call = reinterpret_cast<CuteQSqlDriverCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSqlDriverCall28 call = reinterpret_cast<CuteQSqlDriverCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSqlDriverCall29 call = reinterpret_cast<CuteQSqlDriverCall29>(taken[29]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSqlDriver::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QSqlDriver10metaObjectEv(
    const QSqlDriver *self) {
  return self->metaObject();
}

//  QString QSqlDriver::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSqlDriver2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSqlDriver::tr(s, c, n));
}

//  QSqlDriverPrivate *QSqlDriver::d_func()
extern "C" Q_DECL_EXPORT
QSqlDriverPrivate *ritual_ZN10QSqlDriver6d_funcEv(QSqlDriver *self) {
  return self->d_func();
}

//  const QSqlDriverPrivate *QSqlDriver::d_func() const
extern "C" Q_DECL_EXPORT
const QSqlDriverPrivate *ritual_ZNK10QSqlDriver6d_funcEv(
    const QSqlDriver *self) {
  return self->d_func();
}

//  QSqlDriver::~QSqlDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlDriverD1Ev(QSqlDriver *self) {
  delete self;
}

//  bool QSqlDriver::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlDriver6isOpenEv(const QSqlDriver *self) {
  return self->isOpen();
}

//  bool QSqlDriver::isOpenError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlDriver11isOpenErrorEv(const QSqlDriver *self) {
  return self->isOpenError();
}

//  bool QSqlDriver::beginTransaction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlDriver16beginTransactionEv(QSqlDriver *self) {
  return self->beginTransaction();
}

//  bool QSqlDriver::commitTransaction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlDriver17commitTransactionEv(QSqlDriver *self) {
  return self->commitTransaction();
}

//  bool QSqlDriver::rollbackTransaction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlDriver19rollbackTransactionEv(QSqlDriver *self) {
  return self->rollbackTransaction();
}

//  QStringList QSqlDriver::tables(QSql::TableType tableType) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QSqlDriver6tablesEN4QSql9TableTypeE(
    const QSqlDriver *self,
    QSql::TableType tableType) {
  return new QList<QString>(self->tables(tableType));
}

//  QSqlIndex QSqlDriver::primaryIndex(const QString &tableName) const
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZNK10QSqlDriver12primaryIndexERK7QString(
    const QSqlDriver *self,
    const QString *tableName) {
  return new QSqlIndex(self->primaryIndex(*tableName));
}

//  QSqlRecord QSqlDriver::record(const QString &tableName) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK10QSqlDriver6recordERK7QString(
    const QSqlDriver *self,
    const QString *tableName) {
  return new QSqlRecord(self->record(*tableName));
}

//  QString QSqlDriver::formatValue(const QSqlField &field, bool trimStrings)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlDriver11formatValueERK9QSqlFieldb(
    const QSqlDriver *self,
    const QSqlField *field,
    bool trimStrings) {
  return new QString(self->formatValue(*field, trimStrings));
}

//  QString QSqlDriver::escapeIdentifier(const QString &identifier,
//      IdentifierType type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlDriver16escapeIdentifierERK7QStringNS_14IdentifierTypeE(
    const QSqlDriver *self,
    const QString *identifier,
    QSqlDriver::IdentifierType type) {
  return new QString(self->escapeIdentifier(*identifier, type));
}

//  QString QSqlDriver::sqlStatement(StatementType type, const QString
//      &tableName, const QSqlRecord &rec, bool preparedStatement) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlDriver12sqlStatementENS_13StatementTypeERK7QStringRK10QSqlRecordb(
    const QSqlDriver *self,
    QSqlDriver::StatementType type,
    const QString *tableName,
    const QSqlRecord *rec,
    bool preparedStatement) {
  return new QString(
      self->sqlStatement(
          type,
          *tableName,
          *rec,
          preparedStatement));
}

//  QSqlError QSqlDriver::lastError() const
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZNK10QSqlDriver9lastErrorEv(const QSqlDriver *self) {
  return new QSqlError(self->lastError());
}

//  QVariant QSqlDriver::handle() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QSqlDriver6handleEv(const QSqlDriver *self) {
  return new QVariant(self->handle());
}

//  bool QSqlDriver::hasFeature(DriverFeature f) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlDriver10hasFeatureENS_13DriverFeatureE(
    const QSqlDriver *self,
    QSqlDriver::DriverFeature f) {
  return self->hasFeature(f);
}

//  void QSqlDriver::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlDriver5closeEv(QSqlDriver *self) {
  self->close();
}

//  QSqlResult *QSqlDriver::createResult() const
extern "C" Q_DECL_EXPORT
QSqlResult *ritual_ZNK10QSqlDriver12createResultEv(const QSqlDriver *self) {
  return self->createResult();
}

//  bool QSqlDriver::open(const QString &db, const QString &user, const
//      QString &password, const QString &host, int port, const QString
//      &connOpts)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlDriver4openERK7QStringS2_S2_S2_iS2_(
    QSqlDriver *self,
    const QString *db,
    const QString *user,
    const QString *password,
    const QString *host,
    int port,
    const QString *connOpts) {
  return self->open(*db, *user, *password, *host, port, *connOpts);
}

//  bool QSqlDriver::subscribeToNotification(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlDriver23subscribeToNotificationERK7QString(
    QSqlDriver *self,
    const QString *name) {
  return self->subscribeToNotification(*name);
}

//  bool QSqlDriver::unsubscribeFromNotification(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlDriver27unsubscribeFromNotificationERK7QString(
    QSqlDriver *self,
    const QString *name) {
  return self->unsubscribeFromNotification(*name);
}

//  QStringList QSqlDriver::subscribedToNotifications() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QSqlDriver25subscribedToNotificationsEv(
    const QSqlDriver *self) {
  return new QList<QString>(self->subscribedToNotifications());
}

//  bool QSqlDriver::isIdentifierEscaped(const QString &identifier,
//      IdentifierType type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlDriver19isIdentifierEscapedERK7QStringNS_14IdentifierTypeE(
    const QSqlDriver *self,
    const QString *identifier,
    QSqlDriver::IdentifierType type) {
  return self->isIdentifierEscaped(*identifier, type);
}

//  QString QSqlDriver::stripDelimiters(const QString &identifier,
//      IdentifierType type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlDriver15stripDelimitersERK7QStringNS_14IdentifierTypeE(
    const QSqlDriver *self,
    const QString *identifier,
    QSqlDriver::IdentifierType type) {
  return new QString(self->stripDelimiters(*identifier, type));
}

//  void
//      QSqlDriver::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolic
//      y precisionPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlDriver27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE(
    QSqlDriver *self,
    QSql::NumericalPrecisionPolicy precisionPolicy) {
  self->setNumericalPrecisionPolicy(precisionPolicy);
}

//  QSql::NumericalPrecisionPolicy QSqlDriver::numericalPrecisionPolicy()
//      const
extern "C" Q_DECL_EXPORT
QSql::NumericalPrecisionPolicy ritual_ZNK10QSqlDriver24numericalPrecisionPolicyEv(
    const QSqlDriver *self) {
  return self->numericalPrecisionPolicy();
}

//  DbmsType QSqlDriver::dbmsType() const
extern "C" Q_DECL_EXPORT
QSqlDriver::DbmsType ritual_ZNK10QSqlDriver8dbmsTypeEv(
    const QSqlDriver *self) {
  return self->dbmsType();
}

//  int QSqlDriver::maximumIdentifierLength(IdentifierType type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSqlDriver23maximumIdentifierLengthENS_14IdentifierTypeE(
    const QSqlDriver *self,
    QSqlDriver::IdentifierType type) {
  return self->maximumIdentifierLength(type);
}

//  QString QSqlDriver::connectionName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlDriver14connectionNameEv(const QSqlDriver *self) {
  return new QString(self->connectionName());
}

//  bool QSqlDriver::cancelQuery()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSqlDriver11cancelQueryEv(QSqlDriver *self) {
  return self->cancelQuery();
}

//  void QSqlDriver::setOpen(bool o)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlDriver7setOpenEb(QSqlDriver *self, bool o) {
  self->setOpen(o);
}

//  void QSqlDriver::setOpenError(bool e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlDriver12setOpenErrorEb(QSqlDriver *self, bool e) {
  self->setOpenError(e);
}

//  void QSqlDriver::setLastError(const QSqlError &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlDriver12setLastErrorERK9QSqlError(
    QSqlDriver *self,
    const QSqlError *e) {
  self->setLastError(*e);
}

//  a Python function taken by a CuteQSqlDriver, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlDriver(QSqlDriver *self, const char *key, void *call) {
  return static_cast<CuteQSqlDriver *>(self)->take(key, call);
}

//  bool QSqlDriver::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QSqlDriver6isOpenEv(const QSqlDriver *self) {
  return self->QSqlDriver::isOpen();
}

//  bool QSqlDriver::beginTransaction()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlDriver16beginTransactionEv(QSqlDriver *self) {
  return self->QSqlDriver::beginTransaction();
}

//  bool QSqlDriver::commitTransaction()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlDriver17commitTransactionEv(QSqlDriver *self) {
  return self->QSqlDriver::commitTransaction();
}

//  bool QSqlDriver::rollbackTransaction()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlDriver19rollbackTransactionEv(QSqlDriver *self) {
  return self->QSqlDriver::rollbackTransaction();
}

//  QSqlIndex QSqlDriver::primaryIndex(const QString &tableName) const
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_own_ZNK10QSqlDriver12primaryIndexERK7QString(
    const QSqlDriver *self,
    const QString *tableName) {
  return new QSqlIndex(self->QSqlDriver::primaryIndex(*tableName));
}

//  QSqlRecord QSqlDriver::record(const QString &tableName) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_own_ZNK10QSqlDriver6recordERK7QString(
    const QSqlDriver *self,
    const QString *tableName) {
  return new QSqlRecord(self->QSqlDriver::record(*tableName));
}

//  QString QSqlDriver::formatValue(const QSqlField &field, bool trimStrings)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK10QSqlDriver11formatValueERK9QSqlFieldb(
    const QSqlDriver *self,
    const QSqlField *field,
    bool trimStrings) {
  return new QString(self->QSqlDriver::formatValue(*field, trimStrings));
}

//  QString QSqlDriver::escapeIdentifier(const QString &identifier,
//      IdentifierType type) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK10QSqlDriver16escapeIdentifierERK7QStringNS_14IdentifierTypeE(
    const QSqlDriver *self,
    const QString *identifier,
    QSqlDriver::IdentifierType type) {
  return new QString(self->QSqlDriver::escapeIdentifier(*identifier, type));
}

//  QString QSqlDriver::sqlStatement(StatementType type, const QString
//      &tableName, const QSqlRecord &rec, bool preparedStatement) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK10QSqlDriver12sqlStatementENS_13StatementTypeERK7QStringRK10QSqlRecordb(
    const QSqlDriver *self,
    QSqlDriver::StatementType type,
    const QString *tableName,
    const QSqlRecord *rec,
    bool preparedStatement) {
  return new QString(
      self->QSqlDriver::sqlStatement(
          type,
          *tableName,
          *rec,
          preparedStatement));
}

//  QVariant QSqlDriver::handle() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK10QSqlDriver6handleEv(const QSqlDriver *self) {
  return new QVariant(self->QSqlDriver::handle());
}

//  bool QSqlDriver::subscribeToNotification(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlDriver23subscribeToNotificationERK7QString(
    QSqlDriver *self,
    const QString *name) {
  return self->QSqlDriver::subscribeToNotification(*name);
}

//  bool QSqlDriver::unsubscribeFromNotification(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlDriver27unsubscribeFromNotificationERK7QString(
    QSqlDriver *self,
    const QString *name) {
  return self->QSqlDriver::unsubscribeFromNotification(*name);
}

//  bool QSqlDriver::isIdentifierEscaped(const QString &identifier,
//      IdentifierType type) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QSqlDriver19isIdentifierEscapedERK7QStringNS_14IdentifierTypeE(
    const QSqlDriver *self,
    const QString *identifier,
    QSqlDriver::IdentifierType type) {
  return self->QSqlDriver::isIdentifierEscaped(*identifier, type);
}

//  QString QSqlDriver::stripDelimiters(const QString &identifier,
//      IdentifierType type) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK10QSqlDriver15stripDelimitersERK7QStringNS_14IdentifierTypeE(
    const QSqlDriver *self,
    const QString *identifier,
    QSqlDriver::IdentifierType type) {
  return new QString(self->QSqlDriver::stripDelimiters(*identifier, type));
}

//  int QSqlDriver::maximumIdentifierLength(IdentifierType type) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QSqlDriver23maximumIdentifierLengthENS_14IdentifierTypeE(
    const QSqlDriver *self,
    QSqlDriver::IdentifierType type) {
  return self->QSqlDriver::maximumIdentifierLength(type);
}

//  bool QSqlDriver::cancelQuery()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSqlDriver11cancelQueryEv(QSqlDriver *self) {
  return self->QSqlDriver::cancelQuery();
}

//  void QSqlDriver::setOpen(bool o)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlDriver7setOpenEb(QSqlDriver *self, bool o) {
  static_cast<OwnQSqlDriver *>(self)->OwnQSqlDriver::setOpen(o);
}

//  void QSqlDriver::setOpenError(bool e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlDriver12setOpenErrorEb(QSqlDriver *self, bool e) {
  static_cast<OwnQSqlDriver *>(self)->OwnQSqlDriver::setOpenError(e);
}

//  void QSqlDriver::setLastError(const QSqlError &e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSqlDriver12setLastErrorERK9QSqlError(
    QSqlDriver *self,
    const QSqlError *e) {
  static_cast<OwnQSqlDriver *>(self)->OwnQSqlDriver::setLastError(*e);
}
