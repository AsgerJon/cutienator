//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsa.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <memory>
#include <QtCore/QAnyStringView>
#include <QtCore/QSet>
#include <QtCore/QString>

//  QQmlSA::PassManagerPrivate::PassManagerPrivate(QQmlJSImportVisitor
//      *visitor, QQmlJSTypeResolver *resolver)
extern "C" Q_DECL_EXPORT
QQmlSA::PassManagerPrivate *ritual_ZN6QQmlSA18PassManagerPrivateC1EP19QQmlJSImportVisitorP18QQmlJSTypeResolver(
    QQmlJSImportVisitor *visitor,
    QQmlJSTypeResolver *resolver) {
  return new QQmlSA::PassManagerPrivate(visitor, resolver);
}

//  PassManagerPrivate *QQmlSA::PassManagerPrivate::get(PassManager *manager)
extern "C" Q_DECL_EXPORT
QQmlSA::PassManagerPrivate *ritual_ZN6QQmlSA18PassManagerPrivate3getEPNS_11PassManagerE(
    QQmlSA::PassManager *manager) {
  return QQmlSA::PassManagerPrivate::get(manager);
}

//  const PassManagerPrivate *QQmlSA::PassManagerPrivate::get(const
//      PassManager *manager)
extern "C" Q_DECL_EXPORT
const QQmlSA::PassManagerPrivate *ritual_ZN6QQmlSA18PassManagerPrivate3getEPKNS_11PassManagerE(
    const QQmlSA::PassManager *manager) {
  return QQmlSA::PassManagerPrivate::get(manager);
}

//  PassManager
//      *QQmlSA::PassManagerPrivate::createPassManager(QQmlJSImportVisitor
//      *visitor, QQmlJSTypeResolver *resolver)
extern "C" Q_DECL_EXPORT
QQmlSA::PassManager *ritual_ZN6QQmlSA18PassManagerPrivate17createPassManagerEP19QQmlJSImportVisitorP18QQmlJSTypeResolver(
    QQmlJSImportVisitor *visitor,
    QQmlJSTypeResolver *resolver) {
  return QQmlSA::PassManagerPrivate::createPassManager(visitor, resolver);
}

//  void QQmlSA::PassManagerPrivate::deletePassManager(PassManager *q)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate17deletePassManagerEPNS_11PassManagerE(
    QQmlSA::PassManager *q) {
  QQmlSA::PassManagerPrivate::deletePassManager(q);
}

//  bool QQmlSA::PassManagerPrivate::registerPropertyPass(std::shared_ptr<Pro
//      pertyPass> pass, QAnyStringView moduleName, QAnyStringView typeName,
//      QAnyStringView propertyName, bool allowInheritance)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA18PassManagerPrivate20registerPropertyPassESt10shared_ptrINS_12PropertyPassEE14QAnyStringViewS4_S4_b(
    QQmlSA::PassManagerPrivate *self,
    const std::shared_ptr<QQmlSA::PropertyPass> *pass,
    const QString *moduleName,
    const QString *typeName,
    const QString *propertyName,
    bool allowInheritance) {
  return self->registerPropertyPass(
      *pass,
      QAnyStringView(*moduleName),
      QAnyStringView(*typeName),
      QAnyStringView(*propertyName),
      allowInheritance);
}

//  bool QQmlSA::PassManagerPrivate::registerPropertyPassOnBuiltinType(std::s
//      hared_ptr<PropertyPass> pass, QAnyStringView typeName, QAnyStringView
//      propertyName, bool allowInheritance)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA18PassManagerPrivate33registerPropertyPassOnBuiltinTypeESt10shared_ptrINS_12PropertyPassEE14QAnyStringViewS4_b(
    QQmlSA::PassManagerPrivate *self,
    const std::shared_ptr<QQmlSA::PropertyPass> *pass,
    const QString *typeName,
    const QString *propertyName,
    bool allowInheritance) {
  return self->registerPropertyPassOnBuiltinType(
      *pass,
      QAnyStringView(*typeName),
      QAnyStringView(*propertyName),
      allowInheritance);
}

//  void QQmlSA::PassManagerPrivate::analyze(const Element &root)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate7analyzeERKNS_7ElementE(
    QQmlSA::PassManagerPrivate *self,
    const QQmlSA::Element *root) {
  self->analyze(*root);
}

//  QQmlJSImportVisitor *QQmlSA::PassManagerPrivate::visitor(const
//      QQmlSA::PassManager &a0)
extern "C" Q_DECL_EXPORT
QQmlJSImportVisitor *ritual_ZN6QQmlSA18PassManagerPrivate7visitorERKNS_11PassManagerE(
    const QQmlSA::PassManager *a0) {
  return QQmlSA::PassManagerPrivate::visitor(*a0);
}

//  QQmlJSTypeResolver *QQmlSA::PassManagerPrivate::resolver(const
//      QQmlSA::PassManager &a0)
extern "C" Q_DECL_EXPORT
QQmlJSTypeResolver *ritual_ZN6QQmlSA18PassManagerPrivate8resolverERKNS_11PassManagerE(
    const QQmlSA::PassManager *a0) {
  return QQmlSA::PassManagerPrivate::resolver(*a0);
}

//  QSet<PropertyPass *>
//      QQmlSA::PassManagerPrivate::findPropertyUsePasses(const
//      QQmlSA::Element &element, const QString &propertyName)
extern "C" Q_DECL_EXPORT
QSet<QQmlSA::PropertyPass *> *ritual_ZN6QQmlSA18PassManagerPrivate21findPropertyUsePassesERKNS_7ElementERK7QString(
    QQmlSA::PassManagerPrivate *self,
    const QQmlSA::Element *element,
    const QString *propertyName) {
  return new QSet<QQmlSA::PropertyPass *>(
      self->findPropertyUsePasses(
          *element,
          *propertyName));
}

//  void QQmlSA::PassManagerPrivate::analyzeWrite(const QQmlSA::Element
//      &element, const QString &propertyName, const QQmlSA::Element &value,
//      const QQmlSA::Element &writeScope, const QQmlSA::SourceLocation
//      &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate12analyzeWriteERKNS_7ElementERK7QStringS3_S3_RKNS_14SourceLocationE(
    QQmlSA::PassManagerPrivate *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *value,
    const QQmlSA::Element *writeScope,
    const QQmlSA::SourceLocation *location) {
  self->analyzeWrite(
      *element,
      *propertyName,
      *value,
      *writeScope,
      *location);
}

//  void QQmlSA::PassManagerPrivate::analyzeRead(const QQmlSA::Element
//      &element, const QString &propertyName, const QQmlSA::Element
//      &readScope, const QQmlSA::SourceLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate11analyzeReadERKNS_7ElementERK7QStringS3_RKNS_14SourceLocationE(
    QQmlSA::PassManagerPrivate *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->analyzeRead(*element, *propertyName, *readScope, *location);
}

//  void QQmlSA::PassManagerPrivate::analyzeCall(const QQmlSA::Element
//      &element, const QString &propertyName, const QQmlSA::Element
//      &readScope, const QQmlSA::SourceLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate11analyzeCallERKNS_7ElementERK7QStringS3_RKNS_14SourceLocationE(
    QQmlSA::PassManagerPrivate *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->analyzeCall(*element, *propertyName, *readScope, *location);
}

//  void QQmlSA::PassManagerPrivate::analyzeBinding(const QQmlSA::Element
//      &element, const QQmlSA::Element &value, const QQmlSA::SourceLocation
//      &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate14analyzeBindingERKNS_7ElementES3_RKNS_14SourceLocationE(
    QQmlSA::PassManagerPrivate *self,
    const QQmlSA::Element *element,
    const QQmlSA::Element *value,
    const QQmlSA::SourceLocation *location) {
  self->analyzeBinding(*element, *value, *location);
}

//  void QQmlSA::PassManagerPrivate::addBindingSourceLocations(const
//      QQmlSA::Element &element, const QQmlSA::Element &scope, const QString
//      prefix, bool isAttached)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate25addBindingSourceLocationsERKNS_7ElementES3_7QStringb(
    QQmlSA::PassManagerPrivate *self,
    const QQmlSA::Element *element,
    const QQmlSA::Element *scope,
    const QString *prefix,
    bool isAttached) {
  self->addBindingSourceLocations(*element, *scope, *prefix, isAttached);
}

//  a QSet<QQmlSA::PropertyPass *> a ritual of QQmlSA::PassManagerPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_PassManagerPrivate__QSet_QQmlSA_PropertyPass(
    QSet<QQmlSA::PropertyPass *> *self) {
  delete self;
}
