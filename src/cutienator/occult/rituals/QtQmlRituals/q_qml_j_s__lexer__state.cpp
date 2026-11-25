//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qqmljslexer_p.h, Qt 6.12.0, as the Qt of
//  macOS and of Windows install it, and that of Linux alike. Kept as
//  it is when the generator runs again.
//  Its header pulls in 'private/qqmljsgrammar_p.h', which Qt makes as it
//  builds and an installed Qt has.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljslexer_p.h>
#include <QtCore/qdebug.h>

//  QQmlJS::Lexer::State::~State()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS5Lexer5StateD1Ev(QQmlJS::Lexer::State *self) {
  delete self;
}

//  bool operator==(State const &s1, State const &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJSeqERKNS_5Lexer5StateES3_(
    const QQmlJS::Lexer::State *s1,
    const QQmlJS::Lexer::State *s2) {
  return operator==(*s1, *s2);
}

//  bool operator!=(State const &s1, State const &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJSneERKNS_5Lexer5StateES3_(
    const QQmlJS::Lexer::State *s1,
    const QQmlJS::Lexer::State *s2) {
  return operator!=(*s1, *s2);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, State const &s)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QQmlJSlsE6QDebugRKNS_5Lexer5StateE(
    const QDebug *dbg,
    const QQmlJS::Lexer::State *s) {
  return new QDebug(operator<<(*dbg, *s));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
