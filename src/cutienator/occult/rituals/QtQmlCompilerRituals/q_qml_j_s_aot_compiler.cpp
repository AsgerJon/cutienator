//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompiler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>
#include <variant>
#include <QtCore/QList>
#include <QtCore/QString>
#include <optional>

//  Only a class built on QQmlJSAotCompiler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlJSAotCompiler : QQmlJSAotCompiler {
  using QQmlJSAotCompiler::diagnose;
};

//  A QQmlJSAotCompiler that Python can take functions over in. Every QQmlJSAotCompiler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJSAotCompilerCall0)(const void *, const QmlIR::JSCodeGen *, const QmlIR::Document *, int *);
typedef void (*CuteQQmlJSAotCompilerCall1)(const void *, const QmlIR::Object *, const QmlIR::Object *, int *);
typedef const QQmlJSAotFunction * (*CuteQQmlJSAotCompilerCall2)(const void *, int *);
typedef const QQmlJS::DiagnosticMessage * (*CuteQQmlJSAotCompilerCall3)(const void *, const QString *, int, const QQmlJS::SourceLocation *, int *);
class CuteQQmlJSAotCompiler : public QQmlJSAotCompiler {
public:
  using QQmlJSAotCompiler::QQmlJSAotCompiler;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQmlJSAotCompiler11setDocumentEPKN5QmlIR9JSCodeGenEPKNS0_8DocumentE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlJSAotCompiler8setScopeEPKN5QmlIR6ObjectES3_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQmlJSAotCompiler10globalCodeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQmlJSAotCompiler8diagnoseERK7QString9QtMsgTypeRKN6QQmlJS14SourceLocationE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJSAotCompiler::setDocument(const QmlIR::JSCodeGen *codegen,
  //      const QmlIR::Document *document)
  void setDocument(
      const QmlIR::JSCodeGen *codegen,
      const QmlIR::Document *document) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSAotCompilerCall0 call = reinterpret_cast<CuteQQmlJSAotCompilerCall0>(taken[0]);
      call(this, codegen, document, &handled);
      if (handled) return;
    }
    QQmlJSAotCompiler::setDocument(codegen, document);
  }

  //  void QQmlJSAotCompiler::setScope(const QmlIR::Object *object, const
  //      QmlIR::Object *scope)
  void setScope(
      const QmlIR::Object *object,
      const QmlIR::Object *scope) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSAotCompilerCall1 call = reinterpret_cast<CuteQQmlJSAotCompilerCall1>(taken[1]);
      call(this, object, scope, &handled);
      if (handled) return;
    }
    QQmlJSAotCompiler::setScope(object, scope);
  }

  //  QQmlJSAotFunction QQmlJSAotCompiler::globalCode() const
  QQmlJSAotFunction globalCode() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSAotCompilerCall2 call = reinterpret_cast<CuteQQmlJSAotCompilerCall2>(taken[2]);
      const QQmlJSAotFunction * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJSAotCompiler::globalCode();
  }

  //  QQmlJS::DiagnosticMessage QQmlJSAotCompiler::diagnose(const QString
  //      &message, QtMsgType type, const QQmlJS::SourceLocation &location)
  //      const
  QQmlJS::DiagnosticMessage diagnose(
      const QString &message,
      QtMsgType type,
      const QQmlJS::SourceLocation &location) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSAotCompilerCall3 call = reinterpret_cast<CuteQQmlJSAotCompilerCall3>(taken[3]);
      const QQmlJS::DiagnosticMessage * given = call(this, &message, static_cast<int>(type), &location, &handled);
      if (handled && given) return *given;
    }
    return QQmlJSAotCompiler::diagnose(message, type, location);
  }
};

//  QQmlJSAotCompiler::QQmlJSAotCompiler(QQmlJSImporter *importer, const
//      QString &resourcePath, const QStringList &qmldirFiles, QQmlJSLogger
//      *logger)
extern "C" Q_DECL_EXPORT
QQmlJSAotCompiler *ritual_ZN17QQmlJSAotCompilerC1EP14QQmlJSImporterRK7QStringRK5QListIS2_EP12QQmlJSLogger(
    QQmlJSImporter *importer,
    const QString *resourcePath,
    const QList<QString> *qmldirFiles,
    QQmlJSLogger *logger) {
  return new CuteQQmlJSAotCompiler(
      importer,
      *resourcePath,
      *qmldirFiles,
      logger);
}

//  QQmlJSAotCompiler::~QQmlJSAotCompiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSAotCompilerD1Ev(QQmlJSAotCompiler *self) {
  delete self;
}

//  void QQmlJSAotCompiler::setDocument(const QmlIR::JSCodeGen *codegen,
//      const QmlIR::Document *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSAotCompiler11setDocumentEPKN5QmlIR9JSCodeGenEPKNS0_8DocumentE(
    QQmlJSAotCompiler *self,
    const QmlIR::JSCodeGen *codegen,
    const QmlIR::Document *document) {
  self->setDocument(codegen, document);
}

//  void QQmlJSAotCompiler::setScope(const QmlIR::Object *object, const
//      QmlIR::Object *scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSAotCompiler8setScopeEPKN5QmlIR6ObjectES3_(
    QQmlJSAotCompiler *self,
    const QmlIR::Object *object,
    const QmlIR::Object *scope) {
  self->setScope(object, scope);
}

//  std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>
//      QQmlJSAotCompiler::compileBinding(const QV4::Compiler::Context
//      *context, const QmlIR::Binding &irBinding, QQmlJS::AST::Node
//      *astNode)
extern "C" Q_DECL_EXPORT
std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>> *ritual_ZN17QQmlJSAotCompiler14compileBindingEPKN3QV48Compiler7ContextERKN5QmlIR7BindingEPN6QQmlJS3AST4NodeE(
    QQmlJSAotCompiler *self,
    const QV4::Compiler::Context *context,
    const QmlIR::Binding *irBinding,
    QQmlJS::AST::Node *astNode) {
  return new std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>(
      self->compileBinding(
          context,
          *irBinding,
          astNode));
}

//  std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>
//      QQmlJSAotCompiler::compileFunction(const QV4::Compiler::Context
//      *context, const QString &name, QQmlJS::AST::Node *astNode)
extern "C" Q_DECL_EXPORT
std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>> *ritual_ZN17QQmlJSAotCompiler15compileFunctionEPKN3QV48Compiler7ContextERK7QStringPN6QQmlJS3AST4NodeE(
    QQmlJSAotCompiler *self,
    const QV4::Compiler::Context *context,
    const QString *name,
    QQmlJS::AST::Node *astNode) {
  return new std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>(
      self->compileFunction(
          context,
          *name,
          astNode));
}

//  QQmlJSAotFunction QQmlJSAotCompiler::globalCode() const
extern "C" Q_DECL_EXPORT
QQmlJSAotFunction *ritual_ZNK17QQmlJSAotCompiler10globalCodeEv(
    const QQmlJSAotCompiler *self) {
  return new QQmlJSAotFunction(self->globalCode());
}

//  LookupSignatures QQmlJSAotCompiler::lookupSignatures() const
extern "C" Q_DECL_EXPORT
LookupSignatures *ritual_ZNK17QQmlJSAotCompiler16lookupSignaturesEv(
    const QQmlJSAotCompiler *self) {
  return new LookupSignatures(self->lookupSignatures());
}

//  bool QQmlJSAotCompiler::isLintCompiler() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSAotCompiler14isLintCompilerEv(
    const QQmlJSAotCompiler *self) {
  return self->isLintCompiler();
}

//  bool QQmlJSAotCompiler::noAotValidation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSAotCompiler15noAotValidationEv(
    const QQmlJSAotCompiler *self) {
  return self->noAotValidation();
}

//  std::optional<QList<QQmlJS::DiagnosticMessage>>
//      QQmlJSAotCompiler::finalizeBindingOrFunction()
extern "C" Q_DECL_EXPORT
std::optional<QList<QQmlJS::DiagnosticMessage>> *ritual_ZN17QQmlJSAotCompiler25finalizeBindingOrFunctionEv(
    QQmlJSAotCompiler *self) {
  return new std::optional<QList<QQmlJS::DiagnosticMessage>>(
      self->finalizeBindingOrFunction());
}

//  QQmlJS::DiagnosticMessage QQmlJSAotCompiler::diagnose(const QString
//      &message, QtMsgType type, const QQmlJS::SourceLocation &location)
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::DiagnosticMessage *ritual_ZNK17QQmlJSAotCompiler8diagnoseERK7QString9QtMsgTypeRKN6QQmlJS14SourceLocationE(
    const QQmlJSAotCompiler *self,
    const QString *message,
    QtMsgType type,
    const QQmlJS::SourceLocation *location) {
  return new QQmlJS::DiagnosticMessage(
      self->diagnose(
          *message,
          type,
          *location));
}

//  QQmlJSAotFunction QQmlJSAotCompiler::doCompile(const
//      QV4::Compiler::Context *context, const QQmlJSCompilePass::Function
//      *function)
extern "C" Q_DECL_EXPORT
QQmlJSAotFunction *ritual_ZN17QQmlJSAotCompiler9doCompileEPKN3QV48Compiler7ContextEPKN17QQmlJSCompilePass8FunctionE(
    QQmlJSAotCompiler *self,
    const QV4::Compiler::Context *context,
    const QQmlJSCompilePass::Function *function) {
  return new QQmlJSAotFunction(self->doCompile(context, function));
}

//  QQmlJSAotFunction QQmlJSAotCompiler::doCompileAndRecordAotStats(const
//      QV4::Compiler::Context *context, const QQmlJSCompilePass::Function
//      *function, const QString &name, QQmlJS::SourceLocation location)
extern "C" Q_DECL_EXPORT
QQmlJSAotFunction *ritual_ZN17QQmlJSAotCompiler26doCompileAndRecordAotStatsEPKN3QV48Compiler7ContextEPKN17QQmlJSCompilePass8FunctionERK7QStringN6QQmlJS14SourceLocationE(
    QQmlJSAotCompiler *self,
    const QV4::Compiler::Context *context,
    const QQmlJSCompilePass::Function *function,
    const QString *name,
    const QQmlJS::SourceLocation *location) {
  return new QQmlJSAotFunction(
      self->doCompileAndRecordAotStats(
          context,
          function,
          *name,
          *location));
}

//  a Python function taken by a CuteQQmlJSAotCompiler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSAotCompiler(
    QQmlJSAotCompiler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSAotCompiler *>(self)->take(key, call);
}

//  void QQmlJSAotCompiler::setDocument(const QmlIR::JSCodeGen *codegen,
//      const QmlIR::Document *document)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSAotCompiler11setDocumentEPKN5QmlIR9JSCodeGenEPKNS0_8DocumentE(
    QQmlJSAotCompiler *self,
    const QmlIR::JSCodeGen *codegen,
    const QmlIR::Document *document) {
  self->QQmlJSAotCompiler::setDocument(codegen, document);
}

//  void QQmlJSAotCompiler::setScope(const QmlIR::Object *object, const
//      QmlIR::Object *scope)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSAotCompiler8setScopeEPKN5QmlIR6ObjectES3_(
    QQmlJSAotCompiler *self,
    const QmlIR::Object *object,
    const QmlIR::Object *scope) {
  self->QQmlJSAotCompiler::setScope(object, scope);
}

//  QQmlJSAotFunction QQmlJSAotCompiler::globalCode() const
extern "C" Q_DECL_EXPORT
QQmlJSAotFunction *ritual_own_ZNK17QQmlJSAotCompiler10globalCodeEv(
    const QQmlJSAotCompiler *self) {
  return new QQmlJSAotFunction(self->QQmlJSAotCompiler::globalCode());
}

//  QQmlJS::DiagnosticMessage QQmlJSAotCompiler::diagnose(const QString
//      &message, QtMsgType type, const QQmlJS::SourceLocation &location)
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::DiagnosticMessage *ritual_own_ZNK17QQmlJSAotCompiler8diagnoseERK7QString9QtMsgTypeRKN6QQmlJS14SourceLocationE(
    const QQmlJSAotCompiler *self,
    const QString *message,
    QtMsgType type,
    const QQmlJS::SourceLocation *location) {
  return new QQmlJS::DiagnosticMessage(
      static_cast<const OwnQQmlJSAotCompiler *>(self)->OwnQQmlJSAotCompiler::diagnose(
          *message,
          type,
          *location));
}

//  a std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>> a
//      ritual of QQmlJSAotCompiler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSAotCompiler__std_variant_QQmlJSAotFunction_QList_QQmlJS_DiagnosticMessage(
    std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>> *self) {
  delete self;
}

//  a LookupSignatures a ritual of QQmlJSAotCompiler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSAotCompiler__LookupSignatures(
    LookupSignatures *self) {
  delete self;
}

//  a std::optional<QList<QQmlJS::DiagnosticMessage>> a ritual of
//      QQmlJSAotCompiler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSAotCompiler__std_optional_QList_QQmlJS_DiagnosticMessage(
    std::optional<QList<QQmlJS::DiagnosticMessage>> *self) {
  delete self;
}
