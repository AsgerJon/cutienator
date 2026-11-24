//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsettings.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(settings)
#if !defined(QT_NO_QOBJECT)
#include <QtCore/qsettings.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QSettings may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSettings : QSettings {
  using QSettings::event;
};

//  A QSettings that Python can take functions over in. Every QSettings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(settings)
typedef bool (*CuteQSettingsCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(settings)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSettingsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSettingsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSettingsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSettingsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSettingsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSettingsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSettings : public QSettings {
public:
  using QSettings::QSettings;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(settings)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(settings)
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
#if QT_CONFIG(settings)
  //  bool QSettings::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSettingsCall0 call = reinterpret_cast<CuteQSettingsCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSettings::event(event);
  }
#endif  // QT_CONFIG(settings)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSettingsCall1 call = reinterpret_cast<CuteQSettingsCall1>(taken[1]);
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
      CuteQSettingsCall2 call = reinterpret_cast<CuteQSettingsCall2>(taken[2]);
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
      CuteQSettingsCall3 call = reinterpret_cast<CuteQSettingsCall3>(taken[3]);
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
      CuteQSettingsCall4 call = reinterpret_cast<CuteQSettingsCall4>(taken[4]);
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
      CuteQSettingsCall5 call = reinterpret_cast<CuteQSettingsCall5>(taken[5]);
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
      CuteQSettingsCall6 call = reinterpret_cast<CuteQSettingsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSettings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSettings10metaObjectEv(
    const QSettings *self) {
  return self->metaObject();
}

//  QString QSettings::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSettings2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSettings::tr(s, c, n));
}

#if QT_CONFIG(settings)
//  QSettingsPrivate *QSettings::d_func()
extern "C" Q_DECL_EXPORT
QSettingsPrivate *ritual_ZN9QSettings6d_funcEv(QSettings *self) {
  return self->d_func();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  const QSettingsPrivate *QSettings::d_func() const
extern "C" Q_DECL_EXPORT
const QSettingsPrivate *ritual_ZNK9QSettings6d_funcEv(
    const QSettings *self) {
  return self->d_func();
}
#endif  // QT_CONFIG(settings)

//  QSettings::QSettings(const QString &organization, const QString
//      &application, QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ERK7QStringS2_P7QObject(
    const QString *organization,
    const QString *application,
    QObject *parent) {
  return new CuteQSettings(*organization, *application, parent);
}

//  QSettings::QSettings(Scope scope, const QString &organization, const
//      QString &application, QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ENS_5ScopeERK7QStringS3_P7QObject(
    QSettings::Scope scope,
    const QString *organization,
    const QString *application,
    QObject *parent) {
  return new CuteQSettings(scope, *organization, *application, parent);
}

//  QSettings::QSettings(Format format, Scope scope, const QString
//      &organization, const QString &application, QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ENS_6FormatENS_5ScopeERK7QStringS4_P7QObject(
    QSettings::Format format,
    QSettings::Scope scope,
    const QString *organization,
    const QString *application,
    QObject *parent) {
  return new CuteQSettings(
      format,
      scope,
      *organization,
      *application,
      parent);
}

//  QSettings::QSettings(const QString &fileName, Format format, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ERK7QStringNS_6FormatEP7QObject(
    const QString *fileName,
    QSettings::Format format,
    QObject *parent) {
  return new CuteQSettings(*fileName, format, parent);
}

//  QSettings::QSettings(QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1EP7QObject(QObject *parent) {
  return new CuteQSettings(parent);
}

//  QSettings::QSettings(Scope scope, QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ENS_5ScopeEP7QObject(
    QSettings::Scope scope,
    QObject *parent) {
  return new CuteQSettings(scope, parent);
}

#if QT_CONFIG(settings)
//  QSettings::~QSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettingsD1Ev(QSettings *self) {
  delete self;
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings5clearEv(QSettings *self) {
  self->clear();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings4syncEv(QSettings *self) {
  self->sync();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  Status QSettings::status() const
extern "C" Q_DECL_EXPORT
QSettings::Status ritual_ZNK9QSettings6statusEv(const QSettings *self) {
  return self->status();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  bool QSettings::isAtomicSyncRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings20isAtomicSyncRequiredEv(const QSettings *self) {
  return self->isAtomicSyncRequired();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::setAtomicSyncRequired(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings21setAtomicSyncRequiredEb(
    QSettings *self,
    bool enable) {
  self->setAtomicSyncRequired(enable);
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::beginGroup(QAnyStringView prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings10beginGroupE14QAnyStringView(
    QSettings *self,
    const QString *prefix) {
  self->beginGroup(QAnyStringView(*prefix));
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::endGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings8endGroupEv(QSettings *self) {
  self->endGroup();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QString QSettings::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings5groupEv(const QSettings *self) {
  return new QString(self->group());
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  int QSettings::beginReadArray(QAnyStringView prefix)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QSettings14beginReadArrayE14QAnyStringView(
    QSettings *self,
    const QString *prefix) {
  return self->beginReadArray(QAnyStringView(*prefix));
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::beginWriteArray(QAnyStringView prefix, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings15beginWriteArrayE14QAnyStringViewi(
    QSettings *self,
    const QString *prefix,
    int size) {
  self->beginWriteArray(QAnyStringView(*prefix), size);
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::endArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings8endArrayEv(QSettings *self) {
  self->endArray();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::setArrayIndex(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings13setArrayIndexEi(QSettings *self, int i) {
  self->setArrayIndex(i);
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QStringList QSettings::allKeys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QSettings7allKeysEv(const QSettings *self) {
  return new QList<QString>(self->allKeys());
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QStringList QSettings::childKeys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QSettings9childKeysEv(const QSettings *self) {
  return new QList<QString>(self->childKeys());
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QStringList QSettings::childGroups() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QSettings11childGroupsEv(const QSettings *self) {
  return new QList<QString>(self->childGroups());
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  bool QSettings::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings10isWritableEv(const QSettings *self) {
  return self->isWritable();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::setValue(QAnyStringView key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings8setValueE14QAnyStringViewRK8QVariant(
    QSettings *self,
    const QString *key,
    const QVariant *value) {
  self->setValue(QAnyStringView(*key), *value);
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QVariant QSettings::value(QAnyStringView key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSettings5valueE14QAnyStringViewRK8QVariant(
    const QSettings *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->value(QAnyStringView(*key), *defaultValue));
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QVariant QSettings::value(QAnyStringView key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSettings5valueE14QAnyStringView(
    const QSettings *self,
    const QString *key) {
  return new QVariant(self->value(QAnyStringView(*key)));
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::remove(QAnyStringView key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings6removeE14QAnyStringView(
    QSettings *self,
    const QString *key) {
  self->remove(QAnyStringView(*key));
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  bool QSettings::contains(QAnyStringView key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings8containsE14QAnyStringView(
    const QSettings *self,
    const QString *key) {
  return self->contains(QAnyStringView(*key));
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::setFallbacksEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings19setFallbacksEnabledEb(QSettings *self, bool b) {
  self->setFallbacksEnabled(b);
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  bool QSettings::fallbacksEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings16fallbacksEnabledEv(const QSettings *self) {
  return self->fallbacksEnabled();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QString QSettings::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings8fileNameEv(const QSettings *self) {
  return new QString(self->fileName());
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  Format QSettings::format() const
extern "C" Q_DECL_EXPORT
QSettings::Format ritual_ZNK9QSettings6formatEv(const QSettings *self) {
  return self->format();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  Scope QSettings::scope() const
extern "C" Q_DECL_EXPORT
QSettings::Scope ritual_ZNK9QSettings5scopeEv(const QSettings *self) {
  return self->scope();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QString QSettings::organizationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings16organizationNameEv(const QSettings *self) {
  return new QString(self->organizationName());
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QString QSettings::applicationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings15applicationNameEv(const QSettings *self) {
  return new QString(self->applicationName());
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::setDefaultFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings16setDefaultFormatENS_6FormatE(
    QSettings::Format format) {
  QSettings::setDefaultFormat(format);
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  Format QSettings::defaultFormat()
extern "C" Q_DECL_EXPORT
QSettings::Format ritual_ZN9QSettings13defaultFormatEv() {
  return QSettings::defaultFormat();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QSettings::setPath(Format format, Scope scope, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings7setPathENS_6FormatENS_5ScopeERK7QString(
    QSettings::Format format,
    QSettings::Scope scope,
    const QString *path) {
  QSettings::setPath(format, scope, *path);
}
#endif  // QT_CONFIG(settings)

//  bool QSettings::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSettings5eventEP6QEvent(QSettings *self, QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQSettings, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSettings(QSettings *self, const char *key, void *call) {
  return static_cast<CuteQSettings *>(self)->take(key, call);
}

//  bool QSettings::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QSettings5eventEP6QEvent(QSettings *self, QEvent *event) {
  return static_cast<OwnQSettings *>(self)->OwnQSettings::event(event);
}

#endif  // !defined(QT_NO_QOBJECT)
#endif  // QT_CONFIG(settings)
