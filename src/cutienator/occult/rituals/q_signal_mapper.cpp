//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsignalmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsignalmapper.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QSignalMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSignalMapper10metaObjectEv(
    const QSignalMapper *self) {
  return self->metaObject();
}

//  QString QSignalMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSignalMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSignalMapper::tr(s, c, n));
}

//  QSignalMapper::QSignalMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QSignalMapper *ritual_ZN13QSignalMapperC1EP7QObject(QObject *parent) {
  return new QSignalMapper(parent);
}

//  QSignalMapper::~QSignalMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapperD1Ev(QSignalMapper *self) {
  delete self;
}

//  void QSignalMapper::setMapping(QObject *sender, int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper10setMappingEP7QObjecti(
    QSignalMapper *self,
    QObject *sender,
    int id) {
  self->setMapping(sender, id);
}

//  void QSignalMapper::setMapping(QObject *sender, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper10setMappingEP7QObjectRK7QString(
    QSignalMapper *self,
    QObject *sender,
    const QString *text) {
  self->setMapping(sender, *text);
}

//  void QSignalMapper::setMapping(QObject *sender, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper10setMappingEP7QObjectS1_(
    QSignalMapper *self,
    QObject *sender,
    QObject *object) {
  self->setMapping(sender, object);
}

//  void QSignalMapper::removeMappings(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper14removeMappingsEP7QObject(
    QSignalMapper *self,
    QObject *sender) {
  self->removeMappings(sender);
}

//  QObject *QSignalMapper::mapping(int id) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QSignalMapper7mappingEi(
    const QSignalMapper *self,
    int id) {
  return self->mapping(id);
}

//  QObject *QSignalMapper::mapping(const QString &text) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QSignalMapper7mappingERK7QString(
    const QSignalMapper *self,
    const QString *text) {
  return self->mapping(*text);
}

//  QObject *QSignalMapper::mapping(QObject *object) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QSignalMapper7mappingEP7QObject(
    const QSignalMapper *self,
    QObject *object) {
  return self->mapping(object);
}

//  void QSignalMapper::map()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper3mapEv(QSignalMapper *self) {
  self->map();
}

//  void QSignalMapper::map(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSignalMapper3mapEP7QObject(
    QSignalMapper *self,
    QObject *sender) {
  self->map(sender);
}
