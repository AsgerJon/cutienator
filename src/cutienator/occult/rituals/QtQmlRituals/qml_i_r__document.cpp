//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  bool QmlIR::Document::isSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QmlIR8Document11isSingletonEv(const QmlIR::Document *self) {
  return self->isSingleton();
}

//  int QmlIR::Document::registerString(const QString &str)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QmlIR8Document14registerStringERK7QString(
    QmlIR::Document *self,
    const QString *str) {
  return self->registerString(*str);
}

//  QString QmlIR::Document::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QmlIR8Document8stringAtEi(
    const QmlIR::Document *self,
    int index) {
  return new QString(self->stringAt(index));
}

//  int QmlIR::Document::objectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR8Document11objectCountEv(const QmlIR::Document *self) {
  return self->objectCount();
}

//  Object *QmlIR::Document::objectAt(int i) const
extern "C" Q_DECL_EXPORT
QmlIR::Object *ritual_ZNK5QmlIR8Document8objectAtEi(
    const QmlIR::Document *self,
    int i) {
  return self->objectAt(i);
}
