//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsannotation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QQmlJSMetaMethod::QQmlJSMetaMethod()
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_ZN16QQmlJSMetaMethodC1Ev() {
  return new QQmlJSMetaMethod();
}

//  QQmlJSMetaMethod::QQmlJSMetaMethod(QString name, QString returnType)
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_ZN16QQmlJSMetaMethodC1E7QStringS0_(
    const QString *name,
    const QString *returnType) {
  return new QQmlJSMetaMethod(*name, *returnType);
}

//  QString QQmlJSMetaMethod::methodName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlJSMetaMethod10methodNameEv(
    const QQmlJSMetaMethod *self) {
  return new QString(self->methodName());
}

//  void QQmlJSMetaMethod::setMethodName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod13setMethodNameERK7QString(
    QQmlJSMetaMethod *self,
    const QString *name) {
  self->setMethodName(*name);
}

//  QQmlJS::SourceLocation QQmlJSMetaMethod::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK16QQmlJSMetaMethod14sourceLocationEv(
    const QQmlJSMetaMethod *self) {
  return new QQmlJS::SourceLocation(self->sourceLocation());
}

//  void QQmlJSMetaMethod::setSourceLocation(QQmlJS::SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod17setSourceLocationEN6QQmlJS14SourceLocationE(
    QQmlJSMetaMethod *self,
    const QQmlJS::SourceLocation *location) {
  self->setSourceLocation(*location);
}

//  QQmlJSMetaReturnType QQmlJSMetaMethod::returnValue() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaParameter *ritual_ZNK16QQmlJSMetaMethod11returnValueEv(
    const QQmlJSMetaMethod *self) {
  return new QQmlJSMetaParameter(self->returnValue());
}

//  void QQmlJSMetaMethod::setReturnValue(const QQmlJSMetaReturnType
//      returnValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod14setReturnValueE19QQmlJSMetaParameter(
    QQmlJSMetaMethod *self,
    const QQmlJSMetaParameter *returnValue) {
  self->setReturnValue(*returnValue);
}

//  QString QQmlJSMetaMethod::returnTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlJSMetaMethod14returnTypeNameEv(
    const QQmlJSMetaMethod *self) {
  return new QString(self->returnTypeName());
}

//  void QQmlJSMetaMethod::setReturnTypeName(const QString &typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod17setReturnTypeNameERK7QString(
    QQmlJSMetaMethod *self,
    const QString *typeName) {
  self->setReturnTypeName(*typeName);
}

//  QList<QQmlJSMetaParameter> QQmlJSMetaMethod::parameters() const
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaParameter> *ritual_ZNK16QQmlJSMetaMethod10parametersEv(
    const QQmlJSMetaMethod *self) {
  return new QList<QQmlJSMetaParameter>(self->parameters());
}

//  QStringList QQmlJSMetaMethod::parameterNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QQmlJSMetaMethod14parameterNamesEv(
    const QQmlJSMetaMethod *self) {
  return new QList<QString>(self->parameterNames());
}

//  void QQmlJSMetaMethod::setParameters(const QList<QQmlJSMetaParameter>
//      &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod13setParametersERK5QListI19QQmlJSMetaParameterE(
    QQmlJSMetaMethod *self,
    const QList<QQmlJSMetaParameter> *parameters) {
  self->setParameters(*parameters);
}

//  void QQmlJSMetaMethod::addParameter(const QQmlJSMetaParameter &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod12addParameterERK19QQmlJSMetaParameter(
    QQmlJSMetaMethod *self,
    const QQmlJSMetaParameter *p) {
  self->addParameter(*p);
}

//  QQmlJSMetaMethodType QQmlJSMetaMethod::methodType() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethodType ritual_ZNK16QQmlJSMetaMethod10methodTypeEv(
    const QQmlJSMetaMethod *self) {
  return self->methodType();
}

//  void QQmlJSMetaMethod::setMethodType(MethodType methodType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod13setMethodTypeEN6QQmlSA10MethodTypeE(
    QQmlJSMetaMethod *self,
    QQmlJSMetaMethod::MethodType methodType) {
  self->setMethodType(methodType);
}

//  Access QQmlJSMetaMethod::access() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod::Access ritual_ZNK16QQmlJSMetaMethod6accessEv(
    const QQmlJSMetaMethod *self) {
  return self->access();
}

//  int QQmlJSMetaMethod::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlJSMetaMethod8revisionEv(const QQmlJSMetaMethod *self) {
  return self->revision();
}

//  void QQmlJSMetaMethod::setRevision(int r)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod11setRevisionEi(
    QQmlJSMetaMethod *self,
    int r) {
  self->setRevision(r);
}

//  bool QQmlJSMetaMethod::isCloned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSMetaMethod8isClonedEv(const QQmlJSMetaMethod *self) {
  return self->isCloned();
}

//  void QQmlJSMetaMethod::setIsCloned(bool isCloned)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod11setIsClonedEb(
    QQmlJSMetaMethod *self,
    bool isCloned) {
  self->setIsCloned(isCloned);
}

//  bool QQmlJSMetaMethod::isConstructor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSMetaMethod13isConstructorEv(
    const QQmlJSMetaMethod *self) {
  return self->isConstructor();
}

//  void QQmlJSMetaMethod::setIsConstructor(bool isConstructor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod16setIsConstructorEb(
    QQmlJSMetaMethod *self,
    bool isConstructor) {
  self->setIsConstructor(isConstructor);
}

//  bool QQmlJSMetaMethod::isJavaScriptFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSMetaMethod20isJavaScriptFunctionEv(
    const QQmlJSMetaMethod *self) {
  return self->isJavaScriptFunction();
}

//  void QQmlJSMetaMethod::setIsJavaScriptFunction(bool isJavaScriptFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod23setIsJavaScriptFunctionEb(
    QQmlJSMetaMethod *self,
    bool isJavaScriptFunction) {
  self->setIsJavaScriptFunction(isJavaScriptFunction);
}

//  bool QQmlJSMetaMethod::isImplicitQmlPropertyChangeSignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSMetaMethod33isImplicitQmlPropertyChangeSignalEv(
    const QQmlJSMetaMethod *self) {
  return self->isImplicitQmlPropertyChangeSignal();
}

//  void QQmlJSMetaMethod::setIsImplicitQmlPropertyChangeSignal(bool
//      isPropertyChangeSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod36setIsImplicitQmlPropertyChangeSignalEb(
    QQmlJSMetaMethod *self,
    bool isPropertyChangeSignal) {
  self->setIsImplicitQmlPropertyChangeSignal(isPropertyChangeSignal);
}

//  bool QQmlJSMetaMethod::isConst() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSMetaMethod7isConstEv(const QQmlJSMetaMethod *self) {
  return self->isConst();
}

//  void QQmlJSMetaMethod::setIsConst(bool isConst)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod10setIsConstEb(
    QQmlJSMetaMethod *self,
    bool isConst) {
  self->setIsConst(isConst);
}

//  bool QQmlJSMetaMethod::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSMetaMethod7isValidEv(const QQmlJSMetaMethod *self) {
  return self->isValid();
}

//  const QList<QQmlJSAnnotation> &QQmlJSMetaMethod::annotations() const
extern "C" Q_DECL_EXPORT
QList<QQmlJSAnnotation> *ritual_ZNK16QQmlJSMetaMethod11annotationsEv(
    const QQmlJSMetaMethod *self) {
  return new QList<QQmlJSAnnotation>(self->annotations());
}

//  void QQmlJSMetaMethod::setAnnotations(QList<QQmlJSAnnotation>
//      annotations)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod14setAnnotationsE5QListI16QQmlJSAnnotationE(
    QQmlJSMetaMethod *self,
    const QList<QQmlJSAnnotation> *annotations) {
  self->setAnnotations(*annotations);
}

//  void QQmlJSMetaMethod::setJsFunctionIndex(RelativeFunctionIndex index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod18setJsFunctionIndexENS_21RelativeFunctionIndexE(
    QQmlJSMetaMethod *self,
    QQmlJSMetaMethod::RelativeFunctionIndex index) {
  self->setJsFunctionIndex(index);
}

//  RelativeFunctionIndex QQmlJSMetaMethod::jsFunctionIndex() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod::RelativeFunctionIndex ritual_ZNK16QQmlJSMetaMethod15jsFunctionIndexEv(
    const QQmlJSMetaMethod *self) {
  return self->jsFunctionIndex();
}

//  void QQmlJSMetaMethod::setConstructorIndex(RelativeFunctionIndex index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod19setConstructorIndexENS_21RelativeFunctionIndexE(
    QQmlJSMetaMethod *self,
    QQmlJSMetaMethod::RelativeFunctionIndex index) {
  self->setConstructorIndex(index);
}

//  RelativeFunctionIndex QQmlJSMetaMethod::constructorIndex() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod::RelativeFunctionIndex ritual_ZNK16QQmlJSMetaMethod16constructorIndexEv(
    const QQmlJSMetaMethod *self) {
  return self->constructorIndex();
}

//  void QQmlJSMetaMethod::setMethodIndex(RelativeFunctionIndex index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod14setMethodIndexENS_21RelativeFunctionIndexE(
    QQmlJSMetaMethod *self,
    QQmlJSMetaMethod::RelativeFunctionIndex index) {
  self->setMethodIndex(index);
}

//  RelativeFunctionIndex QQmlJSMetaMethod::methodIndex() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod::RelativeFunctionIndex ritual_ZNK16QQmlJSMetaMethod11methodIndexEv(
    const QQmlJSMetaMethod *self) {
  return self->methodIndex();
}

//  void QQmlJSMetaMethod::setOtherMethodIndex(RelativeFunctionIndex index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethod19setOtherMethodIndexENS_21RelativeFunctionIndexE(
    QQmlJSMetaMethod *self,
    QQmlJSMetaMethod::RelativeFunctionIndex index) {
  self->setOtherMethodIndex(index);
}

//  RelativeFunctionIndex QQmlJSMetaMethod::otherMethodIndex() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod::RelativeFunctionIndex ritual_ZNK16QQmlJSMetaMethod16otherMethodIndexEv(
    const QQmlJSMetaMethod *self) {
  return self->otherMethodIndex();
}

//  QQmlJSMetaMethod::~QQmlJSMetaMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSMetaMethodD1Ev(QQmlJSMetaMethod *self) {
  delete self;
}

//  QList<QQmlJSMetaMethod>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaMethod> *ritual_list_make_QQmlJSMetaMethod() {
  return new QList<QQmlJSMetaMethod>();
}

//  void QList<QQmlJSMetaMethod>::append(const QQmlJSMetaMethod &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlJSMetaMethod(
    QList<QQmlJSMetaMethod> *self,
    const QQmlJSMetaMethod *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlJSMetaMethod>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlJSMetaMethod(
    const QList<QQmlJSMetaMethod> *self) {
  return self->size();
}

//  const QQmlJSMetaMethod &QList<QQmlJSMetaMethod>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_list_at_QQmlJSMetaMethod(
    const QList<QQmlJSMetaMethod> *self,
    long long index) {
  return new QQmlJSMetaMethod(self->at(index));
}

//  QList<QQmlJSMetaMethod>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlJSMetaMethod(QList<QQmlJSMetaMethod> *self) {
  delete self;
}

//  QHash<QString, QQmlJSMetaMethod>: QHash<QString, QQmlJSMetaMethod>()
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaMethod> *ritual_map_make_QHash_QString_QQmlJSMetaMethod() {
  return new QHash<QString, QQmlJSMetaMethod>();
}

//  QHash<QString, QQmlJSMetaMethod>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_QString_QQmlJSMetaMethod(
    QHash<QString, QQmlJSMetaMethod> *self,
    const QString *key,
    const QQmlJSMetaMethod *value) {
  self->insert(*key, *value);
}

//  QHash<QString, QQmlJSMetaMethod>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_QString_QQmlJSMetaMethod(
    const QHash<QString, QQmlJSMetaMethod> *self) {
  return self->size();
}

//  QHash<QString, QQmlJSMetaMethod>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QHash_QString_QQmlJSMetaMethod(
    const QHash<QString, QQmlJSMetaMethod> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QHash<QString, QQmlJSMetaMethod>: the value at a place
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_map_value_QHash_QString_QQmlJSMetaMethod(
    const QHash<QString, QQmlJSMetaMethod> *self,
    long long index) {
  return new QQmlJSMetaMethod(*std::next(self->constBegin(), index));
}

//  QHash<QString, QQmlJSMetaMethod>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_QString_QQmlJSMetaMethod(
    const QHash<QString, QQmlJSMetaMethod> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QHash<QString, QQmlJSMetaMethod>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_map_get_QHash_QString_QQmlJSMetaMethod(
    const QHash<QString, QQmlJSMetaMethod> *self,
    const QString *key) {
  return new QQmlJSMetaMethod(self->value(*key));
}

//  QHash<QString, QQmlJSMetaMethod>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_QString_QQmlJSMetaMethod(
    QHash<QString, QQmlJSMetaMethod> *self) {
  delete self;
}
