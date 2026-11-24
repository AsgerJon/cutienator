//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::Pattern that Python can take functions over in. Every QQmlJS::AST::Pattern
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQmlJS_AST_PatternCall0)(const void *, int *);
typedef bool (*CuteQQmlJS_AST_PatternCall1)(const void *, QQmlJS::SourceLocation *, QString *, int *);
class CuteQQmlJS_AST_Pattern : public QQmlJS::AST::Pattern {
public:
  using QQmlJS::AST::Pattern::Pattern;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST7Pattern11patternCastEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST7Pattern33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  Pattern *QQmlJS::AST::Pattern::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternCall0 call = reinterpret_cast<CuteQQmlJS_AST_PatternCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Pattern::patternCast();
  }

  //  bool QQmlJS::AST::Pattern::convertLiteralToAssignmentPattern(SourceLo
  //      cation *errorLocation, QString *errorMessage)
  bool convertLiteralToAssignmentPattern(
      QQmlJS::SourceLocation *errorLocation,
      QString *errorMessage) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternCall1 call = reinterpret_cast<CuteQQmlJS_AST_PatternCall1>(taken[1]);
      bool given = call(this, errorLocation, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  bool
//      QQmlJS::AST::Pattern::convertLiteralToAssignmentPattern(SourceLocatio
//      n *errorLocation, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Pattern33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString(
    QQmlJS::AST::Pattern *self,
    QQmlJS::SourceLocation *errorLocation,
    QString *errorMessage) {
  return self->convertLiteralToAssignmentPattern(
      errorLocation,
      errorMessage);
}

//  a Python function taken by a CuteQQmlJS_AST_Pattern, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_Pattern(
    QQmlJS::AST::Pattern *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_Pattern *>(self)->take(key, call);
}

//  Pattern *QQmlJS::AST::Pattern::patternCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Pattern *ritual_own_ZN6QQmlJS3AST7Pattern11patternCastEv(
    QQmlJS::AST::Pattern *self) {
  return self->QQmlJS::AST::Pattern::patternCast();
}
