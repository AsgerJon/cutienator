//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineclienthints.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebengineclienthints.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QWebEngineClientHints that Python can take functions over in. Every QWebEngineClientHints
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineClientHintsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineClientHintsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineClientHintsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineClientHintsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineClientHintsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineClientHintsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineClientHintsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineClientHints : public QWebEngineClientHints {
public:
  using QWebEngineClientHints::QWebEngineClientHints;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEngineClientHintsCall0 call = reinterpret_cast<CuteQWebEngineClientHintsCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEngineClientHintsCall1 call = reinterpret_cast<CuteQWebEngineClientHintsCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebEngineClientHintsCall2 call = reinterpret_cast<CuteQWebEngineClientHintsCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebEngineClientHintsCall3 call = reinterpret_cast<CuteQWebEngineClientHintsCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebEngineClientHintsCall4 call = reinterpret_cast<CuteQWebEngineClientHintsCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebEngineClientHintsCall5 call = reinterpret_cast<CuteQWebEngineClientHintsCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebEngineClientHintsCall6 call = reinterpret_cast<CuteQWebEngineClientHintsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineClientHints::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QWebEngineClientHints10metaObjectEv(
    const QWebEngineClientHints *self) {
  return self->metaObject();
}

//  void *QWebEngineClientHints::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QWebEngineClientHints11qt_metacastEPKc(
    QWebEngineClientHints *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineClientHints::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QWebEngineClientHints11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineClientHints *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineClientHints::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QWebEngineClientHints2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineClientHints::tr(s, c, n));
}

//  QWebEngineClientHints::~QWebEngineClientHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHintsD1Ev(QWebEngineClientHints *self) {
  delete self;
}

//  QString QWebEngineClientHints::arch() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineClientHints4archEv(
    const QWebEngineClientHints *self) {
  return new QString(self->arch());
}

//  QString QWebEngineClientHints::platform() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineClientHints8platformEv(
    const QWebEngineClientHints *self) {
  return new QString(self->platform());
}

//  QString QWebEngineClientHints::model() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineClientHints5modelEv(
    const QWebEngineClientHints *self) {
  return new QString(self->model());
}

//  bool QWebEngineClientHints::isMobile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineClientHints8isMobileEv(
    const QWebEngineClientHints *self) {
  return self->isMobile();
}

//  QString QWebEngineClientHints::fullVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineClientHints11fullVersionEv(
    const QWebEngineClientHints *self) {
  return new QString(self->fullVersion());
}

//  QString QWebEngineClientHints::platformVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineClientHints15platformVersionEv(
    const QWebEngineClientHints *self) {
  return new QString(self->platformVersion());
}

//  QString QWebEngineClientHints::bitness() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineClientHints7bitnessEv(
    const QWebEngineClientHints *self) {
  return new QString(self->bitness());
}

//  QVariantMap QWebEngineClientHints::fullVersionList() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK21QWebEngineClientHints15fullVersionListEv(
    const QWebEngineClientHints *self) {
  return new QMap<QString, QVariant>(self->fullVersionList());
}

//  bool QWebEngineClientHints::isWow64() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineClientHints7isWow64Ev(
    const QWebEngineClientHints *self) {
  return self->isWow64();
}

//  QStringList QWebEngineClientHints::formFactors() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QWebEngineClientHints11formFactorsEv(
    const QWebEngineClientHints *self) {
  return new QList<QString>(self->formFactors());
}

//  void QWebEngineClientHints::setArch(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints7setArchERK7QString(
    QWebEngineClientHints *self,
    const QString *a0) {
  self->setArch(*a0);
}

//  void QWebEngineClientHints::setPlatform(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints11setPlatformERK7QString(
    QWebEngineClientHints *self,
    const QString *a0) {
  self->setPlatform(*a0);
}

//  void QWebEngineClientHints::setModel(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints8setModelERK7QString(
    QWebEngineClientHints *self,
    const QString *a0) {
  self->setModel(*a0);
}

//  void QWebEngineClientHints::setIsMobile(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints11setIsMobileEb(
    QWebEngineClientHints *self,
    bool a0) {
  self->setIsMobile(a0);
}

//  void QWebEngineClientHints::setFullVersion(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints14setFullVersionERK7QString(
    QWebEngineClientHints *self,
    const QString *a0) {
  self->setFullVersion(*a0);
}

//  void QWebEngineClientHints::setPlatformVersion(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints18setPlatformVersionERK7QString(
    QWebEngineClientHints *self,
    const QString *a0) {
  self->setPlatformVersion(*a0);
}

//  void QWebEngineClientHints::setBitness(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints10setBitnessERK7QString(
    QWebEngineClientHints *self,
    const QString *a0) {
  self->setBitness(*a0);
}

//  void QWebEngineClientHints::setFullVersionList(const QVariantMap &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints18setFullVersionListERK4QMapI7QString8QVariantE(
    QWebEngineClientHints *self,
    const QMap<QString, QVariant> *a0) {
  self->setFullVersionList(*a0);
}

//  void QWebEngineClientHints::setIsWow64(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints10setIsWow64Eb(
    QWebEngineClientHints *self,
    bool a0) {
  self->setIsWow64(a0);
}

//  void QWebEngineClientHints::setFormFactors(const QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints14setFormFactorsERK5QListI7QStringE(
    QWebEngineClientHints *self,
    const QList<QString> *a0) {
  self->setFormFactors(*a0);
}

//  bool QWebEngineClientHints::isAllClientHintsEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QWebEngineClientHints23isAllClientHintsEnabledEv(
    QWebEngineClientHints *self) {
  return self->isAllClientHintsEnabled();
}

//  void QWebEngineClientHints::setAllClientHintsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints24setAllClientHintsEnabledEb(
    QWebEngineClientHints *self,
    bool enabled) {
  self->setAllClientHintsEnabled(enabled);
}

//  void QWebEngineClientHints::resetAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineClientHints8resetAllEv(
    QWebEngineClientHints *self) {
  self->resetAll();
}

//  QWebEngineClientHints::QWebEngineClientHints(QtWebEngineCore::ProfileAdap
//      ter *profileAdapter)
extern "C" Q_DECL_EXPORT
QWebEngineClientHints *ritual_ZN21QWebEngineClientHintsC1EPN15QtWebEngineCore14ProfileAdapterE(
    QtWebEngineCore::ProfileAdapter *profileAdapter) {
  return new CuteQWebEngineClientHints(profileAdapter);
}

//  a Python function taken by a CuteQWebEngineClientHints, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineClientHints(
    QWebEngineClientHints *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineClientHints *>(self)->take(key, call);
}
