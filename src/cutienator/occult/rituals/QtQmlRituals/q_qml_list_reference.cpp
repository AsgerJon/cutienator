//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmllist.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmllist.h>
#include <QtCore/qvariant.h>

//  QQmlListReference::QQmlListReference()
extern "C" Q_DECL_EXPORT
QQmlListReference *ritual_ZN17QQmlListReferenceC1Ev() {
  return new QQmlListReference();
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QQmlListReference::QQmlListReference(const QVariant &variant, QQmlEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QQmlListReference *ritual_ZN17QQmlListReferenceC1ERK8QVariantP10QQmlEngine(
    const QVariant *variant,
    QQmlEngine *engine) {
  return new QQmlListReference(*variant, engine);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QQmlListReference::QQmlListReference(QObject *o, const char *property,
//      QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
QQmlListReference *ritual_ZN17QQmlListReferenceC1EP7QObjectPKcP10QQmlEngine(
    QObject *o,
    const char *property,
    QQmlEngine *engine) {
  return new QQmlListReference(o, property, engine);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  QQmlListReference::QQmlListReference(const QVariant &variant)
extern "C" Q_DECL_EXPORT
QQmlListReference *ritual_ZN17QQmlListReferenceC1ERK8QVariant(
    const QVariant *variant) {
  return new QQmlListReference(*variant);
}

//  QQmlListReference::QQmlListReference(QObject *o, const char *property)
extern "C" Q_DECL_EXPORT
QQmlListReference *ritual_ZN17QQmlListReferenceC1EP7QObjectPKc(
    QObject *o,
    const char *property) {
  return new QQmlListReference(o, property);
}

//  QQmlListReference::QQmlListReference(const QQmlListReference &a0)
extern "C" Q_DECL_EXPORT
QQmlListReference *ritual_ZN17QQmlListReferenceC1ERKS_(
    const QQmlListReference *a0) {
  return new QQmlListReference(*a0);
}

//  QQmlListReference::~QQmlListReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlListReferenceD1Ev(QQmlListReference *self) {
  delete self;
}

//  bool QQmlListReference::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference7isValidEv(const QQmlListReference *self) {
  return self->isValid();
}

//  QObject *QQmlListReference::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QQmlListReference6objectEv(
    const QQmlListReference *self) {
  return self->object();
}

//  const QMetaObject *QQmlListReference::listElementType() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlListReference15listElementTypeEv(
    const QQmlListReference *self) {
  return self->listElementType();
}

//  bool QQmlListReference::canAppend() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference9canAppendEv(
    const QQmlListReference *self) {
  return self->canAppend();
}

//  bool QQmlListReference::canAt() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference5canAtEv(const QQmlListReference *self) {
  return self->canAt();
}

//  bool QQmlListReference::canClear() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference8canClearEv(
    const QQmlListReference *self) {
  return self->canClear();
}

//  bool QQmlListReference::canCount() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference8canCountEv(
    const QQmlListReference *self) {
  return self->canCount();
}

//  bool QQmlListReference::canReplace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference10canReplaceEv(
    const QQmlListReference *self) {
  return self->canReplace();
}

//  bool QQmlListReference::canRemoveLast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference13canRemoveLastEv(
    const QQmlListReference *self) {
  return self->canRemoveLast();
}

//  bool QQmlListReference::isManipulable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference13isManipulableEv(
    const QQmlListReference *self) {
  return self->isManipulable();
}

//  bool QQmlListReference::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference10isReadableEv(
    const QQmlListReference *self) {
  return self->isReadable();
}

//  bool QQmlListReference::append(QObject *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference6appendEP7QObject(
    const QQmlListReference *self,
    QObject *a0) {
  return self->append(a0);
}

//  QObject *QQmlListReference::at(qsizetype a0) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QQmlListReference2atEx(
    const QQmlListReference *self,
    qsizetype a0) {
  return self->at(a0);
}

//  bool QQmlListReference::clear() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference5clearEv(const QQmlListReference *self) {
  return self->clear();
}

//  qsizetype QQmlListReference::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QQmlListReference5countEv(
    const QQmlListReference *self) {
  return self->count();
}

//  qsizetype QQmlListReference::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QQmlListReference4sizeEv(
    const QQmlListReference *self) {
  return self->size();
}

//  bool QQmlListReference::replace(qsizetype a0, QObject *a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference7replaceExP7QObject(
    const QQmlListReference *self,
    qsizetype a0,
    QObject *a1) {
  return self->replace(a0, a1);
}

//  bool QQmlListReference::removeLast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReference10removeLastEv(
    const QQmlListReference *self) {
  return self->removeLast();
}

//  bool QQmlListReference::operator==(const QQmlListReference &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlListReferenceeqERKS_(
    const QQmlListReference *self,
    const QQmlListReference *other) {
  return self->operator==(*other);
}
