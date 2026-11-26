//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcustomparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcustomparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlerror.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QQmlCustomParser::~QQmlCustomParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlCustomParserD1Ev(QQmlCustomParser *self) {
  delete self;
}

//  void QQmlCustomParser::clearErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlCustomParser11clearErrorsEv(QQmlCustomParser *self) {
  self->clearErrors();
}

//  Flags QQmlCustomParser::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlCustomParser5flagsEv(const QQmlCustomParser *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QQmlCustomParser::verifyBindings(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &a0, const
//      QList<const QV4::CompiledData::Binding *> &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlCustomParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE(
    QQmlCustomParser *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *a0,
    const QList<const QV4::CompiledData::Binding *> *a1) {
  self->verifyBindings(*a0, *a1);
}

//  void QQmlCustomParser::applyBindings(QObject *a0, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const QList<const
//      QV4::CompiledData::Binding *> &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlCustomParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE(
    QQmlCustomParser *self,
    QObject *a0,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *a1,
    const QList<const QV4::CompiledData::Binding *> *a2) {
  self->applyBindings(a0, *a1, *a2);
}

//  QList<QQmlError> QQmlCustomParser::errors() const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK16QQmlCustomParser6errorsEv(
    const QQmlCustomParser *self) {
  return new QList<QQmlError>(self->errors());
}

//  void QQmlCustomParser::error(const QV4::CompiledData::Binding *binding,
//      const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlCustomParser5errorEPKN3QV412CompiledData7BindingERK7QString(
    QQmlCustomParser *self,
    const QV4::CompiledData::Binding *binding,
    const QString *description) {
  self->error(binding, *description);
}

//  void QQmlCustomParser::error(const QV4::CompiledData::Object *object,
//      const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlCustomParser5errorEPKN3QV412CompiledData6ObjectERK7QString(
    QQmlCustomParser *self,
    const QV4::CompiledData::Object *object,
    const QString *description) {
  self->error(object, *description);
}

//  void QQmlCustomParser::error(const QV4::CompiledData::Location &location,
//      const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlCustomParser5errorERKN3QV412CompiledData8LocationERK7QString(
    QQmlCustomParser *self,
    const QV4::CompiledData::Location *location,
    const QString *description) {
  self->error(*location, *description);
}

//  int QQmlCustomParser::evaluateEnum(const QString &a0, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlCustomParser12evaluateEnumERK7QStringPb(
    const QQmlCustomParser *self,
    const QString *a0,
    bool *ok) {
  return self->evaluateEnum(*a0, ok);
}

//  const QMetaObject *QQmlCustomParser::resolveType(const QString &a0) const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlCustomParser11resolveTypeERK7QString(
    const QQmlCustomParser *self,
    const QString *a0) {
  return self->resolveType(*a0);
}

//  QQmlTypeLoader *QQmlCustomParser::typeLoader() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZNK16QQmlCustomParser10typeLoaderEv(
    const QQmlCustomParser *self) {
  return self->typeLoader();
}

//  QHash<int, QQmlCustomParser *>: QHash<int, QQmlCustomParser *>()
extern "C" Q_DECL_EXPORT
QHash<int, QQmlCustomParser *> *ritual_map_make_QHash_int_QQmlCustomParser_ptr() {
  return new QHash<int, QQmlCustomParser *>();
}

//  QHash<int, QQmlCustomParser *>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_int_QQmlCustomParser_ptr(
    QHash<int, QQmlCustomParser *> *self,
    int key,
    QQmlCustomParser *value) {
  self->insert(key, value);
}

//  QHash<int, QQmlCustomParser *>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_int_QQmlCustomParser_ptr(
    const QHash<int, QQmlCustomParser *> *self) {
  return self->size();
}

//  QHash<int, QQmlCustomParser *>: the key at a place
extern "C" Q_DECL_EXPORT
int ritual_map_key_QHash_int_QQmlCustomParser_ptr(
    const QHash<int, QQmlCustomParser *> *self,
    long long index) {
  return *std::next(self->keyBegin(), index);
}

//  QHash<int, QQmlCustomParser *>: the value at a place
extern "C" Q_DECL_EXPORT
QQmlCustomParser *ritual_map_value_QHash_int_QQmlCustomParser_ptr(
    const QHash<int, QQmlCustomParser *> *self,
    long long index) {
  return *std::next(self->constBegin(), index);
}

//  QHash<int, QQmlCustomParser *>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_int_QQmlCustomParser_ptr(
    const QHash<int, QQmlCustomParser *> *self,
    int key) {
  return self->contains(key);
}

//  QHash<int, QQmlCustomParser *>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QQmlCustomParser *ritual_map_get_QHash_int_QQmlCustomParser_ptr(
    const QHash<int, QQmlCustomParser *> *self,
    int key) {
  return self->value(key);
}

//  QHash<int, QQmlCustomParser *>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_int_QQmlCustomParser_ptr(
    QHash<int, QQmlCustomParser *> *self) {
  delete self;
}
