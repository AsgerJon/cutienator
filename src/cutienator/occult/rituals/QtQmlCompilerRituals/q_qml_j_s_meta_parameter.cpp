//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QString QQmlJSMetaParameter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSMetaParameter4nameEv(
    const QQmlJSMetaParameter *self) {
  return new QString(self->name());
}

//  void QQmlJSMetaParameter::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSMetaParameter7setNameERK7QString(
    QQmlJSMetaParameter *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QQmlJSMetaParameter::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSMetaParameter8typeNameEv(
    const QQmlJSMetaParameter *self) {
  return new QString(self->typeName());
}

//  void QQmlJSMetaParameter::setTypeName(const QString &typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSMetaParameter11setTypeNameERK7QString(
    QQmlJSMetaParameter *self,
    const QString *typeName) {
  self->setTypeName(*typeName);
}

//  Constness QQmlJSMetaParameter::typeQualifier() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaParameter::Constness ritual_ZNK19QQmlJSMetaParameter13typeQualifierEv(
    const QQmlJSMetaParameter *self) {
  return self->typeQualifier();
}

//  void QQmlJSMetaParameter::setTypeQualifier(Constness typeQualifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSMetaParameter16setTypeQualifierENS_9ConstnessE(
    QQmlJSMetaParameter *self,
    QQmlJSMetaParameter::Constness typeQualifier) {
  self->setTypeQualifier(typeQualifier);
}

//  bool QQmlJSMetaParameter::isPointer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSMetaParameter9isPointerEv(
    const QQmlJSMetaParameter *self) {
  return self->isPointer();
}

//  void QQmlJSMetaParameter::setIsPointer(bool isPointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSMetaParameter12setIsPointerEb(
    QQmlJSMetaParameter *self,
    bool isPointer) {
  self->setIsPointer(isPointer);
}

//  bool QQmlJSMetaParameter::isList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSMetaParameter6isListEv(
    const QQmlJSMetaParameter *self) {
  return self->isList();
}

//  void QQmlJSMetaParameter::setIsList(bool isList)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSMetaParameter9setIsListEb(
    QQmlJSMetaParameter *self,
    bool isList) {
  self->setIsList(isList);
}

//  bool operator==(const QQmlJSMetaParameter &a, const QQmlJSMetaParameter
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QQmlJSMetaParameterS1_(
    const QQmlJSMetaParameter *a,
    const QQmlJSMetaParameter *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QQmlJSMetaParameter &a, const QQmlJSMetaParameter
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QQmlJSMetaParameterS1_(
    const QQmlJSMetaParameter *a,
    const QQmlJSMetaParameter *b) {
  return operator!=(*a, *b);
}

//  QQmlJSMetaParameter::~QQmlJSMetaParameter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSMetaParameterD1Ev(QQmlJSMetaParameter *self) {
  delete self;
}

//  QList<QQmlJSMetaParameter>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaParameter> *ritual_list_make_QQmlJSMetaParameter() {
  return new QList<QQmlJSMetaParameter>();
}

//  void QList<QQmlJSMetaParameter>::append(const QQmlJSMetaParameter &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlJSMetaParameter(
    QList<QQmlJSMetaParameter> *self,
    const QQmlJSMetaParameter *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlJSMetaParameter>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlJSMetaParameter(
    const QList<QQmlJSMetaParameter> *self) {
  return self->size();
}

//  const QQmlJSMetaParameter &QList<QQmlJSMetaParameter>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQmlJSMetaParameter *ritual_list_at_QQmlJSMetaParameter(
    const QList<QQmlJSMetaParameter> *self,
    long long index) {
  return new QQmlJSMetaParameter(self->at(index));
}

//  QList<QQmlJSMetaParameter>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlJSMetaParameter(QList<QQmlJSMetaParameter> *self) {
  delete self;
}
