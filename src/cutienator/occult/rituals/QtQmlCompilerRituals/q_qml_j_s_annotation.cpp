//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsannotation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsannotation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  bool QQmlJSAnnotation::isDeprecation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSAnnotation13isDeprecationEv(
    const QQmlJSAnnotation *self) {
  return self->isDeprecation();
}

//  QQQmlJSDeprecation QQmlJSAnnotation::deprecation() const
extern "C" Q_DECL_EXPORT
QQQmlJSDeprecation *ritual_ZNK16QQmlJSAnnotation11deprecationEv(
    const QQmlJSAnnotation *self) {
  return new QQQmlJSDeprecation(self->deprecation());
}

//  QQmlJSAnnotation::~QQmlJSAnnotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSAnnotationD1Ev(QQmlJSAnnotation *self) {
  delete self;
}

//  QList<QQmlJSAnnotation>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlJSAnnotation> *ritual_list_make_QQmlJSAnnotation() {
  return new QList<QQmlJSAnnotation>();
}

//  void QList<QQmlJSAnnotation>::append(const QQmlJSAnnotation &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlJSAnnotation(
    QList<QQmlJSAnnotation> *self,
    const QQmlJSAnnotation *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlJSAnnotation>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlJSAnnotation(
    const QList<QQmlJSAnnotation> *self) {
  return self->size();
}

//  const QQmlJSAnnotation &QList<QQmlJSAnnotation>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlJSAnnotation *ritual_list_at_QQmlJSAnnotation(
    const QList<QQmlJSAnnotation> *self,
    long long index) {
  return new QQmlJSAnnotation(self->at(index));
}

//  QList<QQmlJSAnnotation>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlJSAnnotation(QList<QQmlJSAnnotation> *self) {
  delete self;
}
