//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QV4::Compiler::CodegenWarningInterface that Python can take functions over in. Every QV4::Compiler::CodegenWarningInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQV4_Compiler_CodegenWarningInterfaceCall0)(const void *, const QString *, const QString *, const QQmlJS::SourceLocation *, const QQmlJS::SourceLocation *, int *);
typedef void (*CuteQV4_Compiler_CodegenWarningInterfaceCall1)(const void *, const QString *, const QString *, const QQmlJS::SourceLocation *, const QQmlJS::SourceLocation *, int *);
typedef void * (*CuteQV4_Compiler_CodegenWarningInterfaceCall2)(const void *, int *);
class CuteQV4_Compiler_CodegenWarningInterface : public QV4::Compiler::CodegenWarningInterface {
public:
  using QV4::Compiler::CodegenWarningInterface::CodegenWarningInterface;
  CuteQV4_Compiler_CodegenWarningInterface(const QV4::Compiler::CodegenWarningInterface & other) : QV4::Compiler::CodegenWarningInterface(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV48Compiler23CodegenWarningInterface30reportVarUsedBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV48Compiler23CodegenWarningInterface35reportFunctionUsedBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV48Compiler23CodegenWarningInterface18unreachableVisitorEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QV4::Compiler::CodegenWarningInterface::reportVarUsedBeforeDecla
  //      ration(const QString &name, const QString &fileName,
  //      QQmlJS::SourceLocation declarationLocation,
  //      QQmlJS::SourceLocation accessLocation)
  void reportVarUsedBeforeDeclaration(
      const QString &name,
      const QString &fileName,
      QQmlJS::SourceLocation declarationLocation,
      QQmlJS::SourceLocation accessLocation) override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Compiler_CodegenWarningInterfaceCall0 call = reinterpret_cast<CuteQV4_Compiler_CodegenWarningInterfaceCall0>(taken[0]);
      call(this, &name, &fileName, &declarationLocation, &accessLocation, &handled);
      if (handled) return;
    }
    QV4::Compiler::CodegenWarningInterface::reportVarUsedBeforeDeclaration(name, fileName, declarationLocation, accessLocation);
  }

  //  void QV4::Compiler::CodegenWarningInterface::reportFunctionUsedBefore
  //      Declaration(const QString &name, const QString &fileName,
  //      QQmlJS::SourceLocation declarationLocation,
  //      QQmlJS::SourceLocation accessLocation)
  void reportFunctionUsedBeforeDeclaration(
      const QString &name,
      const QString &fileName,
      QQmlJS::SourceLocation declarationLocation,
      QQmlJS::SourceLocation accessLocation) override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Compiler_CodegenWarningInterfaceCall1 call = reinterpret_cast<CuteQV4_Compiler_CodegenWarningInterfaceCall1>(taken[1]);
      call(this, &name, &fileName, &declarationLocation, &accessLocation, &handled);
      if (handled) return;
    }
    QV4::Compiler::CodegenWarningInterface::reportFunctionUsedBeforeDeclaration(name, fileName, declarationLocation, accessLocation);
  }

  //  QQmlJS::AST::Visitor
  //      *QV4::Compiler::CodegenWarningInterface::unreachableVisitor()
  QQmlJS::AST::Visitor *unreachableVisitor() override {
    if (taken[2]) {
      int handled = 0;
      CuteQV4_Compiler_CodegenWarningInterfaceCall2 call = reinterpret_cast<CuteQV4_Compiler_CodegenWarningInterfaceCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Visitor *>(given);
    }
    return QV4::Compiler::CodegenWarningInterface::unreachableVisitor();
  }
};

//  void QV4::Compiler::CodegenWarningInterface::reportVarUsedBeforeDeclarati
//      on(const QString &name, const QString &fileName,
//      QQmlJS::SourceLocation declarationLocation, QQmlJS::SourceLocation
//      accessLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler23CodegenWarningInterface30reportVarUsedBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_(
    QV4::Compiler::CodegenWarningInterface *self,
    const QString *name,
    const QString *fileName,
    const QQmlJS::SourceLocation *declarationLocation,
    const QQmlJS::SourceLocation *accessLocation) {
  self->reportVarUsedBeforeDeclaration(
      *name,
      *fileName,
      *declarationLocation,
      *accessLocation);
}

//  void QV4::Compiler::CodegenWarningInterface::reportFunctionUsedBeforeDecl
//      aration(const QString &name, const QString &fileName,
//      QQmlJS::SourceLocation declarationLocation, QQmlJS::SourceLocation
//      accessLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler23CodegenWarningInterface35reportFunctionUsedBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_(
    QV4::Compiler::CodegenWarningInterface *self,
    const QString *name,
    const QString *fileName,
    const QQmlJS::SourceLocation *declarationLocation,
    const QQmlJS::SourceLocation *accessLocation) {
  self->reportFunctionUsedBeforeDeclaration(
      *name,
      *fileName,
      *declarationLocation,
      *accessLocation);
}

//  QQmlJS::AST::Visitor
//      *QV4::Compiler::CodegenWarningInterface::unreachableVisitor()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Visitor *ritual_ZN3QV48Compiler23CodegenWarningInterface18unreachableVisitorEv(
    QV4::Compiler::CodegenWarningInterface *self) {
  return self->unreachableVisitor();
}

//  QV4::Compiler::CodegenWarningInterface::~CodegenWarningInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler23CodegenWarningInterfaceD1Ev(
    QV4::Compiler::CodegenWarningInterface *self) {
  delete self;
}

//  a Python function taken by a CuteQV4_Compiler_CodegenWarningInterface,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Compiler_CodegenWarningInterface(
    QV4::Compiler::CodegenWarningInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Compiler_CodegenWarningInterface *>(self)->take(key, call);
}

//  void QV4::Compiler::CodegenWarningInterface::reportVarUsedBeforeDeclarati
//      on(const QString &name, const QString &fileName,
//      QQmlJS::SourceLocation declarationLocation, QQmlJS::SourceLocation
//      accessLocation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler23CodegenWarningInterface30reportVarUsedBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_(
    QV4::Compiler::CodegenWarningInterface *self,
    const QString *name,
    const QString *fileName,
    const QQmlJS::SourceLocation *declarationLocation,
    const QQmlJS::SourceLocation *accessLocation) {
  self->QV4::Compiler::CodegenWarningInterface::reportVarUsedBeforeDeclaration(
      *name,
      *fileName,
      *declarationLocation,
      *accessLocation);
}

//  void QV4::Compiler::CodegenWarningInterface::reportFunctionUsedBeforeDecl
//      aration(const QString &name, const QString &fileName,
//      QQmlJS::SourceLocation declarationLocation, QQmlJS::SourceLocation
//      accessLocation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler23CodegenWarningInterface35reportFunctionUsedBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_(
    QV4::Compiler::CodegenWarningInterface *self,
    const QString *name,
    const QString *fileName,
    const QQmlJS::SourceLocation *declarationLocation,
    const QQmlJS::SourceLocation *accessLocation) {
  self->QV4::Compiler::CodegenWarningInterface::reportFunctionUsedBeforeDeclaration(
      *name,
      *fileName,
      *declarationLocation,
      *accessLocation);
}

//  QQmlJS::AST::Visitor
//      *QV4::Compiler::CodegenWarningInterface::unreachableVisitor()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Visitor *ritual_own_ZN3QV48Compiler23CodegenWarningInterface18unreachableVisitorEv(
    QV4::Compiler::CodegenWarningInterface *self) {
  return self->QV4::Compiler::CodegenWarningInterface::unreachableVisitor();
}
