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
#include <QtCore/QSharedPointer>

//  QQmlJSMetaProperty::QQmlJSMetaProperty()
extern "C" Q_DECL_EXPORT
QQmlJSMetaProperty *ritual_ZN18QQmlJSMetaPropertyC1Ev() {
  return new QQmlJSMetaProperty();
}

//  void QQmlJSMetaProperty::setPropertyName(const QString &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty15setPropertyNameERK7QString(
    QQmlJSMetaProperty *self,
    const QString *propertyName) {
  self->setPropertyName(*propertyName);
}

//  QString QQmlJSMetaProperty::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty12propertyNameEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->propertyName());
}

//  void QQmlJSMetaProperty::setTypeName(const QString &typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty11setTypeNameERK7QString(
    QQmlJSMetaProperty *self,
    const QString *typeName) {
  self->setTypeName(*typeName);
}

//  QString QQmlJSMetaProperty::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty8typeNameEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->typeName());
}

//  void QQmlJSMetaProperty::setRead(const QString &read)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty7setReadERK7QString(
    QQmlJSMetaProperty *self,
    const QString *read) {
  self->setRead(*read);
}

//  QString QQmlJSMetaProperty::read() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty4readEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->read());
}

//  void QQmlJSMetaProperty::setWrite(const QString &write)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty8setWriteERK7QString(
    QQmlJSMetaProperty *self,
    const QString *write) {
  self->setWrite(*write);
}

//  QString QQmlJSMetaProperty::write() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty5writeEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->write());
}

//  void QQmlJSMetaProperty::setReset(const QString &reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty8setResetERK7QString(
    QQmlJSMetaProperty *self,
    const QString *reset) {
  self->setReset(*reset);
}

//  QString QQmlJSMetaProperty::reset() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty5resetEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->reset());
}

//  void QQmlJSMetaProperty::setBindable(const QString &bindable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty11setBindableERK7QString(
    QQmlJSMetaProperty *self,
    const QString *bindable) {
  self->setBindable(*bindable);
}

//  QString QQmlJSMetaProperty::bindable() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty8bindableEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->bindable());
}

//  void QQmlJSMetaProperty::setNotify(const QString &notify)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty9setNotifyERK7QString(
    QQmlJSMetaProperty *self,
    const QString *notify) {
  self->setNotify(*notify);
}

//  QString QQmlJSMetaProperty::notify() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty6notifyEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->notify());
}

//  void QQmlJSMetaProperty::setPrivateClass(const QString &privateClass)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty15setPrivateClassERK7QString(
    QQmlJSMetaProperty *self,
    const QString *privateClass) {
  self->setPrivateClass(*privateClass);
}

//  QString QQmlJSMetaProperty::privateClass() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty12privateClassEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->privateClass());
}

//  bool QQmlJSMetaProperty::isPrivate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty9isPrivateEv(
    const QQmlJSMetaProperty *self) {
  return self->isPrivate();
}

//  void QQmlJSMetaProperty::setType(const QDeferredSharedPointer<const
//      QQmlJSScope> &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty7setTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSMetaProperty *self,
    const QDeferredSharedPointer<const QQmlJSScope> *type) {
  self->setType(*type);
}

//  QDeferredSharedPointer<const QQmlJSScope> QQmlJSMetaProperty::type()
//      const
extern "C" Q_DECL_EXPORT
QDeferredSharedPointer<const QQmlJSScope> *ritual_ZNK18QQmlJSMetaProperty4typeEv(
    const QQmlJSMetaProperty *self) {
  return new QDeferredSharedPointer<const QQmlJSScope>(self->type());
}

//  void QQmlJSMetaProperty::setSourceLocation(const QQmlJS::SourceLocation
//      &newSourceLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty17setSourceLocationERKN6QQmlJS14SourceLocationE(
    QQmlJSMetaProperty *self,
    const QQmlJS::SourceLocation *newSourceLocation) {
  self->setSourceLocation(*newSourceLocation);
}

//  QQmlJS::SourceLocation QQmlJSMetaProperty::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK18QQmlJSMetaProperty14sourceLocationEv(
    const QQmlJSMetaProperty *self) {
  return new QQmlJS::SourceLocation(self->sourceLocation());
}

//  void QQmlJSMetaProperty::setAnnotations(const QList<QQmlJSAnnotation>
//      &annotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty14setAnnotationsERK5QListI16QQmlJSAnnotationE(
    QQmlJSMetaProperty *self,
    const QList<QQmlJSAnnotation> *annotation) {
  self->setAnnotations(*annotation);
}

//  const QList<QQmlJSAnnotation> &QQmlJSMetaProperty::annotations() const
extern "C" Q_DECL_EXPORT
QList<QQmlJSAnnotation> *ritual_ZNK18QQmlJSMetaProperty11annotationsEv(
    const QQmlJSMetaProperty *self) {
  return new QList<QQmlJSAnnotation>(self->annotations());
}

//  void QQmlJSMetaProperty::setIsList(bool isList)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty9setIsListEb(
    QQmlJSMetaProperty *self,
    bool isList) {
  self->setIsList(isList);
}

//  bool QQmlJSMetaProperty::isList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty6isListEv(
    const QQmlJSMetaProperty *self) {
  return self->isList();
}

//  void QQmlJSMetaProperty::setIsWritable(bool isWritable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty13setIsWritableEb(
    QQmlJSMetaProperty *self,
    bool isWritable) {
  self->setIsWritable(isWritable);
}

//  bool QQmlJSMetaProperty::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty10isWritableEv(
    const QQmlJSMetaProperty *self) {
  return self->isWritable();
}

//  void QQmlJSMetaProperty::setIsPointer(bool isPointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty12setIsPointerEb(
    QQmlJSMetaProperty *self,
    bool isPointer) {
  self->setIsPointer(isPointer);
}

//  bool QQmlJSMetaProperty::isPointer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty9isPointerEv(
    const QQmlJSMetaProperty *self) {
  return self->isPointer();
}

//  void QQmlJSMetaProperty::setIsTypeConstant(bool isTypeConstant)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty17setIsTypeConstantEb(
    QQmlJSMetaProperty *self,
    bool isTypeConstant) {
  self->setIsTypeConstant(isTypeConstant);
}

//  bool QQmlJSMetaProperty::isTypeConstant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty14isTypeConstantEv(
    const QQmlJSMetaProperty *self) {
  return self->isTypeConstant();
}

//  void QQmlJSMetaProperty::setAliasExpression(const QString &aliasString)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty18setAliasExpressionERK7QString(
    QQmlJSMetaProperty *self,
    const QString *aliasString) {
  self->setAliasExpression(*aliasString);
}

//  QString QQmlJSMetaProperty::aliasExpression() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty15aliasExpressionEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->aliasExpression());
}

//  bool QQmlJSMetaProperty::isAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty7isAliasEv(
    const QQmlJSMetaProperty *self) {
  return self->isAlias();
}

//  void QQmlJSMetaProperty::setAliasTargetName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty18setAliasTargetNameERK7QString(
    QQmlJSMetaProperty *self,
    const QString *name) {
  self->setAliasTargetName(*name);
}

//  QString QQmlJSMetaProperty::aliasTargetName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSMetaProperty15aliasTargetNameEv(
    const QQmlJSMetaProperty *self) {
  return new QString(self->aliasTargetName());
}

//  void QQmlJSMetaProperty::setAliasTargetScope(const QSharedPointer<const
//      QQmlJSScope> &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty19setAliasTargetScopeERK14QSharedPointerIK11QQmlJSScopeE(
    QQmlJSMetaProperty *self,
    const QSharedPointer<const QQmlJSScope> *scope) {
  self->setAliasTargetScope(*scope);
}

//  QSharedPointer<const QQmlJSScope> QQmlJSMetaProperty::aliasTargetScope()
//      const
extern "C" Q_DECL_EXPORT
QSharedPointer<const QQmlJSScope> *ritual_ZNK18QQmlJSMetaProperty16aliasTargetScopeEv(
    const QQmlJSMetaProperty *self) {
  return new QSharedPointer<const QQmlJSScope>(self->aliasTargetScope());
}

//  void QQmlJSMetaProperty::setIsFinal(bool isFinal)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty10setIsFinalEb(
    QQmlJSMetaProperty *self,
    bool isFinal) {
  self->setIsFinal(isFinal);
}

//  bool QQmlJSMetaProperty::isFinal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty7isFinalEv(
    const QQmlJSMetaProperty *self) {
  return self->isFinal();
}

//  void QQmlJSMetaProperty::setIsOverride(bool isOverride)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty13setIsOverrideEb(
    QQmlJSMetaProperty *self,
    bool isOverride) {
  self->setIsOverride(isOverride);
}

//  bool QQmlJSMetaProperty::isOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty10isOverrideEv(
    const QQmlJSMetaProperty *self) {
  return self->isOverride();
}

//  void QQmlJSMetaProperty::setIsVirtual(bool isVirtual)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty12setIsVirtualEb(
    QQmlJSMetaProperty *self,
    bool isVirtual) {
  self->setIsVirtual(isVirtual);
}

//  bool QQmlJSMetaProperty::isVirtual() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty9isVirtualEv(
    const QQmlJSMetaProperty *self) {
  return self->isVirtual();
}

//  void QQmlJSMetaProperty::setIsPropertyConstant(bool isPropertyConstant)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty21setIsPropertyConstantEb(
    QQmlJSMetaProperty *self,
    bool isPropertyConstant) {
  self->setIsPropertyConstant(isPropertyConstant);
}

//  bool QQmlJSMetaProperty::isPropertyConstant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty18isPropertyConstantEv(
    const QQmlJSMetaProperty *self) {
  return self->isPropertyConstant();
}

//  void QQmlJSMetaProperty::setRevision(int revision)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty11setRevisionEi(
    QQmlJSMetaProperty *self,
    int revision) {
  self->setRevision(revision);
}

//  int QQmlJSMetaProperty::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlJSMetaProperty8revisionEv(
    const QQmlJSMetaProperty *self) {
  return self->revision();
}

//  void QQmlJSMetaProperty::setIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaProperty8setIndexEi(
    QQmlJSMetaProperty *self,
    int index) {
  self->setIndex(index);
}

//  int QQmlJSMetaProperty::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlJSMetaProperty5indexEv(const QQmlJSMetaProperty *self) {
  return self->index();
}

//  bool QQmlJSMetaProperty::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSMetaProperty7isValidEv(
    const QQmlJSMetaProperty *self) {
  return self->isValid();
}

//  bool operator==(const QQmlJSMetaProperty &a, const QQmlJSMetaProperty &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QQmlJSMetaPropertyS1_(
    const QQmlJSMetaProperty *a,
    const QQmlJSMetaProperty *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QQmlJSMetaProperty &a, const QQmlJSMetaProperty &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QQmlJSMetaPropertyS1_(
    const QQmlJSMetaProperty *a,
    const QQmlJSMetaProperty *b) {
  return operator!=(*a, *b);
}

//  QQmlJSMetaProperty::~QQmlJSMetaProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSMetaPropertyD1Ev(QQmlJSMetaProperty *self) {
  delete self;
}

//  QHash<QString, QQmlJSMetaProperty>: QHash<QString, QQmlJSMetaProperty>()
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaProperty> *ritual_map_make_QHash_QString_QQmlJSMetaProperty() {
  return new QHash<QString, QQmlJSMetaProperty>();
}

//  QHash<QString, QQmlJSMetaProperty>: insert(const Key &key, const T
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_QString_QQmlJSMetaProperty(
    QHash<QString, QQmlJSMetaProperty> *self,
    const QString *key,
    const QQmlJSMetaProperty *value) {
  self->insert(*key, *value);
}

//  QHash<QString, QQmlJSMetaProperty>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_QString_QQmlJSMetaProperty(
    const QHash<QString, QQmlJSMetaProperty> *self) {
  return self->size();
}

//  QHash<QString, QQmlJSMetaProperty>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QHash_QString_QQmlJSMetaProperty(
    const QHash<QString, QQmlJSMetaProperty> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QHash<QString, QQmlJSMetaProperty>: the value at a place
extern "C" Q_DECL_EXPORT
QQmlJSMetaProperty *ritual_map_value_QHash_QString_QQmlJSMetaProperty(
    const QHash<QString, QQmlJSMetaProperty> *self,
    long long index) {
  return new QQmlJSMetaProperty(*std::next(self->constBegin(), index));
}

//  QHash<QString, QQmlJSMetaProperty>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_QString_QQmlJSMetaProperty(
    const QHash<QString, QQmlJSMetaProperty> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QHash<QString, QQmlJSMetaProperty>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaProperty *ritual_map_get_QHash_QString_QQmlJSMetaProperty(
    const QHash<QString, QQmlJSMetaProperty> *self,
    const QString *key) {
  return new QQmlJSMetaProperty(self->value(*key));
}

//  QHash<QString, QQmlJSMetaProperty>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_QString_QQmlJSMetaProperty(
    QHash<QString, QQmlJSMetaProperty> *self) {
  delete self;
}

//  a QDeferredSharedPointer<const QQmlJSScope> a ritual of
//      QQmlJSMetaProperty gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSMetaProperty__QDeferredSharedPointer_const_QQmlJSScope(
    QDeferredSharedPointer<const QQmlJSScope> *self) {
  delete self;
}

//  a QSharedPointer<const QQmlJSScope> a ritual of QQmlJSMetaProperty gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSMetaProperty__QSharedPointer_const_QQmlJSScope(
    QSharedPointer<const QQmlJSScope> *self) {
  delete self;
}
