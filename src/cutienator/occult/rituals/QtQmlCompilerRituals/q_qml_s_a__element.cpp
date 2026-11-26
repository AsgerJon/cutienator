//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <QtCore/QList>
#include <QtCore/QString>

//  QQmlSA::Element::Element()
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZN6QQmlSA7ElementC1Ev() {
  return new QQmlSA::Element();
}

//  QQmlSA::Element::Element(const Element &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZN6QQmlSA7ElementC1ERKS0_(
    const QQmlSA::Element *a0) {
  return new QQmlSA::Element(*a0);
}

//  QQmlSA::Element::Element(Element &&other)
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZN6QQmlSA7ElementC1EOS0_(QQmlSA::Element *other) {
  return new QQmlSA::Element(std::move(*other));
}

//  Element &QQmlSA::Element::operator=(const Element &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZN6QQmlSA7ElementaSERKS0_(
    QQmlSA::Element *self,
    const QQmlSA::Element *a0) {
  return &(self->operator=(*a0));
}

//  Element &QQmlSA::Element::operator=(Element &&other)
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZN6QQmlSA7ElementaSEOS0_(
    QQmlSA::Element *self,
    QQmlSA::Element *other) {
  return &(self->operator=(std::move(*other)));
}

//  QQmlSA::Element::~Element()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA7ElementD1Ev(QQmlSA::Element *self) {
  delete self;
}

//  ScopeType QQmlSA::Element::scopeType() const
extern "C" Q_DECL_EXPORT
QQmlSA::ScopeType ritual_ZNK6QQmlSA7Element9scopeTypeEv(
    const QQmlSA::Element *self) {
  return self->scopeType();
}

//  Element QQmlSA::Element::baseType() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA7Element8baseTypeEv(
    const QQmlSA::Element *self) {
  return new QQmlSA::Element(self->baseType());
}

//  QString QQmlSA::Element::baseTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA7Element12baseTypeNameEv(
    const QQmlSA::Element *self) {
  return new QString(self->baseTypeName());
}

//  Element QQmlSA::Element::parentScope() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA7Element11parentScopeEv(
    const QQmlSA::Element *self) {
  return new QQmlSA::Element(self->parentScope());
}

//  bool QQmlSA::Element::inherits(const Element &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element8inheritsERKS0_(
    const QQmlSA::Element *self,
    const QQmlSA::Element *a0) {
  return self->inherits(*a0);
}

//  bool QQmlSA::Element::isFileRootComponent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element19isFileRootComponentEv(
    const QQmlSA::Element *self) {
  return self->isFileRootComponent();
}

//  bool QQmlSA::Element::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element6isNullEv(const QQmlSA::Element *self) {
  return self->isNull();
}

//  QString QQmlSA::Element::internalId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA7Element10internalIdEv(
    const QQmlSA::Element *self) {
  return new QString(self->internalId());
}

//  AccessSemantics QQmlSA::Element::accessSemantics() const
extern "C" Q_DECL_EXPORT
QQmlSA::AccessSemantics ritual_ZNK6QQmlSA7Element15accessSemanticsEv(
    const QQmlSA::Element *self) {
  return self->accessSemantics();
}

//  bool QQmlSA::Element::isComposite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element11isCompositeEv(const QQmlSA::Element *self) {
  return self->isComposite();
}

//  bool QQmlSA::Element::hasProperty(const QString &propertyName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element11hasPropertyERK7QString(
    const QQmlSA::Element *self,
    const QString *propertyName) {
  return self->hasProperty(*propertyName);
}

//  bool QQmlSA::Element::hasOwnProperty(const QString &propertyName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element14hasOwnPropertyERK7QString(
    const QQmlSA::Element *self,
    const QString *propertyName) {
  return self->hasOwnProperty(*propertyName);
}

//  Property QQmlSA::Element::property(const QString &propertyName) const
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZNK6QQmlSA7Element8propertyERK7QString(
    const QQmlSA::Element *self,
    const QString *propertyName) {
  return new QQmlSA::Property(self->property(*propertyName));
}

//  bool QQmlSA::Element::isPropertyRequired(const QString &propertyName)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element18isPropertyRequiredERK7QString(
    const QQmlSA::Element *self,
    const QString *propertyName) {
  return self->isPropertyRequired(*propertyName);
}

//  QString QQmlSA::Element::defaultPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA7Element19defaultPropertyNameEv(
    const QQmlSA::Element *self) {
  return new QString(self->defaultPropertyName());
}

//  bool QQmlSA::Element::hasMethod(const QString &methodName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element9hasMethodERK7QString(
    const QQmlSA::Element *self,
    const QString *methodName) {
  return self->hasMethod(*methodName);
}

//  Method::Methods QQmlSA::Element::ownMethods() const
extern "C" Q_DECL_EXPORT
QQmlSA::Method::Methods *ritual_ZNK6QQmlSA7Element10ownMethodsEv(
    const QQmlSA::Element *self) {
  return new QQmlSA::Method::Methods(self->ownMethods());
}

//  QQmlSA::SourceLocation QQmlSA::Element::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA7Element14sourceLocationEv(
    const QQmlSA::Element *self) {
  return new QQmlSA::SourceLocation(self->sourceLocation());
}

//  QQmlSA::SourceLocation QQmlSA::Element::idSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA7Element16idSourceLocationEv(
    const QQmlSA::Element *self) {
  return new QQmlSA::SourceLocation(self->idSourceLocation());
}

//  QString QQmlSA::Element::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA7Element8filePathEv(const QQmlSA::Element *self) {
  return new QString(self->filePath());
}

//  bool QQmlSA::Element::hasPropertyBindings(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element19hasPropertyBindingsERK7QString(
    const QQmlSA::Element *self,
    const QString *name) {
  return self->hasPropertyBindings(*name);
}

//  bool QQmlSA::Element::hasOwnPropertyBindings(const QString &propertyName)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Element22hasOwnPropertyBindingsERK7QString(
    const QQmlSA::Element *self,
    const QString *propertyName) {
  return self->hasOwnPropertyBindings(*propertyName);
}

//  Binding::Bindings QQmlSA::Element::ownPropertyBindings() const
extern "C" Q_DECL_EXPORT
QQmlSA::Binding::Bindings *ritual_ZNK6QQmlSA7Element19ownPropertyBindingsEv(
    const QQmlSA::Element *self) {
  return new QQmlSA::Binding::Bindings(self->ownPropertyBindings());
}

//  Binding::Bindings QQmlSA::Element::ownPropertyBindings(const QString
//      &propertyName) const
extern "C" Q_DECL_EXPORT
QQmlSA::Binding::Bindings *ritual_ZNK6QQmlSA7Element19ownPropertyBindingsERK7QString(
    const QQmlSA::Element *self,
    const QString *propertyName) {
  return new QQmlSA::Binding::Bindings(
      self->ownPropertyBindings(
          *propertyName));
}

//  QList<Binding> QQmlSA::Element::propertyBindings(const QString
//      &propertyName) const
extern "C" Q_DECL_EXPORT
QList<QQmlSA::Binding> *ritual_ZNK6QQmlSA7Element16propertyBindingsERK7QString(
    const QQmlSA::Element *self,
    const QString *propertyName) {
  return new QList<QQmlSA::Binding>(self->propertyBindings(*propertyName));
}

//  bool QQmlSA::Element::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7ElementcvbEv(const QQmlSA::Element *self) {
  return self->operator bool();
}

//  bool QQmlSA::Element::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7ElementntEv(const QQmlSA::Element *self) {
  return self->operator!();
}

//  QString QQmlSA::Element::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA7Element4nameEv(const QQmlSA::Element *self) {
  return new QString(self->name());
}

//  bool operator==(const QQmlSA::Element &lhs, const QQmlSA::Element &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_7ElementES2_(
    const QQmlSA::Element *lhs,
    const QQmlSA::Element *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Element &lhs, const Element &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_7ElementES2_(
    const QQmlSA::Element *lhs,
    const QQmlSA::Element *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QQmlSA::Element::operatorEqualsImpl(const Element &a0, const Element
//      &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA7Element18operatorEqualsImplERKS0_S2_(
    const QQmlSA::Element *a0,
    const QQmlSA::Element *a1) {
  return QQmlSA::Element::operatorEqualsImpl(*a0, *a1);
}

//  size_t QQmlSA::Element::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK6QQmlSA7Element4hashEm(
    const QQmlSA::Element *self,
    size_t seed) {
  return self->hash(seed);
}

//  void QQmlSA::Element::swap(Element &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA7Element4swapERS0_(
    QQmlSA::Element *self,
    QQmlSA::Element *other) {
  self->swap(*other);
}

//  a QList<QQmlSA::Binding> a ritual of QQmlSA::Element gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_Element__QList_QQmlSA_Binding(
    QList<QQmlSA::Binding> *self) {
  delete self;
}
