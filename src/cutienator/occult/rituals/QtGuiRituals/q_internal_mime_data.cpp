//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinternalmimedata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qinternalmimedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QInternalMimeData may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQInternalMimeData : QInternalMimeData {
  using QInternalMimeData::retrieveData;
};

//  A QInternalMimeData that Python can take functions over in. Every QInternalMimeData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQInternalMimeDataCall0)(const void *, const QString *, int *);
typedef const QVariant * (*CuteQInternalMimeDataCall1)(const void *, const QString *, const QMetaType *, int *);
typedef bool (*CuteQInternalMimeDataCall2)(const void *, const QString *, int *);
typedef const QVariant * (*CuteQInternalMimeDataCall3)(const void *, const QString *, const QMetaType *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQInternalMimeDataCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQInternalMimeDataCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInternalMimeDataCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInternalMimeDataCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInternalMimeDataCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInternalMimeDataCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInternalMimeDataCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQInternalMimeData : public QInternalMimeData {
public:
  using QInternalMimeData::QInternalMimeData;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QMimeData9hasFormatERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QMimeData12retrieveDataERK7QString9QMetaType")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QInternalMimeData13hasFormat_sysERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QInternalMimeData16retrieveData_sysERK7QString9QMetaType")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QInternalMimeData::hasFormat(const QString &mimeType) const
  bool hasFormat(const QString &mimeType) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQInternalMimeDataCall0 call = reinterpret_cast<CuteQInternalMimeDataCall0>(taken[0]);
      bool given = call(this, &mimeType, &handled);
      if (handled) return given;
    }
    return QInternalMimeData::hasFormat(mimeType);
  }

  //  QVariant QInternalMimeData::retrieveData(const QString &mimeType,
  //      QMetaType type) const
  QVariant retrieveData(
      const QString &mimeType,
      QMetaType type) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQInternalMimeDataCall1 call = reinterpret_cast<CuteQInternalMimeDataCall1>(taken[1]);
      const QVariant * given = call(this, &mimeType, &type, &handled);
      if (handled && given) return *given;
    }
    return QInternalMimeData::retrieveData(mimeType, type);
  }

  //  bool QInternalMimeData::hasFormat_sys(const QString &mimeType) const
  bool hasFormat_sys(const QString &mimeType) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQInternalMimeDataCall2 call = reinterpret_cast<CuteQInternalMimeDataCall2>(taken[2]);
      bool given = call(this, &mimeType, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QVariant QInternalMimeData::retrieveData_sys(const QString &mimeType,
  //      QMetaType type) const
  QVariant retrieveData_sys(
      const QString &mimeType,
      QMetaType type) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQInternalMimeDataCall3 call = reinterpret_cast<CuteQInternalMimeDataCall3>(taken[3]);
      const QVariant * given = call(this, &mimeType, &type, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQInternalMimeDataCall4 call = reinterpret_cast<CuteQInternalMimeDataCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQInternalMimeDataCall5 call = reinterpret_cast<CuteQInternalMimeDataCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQInternalMimeDataCall6 call = reinterpret_cast<CuteQInternalMimeDataCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQInternalMimeDataCall7 call = reinterpret_cast<CuteQInternalMimeDataCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQInternalMimeDataCall8 call = reinterpret_cast<CuteQInternalMimeDataCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQInternalMimeDataCall9 call = reinterpret_cast<CuteQInternalMimeDataCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQInternalMimeDataCall10 call = reinterpret_cast<CuteQInternalMimeDataCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QInternalMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QInternalMimeData10metaObjectEv(
    const QInternalMimeData *self) {
  return self->metaObject();
}

//  void *QInternalMimeData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QInternalMimeData11qt_metacastEPKc(
    QInternalMimeData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QInternalMimeData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QInternalMimeData11qt_metacallEN11QMetaObject4CallEiPPv(
    QInternalMimeData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QInternalMimeData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QInternalMimeData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInternalMimeData::tr(s, c, n));
}

//  QInternalMimeData::~QInternalMimeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QInternalMimeDataD1Ev(QInternalMimeData *self) {
  delete self;
}

//  bool QInternalMimeData::hasFormat(const QString &mimeType) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QInternalMimeData9hasFormatERK7QString(
    const QInternalMimeData *self,
    const QString *mimeType) {
  return self->hasFormat(*mimeType);
}

//  QStringList QInternalMimeData::formats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QInternalMimeData7formatsEv(
    const QInternalMimeData *self) {
  return new QList<QString>(self->formats());
}

//  bool QInternalMimeData::canReadData(const QString &mimeType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QInternalMimeData11canReadDataERK7QString(
    const QString *mimeType) {
  return QInternalMimeData::canReadData(*mimeType);
}

//  QStringList QInternalMimeData::formatsHelper(const QMimeData *data)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN17QInternalMimeData13formatsHelperEPK9QMimeData(
    const QMimeData *data) {
  return new QList<QString>(QInternalMimeData::formatsHelper(data));
}

//  bool QInternalMimeData::hasFormatHelper(const QString &mimeType, const
//      QMimeData *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QInternalMimeData15hasFormatHelperERK7QStringPK9QMimeData(
    const QString *mimeType,
    const QMimeData *data) {
  return QInternalMimeData::hasFormatHelper(*mimeType, data);
}

//  QByteArray QInternalMimeData::renderDataHelper(const QString &mimeType,
//      const QMimeData *data)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QInternalMimeData16renderDataHelperERK7QStringPK9QMimeData(
    const QString *mimeType,
    const QMimeData *data) {
  return new QByteArray(
      QInternalMimeData::renderDataHelper(
          *mimeType,
          data));
}

//  QVariant QInternalMimeData::retrieveData(const QString &mimeType,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QInternalMimeData12retrieveDataERK7QString9QMetaType(
    const QInternalMimeData *self,
    const QString *mimeType,
    const QMetaType *type) {
  return new QVariant(self->retrieveData(*mimeType, *type));
}

//  bool QInternalMimeData::hasFormat_sys(const QString &mimeType) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QInternalMimeData13hasFormat_sysERK7QString(
    const QInternalMimeData *self,
    const QString *mimeType) {
  return self->hasFormat_sys(*mimeType);
}

//  QStringList QInternalMimeData::formats_sys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QInternalMimeData11formats_sysEv(
    const QInternalMimeData *self) {
  return new QList<QString>(self->formats_sys());
}

//  QVariant QInternalMimeData::retrieveData_sys(const QString &mimeType,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QInternalMimeData16retrieveData_sysERK7QString9QMetaType(
    const QInternalMimeData *self,
    const QString *mimeType,
    const QMetaType *type) {
  return new QVariant(self->retrieveData_sys(*mimeType, *type));
}

//  a Python function taken by a CuteQInternalMimeData, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInternalMimeData(
    QInternalMimeData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInternalMimeData *>(self)->take(key, call);
}

//  bool QInternalMimeData::hasFormat(const QString &mimeType) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QInternalMimeData9hasFormatERK7QString(
    const QInternalMimeData *self,
    const QString *mimeType) {
  return self->QInternalMimeData::hasFormat(*mimeType);
}

//  QVariant QInternalMimeData::retrieveData(const QString &mimeType,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QInternalMimeData12retrieveDataERK7QString9QMetaType(
    const QInternalMimeData *self,
    const QString *mimeType,
    const QMetaType *type) {
  return new QVariant(
      static_cast<const OwnQInternalMimeData *>(self)->OwnQInternalMimeData::retrieveData(
          *mimeType,
          *type));
}
