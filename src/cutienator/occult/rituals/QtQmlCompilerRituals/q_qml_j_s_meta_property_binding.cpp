//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltranslation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>

//  void QQmlJSMetaPropertyBinding::ensureSetBindingTypeOnce()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding24ensureSetBindingTypeOnceEv(
    QQmlJSMetaPropertyBinding *self) {
  self->ensureSetBindingTypeOnce();
}

//  bool QQmlJSMetaPropertyBinding::isLiteralBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlJSMetaPropertyBinding16isLiteralBindingEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->isLiteralBinding();
}

//  bool QQmlJSMetaPropertyBinding::isLiteralBinding(BindingType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQmlJSMetaPropertyBinding16isLiteralBindingEN6QQmlSA11BindingTypeE(
    QQmlJSMetaPropertyBinding::BindingType type) {
  return QQmlJSMetaPropertyBinding::isLiteralBinding(type);
}

//  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding()
extern "C" Q_DECL_EXPORT
QQmlJSMetaPropertyBinding *ritual_ZN25QQmlJSMetaPropertyBindingC1Ev() {
  return new QQmlJSMetaPropertyBinding();
}

//  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::SourceLocati
//      on location)
extern "C" Q_DECL_EXPORT
QQmlJSMetaPropertyBinding *ritual_ZN25QQmlJSMetaPropertyBindingC1EN6QQmlJS14SourceLocationE(
    const QQmlJS::SourceLocation *location) {
  return new QQmlJSMetaPropertyBinding(*location);
}

//  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::SourceLocati
//      on location, const QString &propName)
extern "C" Q_DECL_EXPORT
QQmlJSMetaPropertyBinding *ritual_ZN25QQmlJSMetaPropertyBindingC1EN6QQmlJS14SourceLocationERK7QString(
    const QQmlJS::SourceLocation *location,
    const QString *propName) {
  return new QQmlJSMetaPropertyBinding(*location, *propName);
}

//  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::SourceLocati
//      on location, const QQmlJSMetaProperty &prop)
extern "C" Q_DECL_EXPORT
QQmlJSMetaPropertyBinding *ritual_ZN25QQmlJSMetaPropertyBindingC1EN6QQmlJS14SourceLocationERK18QQmlJSMetaProperty(
    const QQmlJS::SourceLocation *location,
    const QQmlJSMetaProperty *prop) {
  return new QQmlJSMetaPropertyBinding(*location, *prop);
}

//  void QQmlJSMetaPropertyBinding::setPropertyName(const QString
//      &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding15setPropertyNameERK7QString(
    QQmlJSMetaPropertyBinding *self,
    const QString *propertyName) {
  self->setPropertyName(*propertyName);
}

//  QString QQmlJSMetaPropertyBinding::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlJSMetaPropertyBinding12propertyNameEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QString(self->propertyName());
}

//  const QQmlJS::SourceLocation &QQmlJSMetaPropertyBinding::sourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK25QQmlJSMetaPropertyBinding14sourceLocationEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QQmlJS::SourceLocation(self->sourceLocation());
}

//  BindingType QQmlJSMetaPropertyBinding::bindingType() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaPropertyBinding::BindingType ritual_ZNK25QQmlJSMetaPropertyBinding11bindingTypeEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->bindingType();
}

//  bool QQmlJSMetaPropertyBinding::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlJSMetaPropertyBinding7isValidEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->isValid();
}

//  void QQmlJSMetaPropertyBinding::setStringLiteral(QAnyStringView value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding16setStringLiteralE14QAnyStringView(
    QQmlJSMetaPropertyBinding *self,
    const QString *value) {
  self->setStringLiteral(QAnyStringView(*value));
}

//  void QQmlJSMetaPropertyBinding::setScriptBinding(QQmlJSMetaMethod::Relati
//      veFunctionIndex value, ScriptBindingKind kind, ScriptBindingValueType
//      valueType)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding16setScriptBindingEN16QQmlJSMetaMethod21RelativeFunctionIndexEN6QQmlSA17ScriptBindingKindE22ScriptBindingValueType(
    QQmlJSMetaPropertyBinding *self,
    QQmlJSMetaMethod::RelativeFunctionIndex value,
    QQmlJSMetaPropertyBinding::ScriptBindingKind kind,
    ScriptBindingValueType valueType) {
  self->setScriptBinding(value, kind, valueType);
}

//  void QQmlJSMetaPropertyBinding::setGroupBinding(const
//      QSharedPointer<const QQmlJSScope> &groupScope)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding15setGroupBindingERK14QSharedPointerIK11QQmlJSScopeE(
    QQmlJSMetaPropertyBinding *self,
    const QSharedPointer<const QQmlJSScope> *groupScope) {
  self->setGroupBinding(*groupScope);
}

//  void QQmlJSMetaPropertyBinding::setAttachedBinding(const
//      QSharedPointer<const QQmlJSScope> &attachingScope)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding18setAttachedBindingERK14QSharedPointerIK11QQmlJSScopeE(
    QQmlJSMetaPropertyBinding *self,
    const QSharedPointer<const QQmlJSScope> *attachingScope) {
  self->setAttachedBinding(*attachingScope);
}

//  void QQmlJSMetaPropertyBinding::setBoolLiteral(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding14setBoolLiteralEb(
    QQmlJSMetaPropertyBinding *self,
    bool value) {
  self->setBoolLiteral(value);
}

//  void QQmlJSMetaPropertyBinding::setNullLiteral()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding14setNullLiteralEv(
    QQmlJSMetaPropertyBinding *self) {
  self->setNullLiteral();
}

//  void QQmlJSMetaPropertyBinding::setNumberLiteral(double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding16setNumberLiteralEd(
    QQmlJSMetaPropertyBinding *self,
    double value) {
  self->setNumberLiteral(value);
}

//  void QQmlJSMetaPropertyBinding::setRegexpLiteral(QAnyStringView value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding16setRegexpLiteralE14QAnyStringView(
    QQmlJSMetaPropertyBinding *self,
    const QString *value) {
  self->setRegexpLiteral(QAnyStringView(*value));
}

//  void QQmlJSMetaPropertyBinding::setTranslation(QStringView text,
//      QStringView comment, QStringView context, int number)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding14setTranslationE11QStringViewS0_S0_i(
    QQmlJSMetaPropertyBinding *self,
    const QString *text,
    const QString *comment,
    const QString *context,
    int number) {
  self->setTranslation(
      QStringView(*text),
      QStringView(*comment),
      QStringView(*context),
      number);
}

//  void QQmlJSMetaPropertyBinding::setTranslationId(QStringView id, int
//      number)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding16setTranslationIdE11QStringViewi(
    QQmlJSMetaPropertyBinding *self,
    const QString *id,
    int number) {
  self->setTranslationId(QStringView(*id), number);
}

//  void QQmlJSMetaPropertyBinding::setObject(const QString &typeName, const
//      QSharedPointer<const QQmlJSScope> &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding9setObjectERK7QStringRK14QSharedPointerIK11QQmlJSScopeE(
    QQmlJSMetaPropertyBinding *self,
    const QString *typeName,
    const QSharedPointer<const QQmlJSScope> *type) {
  self->setObject(*typeName, *type);
}

//  void QQmlJSMetaPropertyBinding::setInterceptor(const QString &typeName,
//      const QSharedPointer<const QQmlJSScope> &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding14setInterceptorERK7QStringRK14QSharedPointerIK11QQmlJSScopeE(
    QQmlJSMetaPropertyBinding *self,
    const QString *typeName,
    const QSharedPointer<const QQmlJSScope> *type) {
  self->setInterceptor(*typeName, *type);
}

//  void QQmlJSMetaPropertyBinding::setValueSource(const QString &typeName,
//      const QSharedPointer<const QQmlJSScope> &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBinding14setValueSourceERK7QStringRK14QSharedPointerIK11QQmlJSScopeE(
    QQmlJSMetaPropertyBinding *self,
    const QString *typeName,
    const QSharedPointer<const QQmlJSScope> *type) {
  self->setValueSource(*typeName, *type);
}

//  bool QQmlJSMetaPropertyBinding::boolValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlJSMetaPropertyBinding9boolValueEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->boolValue();
}

//  double QQmlJSMetaPropertyBinding::numberValue() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QQmlJSMetaPropertyBinding11numberValueEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->numberValue();
}

//  QString QQmlJSMetaPropertyBinding::stringValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlJSMetaPropertyBinding11stringValueEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QString(self->stringValue());
}

//  QString QQmlJSMetaPropertyBinding::regExpValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlJSMetaPropertyBinding11regExpValueEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QString(self->regExpValue());
}

//  QQmlTranslation QQmlJSMetaPropertyBinding::translationDataValue(QString
//      qmlFileNameForContext) const
extern "C" Q_DECL_EXPORT
QQmlTranslation *ritual_ZNK25QQmlJSMetaPropertyBinding20translationDataValueE7QString(
    const QQmlJSMetaPropertyBinding *self,
    const QString *qmlFileNameForContext) {
  return new QQmlTranslation(
      self->translationDataValue(
          *qmlFileNameForContext));
}

//  QSharedPointer<const QQmlJSScope>
//      QQmlJSMetaPropertyBinding::literalType(const QQmlJSTypeResolver
//      *resolver) const
extern "C" Q_DECL_EXPORT
QSharedPointer<const QQmlJSScope> *ritual_ZNK25QQmlJSMetaPropertyBinding11literalTypeEPK18QQmlJSTypeResolver(
    const QQmlJSMetaPropertyBinding *self,
    const QQmlJSTypeResolver *resolver) {
  return new QSharedPointer<const QQmlJSScope>(self->literalType(resolver));
}

//  QQmlJSMetaMethod::RelativeFunctionIndex
//      QQmlJSMetaPropertyBinding::scriptIndex() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod::RelativeFunctionIndex ritual_ZNK25QQmlJSMetaPropertyBinding11scriptIndexEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->scriptIndex();
}

//  ScriptBindingKind QQmlJSMetaPropertyBinding::scriptKind() const
extern "C" Q_DECL_EXPORT
QQmlJSMetaPropertyBinding::ScriptBindingKind ritual_ZNK25QQmlJSMetaPropertyBinding10scriptKindEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->scriptKind();
}

//  ScriptBindingValueType QQmlJSMetaPropertyBinding::scriptValueType() const
extern "C" Q_DECL_EXPORT
ScriptBindingValueType ritual_ZNK25QQmlJSMetaPropertyBinding15scriptValueTypeEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->scriptValueType();
}

//  QString QQmlJSMetaPropertyBinding::objectTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlJSMetaPropertyBinding14objectTypeNameEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QString(self->objectTypeName());
}

//  QSharedPointer<const QQmlJSScope> QQmlJSMetaPropertyBinding::objectType()
//      const
extern "C" Q_DECL_EXPORT
QSharedPointer<const QQmlJSScope> *ritual_ZNK25QQmlJSMetaPropertyBinding10objectTypeEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QSharedPointer<const QQmlJSScope>(self->objectType());
}

//  QString QQmlJSMetaPropertyBinding::interceptorTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlJSMetaPropertyBinding19interceptorTypeNameEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QString(self->interceptorTypeName());
}

//  QSharedPointer<const QQmlJSScope>
//      QQmlJSMetaPropertyBinding::interceptorType() const
extern "C" Q_DECL_EXPORT
QSharedPointer<const QQmlJSScope> *ritual_ZNK25QQmlJSMetaPropertyBinding15interceptorTypeEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QSharedPointer<const QQmlJSScope>(self->interceptorType());
}

//  QString QQmlJSMetaPropertyBinding::valueSourceTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlJSMetaPropertyBinding19valueSourceTypeNameEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QString(self->valueSourceTypeName());
}

//  QSharedPointer<const QQmlJSScope>
//      QQmlJSMetaPropertyBinding::valueSourceType() const
extern "C" Q_DECL_EXPORT
QSharedPointer<const QQmlJSScope> *ritual_ZNK25QQmlJSMetaPropertyBinding15valueSourceTypeEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QSharedPointer<const QQmlJSScope>(self->valueSourceType());
}

//  QSharedPointer<const QQmlJSScope> QQmlJSMetaPropertyBinding::groupType()
//      const
extern "C" Q_DECL_EXPORT
QSharedPointer<const QQmlJSScope> *ritual_ZNK25QQmlJSMetaPropertyBinding9groupTypeEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QSharedPointer<const QQmlJSScope>(self->groupType());
}

//  QSharedPointer<const QQmlJSScope>
//      QQmlJSMetaPropertyBinding::attachedType() const
extern "C" Q_DECL_EXPORT
QSharedPointer<const QQmlJSScope> *ritual_ZNK25QQmlJSMetaPropertyBinding12attachedTypeEv(
    const QQmlJSMetaPropertyBinding *self) {
  return new QSharedPointer<const QQmlJSScope>(self->attachedType());
}

//  bool QQmlJSMetaPropertyBinding::hasLiteral() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlJSMetaPropertyBinding10hasLiteralEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->hasLiteral();
}

//  bool QQmlJSMetaPropertyBinding::hasObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlJSMetaPropertyBinding9hasObjectEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->hasObject();
}

//  bool QQmlJSMetaPropertyBinding::hasInterceptor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlJSMetaPropertyBinding14hasInterceptorEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->hasInterceptor();
}

//  bool QQmlJSMetaPropertyBinding::hasValueSource() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlJSMetaPropertyBinding14hasValueSourceEv(
    const QQmlJSMetaPropertyBinding *self) {
  return self->hasValueSource();
}

//  bool operator==(const QQmlJSMetaPropertyBinding &a, const
//      QQmlJSMetaPropertyBinding &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK25QQmlJSMetaPropertyBindingS1_(
    const QQmlJSMetaPropertyBinding *a,
    const QQmlJSMetaPropertyBinding *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QQmlJSMetaPropertyBinding &a, const
//      QQmlJSMetaPropertyBinding &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK25QQmlJSMetaPropertyBindingS1_(
    const QQmlJSMetaPropertyBinding *a,
    const QQmlJSMetaPropertyBinding *b) {
  return operator!=(*a, *b);
}

//  QQmlJSMetaPropertyBinding::~QQmlJSMetaPropertyBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSMetaPropertyBindingD1Ev(
    QQmlJSMetaPropertyBinding *self) {
  delete self;
}

//  QList<QQmlJSMetaPropertyBinding>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaPropertyBinding> *ritual_list_make_QQmlJSMetaPropertyBinding() {
  return new QList<QQmlJSMetaPropertyBinding>();
}

//  void QList<QQmlJSMetaPropertyBinding>::append(const
//      QQmlJSMetaPropertyBinding &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlJSMetaPropertyBinding(
    QList<QQmlJSMetaPropertyBinding> *self,
    const QQmlJSMetaPropertyBinding *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlJSMetaPropertyBinding>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlJSMetaPropertyBinding(
    const QList<QQmlJSMetaPropertyBinding> *self) {
  return self->size();
}

//  const QQmlJSMetaPropertyBinding
//      &QList<QQmlJSMetaPropertyBinding>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaPropertyBinding *ritual_list_at_QQmlJSMetaPropertyBinding(
    const QList<QQmlJSMetaPropertyBinding> *self,
    long long index) {
  return new QQmlJSMetaPropertyBinding(self->at(index));
}

//  QList<QQmlJSMetaPropertyBinding>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlJSMetaPropertyBinding(
    QList<QQmlJSMetaPropertyBinding> *self) {
  delete self;
}

//  a QSharedPointer<const QQmlJSScope> a ritual of QQmlJSMetaPropertyBinding
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSMetaPropertyBinding__QSharedPointer_const_QQmlJSScope(
    QSharedPointer<const QQmlJSScope> *self) {
  delete self;
}
