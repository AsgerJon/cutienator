//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqlnulldriver_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqlnulldriver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtSql/qsqlerror.h>
#include <QtSql/qsqlindex.h>
#include <QtSql/qsqlrecord.h>
#include <QtSql/qsqlfield.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSqlNullDriver may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlNullDriver : QSqlNullDriver {
  using QSqlNullDriver::setOpen;
  using QSqlNullDriver::setOpenError;
  using QSqlNullDriver::setLastError;
};

//  A QSqlNullDriver that Python can take functions over in. Every QSqlNullDriver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSqlNullDriverCall0)(const void *, int, int *);
typedef bool (*CuteQSqlNullDriverCall1)(const void *, const QString *, const QString *, const QString *, const QString *, int, const QString *, int *);
typedef void (*CuteQSqlNullDriverCall2)(const void *, int *);
typedef void * (*CuteQSqlNullDriverCall3)(const void *, int *);
typedef void (*CuteQSqlNullDriverCall4)(const void *, bool, int *);
typedef void (*CuteQSqlNullDriverCall5)(const void *, bool, int *);
typedef void (*CuteQSqlNullDriverCall6)(const void *, const QSqlError *, int *);
typedef bool (*CuteQSqlNullDriverCall7)(const void *, int *);
typedef bool (*CuteQSqlNullDriverCall8)(const void *, int *);
typedef bool (*CuteQSqlNullDriverCall9)(const void *, int *);
typedef bool (*CuteQSqlNullDriverCall10)(const void *, int *);
typedef const QSqlIndex * (*CuteQSqlNullDriverCall11)(const void *, const QString *, int *);
typedef const QSqlRecord * (*CuteQSqlNullDriverCall12)(const void *, const QString *, int *);
typedef QString * (*CuteQSqlNullDriverCall13)(const void *, const QSqlField *, bool, int *);
typedef QString * (*CuteQSqlNullDriverCall14)(const void *, const QString *, int, int *);
typedef QString * (*CuteQSqlNullDriverCall15)(const void *, int, const QString *, const QSqlRecord *, bool, int *);
typedef const QVariant * (*CuteQSqlNullDriverCall16)(const void *, int *);
typedef bool (*CuteQSqlNullDriverCall17)(const void *, const QString *, int *);
typedef bool (*CuteQSqlNullDriverCall18)(const void *, const QString *, int *);
typedef bool (*CuteQSqlNullDriverCall19)(const void *, const QString *, int, int *);
typedef QString * (*CuteQSqlNullDriverCall20)(const void *, const QString *, int, int *);
typedef int (*CuteQSqlNullDriverCall21)(const void *, int, int *);
typedef bool (*CuteQSqlNullDriverCall22)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlNullDriverCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlNullDriverCall24)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlNullDriverCall25)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlNullDriverCall26)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlNullDriverCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlNullDriverCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlNullDriverCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSqlNullDriver : public QSqlNullDriver {
public:
  using QSqlNullDriver::QSqlNullDriver;
  void *taken[30] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSqlDriver10hasFeatureENS_13DriverFeatureE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver4openERK7QStringS2_S2_S2_iS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver5closeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver12createResultEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver7setOpenEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver12setOpenErrorEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver12setLastErrorERK9QSqlError")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver6isOpenEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver16beginTransactionEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver17commitTransactionEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver19rollbackTransactionEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver12primaryIndexERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver6recordERK7QString")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver11formatValueERK9QSqlFieldb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver16escapeIdentifierERK7QStringNS_14IdentifierTypeE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver12sqlStatementENS_13StatementTypeERK7QStringRK10QSqlRecordb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver6handleEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver23subscribeToNotificationERK7QString")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver27unsubscribeFromNotificationERK7QString")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver19isIdentifierEscapedERK7QStringNS_14IdentifierTypeE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver15stripDelimitersERK7QStringNS_14IdentifierTypeE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSqlDriver23maximumIdentifierLengthENS_14IdentifierTypeE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSqlDriver11cancelQueryEv")) {
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

  //  bool QSqlNullDriver::hasFeature(DriverFeature a0) const
  bool hasFeature(QSqlDriver::DriverFeature a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlNullDriverCall0 call = reinterpret_cast<CuteQSqlNullDriverCall0>(taken[0]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QSqlNullDriver::hasFeature(a0);
  }

  //  bool QSqlNullDriver::open(const QString &a0, const QString &a1, const
  //      QString &a2, const QString &a3, int a4, const QString &a5)
  bool open(
      const QString &a0,
      const QString &a1,
      const QString &a2,
      const QString &a3,
      int a4,
      const QString &a5) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlNullDriverCall1 call = reinterpret_cast<CuteQSqlNullDriverCall1>(taken[1]);
      bool given = call(this, &a0, &a1, &a2, &a3, a4, &a5, &handled);
      if (handled) return given;
    }
    return QSqlNullDriver::open(a0, a1, a2, a3, a4, a5);
  }

  //  void QSqlNullDriver::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlNullDriverCall2 call = reinterpret_cast<CuteQSqlNullDriverCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlNullDriver::close();
  }

  //  QSqlResult *QSqlNullDriver::createResult() const
  QSqlResult *createResult() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlNullDriverCall3 call = reinterpret_cast<CuteQSqlNullDriverCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSqlResult *>(given);
    }
    return QSqlNullDriver::createResult();
  }

  //  void QSqlNullDriver::setOpen(bool a0)
  void setOpen(bool a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSqlNullDriverCall4 call = reinterpret_cast<CuteQSqlNullDriverCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSqlNullDriver::setOpen(a0);
  }

  //  void QSqlNullDriver::setOpenError(bool a0)
  void setOpenError(bool a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSqlNullDriverCall5 call = reinterpret_cast<CuteQSqlNullDriverCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSqlNullDriver::setOpenError(a0);
  }

  //  void QSqlNullDriver::setLastError(const QSqlError &a0)
  void setLastError(const QSqlError &a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSqlNullDriverCall6 call = reinterpret_cast<CuteQSqlNullDriverCall6>(taken[6]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSqlNullDriver::setLastError(a0);
  }

  //  bool QSqlDriver::isOpen() const
  bool isOpen() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSqlNullDriverCall7 call = reinterpret_cast<CuteQSqlNullDriverCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::isOpen();
  }

  //  bool QSqlDriver::beginTransaction()
  bool beginTransaction() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSqlNullDriverCall8 call = reinterpret_cast<CuteQSqlNullDriverCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::beginTransaction();
  }

  //  bool QSqlDriver::commitTransaction()
  bool commitTransaction() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSqlNullDriverCall9 call = reinterpret_cast<CuteQSqlNullDriverCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::commitTransaction();
  }

  //  bool QSqlDriver::rollbackTransaction()
  bool rollbackTransaction() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSqlNullDriverCall10 call = reinterpret_cast<CuteQSqlNullDriverCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::rollbackTransaction();
  }

  //  QSqlIndex QSqlDriver::primaryIndex(const QString &tableName) const
  QSqlIndex primaryIndex(const QString &tableName) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSqlNullDriverCall11 call = reinterpret_cast<CuteQSqlNullDriverCall11>(taken[11]);
      const QSqlIndex * given = call(this, &tableName, &handled);
      if (handled && given) return *given;
    }
    return QSqlDriver::primaryIndex(tableName);
  }

  //  QSqlRecord QSqlDriver::record(const QString &tableName) const
  QSqlRecord record(const QString &tableName) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSqlNullDriverCall12 call = reinterpret_cast<CuteQSqlNullDriverCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQSqlNullDriverCall13 call = reinterpret_cast<CuteQSqlNullDriverCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQSqlNullDriverCall14 call = reinterpret_cast<CuteQSqlNullDriverCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQSqlNullDriverCall15 call = reinterpret_cast<CuteQSqlNullDriverCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQSqlNullDriverCall16 call = reinterpret_cast<CuteQSqlNullDriverCall16>(taken[16]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSqlDriver::handle();
  }

  //  bool QSqlDriver::subscribeToNotification(const QString &name)
  bool subscribeToNotification(const QString &name) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSqlNullDriverCall17 call = reinterpret_cast<CuteQSqlNullDriverCall17>(taken[17]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QSqlDriver::subscribeToNotification(name);
  }

  //  bool QSqlDriver::unsubscribeFromNotification(const QString &name)
  bool unsubscribeFromNotification(const QString &name) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSqlNullDriverCall18 call = reinterpret_cast<CuteQSqlNullDriverCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQSqlNullDriverCall19 call = reinterpret_cast<CuteQSqlNullDriverCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQSqlNullDriverCall20 call = reinterpret_cast<CuteQSqlNullDriverCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQSqlNullDriverCall21 call = reinterpret_cast<CuteQSqlNullDriverCall21>(taken[21]);
      int given = call(this, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return QSqlDriver::maximumIdentifierLength(type);
  }

  //  bool QSqlDriver::cancelQuery()
  bool cancelQuery() override {
    if (taken[22]) {
      int handled = 0;
      CuteQSqlNullDriverCall22 call = reinterpret_cast<CuteQSqlNullDriverCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlDriver::cancelQuery();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSqlNullDriverCall23 call = reinterpret_cast<CuteQSqlNullDriverCall23>(taken[23]);
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
      CuteQSqlNullDriverCall24 call = reinterpret_cast<CuteQSqlNullDriverCall24>(taken[24]);
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
      CuteQSqlNullDriverCall25 call = reinterpret_cast<CuteQSqlNullDriverCall25>(taken[25]);
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
      CuteQSqlNullDriverCall26 call = reinterpret_cast<CuteQSqlNullDriverCall26>(taken[26]);
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
      CuteQSqlNullDriverCall27 call = reinterpret_cast<CuteQSqlNullDriverCall27>(taken[27]);
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
      CuteQSqlNullDriverCall28 call = reinterpret_cast<CuteQSqlNullDriverCall28>(taken[28]);
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
      CuteQSqlNullDriverCall29 call = reinterpret_cast<CuteQSqlNullDriverCall29>(taken[29]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSqlNullDriver::QSqlNullDriver()
extern "C" Q_DECL_EXPORT
QSqlNullDriver *ritual_ZN14QSqlNullDriverC1Ev() {
  return new CuteQSqlNullDriver();
}

//  bool QSqlNullDriver::hasFeature(DriverFeature a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSqlNullDriver10hasFeatureEN10QSqlDriver13DriverFeatureE(
    const QSqlNullDriver *self,
    QSqlDriver::DriverFeature a0) {
  return self->hasFeature(a0);
}

//  bool QSqlNullDriver::open(const QString &a0, const QString &a1, const
//      QString &a2, const QString &a3, int a4, const QString &a5)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlNullDriver4openERK7QStringS2_S2_S2_iS2_(
    QSqlNullDriver *self,
    const QString *a0,
    const QString *a1,
    const QString *a2,
    const QString *a3,
    int a4,
    const QString *a5) {
  return self->open(*a0, *a1, *a2, *a3, a4, *a5);
}

//  void QSqlNullDriver::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullDriver5closeEv(QSqlNullDriver *self) {
  self->close();
}

//  QSqlResult *QSqlNullDriver::createResult() const
extern "C" Q_DECL_EXPORT
QSqlResult *ritual_ZNK14QSqlNullDriver12createResultEv(
    const QSqlNullDriver *self) {
  return self->createResult();
}

//  void QSqlNullDriver::setOpen(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullDriver7setOpenEb(QSqlNullDriver *self, bool a0) {
  self->setOpen(a0);
}

//  void QSqlNullDriver::setOpenError(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullDriver12setOpenErrorEb(
    QSqlNullDriver *self,
    bool a0) {
  self->setOpenError(a0);
}

//  void QSqlNullDriver::setLastError(const QSqlError &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlNullDriver12setLastErrorERK9QSqlError(
    QSqlNullDriver *self,
    const QSqlError *a0) {
  self->setLastError(*a0);
}

//  a Python function taken by a CuteQSqlNullDriver, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlNullDriver(
    QSqlNullDriver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlNullDriver *>(self)->take(key, call);
}

//  bool QSqlNullDriver::hasFeature(DriverFeature a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QSqlNullDriver10hasFeatureEN10QSqlDriver13DriverFeatureE(
    const QSqlNullDriver *self,
    QSqlDriver::DriverFeature a0) {
  return self->QSqlNullDriver::hasFeature(a0);
}

//  bool QSqlNullDriver::open(const QString &a0, const QString &a1, const
//      QString &a2, const QString &a3, int a4, const QString &a5)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlNullDriver4openERK7QStringS2_S2_S2_iS2_(
    QSqlNullDriver *self,
    const QString *a0,
    const QString *a1,
    const QString *a2,
    const QString *a3,
    int a4,
    const QString *a5) {
  return self->QSqlNullDriver::open(*a0, *a1, *a2, *a3, a4, *a5);
}

//  void QSqlNullDriver::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullDriver5closeEv(QSqlNullDriver *self) {
  self->QSqlNullDriver::close();
}

//  QSqlResult *QSqlNullDriver::createResult() const
extern "C" Q_DECL_EXPORT
QSqlResult *ritual_own_ZNK14QSqlNullDriver12createResultEv(
    const QSqlNullDriver *self) {
  return self->QSqlNullDriver::createResult();
}

//  void QSqlNullDriver::setOpen(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullDriver7setOpenEb(QSqlNullDriver *self, bool a0) {
  static_cast<OwnQSqlNullDriver *>(self)->OwnQSqlNullDriver::setOpen(a0);
}

//  void QSqlNullDriver::setOpenError(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullDriver12setOpenErrorEb(
    QSqlNullDriver *self,
    bool a0) {
  static_cast<OwnQSqlNullDriver *>(self)->OwnQSqlNullDriver::setOpenError(
      a0);
}

//  void QSqlNullDriver::setLastError(const QSqlError &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlNullDriver12setLastErrorERK9QSqlError(
    QSqlNullDriver *self,
    const QSqlError *a0) {
  static_cast<OwnQSqlNullDriver *>(self)->OwnQSqlNullDriver::setLastError(
      *a0);
}
