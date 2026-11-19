//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsettings.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsettings.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qvariant.h>

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

//  QSettings::QSettings(const QString &organization, const QString
//      &application, QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ERK7QStringS2_P7QObject(
    const QString *organization,
    const QString *application,
    QObject *parent) {
  return new QSettings(*organization, *application, parent);
}

//  QSettings::QSettings(Scope scope, const QString &organization, const
//      QString &application, QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ENS_5ScopeERK7QStringS3_P7QObject(
    QSettings::Scope scope,
    const QString *organization,
    const QString *application,
    QObject *parent) {
  return new QSettings(scope, *organization, *application, parent);
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
  return new QSettings(format, scope, *organization, *application, parent);
}

//  QSettings::QSettings(const QString &fileName, Format format, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ERK7QStringNS_6FormatEP7QObject(
    const QString *fileName,
    QSettings::Format format,
    QObject *parent) {
  return new QSettings(*fileName, format, parent);
}

//  QSettings::QSettings(QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1EP7QObject(QObject *parent) {
  return new QSettings(parent);
}

//  QSettings::QSettings(Scope scope, QObject *parent)
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN9QSettingsC1ENS_5ScopeEP7QObject(
    QSettings::Scope scope,
    QObject *parent) {
  return new QSettings(scope, parent);
}

//  QSettings::~QSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettingsD1Ev(QSettings *self) {
  delete self;
}

//  void QSettings::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings5clearEv(QSettings *self) {
  self->clear();
}

//  void QSettings::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings4syncEv(QSettings *self) {
  self->sync();
}

//  Status QSettings::status() const
extern "C" Q_DECL_EXPORT
QSettings::Status ritual_ZNK9QSettings6statusEv(const QSettings *self) {
  return self->status();
}

//  bool QSettings::isAtomicSyncRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings20isAtomicSyncRequiredEv(const QSettings *self) {
  return self->isAtomicSyncRequired();
}

//  void QSettings::setAtomicSyncRequired(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings21setAtomicSyncRequiredEb(
    QSettings *self,
    bool enable) {
  self->setAtomicSyncRequired(enable);
}

//  void QSettings::beginGroup(QAnyStringView prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings10beginGroupE14QAnyStringView(
    QSettings *self,
    const QString *prefix) {
  self->beginGroup(QAnyStringView(*prefix));
}

//  void QSettings::endGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings8endGroupEv(QSettings *self) {
  self->endGroup();
}

//  QString QSettings::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings5groupEv(const QSettings *self) {
  return new QString(self->group());
}

//  int QSettings::beginReadArray(QAnyStringView prefix)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QSettings14beginReadArrayE14QAnyStringView(
    QSettings *self,
    const QString *prefix) {
  return self->beginReadArray(QAnyStringView(*prefix));
}

//  void QSettings::beginWriteArray(QAnyStringView prefix, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings15beginWriteArrayE14QAnyStringViewi(
    QSettings *self,
    const QString *prefix,
    int size) {
  self->beginWriteArray(QAnyStringView(*prefix), size);
}

//  void QSettings::endArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings8endArrayEv(QSettings *self) {
  self->endArray();
}

//  void QSettings::setArrayIndex(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings13setArrayIndexEi(QSettings *self, int i) {
  self->setArrayIndex(i);
}

//  bool QSettings::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings10isWritableEv(const QSettings *self) {
  return self->isWritable();
}

//  void QSettings::setValue(QAnyStringView key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings8setValueE14QAnyStringViewRK8QVariant(
    QSettings *self,
    const QString *key,
    const QVariant *value) {
  self->setValue(QAnyStringView(*key), *value);
}

//  QVariant QSettings::value(QAnyStringView key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSettings5valueE14QAnyStringViewRK8QVariant(
    const QSettings *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->value(QAnyStringView(*key), *defaultValue));
}

//  QVariant QSettings::value(QAnyStringView key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSettings5valueE14QAnyStringView(
    const QSettings *self,
    const QString *key) {
  return new QVariant(self->value(QAnyStringView(*key)));
}

//  void QSettings::remove(QAnyStringView key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings6removeE14QAnyStringView(
    QSettings *self,
    const QString *key) {
  self->remove(QAnyStringView(*key));
}

//  bool QSettings::contains(QAnyStringView key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings8containsE14QAnyStringView(
    const QSettings *self,
    const QString *key) {
  return self->contains(QAnyStringView(*key));
}

//  void QSettings::setFallbacksEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings19setFallbacksEnabledEb(QSettings *self, bool b) {
  self->setFallbacksEnabled(b);
}

//  bool QSettings::fallbacksEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSettings16fallbacksEnabledEv(const QSettings *self) {
  return self->fallbacksEnabled();
}

//  QString QSettings::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings8fileNameEv(const QSettings *self) {
  return new QString(self->fileName());
}

//  Format QSettings::format() const
extern "C" Q_DECL_EXPORT
QSettings::Format ritual_ZNK9QSettings6formatEv(const QSettings *self) {
  return self->format();
}

//  Scope QSettings::scope() const
extern "C" Q_DECL_EXPORT
QSettings::Scope ritual_ZNK9QSettings5scopeEv(const QSettings *self) {
  return self->scope();
}

//  QString QSettings::organizationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings16organizationNameEv(const QSettings *self) {
  return new QString(self->organizationName());
}

//  QString QSettings::applicationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSettings15applicationNameEv(const QSettings *self) {
  return new QString(self->applicationName());
}

//  void QSettings::setDefaultFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings16setDefaultFormatENS_6FormatE(
    QSettings::Format format) {
  QSettings::setDefaultFormat(format);
}

//  Format QSettings::defaultFormat()
extern "C" Q_DECL_EXPORT
QSettings::Format ritual_ZN9QSettings13defaultFormatEv() {
  return QSettings::defaultFormat();
}

//  void QSettings::setPath(Format format, Scope scope, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSettings7setPathENS_6FormatENS_5ScopeERK7QString(
    QSettings::Format format,
    QSettings::Scope scope,
    const QString *path) {
  QSettings::setPath(format, scope, *path);
}
